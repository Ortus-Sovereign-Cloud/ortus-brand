#type2
import re, json, os
D='/tmp/claude-1002/-home-bohdaq-git/6b5adcb0-31d6-44c8-b201-55c34d7527ea/scratchpad/mailui/project/'
src=open(D+'BrandIcons.dc.html').read()
icons={}
for m in re.finditer(r'<span style="width: 96px; height: 96px; border-radius: 28px; background: (linear-gradient\([^)]*\));[^"]*"><svg width="56" height="56" viewBox="0 0 48 48" aria-hidden="true">(.*?)</svg></span><span style="font-size: 13px; font-weight: 500">([^<]+)</span>', src, re.S):
    icons[m.group(3)]=(m.group(1), m.group(2))
G='linear-gradient(155deg, #2A2D38, #0B0D14)'
icons['Files']=('linear-gradient(155deg, #263311, #0B0D14)','<path d="M5 14 A4 4 0 0 1 9 10 H19 L23 15 H39 A4 4 0 0 1 43 19 V36 A4 4 0 0 1 39 40 H9 A4 4 0 0 1 5 36 Z" fill="#C6F06B"/><rect x="5" y="20" width="38" height="4" fill="#ECEEF3" opacity=".8"/>')
icons['Terminal']=(G,'<rect x="5" y="8" width="38" height="32" rx="7" fill="#9198A8"/><path d="M13 18 L20 24 L13 30" fill="none" stroke="#0B0D14" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/><rect x="23" y="28" width="12" height="4" rx="2" fill="#ECEEF3"/>')
icons['Settings']=(G,'<circle cx="24" cy="24" r="17" fill="#9198A8"/><circle cx="24" cy="24" r="7" fill="#ECEEF3"/><path d="M24 7 V13 M24 35 V41 M7 24 H13 M35 24 H41" stroke="#0B0D14" stroke-width="4"/>')
icons['Browser']=('linear-gradient(155deg, #1B2350, #0B0D14)','<circle cx="24" cy="24" r="18" fill="#6E86FF"/><path d="M24 10 L29 24 L24 38 L19 24 Z" fill="#ECEEF3"/><circle cx="24" cy="24" r="3" fill="#0B0D14"/>')
icons['Trash']=(G,'<path d="M12 14 H36 L33 42 H15 Z" fill="#9198A8" opacity=".7"/><rect x="9" y="9" width="30" height="5" rx="2.5" fill="#ECEEF3"/>')
MARK='<path d="M22 30 L4 30 A18 18 0 0 1 22 12 Z" fill="{a}"/><path d="M26 30 L26 12 A18 18 0 0 1 44 30 Z" fill="{b}"/><rect x="4" y="34" width="40" height="5" rx="2.5" fill="{c}"/>'
def mark(s,a='{{accent}}',b='#6E86FF',c='#4FD1C5'): return f'<svg width="{s}" height="{s}" viewBox="0 0 48 48" aria-hidden="true">'+MARK.format(a=a,b=b,c=c)+'</svg>'
def tile(n,s,shadow=True):
    bg,g=icons[n]; r=round(s*.24)
    sh='box-shadow: inset 0 1px 0 rgba(255,255,255,.14), 0 8px 18px rgba(0,0,0,.35); ' if shadow else ''
    return f'<span aria-hidden="true" style="width: {s}px; height: {s}px; flex: none; border-radius: {r}px; background: {bg}; {sh}display: flex; align-items: center; justify-content: center"><svg width="{round(s*.6)}" height="{round(s*.6)}" viewBox="0 0 48 48">{g}</svg></span>'
HEAD='''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
body{{margin:0}}
</style>
</helmet>
'''
FOOT='''</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"accent":{"editor":"color","default":"#8EA2FF","options":["#8EA2FF","#4FD1C5","#C6F06B","#F5A35C"]},"$preview":{"width":1440,"height":900}}'>
class Component extends DCLogic {
  renderVals() { return { accent: this.props.accent ?? '#8EA2FF' }; }
}
</script>
</body>
</html>
'''
WALL='background: radial-gradient(700px 520px at 18% 78%, rgba(79,209,197,.45), transparent 70%), radial-gradient(800px 600px at 82% 20%, rgba(110,134,255,.6), transparent 70%), radial-gradient(600px 500px at 55% 60%, rgba(160,110,255,.35), transparent 70%), linear-gradient(160deg, #0B1030 0%, #07080C 100%)'
GLASS='background: rgba(24,27,38,.74); backdrop-filter: blur(30px) saturate(160%); -webkit-backdrop-filter: blur(30px) saturate(160%); border: 1px solid rgba(255,255,255,.12)'
def lights():
    b=lambda lab,path,col: f'<span role="button" aria-label="{lab}" style="width: 18px; height: 18px; border-radius: 6px; background: rgba(255,255,255,.12); display: flex; align-items: center; justify-content: center"><svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="{col}" stroke-width="3" stroke-linecap="round" aria-hidden="true">{path}</svg></span>'
    return '<span style="display: flex; gap: 6px">'+b('Close','<path d="M6 6l12 12M18 6 6 18"/>','#FF9A92')+b('Minimise','<path d="M5 12h14"/>','#ECEEF3')+b('Maximise','<path d="M7 7h10v10H7z"/>','#ECEEF3')+'</span>'
