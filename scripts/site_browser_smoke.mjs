/** Actual Chromium checks against a running server, a file URL, or deployed Pages. */
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
    const page = await browser.newPage({viewport:{width:1440,height:1000}});
    const errors = [], failed = [], bad = [], snapshotFetches = [];
    page.on('console',m=>{if(m.type()==='error') errors.push(m.text())});
    page.on('pageerror',e=>errors.push(e.message));
    page.on('requestfailed',r=>failed.push({url:r.url(),reason:r.failure()?.errorText}));
    page.on('response',r=>{if(r.status()>=400) bad.push({url:r.url(),status:r.status()})});
    page.on('request',r=>{if(['fetch','xhr'].includes(r.resourceType()) && /data\/(manifest|evaluation|performance|snapshot)\.json/.test(r.url())) snapshotFetches.push(r.url())});
    await page.goto(url,{waitUntil:'networkidle'});
    await page.locator('.status, #mode-pill').first().waitFor();
    assert.ok(await page.evaluate(()=>Boolean(window.__SNAPSHOT__?.evaluation?.heldout_v3_b)));
    assert.ok(!/Load failed|Snapshot failed to load/i.test(await page.locator('body').innerText()));
    assert.deepEqual(errors,[],'console errors'); assert.deepEqual(failed,[],'failed requests');
    assert.deepEqual(bad,[],'HTTP failures'); assert.deepEqual(snapshotFetches,[],'snapshot must not fetch');
    report.checks.push({url:url.startsWith('file:')?'file://website/index.html':url,status:'passed',console_errors:errors,http_errors:bad,failed_requests:failed,snapshot_fetches:snapshotFetches});
    await page.close();
  }
  report.status='passed';
} catch(error) {report.status='failed'; report.error=String(error); throw error}
finally {await browser.close(); await fs.mkdir('reports',{recursive:true}); await fs.writeFile(arg('--report')||'reports/site_browser_smoke.json',JSON.stringify(report,null,2)+'\n'); console.log(JSON.stringify(report,null,2))}
