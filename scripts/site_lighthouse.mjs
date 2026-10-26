import lighthouse from 'lighthouse';
import * as chromeLauncher from 'chrome-launcher';
import {chromium} from '@playwright/test';
import fs from 'node:fs/promises';
import {execFileSync} from 'node:child_process';
const arg=name=>{const i=process.argv.indexOf(name);return i<0?undefined:process.argv[i+1]};
const base=arg('--url')||'http://127.0.0.1:8081/';
const report={time_utc:new Date().toISOString(),git_sha:execFileSync('git',['rev-parse','HEAD'],{encoding:'utf8'}).trim(),lighthouse_version:null,environment:'Headless Chromium; Lighthouse default simulated mobile throttling; one run per page.',pages:[]};
const chrome=await chromeLauncher.launch({chromePath:chromium.executablePath(),chromeFlags:['--headless','--no-sandbox','--disable-gpu']});
try{for(const slug of ['','problem','how-it-works','cases','results','system','data','limits']){
 const url=new URL((slug?slug+'/':'')+'index.html',base).href;
 const {lhr}=await lighthouse(url,{port:chrome.port,output:'json',logLevel:'error',onlyCategories:['performance','accessibility','best-practices','seo']});
 report.lighthouse_version=lhr.lighthouseVersion;
 const scores=Object.fromEntries(Object.entries(lhr.categories).map(([k,v])=>[k,Math.round(v.score*100)]));
 const item={page:slug||'home',url,scores,metrics:{lcp_ms:lhr.audits['largest-contentful-paint'].numericValue,cls:lhr.audits['cumulative-layout-shift'].numericValue},findings:Object.entries(lhr.audits).filter(([,v])=>v.score!==null&&v.score<1).map(([id,v])=>({id,score:v.score,title:v.title,description:v.description,details:Array.isArray(v.details?.items)?v.details.items.slice(0,3):undefined}))};
 report.pages.push(item);console.log(JSON.stringify({page:item.page,scores}));
}}finally{await chrome.kill();report.meets_95=report.pages.length===8&&report.pages.every(p=>Object.values(p.scores).every(s=>s>=95));await fs.writeFile(arg('--report')||'reports/lighthouse_local.json',JSON.stringify(report,null,2)+'\n');}
if(!report.meets_95)process.exitCode=1;
