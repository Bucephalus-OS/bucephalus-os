import svgwrite, os
from PIL import Image, ImageDraw
import noise, numpy as np

os.makedirs('assets/wallpapers', exist_ok=True)
os.makedirs('assets/themes/CyberNexus/contents/colors', exist_ok=True)

# Logo + Symbol
dwg = svgwrite.Drawing('assets/bucephalus-logo.svg', size=('1000px','320px'))
dwg.add(dwg.path(d="M100,240 Q300,80 520,160 Q760,240 900,200 L900,300 L100,300 Z",
                 fill='#00D4FF', stroke='#FF004D', stroke_width=16))
dwg.add(dwg.text('BUCEPHALUS OS', insert=(180,260), fill='#F5F5F5', font_size=80, font_weight='bold'))
dwg.save()

# 4 Wallpapers (matrix rain)
def wp(name, color):
    img = Image.new('RGB', (3840,2160), color)
    draw = ImageDraw.Draw(img)
    for x in range(0,3840,42):
        for y in range(0,2160,62):
            if np.random.rand() > 0.945:
                v = int(160 + 95*np.random.rand())
                draw.text((x,y), '1', fill=(0,v,v//2), font_size=24)
    img.save(f'assets/wallpapers/{name}.png')

wp('cybernexus-8k',      '#0D0208')
wp('voidemperor-8k',     '#0A0014')
wp('quantumblade-8k',    '#0F0022')
wp('obsidianforge-8k',   '#1a000d')

# KDE Theme
for t in ['CyberNexus', 'VoidEmperor', 'QuantumBlade', 'ObsidianForge']:
    os.makedirs(f'assets/themes/{t}/contents/colors', exist_ok=True)
    open(f'assets/themes/{t}/metadata.desktop','w').write(f"[Desktop Entry]\nName={t}\n")
    open(f'assets/themes/{t}/contents/colors/{t}.colors','w').write(
        "[Colors:Window]\nBackground=#0D0208\nForeground=#00D4FF\nDecorationFocus=#00D4FF\n")
print("Graphics forged")