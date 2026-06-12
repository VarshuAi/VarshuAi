"""
VarshuOS — A Fake Operating System as a GitHub README
─────────────────────────────────────────────────────
Your profile IS a computer. Visitors watch it boot up,
login, and can click "apps" to explore sections.

Each day of the week = a different Linux distro theme.
"""

import datetime
import os
import urllib.parse

IST = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
today = datetime.datetime.now(IST)
day = today.strftime("%A")
date_str = today.strftime("%a %b %d %H:%M:%S IST %Y")
short_date = today.strftime("%d %b %Y")

# ── DAILY DISTRO THEMES ──────────────────────────────

DISTROS = {
    "Monday":    {"distro": "RedStrike OS",  "ver": "14.2",  "kernel": "6.8.0-redstrike",   "accent": "FF0000", "accent2": "FF6B6B", "border": "8B0000", "codename": "Inferno",     "motd": "New week. New exploits. No mercy.", "pkg_mgr": "dnf"},
    "Tuesday":   {"distro": "DeepBlue OS",   "ver": "12.1",  "kernel": "6.8.0-deepblue",    "accent": "0074D9", "accent2": "7FDBFF", "border": "001F54", "codename": "Abyss",       "motd": "Silence the noise. Enter the flow.", "pkg_mgr": "apt"},
    "Wednesday": {"distro": "NeonArc OS",    "ver": "3.7",   "kernel": "6.8.0-neonarc",     "accent": "FF00FF", "accent2": "DA70D6", "border": "6C0BA9", "codename": "Glitch",      "motd": "Midweek. Maximum output. No excuses.", "pkg_mgr": "pacman"},
    "Thursday":  {"distro": "ForestRoot OS", "ver": "22.04", "kernel": "6.8.0-forestroot",  "accent": "00FF41", "accent2": "A8E6CF", "border": "0B3D0B", "codename": "Banyan",      "motd": "Grow one commit at a time.", "pkg_mgr": "apt"},
    "Friday":    {"distro": "GoldRush OS",   "ver": "40.1",  "kernel": "6.8.0-goldrush",    "accent": "FFD700", "accent2": "FFE066", "border": "B8860B", "codename": "Midas",       "motd": "Ship it. Its Friday. YOLO.", "pkg_mgr": "dnf"},
    "Saturday":  {"distro": "CyberKali OS",  "ver": "2024.3","kernel": "6.8.0-cyberkali",   "accent": "00FFFF", "accent2": "FF1493", "border": "008B8B", "codename": "Phantom",     "motd": "No rules. No deadlines. Pure chaos.", "pkg_mgr": "apt"},
    "Sunday":    {"distro": "ZenMint OS",    "ver": "21.3",  "kernel": "6.8.0-zenmint",     "accent": "FF6347", "accent2": "FF8C00", "border": "8B4513", "codename": "Satori",      "motd": "Rest day. Opens laptop anyway.", "pkg_mgr": "apt"},
}

d = DISTROS[day]

