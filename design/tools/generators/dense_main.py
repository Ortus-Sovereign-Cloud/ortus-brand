import re
P='/tmp/claude-1002/-home-bohdaq-git/6b5adcb0-31d6-44c8-b201-55c34d7527ea/scratchpad/mailui/project/'
def edit(name,reps):
    s=open(P+name).read()
    assert '/*dense2*/' not in s, name
    for a,b,*n in reps:
        n=n[0] if n else 1
        assert s.count(a)==n,(name,a[:60],s.count(a))
        s=s.replace(a,b)
    s=s.replace('/*type2*/','/*type2*//*dense2*/')
    open(P+name,'w').write(s)
MONO12="font: 500 12px 'Geist Mono', monospace"
T13="font-size: 13px; font-variant-numeric: tabular-nums"
edit('Main.dc.html',[
 ('''      <span style="font-size: 13px; color: #9198A8">workspace</span>\n''',''),
 ('''    <span style="display: flex; align-items: center; gap: 6px; font-size: 13px; color: #9198A8"><span style="width: 7px; height: 7px; border-radius: 50%; background: #4FD1C5; box-shadow: 0 0 0 3px rgba(79,209,197,.18)"></span>Live</span>\n''',''),
 ('''    <button aria-label="Account" style="width: 36px; height: 36px; border-radius: 50%; border: 1px solid #333846; background: #1B1E27; color: #ECEEF3; font: 600 13px Geist, sans-serif">OH</button>\n''',''),
 ('padding: 12px 16px; border-bottom: 1px solid #1E2129; flex-wrap: wrap','padding: 14px 24px; border-bottom: 1px solid #1E2129; flex-wrap: wrap'),
 ('max-width: 236px; padding: 14px 10px; display: flex; flex-direction: column; gap: 2px','max-width: 236px; padding: 20px 12px; display: flex; flex-direction: column; gap: 4px'),
 ('''        New message <kbd style="font: 500 12px 'Geist Mono', monospace; opacity: .7">C</kbd>''','        New message'),
 ('margin-bottom: 14px">\n        New message','margin-bottom: 16px">\n        New message'),
 ('font-size: 12px; font-weight: 600; color: #9198A8; padding: 18px 12px 6px; letter-spacing: .08em; text-transform: uppercase','font-size: 13px; font-weight: 500; color: #9198A8; padding: 24px 12px 8px'),
 ('height: 34px; padding: 0 12px; border-radius: 10px; color: #ECEEF3; text-decoration: none"><span style="width: 8px','height: 40px; padding: 0 12px; border-radius: 10px; color: #ECEEF3; text-decoration: none"><span style="width: 8px'),
 ("justify-content: space-between; height: 36px; padding: 0 12px;","justify-content: space-between; height: 40px; padding: 0 12px;"),
 ('max-width: 420px; padding: 14px 8px; display: flex; flex-direction: column; gap: 10px','max-width: 420px; padding: 20px 8px; display: flex; flex-direction: column; gap: 16px'),
 ('<div style="padding: 14px; border-radius: 16px; background: #13151C; border: 1px solid #262A35; display: flex; flex-direction: column; gap: 8px">','<div style="padding: 16px 20px; border-radius: 16px; background: #13151C; border: 1px solid #262A35; display: flex; flex-direction: column; gap: 10px">'),
 ('''<div style="display: flex; gap: 6px"><button style="height: 30px; padding: 0 10px; border-radius: 8px; border: 1px solid #333846; background: transparent; color: #ECEEF3; font: 500 13px Geist, sans-serif">Show the 3</button><button style="height: 30px; padding: 0 10px; border-radius: 8px; border: 1px solid #333846; background: transparent; color: #ECEEF3; font: 500 13px Geist, sans-serif">Archive the rest</button></div>''','''<div><button style="height: 36px; padding: 0 14px; border-radius: 10px; border: 1px solid #333846; background: transparent; color: #ECEEF3; font: 500 14px Geist, sans-serif">Show the 3</button></div>'''),
 ('height: 30px; padding: 0 12px; border-radius: 8px; border: 0;','height: 36px; padding: 0 14px; border-radius: 10px; border: 0;',3),
 ('<div style="display: flex; flex-direction: column; gap: 2px">\n        <sc-for list="{{messages}}"','<div style="display: flex; flex-direction: column; gap: 4px">\n        <sc-for list="{{messages}}"'),
 ('width: 34px; height: 34px; flex: none; border-radius: 11px; background: {{m.bg}}','width: 40px; height: 40px; flex: none; border-radius: 13px; background: {{m.bg}}'),
 ('<div style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 3px">\n              <div style="display: flex; align-items: baseline; gap: 8px">','<div style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 4px">\n              <div style="display: flex; align-items: baseline; gap: 8px">'),
 ('''<span style="font: 500 12px 'Geist Mono', monospace; color: #9198A8">{{m.time}}</span>''','<span style="'+T13+'; color: #9198A8">{{m.time}}</span>'),
 ('''              <span style="{{m.subjStyle}}">{{m.subject}}</span>
              <div style="display: flex; gap: 6px; align-items: center">
                <sc-if value="{{m.tag}}" hint-placeholder-val="{{ false }}"><span style="font-size: 12px; font-weight: 600; padding: 2px 7px; border-radius: 6px; background: {{m.tagBg}}; color: {{m.tagFg}}">{{m.tag}}</span></sc-if>
                <span style="flex: 1; min-width: 0; color: #9198A8; font-size: 14px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis">{{m.snippet}}</span>
              </div>''','''              <div style="display: flex; gap: 8px; align-items: center">
                <span style="{{m.subjStyle}}">{{m.subject}}</span>
                <sc-if value="{{m.tag}}" hint-placeholder-val="{{ false }}"><span style="flex: none; font-size: 13px; font-weight: 500; padding: 2px 8px; border-radius: 7px; background: {{m.tagBg}}; color: {{m.tagFg}}">{{m.tag}}</span></sc-if>
              </div>'''),
 ("rowStyle: 'display: flex; gap: 12px; padding: 12px; border-radius: 14px;","rowStyle: 'display: flex; align-items: center; gap: 14px; padding: 14px 16px; border-radius: 14px;"),
 ("subjStyle: 'white-space: nowrap;","subjStyle: 'flex: 1; min-width: 0; white-space: nowrap;"),
 ('margin: 14px 8px; padding: 22px 26px; border-radius: 20px; background: #11131A; border: 1px solid #1E2129; display: flex; flex-direction: column; gap: 16px','margin: 20px 8px; padding: 32px; border-radius: 20px; background: #11131A; border: 1px solid #1E2129; display: flex; flex-direction: column; gap: 24px'),
 ('font-size: 12px; font-weight: 600; padding: 2px 7px; border-radius: 6px; background: rgba(245,163,92,.15); color: #F5B57A">Flood','font-size: 13px; font-weight: 500; padding: 2px 8px; border-radius: 7px; background: rgba(245,163,92,.15); color: #F5B57A">Flood'),
 ('width: 38px; height: 38px; border-radius: 10px; border: 1px solid #262A35','width: 40px; height: 40px; border-radius: 12px; border: 1px solid #262A35',3),
 ('gap: 10px; padding: 10px 14px; border-radius: 12px; background: #161922; font-size: 14px; color: #C3C8D4">','gap: 14px; padding: 14px 18px; border-radius: 14px; background: #161922; font-size: 14px; line-height: 1.5; color: #C3C8D4">'),
 ('''<span style="font: 500 12px 'Geist Mono', monospace; color: {{accent}}">TL;DR</span>''','<span style="flex: none; font-size: 13px; font-weight: 600; color: {{accent}}">Summary</span>'),
 ('<div style="display: flex; flex-direction: column; gap: 14px">\n        <div style="display: flex; align-items: center; gap: 12px">','<div style="display: flex; flex-direction: column; gap: 20px">\n        <div style="display: flex; align-items: center; gap: 12px">'),
 ('width: 38px; height: 38px; border-radius: 12px; background: #F5B57A','width: 40px; height: 40px; border-radius: 13px; background: #F5B57A'),
 ('''<span style="font: 500 12px 'Geist Mono', monospace; color: #9198A8">10:42</span>''','<span style="'+T13+'; color: #9198A8">10:42</span>'),
 ('gap: 14px; padding: 14px; border-radius: 14px; border: 1px solid #333846; background: #161922; flex-wrap: wrap','gap: 16px; padding: 18px 20px; border-radius: 16px; border: 1px solid #333846; background: #161922; flex-wrap: wrap'),
 ('<span style="font-size: 12px; color: {{accent}}; font-weight: 600">THU</span>','<span style="font-size: 13px; color: {{accent}}; font-weight: 600">Thu</span>'),
 ('<button style="height: 36px; padding: 0 14px; border-radius: 10px; border: 0; background: {{accent}}; color: #0A0B10; font: 600 14px Geist, sans-serif">Accept</button>','<button style="height: 40px; padding: 0 18px; border-radius: 12px; border: 0; background: {{accent}}; color: #0A0B10; font: 600 14px Geist, sans-serif">Accept</button>'),
 ('<button style="height: 36px; padding: 0 12px; border-radius: 10px; border: 1px solid #333846; background: transparent; color: #ECEEF3; font: 500 14px Geist, sans-serif">','<button style="height: 40px; padding: 0 16px; border-radius: 12px; border: 1px solid #333846; background: transparent; color: #ECEEF3; font: 500 14px Geist, sans-serif">',2),
 ('gap: 10px; padding: 8px 12px 8px 8px; border-radius: 12px; background: #161922','gap: 12px; padding: 10px 16px 10px 10px; border-radius: 14px; background: #161922',2),
 ("font: 600 12px 'Geist Mono', monospace; display: flex; align-items: center; justify-content: center\">PDF","font: 600 12px Geist, sans-serif; display: flex; align-items: center; justify-content: center\">PDF"),
 ("font: 600 12px 'Geist Mono', monospace; display: flex; align-items: center; justify-content: center\">DOC","font: 600 12px Geist, sans-serif; display: flex; align-items: center; justify-content: center\">DOC"),
 ('<span style="font-size: 12px; color: #9198A8">212 KB</span>','<span style="font-size: 13px; color: #9198A8">212 KB</span>'),
 ('<span style="font-size: 12px; color: #9198A8">48 KB</span>','<span style="font-size: 13px; color: #9198A8">48 KB</span>'),
 ('gap: 10px; padding: 8px 8px 8px 16px; border-radius: 14px; background: #161922; border: 1px solid #333846">','gap: 10px; padding: 10px 10px 10px 20px; border-radius: 16px; background: #161922; border: 1px solid #333846">'),
 ('''        <kbd style="font: 500 12px 'Geist Mono', monospace; color: #9198A8">R</kbd>\n''',''),
 ('<button aria-label="Send" style="width: 36px; height: 36px; border-radius: 10px;','<button aria-label="Send" style="width: 40px; height: 40px; border-radius: 12px;'),
 ('max-width: 280px; padding: 14px 16px 14px 8px; display: flex; flex-direction: column; gap: 10px','max-width: 280px; padding: 20px 24px 20px 8px; display: flex; flex-direction: column; gap: 12px'),
 ('''<span style="font: 500 12px 'Geist Mono', monospace; color: #9198A8">WED 18 NOV</span>''','<span style="font-size: 13px; color: #9198A8">Wed 18 Nov</span>'),
 ('''<span style="font: 500 12px 'Geist Mono', monospace; color: #9198A8">{{e.time}}</span>''','<span style="'+T13+'; color: #9198A8">{{e.time}}</span>'),
 ('''          <span style="font-size: 13px; color: #9198A8">{{e.meta}}</span>\n''',''),
 ("gap: 3px; padding: 10px 12px; border-radius: 12px; ' + (e.now","gap: 4px; padding: 14px 16px; border-radius: 14px; ' + (e.now"),
])
s=open(P+'Main.dc.html').read()
a=s.index('      <a href="WebAppointments.dc.html" style="margin-top: 6px'); b=s.index('</a>',a)+5
s=s[:a]+s[b:]
open(P+'Main.dc.html','w').write(s)
