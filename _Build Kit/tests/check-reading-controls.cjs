const fs = require('fs'), path = require('path'), vm = require('vm'), assert = require('assert/strict');
const site = path.resolve(__dirname, '../../Career Assessments Web');
const source = fs.readFileSync(path.join(site, 'a11y-controls.js'), 'utf8');
function boot(stored = {}, osDark = false, blocked = false) {
  const data = {...stored}, events = {}, mediaEvents = {}, classes = new Set();
  const button = value => ({dataset: {textSize:value}, attrs:{}, events:{}, setAttribute(k,v){this.attrs[k]=v;}, addEventListener(k,v){this.events[k]=v;}});
  const sizes = ['normal','large','xl'].map(button), dark = button(), root = {dataset:{}};
  const media = {matches:osDark, addEventListener:(k,v)=>mediaEvents[k]=v};
  const document = {documentElement:root, body:{classList:{toggle:(k,on)=>on?classes.add(k):classes.delete(k)}}, querySelectorAll:()=>sizes, getElementById:()=>dark};
  const window = {matchMedia:()=>media,addEventListener:(k,v)=>events[k]=v};
  const localStorage = {getItem:k=>{if(blocked)throw Error();return data[k]??null;},setItem:(k,v)=>{if(blocked)throw Error();data[k]=v;}};
  vm.runInNewContext(source,{window,document,localStorage});
  return {data,events,media,mediaEvents,sizes,dark,root,classes};
}
for (const os of [false,true]) {
  const s = boot({},os);
  assert.equal(s.root.dataset.theme,os?'dark':'light');
  assert.deepEqual(s.data,{}); // Following the OS must not silently become a saved choice.
  s.dark.events.click();
  assert.equal(s.data.theme,os?'light':'dark');
  s.sizes[2].events.click();assert.equal(s.data.textSize,'xl');assert.equal(s.sizes[2].attrs['aria-pressed'],'true');
  const reloaded=boot(s.data,os);assert.equal(reloaded.root.dataset.textSize,'xl');assert.equal(reloaded.root.dataset.theme,s.data.theme);
  s.data.theme='light';s.data.textSize='normal';s.events.pageshow();
  assert.equal(s.root.dataset.theme,'light');assert.equal(s.root.dataset.textSize,'normal');
  const system=boot({},os);system.media.matches=!os;system.mediaEvents.change();assert.equal(system.root.dataset.theme,os?'light':'dark');
}
const denied=boot({},false,true);denied.dark.events.click();denied.sizes[1].events.click();assert.equal(denied.root.dataset.textSize,'large');
const pages=['index.html',...fs.readdirSync(site,{withFileTypes:true}).filter(d=>d.isDirectory()&&fs.existsSync(path.join(site,d.name,'index.html'))).map(d=>d.name+'/index.html')];
assert.equal(pages.length,13);
for(const p of pages){const h=fs.readFileSync(path.join(site,p),'utf8');for(const id of ['sizeNormal','sizeLarge','sizeXL','themeBtn'])assert.equal(h.split('id="'+id+'"').length-1,1,p);assert(h.includes('a11y-controls.js')&&h.includes('a11y-controls.css'),p);}
assert(!/font(?:-size)?:[^;}]*\dpx/.test(fs.readFileSync(path.join(site,'home.css'),'utf8')));
console.log('PASS: system theme, explicit overrides, persisted sizes, back-navigation refresh, blocked storage, and all 13 front-end pages.');