readme = f"""<!--
  VarshuOS v{d["ver"]} "{d["codename"]}" | Auto-rotated: {short_date}
  This README IS an operating system. It boots daily into a new distro.
  Come back tomorrow — it'll be a completely different OS.
-->

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=rect&color=0D1117&height=1" width="100%"/>
</div>

```
                                                                              
                                                                              
  ██╗   ██╗ █████╗ ██████╗ ███████╗██╗  ██╗██╗   ██╗     ██████╗ ███████╗    
  ██║   ██║██╔══██╗██╔══██╗██╔════╝██║  ██║██║   ██║    ██╔═══██╗██╔════╝    
  ██║   ██║███████║██████╔╝███████╗███████║██║   ██║    ██║   ██║███████╗    
  ╚██╗ ██╔╝██╔══██║██╔══██╗╚════██║██╔══██║██║   ██║    ██║   ██║╚════██║    
   ╚████╔╝ ██║  ██║██║  ██║███████║██║  ██║╚██████╔╝    ╚██████╔╝███████║    
    ╚═══╝  ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝      ╚═════╝ ╚══════╝    
                                                                              
```

```
 ┌─────────────────────────────────────────────────────────────────────────┐
 │                        VARSHUOS BIOS v4.20.69                          │
 │─────────────────────────────────────────────────────────────────────────│
 │                                                                         │
 │  CPU      : Varshan Gowda @ mass_clock_speed          [  OK  ]         │
 │  RAM      : Mass Creativity (Unlimited GB)             [  OK  ]         │
 │  GPU      : Imagination RTX 9090 Ti                    [  OK  ]         │
 │  STORAGE  : 197+ Repositories (Expanding...)           [  OK  ]         │
 │  NETWORK  : Connected to Open Source Network           [  OK  ]         │
 │  CHAI     : Filter Coffee Module Loaded                [  OK  ]         │
 │                                                                         │
 │  Keyboard : Indian Standard (Chai-Resistant)           [  OK  ]         │
 │  Audio    : Lo-fi Hip Hop Radio                        [  OK  ]         │
 │  Clock    : 3:00 AM (Normal Operating Hours)           [  OK  ]         │
 │                                                                         │
 │  All systems nominal. Booting {d["distro"]} v{d["ver"]}...                       │
 │                                                                         │
 └─────────────────────────────────────────────────────────────────────────┘
```

```
[    0.000000] VarshuOS kernel {d["kernel"]} booting...
[    0.000001] Command line: BOOT_IMAGE=/vmlinuz root=/dev/mass_coding
[    0.042069] India/Kolkata timezone loaded. Chai dependency resolved.
[    0.100000] Loading distro: {d["distro"]} v{d["ver"]} "{d["codename"]}"
[    0.200000] Mounting /dev/github ... 197+ repos found
[    0.300000] Mounting /dev/brain ... creativity: UNLIMITED
[    0.400000] Loading module: python3.12 .................... [ OK ]
[    0.410000] Loading module: javascript-v8 ................. [ OK ]
[    0.420000] Loading module: typescript-strict .............. [ OK ]
[    0.430000] Loading module: golang-1.22 ................... [ OK ]
[    0.440000] Loading module: rust-nightly .................. [ OK ]
[    0.450000] Loading module: security-toolkit .............. [ OK ]
[    0.460000] Loading module: chai-brewing-engine ........... [ OK ]
[    0.500000] Loading module: mass-uploader-daemon .......... [ OK ]
[    0.600000] Network: GitHub API connected (rate limit: mass_pushing)
[    0.700000] Starting display manager...
[    0.800000] Welcome to {d["distro"]}. {d["motd"]}
[    1.000000] Login: varshuai | Shell: /bin/mass_code
```

```
┌─────────────────────────────────────────────────────────────────────────┐
│  {d["distro"]} v{d["ver"]} "{d["codename"]}"                                               │
│  {date_str}                                              │
│                                                                         │
│  varshuai@mass-coder:~$                                                 │
│                                                                         │
│  Welcome back, Varshan.                                                 │
│  Today is {day}. Distro: {d["distro"]}.                                      │
│  "{d["motd"]}"                                                │
│                                                                         │
│  Last login: yesterday from mass-coding-session                         │
│  Repos: 197+ | Languages: 11 | Uptime: mass_days                       │
│  Chai consumed today: yes                                               │
│                                                                         │
│  Type 'help' or click an app below to explore.                          │
└─────────────────────────────────────────────────────────────────────────┘
```

<div align="center">

> **`{d["distro"]} v{d["ver"]}`** · `Kernel: {d["kernel"]}`  · `Theme rotates daily across 7 distros` · `Today: {day}`

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">

</div>

<!-- ═══════════ DESKTOP — CLICKABLE APPS ═══════════ -->

<details>
<summary><b>📂 /home/varshuai/about.txt</b> — <i>cat about.txt</i></summary>

<br>

```
varshuai@mass-coder:~$ cat about.txt
```

```yaml

  ┌─────────────────────────────────────────────────────────────┐
  │                                                             │
  │  Name        Varshan Gowda                                  │
  │  Handle      @VarshuAi                                      │
  │  Location    India                                          │
  │  Title       just a guy who codes                           │
  │  Student     nope                                           │
  │  Degree      doesn't matter                                 │
  │  Why I code  because its fun                                │
  │                                                             │
  │  What I actually do:                                        │
  │    > see a problem                                          │
  │    > build a solution                                       │
  │    > mass upload to GitHub at 3 AM                          │
  │    > drink chai                                             │
  │    > repeat                                                 │
  │                                                             │
  │  Repos       197+ and counting                              │
  │  Languages   11 (lost count honestly)                       │
  │  Sleep       optional                                       │
  │  Chai        mandatory                                      │
  │                                                             │
  │  I'm not a "developer" or an "engineer".                    │
  │  I'm an Indian guy who just loves coding                    │
  │  and uploading stuff. That's the whole bio.                 │
  │                                                             │
  └─────────────────────────────────────────────────────────────┘

```

```
varshuai@mass-coder:~$ _
```

</details>

---

<details>
<summary><b>📦 /usr/bin/{d["pkg_mgr"]}</b> — <i>{d["pkg_mgr"]} list --installed</i> (Tech Stack)</summary>

<br>

```
varshuai@mass-coder:~$ {d["pkg_mgr"]} list --installed | grep -E "(lang|framework|tool)"
```

```apache
PACKAGE                          VERSION        STATUS       PROFICIENCY
─────────────────────────────────────────────────────────────────────────
python3                          3.12.4         installed    ████████████████████ 93%
javascript/node                  22.0.0         installed    ███████████████████░ 90%
typescript                       5.5.0          installed    ██████████████████░░ 87%
golang                           1.22.0         installed    █████████████████░░░ 82%
rust                             nightly        installed    ███████████████░░░░░ 75%
cpp/gcc                          14.0.0         installed    ████████████████░░░░ 78%
dart                             3.4.0          installed    ████████████████░░░░ 80%
java/openjdk                     21.0.0         installed    █████████████████░░░ 85%
kotlin                           2.0.0          installed    ████████████████░░░░ 76%
bash                             5.2.0          installed    ███████████████████░ 90%
sql/postgresql                   16.0           installed    █████████████████░░░ 85%
```

```
varshuai@mass-coder:~$ {d["pkg_mgr"]} list --installed | grep "framework"
```

```apache
PACKAGE                          VERSION        STATUS       TYPE
─────────────────────────────────────────────────────────────────────────
react                            18.3.0         installed    frontend
nextjs                           14.2.0         installed    fullstack
nodejs/express                   4.19.0         installed    backend
fastapi                          0.111.0        installed    backend
flask                            3.0.0          installed    backend
django                           5.0.0          installed    backend
flutter                          3.22.0         installed    mobile
tailwindcss                      3.4.0          installed    css
vue                              3.4.0          installed    frontend
svelte                           4.2.0          installed    frontend
graphql                          16.8.0         installed    api
```

```
varshuai@mass-coder:~$ {d["pkg_mgr"]} list --installed | grep "cloud"
```

```apache
PACKAGE                          VERSION        STATUS
─────────────────────────────────────────────────────────────────
aws-cli                          2.15.0         installed
gcloud-sdk                       472.0          installed
azure-cli                        2.60.0         installed
firebase-tools                   13.0.0         installed
docker-ce                        26.0.0         installed
kubectl                          1.30.0         installed
terraform                        1.8.0          installed
```

```
varshuai@mass-coder:~$ {d["pkg_mgr"]} list --installed | grep "ai"
```

```apache
PACKAGE                          VERSION        STATUS
─────────────────────────────────────────────────────────────────
tensorflow                       2.16.0         installed
pytorch                          2.3.0          installed
openai-sdk                       1.30.0         installed
huggingface-hub                  0.23.0         installed
langchain                        0.2.0          installed
```

```
varshuai@mass-coder:~$ echo "total packages: mass_amount"
total packages: mass_amount
varshuai@mass-coder:~$ _
```

</details>

---

<details>
<summary><b>🔐 /opt/security-arsenal</b> — <i>ls -la /opt/security-arsenal/</i></summary>

<br>

```
varshuai@mass-coder:~$ ls -la /opt/security-arsenal/
total 150+
```

```
drwxr-xr-x  varshuai  recon/
  ├── nmap                    # network discovery & port scanning
  ├── masscan                 # mass IP port scanner  
  ├── amass                   # subdomain enumeration
  ├── subfinder               # passive subdomain discovery
  └── shodan-cli              # internet-wide scanning

drwxr-xr-x  varshuai  exploitation/
  ├── metasploit-framework    # penetration testing framework
  ├── sqlmap                  # SQL injection automation
  ├── burpsuite-pro           # web vulnerability scanner
  ├── cobalt-strike           # adversary simulation
  └── hydra                   # brute force tool

drwxr-xr-x  varshuai  analysis/
  ├── wireshark               # packet analysis
  ├── ghidra                  # reverse engineering (NSA)
  ├── ida-pro                 # disassembler
  ├── radare2                 # RE framework
  └── volatility              # memory forensics

drwxr-xr-x  varshuai  wireless/
  ├── aircrack-ng             # WiFi security auditing
  ├── wifite                  # automated wireless attack
  └── bettercap               # MITM framework

drwxr-xr-x  varshuai  web/
  ├── owasp-zap               # web app scanner
  ├── nikto                   # web server scanner
  ├── ffuf                    # web fuzzer
  └── nuclei                  # vulnerability scanner

drwxr-xr-x  varshuai  osint/
  ├── maltego                 # OSINT & graphing
  ├── theHarvester            # email/domain recon
  └── sherlock                # social media hunter

150+ tools loaded. arsenal status: ARMED.
```

```
varshuai@mass-coder:~$ _
```

</details>

---

<details>
<summary><b>📊 /proc/github-stats</b> — <i>cat /proc/github-stats</i> (Live Metrics)</summary>

<br>

```
varshuai@mass-coder:~$ cat /proc/github-stats
```

<div align="center">

<table align="center">
  <tr>
    <td align="center">
      <a href="https://github.com/VarshuAi">
        <img src="https://github-readme-stats-sigma-five.vercel.app/api?username=VarshuAi&show_icons=true&bg_color=0D1117&border_color={d["border"]}&title_color={d["accent"]}&icon_color={d["accent2"]}&text_color=8B949E&count_private=true&include_all_commits=true" alt="Stats" height="195px">
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/VarshuAi">
        <img src="https://github-readme-stats-sigma-five.vercel.app/api/top-langs/?username=VarshuAi&layout=compact&bg_color=0D1117&border_color={d["border"]}&title_color={d["accent"]}&text_color=8B949E&langs_count=10&card_width=400" alt="Langs" height="195px">
      </a>
    </td>
  </tr>
  <tr>
    <td align="center" colspan="2">
      <br>
      <img src="https://streak-stats.demolab.com?user=VarshuAi&background=0D1117&border={d["border"]}&ring={d["accent"]}&fire={d["accent2"]}&currStreakLabel={d["accent2"]}&sideLabels={d["accent"]}&currStreakNum=C9D1D9&sideNums=C9D1D9&dates=555555" alt="Streak" height="195px">
    </td>
  </tr>
</table>

<br>

<img src="https://github-readme-activity-graph.vercel.app/graph?username=VarshuAi&bg_color=0D1117&color={d["accent"]}&line={d["accent2"]}&point={d["accent"]}&area_color={d["accent"]}22&area=true&hide_border=true&custom_title=varshuai@mass-coder:~$+cat+/var/log/commits.log" width="98%">

</div>

```
varshuai@mass-coder:~$ _
```

</details>

---

<details>
<summary><b>📁 /home/varshuai/projects/</b> — <i>ls -la ~/projects/</i> (Featured Work)</summary>

<br>

```
varshuai@mass-coder:~$ ls -la ~/projects/

drwxr-xr-x  varshuai  go-ssh-auditor/       # SSH security audit tool
drwxr-xr-x  varshuai  py-packet-sniffer/    # raw socket packet capture
drwxr-xr-x  varshuai  rust-port-scanner/    # async port scanner
drwxr-xr-x  varshuai  bash-sys-monitor/     # system monitoring dashboard
drwxr-xr-x  varshuai  ...194 more repos...  # I told you, MASS uploads
```

<div align="center">

<table>
<tr>
<td width="50%">
<a href="https://github.com/VarshuAi/go-ssh-auditor"><img src="https://github-readme-stats-sigma-five.vercel.app/api/pin/?username=VarshuAi&repo=go-ssh-auditor&bg_color=0D1117&border_color={d["border"]}&title_color={d["accent"]}&icon_color={d["accent2"]}&text_color=8B949E" alt="go-ssh-auditor"></a>
</td>
<td width="50%">
<a href="https://github.com/VarshuAi/py-packet-sniffer"><img src="https://github-readme-stats-sigma-five.vercel.app/api/pin/?username=VarshuAi&repo=py-packet-sniffer&bg_color=0D1117&border_color={d["border"]}&title_color={d["accent"]}&icon_color={d["accent2"]}&text_color=8B949E" alt="py-packet-sniffer"></a>
</td>
</tr>
<tr>
<td width="50%">
<a href="https://github.com/VarshuAi/rust-port-scanner"><img src="https://github-readme-stats-sigma-five.vercel.app/api/pin/?username=VarshuAi&repo=rust-port-scanner&bg_color=0D1117&border_color={d["border"]}&title_color={d["accent"]}&icon_color={d["accent2"]}&text_color=8B949E" alt="rust-port-scanner"></a>
</td>
<td width="50%">
<a href="https://github.com/VarshuAi/bash-sys-monitor"><img src="https://github-readme-stats-sigma-five.vercel.app/api/pin/?username=VarshuAi&repo=bash-sys-monitor&bg_color=0D1117&border_color={d["border"]}&title_color={d["accent"]}&icon_color={d["accent2"]}&text_color=8B949E" alt="bash-sys-monitor"></a>
</td>
</tr>
</table>

</div>

```
varshuai@mass-coder:~$ _
```

</details>

---

<details>
<summary><b>🗺️ /etc/varshuai/domains.conf</b> — <i>cat /etc/varshuai/domains.conf</i></summary>

<br>

```
varshuai@mass-coder:~$ cat /etc/varshuai/domains.conf
```

```nginx
# ╔═══════════════════════════════════════════════════════════════════╗
# ║               VARSHUAI COMPETENCY MAP                            ║
# ╠═══════════════════════════════════════════════════════════════════╣
# ║                                                                   ║
# ║   DOMAIN              SKILLS                       LEVEL          ║
# ║   ─────────────────────────────────────────────────────────       ║
# ║                                                                   ║
# ║   Security            Pentesting, Vuln Research,   ██████ EXPERT  ║
# ║                       SIEM, Red Teaming                           ║
# ║                                                                   ║
# ║   Backend             Microservices, APIs,         ██████ EXPERT  ║
# ║                       Distributed Systems                         ║
# ║                                                                   ║
# ║   DevOps              CI/CD, IaC, K8s,             ██████ EXPERT  ║
# ║                       Container Orchestration                     ║
# ║                                                                   ║
# ║   Cloud               Multi-cloud, Serverless,     ██████ EXPERT  ║
# ║                       AWS + GCP + Azure                           ║
# ║                                                                   ║
# ║   Frontend            React, Next.js, Vue,         █████░ ADV     ║
# ║                       Animation, WebGL                            ║
# ║                                                                   ║
# ║   AI/ML               NLP, CV, LLM Fine-tuning,   █████░ ADV     ║
# ║                       RAG, Agents                                 ║
# ║                                                                   ║
# ║   Mobile              Flutter, React Native,       █████░ ADV     ║
# ║                       Native Android                              ║
# ║                                                                   ║
# ╚═══════════════════════════════════════════════════════════════════╝
```

```
varshuai@mass-coder:~$ _
```

</details>

---

<details>
<summary><b>🐍 /var/log/contributions.log</b> — <i>tail -f /var/log/contributions.log</i></summary>

<br>

```
varshuai@mass-coder:~$ tail -f /var/log/contributions.log
```

<div align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/platane/snk/output/github-contribution-grid-snake-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/platane/snk/output/github-contribution-grid-snake.svg">
  <img alt="Snake animation" src="https://raw.githubusercontent.com/platane/snk/output/github-contribution-grid-snake-dark.svg" width="100%">
</picture>
</div>

```
varshuai@mass-coder:~$ _
```

</details>

---

<details>
<summary><b>⚙️ /etc/varshuai/distro-rotation.conf</b> — <i>How this README works</i></summary>

<br>

```
varshuai@mass-coder:~$ cat /etc/varshuai/distro-rotation.conf
```

```bash
# ╔══════════════════════════════════════════════════════════════════╗
# ║         VARSHUOS DAILY DISTRO ROTATION TABLE                    ║
# ╠══════════════════════════════════════════════════════════════════╣
# ║                                                                  ║
# ║   DAY          DISTRO             CODENAME     VIBE              ║
# ║   ──────────────────────────────────────────────────────────     ║
# ║   Monday       RedStrike OS       Inferno      attack mode       ║
# ║   Tuesday      DeepBlue OS        Abyss        deep focus        ║
# ║   Wednesday    NeonArc OS         Glitch       midweek chaos     ║
# ║   Thursday     ForestRoot OS      Banyan       growth mode       ║
# ║   Friday       GoldRush OS        Midas        ship everything   ║
# ║   Saturday     CyberKali OS       Phantom      side projects     ║
# ║   Sunday       ZenMint OS         Satori       chill (but code)  ║
# ║                                                                  ║
# ║   * This README auto-rotates at midnight IST via GitHub Actions  ║
# ║   * Each distro has its own kernel, colors, and personality      ║
# ║   * Come back tomorrow to see a different OS boot up             ║
# ║                                                                  ║
# ║   TODAY: {day} — {d["distro"]} v{d["ver"]} "{d["codename"]}"
# ║                                                                  ║
# ╚══════════════════════════════════════════════════════════════════╝
```

```
varshuai@mass-coder:~$ _
```

</details>

---

<div align="center">

```
varshuai@mass-coder:~$ neofetch
```

```
                            varshuai@mass-coder
        .--.               ─────────────────────
       |o_o |              OS      {d["distro"]} v{d["ver"]} "{d["codename"]}"
       |:_/ |              Kernel  {d["kernel"]}
      //   \ \             Shell   /bin/mass_code
     (|     | )            Uptime  mass_days (since mass_day_one)
    /'\_   _/`\            Repos   197+
    \___)=(___/            Lang    Python, JS, TS, Go, Rust, C++,
                                   Dart, Java, Kotlin, Bash, SQL
                           Chai    filter > instant (always)
                           Editor  VS Code / Vim (depends on mood)
                           Theme   {d["distro"]} [{day}]
                           Status  {d["motd"]}
```

```
varshuai@mass-coder:~$ uptime
 mass_time up mass_days, 1 user, mass_load average: coding, coding, coding

varshuai@mass-coder:~$ echo "thanks for visiting. star a repo if you vibe."
thanks for visiting. star a repo if you vibe.

varshuai@mass-coder:~$ exit
logout
Connection to github.com/VarshuAi closed.
```

<br>

<img src="https://komarev.com/ghpvc/?username=VarshuAi&label=ssh+connections&style=flat-square&color={d["accent"]}" alt="visitors">

<br>

<sub><code>VarshuOS v{d["ver"]} "{d["codename"]}" | kernel {d["kernel"]} | auto-rotated on {short_date} | powered by mass chai</code></sub>

<br>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0D1117,50:{d["accent"]},100:0D1117&height=100&section=footer" width="100%"/>

</div>
"""

# ── WRITE ──
script_dir = os.path.dirname(os.path.abspath(__file__))
repo_root = os.path.dirname(script_dir)
readme_path = os.path.join(repo_root, "README.md")

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(readme)

print(f"[OK] VarshuOS README generated!")
print(f"Day: {day}")
print(f"Distro: {d['distro']} v{d['ver']} ({d['codename']})")
print(f"Written to: {readme_path}")
