"""
VarshuOS v2 — Animated SVG + README Generator
──────────────────────────────────────────────
Creates animated SVG files (loading bars, typing, colors)
and a README that references them. GitHub renders SVG animations!
"""

import datetime
import os

IST = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
today = datetime.datetime.now(IST)
day = today.strftime("%A")
date_str = today.strftime("%a %b %d %H:%M:%S IST %Y")
short_date = today.strftime("%d %b %Y")

DISTROS = {
    "Monday":    {"distro": "RedStrike OS",  "ver": "14.2",  "kernel": "6.8.0-redstrike",  "accent": "#FF0000", "accent2": "#FF6B6B", "glow": "#FF000055", "border": "#8B0000", "codename": "Inferno",  "motd": "New week. New exploits. No mercy.", "bg": "#0D1117"},
    "Tuesday":   {"distro": "DeepBlue OS",   "ver": "12.1",  "kernel": "6.8.0-deepblue",   "accent": "#0074D9", "accent2": "#7FDBFF", "glow": "#0074D955", "border": "#001F54", "codename": "Abyss",    "motd": "Silence the noise. Enter the flow.", "bg": "#0D1117"},
    "Wednesday": {"distro": "NeonArc OS",    "ver": "3.7",   "kernel": "6.8.0-neonarc",    "accent": "#FF00FF", "accent2": "#DA70D6", "glow": "#FF00FF55", "border": "#6C0BA9", "codename": "Glitch",   "motd": "Midweek. Maximum output.", "bg": "#0D1117"},
    "Thursday":  {"distro": "ForestRoot OS", "ver": "22.04", "kernel": "6.8.0-forestroot", "accent": "#00FF41", "accent2": "#A8E6CF", "glow": "#00FF4155", "border": "#0B3D0B", "codename": "Banyan",   "motd": "Grow one commit at a time.", "bg": "#0D1117"},
    "Friday":    {"distro": "GoldRush OS",   "ver": "40.1",  "kernel": "6.8.0-goldrush",   "accent": "#FFD700", "accent2": "#FFE066", "glow": "#FFD70055", "border": "#B8860B", "codename": "Midas",    "motd": "Ship it. Its Friday. YOLO.", "bg": "#0D1117"},
    "Saturday":  {"distro": "CyberKali OS",  "ver": "2024.3","kernel": "6.8.0-cyberkali",  "accent": "#00FFFF", "accent2": "#FF1493", "glow": "#00FFFF55", "border": "#008B8B", "codename": "Phantom",  "motd": "No rules. No deadlines. Pure chaos.", "bg": "#0D1117"},
    "Sunday":    {"distro": "ZenMint OS",    "ver": "21.3",  "kernel": "6.8.0-zenmint",    "accent": "#FF6347", "accent2": "#FF8C00", "glow": "#FF634755", "border": "#8B4513", "codename": "Satori",   "motd": "Rest day. Opens laptop anyway.", "bg": "#0D1117"},
}

d = DISTROS[day]
ac = d["accent"]
ac2 = d["accent2"]
bg = d["bg"]
glow = d["glow"]

# ═══════════════════════════════════════════════
# SVG 1: ANIMATED BOOT SEQUENCE
# ═══════════════════════════════════════════════

