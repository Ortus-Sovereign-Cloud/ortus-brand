import re,glob,os,json,sys
P='/tmp/claude-1002/-home-bohdaq-git/6b5adcb0-31d6-44c8-b201-55c34d7527ea/scratchpad/mailui/project/'
c=json.load(open(P+'canvas.json'))
NEW={'WebRecordFiled','AdminPolicy','WebWelcome','MobileWelcome','MobileCitizenForm','MobileCitizenReceipt'}
GEN={'OSDesktop','OSSecurity','OSControl','OSApps','OSLock','OSOverview','OSDialogs','OSStore'}
WEB={9:11,10:12,11:12,12:13,13:14,14:15}
MOB={9:11,10:12,11:12}
def bump(s,m):
    s=re.sub(r'font-size: (\d+)px', lambda x: f'font-size: {m.get(int(x.group(1)),int(x.group(1)))}px', s)
    s=re.sub(r"(font: (?:italic )?(?:\d{3} )?)(\d+)px", lambda x: f'{x.group(1)}{m.get(int(x.group(2)),int(x.group(2)))}px', s)
    return s
marker='/*type2*/'
for p in sorted(glob.glob(P+'*.dc.html')):
    n=os.path.basename(p)[:-8]
    if n in NEW or n in GEN or n.startswith('Brand'): continue
    s=open(p).read()
    if marker in s: continue
    mob = n.startswith('Mobile')
    fixed = n in ('WorkstationLogin','OSFirstBoot')
    s=bump(s, MOB if mob else WEB)
    if not mob:
        # keep rail labels compact
        i=s.find('<nav aria-label="Apps"')
        if i>=0:
            j=s.index('</nav>',i); r=s[i:j].replace('font-size: 12px','font-size: 11px'); s=s[:i]+r+s[j:]
    s=s.replace('#6E7585','#8A91A1')
    s=s.replace('<style>','<style>'+marker,1)
    open(p,'w').write(s)
H=os.path.dirname(os.path.abspath(__file__))+'/'
for g in ['os.py','os2.py']:
    s=open(H+g).read()
    if '#type2' in s: continue
    s=bump(s,{10:11,11:12,12:13,13:14})
    s=s.replace('#6E7585','#8A91A1')
    open(H+g,'w').write('#type2\n'+s)
print('done')
