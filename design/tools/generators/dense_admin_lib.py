import re
P='/tmp/claude-1002/-home-bohdaq-git/6b5adcb0-31d6-44c8-b201-55c34d7527ea/scratchpad/mailui/project/'
M12="font: 500 12px 'Geist Mono', monospace"
M13="font: 500 13px 'Geist Mono', monospace"
COMMON=[
 ("""<span style="font: 500 12px 'Geist Mono', monospace; padding: 3px 8px; border-radius: 7px; background: #1E2230; color: #C3C8D4">MINISTRY OF [NAME]</span>""",
  """<span style="font-size: 13px; padding: 3px 10px; border-radius: 7px; background: #1E2230; color: #C3C8D4">Ministry of [Name]</span>"""),
 ('<header style="display: flex; align-items: center; gap: 12px; padding: 12px 16px; border-bottom: 1px solid #1E2129">','<header style="display: flex; align-items: center; gap: 12px; padding: 14px 24px; border-bottom: 1px solid #1E2129">'),
 ('max-width: 236px; padding: 14px 10px; display: flex; flex-direction: column; gap: 2px','max-width: 236px; padding: 20px 12px; display: flex; flex-direction: column; gap: 4px'),
 ("justify-content: space-between; height: 36px; padding: 0 12px; border-radius: 10px; text-decoration: none; color: #ECEEF3; ' + (a ?","justify-content: space-between; height: 40px; padding: 0 12px; border-radius: 10px; text-decoration: none; color: #ECEEF3; ' + (a ?"),
 ("""<span>{{n.name}}</span><span style="font: 500 12px 'Geist Mono', monospace; color: #9198A8">{{n.badge}}</span>""","""<span>{{n.name}}</span><span style="font-size: 13px; font-variant-numeric: tabular-nums; color: #9198A8">{{n.badge}}</span>"""),
 ("badgeStyle: 'font: 500 12px Geist Mono, monospace; color: '","badgeStyle: 'font-size: 13px; font-variant-numeric: tabular-nums; color: '"),
]
def edit(name,reps,common=True):
    s=open(P+name+'.dc.html').read()
    if common:
        for a,b in COMMON:
            if a in s: s=s.replace(a,b)
    for a,b,*n in reps:
        n=n[0] if n else 1
        assert s.count(a)==n,(name,a[:70],s.count(a))
        s=s.replace(a,b)
    if '/*dense2*/' not in s: s=s.replace('/*type2*/','/*type2*//*dense2*/')
    open(P+name+'.dc.html','w').write(s)