def icon(p,s=15): return f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{p}</svg>'
WIFI=icon('<path d="M2 9a15 15 0 0 1 20 0M5 12.5a10 10 0 0 1 14 0M8.5 16a5 5 0 0 1 7 0"/><circle cx="12" cy="19.5" r="1"/>')
BAT='<span aria-hidden="true" style="display: flex; align-items: center; gap: 2px"><span style="width: 22px; height: 11px; border-radius: 3px; border: 1.5px solid #ECEEF3; padding: 1px; box-sizing: border-box"><span style="display: block; width: 78%; height: 100%; border-radius: 1px; background: #ECEEF3"></span></span><span style="width: 2px; height: 4px; border-radius: 1px; background: #ECEEF3"></span></span>'
CC=icon('<rect x="3" y="4" width="18" height="7" rx="3.5"/><circle cx="7.5" cy="7.5" r="1.5"/><rect x="3" y="13" width="18" height="7" rx="3.5"/><circle cx="16.5" cy="16.5" r="1.5"/>')
SRCH=icon('<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/>')
def menubar(app,menus=None,cc_active=False,call=False):
    cc_st='display: flex; align-items: center; padding: 2px 6px; border-radius: 6px; '+('background: rgba(255,255,255,.2)' if cc_active else '')
    priv=(f'<span title="Microphone and camera in use" style="display: flex; align-items: center; gap: 4px; height: 20px; padding: 0 7px; border-radius: 10px; background: #F5A35C; color: #0A0B10">{icon("<rect x=\'9\' y=\'3\' width=\'6\' height=\'11\' rx=\'3\'/><path d=\'M5 11a7 7 0 0 0 14 0\'/>",12)}{icon("<rect x=\'2\' y=\'6\' width=\'14\' height=\'12\' rx=\'2\'/><path d=\'m16 10 6-3v10l-6-3\'/>",12)}</span>') if call else ''
    return f'''<header style="position: absolute; left: 0; right: 0; top: 0; height: 30px; display: flex; align-items: center; gap: 16px; padding: 0 14px; background: rgba(10,12,20,.6); backdrop-filter: blur(30px) saturate(160%); -webkit-backdrop-filter: blur(30px) saturate(160%); font-size: 14px; z-index: 5">
    <span style="display: flex; align-items: center">{mark(16,'#ECEEF3','#ECEEF3','#ECEEF3')}</span>
    <span style="font-weight: 700">{app}</span>
    <span style="flex: 1"></span>
    {priv}
    <span title="Managed and compliant" style="display: flex; align-items: center; color: #8FECE3">{icon('<path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6Z"/><path d="m9 12 2 2 4-4"/>')}</span>
    <span title="Keyboard layout" style="font: 600 12px 'Geist Mono', monospace; padding: 1px 6px; border-radius: 5px; border: 1px solid rgba(255,255,255,.4)">UA</span>
    {BAT}<span style="display: flex">{WIFI}</span><span style="display: flex">{SRCH}</span><span style="{cc_st}">{CC}</span>
    <span style="font-weight: 500">Wed 18 Nov  11:08</span>
  </header>'''
PILL='<span style="font: 600 11px \'Geist Mono\', monospace; padding: 2px 7px; border-radius: 5px; background: rgba(245,163,92,.25); color: #FFD3A8">OFFICIAL-SENSITIVE</span>'
def dock(mag='Chat'):
    apps=[('Files',1),('Mail',1),('Chat',1),('Calendar',0),('Tasks',0),('Drive',0),('Docs',1),('Spaces',0),('Browser',1),('Terminal',0),('Settings',0)]
    out=''
    order=[a for a,_ in apps]; mi=order.index(mag)
    for i,(n,run) in enumerate(apps):
        d=abs(i-mi); s=78 if d==0 else 64 if d==1 else 56
        lab=f'<span style="position: absolute; bottom: calc(100% + 10px); left: 50%; transform: translateX(-50%); padding: 4px 10px; border-radius: 8px; background: rgba(24,27,38,.9); border: 1px solid rgba(255,255,255,.12); font-size: 13px; white-space: nowrap">{n}</span>' if d==0 else ''
        badge='<span style="position: absolute; right: -4px; top: -4px; min-width: 20px; height: 20px; padding: 0 5px; box-sizing: border-box; border-radius: 10px; background: #FF5A50; color: #FFFFFF; font: 700 12px Geist, sans-serif; display: flex; align-items: center; justify-content: center">5</span>' if n=='Chat' else ('<span style="position: absolute; right: -4px; top: -4px; min-width: 20px; height: 20px; padding: 0 5px; box-sizing: border-box; border-radius: 10px; background: #FF5A50; color: #FFFFFF; font: 700 12px Geist, sans-serif; display: flex; align-items: center; justify-content: center">12</span>' if n=='Mail' else '')
        dot=f'<span style="width: 4px; height: 4px; border-radius: 50%; background: {"rgba(255,255,255,.8)" if run else "transparent"}"></span>'
        out+=f'<span title="{n}" style="position: relative; display: flex; flex-direction: column; align-items: center; justify-content: flex-end; gap: 4px">{lab}<span style="position: relative; display: flex">{tile(n,s)}{badge}</span>{dot}</span>'
    out+='<span aria-hidden="true" style="width: 1px; height: 52px; background: rgba(255,255,255,.18); margin: 0 6px 10px"></span>'
    out+='<span title="Downloads" style="display: flex; flex-direction: column; align-items: center; gap: 4px"><span style="position: relative; width: 56px; height: 56px"><span style="position: absolute; left: 10px; top: 4px; width: 40px; height: 48px; border-radius: 6px; background: #FBFBF9; transform: rotate(-8deg); box-shadow: 0 6px 14px rgba(0,0,0,.4)"></span><span style="position: absolute; left: 6px; top: 8px; width: 40px; height: 48px; border-radius: 6px; background: linear-gradient(160deg,#FF9A92,#C2620E); transform: rotate(6deg); box-shadow: 0 6px 14px rgba(0,0,0,.4)"></span></span><span style="width: 4px; height: 4px"></span></span>'
    out+=f'<span title="Trash" style="display: flex; flex-direction: column; align-items: center; gap: 4px">{tile("Trash",56)}<span style="width: 4px; height: 4px"></span></span>'
    return f'<nav aria-label="Dock" style="position: absolute; left: 50%; bottom: 10px; transform: translateX(-50%); display: flex; align-items: flex-end; gap: 8px; padding: 8px 12px 4px; border-radius: 26px; {GLASS}; box-shadow: 0 20px 50px rgba(0,0,0,.45); z-index: 4">{out}</nav>'

