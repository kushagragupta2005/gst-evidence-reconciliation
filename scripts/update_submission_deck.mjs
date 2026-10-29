// Requires the documented Codex bundled @oai/artifact-tool runtime for export.
// All quantitative replacements come from committed result/report artifacts.
import fs from 'node:fs/promises';
import path from 'node:path';
import {execFileSync} from 'node:child_process';
import {pathToFileURL} from 'node:url';
import {PresentationFile,FileBlob} from '@oai/artifact-tool';
const root=process.cwd(),load=async p=>JSON.parse(await fs.readFile(p,'utf8'));
try{
const b=await load('results.json'),c=await load('reports/v3_c_results.json'),bounds=await load('reports/wrong_clear_bounds.json'),bench=await load('reports/benchmark_current_reader.json');
const historical=await load('reports/benchmark_full.json');
const percent=n=>(100*n).toFixed(2)+'%',p=await PresentationFile.importPptx(await FileBlob.load('docs/archive/legacy/submission/pre_v3_pitch.pptx'));
function replace(slide,old,value){const shape=slide.shapes.items.find(s=>String(s.text)===old);if(!shape)throw Error('Missing exact source text: '+old);shape.text.replace(old,value);return shape;}
replace(p.slides.items[1],'Today, officers must reconcile sources manually, even when physical and financial evidence disagree.','This prototype targets officers reviewing declarations when supporting records arrive separately.');
replace(p.slides.items[1],'Invoice matching finds inconsistencies inside the tax system. It does not reconcile declarations with independent operational evidence.','Invoice matching compares tax documents. We add operational records; no benchmark of commercial fraud systems is claimed.');
replace(p.slides.items[2],'Four SQL conservation checks run in Exasol Personal. The LLM writes notes only after SQL has selected a case.','Six SQL checks form four source families. Displayed notes use a validated deterministic fallback; an LLM is optional.');
const s=p.slides.items[2];
for(const [a,v] of [['Material → output','Production'],['Purchased inputs and power','Material, power and stock'],['Dispatch → invoice','Movement'],['Goods movement and invoice','Dispatch, invoice and reuse'],['Stock roll-forward','Supplier'],['Opening, production and dispatch','Supplier returns; loop context'],['Supplier chain','Financial'],['Returns and looping links','Bank vs sales and purchases'],['PRIORITISE ONLY WHEN TWO INDEPENDENT SOURCE FAMILIES FIRE','PRIORITISE ONLY WHEN AT LEAST TWO SOURCE FAMILIES FIRE']])replace(s,a,v);
const caption=s.shapes.items.find(x=>String(x.text)==='A single-source month stays review-only or receives a documented cleared disposition.');
caption.position={...caption.position,top:586,height:20};
const r=p.slides.items[3];replace(r,'Seed C results and limits','V3 held-out results and limits');
replace(r,'Seed A selected the threshold and factory queue rule. Seed C reports the held-out result.',`V3-A selected threshold ${c.protocol.threshold.toFixed(2)} and K=${c.factory_queue.k}. V3-C confirms frozen choices.`);
replace(r,'84.01%',percent(c.factory_month.recall));replace(r,'16.58%',percent(c.factory_month.fpr));replace(r,'58.67%',percent(c.factory.precision));replace(r,'Queue precision after K=4 months',`Factory queue precision, K=${c.factory_queue.k}`);
replace(r,'917 factories enter the K-month queue. The top 50-case snapshot has 75.00% synthetic precision.',`${c.factory_queue.queue_size} factories enter the queue. Top-50 monthly macro precision: ${percent(c.precision_at_k['50'].macro_precision)}.`);
replace(r,'Limits: synthetic data only. Human review remains required. Confidence intervals do not measure generator bias. Power and bank data require lawful access and privacy safeguards.','Synthetic only. Verification labels are generated. Forger test, ablation intervals and second-machine reproduction remain open. Human review required.');
const detail=r.shapes.add({geometry:'textbox',position:{left:64,top:258,width:1100,height:120},fill:'none',line:{fill:'none',width:0}});
detail.text=`V3-C 95% CIs: recall ${c.factory_month.ci95.recall.map(percent).join(' – ')}; FPR ${c.factory_month.ci95.fpr.map(percent).join(' – ')}.\nV3-B primary: recall ${percent(b.factory_month.recall)}; FPR ${percent(b.factory_month.fpr)}.\nWrong-clears: ${bounds.seeds.v3_c.wrong_clear_factories} of ${bounds.seeds.v3_c.active_cheat_factories} active-cheat factories; approximate upper bound ${percent(bounds.seeds.v3_c.approximate_upper_95)}. Assumes independent factories.`;
detail.text.style={fontSize:19,typeface:'Aptos',color:'#F6F1E8'};
const last=p.slides.items[4];replace(last,'20,978,945 raw evidence rows',`${bench.current_feature_rows.toLocaleString('en-US')} current V3-C feature rows`);
replace(last,'Ranked workload timing: 48.946 s raw; 6.141 s after the batch ledger refresh. Measured on a MacBook.',`${bench.current_factories.toLocaleString('en-US')} factories. Stock median: Exasol ${bench.checks.stock_rollforward.exasol_median_seconds.toFixed(3)} s; DuckDB ${bench.checks.stock_rollforward.duckdb_median_seconds.toFixed(3)} s. DuckDB was faster. MacBook workload timings.`);
replace(last,'Germany: the same reconciliation pattern would need local tax rules, lawful data access and independent validation. This deck claims no German deployment or statistic.',`The ${(historical.manifest.raw_evidence_rows/1e6).toFixed(2)}M-row run is historical DEV, not fresh. Current timings exclude Exasol ingestion; DuckDB load is separate. No German deployment is claimed.`);
for(let i=0;i<p.slides.items.length;i++)p.slides.items[i].speakerNotes.text=`Sources: results.json (V3-B); reports/v3_c_results.json (V3-C); reports/wrong_clear_bounds.json; reports/benchmark_current_reader.json; docs/PROJECT_GUIDE.md. Every dataset is synthetic. Author: Kushagra Gupta, solo participant. AI coding assistants helped. Public demo: https://kushagragupta2005.github.io/gst-evidence-reconciliation/. Slide ${i+1}. Existing source template: docs/archive/legacy/submission/pre_v3_pitch.pptx. Loop tracing is context, not a standalone trigger. Zero-event bound is approximate, conditional on independent factories. Top-50 means monthly snapshots, not a measured weekly queue; Jan–Mar contain no active cheat months in this generator.`;
await fs.mkdir('.pitch_build/judge/final',{recursive:true});const candidate=path.join(root,'.pitch_build/judge/candidate.pptx');await(await PresentationFile.exportPptx(p)).save(candidate);
const skill=process.env.GST_PRESENTATIONS_SKILL;if(!skill)throw Error('Set GST_PRESENTATIONS_SKILL to the installed presentations skill directory.');
const {finalizePresentation}=await import(pathToFileURL(path.join(skill,'container_tools/artifact_tool_utils.mjs')).href);
const final=path.join(root,'00_SUBMISSION/Pitch.pptx');
await finalizePresentation({workspaceDir:root,candidatePath:candidate,finalPath:final,pythonExecutable:process.env.GST_RUNTIME_PYTHON,integrityValidatorPath:path.join(skill,'container_tools/inspect_presentation_package_integrity.py'),layoutValidatorPath:path.join(skill,'container_tools/inspect_presentation_layout_geometry.py'),layoutArgs:['--expected-slide-size-emu','12192000,6858000','--validate-heading-fit'],explicitTotalSlideCount:5,fontPolicy:{basis:'design',families:['Aptos']},verifyArtifactToolImport:true,receiptPath:path.join(root,'.pitch_build/judge/deck.validation.json')});
for(let i=0;i<p.slides.items.length;i++){const blob=await p.export({slide:p.slides.items[i],format:'png',scale:1});await fs.mkdir('docs/deck',{recursive:true});await fs.writeFile(`docs/deck/slide-${String(i+1).padStart(2,'0')}.png`,new Uint8Array(await blob.arrayBuffer()));}
execFileSync(process.env.GST_RUNTIME_PYTHON,['scripts/render_pitch_pdf.py'],{stdio:'inherit'});
console.log('Updated editable PPTX and matching PDF from frozen V3 artifacts.');
}catch(e){console.error(e.message);process.exitCode=1;}
