/** Actual Chromium checks against a running server, a file URL, or deployed Pages. */
import AxeBuilder from '@axe-core/playwright';
import { chromium } from '@playwright/test';
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import path from 'node:path';
import { pathToFileURL } from 'node:url';
const arg = (name) => {const i = process.argv.indexOf(name); return i < 0 ? undefined : process.argv[i+1]};
const urls = arg('--url') ? [arg('--url')] : ['http://127.0.0.1:8081/', pathToFileURL(path.resolve('website/index.html')).href];
const browser = await chromium.launch({headless:true});
const report = {time_utc:new Date().toISOString(), checks:[]};
try {
  for (const url of urls) {
   for (const width of [1440,390]) {
    const context = await browser.newContext({viewport:{width,height:1000},reducedMotion:'reduce'});
    const page = await context.newPage();
    const errors = [], failed = [], bad = [], snapshotFetches = [];
    page.on('console',m=>{if(m.type()==='error') errors.push(m.text())});
    page.on('pageerror',e=>errors.push(e.message));
    page.on('requestfailed',r=>failed.push({url:r.url(),reason:r.failure()?.errorText}));
    page.on('response',r=>{if(r.status()>=400) bad.push({url:r.url(),status:r.status()})});
    page.on('request',r=>{if(['fetch','xhr'].includes(r.resourceType()) && /data\/(manifest|evaluation|performance|snapshot)\.json/.test(r.url())) snapshotFetches.push(r.url())});
    await page.goto(url,{waitUntil:'networkidle'});
    await page.locator('.status, #mode-pill').first().waitFor();
    assert.ok(await page.evaluate(()=>Boolean(window.__SNAPSHOT__?.evaluation?.heldout_v3_b)));
    for (const seed of ['v3_c','v3_b']) {await page.locator(`[data-seed="${seed}"]`).click();assert.equal(await page.locator('#result-stats .value').first().textContent(), await page.evaluate(s=>(window.__SNAPSHOT__.evaluation['heldout_'+s].factory_month.recall*100).toLocaleString('en-US',{minimumFractionDigits:1,maximumFractionDigits:1})+'%',seed));}
    for(const i of ['0','1','2']){await page.locator('#factory').selectOption(i);assert.match(await page.locator('#case-content').innerText(),/Validator: passed/);}
    await page.locator('#factory').selectOption('0');
    for(const i of ['0','1','2']){await page.locator(`[data-question="${i}"]`).click();await page.locator('#answer .sql').waitFor();assert.match(await page.locator('#answer .sql').innerText(),/^SELECT .* LIMIT 200$/);}
    assert.ok(await page.evaluate(()=>{const values=new Set();function walk(x){if(typeof x==='number')values.add(x);else if(x&&typeof x==='object')Object.values(x).forEach(walk);}walk(window.__SNAPSHOT__);return [...document.querySelectorAll('[data-value]')].every(e=>values.has(Number(e.dataset.value)));}),'displayed metric provenance');
    assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),'no horizontal overflow');
    if(!url.startsWith('file:')) {const accessibility=await new AxeBuilder({page}).withTags(['wcag2a','wcag2aa','wcag21aa']).analyze();assert.deepEqual(accessibility.violations.map(v=>({id:v.id,nodes:v.nodes.map(n=>n.target)})),[],'AA accessibility');}
    await page.keyboard.press('Tab');assert.ok(await page.evaluate(()=>document.activeElement!==document.body),'keyboard focus');
    if(url===urls[0] && !arg('--url')){await fs.mkdir('docs/screenshots',{recursive:true});await page.evaluate(()=>{document.activeElement?.blur();window.scrollTo(0,0)});await page.screenshot({path:`docs/screenshots/site-${width===1440?'desktop':'mobile'}.png`,fullPage:true});}
    assert.ok(!/Load failed|Snapshot failed to load/i.test(await page.locator('body').innerText()));
    assert.deepEqual(errors,[],'console errors'); assert.deepEqual(failed,[],'failed requests');
    assert.deepEqual(bad,[],'HTTP failures'); assert.deepEqual(snapshotFetches,[],'snapshot must not fetch');
    report.checks.push({url:url.startsWith('file:')?'file://website/index.html':url,width,mode:await page.locator('#mode-pill').innerText(),accessibility:url.startsWith('file:')?'tested on identical HTTP page; axe fetches CSS on file URLs':'AA passed',status:'passed',console_errors:errors,http_errors:bad,failed_requests:failed,snapshot_fetches:snapshotFetches});
    await context.close();
   }
  }
  report.status='passed';
} catch(error) {report.status='failed'; report.error=String(error); throw error}
finally {await browser.close(); await fs.mkdir('reports',{recursive:true}); await fs.writeFile(arg('--report')||'reports/site_browser_smoke.json',JSON.stringify(report,null,2)+'\n'); console.log(JSON.stringify(report,null,2))}
