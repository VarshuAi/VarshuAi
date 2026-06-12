"""
🎨 VarshuAi README Theme Rotator
─────────────────────────────────
Generates 7 unique themed README.md files — one for each day of the week.
Run via GitHub Actions cron or manually with: python scripts/generate_readme.py
"""

import datetime
import os

# ──────────────────────────────────────────────
# TIMEZONE: IST (UTC+5:30)
# ──────────────────────────────────────────────
IST = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
today = datetime.datetime.now(IST)
day = today.strftime("%A")  # Monday, Tuesday, etc.

# ──────────────────────────────────────────────
# THEME CONFIGS — colors, moods, vibes per day
# ──────────────────────────────────────────────

THEMES = {
    "Monday": {
        "name": "WARZONE",
        "emoji": "🔴",
        "icon": "⚔️",
        "header_gradient": "0:0D1117,30:8B0000,60:FF0000,100:0D1117",
        "accent": "FF0000",
        "accent2": "FF6B6B",
        "text": "C9D1D9",
        "border": "8B0000",
        "bg": "0D1117",
        "vibe": "ATTACK MODE ACTIVATED",
        "mood": "Monday doesn't scare me. I scare Monday.",
        "typing_lines": [
            "☕ chai loaded... mass coding begins",
            "🔴 Monday? More like MONSTERday — let's build",
            "💻 new week = new repos. no excuses.",
            "⚔️ shipping code before the world wakes up",
        ],
        "ascii_top": """
 ███╗   ███╗ ██████╗ ███╗   ██╗██████╗  █████╗ ██╗   ██╗
 ████╗ ████║██╔═══██╗████╗  ██║██╔══██╗██╔══██╗╚██╗ ██╔╝
 ██╔████╔██║██║   ██║██╔██╗ ██║██║  ██║███████║ ╚████╔╝ 
 ██║╚██╔╝██║██║   ██║██║╚██╗██║██║  ██║██╔══██║  ╚██╔╝  
 ██║ ╚═╝ ██║╚██████╔╝██║ ╚████║██████╔╝██║  ██║   ██║   
 ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝   ╚═╝   """,
        "quote": "Mondays are for those who have unfinished code from Sunday night.",
        "status": "🔴 LOCKED IN — DO NOT DISTURB",
    },
    "Tuesday": {
        "name": "DEEP OCEAN",
        "emoji": "🔵",
        "icon": "🌊",
        "header_gradient": "0:0D1117,30:001F54,60:0074D9,100:0D1117",
        "accent": "0074D9",
        "accent2": "7FDBFF",
        "text": "C9D1D9",
        "border": "001F54",
        "bg": "0D1117",
        "vibe": "DEEP FOCUS ENGAGED",
        "mood": "Silence. Keyboard. Code. Repeat.",
        "typing_lines": [
            "🌊 diving deep into the codebase...",
            "🔵 flow state = ON | distractions = OFF",
            "🧠 brain.exe running at 100% — don't interrupt",
            "☕ second chai hit different on Tuesdays",
        ],
        "ascii_top": """
 ████████╗██╗   ██╗███████╗███████╗██████╗  █████╗ ██╗   ██╗
 ╚══██╔══╝██║   ██║██╔════╝██╔════╝██╔══██╗██╔══██╗╚██╗ ██╔╝
    ██║   ██║   ██║█████╗  ███████╗██║  ██║███████║ ╚████╔╝ 
    ██║   ██║   ██║██╔══╝  ╚════██║██║  ██║██╔══██║  ╚██╔╝  
    ██║   ╚██████╔╝███████╗███████║██████╔╝██║  ██║   ██║   
    ╚═╝    ╚═════╝ ╚══════╝╚══════╝╚═════╝ ╚═╝  ╚═╝   ╚═╝   """,
        "quote": "The code doesn't care what day it is. Neither do I.",
        "status": "🔵 IN THE ZONE — BUILDING SOMETHING",
    },
    "Wednesday": {
        "name": "NEON ARCADE",
        "emoji": "🟣",
        "icon": "🕹️",
        "header_gradient": "0:0D1117,25:6C0BA9,50:FF00FF,75:6C0BA9,100:0D1117",
        "accent": "FF00FF",
        "accent2": "DA70D6",
        "text": "C9D1D9",
        "border": "6C0BA9",
        "bg": "0D1117",
        "vibe": "MIDWEEK MADNESS",
        "mood": "Halfway through the week. Code output: MAXIMUM.",
        "typing_lines": [
            "🕹️ wednesday = level 4 of 7. boss fight incoming",
            "🟣 midweek energy? nah, EVERY day energy",
            "💜 code hits different at 2 AM with lo-fi on",
            "🎮 treating every bug like a game boss — and winning",
        ],
        "ascii_top": """
 ██╗    ██╗███████╗██████╗ ███╗   ██╗███████╗███████╗██████╗  █████╗ ██╗   ██╗
 ██║    ██║██╔════╝██╔══██╗████╗  ██║██╔════╝██╔════╝██╔══██╗██╔══██╗╚██╗ ██╔╝
 ██║ █╗ ██║█████╗  ██║  ██║██╔██╗ ██║█████╗  ███████╗██║  ██║███████║ ╚████╔╝ 
 ██║███╗██║██╔══╝  ██║  ██║██║╚██╗██║██╔══╝  ╚════██║██║  ██║██╔══██║  ╚██╔╝  
 ╚███╔███╔╝███████╗██████╔╝██║ ╚████║███████╗███████║██████╔╝██║  ██║   ██║   
  ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═══╝╚══════╝╚══════╝╚═════╝ ╚═╝  ╚═╝   ╚═╝""",
        "quote": "Wednesday: too late to quit, too early to celebrate. Just code.",
        "status": "🟣 CODING THROUGH THE CHAOS",
    },
    "Thursday": {
        "name": "EMERALD FOREST",
        "emoji": "🟢",
        "icon": "🌿",
        "header_gradient": "0:0D1117,30:0B3D0B,60:00FF41,100:0D1117",
        "accent": "00FF41",
        "accent2": "A8E6CF",
        "text": "C9D1D9",
        "border": "0B3D0B",
        "bg": "0D1117",
        "vibe": "GROWTH MODE",
        "mood": "Plant seeds today. Watch them compile tomorrow.",
        "typing_lines": [
            "🌿 growing one commit at a time",
            "🟢 thursday = almost there. keep pushing.",
            "🌱 every project starts with one 'git init'",
            "☕ filter coffee > energy drink. always.",
        ],
        "ascii_top": """
 ████████╗██╗  ██╗██╗   ██╗██████╗ ███████╗██████╗  █████╗ ██╗   ██╗
 ╚══██╔══╝██║  ██║██║   ██║██╔══██╗██╔════╝██╔══██╗██╔══██╗╚██╗ ██╔╝
    ██║   ███████║██║   ██║██████╔╝███████╗██║  ██║███████║ ╚████╔╝ 
    ██║   ██╔══██║██║   ██║██╔══██╗╚════██║██║  ██║██╔══██║  ╚██╔╝  
    ██║   ██║  ██║╚██████╔╝██║  ██║███████║██████╔╝██║  ██║   ██║   
    ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝  ╚═╝   ╚═╝""",
        "quote": "Code is the tree. The repo is the forest. Keep planting.",
        "status": "🟢 SPROUTING NEW IDEAS",
    },
    "Friday": {
        "name": "GOLDEN HOUR",
        "emoji": "🟡",
        "icon": "🏆",
        "header_gradient": "0:0D1117,25:B8860B,50:FFD700,75:B8860B,100:0D1117",
        "accent": "FFD700",
        "accent2": "FFE066",
        "text": "C9D1D9",
        "border": "B8860B",
        "bg": "0D1117",
        "vibe": "VICTORY LAP",
        "mood": "Friday night = deploy night. Ship it and chill.",
        "typing_lines": [
            "🏆 friday deploy? living on the edge 😎",
            "🟡 week survived. code shipped. chai earned.",
            "🎉 pushing to main on friday because YOLO",
            "💛 weekend loading... but first, one more commit",
        ],
        "ascii_top": """
 ███████╗██████╗ ██╗██████╗  █████╗ ██╗   ██╗
 ██╔════╝██╔══██╗██║██╔══██╗██╔══██╗╚██╗ ██╔╝
 █████╗  ██████╔╝██║██║  ██║███████║ ╚████╔╝ 
 ██╔══╝  ██╔══██╗██║██║  ██║██╔══██║  ╚██╔╝  
 ██║     ██║  ██║██║██████╔╝██║  ██║   ██║   
 ╚═╝     ╚═╝  ╚═╝╚═╝╚═════╝ ╚═╝  ╚═╝   ╚═╝   """,
        "quote": "The weekend belongs to those who shipped on Friday.",
        "status": "🟡 SHIPPING & VIBING",
    },
    "Saturday": {
        "name": "CYBER PUNK",
        "emoji": "🩷",
        "icon": "⚡",
        "header_gradient": "0:0D1117,25:FF1493,50:00FFFF,75:FF1493,100:0D1117",
        "accent": "FF1493",
        "accent2": "00FFFF",
        "text": "C9D1D9",
        "border": "FF1493",
        "bg": "0D1117",
        "vibe": "WEEKEND WARRIOR",
        "mood": "No deadlines. No pressure. Pure passion projects.",
        "typing_lines": [
            "⚡ saturday = side project day. let's get weird.",
            "🩷 no boss. no deadline. just me and vim.",
            "🎧 lo-fi + dark room + code = perfection",
            "💿 building things nobody asked for. that's the fun.",
        ],
        "ascii_top": """
 ███████╗ █████╗ ████████╗██╗   ██╗██████╗ ██████╗  █████╗ ██╗   ██╗
 ██╔════╝██╔══██╗╚══██╔══╝██║   ██║██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝
 ███████╗███████║   ██║   ██║   ██║██████╔╝██║  ██║███████║ ╚████╔╝ 
 ╚════██║██╔══██║   ██║   ██║   ██║██╔══██╗██║  ██║██╔══██║  ╚██╔╝  
 ███████║██║  ██║   ██║   ╚██████╔╝██║  ██║██████╔╝██║  ██║   ██║   
 ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝   ╚═╝""",
        "quote": "The best code is written when nobody's watching.",
        "status": "🩷 HACKING ON PASSION PROJECTS",
    },
    "Sunday": {
        "name": "SUNSET CHILL",
        "emoji": "🟠",
        "icon": "🌅",
        "header_gradient": "0:0D1117,25:8B4513,50:FF6347,75:FF8C00,100:0D1117",
        "accent": "FF6347",
        "accent2": "FF8C00",
        "text": "C9D1D9",
        "border": "8B4513",
        "bg": "0D1117",
        "vibe": "REST & RECHARGE",
        "mood": "Even machines need a reboot. But maybe one tiny commit...",
        "typing_lines": [
            "🌅 sunday chill... opens laptop anyway",
            "🟠 'rest day' = refactoring day. same thing right?",
            "☕ sunday morning chai + cleaning up old code",
            "🧘 today's commit: inner peace. and maybe a bugfix.",
        ],
        "ascii_top": """
 ███████╗██╗   ██╗███╗   ██╗██████╗  █████╗ ██╗   ██╗
 ██╔════╝██║   ██║████╗  ██║██╔══██╗██╔══██╗╚██╗ ██╔╝
 ███████╗██║   ██║██╔██╗ ██║██║  ██║███████║ ╚████╔╝ 
 ╚════██║██║   ██║██║╚██╗██║██║  ██║██╔══██║  ╚██╔╝  
 ███████║╚██████╔╝██║ ╚████║██████╔╝██║  ██║   ██║   
 ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝   ╚═╝   """,
        "quote": "Rest is not the enemy of productivity. Burnout is.",
        "status": "🟠 RECHARGING... (but probably coding)",
    },
}