# ---------- Desktop ----------

def _mailwin():
    rail=''.join(f'<span title="{n}" style="display: flex; padding: 5px; border-radius: 10px; {"background: rgba(255,255,255,.1)" if n=="Mail" else ""}">{tile(n,26,False)}</span>' for n in ['Mail','Chat','Calendar','Drive','Docs','Tasks'])
    T={'Flood':('rgba(245,163,92,.15)','#F5B57A'),'Team':('rgba(142,162,255,.15)','#A9B6FF'),'Invite':('rgba(79,209,197,.15)','#6FE0D5')}
    rows=''
    for f,i,bg,sub,sn,t,un,tag,sel in [('Anna Kowalska','AK','#F5B57A','Gauge report and updated shelter agreement','Attached is today’s gauge report…','10:42',1,'Flood',1),('River Authority alerts','PA','#9198A8','Gauge at the bridge: 4.2 m','Rising 12 cm per hour…','11:08',1,'',0),('Marek, Ana','MA','#A9B6FF','Shelter capacity sheet','Fill in your district…','09:15',1,'Team',0),('Daniel Price','DP','#6FE0D5','Invitation: hydrology briefing','Thu 16:00 · 45 min','08:30',0,'Invite',0)]:
        tg=f'<span style="font-size: 11px; font-weight: 600; padding: 1px 6px; border-radius: 5px; background: {T[tag][0]}; color: {T[tag][1]}">{tag}</span>' if tag else ''
        st='background: #1A1D27; box-shadow: inset 0 0 0 1px #333846' if sel else ''
        rows+=f'<div style="display: flex; gap: 10px; padding: 10px; border-radius: 12px; {st}"><span style="width: 30px; height: 30px; flex: none; border-radius: 10px; background: {bg}; color: #0A0B10; font-size: 12px; font-weight: 700; display: flex; align-items: center; justify-content: center">{i}</span><span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px"><span style="display: flex; gap: 6px"><span style="flex: 1; font-weight: {600 if un else 400}; white-space: nowrap; overflow: hidden; text-overflow: ellipsis">{f}</span><span style="font: 500 11px Geist Mono, monospace; color: #9198A8">{t}</span></span><span style="font-size: 13px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis">{sub}</span><span style="display: flex; gap: 6px; align-items: center">{tg}<span style="font-size: 12px; color: #9198A8; white-space: nowrap; overflow: hidden; text-overflow: ellipsis">{sn}</span></span></span></div>'
    return f"""<section aria-label="Mail window" style="position: absolute; left: 400px; top: 64px; width: 820px; height: 560px; border-radius: 14px; background: #0A0B10; border: 1px solid rgba(255,255,255,.1); box-shadow: 0 40px 90px rgba(0,0,0,.6); overflow: hidden; display: flex; flex-direction: column; z-index: 2">
    <div style="height: 38px; flex: none; display: flex; align-items: center; gap: 12px; padding: 0 12px; background: #0D0E14; border-bottom: 1px solid #1E2129">{lights()}<span style="flex: 1; text-align: center; font-weight: 600">Ortus Mail</span><span style="height: 24px; padding: 0 10px; border-radius: 8px; background: #13151C; border: 1px solid #262A35; color: #9198A8; display: flex; align-items: center; gap: 6px; font-size: 13px">{SRCH}Search <span style="font: 500 11px Geist Mono, monospace">Ctrl K</span></span></div>
    <div style="flex: 1; min-height: 0; display: flex">
      <nav aria-label="Apps" style="width: 48px; flex: none; padding: 8px 0; display: flex; flex-direction: column; align-items: center; gap: 4px; background: #07080C; border-right: 1px solid #1E2129">{rail}</nav>
      <div style="width: 290px; flex: none; padding: 10px 8px; display: flex; flex-direction: column; gap: 6px">
        <div style="padding: 10px; border-radius: 12px; background: #13151C; border: 1px solid #262A35; display: flex; flex-direction: column; gap: 4px"><span style="font-size: 12px; color: #9198A8"><span style="font-weight: 600; color: {{{{accent}}}}">Catch up</span> · since yesterday</span><span style="font-size: 13px; line-height: 1.45">2 need a reply, 1 invite Thu 14:00.</span></div>
        {rows}
      </div>
      <div style="flex: 1; min-width: 0; margin: 8px 8px 8px 0; padding: 16px 18px; border-radius: 16px; background: #11131A; border: 1px solid #1E2129; display: flex; flex-direction: column; gap: 10px">
        <span style="display: flex; align-items: center; gap: 8px; flex-wrap: wrap"><span style="font-size: 17px; font-weight: 600">Gauge report and updated shelter agreement</span>{PILL}</span>
        <span style="display: flex; gap: 8px; align-items: center; padding: 8px 10px; border-radius: 10px; background: #161922; font-size: 13px; color: #C3C8D4"><span style="font: 500 11px Geist Mono, monospace; color: {{{{accent}}}}">TL;DR</span>Gauge at 4.2 m and rising. Agreement adds the Park Street school.</span>
        <span style="display: flex; gap: 10px; align-items: center"><span style="width: 32px; height: 32px; border-radius: 10px; background: #F5B57A; color: #0A0B10; font-size: 12px; font-weight: 700; display: flex; align-items: center; justify-content: center">AK</span><span style="display: flex; flex-direction: column"><span style="font-weight: 600">Anna Kowalska</span><span style="font-size: 12px; color: #9198A8">to me, finance · <span style="color: #4FD1C5">verified sender</span> · 10:42</span></span></span>
        <span style="line-height: 1.6; color: #D6D9E1">Attached is today’s gauge report and the updated shelter agreement. The only change is the school on Park Street as the second site. I sent a slot for Thursday.</span>
        <span style="display: flex; gap: 10px; align-items: center; padding: 10px; border-radius: 12px; border: 1px solid #333846; background: #161922"><span style="width: 42px; height: 46px; border-radius: 10px; background: #1E2230; display: flex; flex-direction: column; align-items: center; justify-content: center; font-size: 11px; color: {{{{accent}}}}; font-weight: 600">THU<span style="font-size: 17px; color: #ECEEF3; font-weight: 700">19</span></span><span style="flex: 1; display: flex; flex-direction: column"><span style="font-weight: 600">Shelter agreement review with legal</span><span style="font-size: 12px; color: #9198A8">14:00 – 14:30 · you’re free</span></span><span style="height: 28px; padding: 0 12px; border-radius: 9px; background: {{{{accent}}}}; color: #0A0B10; display: flex; align-items: center; font-weight: 600">Accept</span></span>
      </div>
    </div>
  </section>"""
