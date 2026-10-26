import {chromium} from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
const arg=name=>{const i=process.argv.indexOf(name);return i<0?undefined:process.argv[i+1]};
const slugs=['','problem','how-it-works','cases','results','system','data','limits'];
const base=arg('--url')||'http://127.0.0.1:8081/';
const browser=await chromium.launch({headless:true});const report={time_utc:new Date().toISOString(),checks:[],links:[]};
try{
 for(const width of [375,768,1440])for(const theme of ['light','dark']){
  const context=await browser.newContext({viewport:{width,height:1000},colorScheme:theme,reducedMotion:'reduce'});
  for(const slug of slugs){
   const url=new URL((slug?slug+'/':'')+'index.html',base).href;const p=await context.newPage();const errors=[],bad=[],failed=[];
   p.on('console',m=>{if(m.type()==='error')errors.push(m.text())});p.on('pageerror',e=>errors.push(e.message));p.on('response',r=>{if(r.status()>=400)bad.push([r.url(),r.status()])});p.on('requestfailed',r=>failed.push(r.url()));
   const response=await p.goto(url,{waitUntil:'networkidle'});assert.equal(response.status(),200);
   assert.ok(await p.evaluate(()=>Boolean(window.__METRICS__)));
   assert.equal(await p.locator('h1').count(),1);
   await p.locator('.menu-toggle').click();assert.equal(await p.locator('.menu-toggle').getAttribute('aria-expanded'),'true');assert.equal(await p.locator('#explore-menu a').count(),8);await p.keyboard.press('Escape');assert.equal(await p.locator('.menu-toggle').getAttribute('aria-expanded'),'false');
   if(slug==='cases'){
    await p.locator('#answer .sql').waitFor();
    for(const i of [0,1,2]){await p.locator(`[data-case="${i}"]`).click();assert.match(await p.locator('#case-content').innerText(),/Validator: passed/);}
    await p.locator('[data-case="0"]').click();
    // Exercise all intents once per theme/width; no arbitrary SQL is accepted by the server.
    for(const i of [0,1,2]){await p.locator(`[data-question="${i}"]`).click();await p.locator('#answer .sql').waitFor();assert.match(await p.locator('#answer .sql').innerText(),/^SELECT .* LIMIT 200$/);}
   }
   if(slug==='results')for(const seed of ['v3_c','v3_b']){await p.locator(`[data-seed="${seed}"]`).click();const expected=await p.evaluate(s=>(window.__METRICS__.results[s].factory_month.recall*100).toLocaleString('en-IN',{minimumFractionDigits:1,maximumFractionDigits:1})+'%',seed);assert.equal(await p.locator('#result-stats .stat-value').first().textContent(),expected);}
   assert.ok(await p.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),'horizontal overflow '+slug);
   assert.ok(await p.evaluate(()=>{const v=new Set();const walk=x=>{if(typeof x==='number')v.add(x);else if(x&&typeof x==='object')Object.values(x).forEach(walk)};walk(window.__METRICS__);return [...document.querySelectorAll('[data-value]')].every(e=>v.has(Number(e.dataset.value)))}),'metric provenance');
   const axe=await new AxeBuilder({page:p}).withTags(['wcag2a','wcag2aa','wcag21aa']).analyze();assert.deepEqual(axe.violations.map(v=>({id:v.id,nodes:v.nodes.map(n=>n.target)})),[],`${slug} ${width} ${theme} accessibility`);
   assert.deepEqual(errors,[]);assert.deepEqual(bad,[]);assert.deepEqual(failed,[]);
   if(width===1440&&theme==='light'){
    const links=await p.locator('a[href]').evaluateAll(a=>a.map(x=>x.href));
    for(const href of [...new Set(links)])if(href.startsWith(base)&&!href.includes('#')){const r=await context.request.get(href);assert.equal(r.status(),200,'internal link '+href);report.links.push({url:href,status:r.status()});}
   }
   if(!arg('--url')&&['','cases','results'].includes(slug)&&[375,1440].includes(width)){
    await fs.mkdir('docs/screenshots',{recursive:true});await p.evaluate(()=>{document.activeElement?.blur();scrollTo(0,0)});
    await p.screenshot({path:`docs/screenshots/${slug||'home'}-${width}-${theme}.png`,fullPage:true});
   }
   report.checks.push({page:slug||'home',url,width,theme,status:'passed',mode:await p.locator('#mode-pill').innerText(),console_errors:errors,http_errors:bad});await p.close();
  }await context.close();
 }
 if(!arg('--url')){
  for(const slug of slugs){const p=await browser.newPage({viewport:{width:375,height:1000},reducedMotion:'reduce'});const errors=[];p.on('pageerror',e=>errors.push(e.message));p.on('console',m=>{if(m.type()==='error')errors.push(m.text())});p.on('requestfailed',r=>errors.push(r.url()));await p.goto(pathToFileURL(path.resolve('website',slug,'index.html')).href);assert.ok(await p.evaluate(()=>Boolean(window.__METRICS__)));assert.deepEqual(errors,[]);report.checks.push({page:slug||'home',mode:'file Snapshot',status:'passed'});await p.close();}
 }
 report.status='passed';
}catch(error){report.status='failed';report.error=String(error);throw error;}
finally{await browser.close();await fs.writeFile(arg('--report')||'reports/site_browser_smoke.json',JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify({status:report.status,checks:report.checks.length,links:report.links.length,error:report.error}));}
