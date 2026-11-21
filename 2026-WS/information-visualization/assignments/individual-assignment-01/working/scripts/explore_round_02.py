"""Reproducible, dependency-free exploration of the preserved Eurostat extract.
Run with bundled Python; writes only round_02_findings.json. No network calls.
All differences are percentage points unless explicitly labelled relative.
"""
import json, hashlib, itertools, statistics
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT/'data/raw/ilc_lvho07b_20261121T183016Z.json'
EU = 'BE BG CZ DK DE EE IE EL ES FR HR IT CY LV LT LU HU MT NL AT PL PT RO SI SK FI SE'.split()
GROUPS = ['TOTAL'] + [f'QU{i}' for i in range(1,6)]
d = json.loads(SOURCE.read_text())
cats = [sorted(d['dimension'][k]['category']['index'], key=d['dimension'][k]['category']['index'].get) for k in d['id']]
rows=[]
for i, combo in enumerate(itertools.product(*cats)):
 if str(i) in d['value']:
  rows.append(dict(zip(d['id'],combo), value=d['value'][str(i)],status=d.get('status',{}).get(str(i),'')))
assert len(rows)==len(d['value'])==4966
assert all(0<=r['value']<=100 for r in rows)
lookup={(r['geo'],r['quant_inc'],int(r['time'])):r for r in rows}
assert len(lookup)==len(rows)
prov=json.loads(SOURCE.with_suffix('.provenance.json').read_text())
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()==prov['sha256']
def val(g,q,y): return lookup[g,q,y]['value']
def series(g,q,a,b): return [lookup[g,q,y] for y in range(a,b+1) if (g,q,y) in lookup]
def flags(g,a,b): return [r for r in rows if r['geo']==g and a<=int(r['time'])<=b and r['status']]
def delta(g,q,a,b): return round(val(g,q,b)-val(g,q,a),4)
geos=cats[d['id'].index('geo')]
countries=[g for g in geos if not g.startswith(('EU','EA'))]
windows=[]
for g in countries+['EU27_2020']:
 for a,b in itertools.combinations(range(2003,2026),2):
  if b-a<3 or not all((g,q,y) in lookup for q in GROUPS for y in range(a,b+1)):continue
  ds={q:delta(g,q,a,b) for q in GROUPS}
  windows.append(dict(geo=g,start=a,end=b,change=ds,flags=flags(g,a,b),q1_min=min(val(g,'QU1',y) for y in range(a,b+1)),q1_max=max(val(g,'QU1',y) for y in range(a,b+1))))
rankings={}
for y in range(2003,2026):
 members=[g for g in EU if all((g,q,y) in lookup for q in GROUPS)]
 rankings[str(y)]={q:sorted([dict(geo=g,value=val(g,q,y),status=lookup[g,q,y]['status']) for g in members],key=lambda r:(r['value'],r['geo'])) for q in GROUPS}
# Equal country means describe countries, never the EU population.
means=[]
for y in range(2010,2026):
 if all((g,q,y) in lookup for g in EU for q in GROUPS):
  means.append(dict(year=y,groups={q:dict(unweighted_country_mean=statistics.mean(val(g,q,y) for g in EU),median=statistics.median(val(g,q,y) for g in EU),published_EU=val('EU27_2020',q,y)) for q in GROUPS}))
# Every pair reversal in 2025: lower total, higher Q1.
reversals=[]
for a,b in itertools.permutations(EU,2):
 if val(a,'TOTAL',2025)<val(b,'TOTAL',2025) and val(a,'QU1',2025)>val(b,'QU1',2025):
  reversals.append(dict(lower_total=a,higher_total=b,total_gap=round(val(a,'TOTAL',2025)-val(b,'TOTAL',2025),4),q1_gap=round(val(a,'QU1',2025)-val(b,'QU1',2025),4)))