MAILWIN=_mailwin()
mailrows=[('Anna Kowalska','10:42','Gauge report and updated shelter agreement','Attached is today’s gauge report and the…',True),('River Authority alerts','11:08','Gauge at the bridge: 4.2 m','Rising 12 cm per hour',False),('Marek, Ana','09:15','Shelter capacity sheet','Please fill in your district…',False),('Daniel Price','08:30','Invitation: hydrology briefing','Thu 16:00 · 45 min',False),('Ana Ferreira','Tue','Town hall tonight: talking points','Please check the shelter numbers…',False)]
rows=''.join(f'<div style="display: flex; flex-direction: column; gap: 2px; padding: 9px 12px; margin: 0 8px; border-radius: 10px; {"background: {{accent}}; color: #0A0B10" if sel else ""}"><span style="display: flex"><span style="flex: 1; font-weight: 600">{f}</span><span style="font-size: 12px; opacity: .75">{t}</span></span><span style="font-weight: 500">{s}</span><span style="font-size: 13px; opacity: .7; white-space: nowrap; overflow: hidden; text-overflow: ellipsis">{p}</span></div>' for f,t,s,p,sel in mailrows)
side=''.join(f'<span style="display: flex; align-items: center; gap: 8px; padding: 5px 10px; border-radius: 7px; {"background: rgba(255,255,255,.12)" if a else ""}"><span style="width: 8px; height: 8px; border-radius: 3px; background: {c}"></span><span style="flex: 1">{n}</span><span style="font-size: 12px; color: #C3C8D4">{k}</span></span>' for n,c,k,a in [('Inbox','{{accent}}','12',1),('Flagged','#F5A35C','3',0),('Drafts','#9198A8','2',0),('Sent','#9198A8','',0),('Archive','#9198A8','',0)])
desktop=HEAD.format(title='Ortus OS desktop')+f'''<div style="width: 1440px; height: 900px; position: relative; overflow: hidden; {WALL}; color: #ECEEF3; font-family: Geist, system-ui, sans-serif; font-size: 14px">
  <svg aria-hidden="true" width="760" height="760" viewBox="0 0 48 48" style="position: absolute; right: -60px; bottom: -180px; opacity: .07">{MARK.format(a="#FFFFFF",b="#FFFFFF",c="#FFFFFF")}</svg>
  {menubar('Mail',['File','Edit','View','Mailbox','Message','Window','Help'])}

  <aside aria-label="Widgets" style="position: absolute; left: 28px; top: 56px; width: 340px; display: flex; flex-direction: column; gap: 14px">
    <div style="padding: 16px; border-radius: 22px; {GLASS}; display: flex; flex-direction: column; gap: 8px">
      <span style="font: 600 12px Geist, sans-serif; color: #FF9A92; letter-spacing: .04em">WEDNESDAY</span>
      <span style="font-size: 44px; font-weight: 600; line-height: 1">18</span>
      <span style="display: flex; gap: 8px; align-items: center"><span style="width: 3px; height: 30px; border-radius: 2px; background: #4FD1C5"></span><span style="display: flex; flex-direction: column"><span style="font-weight: 600">Call: River Authority</span><span style="color: #C3C8D4">11:30 – 12:00 · in 22 min</span></span></span>
      <span style="display: flex; gap: 8px; align-items: center"><span style="width: 3px; height: 30px; border-radius: 2px; background: {{{{accent}}}}"></span><span style="display: flex; flex-direction: column"><span style="font-weight: 600">Focus: bus plan</span><span style="color: #C3C8D4">15:00 – 16:00</span></span></span>
    </div>
    <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 14px">
      <div style="padding: 14px; border-radius: 22px; {GLASS}; display: flex; flex-direction: column; gap: 6px; aspect-ratio: 1"><span style="font-size: 12px; color: #C3C8D4">Approvals</span><span style="font-size: 34px; font-weight: 600">2</span><span style="font-size: 13px">Review flood plan by 14:00</span></div>
      <div style="padding: 14px; border-radius: 22px; {GLASS}; display: flex; flex-direction: column; gap: 6px; aspect-ratio: 1"><span style="font-size: 12px; color: #C3C8D4">River gauge</span><span style="font-size: 34px; font-weight: 600; color: #FFD3A8">4.2 m</span><svg viewBox="0 0 100 30" style="width: 100%; height: 30px" aria-hidden="true"><path d="M0 26 L20 24 L40 20 L60 15 L80 9 L100 4" fill="none" stroke="#F5A35C" stroke-width="2.5" stroke-linecap="round"/></svg></div>
    </div>
  </aside>

  {MAILWIN}

  <section aria-label="Chat window" style="position: absolute; left: 1010px; top: 420px; width: 410px; height: 350px; border-radius: 14px; background: rgba(18,20,28,.8); backdrop-filter: blur(30px) saturate(160%); border: 1px solid rgba(255,255,255,.12); box-shadow: 0 40px 90px rgba(0,0,0,.6); overflow: hidden; display: flex; flex-direction: column; z-index: 3">
    <div style="height: 46px; display: flex; align-items: center; gap: 12px; padding: 0 14px; border-bottom: 1px solid rgba(255,255,255,.06)">{lights()}<span style="flex: 1; text-align: center; font-weight: 600; white-space: nowrap">#flood-response</span>{PILL}</div>
    <div style="flex: 1; padding: 14px; display: flex; flex-direction: column; gap: 10px; justify-content: flex-end">
      <span style="font-size: 12px; color: #C3C8D4">Anna · Regional</span>
      <span style="align-self: flex-start; max-width: 78%; padding: 8px 12px; border-radius: 18px 18px 18px 6px; background: rgba(255,255,255,.1)">Gauge at 4.2 m and rising. Close R-12?</span>
      <span style="align-self: flex-end; max-width: 78%; padding: 8px 12px; border-radius: 18px 18px 6px 18px; background: {{{{accent}}}}; color: #0A0B10">Agreed, closing at 11:30.</span>
      <span style="font-size: 12px; color: #C3C8D4">Jonas · Police</span>
      <span style="align-self: flex-start; max-width: 78%; padding: 8px 12px; border-radius: 18px 18px 18px 6px; background: rgba(255,255,255,.1)">Two units on the way 🚓</span>
    </div>
    <div style="margin: 0 12px 12px; height: 34px; border-radius: 17px; background: rgba(255,255,255,.08); display: flex; align-items: center; padding: 0 14px; color: #C3C8D4">Message</div>
  </section>

  <div role="status" style="position: absolute; right: 14px; top: 42px; width: 340px; padding: 12px 14px; border-radius: 18px; {GLASS}; box-shadow: 0 16px 40px rgba(0,0,0,.45); display: flex; gap: 12px; z-index: 6">
    {tile('Approvals',38)}
    <span style="flex: 1; display: flex; flex-direction: column; gap: 2px"><span style="display: flex"><span style="flex: 1; font-weight: 600">Approvals</span><span style="font-size: 12px; color: #C3C8D4">now</span></span><span style="font-weight: 500">Review: Flood response plan v12</span><span style="color: #C3C8D4">Due 14:00 · open in Ortus Docs</span></span>
  </div>

  {dock('Chat')}
</div>
'''+FOOT.replace("$preview\":{\"width\":1440,\"height\":900}","$preview\":{\"width\":1440,\"height\":900}")
desktop=desktop.replace('🚓','')
open(D+'OSDesktop.dc.html','w').write(desktop)

