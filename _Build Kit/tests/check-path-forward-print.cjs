// Run with Playwright installed and Chromium or PLAYWRIGHT_CHANNEL=msedge.
const {chromium}=require('playwright');
const assert=require('node:assert/strict');
const path=require('node:path');
const {pathToFileURL}=require('node:url');
(async()=>{
 const browser=await chromium.launch({headless:true,...(process.env.PLAYWRIGHT_CHANNEL?{channel:process.env.PLAYWRIGHT_CHANNEL}:{})});
 try {
  for(const theme of ['light','dark']) {
   const page=await browser.newPage();
   await page.goto(pathToFileURL(path.resolve(__dirname,'../../Career Assessments Web/your-path-forward.html')).href);
   await page.evaluate(theme=>{document.documentElement.dataset.theme=theme;QUESTIONS.forEach((q,i)=>ratings[i]=3);selectedValues.add(0);selectedGoals.add(0);document.getElementById('studentNotes').value='Print regression: final notes included.';goTo(7);},theme);
   await page.emulateMedia({media:'print'});
   assert(await page.locator('#s7').isVisible(),'Report must remain visible in print');
   assert(!(await page.locator('#s1').isVisible()),'Questions must stay hidden');
   assert(!(await page.getByRole('button',{name:'Print My Report'}).isVisible()),'Print button must not print');
   const text=await page.locator('#results-content').textContent();
   for(const expected of ['Student Career Exploration Report','Career Matches','What Matters to You','Next Steps You Want to Take','Print regression: final notes included.','(800) 526-7234']) assert(text.includes(expected),expected);
   await page.pdf({path:path.resolve(process.env.PRINT_TEST_OUTPUT||'.',`path-forward-${theme}.pdf`),preferCSSPageSize:true,printBackground:false});
   await page.close();
  }
  console.log('PASS: light/dark print visibility, report sections, hidden questions and controls; PDFs generated.');
 } finally {await browser.close();}
})().catch(error=>{console.error(error);process.exitCode=1;});

