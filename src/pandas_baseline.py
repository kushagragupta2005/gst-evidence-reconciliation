"""Same ratios/threshold/count/gap checksums in pandas; not a universal DB comparison."""
import argparse
import gc
import json
import time
from pathlib import Path
import numpy as np
import pandas as pd


def benchmark(data,label):
    r=json.load(open('results.json')); b=r['performance'][label];t=r['protocol']['threshold']
    names=sorted((v for v in b['unoptimised'] if v!='V_RANKED_CASES'),key=lambda v:-b['unoptimised'][v]['seconds'])[:2]
    output={}
    keys=['factory_id','period_month']
    for name in names:
        frames={};start=time.perf_counter()
        def read(table,cols):
            frames[table]=pd.read_csv(Path(data)/(table+'.csv'),usecols=cols)
            return frames[table]
        if name=='V_STOCK_ROLLFORWARD':
            m=read('factory_month',keys+['opening_stock','purchases_finished','declared_output','declared_dispatch','closing_stock'])
        elif name=='V_MATERIAL_OUTPUT':
            m=read('factory_month',keys+['purchases_kg','declared_output','power_kwh'])
        elif name=='V_DISPATCH_INVOICE':
            e=read('eway_bills',keys+['eway_id','quantity']);i=read('invoices',keys+['quantity'])
        else:
            p=read('purchase_invoices',['buyer_factory_id','period_month','quantity']);s=read('suppliers',['supplier_id','owner_factory_id']);sr=read('supplier_returns',['supplier_id','period_month','declared_sales_kg'])
        read_seconds=time.perf_counter()-start;start=time.perf_counter()
        if name=='V_STOCK_ROLLFORWARD':
            m=m.sort_values(keys);prev=m.groupby('factory_id').closing_stock.shift().fillna(m.opening_stock)
            gap=m.opening_stock+m.purchases_finished+m.declared_output-m.declared_dispatch-m.closing_stock
            ratio=np.maximum(abs(gap),abs(m.opening_stock-prev))/m.declared_output
        elif name=='V_MATERIAL_OUTPUT':
            gap=m.purchases_kg*.8-m.declared_output
            ratio=np.maximum(abs(gap)/(m.purchases_kg*.8),abs(m.power_kwh/4-m.declared_output)/(m.power_kwh/4))
        elif name=='V_DISPATCH_INVOICE':
            a=e.groupby(keys).agg(dispatch=('quantity','sum'),docs=('eway_id','nunique'),n=('eway_id','count'))
            a=a.join(i.groupby(keys).quantity.sum().rename('invoice')).fillna(0)
            gap=a.dispatch-a.invoice;ratio=np.maximum(abs(gap)/a.dispatch,1-a.docs/a.n)
        else:
            a=p.groupby(['buyer_factory_id','period_month']).quantity.sum().reset_index().rename(columns={'buyer_factory_id':'factory_id'})
            a=a.merge(s,left_on='factory_id',right_on='owner_factory_id').merge(sr,on=['supplier_id','period_month'],how='left')
            gap=a.quantity-a.declared_sales_kg.fillna(0);ratio=abs(gap)/a.quantity
        mask=ratio>t
        count=int(mask.sum());checksum=float(abs(gap[mask]).sum())
        seconds=time.perf_counter()-start
        expected=b['unoptimised'][name]['rows'][0]
        assert count==expected[0],(name,count,expected)
        assert abs(checksum-float(expected[1] or 0)) < max(.01,abs(checksum)*1e-8),(name,checksum,expected)
        output[name]={'csv_read_seconds':read_seconds,'compute_seconds':seconds,'total_seconds':read_seconds+seconds,'rows':count,'checksum':checksum,'exasol_raw_seconds':b['unoptimised'][name]['seconds'],'equivalent_counts_and_gaps':True}
        frames.clear();gc.collect()
    r['performance'][label]['pandas']=output
    Path('results.json').write_text(json.dumps(r,indent=2)+'\n')
    Path(f'reports/pandas_{label}.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(output,indent=2))
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--data',default='data/generated');p.add_argument('--label',default='small');a=p.parse_args();benchmark(a.data,a.label)