# ---------- Settings ----------
def sbi(n,c,glyph,active=False):
    st='display: flex; align-items: center; gap: 9px; padding: 5px 8px; border-radius: 7px; '+('background: {{accent}}; color: #0A0B10; font-weight: 600' if active else '')
    return f'<span style="{st}"><span style="width: 22px; height: 22px; border-radius: 6px; background: {c}; color: #FFFFFF; display: flex; align-items: center; justify-content: center">{icon(glyph,13)}</span>{n}</span>'
items=[('Wi-Fi','#3B82F6','<path d="M2 9a15 15 0 0 1 20 0M5 12.5a10 10 0 0 1 14 0M8.5 16a5 5 0 0 1 7 0"/>'),('Bluetooth','#3B82F6','<path d="m7 7 10 10-5 5V2l5 5L7 17"/>'),('Network','#3B82F6','<circle cx="12" cy="12" r="9"/><path d="M3 12h18"/>'),(None,None,None),('Notifications','#EF4444','<path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9"/>'),('Sound','#EC4899','<path d="M11 5 6 9H2v6h4l5 4V5Z"/>'),('Focus','#6366F1','<path d="M12 3a9 9 0 1 0 9 9 7 7 0 0 1-9-9Z"/>'),(None,None,None),('Appearance','#334155','<circle cx="12" cy="12" r="9"/><path d="M12 3v18"/>'),('Displays & GPU','#0EA5E9','<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8"/>'),('Wallpaper','#14B8A6','<rect x="3" y="4" width="18" height="16" rx="2"/><path d="m3 16 5-5 4 4 3-3 6 6"/>'),('Accessibility','#2563EB','<circle cx="12" cy="5" r="2"/><path d="M5 9h14M12 9v12M8 21l4-7 4 7"/>'),(None,None,None),('Privacy & Security','#4F46E5','<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>'),('Updates','#64748B','<path d="M21 12a9 9 0 1 1-3-6.7L21 8"/><path d="M21 3v5h-5"/>'),('Device management','#0F766E','<path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6Z"/>'),('Sign-in & passkeys','#7C3AED','<circle cx="8" cy="12" r="4"/><path d="M12 12h10M18 12v3"/>')]
sb=''
for n,c,g in items:
    sb+= '<span style="height: 10px"></span>' if n is None else sbi(n,c,g,n=='Privacy & Security')
