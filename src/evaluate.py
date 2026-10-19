"""Calibrate on A once; evaluate B with factory-cluster bootstrap intervals."""
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np
import pandas as pd

CLASSES=['mismatch','missing documents','supplier issue','contradicting evidence','needs human review']
GRID=[.025,.05,.075,.10,.125,.15,.20,.25,.30,.40,.55]
FAMILIES=['production','movement','supplier','financial']

def prepare(directory):
    d=Path(directory)
    truth=pd.read_csv(d/'truth.csv')
    features=pd.read_csv(d/'features.csv')
    features.columns=features.columns.str.lower()
    keys=['factory_id','period_month']
    matrix=features.pivot_table(index=keys,columns='source_family',values='severity',aggfunc='max').reindex(columns=FAMILIES).fillna(0)
    truth=truth.set_index(keys).sort_index()
    matrix=matrix.reindex(truth.index)
    assert len(features)==len(truth)*6 and not matrix.isna().any().any()
    return truth,matrix,features

def rates(y,p):
    y,p=np.asarray(y,dtype=bool),np.asarray(p,dtype=bool)
    tp,fp,fn,tn=[int(v) for v in ((y&p).sum(),(~y&p).sum(),(y&~p).sum(),(~y&~p).sum())]
    return {'tp':tp,'fp':fp,'fn':fn,'tn':tn,'recall':tp/(tp+fn) if tp+fn else None,'fpr':fp/(fp+tn) if fp+tn else None,'precision':tp/(tp+fp) if tp+fp else None}

def clustered_metrics(frame, iterations=1000):
    result=rates(frame.is_cheat,frame.flagged)
    z=frame.copy()
    y,p=z.is_cheat.astype(bool),z.flagged.astype(bool)
    z['tp'],z['fp'],z['fn'],z['tn']=y&p,~y&p,y&~p,~y&~p
    counts=z.groupby('factory_id')[['tp','fp','fn','tn']].sum().to_numpy()
    rng=np.random.default_rng(721)
    samples=[]
    for _ in range(iterations):
        a,b,c,d=counts[rng.integers(0,len(counts),len(counts))].sum(axis=0)
        samples.append([a/(a+c) if a+c else np.nan,b/(b+d) if b+d else np.nan,a/(a+b) if a+b else np.nan])
    result['ci95']={name:[float(x) for x in np.nanquantile(np.asarray(samples)[:,j],[.025,.975])] for j,name in enumerate(['recall','fpr','precision']) if not np.isnan(np.asarray(samples)[:,j]).all()}
    return result

