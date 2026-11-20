import sys; sys.path.insert(0,'/tmp/claude-1002/-home-bohdaq-git/6b5adcb0-31d6-44c8-b201-55c34d7527ea/scratchpad/gen')
from dense_lib import edit
edit('AppSwitcher',[('position: absolute; right: 22px; top: 12px; width: 8px','position: absolute; left: calc(50% + 20px); top: 10px; width: 8px',6)])
M="font: 500 12px 'Geist Mono', monospace"
edit('WebWelcome',[
 ('<span style="'+M+'; color: #A4ABBA">WEDNESDAY 18 NOVEMBER · YOUR FIRST DAY</span>','<span style="font-size: 14px; color: #A4ABBA">Wednesday 18 November · your first day</span>'),
 ('<span style="'+M+'; color: #6FE0D5">DONE</span>','<span style="font-size: 13px; font-weight: 600; color: #6FE0D5">Done</span>'),
 ('<span style="'+M+'; color: {{accent}}">STEP 2</span>','<span style="font-size: 13px; font-weight: 600; color: {{accent}}">Step 2</span>'),
 ('<span style="'+M+'; color: {{accent}}">STEP 3</span>','<span style="font-size: 13px; font-weight: 600; color: {{accent}}">Step 3</span>'),
 ('<span style="'+M+'; color: #A4ABBA">YOUR PEOPLE</span>','<span style="font-size: 14px; font-weight: 500; color: #A4ABBA">Your people</span>'),
 ('padding: 36px 24px; box-sizing: border-box; display: flex; flex-direction: column; gap: 26px','padding: 48px 32px; box-sizing: border-box; display: flex; flex-direction: column; gap: 32px'),
 ('<div style="display: flex; gap: 14px; flex-wrap: wrap">','<div style="display: flex; gap: 16px; flex-wrap: wrap">',2),
 ('flex: 1 1 240px; padding: 18px; border-radius: 18px;','flex: 1 1 240px; padding: 24px; border-radius: 18px;',3),
 ('display: flex; flex-direction: column; gap: 8px"><span style="font-size: 13px; font-weight: 600','display: flex; flex-direction: column; gap: 10px"><span style="font-size: 13px; font-weight: 600',3),
 ('<section style="padding: 18px; border-radius: 18px; background: #11131A; border: 1px solid #1E2129; display: flex; align-items: center; gap: 28px; flex-wrap: wrap">','<section style="padding: 20px 24px; border-radius: 18px; background: #11131A; border: 1px solid #1E2129; display: flex; align-items: center; gap: 36px; flex-wrap: wrap">'),
 ('<span style="display: flex; align-items: center; gap: 10px"><span style="width: 40px; height: 40px;','<span style="display: flex; align-items: center; gap: 12px"><span style="width: 40px; height: 40px;',3),
 ('<span style="display: flex; flex-direction: column"><span style="font-weight: 600">','<span style="display: flex; flex-direction: column; gap: 2px"><span style="font-weight: 600">',3),
 ('flex: 1 1 260px; padding: 22px; border-radius: 18px; background: #0F1117; border: 1px dashed #333846; display: flex; flex-direction: column; align-items: flex-start; gap: 10px','flex: 1 1 260px; padding: 24px; border-radius: 18px; background: #0F1117; border: 1px dashed #333846; display: flex; flex-direction: column; align-items: flex-start; gap: 12px',3),
 ('<button style="height: 44px; padding: 0 18px; border-radius: 12px; font: 600 15px Geist, sans-serif; border: 0; background: {{accent}}; color: #0A0B10; ">Accept</button>','<button style="height: 44px; padding: 0 18px; border-radius: 12px; font: 600 15px Geist, sans-serif; border: 1px solid {{accent}}; background: transparent; color: {{accent}}; ">Accept</button>'),
])