def sw(on): return f'<span aria-hidden="true" style="width: 38px; height: 22px; border-radius: 11px; position: relative; background: {"{{accent}}" if on else "rgba(255,255,255,.2)"}"><span style="position: absolute; top: 2px; left: {"18px" if on else "2px"}; width: 18px; height: 18px; border-radius: 50%; background: #0A0B10; box-shadow: 0 1px 3px rgba(0,0,0,.3)"></span></span>'
def group(title,rows):
    r=''.join(f'<div style="display: flex; align-items: center; gap: 12px; padding: 10px 14px; {"border-top: 1px solid rgba(255,255,255,.07)" if i else ""}"><span style="flex: 1; display: flex; flex-direction: column"><span>{a}</span>{f"<span style=\"font-size: 13px; color: #C3C8D4\">{b}</span>" if b else ""}</span>{c}</div>' for i,(a,b,c) in enumerate(rows))
    t=f'<span style="font-size: 13px; font-weight: 600; color: #C3C8D4; padding: 0 6px">{title}</span>' if title else ''
    return f'<div style="display: flex; flex-direction: column; gap: 6px">{t}<div style="border-radius: 12px; background: rgba(255,255,255,.05); border: 1px solid rgba(255,255,255,.06)">{r}</div></div>'
ok=lambda t: f'<span style="color: #8FECE3; font-size: 14px">{t}</span>'
mute=lambda t: f'<span style="color: #C3C8D4; font-size: 14px">{t}</span>'
btn=lambda t,p=False: f'<span style="height: 26px; padding: 0 12px; border-radius: 7px; display: flex; align-items: center; font-weight: 500; {"background: {{accent}}; color: #0A0B10" if p else "background: rgba(255,255,255,.12)"}">{t}</span>'
pane=f'''<div style="display: flex; align-items: center; gap: 14px; padding: 16px; border-radius: 14px; background: linear-gradient(135deg, rgba(79,209,197,.18), rgba(110,134,255,.12)); border: 1px solid rgba(79,209,197,.3)">
  <span style="width: 52px; height: 52px; border-radius: 16px; background: rgba(79,209,197,.25); color: #8FECE3; display: flex; align-items: center; justify-content: center">{icon('<path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6Z"/><path d="m9 12 2 2 4-4"/>',26)}</span>
  <span style="flex: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 16px; font-weight: 600">This Mac-class laptop is protected</span><span style="color: #C3C8D4">Boot measured and verified 2 min ago · managed by Ministry of [Name]</span></span>{btn('What can IT see?')}</div>'''.replace('This Mac-class laptop is protected','This device is protected')
