const fs=require('fs'),vm=require('vm'),path=require('path'),assert=require('assert');
const root=path.resolve(__dirname,'../..'),site=path.join(root,'Career Assessments Web');
const data=JSON.parse(fs.readFileSync(path.join(site,'search-index.json'),'utf8'));
const added=data.careers.filter(c=>c.area==='jobs-you-can-start-now');
assert.equal(added.length,23);
for(const c of added){
 const html=fs.readFileSync(path.join(site,c.url),'utf8');
 for(const [i,m] of [...html.matchAll(/<script[^>]*>([\s\S]*?)<\/script>/g)].entries()) new vm.Script(m[1],{filename:c.url+':'+i});
}
const hub=fs.readFileSync(path.join(root,'Jobs_You_Can_Start_Now_Career_Assessments.html'),'utf8');
const embedded=JSON.parse(hub.match(/var ASSESSMENTS_DATA = (\{[\s\S]*?\});/)[1]);
assert.equal(Object.keys(embedded).length,23);
// The web edition adds site attribution; portable hub assessment content must still match.
function assessmentContent(value){return String(value).replace(/<nav class="dvr-nav"[\s\S]*?<\/nav>/,'').replaceAll('../student-opportunities.html','https://shariwhittyphi-collab.github.io/career-factory/student-opportunities.html').replace(/\/\* ---- Site attribution ---- \*\/[\s\S]*?(?=<\/style>)/,'').replace(/<!-- Site attribution \(attribution\.py\) -->[\s\S]*?<\/aside>/,'').split('\n').map(line=>line.trim()).filter(Boolean).join('\n');}
for(const c of added){const raw=assessmentContent(fs.readFileSync(path.join(site,c.url),'utf8')); assert(Object.values(embedded).some(v=>assessmentContent(Buffer.from(v,'base64').toString('utf8'))===raw),c.url);}
const html=fs.readFileSync(path.join(site,'jobs-you-can-start-now/private-investigator.html'),'utf8');
const report=html.match(/        function generateReport\(\) \{[\s\S]*?\n        \}/)[0];
const next=html.match(/        function nextSection\(\) \{[\s\S]*?\n        \}/)[0];
const items=Array.from({length:9},(_,i)=>'Question '+(i+1));
function run(ninth){
 const elements={comments:{value:''},reportContent:{innerHTML:''},progress:{textContent:''}};
 const answers={future:'plan',motivation:'interest'};items.forEach((_,i)=>answers['readiness'+(i+1)]='yes');answers.readiness9=ninth;
 const ctx={DATA:{readinessItems:items,scores:{interest:10},motLabels:{interest:'Interest'},futureLabels:{plan:'Plan'},recs:['a','b','c','d','e'],nextSteps:[],finalWords:''},document:{getElementById:id=>elements[id]},checked:name=>answers[name],esc:s=>s,show:()=>{},alertMsg:s=>ctx.alert=s,updateProgress:()=>{},currentSection:10};
 vm.createContext(ctx);vm.runInContext(report+'\n'+next+'\nnextSection();generateReport();',ctx);return {ctx,report:elements.reportContent.innerHTML};
}
let r=run(null);assert.match(r.ctx.alert,/question 9/);assert.equal(r.ctx.currentSection,10);
r=run('no');assert.match(r.report,/8 \/ 9/);assert.match(r.report,/Question 9 \(you said: no\)/);
r=run('yes');assert.match(r.report,/9 \/ 9/);assert.match(r.report,/width: 100%/);
console.log('PASS: all 23 assessment scripts compile; hub assessment content matches web pages (excluding site attribution); ninth-answer validation, scoring, feedback, and 100% score tested.');