out=dict(source=prov,source_updated=d['updated'],geo_labels=d['dimension']['geo']['category']['label'],observations=rows,windows=windows,rankings=rankings,country_means=means,pair_reversals_2025=reversals)
path=ROOT/'data/derived/round_02_findings.json'
# Candidate-specific evidence and robustness checks. Ranks use competition ranking.
def rank(g,q,y): return 1+sum(val(h,q,y)<val(g,q,y) for h in EU if (h,q,y) in lookup)
def rel(g,q,a,b): return 100*(val(g,q,b)/val(g,q,a)-1)
clean15=[g for g in EU if not flags(g,2015,2025) and all((g,q,y) in lookup for q in GROUPS for y in range(2015,2026))]
def dispersion(gs,q,y):return dict(mean=statistics.mean(val(g,q,y) for g in gs),sd=statistics.pstdev(val(g,q,y) for g in gs),minimum=min(val(g,q,y) for g in gs),maximum=max(val(g,q,y) for g in gs))
ratio_a=val('AT','QU1',2015)/val('EU27_2020','QU1',2015)
ratio_b=val('AT','QU1',2025)/val('EU27_2020','QU1',2025)
candidates={
 'greece_recovery':dict(annual=[r for r in rows if r['geo']=='EL' and 2015<=int(r['time'])<=2025],relative_change_2015_2025={q:rel('EL',q,2015,2025) for q in GROUPS},change_2021_2025={q:delta('EL',q,2021,2025) for q in GROUPS},q1_above_2021_every_year=all(val('EL','QU1',y)>val('EL','QU1',2021) for y in range(2022,2026))),
 'austria_moving_benchmark':dict(ratio_2015=ratio_a,ratio_2025=ratio_b,relative_ratio_change_percent=100*(ratio_b/ratio_a-1),AT_relative_change_percent=rel('AT','QU1',2015,2025),EU_relative_change_percent=rel('EU27_2020','QU1',2015,2025),gap_change_pp=delta('AT','QU1',2015,2025)-delta('EU27_2020','QU1',2015,2025),annual=[dict(year=y,AT=val('AT','QU1',y),EU=val('EU27_2020','QU1',y),ratio=val('AT','QU1',y)/val('EU27_2020','QU1',y)) for y in range(2015,2026)]),
 'netherlands_latest_distribution':dict(annual=[r for r in rows if r['geo']=='NL' and 2017<=int(r['time'])<=2025],change_2024_2025={q:delta('NL',q,2024,2025) for q in GROUPS},q1_recent_relative_change=rel('NL','QU1',2024,2025)),
 'convergence':dict(countries=clean15,scope_reason='Complete annual six-group coverage, no source observation flags 2015–2025; NOT representative of all EU countries',all={str(y):{q:dispersion(clean15,q,y) for q in ['TOTAL','QU1']} for y in [2015,2025]},without_greece={str(y):{q:dispersion([g for g in clean15 if g!='EL'],q,y) for q in ['TOTAL','QU1']} for y in [2015,2025]},q1_increases=[dict(geo=g,change_pp=delta(g,'QU1',2015,2025)) for g in clean15 if delta(g,'QU1',2015,2025)>0]),
 'sweden_germany':dict(values=[r for r in rows if r['geo'] in ['SE','DE'] and r['time']=='2025'],rank={g:{q:rank(g,q,2025) for q in ['TOTAL','QU1']} for g in ['SE','DE']}),
 'mean_benchmark':dict(year=2025,mean=means[-1]['groups']['TOTAL']['unweighted_country_mean'],median=means[-1]['groups']['TOTAL']['median'],published_EU=val('EU27_2020','TOTAL',2025),ES=val('ES','TOTAL',2025)),
 'malta_complement':dict(annual=[r for r in rows if r['geo']=='MT' and 2015<=int(r['time'])<=2025],TOTAL_relative_change_percent=rel('MT','TOTAL',2015,2025),q1_relative_change_percent=rel('MT','QU1',2015,2025),non_overburdened_total=[100-val('MT','TOTAL',y) for y in [2015,2025]],non_overburdened_q1=[100-val('MT','QU1',y) for y in [2015,2025]]),
 'greece_progress_vs_residual':dict(total_change_pp=delta('EL','TOTAL',2015,2025),q1_change_pp=delta('EL','QU1',2015,2025),total_rank_2025=rank('EL','TOTAL',2025),q1_rank_2025=rank('EL','QU1',2025),clean_country_changes=sorted([dict(geo=g,change_pp=delta(g,'TOTAL',2015,2025),value_2025=val(g,'TOTAL',2025)) for g in clean15],key=lambda r:r['change_pp']))
}
assert abs(candidates['greece_recovery']['change_2021_2025']['QU1']-6.3)<1e-9
assert abs(candidates['austria_moving_benchmark']['gap_change_pp']-10.9)<1e-9
assert candidates['netherlands_latest_distribution']['change_2024_2025']['QU1']==3
assert all(not flags(g,2015,2025) for g in ['AT','EL','MT'])
assert all(val('EL',q,2015)>val('EL',q,2019)>val('EL',q,2025) for q in GROUPS)
assert candidates['greece_progress_vs_residual']['clean_country_changes'][0]['geo']=='EL'
out['candidate_evidence']=candidates
out['exploration_notes']=['Windows require all six groups in all years, duration >=3 years; 5452 eligible windows across countries and fixed EU aggregate.', 'No significance or causal testing; all selection is exploratory.', 'Published EU aggregates and equal-country statistics kept separate.', 'Missing records are excluded, never filled with zero.']
# Preserve flags once in source rows; window keys point to flagged observations.
for w in out['windows']:
 w['flag_keys']=[[r['quant_inc'],r['time'],r['status']] for r in w.pop('flags')]
path.write_text(json.dumps(out,indent=2)+'\n')
print('CANDIDATE SUMMARY')
for k,c in candidates.items():print(k,{key:v for key,v in c.items() if key not in ['annual','values','all','without_greece','clean_country_changes']})