pane+=group('Software update',[('Ortus OS 1.4.3 is ready','Installs in about 20 seconds on restart · 1.4.2 kept for rollback',f'<span style="display: flex; gap: 6px">{btn("Tonight")}{btn("Restart now",True)}</span>')])
pane+=group('Startup security',[('Secure Boot','Ortus signing keys',ok('On')),('Disk encryption','Unlocked by security chip + PIN',ok('On')),('System files','Read-only and verified',ok('Verified'))])
pane+=group('Sign-in',[('Phone sign-in (QR)','iPhone · Olena’s phone',mute('Primary')),('Smart card / eID','',ok('Enrolled')),('Security key','',btn('Add…')),('Lock when phone is away','Bluetooth, about 5 m',sw(True))])
settings=HEAD.format(title='Ortus OS settings')+f'''<div style="width: 1440px; height: 900px; position: relative; overflow: hidden; {WALL}; color: #ECEEF3; font-family: Geist, system-ui, sans-serif; font-size: 14px">
  {menubar('Settings',['File','Edit','View','Window','Help'])}
  <section aria-label="Settings window" style="position: absolute; left: 50%; top: 60px; transform: translateX(-50%); width: 980px; height: 780px; border-radius: 16px; background: rgba(18,20,28,.93); border: 1px solid rgba(255,255,255,.1); box-shadow: 0 40px 100px rgba(0,0,0,.6); overflow: hidden; display: flex">
    <nav aria-label="Settings sections" style="width: 260px; padding: 14px 10px; background: rgba(40,44,60,.55); backdrop-filter: blur(30px); border-right: 1px solid rgba(255,255,255,.06); display: flex; flex-direction: column; gap: 2px">
      <span style="padding: 0 6px 14px">{lights()}</span>
      <span style="display: flex; align-items: center; gap: 8px; height: 28px; padding: 0 10px; margin-bottom: 10px; border-radius: 7px; background: rgba(255,255,255,.08); color: #C3C8D4">{SRCH}Search</span>
      <span style="display: flex; align-items: center; gap: 10px; padding: 8px; border-radius: 10px; margin-bottom: 8px"><span style="width: 40px; height: 40px; border-radius: 50%; background: linear-gradient(135deg,#A9B6FF,#6E86FF); color: #0A0B10; display: flex; align-items: center; justify-content: center; font-weight: 700">OH</span><span style="display: flex; flex-direction: column"><span style="font-weight: 600">Olena Hrytsenko</span><span style="font-size: 12px; color: #C3C8D4">Ortus account · Ministry</span></span></span>
      {sb}
    </nav>
    <main style="flex: 1; display: flex; flex-direction: column">
      <div style="height: 52px; display: flex; align-items: center; gap: 12px; padding: 0 20px; border-bottom: 1px solid rgba(255,255,255,.06)"><span style="color: #C3C8D4">‹ ›</span><span style="font-size: 15px; font-weight: 700">Privacy & Security</span></div>
      <div style="flex: 1; padding: 20px 26px; display: flex; flex-direction: column; gap: 18px; overflow: hidden">{pane}</div>
    </main>
  </section>
</div>
'''+FOOT
open(D+'OSSecurity.dc.html','w').write(settings)

