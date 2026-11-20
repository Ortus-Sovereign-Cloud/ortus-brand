P='/tmp/claude-1002/-home-bohdaq-git/6b5adcb0-31d6-44c8-b201-55c34d7527ea/scratchpad/mailui/project/'
def edit(name,reps,mark=True):
    s=open(P+name+'.dc.html').read()
    for a,b,*n in reps:
        n=n[0] if n else 1
        assert s.count(a)==n,(name,a[:70],s.count(a))
        s=s.replace(a,b)
    if mark and '/*dense2*/' not in s: s=s.replace('/*type2*/','/*type2*//*dense2*/')
    open(P+name+'.dc.html','w').write(s)