def make_boot_svg():
    modules = [
        ("python3.12", "93"),
        ("javascript-v8", "90"),
        ("typescript-strict", "87"),
        ("golang-1.22", "82"),
        ("rust-nightly", "75"),
        ("security-toolkit", "95"),
        ("docker-engine", "92"),
        ("chai-brewing-engine", "100"),
        ("mass-uploader-daemon", "99"),
    ]

    # Build module lines with staggered animations
    module_lines = ""
    bar_anims = ""
    for i, (name, pct) in enumerate(modules):
        y = 310 + i * 28
        delay = 1.5 + i * 0.4
        bar_width = int(int(pct) * 1.2)

        module_lines += f'''
    <text x="30" y="{y}" class="log" style="animation-delay:{delay}s">[  {pct}%  ] Loading {name}</text>
    <rect x="520" y="{y - 12}" width="0" height="14" rx="2" fill="{ac}" opacity="0.8">
      <animate attributeName="width" from="0" to="{bar_width}" dur="0.8s" begin="{delay}s" fill="freeze"/>
    </rect>
    <rect x="520" y="{y - 12}" width="{bar_width}" height="14" rx="2" fill="{ac}" opacity="0.15"/>'''

        bar_anims += f'''
    @keyframes bar{i} {{ from {{ width: 0; }} to {{ width: {bar_width}px; }} }}'''

    final_y = 310 + len(modules) * 28 + 20
    final_delay = 1.5 + len(modules) * 0.4 + 0.5

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="850" height="{final_y + 80}" viewBox="0 0 850 {final_y + 80}">
  <style>
    @keyframes fadeIn {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}
    @keyframes blink {{ 0%,100% {{ opacity: 1; }} 50% {{ opacity: 0; }} }}
    @keyframes scanline {{ 0% {{ top: 0; }} 100% {{ top: 100%; }} }}
    @keyframes glowPulse {{ 0%,100% {{ opacity: 0.3; }} 50% {{ opacity: 0.6; }} }}
    {bar_anims}

    .bg {{ fill: {bg}; }}
    .border {{ fill: none; stroke: {ac}; stroke-width: 1; opacity: 0.3; }}
    .title {{ font-family: 'Courier New', monospace; font-size: 14px; font-weight: bold; fill: {ac}; }}
    .bios {{ font-family: 'Courier New', monospace; font-size: 13px; fill: #8B949E; animation: fadeIn 0.3s forwards; opacity: 0; }}
    .ok {{ fill: {ac}; font-weight: bold; }}
    .log {{ font-family: 'Courier New', monospace; font-size: 12px; fill: {ac2}; animation: fadeIn 0.5s forwards; opacity: 0; }}
    .header {{ font-family: 'Courier New', monospace; font-size: 11px; fill: {ac}; opacity: 0.5; }}
    .cursor {{ font-family: 'Courier New', monospace; font-size: 13px; fill: {ac}; animation: blink 1s infinite; }}
    .motd {{ font-family: 'Courier New', monospace; font-size: 14px; fill: {ac}; font-weight: bold; animation: fadeIn 0.5s forwards; opacity: 0; }}
    .glow {{ fill: {glow}; filter: blur(40px); animation: glowPulse 3s infinite; }}
  </style>

  <!-- Background -->
  <rect width="850" height="{final_y + 80}" class="bg"/>
  <rect x="5" y="5" width="840" height="{final_y + 70}" rx="8" class="border"/>

  <!-- Glow effect -->
  <ellipse cx="425" cy="50" rx="200" ry="30" class="glow"/>

  <!-- BIOS Header -->
  <text x="30" y="35" class="title">VARSHUOS BIOS v4.20.69</text>
  <text x="620" y="35" class="header">{d["distro"]} {d["ver"]}</text>
  <line x1="30" y1="45" x2="820" y2="45" stroke="{ac}" stroke-width="0.5" opacity="0.3"/>

  <!-- System Checks -->
  <text x="30" y="75" class="bios" style="animation-delay:0.1s">  CPU      : Varshan Gowda @ mass_clock_speed          <tspan class="ok">[  OK  ]</tspan></text>
  <text x="30" y="100" class="bios" style="animation-delay:0.2s">  RAM      : Mass Creativity (Unlimited GB)             <tspan class="ok">[  OK  ]</tspan></text>
  <text x="30" y="125" class="bios" style="animation-delay:0.3s">  GPU      : Imagination RTX 9090 Ti                    <tspan class="ok">[  OK  ]</tspan></text>
  <text x="30" y="150" class="bios" style="animation-delay:0.4s">  STORAGE  : 197+ Repositories (Expanding...)           <tspan class="ok">[  OK  ]</tspan></text>
  <text x="30" y="175" class="bios" style="animation-delay:0.5s">  NETWORK  : Connected to Open Source Network           <tspan class="ok">[  OK  ]</tspan></text>
  <text x="30" y="200" class="bios" style="animation-delay:0.6s">  CHAI     : Filter Coffee Module Loaded                <tspan class="ok">[  OK  ]</tspan></text>
  <text x="30" y="225" class="bios" style="animation-delay:0.7s">  AUDIO    : Lo-fi Hip Hop Radio                        <tspan class="ok">[  OK  ]</tspan></text>
  <text x="30" y="250" class="bios" style="animation-delay:0.8s">  CLOCK    : 3:00 AM (Normal Operating Hours)           <tspan class="ok">[  OK  ]</tspan></text>

  <line x1="30" y1="265" x2="820" y2="265" stroke="{ac}" stroke-width="0.5" opacity="0.3"/>

  <!-- Kernel Boot -->
  <text x="30" y="290" class="title" style="animation: fadeIn 0.5s forwards; opacity:0; animation-delay:1.2s">Booting {d["distro"]} v{d["ver"]} "{d["codename"]}"  //  Kernel {d["kernel"]}</text>

  <!-- Module Loading with animated bars -->
  {module_lines}

  <!-- Final -->
  <text x="30" y="{final_y}" class="motd" style="animation-delay:{final_delay}s">&gt; {d["motd"]}</text>
  <text x="30" y="{final_y + 30}" class="bios" style="animation-delay:{final_delay + 0.3}s">varshuai@mass-coder:~$ <tspan class="cursor">_</tspan></text>

  <!-- Scanline overlay -->
  <rect x="0" y="0" width="850" height="2" fill="{ac}" opacity="0.03">
    <animate attributeName="y" from="0" to="{final_y + 80}" dur="4s" repeatCount="indefinite"/>
  </rect>
</svg>'''


# ═══════════════════════════════════════════════
# SVG 2: ANIMATED NEOFETCH
# ═══════════════════════════════════════════════

def make_neofetch_svg():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="850" height="380" viewBox="0 0 850 380">
  <style>
    @keyframes fadeIn {{ from {{ opacity: 0; transform: translateY(5px); }} to {{ opacity: 1; transform: translateY(0); }} }}
    @keyframes blink {{ 0%,100% {{ opacity: 1; }} 50% {{ opacity: 0; }} }}
    @keyframes glowPulse {{ 0%,100% {{ opacity: 0.2; }} 50% {{ opacity: 0.5; }} }}

    .bg {{ fill: {bg}; }}
    .border {{ fill: none; stroke: {ac}; stroke-width: 1; opacity: 0.3; }}
    .label {{ font-family: 'Courier New', monospace; font-size: 13px; fill: {ac}; font-weight: bold; }}
    .value {{ font-family: 'Courier New', monospace; font-size: 13px; fill: #8B949E; }}
    .ascii {{ font-family: 'Courier New', monospace; font-size: 14px; fill: {ac}; }}
    .user {{ font-family: 'Courier New', monospace; font-size: 14px; fill: {ac2}; font-weight: bold; }}
    .sep {{ font-family: 'Courier New', monospace; font-size: 13px; fill: {ac}; opacity: 0.5; }}
    .line {{ animation: fadeIn 0.4s forwards; opacity: 0; }}
    .cursor {{ animation: blink 1s infinite; }}
    .glow {{ fill: {glow}; filter: blur(50px); animation: glowPulse 3s infinite; }}
    .cmd {{ font-family: 'Courier New', monospace; font-size: 13px; fill: {ac}; }}
  </style>

  <rect width="850" height="380" class="bg"/>
  <rect x="5" y="5" width="840" height="370" rx="8" class="border"/>
  <ellipse cx="200" cy="180" rx="120" ry="80" class="glow"/>

  <!-- Command -->
  <text x="30" y="35" class="cmd" style="animation: fadeIn 0.3s forwards; opacity:0">varshuai@mass-coder:~$ neofetch</text>

  <!-- ASCII Art -->
  <text x="40" y="80" class="ascii line" style="animation-delay:0.5s">        .--.       </text>
  <text x="40" y="98" class="ascii line" style="animation-delay:0.6s">       |o_o |      </text>
  <text x="40" y="116" class="ascii line" style="animation-delay:0.7s">       |:_/ |      </text>
  <text x="40" y="134" class="ascii line" style="animation-delay:0.8s">      //   \\ \\   </text>
  <text x="40" y="152" class="ascii line" style="animation-delay:0.9s">     (|     | )    </text>
  <text x="40" y="170" class="ascii line" style="animation-delay:1.0s">    /'\\\_   _/`\\  </text>
  <text x="40" y="188" class="ascii line" style="animation-delay:1.1s">    \\___)=(___/   </text>

  <!-- Info -->
  <text x="260" y="80" class="line" style="animation-delay:0.5s"><tspan class="user">varshuai</tspan><tspan class="sep">@</tspan><tspan class="user">mass-coder</tspan></text>
  <text x="260" y="98" class="sep line" style="animation-delay:0.6s">------------------------</text>
  <text x="260" y="118" class="line" style="animation-delay:0.7s"><tspan class="label">OS      </tspan><tspan class="value">{d["distro"]} v{d["ver"]} "{d["codename"]}"</tspan></text>
  <text x="260" y="138" class="line" style="animation-delay:0.8s"><tspan class="label">Kernel  </tspan><tspan class="value">{d["kernel"]}</tspan></text>
  <text x="260" y="158" class="line" style="animation-delay:0.9s"><tspan class="label">Shell   </tspan><tspan class="value">/bin/mass_code</tspan></text>
  <text x="260" y="178" class="line" style="animation-delay:1.0s"><tspan class="label">Uptime  </tspan><tspan class="value">mass_days (since day one)</tspan></text>
  <text x="260" y="198" class="line" style="animation-delay:1.1s"><tspan class="label">Repos   </tspan><tspan class="value">197+ (and counting)</tspan></text>
  <text x="260" y="218" class="line" style="animation-delay:1.2s"><tspan class="label">Lang    </tspan><tspan class="value">Python, JS, TS, Go, Rust, C++</tspan></text>
  <text x="260" y="238" class="line" style="animation-delay:1.3s"><tspan class="label">        </tspan><tspan class="value">Dart, Java, Kotlin, Bash, SQL</tspan></text>
  <text x="260" y="258" class="line" style="animation-delay:1.4s"><tspan class="label">Chai    </tspan><tspan class="value">filter &gt; instant (always)</tspan></text>
  <text x="260" y="278" class="line" style="animation-delay:1.5s"><tspan class="label">Editor  </tspan><tspan class="value">VS Code / Vim (depends on mood)</tspan></text>
  <text x="260" y="298" class="line" style="animation-delay:1.6s"><tspan class="label">Theme   </tspan><tspan class="value">{d["distro"]} [{day}]</tspan></text>
  <text x="260" y="318" class="line" style="animation-delay:1.7s"><tspan class="label">Status  </tspan><tspan class="value">{d["motd"]}</tspan></text>

  <!-- Color blocks -->
  <g class="line" style="animation-delay:1.9s">
    <rect x="260" y="335" width="20" height="20" fill="#0D1117"/>
    <rect x="283" y="335" width="20" height="20" fill="#FF0000"/>
    <rect x="306" y="335" width="20" height="20" fill="#00FF41"/>
    <rect x="329" y="335" width="20" height="20" fill="#FFD700"/>
    <rect x="352" y="335" width="20" height="20" fill="#0074D9"/>
    <rect x="375" y="335" width="20" height="20" fill="#FF00FF"/>
    <rect x="398" y="335" width="20" height="20" fill="#00FFFF"/>
    <rect x="421" y="335" width="20" height="20" fill="#FFFFFF"/>
  </g>

  <!-- Scanline -->
  <rect x="0" y="0" width="850" height="2" fill="{ac}" opacity="0.03">
    <animate attributeName="y" from="0" to="380" dur="3s" repeatCount="indefinite"/>
  </rect>
</svg>'''


# ═══════════════════════════════════════════════
# SVG 3: ANIMATED SKILLS / PACKAGES
# ═══════════════════════════════════════════════

def make_skills_svg():
    skills = [
        ("Security Research", 95),
        ("Python", 93),
        ("System Design", 93),
        ("Cloud / DevOps", 92),
        ("JavaScript", 90),
        ("Bash Scripting", 90),
        ("TypeScript", 87),
        ("Java", 85),
        ("Go", 82),
        ("AI / ML", 80),
        ("Rust", 75),
    ]

    h = 80 + len(skills) * 38 + 30
    lines = ""
    for i, (name, pct) in enumerate(skills):
        y = 75 + i * 38
        delay = 0.3 + i * 0.2
        bar_w = int(pct * 4.5)

        lines += f'''
    <g class="line" style="animation-delay:{delay}s">
      <text x="30" y="{y}" class="label">{name}</text>
      <rect x="220" y="{y - 13}" width="450" height="18" rx="4" fill="#21262D"/>
      <rect x="220" y="{y - 13}" width="0" height="18" rx="4" fill="{ac}" opacity="0.7">
        <animate attributeName="width" from="0" to="{bar_w}" dur="1s" begin="{delay}s" fill="freeze"/>
      </rect>
      <rect x="220" y="{y - 13}" width="0" height="18" rx="4" fill="{glow}">
        <animate attributeName="width" from="0" to="{bar_w}" dur="1s" begin="{delay}s" fill="freeze"/>
      </rect>
      <text x="690" y="{y}" class="pct">{pct}%</text>
    </g>'''

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="850" height="{h}" viewBox="0 0 850 {h}">
  <style>
    @keyframes fadeIn {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}
    .bg {{ fill: {bg}; }}
    .border {{ fill: none; stroke: {ac}; stroke-width: 1; opacity: 0.3; }}
    .label {{ font-family: 'Courier New', monospace; font-size: 13px; fill: #C9D1D9; }}
    .pct {{ font-family: 'Courier New', monospace; font-size: 12px; fill: {ac}; font-weight: bold; }}
    .title {{ font-family: 'Courier New', monospace; font-size: 14px; fill: {ac}; font-weight: bold; }}
    .line {{ animation: fadeIn 0.4s forwards; opacity: 0; }}
  </style>

  <rect width="850" height="{h}" class="bg"/>
  <rect x="5" y="5" width="840" height="{h - 10}" rx="8" class="border"/>

  <text x="30" y="35" class="title">varshuai@mass-coder:~$ cat /proc/skill-levels</text>
  <line x1="30" y1="48" x2="820" y2="48" stroke="{ac}" stroke-width="0.5" opacity="0.2"/>

  {lines}
</svg>'''


# ═══════════════════════════════════════════════
# README GENERATOR
# ═══════════════════════════════════════════════

def make_readme():
    border_hex = d["border"].replace("#", "")
    accent_hex = d["accent"].replace("#", "")
    accent2_hex = d["accent2"].replace("#", "")

    return f"""<!--
  VarshuOS v{d["ver"]} "{d["codename"]}" | {short_date} | This README is alive.
-->

<div align="center">

<!-- ANIMATED BOOT SEQUENCE -->
<img src="https://raw.githubusercontent.com/VarshuAi/VarshuAi/main/assets/boot.svg" width="100%" alt="VarshuOS Boot Sequence"/>

<br>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

</div>

<!-- ═══════ APPS / CLICKABLE SECTIONS ═══════ -->

<details>
<summary>&nbsp;&nbsp;<b>📂 /home/varshuai/about.txt</b>&nbsp;&nbsp;—&nbsp;&nbsp;<code>cat about.txt</code></summary>

<br>

<div align="center">

| | |
|:--|:--|
| **Name** | Varshan Gowda |
| **Handle** | @VarshuAi |
| **From** | India |
| **What I am** | Just a guy who codes |
| **Student?** | Nope |
| **Why I code** | Because it's fun |
| **Repos** | 197+ and I'm not stopping |
| **Sleep** | Optional |
| **Chai** | Mandatory |

</div>

> *I'm not a "developer" or an "engineer". I'm an Indian guy who just loves coding and mass uploading stuff. I see a problem, I build a solution, I push it at 3 AM. That's the whole bio.*

<br>
</details>

---

<details>
<summary>&nbsp;&nbsp;<b>📊 /proc/skill-levels</b>&nbsp;&nbsp;—&nbsp;&nbsp;<code>Animated proficiency bars</code></summary>

<br>

<div align="center">
<img src="https://raw.githubusercontent.com/VarshuAi/VarshuAi/main/assets/skills.svg" width="100%" alt="Skill Levels"/>
</div>

<br>
</details>

---

<details>
<summary>&nbsp;&nbsp;<b>📦 /usr/bin/packages</b>&nbsp;&nbsp;—&nbsp;&nbsp;<code>Installed tech stack</code></summary>

<br>

<div align="center">

#### Languages
<img src="https://skillicons.dev/icons?i=python,javascript,typescript,go,rust,cpp,dart,java,kotlin,bash&perline=10&theme=dark" />

#### Frameworks
<img src="https://skillicons.dev/icons?i=react,nextjs,nodejs,express,fastapi,flask,django,flutter,tailwind,vue,svelte,graphql&perline=12&theme=dark" />

#### Security & DevOps
<img src="https://skillicons.dev/icons?i=kali,docker,kubernetes,terraform,githubactions,linux,nginx,ansible&perline=8&theme=dark" />

#### Cloud & Data
<img src="https://skillicons.dev/icons?i=aws,gcp,azure,firebase,mongodb,postgres,redis,supabase&perline=8&theme=dark" />

#### AI & ML
<img src="https://skillicons.dev/icons?i=tensorflow,pytorch&perline=5&theme=dark" />

</div>

<br>
</details>

---

<details>
<summary>&nbsp;&nbsp;<b>🔐 /opt/security-arsenal</b>&nbsp;&nbsp;—&nbsp;&nbsp;<code>150+ tools loaded</code></summary>

<br>

```
 /opt/security-arsenal/
 ├── recon/           nmap, masscan, amass, subfinder, shodan
 ├── exploitation/    metasploit, sqlmap, burpsuite, hydra
 ├── analysis/        wireshark, ghidra, ida-pro, radare2, volatility
 ├── wireless/        aircrack-ng, wifite, bettercap
 ├── web/             owasp-zap, nikto, ffuf, nuclei
 └── osint/           maltego, theHarvester, sherlock

 150+ tools loaded. arsenal: ARMED.
```

<br>
</details>

---

<details>
<summary>&nbsp;&nbsp;<b>📈 /proc/github-stats</b>&nbsp;&nbsp;—&nbsp;&nbsp;<code>Live surveillance data</code></summary>

<br>

<div align="center">

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/VarshuAi">
        <img src="https://github-readme-stats-sigma-five.vercel.app/api?username=VarshuAi&show_icons=true&bg_color=0D1117&border_color={border_hex}&title_color={accent_hex}&icon_color={accent2_hex}&text_color=8B949E&count_private=true&include_all_commits=true" height="195px">
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/VarshuAi">
        <img src="https://github-readme-stats-sigma-five.vercel.app/api/top-langs/?username=VarshuAi&layout=compact&bg_color=0D1117&border_color={border_hex}&title_color={accent_hex}&text_color=8B949E&langs_count=10&card_width=400" height="195px">
      </a>
    </td>
  </tr>
  <tr>
    <td colspan="2" align="center">
      <br>
      <img src="https://streak-stats.demolab.com?user=VarshuAi&background=0D1117&border={border_hex}&ring={accent_hex}&fire={accent2_hex}&currStreakLabel={accent2_hex}&sideLabels={accent_hex}&currStreakNum=C9D1D9&sideNums=C9D1D9&dates=555555" height="195px">
    </td>
  </tr>
</table>

<br>

<img src="https://github-readme-activity-graph.vercel.app/graph?username=VarshuAi&bg_color=0D1117&color={accent_hex}&line={accent2_hex}&point={accent_hex}&area_color={accent_hex}22&area=true&hide_border=true" width="98%">

</div>

<br>
</details>

---

<details>
<summary>&nbsp;&nbsp;<b>📁 /home/varshuai/projects/</b>&nbsp;&nbsp;—&nbsp;&nbsp;<code>Featured repos</code></summary>

<br>

<div align="center">
<table>
<tr>
<td width="50%">
<a href="https://github.com/VarshuAi/go-ssh-auditor"><img src="https://github-readme-stats-sigma-five.vercel.app/api/pin/?username=VarshuAi&repo=go-ssh-auditor&bg_color=0D1117&border_color={border_hex}&title_color={accent_hex}&icon_color={accent2_hex}&text_color=8B949E"></a>
</td>
<td width="50%">
<a href="https://github.com/VarshuAi/py-packet-sniffer"><img src="https://github-readme-stats-sigma-five.vercel.app/api/pin/?username=VarshuAi&repo=py-packet-sniffer&bg_color=0D1117&border_color={border_hex}&title_color={accent_hex}&icon_color={accent2_hex}&text_color=8B949E"></a>
</td>
</tr>
<tr>
<td width="50%">
<a href="https://github.com/VarshuAi/rust-port-scanner"><img src="https://github-readme-stats-sigma-five.vercel.app/api/pin/?username=VarshuAi&repo=rust-port-scanner&bg_color=0D1117&border_color={border_hex}&title_color={accent_hex}&icon_color={accent2_hex}&text_color=8B949E"></a>
</td>
<td width="50%">
<a href="https://github.com/VarshuAi/bash-sys-monitor"><img src="https://github-readme-stats-sigma-five.vercel.app/api/pin/?username=VarshuAi&repo=bash-sys-monitor&bg_color=0D1117&border_color={border_hex}&title_color={accent_hex}&icon_color={accent2_hex}&text_color=8B949E"></a>
</td>
</tr>
</table>
</div>

<br>
</details>

---

<details>
<summary>&nbsp;&nbsp;<b>🐍 /var/log/contributions</b>&nbsp;&nbsp;—&nbsp;&nbsp;<code>Movement pattern</code></summary>

<br>

<div align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/platane/snk/output/github-contribution-grid-snake-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/platane/snk/output/github-contribution-grid-snake.svg">
  <img alt="Snake animation" src="https://raw.githubusercontent.com/platane/snk/output/github-contribution-grid-snake-dark.svg" width="100%">
</picture>
</div>

<br>
</details>

---

<!-- NEOFETCH -->
<div align="center">

<img src="https://raw.githubusercontent.com/VarshuAi/VarshuAi/main/assets/neofetch.svg" width="100%" alt="neofetch"/>

<br><br>

<img src="https://komarev.com/ghpvc/?username=VarshuAi&label=ssh+connections&style=flat-square&color={accent_hex}" alt="visitors">

<br>

<sub><code>VarshuOS v{d["ver"]} "{d["codename"]}" | {d["kernel"]} | rotated {short_date} | powered by mass chai</code></sub>

<br>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0D1117,50:{accent_hex},100:0D1117&height=100&section=footer" width="100%"/>

</div>
"""


# ═══════════════════════════════════════════════
# MAIN — Generate everything
# ═══════════════════════════════════════════════

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    assets_dir = os.path.join(repo_root, "assets")
    os.makedirs(assets_dir, exist_ok=True)

    # Write SVGs
    with open(os.path.join(assets_dir, "boot.svg"), "w", encoding="utf-8") as f:
        f.write(make_boot_svg())

    with open(os.path.join(assets_dir, "neofetch.svg"), "w", encoding="utf-8") as f:
        f.write(make_neofetch_svg())

    with open(os.path.join(assets_dir, "skills.svg"), "w", encoding="utf-8") as f:
        f.write(make_skills_svg())

    # Write README
    with open(os.path.join(repo_root, "README.md"), "w", encoding="utf-8") as f:
        f.write(make_readme())

    print("[OK] VarshuOS v2 generated!")
    print(f"Day: {day}")
    print(f"Distro: {d['distro']} v{d['ver']} ({d['codename']})")
    print(f"Files: README.md, assets/boot.svg, assets/neofetch.svg, assets/skills.svg")
