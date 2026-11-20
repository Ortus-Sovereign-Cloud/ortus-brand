# Rebuild storyboard thumbnail strips from render/png (run after render/check.sh on every board in the stories).
import re,glob,subprocess,json,sys
S='/tmp/claude-1002/-home-bohdaq-git/6b5adcb0-31d6-44c8-b201-55c34d7527ea/scratchpad/'
sys.path.insert(0,S+'gen')
src=open(S+'gen/story.py').read()
B=glob.glob('/home/bohdaq/.cache/ms-playwright/chromium_headless_shell-1248/*/chrome-headless-shell')[0]
blocks=re.split(r"dict\(k='(s\d)'",src)[1:]
m={}
for k,body in zip(blocks[0::2],blocks[1::2]):
    seg=body[body.index('steps=['):body.index('states=[')]
    boards=re.findall(r"\('S[\w.–]+','[^']*','[^']*','[^']*',('\w+'|None),'(?:V1|V2|Later)','\w*'\)",seg)
    boards=[None if b=='None' else b.strip("'") for b in boards]
    m[k]=boards
    cells=''
    for b in boards:
        if not b: cells+='<div style="width:440px;height:275px;flex:none"></div>'; continue
        mob=b.startswith('Mobile')
        cells+=f'<div style="width:440px;height:275px;flex:none;background:#0D0F15;display:flex;justify-content:center;overflow:hidden"><img src="../png/{b}.png" style="{"height:275px" if mob else "width:440px;height:275px"};display:block"></div>'
    open(S+f'render/strips/{k}.html','w').write(f'<body style="margin:0;display:flex;background:#0D0F15">{cells}</body>')
    subprocess.run([B,'--no-sandbox','--hide-scrollbars','--disable-gpu','--force-device-scale-factor=2',f'--window-size={440*len(boards)},275',f'--screenshot={S}render/strips/{k}.png',f'file://{S}render/strips/{k}.html'],capture_output=True)
    print(k,len(boards),boards)
json.dump(m,open(S+'render/strips/map.json','w'))