def evaluate(train_dir,test_dir,output='results.json'):
    a,am,_=prepare(train_dir)
    calibration=[]
    for t in GRID:
        r=rates(a.is_cheat,(am>t).sum(axis=1)>=2)
        calibration.append({'threshold':t,**r,'balanced_error':((1-r['recall'])+r['fpr'])/2})
    # Predeclared objective, no desired catch/FPR target. Conservative tie-break.
    threshold=min(calibration,key=lambda r:(r['balanced_error'],-r['threshold']))['threshold']
    Path("reports/calibration.json").write_text(json.dumps({"threshold":threshold,"calibration":calibration},indent=2)+"\n")
    b,bm,features=prepare(test_dir)
    b=b.reset_index()
    b['signals']=(bm.to_numpy()>threshold).sum(axis=1)
    b['flagged']=b.signals>=2
    b['score']=np.where(bm.to_numpy()>threshold,bm.to_numpy(),0).sum(axis=1)
    factory=b.groupby('factory_id').agg(is_cheat=('is_cheat','max'),flagged=('flagged','max'),scenario=('scenario','first'),intensity=('intensity','first'),evasive=('evasive','first')).reset_index()
    result={
      'protocol':{'train_seed':json.loads((Path(train_dir)/'manifest.json').read_text())['seed'],'held_out_seed':json.loads((Path(test_dir)/'manifest.json').read_text())['seed'],'months_per_factory':12,'threshold':threshold,'objective':'minimum factory-month balanced error on A; larger threshold on ties','calibration':calibration,'bootstrap':'1000 factory-cluster resamples; percentile 95% intervals, seed 721; conditional on fixed threshold','warning':'B shares the same synthetic generator as A. Not evidence of real-world accuracy. Features do not use truth labels.'},
      'dataset':json.loads((Path(test_dir)/'manifest.json').read_text()),
      'factory_month':clustered_metrics(b),'factory':clustered_metrics(factory),
      'recall_by_type_intensity':{},'fpr_by_decoy':{},'evasive':{},'confusion':{},'precision_at_k':{},
    }
    for level,frame in [('factory_month',b),('factory',factory)]:
        result['recall_by_type_intensity'][level]={f'{s}/{i:.0%}':clustered_metrics(g) for (s,i),g in frame[frame.is_cheat==1].groupby(['scenario','intensity'])}
        result['fpr_by_decoy'][level]={s:clustered_metrics(g) for s,g in frame[(frame.is_cheat==0)&frame.scenario.isin(__import__('src.generate',fromlist=['DECOYS']).DECOYS)].groupby('scenario')}
        result['evasive'][level]=clustered_metrics(frame[(frame.is_cheat==1)&(frame.evasive==1)])
    fired=features[features.severity>threshold].copy()
    # Evidence class from strongest non-bank discrepancy; financial-only remains review.
    fired['priority']=fired.check_family.isin(['bank_sales','bank_purchases']).astype(int)
    chosen=fired.sort_values(['priority','severity'],ascending=[True,False]).drop_duplicates(['factory_id','period_month'])
    pred=b.merge(chosen[['factory_id','period_month','discrepancy_class']],on=['factory_id','period_month'],how='left',suffixes=('_truth','_pred'))
    matrix=pd.crosstab(pred.discrepancy_class_truth,pred.discrepancy_class_pred.fillna('no signal')).reindex(index=CLASSES,columns=CLASSES+['no signal'],fill_value=0)
    result['confusion']={'unit':'factory-month; strongest non-financial evidence; includes unprioritised single-signal cases; clean months excluded','rows_truth':CLASSES,'columns_predicted':CLASSES+['no signal'],'counts':matrix.to_numpy().tolist()}
    for k in [50,200]:
        months=[]
        for month,g in b.groupby('period_month'):
            top=g[g.flagged].sort_values(['score','factory_id'],ascending=[False,True]).head(k)
            months.append({'month':month,'returned':len(top),'true_cheats':int(top.is_cheat.sum()),'precision':float(top.is_cheat.mean()) if len(top) else None})
        vals=[m['precision'] for m in months if m['precision'] is not None]
        rng=np.random.default_rng(721)
        # Resample factories, recompute queues, preserving all months within each cluster.
        ids=b.factory_id.unique(); groups={fid:g for fid,g in b.groupby('factory_id')}
        boots=[]
        for _ in range(200):
            sample=pd.concat([groups[fid] for fid in rng.choice(ids,len(ids))],ignore_index=True)
            tops=sample[sample.flagged].sort_values(['score','factory_id'],ascending=[False,True]).groupby('period_month').head(k)
            boots.append(tops.groupby('period_month').is_cheat.mean().mean())
        result['precision_at_k'][str(k)]={'macro_precision':float(np.mean(vals)) if vals else None,'ci95':[float(x) for x in np.nanquantile(boots,[.025,.975])],'bootstrap_replicates':200,'monthly_queues':months,'definition':'monthly snapshot proxy for weekly review; return up to k prioritised distinct factories each month; empty queues excluded; never pad with cleared cases'}
    result['single_signal_decoy_months']=int(((b.signals==1)&b.scenario.isin(__import__('src.generate',fromlist=['DECOYS']).DECOYS)&(b.is_cheat==0)).sum())
    misses=b[(b.is_cheat==1)&~b.flagged].copy()
    misses['reason']=np.where(misses.signals==0,'all independent source ratios below threshold','only one independent source family exceeded threshold')
    result['misses']={'factory_months':len(misses),'factories_never_caught':int(((factory.is_cheat==1)&~factory.flagged).sum()),'reasons':misses.reason.value_counts().to_dict(),'examples':misses.head(12).to_dict('records')}
    result['threshold_curve']=[{'threshold':t,**rates(b.is_cheat,(bm.to_numpy()>t).sum(axis=1)>=2)} for t in GRID]
    result['provenance']={'feature_sha256':hashlib.sha256((Path(test_dir)/'features.csv').read_bytes()).hexdigest(),'truth_sha256':hashlib.sha256((Path(test_dir)/'truth.csv').read_bytes()).hexdigest()}
    Path(output).write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    b.to_csv('reports/held_out_predictions.csv',index=False)
    misses.to_csv('reports/misses.csv',index=False)
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--train',default='data/train');p.add_argument('--test',default='data/generated');a=p.parse_args()
    r=evaluate(a.train,a.test);print(json.dumps({k:r[k] for k in ['protocol','factory_month','factory','single_signal_decoy_months']},indent=2))
