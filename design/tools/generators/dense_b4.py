import sys; sys.path.insert(0,'/tmp/claude-1002/-home-bohdaq-git/6b5adcb0-31d6-44c8-b201-55c34d7527ea/scratchpad/gen')
from dense_lib import edit
edit('WebTasks',[
 ('gap: 12px; padding: 12px 16px; border-bottom: 1px solid #1E2129; flex-wrap: wrap','gap: 14px; padding: 14px 24px; border-bottom: 1px solid #1E2129; flex-wrap: wrap'),
 ('display: flex; gap: 2px; padding: 3px; border-radius: 10px; background: #13151C','margin-left: 8px; display: flex; gap: 2px; padding: 4px; border-radius: 12px; background: #13151C'),
 ('height: 28px; padding: 0 10px; border-radius: 7px; border: 0; background: #1E2230; color: #ECEEF3; font: 600 13px','height: 32px; padding: 0 14px; border-radius: 9px; border: 0; background: #1E2230; color: #ECEEF3; font: 600 14px'),
 ('height: 28px; padding: 0 10px; border-radius: 7px; border: 0; background: transparent; color: #9198A8; font: 500 13px','height: 32px; padding: 0 14px; border-radius: 9px; border: 0; background: transparent; color: #9198A8; font: 500 14px',3),
 ('height: 36px; padding: 0 14px; border-radius: 10px; border: 0; background: {{accent}}','height: 40px; padding: 0 18px; border-radius: 12px; border: 0; background: {{accent}}'),
 ('<div style="flex: 1; padding: 16px; overflow-x: auto">','<div style="flex: 1; padding: 24px; overflow-x: auto">'),
 ('min-width: 1100px; display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 12px','min-width: 1100px; display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 16px'),
 ('<section style="padding: 12px; border-radius: 18px; background: #0F1117; border: 1px solid #1E2129; display: flex; flex-direction: column; gap: 10px">','<section style="padding: 16px; border-radius: 18px; background: #0F1117; border: 1px solid #1E2129; display: flex; flex-direction: column; gap: 12px">'),
 ('gap: 8px; padding: 0 4px"><span style="width: 8px; height: 8px; border-radius: 50%; background: {{col.c}}"></span>','gap: 10px; padding: 4px 4px 4px"><span style="width: 8px; height: 8px; border-radius: 50%; background: {{col.c}}"></span>'),
 ('''<span style="font: 500 12px 'Geist Mono', monospace; color: #9198A8">{{col.n}}</span>''','<span style="font-size: 13px; color: #9198A8">{{col.n}}</span>'),
 ('<a href="#" style="padding: 12px; border-radius: 14px; background: #161922; border: 1px solid #262A35; text-decoration: none; color: #ECEEF3; display: flex; flex-direction: column; gap: 8px">','<a href="#" style="padding: 16px; border-radius: 14px; background: #161922; border: 1px solid #262A35; text-decoration: none; color: #ECEEF3; display: flex; flex-direction: column; gap: 12px">'),
 ('''              <sc-if value="{{t.src}}" hint-placeholder-val="{{ false }}"><span style="font-size: 13px; color: {{accent}}">{{t.src}}</span></sc-if>\n''',''),
 ('gap: 8px"><span style="width: 22px; height: 22px; border-radius: 7px; background: {{t.bg}}; color: #0A0B10; font-size: 11px;','gap: 10px"><span style="width: 28px; height: 28px; border-radius: 9px; background: {{t.bg}}; color: #0A0B10; font-size: 11px;'),
 ('''<span style="font: 500 12px 'Geist Mono', monospace; color: #9198A8">{{t.sub}}</span>''','<span style="font-size: 13px; font-variant-numeric: tabular-nums; color: #9198A8">{{t.sub}}</span>'),
 ("'font: 500 12px Geist Mono, monospace; color: ' + (d.startsWith('OVERDUE') ? '#FF9A92' : d === 'TODAY' ?","'font-size: 13px; font-weight: 500; color: ' + (d.startsWith('Overdue') ? '#FF9A92' : d === 'Today' ?"),
 ("'FRI'","'Fri'"),("'TODAY'","'Today'",3),("'MON'","'Mon'",3),("'OVERDUE 1 d'","'Overdue 1 day'"),("'THU'","'Thu'"),
 ("'0/3'","'0 of 3'"),("'2/4'","'2 of 4'"),("'3/5'","'3 of 5'"),
])
