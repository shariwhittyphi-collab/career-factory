const {chromium}=require('playwright');
const assert=require('node:assert/strict');
const path=require('node:path');
const {pathToFileURL}=require('node:url');
(async()=>{
 const browser=await chromium.launch({headless:true,...(process.env.PLAYWRIGHT_CHANNEL?{channel:process.env.PLAYWRIGHT_CHANNEL}:{})});
 try {
  const page=await browser.newPage({viewport:{width:390,height:844}});
  await page.addInitScript(()=>{
   window.spoken=[];window.cancelCount=0;
   Object.defineProperty(window,'speechSynthesis',{value:{speak(u){window.spoken.push(u.text);},cancel(){window.cancelCount++;}}});
   window.SpeechSynthesisUtterance=class{constructor(text){this.text=text;}};
  });
  await page.goto(pathToFileURL(path.resolve(__dirname,'../../Career Assessments Web/your-path-forward.html')).href);
  await page.evaluate(()=>goTo(1));
  assert.equal(await page.locator('.q-text .listen-button').count(),30);
  const first=page.locator('.q-text .listen-button').first();
  await first.focus();await page.keyboard.press('Enter');
  assert.equal((await page.evaluate(()=>window.spoken))[0],await page.evaluate(()=>QUESTIONS[0].q));
  assert.equal(await first.getAttribute('aria-pressed'),'true');
  await first.click();assert.equal(await first.getAttribute('aria-pressed'),'false');
  await first.click();await page.evaluate(()=>QUESTIONS.forEach((q,i)=>ratings[i]=3));
  await page.locator('#s1 .btn-primary').click();
  assert.equal(await first.getAttribute('aria-pressed'),'false');
  await page.locator('#s2 .section-header .listen-button').click();
  assert((await page.evaluate(()=>window.spoken.at(-1))).includes('Good Pay'));
  await page.evaluate(()=>startOver());
  assert.equal(await page.locator('.q-text .listen-button').count(),30);
  await page.evaluate(()=>goTo(1));
  assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),'Phone layout should not scroll sideways');
  await page.emulateMedia({media:'print'});
  assert.equal(await page.locator('.listen-button:visible').count(),0);
  console.log('PASS: 30 question controls, keyboard speech/stop, choices spoken, navigation stops, restart, phone width and print hiding. Speech engine stubbed; device voices vary.');
 } finally {await browser.close();}
})().catch(error=>{console.error(error);process.exitCode=1;});
