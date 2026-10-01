'use strict';
const byId = id => document.getElementById(id);
const controls = ['search', 'area', 'pay', 'growth', 'sort'].map(byId);
const PAGE_SIZE = 6;
let careers = [], visibleCount = PAGE_SIZE;
const preferred = ['Electrician', 'Registered Nurse', 'Software Developer', 'Welder', 'Dental Hygienist', 'Heavy and Tractor-Trailer Truck Driver'];
const currency = new Intl.NumberFormat('en-US', {style:'currency', currency:'USD', maximumFractionDigits:0});
const hourly = new Intl.NumberFormat('en-US', {style:'currency', currency:'USD', minimumFractionDigits:2, maximumFractionDigits:2});
const decode = value => {const el = document.createElement('textarea'); el.innerHTML = String(value); return el.value;};
const normalized = value => value.toLocaleLowerCase().replace(/[^a-z0-9]+/g, ' ').trim();
function element(tag, className, text) {const el = document.createElement(tag); if (className) el.className = className; if (text !== undefined) el.textContent = text; return el;}
function payMatches(c, value) {
  if (!value) return true;
  if (value === 'annual') return c.payBasis === 'annual-contract';
  if (c.payBasis === 'annual-contract' || c.medianHourly == null) return false;
  return value === 'under-20' ? c.medianHourly < 20 : value === '20-to-30' ? c.medianHourly >= 20 && c.medianHourly < 30 : c.medianHourly >= 30;
}
function growthMatches(c, value) {
  if (!value) return true;
  if (value === 'unknown') return c.ndGrowthPct == null;
  if (c.ndGrowthPct == null) return false;
  if (value === 'growing-fast') return c.ndGrowthPct >= 10;
  if (value === 'steady') return c.ndGrowthPct >= 5 && c.ndGrowthPct < 10;
  if (value === 'flat') return c.ndGrowthPct >= 0 && c.ndGrowthPct < 5;
  return c.ndGrowthPct < 0;
}
function card(c) {
  const item = element('article', 'career-card'); item.dataset.area = c.area;
  item.append(element('div', 'career-category', c.areaName));
  const heading = element('h3'), link = element('a', '', c.name); link.href = c.url; heading.append(link); item.append(heading, element('p', '', c.subtitle));
  const meta = element('div', 'career-meta'), pay = element('div');
  const isAnnual = c.payBasis === 'annual-contract' || c.medianHourly == null;
  const amount = isAnnual ? c.medianAnnual : c.medianHourly;
  const value = element('span', 'pay-amount', amount == null ? 'Not listed' : (isAnnual ? currency : hourly).format(amount));
  if (amount != null) value.append(element('span', 'pay-unit', isAnnual ? ' / year' : ' / hour'));
  pay.append(value, element('span', 'pay-label', isAnnual && c.payBasis === 'annual-contract' ? 'Median pay · annual contract' : 'Median pay · North Dakota'));
  const arrow = element('span', 'card-arrow', '↗'); arrow.setAttribute('aria-hidden', 'true'); meta.append(pay, arrow); item.append(meta);
  const growth = c.ndGrowthPct == null ? 'No ND growth figure in this assessment' : `${c.ndGrowthPct > 0 ? '+' : ''}${c.ndGrowthPct}% projected ND growth`;
  item.append(element('div', 'growth-note', growth)); return item;
}
function filtered() {
  const words = normalized(byId('search').value).split(' ').filter(Boolean);
  const area = byId('area').value, pay = byId('pay').value, growth = byId('growth').value;
  const matches = careers.filter(c => words.every(w => c.searchText.includes(w)) && (!area || c.area === area) && payMatches(c, pay) && growthMatches(c, growth));
  const order = byId('sort').value;
  matches.sort((a,b) => order === 'az' ? a.name.localeCompare(b.name) : order === 'za' ? b.name.localeCompare(a.name) : a.rank - b.rank || a.name.localeCompare(b.name));
  return matches;
}
function render() {
  const matches = filtered(); byId('results').replaceChildren(...matches.slice(0,visibleCount).map(card));
  byId('result-count').textContent = `${matches.length} ${matches.length === 1 ? 'career' : 'careers'} to explore`;
  byId('empty').hidden = matches.length !== 0; byId('more').hidden = matches.length <= visibleCount;
  byId('shown').textContent = matches.length ? `Showing ${Math.min(visibleCount,matches.length)} of ${matches.length} careers` : '';
}
function reset() {controls.forEach(el => el.value = el.id === 'sort' ? 'discovery' : ''); visibleCount = PAGE_SIZE; render();}
controls.forEach(el => el.addEventListener(el.id === 'search' ? 'input' : 'change', () => {visibleCount = PAGE_SIZE; render();}));
byId('reset').addEventListener('click', reset);
byId('empty-reset').addEventListener('click', () => {reset(); byId('search').focus();});
byId('more').addEventListener('click', () => {const previous = visibleCount; visibleCount += PAGE_SIZE; render(); byId('results').children[previous]?.querySelector('a')?.focus({preventScroll:true});});
async function start() {
  try {
    const response = await fetch('search-index.json'); if (!response.ok) throw new Error('Index unavailable');
    const data = await response.json();
    careers = data.careers.filter(c => c.published === true && /^[a-z0-9-]+\/[a-z0-9-]+\.html$/.test(c.url)).map(c => {
      const name = decode(c.name), subtitle = decode(c.subtitle), areaName = decode(c.areaName), i = preferred.indexOf(name);
      return {...c, name, subtitle, areaName, rank:i < 0 ? preferred.length : i, searchText:normalized([name, subtitle, areaName, ...(c.tags || [])].join(' '))};
    });
    const areas = data.areas.filter(a => careers.some(c => c.area === a.slug));
    areas.forEach(a => {const option = element('option','',decode(a.name)); option.value = a.slug; byId('area').append(option); const count = careers.filter(c=>c.area === a.slug).length; const label = document.querySelector(`[data-area="${a.slug}"] .area-count`); if(label) label.textContent = `${count} careers`;});
    document.querySelector('[data-total]').textContent = careers.length; document.querySelector('[data-areas]').textContent = areas.length; render();
  } catch (error) {
    byId('result-count').textContent = 'Search is unavailable. You can still browse all career areas below.';
    controls.forEach(el=>el.disabled=true); byId('reset').disabled=true;
    const link = element('a','button secondary','Browse career areas'); link.href='#areas'; byId('results').append(link);
  }
}
start();
