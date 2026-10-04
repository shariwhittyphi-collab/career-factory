const fs=require('fs'),path=require('path'),vm=require('vm'),assert=require('assert/strict');
const root=path.resolve(__dirname,'../..'),site=path.join(root,'Career Assessments Web');
const careers=JSON.parse(fs.readFileSync(path.join(root,'_Build Kit/Rural Additions/careers.json'),'utf8'));
const index=JSON.parse(fs.readFileSync(path.join(site,'search-index.json'),'utf8'));
assert.equal(index.careers.length,195);
for(const c of index.careers)assert(fs.existsSync(path.join(site,c.url)),c.url);
const members=new Set(JSON.parse(fs.readFileSync(path.join(site,'nd-in-demand.json'),'utf8')).careers.map(c=>c.url));
for(const c of careers){
 const url=c.area+'/'+c.slug+'.html',raw=fs.readFileSync(path.join(site,url),'utf8');
 assert(!members.has(url),'new specialty must not silently acquire a list marker');
 const hub=fs.readFileSync(path.join(root,c.area==='science'?'Science_Career_Assessments.html':'Jobs_You_Can_Start_Now_Career_Assessments.html'),'utf8');
 const embedded=JSON.parse(hub.match(/var ASSESSMENTS_DATA = (\{[\s\S]*?\});/)[1]);
 const portable=Buffer.from(embedded[c.name+' Career Assessment'],'base64').toString('utf8');
 const normalized=raw.replace(/<nav class="dvr-nav"[\s\S]*?<\/nav>/,'').replaceAll('../student-opportunities.html','https://shariwhittyphi-collab.github.io/career-factory/student-opportunities.html');
 assert.equal(portable.replaceAll('\r\n','\n')===normalized.replaceAll('\r\n','\n'),true,'web and portable core content must match');
 for(const original of [raw,portable]){
  const h=original.replaceAll('\r\n','\n');
  for(const [i,m]of [...h.matchAll(/<script[^>]*>([\s\S]*?)<\/script>/g)].entries())new vm.Script(m[1],{filename:c.slug+':'+i});
  assert.equal((h.match(/data:image\/jpeg;base64,/g)||[]).length,2);
  assert.equal((h.match(/id="section\d+"/g)||[]).length,11);
  const DATA=JSON.parse(h.match(/const DATA = (.*);\n/)[1]);
  const report=h.match(/        function generateReport\(\) \{[\s\S]*?\n        \}/)[0];
  const next=h.match(/        function nextSection\(\) \{[\s\S]*?\n        \}/)[0];
  for(const answer of ['yes','no','unsure'])for(const future of c.future.map(x=>x[0])){
   const answers={motivation:'explore',future};for(let i=1;i<=8;i++)answers['readiness'+i]=answer;
   const elements={comments:{value:'<img src=x onerror=alert(1)>'},reportContent:{innerHTML:''},progress:{textContent:''}};
   const ctx={DATA,document:{getElementById:id=>elements[id]},checked:n=>answers[n],esc:s=>s.replace(/[&<>"']/g,ch=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[ch])),show:id=>ctx.shown=id,alertMsg:s=>ctx.alert=s,updateProgress:()=>{},currentSection:10};
   vm.runInNewContext(next+'\n'+report+'\nnextSection();generateReport();',ctx);
   const out=elements.reportContent.innerHTML;
   assert.equal(ctx.shown,'report');assert(out.includes(`Activities that sound comfortable: ${answer==='yes'?8:0} / 8`));
   assert(!out.includes('<img src=x'));assert(out.includes('&lt;img'));
   assert(out.includes(DATA.futureLabels[future]));
   for(const step of DATA.futureSteps[future]||DATA.nextSteps)assert(out.includes(step),step);
   assert(!out.includes('excellent fit')&&!out.includes('not your best fit'));
   delete answers.readiness8;ctx.currentSection=10;vm.runInNewContext('nextSection()',ctx);assert.equal(ctx.currentSection,10);assert(ctx.alert.includes('8'));
   answers.readiness8=answer;delete answers.future;vm.runInNewContext('generateReport()',ctx);assert(ctx.alert.includes('plan'));
  }
  // The inherited print controller must include only the visible report, handle
  // print-one independently, and retain the correct career title in both themes.
  const print=h.slice(h.lastIndexOf('/* ---- Unified print behavior (printfix2) ---- */')).match(/\/\* ---- Unified print behavior \(printfix2\) ---- \*\/[\s\S]*?(\(function \(\) \{[\s\S]*?\}\)\(\);)/)[1];
  for(const theme of ['light','dark'])for(const visible of [false,true])for(const one of [false,true]){
   const classes=new Set(one?['print-one']:[]);let title;
   const r={offsetHeight:visible?100:0,querySelector:()=>null,insertBefore:d=>title=d.children[0].textContent};
   const ctx={Date,setInterval:()=>{},window:{addEventListener:()=>{}},document:{readyState:'complete',documentElement:{dataset:{theme}},body:{classList:{contains:x=>classes.has(x),add:x=>classes.add(x),remove:x=>classes.delete(x)}},getElementById:id=>id==='report'?r:null,createElement:()=>({children:[],appendChild(x){this.children.push(x)}})}};
   vm.runInNewContext(print,ctx);assert.equal(classes.has('print-report'),visible&&!one);if(visible&&!one)assert(title.includes(c.name));
  }
 }
}
const opportunities=fs.readFileSync(path.join(site,'student-opportunities.html'),'utf8');
for(const name of ['Gooseneck','RDO','Titan','Butler','Plains Ag'])assert(opportunities.includes(name));
assert(opportunities.includes('October 4, 2026'));
new vm.Script(fs.readFileSync(path.join(site,'student-opportunities.js'),'utf8'));
console.log('PASS: 195 links; new careers unmarked; matching web/hub content; 2 images and 11 sections each; reflections, missing answers, plan-specific steps, escaped notes; light/dark and one-section print controller.');
