// Fails if any career page or hub copy still hands down a verdict (Shari's Oct 10 2026 decision).
const fs=require('fs'),path=require('path'),assert=require('assert');
const root=path.resolve(__dirname,'../..'),site=path.join(root,'Career Assessments Web');
const bad=/excellent fit|not your best fit|best fit right now|Pursue this|The Verdict|Motivation Score|You look ready|THINK ABOUT IT|Excellent Fit|Low Readiness|Strong Readiness|This is your path/;
let n=0;
for(const d of fs.readdirSync(site,{withFileTypes:true}))if(d.isDirectory())for(const f of fs.readdirSync(path.join(site,d.name))){
  if(!f.endsWith('.html')||f==='index.html')continue;n++;
  const h=fs.readFileSync(path.join(site,d.name,f),'utf8');const m=h.match(bad);assert(!m,d.name+'/'+f+': '+(m&&m[0]));}
let e=0;
for(const f of fs.readdirSync(root).filter(f=>f.endsWith('_Career_Assessments.html'))){
  const s=fs.readFileSync(path.join(root,f),'utf8');const data=JSON.parse(s.match(/var ASSESSMENTS_DATA = (\{[\s\S]*?\});/)[1]);
  for(const [k,v] of Object.entries(data)){e++;const m=Buffer.from(v,'base64').toString('utf8').match(bad);assert(!m,f+' / '+k+': '+(m&&m[0]));}}
console.log('PASS: no verdict wording in '+n+' career pages or '+e+' hub copies.');
