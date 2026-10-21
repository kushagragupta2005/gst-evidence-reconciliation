const e=window.EVALUATION, pct=x=>(x*100).toFixed(2)+'%';
document.querySelector('#recall').textContent=pct(e.monthly_recall);
document.querySelector('#fpr').textContent=pct(e.monthly_fpr);
document.querySelector('#queue').textContent=e.queue_size.toLocaleString();
document.querySelector('#p50').textContent=pct(e.top50_precision);
document.querySelector('#queue-detail').textContent=`K = ${e.queue_k} prioritised months · ${pct(e.queue_precision)} factory-queue precision`;
document.querySelector('#scale-text').textContent=`${e.evidence_rows.toLocaleString()} raw evidence rows were measured in a local Exasol Personal workload on a MacBook. The ranked view took ${e.ranked_raw_seconds.toFixed(3)} s raw and ${e.ranked_ledger_seconds.toFixed(3)} s after the batch ledger refresh. Timings are workload measurements, not a general benchmark.`;
const verdict=document.querySelector('#verdict');document.querySelectorAll('.family').forEach(row=>row.addEventListener('click',()=>{row.classList.toggle('on');row.querySelector('strong').textContent=row.classList.contains('on')?'fires':'off';const n=document.querySelectorAll('.family.on').length;verdict.textContent=n>=2?`${n} independent families: prioritise for human review.`:`${n||'No'} independent ${n===1?'family':'families'}: review-only.`;verdict.style.color=n>=2?'#f24b95':'#bcde63'}));
