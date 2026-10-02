const INDEX = 'https://raw.githubusercontent.com/shariwhittyphi-collab/career-factory/main/Career%20Assessments%20Web/search-index.json';
const SITE = 'https://careerfactorynd.org/';
const normalize = value => String(value).toLowerCase().replace(/[^a-z0-9]+/g, ' ').trim();
function json(body, status = 200, extra = {}) {
  return new Response(JSON.stringify(body, null, 2), {status, headers: {
    'Content-Type':'application/json; charset=utf-8', 'Access-Control-Allow-Origin':'*',
    'Access-Control-Allow-Methods':'GET, HEAD, OPTIONS', 'Access-Control-Allow-Headers':'Accept, Content-Type',
    'Cache-Control':status === 200 ? 'public, max-age=300' : 'no-store',
    'X-Content-Type-Options':'nosniff', ...extra
  }});
}
export async function handle(request, fetcher = fetch) {
  if (request.method === 'OPTIONS') return new Response(null, {status:204,headers:json({}).headers});
  if (!['GET','HEAD'].includes(request.method)) return json({error:'Read-only API. Use GET.'},405,{'Allow':'GET, HEAD, OPTIONS'});
  const url = new URL(request.url), path = url.pathname.replace(/\/$/,'') || '/';
  if (path === '/') return json({name:'Career Factory API',version:'1',website:SITE,endpoints:{careers:'/v1/careers?q=welder&area=skilled-trades&limit=20&offset=0',career:'/v1/careers/skilled-trades/welder',areas:'/v1/areas'},notes:'Public career information only. Pay is median pay, not a starting wage or guarantee. Open assessmentUrl for source links and data dates. Null figures mean unavailable; annual-contract pay is not hourly pay.'});
  const detail = path.match(/^\/v1\/careers\/([a-z0-9-]+)\/([a-z0-9-]+)$/);
  if (path !== '/v1/careers' && path !== '/v1/areas' && !detail) return json({error:'Endpoint not found.'},404);
  const q = url.searchParams.get('q') || '', area = url.searchParams.get('area') || '';
  const limitText = url.searchParams.get('limit') ?? '20', offsetText = url.searchParams.get('offset') ?? '0';
  if (q.length > 200 || !/^\d+$/.test(limitText) || !/^\d+$/.test(offsetText) || Number(limitText)<1 || Number(limitText)>100 || !Number.isSafeInteger(Number(offsetText))) return json({error:'Use a search of at most 200 characters, limit 1–100, and a nonnegative integer offset.'},400);
  try {
    const upstream = await fetcher(INDEX, {cf:{cacheTtl:300,cacheEverything:true},signal:AbortSignal.timeout(8000)});
    if (!upstream.ok) throw new Error('Index unavailable');
    const data = await upstream.json();
    if (!Array.isArray(data.careers) || !Array.isArray(data.areas)) throw new Error('Invalid index');
    const careers = data.careers.filter(c=>c.published===true && /^[a-z0-9-]+\/[a-z0-9-]+\.html$/.test(c.url)).map(c=>({...c,id:c.url.replace(/\.html$/,''),assessmentUrl:SITE+c.url}));
    const areas = data.areas.filter(a=>careers.some(c=>c.area===a.slug)).map(a=>({...a,count:careers.filter(c=>c.area===a.slug).length}));
    let response;
    if (path === '/v1/areas') response=json({total:areas.length,areas});
    else if (detail) {
      const career=careers.find(c=>c.id===detail[1]+'/'+detail[2]);
      response=career?json({career}):json({error:'Career not found.'},404);
    } else {
      if (area && !areas.some(a=>a.slug===area)) return json({error:'Unknown career area. See /v1/areas.'},400);
      const words=normalize(q).split(' ').filter(Boolean);
      const matches=careers.filter(c=>(!area||c.area===area)&&words.every(w=>normalize([c.name,c.subtitle,c.areaName,...(c.tags||[])].join(' ')).includes(w))).sort((a,b)=>a.name.localeCompare(b.name));
      const limit=Number(limitText),offset=Number(offsetText);
      response=json({total:matches.length,limit,offset,careers:matches.slice(offset,offset+limit)});
    }
    return request.method==='HEAD'?new Response(null,{status:response.status,headers:response.headers}):response;
  } catch { return json({error:'Career information is temporarily unavailable. Please try again shortly.'},503); }
}
export default {fetch:request=>handle(request)};
