#!/usr/bin/env python3
"""news-23 b69 front-page-dense: draw THE WORLD TODAY, Monday 23 November 2026.
1024x1024, PIL. Writes entry.png next to this script."""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")

FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def f(size, bold=False):
    return ImageFont.truetype(FB if bold else FR, size)


BLACK = (17, 17, 17)
WHITE = (255, 255, 255)
GOLD = (201, 162, 39)
GOLD_L = (212, 175, 55)
RED = (185, 28, 28)
RED_D = (153, 27, 27)
TEAL = (14, 124, 123)
NAVY = (30, 58, 95)
NAVY_D = (15, 36, 64)
BLUE = (29, 78, 216)
PURPLE = (109, 40, 217)
BROWN = (146, 64, 14)
GREY = (75, 85, 99)
GREY_L = (107, 114, 128)
CREAM = (250, 243, 224)
GREEN_L = (187, 230, 168)
GREEN_M = (134, 199, 120)

img = Image.new("RGB", (W, H), WHITE)
d = ImageDraw.Draw(img)


def tw(text, font):
    return d.textlength(text, font=font)


def wrap(text, font, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if tw(t, font) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text(x, y, s, font, fill=BLACK, anchor="la"):
    d.text((x, y), s, font=font, fill=fill, anchor=anchor)


def rrect(x0, y0, x1, y1, fill, outline=None, radius=3):
    d.rounded_rectangle([x0, y0, x1, y1], radius=radius, fill=fill, outline=outline)


def chip(x_right, y, label, fill):
    """Chip right-aligned at x_right, top y. Returns left edge."""
    font = f(9, True)
    w = int(tw(label, font)) + 12
    rrect(x_right - w, y, x_right, y + 14, fill, radius=3)
    text(x_right - w + 6, y + 2, label, font, WHITE)
    return x_right - w


# ---------------------------------------------------------------- masthead
d.rectangle([0, 0, W, 48], fill=BLACK)
text(10, 6, "THE WORLD TODAY", f(34, True), WHITE)
text(W - 10, 16, "MONDAY 23 NOVEMBER 2026", f(14, True), GOLD_L, anchor="ra")

# ---------------------------------------------------------------- kicker
text(10, 52, "AI rout hits Asia  \u00b7  UN chief urges AI rules  \u00b7  US lead over China at record low  \u00b7  Anthropic IPO $107.3B",
     f(13, True), RED)

# ---------------------------------------------------------------- number strip (2 rows x 5 cols)
strip = [
    [("-3.3%", "KOSPI", RED), ("5.3", "US-CHINA POWER GAP", NAVY),
     ("11,762", "EBOLA CASES, DRC", (22, 163, 74)), ("10T won", "SEOUL STABILISATION FUND", BROWN),
     ("2%", "BILLIONAIRE TAX IN PARIS", PURPLE)],
    [("$450M", "SKUBAL DEAL", PURPLE), ("165", "RUSSIAN MISSILES/WEEK", RED),
     ("12,000", "CLEARED IN MANCHESTER", BLUE), ("264 kg", "EXPLOSIVES SEIZED", BROWN),
     ("$107.3B", "ANTHROPIC IPO", PURPLE)],
]
col_w = 200
for r, row in enumerate(strip):
    yv = 68 + r * 27
    for c, (val, lab, col) in enumerate(row):
        x = 10 + c * col_w
        text(x, yv, val, f(17, True), col)
        text(x, yv + 17, lab, f(9, True), BLACK)

# ---------------------------------------------------------------- region bar
regions = [("ASIA-PACIFIC 7", (15, 118, 110), 168), ("AMERICAS 8", BLUE, 168),
           ("MIDDLE EAST 6", BROWN, 168), ("EUROPE 5", PURPLE, 168),
           ("AFRICA 3", RED, 168), ("WORLD 2", GREY, 168)]
x = 8
for name, col, wdt in regions:
    d.rectangle([x, 122, x + wdt - 2, 142], fill=col)
    text(x + wdt // 2, 127, name, f(11, True), WHITE, anchor="ma")
    x += wdt

# ---------------------------------------------------------------- UTC strip
text(10, 146, "THE DAY IN UTC   ~00:00 Kospi dives   ~06:30 Guterres opens   ~09:00 Power Index   ~12:00 Paris 2% tax   ~15:00 Kyiv missiles",
     f(10), GREY)
text(W - 10, 146, "~ APPROX", f(10), GREY_L, anchor="ra")

# ---------------------------------------------------------------- hero scenes
HX = [8, 352, 696]          # hero x starts
HW = 320                    # hero width
SY, SH = 160, 118           # scene y, height
CY = SY + SH                # caption strip y (278), height 14

# --- scene 1: Kospi skyline + chart
x0 = HX[0]
d.rectangle([x0, SY, x0 + HW, SY + SH], fill=NAVY_D)
text(x0 + 8, SY + 6, "-3.3%", f(26, True), (255, 90, 60))
# buildings with lit windows (max height 52px, bottom at SY+SH)
import random
random.seed(69)
bx = x0 + 6
while bx < x0 + HW - 14:
    bw = random.randint(16, 26)
    bh = random.randint(28, 52)
    by = SY + SH - bh
    d.rectangle([bx, by, bx + bw, SY + SH], fill=(24, 58, 96))
    for wy in range(by + 5, SY + SH - 4, 9):
        for wx in range(bx + 3, bx + bw - 3, 7):
            if random.random() < 0.55:
                d.rectangle([wx, wy, wx + 3, wy + 4], fill=(255, 214, 90))
    bx += bw + 3
# orange chart line across lower-middle zone (below the -3.3% text)
pts = [(x0 + 10, 232), (x0 + 45, 218), (x0 + 80, 228), (x0 + 115, 210),
       (x0 + 150, 222), (x0 + 185, 206), (x0 + 220, 216), (x0 + 255, 204),
       (x0 + 290, 212), (x0 + 312, 200)]
d.line(pts, fill=(255, 165, 0), width=3)
for px, py in pts:
    d.ellipse([px - 3, py - 3, px + 3, py + 3], fill=(255, 200, 90), outline=(255, 165, 0))

# --- scene 2: Guterres teal + globe
x0 = HX[1]
d.rectangle([x0, SY, x0 + HW, SY + SH], fill=TEAL)
text(x0 + 10, SY + 10, "150 DELEGATES", f(24, True), GOLD_L)
text(x0 + 10, SY + 40, "BACK A RISK", f(24, True), GOLD_L)
text(x0 + 10, SY + 70, "FRAMEWORK", f(24, True), GOLD_L)
# globe
gx, gy, gr = x0 + 262, SY + 62, 42
d.ellipse([gx - gr, gy - gr, gx + gr, gy + gr], outline=WHITE, width=2)
d.ellipse([gx - gr // 2, gy - gr, gx + gr // 2, gy + gr], outline=WHITE, width=1)
d.line([gx - gr, gy, gx + gr, gy], fill=WHITE, width=1)
d.arc([gx - gr, gy - gr // 2, gx + gr, gy + gr // 2], 0, 360, fill=WHITE, width=1)

# --- scene 3: Power Index bars
x0 = HX[2]
d.rectangle([x0, SY, x0 + HW, SY + SH], fill=CREAM)
text(x0 + 10, SY + 6, "NARROWEST SINCE 2018", f(11, True), BLACK)
text(x0 + HW - 10, SY + 6, "GAP 5.3", f(11, True), BROWN, anchor="ra")
base = SY + SH - 6
bars = [("US", 78.9, NAVY), ("CHINA", 73.6, RED), ("INDIA", 40.5, (180, 130, 29))]
bw2, gap2 = 62, 34
bx = x0 + 28
for name, val, col in bars:
    bh = int(val / 100 * 66)
    top = base - bh
    d.rectangle([bx, top, bx + bw2, base], fill=col)
    vfont = f(13, True)
    if bh >= 40:  # value inside bar, white
        text(bx + bw2 // 2, top + 5, f"{val}", vfont, WHITE, anchor="ma")
        text(bx + bw2 // 2, base - 18, name, f(10, True), WHITE, anchor="ma")
    else:         # short bar: value above bar in dark
        text(bx + bw2 // 2, top - 17, f"{val}", vfont, BLACK, anchor="ma")
        text(bx + bw2 // 2, base - 18, name, f(10, True), WHITE, anchor="ma")
    bx += bw2 + gap2

# caption strips under scenes
caps = ["KOSPI 4,708.54   \u00b7   -161 PTS", "UN   \u00b7   BRIDGETOWN", "ASIA POWER INDEX 2026"]
for i, cap in enumerate(caps):
    d.rectangle([HX[i], CY, HX[i] + HW, CY + 14], fill=BLACK)
    text(HX[i] + 8, CY + 2, cap, f(10, True), WHITE)

# ---------------------------------------------------------------- hero headlines / bodies / chips
heroes = [
    ("AI ROUT HITS ASIA",
     "Kospi closes -3.3% to 4,708.54, sheds 161 pts; intraday -5.8%. Samsung -3.1%, SK Hynix -2.5%.",
     "KOREA EXCHANGE", "REPORTED", BLUE),
    ("GUTERRES: REGULATE AI BEFORE IT'S TOO LATE",
     "UN chief urges global AI safety rules at the Bridgetown summit; 150 back a risk framework.",
     "UNITED NATIONS", "REPORTED", BLUE),
    ("US LEAD OVER CHINA AT RECORD LOW",
     "Asia Power Index 2026: US 78.9, China 73.6 \u2014 gap 5.3, narrowest since 2018. India third at 40.5.",
     "LOWY INSTITUTE", "REPORTED", BLUE),
]
HY = 296
for i, (hl, body, src, chiplab, chipcol) in enumerate(heroes):
    x0 = HX[i]
    lines = wrap(hl, f(19, True), HW)
    yy = HY
    for ln in lines[:2]:
        text(x0, yy, ln, f(19, True), BLACK)
        yy += 20
    blines = wrap(body, f(11), HW)
    yy = HY + 42
    for ln in blines[:2]:
        text(x0, yy, ln, f(11), BLACK)
        yy += 13
    text(x0, HY + 70, src, f(9), GREY)
    chip(x0 + HW, HY + 68, chiplab, chipcol)

# ---------------------------------------------------------------- MORE OF THE DAY bar
d.rectangle([8, 382, 1016, 398], fill=BLACK)
text(10, 385, "MORE OF THE DAY  \u2014  10 STORIES", f(12, True), WHITE)

# ---------------------------------------------------------------- cards (5 x 2)
cards = [
    ("AMERICAS", RED, "BESSENT: NVIDIA ANSWERS", "Treasury wants answers.", "Reuters", "REPORTED", BLUE),
    ("FBI", RED_D, "FBI PROBES NCIC HACK", "NCIC database hacked.", "AP", "REPORTED", BLUE),
    ("WHITE HOUSE", BROWN, "TRUMP: IRAN STRIKES MAY RESUME", "May resume in New Year.", "Reuters", "REPORTED", BLUE),
    ("MARKETS", BLUE, "US FUTURES JUMP 3%", "Holiday rally lifts futures 3%.", "Bloomberg", "REPORTED", BLUE),
    ("SPORT", RED, "SKUBAL'S $450M METS DEAL", "Nine-year deal, largest ever.", "AP", "REPORTED", BLUE),
    ("SPORT", RED, "TOM JACKSON DIES AT 75", "Broncos LB, ESPN voice, dies.", "ESPN", "REPORTED", BLUE),
    ("LEGAL", PURPLE, "STATES SUE SPACEX", "Ten states challenge AI claims.", "AP", "REPORTED", BLUE),
    ("TECH", BLUE, "ANTHROPIC IPO: $107.3B", "Raised at $83; closes $97.17.", "WSJ", "REPORTED", BLUE),
    ("EUROPE", PURPLE, "POLAND: 3 MISSILES CROSSED AIRSPACE", "Kyiv: three Kh-101s crossed.", "AP", "CLAIM", RED),
    ("SPACE", GREY, "RUSSIAN NUCLEAR SATELLITE", "May carry a nuke.", "Reuters", "CLAIM", RED),
]
CW, CG = 195, 8
for idx, (reg, col, hl, body, src, chiplab, chipcol) in enumerate(cards):
    r, c = divmod(idx, 5)
    x0 = 8 + c * (CW + CG)
    y0 = 402 + r * 88
    d.rectangle([x0, y0, x0 + CW, y0 + 14], fill=col)
    text(x0 + 5, y0 + 2, reg, f(9, True), WHITE)
    text(x0 + CW - 5, y0 + 2, str(idx + 1), f(9, True), WHITE, anchor="ra")
    lines = wrap(hl, f(12, True), CW - 4)
    yy = y0 + 18
    for ln in lines[:2]:
        text(x0 + 2, yy, ln, f(12, True), BLACK)
        yy += 14
    text(x0 + 2, y0 + 50, body, f(10), BLACK)
    text(x0 + 2, y0 + 66, src, f(9), GREY)
    chip(x0 + CW, y0 + 64, chiplab, chipcol)

# ---------------------------------------------------------------- WHERE / ALSO header bar
d.rectangle([8, 578, 330, 594], fill=BLACK)
text(10, 581, "WHERE IT HAPPENED", f(12, True), WHITE)
d.rectangle([340, 578, 1016, 594], fill=BLACK)
text(342, 581, "ALSO ON MONDAY", f(12, True), WHITE)

# ---------------------------------------------------------------- map (left)
d.rectangle([8, 598, 330, 830], fill=(245, 245, 240))
for gx in range(8, 331, 16):
    d.line([gx, 598, gx, 830], fill=(225, 225, 215), width=1)
for gy in range(598, 831, 16):
    d.line([8, gy, 330, gy], fill=(225, 225, 215), width=1)
# stylised land blobs: Americas (left), Eurasia (right), SE Asia (small)
d.ellipse([18, 620, 150, 790], fill=GREEN_L)
d.ellipse([60, 760, 140, 815], fill=GREEN_L)
d.ellipse([165, 610, 315, 780], fill=GREEN_L)
d.ellipse([205, 755, 265, 800], fill=GREEN_L)
pins = [
    (1, 52, 668), (2, 92, 748), (3, 128, 640), (4, 78, 700), (5, 108, 690),
    (6, 196, 742), (7, 46, 724), (8, 34, 690), (9, 66, 748), (10, 96, 772),
    (11, 216, 668), (12, 246, 690), (13, 282, 660),
]
for n, px, py in pins:
    d.ellipse([px - 8, py - 8, px + 8, py + 8], fill=RED, outline=WHITE, width=1)
    text(px, py - 6, str(n), f(9, True), WHITE, anchor="ma")
text(10, 800, "Pins 1\u201313: 1 Seoul \u00b7 2 Bridgetown \u00b7 3 Beijing", f(8), GREY)
text(10, 810, "4 Washington \u00b7 5 New York \u00b7 6 Tehran \u00b7 7 Chicago", f(8), GREY)
text(10, 820, "8 SF \u00b7 9 Denver \u00b7 10 Austin \u00b7 11 Warsaw \u00b7 12 Kyiv \u00b7 13 Moscow", f(8), GREY)

# ---------------------------------------------------------------- ALSO list (right, 2 cols x 9)
also_l = [
    "14. Paris: 100+ back 2% billionaire tax",
    "15. Manchester: 12,000 cleared",
    "16. Zelenskyy: 165 missiles in a week",
    "17. COP31: the day after pact rejected",
    "18. Benghazi: UN demands port probe",
    "19. Israel unity talks resume",
    "20. Gaza: two killed in Israeli strike",
    "21. West Bank settler attacks",
    "22. Iran war: no deal in sight",
]
also_r = [
    "23. Lebanon seizes 264 kg explosives",
    "24. Bahrain: strike hits plant, 2 hurt",
    "25. Sudan: defences down drones",
    "26. DRC: fighting traps Ebola teams",
    "27. Bangladesh: Hasina jailed if she returns",
    "28. Seoul minister quits in exam row",
    "29. SK Telecom -7.3% as hype cools",
    "30. China eases margin rules",
    "31. Seoul readies 10T-won fund",
]
for i, s in enumerate(also_l):
    text(342, 600 + i * 25, s, f(11), BLACK)
for i, s in enumerate(also_r):
    text(682, 600 + i * 25, s, f(11), BLACK)

# ---------------------------------------------------------------- DATE CHECK box
d.rectangle([8, 836, 1016, 890], outline=RED, width=2)
text(12, 840, "DATE CHECK", f(12, True), RED)
text(1012, 840, "READ 23 NOV 2026, 23:59 UTC \u2014 STORIES DATED 23 NOV ONLY", f(9, True), RED, anchor="ra")
text(12, 858, "LEFT OUT \u2014 NOT 23 NOV: Dems 258 seats (22 Nov) \u00b7 Sparta II fire (22 Nov) \u00b7 El Chapo (22 Nov) \u00b7 EU\u2013Indonesia pact (21 Nov) \u00b7 Nigeria boat (21 Nov) \u00b7 ICJ Myanmar (19 Nov)",
     f(11), BLACK)
text(12, 874, "NOT YET: Dymer search continues (14 missing) \u00b7 4 House races uncalled \u00b7 COP32 venue not set \u00b7 WHO evacuating trapped Ebola staff",
     f(11), BLACK)

# ---------------------------------------------------------------- footer
text(10, 896, "Sources: Reuters \u00b7 AP \u00b7 Bloomberg \u00b7 AFP \u00b7 Yonhap \u00b7 BBC \u00b7 WSJ \u00b7 NYT \u00b7 ESPN \u00b7 Lowy Institute (Asia Power Index 2026).", f(9), GREY)
text(10, 908, "CHIPS: REPORTED = confirmed by wires. CLAIM = one side's claim, not independently confirmed. ONGOING = still developing.", f(9), GREY)
text(10, 920, "All times UTC. Figures as reported 23 Nov 2026. Scenes are drawn illustrations, not photographs.", f(9), GREY)

# ---------------------------------------------------------------- bottom bar
d.rectangle([0, 948, W, H], fill=BLACK)
text(W // 2, 976, "THE WORLD TODAY  \u2014  Monday 23 November 2026  \u00b7  31 stories  \u00b7  6 regions",
     f(16, True), GOLD_L, anchor="ma")

img.save(OUT)
print("saved", OUT, os.path.getsize(OUT), "bytes")