# ---------- Control centre + search ----------
tiles_html=f'''<div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 10px">
  <div style="grid-column: span 2; grid-row: span 2; padding: 12px; border-radius: 18px; background: rgba(255,255,255,.08); display: flex; flex-direction: column; gap: 10px">
    {''.join(f'<span style="display: flex; align-items: center; gap: 10px"><span style="width: 32px; height: 32px; border-radius: 50%; background: {bg}; color: {fg}; display: flex; align-items: center; justify-content: center">{icon(g,15)}</span><span style="display: flex; flex-direction: column"><span style="font-weight: 600">{n}</span><span style="font-size: 12px; color: #C3C8D4">{s}</span></span></span>' for n,s,g,bg,fg in [('Wi-Fi','GOV-LAN','<path d="M2 9a15 15 0 0 1 20 0M5 12.5a10 10 0 0 1 14 0M8.5 16a5 5 0 0 1 7 0"/>','#3B82F6','#FFFFFF'),('Bluetooth','Phone nearby','<path d="m7 7 10 10-5 5V2l5 5L7 17"/>','#3B82F6','#FFFFFF'),('VPN','Off · on GOV-LAN','<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>','rgba(255,255,255,.15)','#ECEEF3')])}
  </div>
  <div style="grid-column: span 2; padding: 12px; border-radius: 18px; background: rgba(255,255,255,.08); display: flex; align-items: center; gap: 10px"><span style="width: 32px; height: 32px; border-radius: 50%; background: #6366F1; color: #FFFFFF; display: flex; align-items: center; justify-content: center">{icon('<path d="M12 3a9 9 0 1 0 9 9 7 7 0 0 1-9-9Z"/>',15)}</span><span style="display: flex; flex-direction: column"><span style="font-weight: 600">Focus</span><span style="font-size: 12px; color: #C3C8D4">Until 12:00</span></span></div>
  <div style="padding: 12px; border-radius: 18px; background: rgba(255,255,255,.08); display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 4px; font-size: 12px; text-align: center">{icon('<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8"/>',18)}Screen share</div>
  <div style="padding: 12px; border-radius: 18px; background: rgba(255,255,255,.08); display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 4px; font-size: 12px; text-align: center">{icon('<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>',18)}Lock</div>
  <div style="grid-column: span 4; padding: 12px 14px; border-radius: 18px; background: rgba(255,255,255,.08); display: flex; flex-direction: column; gap: 8px"><span style="font-weight: 600">Display</span><span style="height: 24px; border-radius: 12px; background: rgba(255,255,255,.12); overflow: hidden; display: flex"><span style="width: 70%; background: #ECEEF3; display: flex; align-items: center; padding-left: 8px; color: #0A0B10">{icon('<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2"/>',13)}</span></span></div>
  <div style="grid-column: span 4; padding: 12px 14px; border-radius: 18px; background: rgba(255,255,255,.08); display: flex; flex-direction: column; gap: 8px"><span style="font-weight: 600">Sound</span><span style="height: 24px; border-radius: 12px; background: rgba(255,255,255,.12); overflow: hidden; display: flex"><span style="width: 45%; background: #ECEEF3; display: flex; align-items: center; padding-left: 8px; color: #0A0B10">{icon('<path d="M11 5 6 9H2v6h4l5 4V5Z"/>',13)}</span></span></div>
  <div style="grid-column: span 4; padding: 12px 14px; border-radius: 18px; background: rgba(79,209,197,.14); border: 1px solid rgba(79,209,197,.3); display: flex; align-items: center; gap: 12px">{tile('Calls',34,False)}<span style="flex: 1; display: flex; flex-direction: column"><span style="font-weight: 600">In call · #flood-response</span><span style="font-size: 12px; color: #C3C8D4">6 people · 24:13 · mic on</span></span><span style="height: 28px; padding: 0 12px; border-radius: 14px; background: #FF5A50; color: #FFFFFF; display: flex; align-items: center; font-weight: 600">Leave</span></div>
  <div style="grid-column: span 4; padding: 10px 14px; border-radius: 18px; background: rgba(255,255,255,.06); display: flex; align-items: center; gap: 8px; font-size: 13px; color: #C3C8D4"><span style="color: #8FECE3; display: flex">{icon('<path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6Z"/>',14)}</span>Managed by Ministry of [Name] · compliant · label OFFICIAL-SENSITIVE</div>
</div>'''
results=[('Docs','Flood response plan 2026','Ortus Docs · edited 2 min ago',True),('Mail','Gauge report and updated shelter agreement','Mail · Anna Kowalska',False),('Chat','#flood-response-2026','Chat · 3 unread',False),('Calendar','Shelter agreement review with legal','Thu 19 Nov · 14:00',False),('Records','Case 2026/EM/0114','Records · Flood response',False)]
res=''.join(f'<div style="display: flex; align-items: center; gap: 12px; padding: 8px 12px; border-radius: 10px; {"background: {{accent}}; color: #0A0B10" if sel else ""}">{tile(n,32,False)}<span style="flex: 1; display: flex; flex-direction: column"><span style="font-weight: 600">{t}</span><span style="font-size: 13px; {"opacity: .75" if sel else "color: #C3C8D4"}">{m}</span></span>{"<span style=\"font: 500 12px Geist Mono, monospace\">↵ open</span>" if sel else ""}</div>' for n,t,m,sel in results)
control=HEAD.format(title='Ortus OS control centre and search')+f'''<div style="width: 1440px; height: 900px; position: relative; overflow: hidden; {WALL}; color: #ECEEF3; font-family: Geist, system-ui, sans-serif; font-size: 14px">
  {menubar('Finder-free desktop',None,True,True).replace('Finder-free desktop','Files')}
  <div aria-hidden="true" style="position: absolute; inset: 30px 0 0 0; background: rgba(7,8,12,.25)"></div>
  <section role="dialog" aria-label="Ortus search" style="position: absolute; left: 50%; top: 170px; transform: translateX(-50%); width: 680px; border-radius: 22px; {GLASS}; background: rgba(24,27,38,.75); box-shadow: 0 40px 100px rgba(0,0,0,.55); overflow: hidden; z-index: 4">
    <div style="display: flex; align-items: center; gap: 12px; padding: 16px 20px; border-bottom: 1px solid rgba(255,255,255,.08)"><span style="display: flex; color: #C3C8D4">{icon('<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/>',22)}</span><span style="flex: 1; font-size: 22px; font-weight: 500">flood plan<span style="display: inline-block; width: 2px; height: 22px; margin-left: 2px; vertical-align: middle; background: {{{{accent}}}}"></span></span>{mark(22)}</div>
    <div style="padding: 8px; display: flex; flex-direction: column; gap: 2px">
      <span style="font-size: 12px; font-weight: 600; color: #C3C8D4; padding: 6px 12px">TOP HITS · ACROSS ALL APPS</span>
      {res}
      <span style="font-size: 12px; font-weight: 600; color: #C3C8D4; padding: 10px 12px 6px">ACTIONS</span>
      <div style="display: flex; gap: 8px; padding: 0 12px 10px; flex-wrap: wrap"><span style="height: 30px; padding: 0 12px; border-radius: 15px; background: rgba(255,255,255,.1); display: flex; align-items: center">Review the plan</span><span style="height: 30px; padding: 0 12px; border-radius: 15px; background: rgba(255,255,255,.1); display: flex; align-items: center">Share with #flood-response</span><span style="height: 30px; padding: 0 12px; border-radius: 15px; background: rgba(255,255,255,.1); display: flex; align-items: center">Summarise changes</span></div>
    </div>
  </section>
  <section aria-label="Control centre" style="position: absolute; right: 12px; top: 38px; width: 330px; padding: 12px; border-radius: 24px; {GLASS}; background: rgba(24,27,38,.7); box-shadow: 0 30px 80px rgba(0,0,0,.5); z-index: 5">{tiles_html}</section>
  {dock('Docs')}
</div>
'''+FOOT
open(D+'OSControl.dc.html','w').write(control)

c=json.load(open(D+'canvas.json'))
c['boards']['OSControl.dc.html']={"x":0,"y":19980,"w":1440,"h":900,"title":"Ortus OS · Search & control centre"}
if 'OSControl.dc.html' not in c['order']: c['order'].append('OSControl.dc.html')
c['boards']['OSSecurity.dc.html']['title']='Ortus OS · Settings: privacy & security'
c['notes']['osLook']={"x":1520,"y":19980,"w":440,"size":"m","fill":"purple","text":"Ortus OS look\n• Global menu bar (app menus left, status right) with classification + managed shield\n• Windows: traffic-light controls, frosted sidebars, unified toolbars\n• Dock: glass, magnifies on hover, running dots, badges, stacks + trash\n• Widgets on the desktop: agenda, approvals, live data\n• Ortus Search (⌘Space): one box for apps, files, mail, chat, records + actions\n• Control centre: Wi-Fi, Bluetooth/phone, Focus, sliders, live call, compliance\n• All blur/glass is GPU-composited in the Rust compositor (wgpu)"}
json.dump(c,open(D+'canvas.json','w'),ensure_ascii=False)
print('ok')
