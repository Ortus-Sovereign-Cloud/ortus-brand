P='/tmp/claude-1002/-home-bohdaq-git/6b5adcb0-31d6-44c8-b201-55c34d7527ea/scratchpad/mailui/project/'
T13="font-size: 13px; font-variant-numeric: tabular-nums"
def edit(name,reps,mark=True):
    f=P+name+'.dc.html'; s=open(f).read()
    for a,b,*n in reps:
        n=n[0] if n else 1
        assert s.count(a)==n,(name,a[:70],s.count(a))
        s=s.replace(a,b)
    if mark and '/*dense2*/' not in s: s=s.replace('/*type2*/','/*type2*//*dense2*/')
    open(f,'w').write(s)
def show(name):
    s=open(P+name+'.dc.html').read()
    a=s.find('<nav aria-label="Apps"')
    if a>=0:
        b=s.index('</nav>',a)+6; s=s[:a]+'[RAIL]'+s[b:]
    a=s.index('<x-dc>'); print(s[a:])
