"""Frozen seed-A calibration, seed-C evaluation, ranking and queue analysis."""
import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd

from src.evaluate import (CLASSES, FAMILIES, GRID, clustered_metrics, prepare,
                          rates)
from src.generate import DECOYS


def json_safe(value):
    """Use JSON null for undefined subgroup metrics, never non-standard NaN."""
    if isinstance(value, dict):
        return {str(key): json_safe(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [json_safe(item) for item in value]
    if isinstance(value, (float, np.floating)):
        return float(value) if np.isfinite(value) else None
    if isinstance(value, np.integer):
        return int(value)
    return value


def choose_threshold(train_truth, train_matrix):
    rows = []
    for threshold in GRID:
        item = rates(train_truth.is_cheat, (train_matrix.to_numpy() > threshold).sum(axis=1) >= 2)
        item.update(threshold=threshold, balanced_error=((1-item['recall'])+item['fpr'])/2)
        rows.append(item)
    return min(rows, key=lambda x: (x['balanced_error'], -x['threshold']))['threshold'], rows


def monthly_frame(truth, matrix, features, threshold):
    out = truth.reset_index().copy()
    values = matrix.to_numpy()
    out['signals'] = (values > threshold).sum(axis=1)
    # This is the unchanged, evidence-only monthly decision rule.
    out['flagged'] = out.signals >= 2
    out['weakest_link_normalised_gap'] = [min(row[row > threshold]) if any(row > threshold) else 0 for row in values]
    fired = features[features.severity > threshold].copy()
    fired['source_family'] = fired.source_family.astype(str)
    families = fired.groupby(['factory_id', 'period_month']).source_family.agg(lambda v: '+'.join(sorted(set(v)))).rename('families_firing')
    gaps = (features.assign(value_at_risk=np.where(
        features.check_family.str.startswith('bank_'), features.gap.abs(), features.gap.abs()*120))
        .groupby(['factory_id','period_month']).value_at_risk.max())
    out = out.join(families, on=['factory_id','period_month']).join(gaps, on=['factory_id','period_month'])
    out['families_firing'] = out.families_firing.fillna('none')
    out['value_at_risk'] = out.value_at_risk.fillna(0.0)
    return out, fired


def ordered_queue(frame, keys):
    ascending = [False if key != 'factory_id' else True for key in keys]
    return frame[frame.flagged].sort_values(keys, ascending=ascending, kind='mergesort')


def precision_at_k(frame, k, keys):
    snapshots = []
    for month, group in frame.groupby('period_month'):
        top = ordered_queue(group, keys).head(k)
        snapshots.append({'month':month, 'returned':len(top), 'true_cheats':int(top.is_cheat.sum()),
                          'precision':float(top.is_cheat.mean()) if len(top) else None})
    usable = [x['precision'] for x in snapshots if x['precision'] is not None]
    return {'macro_precision':float(np.mean(usable)) if usable else None,
            'monthly_queues':snapshots,
            'definition':'up to k prioritised factory-months per monthly snapshot; no cleared rows are padded'}


def factory_queue(frame, k):
    group = frame.groupby('factory_id').agg(
        is_cheat=('is_cheat','max'), scenario=('scenario','first'),
        intensity=('intensity','first'), evasive=('evasive','first'),
        prioritised_months=('flagged','sum'), value_at_risk=('value_at_risk','sum'))
    group['flagged'] = group.prioritised_months >= k
    return group.reset_index()


def calibration_queue(frame):
    choices = []
    for k in (2, 3, 4):
        q = factory_queue(frame, k)
        metric = rates(q.is_cheat, q.flagged)
        choices.append({'k':k, **metric,
                        'queue_size':int(q.flagged.sum()),
                        'balanced_error':((1-metric['recall'])+metric['fpr'])/2})
    # Safety first when calibration is tied: require more corroborated months.
    return min(choices, key=lambda x: (x['balanced_error'], -x['k']))['k'], choices


def class_confusion(frame, fired):
    pick = fired.copy()
    pick['financial'] = pick.check_family.str.startswith('bank_').astype(int)
    pick = pick.sort_values(['factory_id','period_month','financial','severity'], ascending=[True,True,True,False])
    pick = pick.drop_duplicates(['factory_id','period_month'])
    joined = frame.merge(pick[['factory_id','period_month','discrepancy_class']], how='left',
                         on=['factory_id','period_month'], suffixes=('_truth','_pred'))
    matrix = pd.crosstab(joined.discrepancy_class_truth,
                         joined.discrepancy_class_pred.fillna('no signal')).reindex(
                             index=CLASSES, columns=CLASSES+['no signal'], fill_value=0)
    return {'unit':'factory-month; strongest non-financial evidence, including review-only cases; clean months excluded',
            'rows_truth':CLASSES,'columns_predicted':CLASSES+['no signal'],'counts':matrix.to_numpy().tolist()}


def check_metrics(frame, features, threshold):
    """Detection rate of each individual SQL check before family combination."""
    labels = frame[['factory_id','period_month','is_cheat']]
    joined = features.merge(labels, on=['factory_id','period_month'], validate='many_to_one')
    result = {}
    for check, group in joined.groupby('check_family'):
        group = group.copy()
        group['flagged'] = group.severity > threshold
        result[check] = clustered_metrics(group)
    return result


def evaluate(train_dir, test_dir, v1_path='results.json', output='results.json', reports_dir='reports'):
    reports = Path(reports_dir)
    reports.mkdir(parents=True, exist_ok=True)
    train, train_matrix, _ = prepare(train_dir)
    threshold, calibration = choose_threshold(train, train_matrix)
    a_frame, _ = monthly_frame(train, train_matrix, prepare(train_dir)[2], threshold)
    queue_k, queue_calibration = calibration_queue(a_frame)
    ranking_keys = ['signals','weakest_link_normalised_gap','value_at_risk','factory_id']
    sort_tests = {}
    for name, keys in {
        'families_only':['signals','factory_id'],
        'families_then_weakest_link':['signals','weakest_link_normalised_gap','factory_id'],
        'families_then_weakest_link_then_value_at_risk':ranking_keys,
    }.items():
        sort_tests[name] = precision_at_k(a_frame, 50, keys)

    truth, matrix, features = prepare(test_dir)
    frame, fired = monthly_frame(truth, matrix, features, threshold)
    fac = factory_queue(frame, queue_k)
    monthly_metrics = clustered_metrics(frame)
    factory_metrics = clustered_metrics(fac)
    by_type = {}
    for level, data in [('factory_month',frame),('factory',fac)]:
        by_type[level] = {f'{s}/{i:.0%}':clustered_metrics(g)
            for (s,i),g in data[data.is_cheat==1].groupby(['scenario','intensity'])}
    fpr_by_decoy = {level:{s:clustered_metrics(g) for s,g in data[(data.is_cheat==0)&data.scenario.isin(DECOYS)].groupby('scenario')}
                    for level,data in [('factory_month',frame),('factory',fac)]}
    fpr_clean_decoy = {}
    for label, data in [('factory_month',frame),('factory',fac)]:
        fpr_clean_decoy[label] = {
          'clean_factories':clustered_metrics(data[(data.is_cheat==0)&(data.scenario=='honest')]),
          'honest_decoys':clustered_metrics(data[(data.is_cheat==0)&data.scenario.isin(DECOYS)])}
    false_pairs = frame[(frame.is_cheat==0)&frame.scenario.isin(DECOYS)].copy()
    false_pairs['signal_pair'] = false_pairs.families_firing
    decoy_pairs = false_pairs.groupby(['scenario','signal_pair']).agg(
        months=('flagged','size'), false_positives=('flagged','sum')).reset_index()
    decoy_pairs['fpr'] = decoy_pairs.false_positives / decoy_pairs.months
    at_k = {str(k):precision_at_k(frame,k,ranking_keys) for k in (50,200)}
    misses = frame[(frame.is_cheat==1)&~frame.flagged].copy()
    misses['reason'] = np.where(misses.signals==0, 'all independent source ratios below threshold',
                                'only one independent source family exceeded threshold')
    observed_prev = float(frame.is_cheat.mean())
    prevalence = {}
    for p in (.01,.05,.10,observed_prev):
        sensitivity, fpr = monthly_metrics['recall'], monthly_metrics['fpr']
        prevalence[f'{p:.2%}' if p != observed_prev else 'synthetic observed'] = {
            'assumed_prevalence':p,
            'precision':sensitivity*p/(sensitivity*p + fpr*(1-p)) if sensitivity*p + fpr*(1-p) else None}

    v1 = json.loads(Path(v1_path).read_text()) if Path(v1_path).exists() else {}
    result = {
      'protocol': {'train_seed':json.loads((Path(train_dir)/'manifest.json').read_text())['seed'],
        'held_out_seed':json.loads((Path(test_dir)/'manifest.json').read_text())['seed'],
        'evaluation_version':'v2', 'months_per_factory':12, 'threshold':threshold,
        'objective':'minimum factory-month balanced error on seed A; larger threshold on ties; K selected on seed A only',
        'calibration':calibration, 'bootstrap':'1000 factory-cluster resamples; percentile 95% intervals, seed 721; conditional on frozen choices',
        'warning':'Synthetic scenario recovery only. Truth and taxpayer explanations are excluded from detector SQL.'},
      'dataset':json.loads((Path(test_dir)/'manifest.json').read_text()),
      'factory_month':monthly_metrics,'factory':factory_metrics,
      'recall_by_type_intensity':by_type,'per_check':check_metrics(frame,features,threshold),'evasive':{},'fpr_by_decoy':fpr_by_decoy,
      'fpr_clean_vs_decoy':fpr_clean_decoy,'decoy_signal_pairs':decoy_pairs.to_dict('records'),
      'factory_queue':{'k':queue_k,'seed_a_calibration':queue_calibration,'seed_c':factory_metrics,
                       'queue_size':int(fac.flagged.sum()),'definition':'factory enters queue after K prioritised months; monthly SQL flag remains unchanged'},
      'ranking':{'sort_key':'families firing, then weakest-link normalised gap, then value at risk',
                 'seed_a_sort_test':sort_tests,'seed_c_precision_at_k':at_k},
      'precision_at_k':at_k, 'prevalence_adjusted_precision':prevalence,
      'review_capacity':{'framing':'If a team can review K cases per monthly snapshot, the table reports the observed synthetic precision at K.',
                         'capacity_rows':[{'cases_per_snapshot':int(k),'precision':v['macro_precision']} for k,v in at_k.items()]},
      'confusion':class_confusion(frame,fired),
      'single_signal_decoy_months':int(((frame.signals==1)&frame.scenario.isin(DECOYS)&(frame.is_cheat==0)).sum()),
      'misses':{'factory_months':len(misses),'factories_never_caught':int(((fac.is_cheat==1)&~fac.flagged).sum()),
                'reasons':misses.reason.value_counts().to_dict(),'examples':misses.head(12).to_dict('records')},
      'threshold_curve':[{'threshold':t,**rates(frame.is_cheat,(matrix.to_numpy()>t).sum(axis=1)>=2)} for t in GRID],
      'provenance':{'feature_sha256':hashlib.sha256((Path(test_dir)/'features.csv').read_bytes()).hexdigest(),
                    'truth_sha256':hashlib.sha256((Path(test_dir)/'truth.csv').read_bytes()).hexdigest()},
      'v1_vs_v2':{'v1_seed_b':{'seed':v1.get('protocol',{}).get('held_out_seed'),
                      'factory_month':v1.get('factory_month'),'factory':v1.get('factory')},
                   'v2_seed_c':{'seed':json.loads((Path(test_dir)/'manifest.json').read_text())['seed'],
                      'factory_month':monthly_metrics,'factory':factory_metrics}}
    }
    for level, data in [('factory_month',frame),('factory',fac)]:
        result['evasive'][level] = clustered_metrics(data[(data.is_cheat==1)&(data.evasive==1)])
    if 'performance' in v1: result['performance'] = v1['performance']
    result = json_safe(result)
    Path(output).write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    calibration_report = json_safe({'threshold':threshold,'calibration':calibration,
                                    'factory_queue':queue_calibration})
    (reports/'calibration.json').write_text(json.dumps(calibration_report, indent=2, allow_nan=False)+'\n')
    frame.to_csv(reports/'held_out_predictions.csv',index=False)
    misses.to_csv(reports/'misses.csv',index=False)
    fac.to_csv(reports/'factory_queue.csv',index=False)
    return result


if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--train',default='data/train'); parser.add_argument('--test',default='data/seed_c')
    parser.add_argument('--v1',default='results.json'); parser.add_argument('--output',default='results.json')
    parser.add_argument('--reports-dir',default='reports')
    args=parser.parse_args(); output=evaluate(args.train,args.test,args.v1,args.output,args.reports_dir)
    print(json.dumps({'threshold':output['protocol']['threshold'],'factory_month':output['factory_month'],
                      'factory_queue':output['factory_queue']},indent=2))