def generate_typing_url(lines, color):
    """Generate readme-typing-svg URL from list of lines."""
    encoded = ";".join(lines).replace(" ", "+").replace("&", "%26").replace("=", "%3D").replace("#", "%23")
    return (
        f"https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=500&size=18"
        f"&duration=3000&pause=1000&color={color}&center=true&vCenter=true"
        f"&multiline=true&repeat=true&random=false&width=700&height=80&lines={encoded}"
    )


def build_readme(t):
    """Build the full README markdown for a given theme dict."""
    typing_url = generate_typing_url(t["typing_lines"], t["accent"])

    return f"""<!-- 
  🎨 AUTO-GENERATED by VarshuAi Theme Rotator
  📅 Today's Theme: {t["emoji"]} {t["name"]} ({day})
  🤖 This README changes every day. Come back tomorrow for a new vibe.
  ⏰ Last rotated: {today.strftime("%d %b %Y, %I:%M %p IST")}
-->

<div align="center">

<!-- HEADER WAVE -->
<img src="https://capsule-render.vercel.app/api?type=waving&color={t["header_gradient"]}&height=200&section=header&text=VARSHU+AI&fontSize=70&fontColor={t["accent"]}&animation=fadeIn&fontAlignY=33&desc={t["vibe"].replace(" ", "+")}&descAlignY=55&descSize=16&descColor={t["accent2"]}" width="100%"/>

<!-- TYPING ANIMATION — changes with theme -->
<br>

<a href="https://git.io/typing-svg"><img src="{typing_url}" alt="Typing SVG" /></a>

<br>

<!-- TODAY'S MOOD BADGE -->
<img src="https://img.shields.io/badge/{day.upper()}-{t["name"].replace(" ", "_")}-{t["accent"]}?style=for-the-badge&labelColor=0D1117" />
<img src="https://img.shields.io/badge/STATUS-{t["status"].split(" ", 1)[1].replace(" ", "_").replace("—", "-")}-{t["accent2"]}?style=for-the-badge&labelColor=0D1117" />
<img src="https://img.shields.io/badge/THEME_ROTATES-DAILY_🔄-{t["accent"]}?style=for-the-badge&labelColor=0D1117" />

<br><br>

> **{t["icon"]} `{t["mood"]}`**

<br>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

</div>

<!-- ═══════════════════════════════════════════════════════════ -->
<!--                      WHO AM I                               -->
<!-- ═══════════════════════════════════════════════════════════ -->

## {t["emoji"]} `// WHO AM I`

<img align="right" src="https://raw.githubusercontent.com/rahulbanerjee26/githubProfileReadmeGenerator/main/gifs/code.gif" width="300px"/>

```yaml
┌──────────────────────────────────────────────┐
│  name       : Varshan Gowda                  │
│  aka        : VarshuAi                       │
│  from       : India 🇮🇳                       │
│  vibe       : coding enthusiast              │
│  student    : nah. just a guy who codes.     │
│  why        : because it's fun, that's why   │
│                                              │
│  what I do:                                  │
│    → build stuff nobody asked for            │
│    → upload it at 3 AM                       │
│    → mass upload repos like a madman         │
│    → drink chai, repeat                      │
│                                              │
│  languages  : 11 and counting               │
│  repos      : 197+ (and I'm not stopping)   │
│  motto      : "just build it bro"           │
│                                              │
│  today      : {day}                    │
│  theme      : {t["emoji"]} {t["name"]:<20}         │
│  status     : {t["status"]:<30} │
└──────────────────────────────────────────────┘
```

<br clear="both"/>

> 🇮🇳 *Indian guy who just loves coding. No fancy title. No degree flex. I see a problem → I build a solution → I upload it. That's the whole story.*

<br>

<!-- SNAKE ANIMATION -->
<div align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/platane/snk/output/github-contribution-grid-snake-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/platane/snk/output/github-contribution-grid-snake.svg">
  <img alt="Snake animation" src="https://raw.githubusercontent.com/platane/snk/output/github-contribution-grid-snake-dark.svg" width="100%">
</picture>
</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

<!-- ═══════════════════════════════════════════════════════════ -->
<!--                     WHAT I USE                              -->
<!-- ═══════════════════════════════════════════════════════════ -->

## {t["emoji"]} `// WHAT I CODE WITH`

<div align="center">

#### `⚡ LANGUAGES I THINK IN`

<p>
  <img src="https://skillicons.dev/icons?i=python,javascript,typescript,go,rust,cpp,dart,java,kotlin,bash&perline=10&theme=dark" />
</p>

#### `🛠️ FRAMEWORKS I BUILD WITH`

<p>
  <img src="https://skillicons.dev/icons?i=react,nextjs,nodejs,express,fastapi,flask,django,flutter,tailwind,vue,svelte,graphql&perline=12&theme=dark" />
</p>

#### `🔐 SECURITY & INFRA`

<p>
  <img src="https://skillicons.dev/icons?i=kali,docker,kubernetes,terraform,githubactions,linux,nginx,ansible&perline=8&theme=dark" />
</p>

#### `☁️ CLOUD & DATA`

<p>
  <img src="https://skillicons.dev/icons?i=aws,gcp,azure,firebase,mongodb,postgres,redis,supabase&perline=8&theme=dark" />
</p>

#### `🧠 AI & ML`

<p>
  <img src="https://skillicons.dev/icons?i=tensorflow,pytorch&perline=5&theme=dark" />
  <br>
  <img src="https://img.shields.io/badge/OpenAI-412991?style=flat-square&logo=openai&logoColor=white" alt="OpenAI">
  <img src="https://img.shields.io/badge/HuggingFace-FFD21E?style=flat-square&logo=huggingface&logoColor=black" alt="HF">
  <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white" alt="LangChain">
</p>

</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

<!-- ═══════════════════════════════════════════════════════════ -->
<!--                    HOW HARD I GO                            -->
<!-- ═══════════════════════════════════════════════════════════ -->

## {t["emoji"]} `// HOW HARD I GO`

```text
Security         ████████████████████████░   95%   ← this is where the fun is
Python           ███████████████████████░░   93%   ← first love
System Design    ███████████████████████░░   93%   ← big brain stuff
Cloud / DevOps   ██████████████████████░░░   92%   ← deploy everything
JavaScript       █████████████████████░░░░   90%   ← the universal language
Bash Scripting   █████████████████████░░░░   90%   ← automate ALL the things
TypeScript       ████████████████████░░░░░   87%   ← JS but make it strict
Java             ████████████████████░░░░░   85%   ← old reliable
Go               ███████████████████░░░░░░   82%   ← fast and clean
AI / ML          ████████████████████░░░░░   80%   ← building the future
Rust             ██████████████████░░░░░░░   75%   ← learning daily
```

<div align="center">

<img src="https://img.shields.io/badge/197+-REPOS_UPLOADED-{t["accent"]}?style=for-the-badge&labelColor=0D1117&logo=github&logoColor={t["accent"]}" alt="Repos">
<img src="https://img.shields.io/badge/11-LANGUAGES-{t["accent2"]}?style=for-the-badge&labelColor=0D1117&logo=stackblitz&logoColor={t["accent2"]}" alt="Languages">
<img src="https://img.shields.io/badge/150+-SECURITY_TOOLS-{t["accent"]}?style=for-the-badge&labelColor=0D1117&logo=hackthebox&logoColor={t["accent"]}" alt="Tools">
<img src="https://img.shields.io/badge/12+-FRAMEWORKS-{t["accent2"]}?style=for-the-badge&labelColor=0D1117&logo=buffer&logoColor={t["accent2"]}" alt="Frameworks">

</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

<!-- ═══════════════════════════════════════════════════════════ -->
<!--                       STATS                                 -->
<!-- ═══════════════════════════════════════════════════════════ -->

## {t["emoji"]} `// THE NUMBERS`

<div align="center">

<table align="center">
  <tr>
    <td align="center">
      <a href="https://github.com/VarshuAi">
        <img src="https://github-readme-stats-sigma-five.vercel.app/api?username=VarshuAi&show_icons=true&bg_color={t["bg"]}&border_color={t["border"]}&title_color={t["accent"]}&icon_color={t["accent2"]}&text_color={t["text"]}&count_private=true&include_all_commits=true" alt="Stats" height="195px">
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/VarshuAi">
        <img src="https://github-readme-stats-sigma-five.vercel.app/api/top-langs/?username=VarshuAi&layout=compact&bg_color={t["bg"]}&border_color={t["border"]}&title_color={t["accent"]}&text_color={t["text"]}&langs_count=10&card_width=400" alt="Langs" height="195px">
      </a>
    </td>
  </tr>
  <tr>
    <td align="center" colspan="2">
      <br>
      <img src="https://streak-stats.demolab.com?user=VarshuAi&background={t["bg"]}&border={t["border"]}&ring={t["accent"]}&fire={t["accent2"]}&currStreakLabel={t["accent2"]}&sideLabels={t["accent"]}&currStreakNum={t["text"]}&sideNums={t["text"]}&dates=555555" alt="Streak" height="195px">
    </td>
  </tr>
</table>

<br>

<img src="https://github-readme-activity-graph.vercel.app/graph?username=VarshuAi&bg_color={t["bg"]}&color={t["accent"]}&line={t["accent2"]}&point={t["accent"]}&area_color={t["accent"]}33&area=true&hide_border=true&custom_title=%3E_+VarshuAi+%2F%2F+Contribution+Graph" width="98%" alt="Activity Graph">

</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

<!-- ═══════════════════════════════════════════════════════════ -->
<!--                   FEATURED PROJECTS                         -->
<!-- ═══════════════════════════════════════════════════════════ -->

## {t["emoji"]} `// STUFF I BUILT`

<div align="center">

<table>
<tr>
<td width="50%">
<a href="https://github.com/VarshuAi/go-ssh-auditor"><img src="https://github-readme-stats-sigma-five.vercel.app/api/pin/?username=VarshuAi&repo=go-ssh-auditor&bg_color={t["bg"]}&border_color={t["border"]}&title_color={t["accent"]}&icon_color={t["accent2"]}&text_color={t["text"]}" alt="go-ssh-auditor"></a>
</td>
<td width="50%">
<a href="https://github.com/VarshuAi/py-packet-sniffer"><img src="https://github-readme-stats-sigma-five.vercel.app/api/pin/?username=VarshuAi&repo=py-packet-sniffer&bg_color={t["bg"]}&border_color={t["border"]}&title_color={t["accent"]}&icon_color={t["accent2"]}&text_color={t["text"]}" alt="py-packet-sniffer"></a>
</td>
</tr>
<tr>
<td width="50%">
<a href="https://github.com/VarshuAi/rust-port-scanner"><img src="https://github-readme-stats-sigma-five.vercel.app/api/pin/?username=VarshuAi&repo=rust-port-scanner&bg_color={t["bg"]}&border_color={t["border"]}&title_color={t["accent"]}&icon_color={t["accent2"]}&text_color={t["text"]}" alt="rust-port-scanner"></a>
</td>
<td width="50%">
<a href="https://github.com/VarshuAi/bash-sys-monitor"><img src="https://github-readme-stats-sigma-five.vercel.app/api/pin/?username=VarshuAi&repo=bash-sys-monitor&bg_color={t["bg"]}&border_color={t["border"]}&title_color={t["accent"]}&icon_color={t["accent2"]}&text_color={t["text"]}" alt="bash-sys-monitor"></a>
</td>
</tr>
</table>

</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

<!-- ═══════════════════════════════════════════════════════════ -->
<!--                     THEME GUIDE                             -->
<!-- ═══════════════════════════════════════════════════════════ -->

## 🔄 `// THIS README HAS 7 LIVES`

> **This profile auto-rotates its entire theme every day of the week.**
> Come back on a different day — the colors, mood, vibes, and energy will be completely different.

<div align="center">

```
╔══════════════════════════════════════════════════════════════╗
║  DAY          THEME              VIBE                       ║
╠══════════════════════════════════════════════════════════════╣
║  Monday       🔴 WARZONE         Attack mode. Ship hard.    ║
║  Tuesday      🔵 DEEP OCEAN      Deep focus. No distractions║
║  Wednesday    🟣 NEON ARCADE      Midweek madness.           ║
║  Thursday     🟢 EMERALD FOREST   Growth mode. Plant seeds.  ║
║  Friday       🟡 GOLDEN HOUR     Victory lap. Deploy day.   ║
║  Saturday     🩷 CYBER PUNK       Side projects. No rules.   ║
║  Sunday       🟠 SUNSET CHILL    Recharge. (but still code) ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  📅 TODAY: {day.upper():<10}  {t["emoji"]} {t["name"]:<16}                      ║
║  🔄 NEXT ROTATION: Tomorrow at midnight IST                 ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

<!-- ═══════════════════════════════════════════════════════════ -->
<!--                      FOOTER                                 -->
<!-- ═══════════════════════════════════════════════════════════ -->

<div align="center">

<br>

```
  "{t["quote"]}"
```

<br>

<img src="https://komarev.com/ghpvc/?username=VarshuAi&label=PROFILE+VIEWS&style=for-the-badge&color={t["accent"]}" alt="Profile Views">

<br><br>

<sub>

`🤖 this README was auto-generated at {today.strftime("%I:%M %p IST, %d %b %Y")} · theme: {t["emoji"]} {t["name"]} · powered by GitHub Actions`

</sub>

<br>

<img src="https://capsule-render.vercel.app/api?type=waving&color={t["header_gradient"]}&height=120&section=footer" width="100%"/>

</div>
"""


# ──────────────────────────────────────────────
# MAIN: Generate and write README.md
# ──────────────────────────────────────────────

if __name__ == "__main__":
    theme = THEMES[day]
    readme_content = build_readme(theme)

    # Write to repo root
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    readme_path = os.path.join(repo_root, "README.md")

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme_content)

    print(f"[OK] README.md generated!")
    print(f"Day: {day}")
    print(f"Theme: {theme['name']}")
    print(f"Written to: {readme_path}")
