import os
import sys
import json
import urllib.request
import urllib.parse
import urllib.error
import time
import base64
from datetime import datetime

# Reconfigure stdout to support UTF-8 characters on Windows terminal
sys.stdout.reconfigure(encoding='utf-8')

# Configuration
GITHUB_USERNAME = "VarshuAi"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")

# Map day of week to theme name
DAYS_MAP = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

# Theme details
THEME_CONFIGS = {
    "Monday": {
        "name": "Anime",
        "primary_color": "FF9EB5",  # Sakura Pink
        "bg_color": "000000",
        "border_color": "FF9EB5",
        "title_color": "FF9EB5",
        "icon_color": "c9b8ff",
        "text_color": "ffd6e0",
        "gradient": "ff9eb5,ffb7c5,ffd6e0,c9b8ff",
        "banner_type": "waving",
        "font": "Noto Sans JP",
        "emojis": ["🌸", "🍡", "✨", "⚔️", "💌", "🔮"],
        "typing_lines": [
            "🌸 Welcome to {} 🌸",
            "⚡ Built with {} • Optimized ⚡",
            "「最強のモジュール」"
        ],
        "profile_typing_lines": [
            "🌸 Security Researcher | Full-Stack Engineer 🌸",
            "✨ System Architect | DevSecOps Specialist ✨",
            "「最強のフルスタック」• 650+ Repositories"
        ],
        "headers": {
            "ABOUT": "🌸 ABOUT (Arc Begin)",
            "FEATURES": "✨ SPECIAL ABILITIES (Features)",
            "COMMANDS": "⚔️ COMBAT CONTROLS (Usage)",
            "TECH_STACK": "📦 INVENTORY (Tech Stack)",
            "SETUP": "🔮 RITUAL SUMMON (Setup)",
            "STRUCTURE": "📁 ARCHITECTURAL MAP (Structure)"
        }
    },
    "Tuesday": {
        "name": "Coding",
        "primary_color": "00FF41",  # Terminal Green
        "bg_color": "0D1117",
        "border_color": "00FF41",
        "title_color": "00FF41",
        "icon_color": "00FF41",
        "text_color": "00CC33",
        "gradient": "0d1117,1a1b27,0d1117",
        "banner_type": "rect",
        "font": "Fira Code",
        "emojis": ["💻", "⚙️", "🖥️", "📡", "📁", "🔌"],
        "typing_lines": [
            "$ python3 -m {}",
            "[OK] Loading dependencies...",
            "[OK] Main thread running...",
            "[OK] Status: Active"
        ],
        "profile_typing_lines": [
            ">_ Security Researcher | Full-Stack Engineer",
            ">_ System Architect | DevSecOps Specialist",
            ">_ Open-Source Contributor | 650+ Repos"
        ],
        "headers": {
            "ABOUT": "[>_] SYSTEM LOG (About)",
            "FEATURES": "[⚙️] SERVICE MODULES (Features)",
            "COMMANDS": "[📡] INPUT / OUTPUT (Usage)",
            "TECH_STACK": "[📦] DEPENDENCIES (Tech Stack)",
            "SETUP": "[⚡] ENVIRONMENT BOOT (Setup)",
            "STRUCTURE": "[📁] REPO_TREE (Structure)"
        }
    },
    "Wednesday": {
        "name": "Gaming",
        "primary_color": "FF007F",  # Neon Pink/Cyan
        "bg_color": "000000",
        "border_color": "FF007F",
        "title_color": "00f0ff",
        "icon_color": "ff007f",
        "text_color": "ffffff",
        "gradient": "ff007f,7000ff,00f0ff",
        "banner_type": "slice",
        "font": "Orbitron",
        "emojis": ["🎮", "👾", "🏆", "⚔️", "🛡️", "🏁"],
        "typing_lines": [
            "🎮 PRESS START 🎮",
            "⚡ LOADING {} MODULE... ⚡",
            "🏆 HIGH SCORE UNLOCKED 🏆"
        ],
        "profile_typing_lines": [
            "👾 PLAYER_1: VarshuAi | LEVEL: MAX 👾",
            "⚔️ Security Specialist | Quest Completed ⚔️",
            "🏆 Achievement Unlocked: 650+ Repos Created 🏆"
        ],
        "headers": {
            "ABOUT": "🎮 MISSION OBJECTIVES (About)",
            "FEATURES": "⚔️ SPECIAL SKILLS (Features)",
            "COMMANDS": "🕹️ GAME CONTROLS (Usage)",
            "TECH_STACK": "📦 INVENTORY BAG (Tech Stack)",
            "SETUP": "🏁 LEVEL SELECT (Setup)",
            "STRUCTURE": "🗺️ WORLD MAP (Structure)"
        }
    },
    "Thursday": {
        "name": "Hacking",
        "primary_color": "00FF00",  # Matrix Green
        "bg_color": "000000",
        "border_color": "00FF00",
        "title_color": "00FF00",
        "icon_color": "00FF00",
        "text_color": "008000",
        "gradient": "000000,005f00,000000",
        "banner_type": "cylinder",
        "font": "Share Tech Mono",
        "emojis": ["🕵️", "🔒", "🌐", "💻", "⚡", "🔌"],
        "typing_lines": [
            "🕵️ Establishing connection...",
            "🔓 Bypassing firewalls...",
            "💻 System decrypted successfully!"
        ],
        "profile_typing_lines": [
            "🕵️ Root Terminal Established @VarshuAi",
            "🌐 Decrypting Core Network Components...",
            "🔒 Bypass Successful | DevSecOps Expert"
        ],
        "headers": {
            "ABOUT": "🕵️ DECRYPTION PROTOCOL (About)",
            "FEATURES": "⚡ EXPLOIT CAPABILITIES (Features)",
            "COMMANDS": "💻 TERMINAL EXPLOIT (Usage)",
            "TECH_STACK": "🛠️ Hacker Arsenal (Tech Stack)",
            "SETUP": "🔌 TARGET CONNECTION (Setup)",
            "STRUCTURE": "📁 ARCHIVE DECRYPTED (Structure)"
        }
    },
    "Friday": {
        "name": "Nature",
        "primary_color": "2E7D32",  # Leaf Green
        "bg_color": "000000",
        "border_color": "a8e6cf",
        "title_color": "dcedc1",
        "icon_color": "a8e6cf",
        "text_color": "ffd3b6",
        "gradient": "a8e6cf,dcedc1,ffd3b6",
        "banner_type": "soft",
        "font": "Comfortaa",
        "emojis": ["🌿", "🍃", "🌾", "🌱", "🌳", "🌻"],
        "typing_lines": [
            "🌿 Growing Green Software...",
            "🍃 Clean • Sustainable • Pure",
            "☀️ Powered by Nature"
        ],
        "profile_typing_lines": [
            "🌿 Green Developer | Building Clean Code 🌿",
            "🍃 Organic System Design & Microservices 🍃",
            "☀️ Open Source Cultivator | 650+ Seeds Planted"
        ],
        "headers": {
            "ABOUT": "🌿 THE ROOT SYSTEM (About)",
            "FEATURES": "🌸 DYNAMIC BLOSSOMS (Features)",
            "COMMANDS": "🌾 SUNLIGHT HARVEST (Usage)",
            "TECH_STACK": "🌱 NUTRITIONAL BASE (Tech Stack)",
            "SETUP": "🌳 SEED SOWING (Setup)",
            "STRUCTURE": "📁 PLANT ANATOMY (Structure)"
        }
    },
    "Saturday": {
        "name": "Forest",
        "primary_color": "1B5E20",  # Deep Forest
        "bg_color": "000000",
        "border_color": "1B5E20",
        "title_color": "a5d6a7",
        "icon_color": "81c784",
        "text_color": "e8f5e9",
        "gradient": "0b2512,1b5e20,0b2512",
        "banner_type": "rounded",
        "font": "Cinzel",
        "emojis": ["🌲", "🌳", "🪵", "🍂", "🍄", "🍁"],
        "typing_lines": [
            "🌲 Into the Deep Forest...",
            "🍂 Ancient Roots • Modern Code",
            "🦌 Guardians of the System"
        ],
        "profile_typing_lines": [
            "🌲 Architect of the Digital Forest 🌲",
            "🍂 Secure Infrastructure Roots • Deep Canopy 🍂",
            "🍄 Mycelium Network Specialist | 650+ Nodes"
        ],
        "headers": {
            "ABOUT": "🌲 THE ECOSYSTEM (About)",
            "FEATURES": "🌳 FOREST CANOPY (Features)",
            "COMMANDS": "🪵 WOODLAND HARVEST (Usage)",
            "TECH_STACK": "🍂 ANCIENT SOIL (Tech Stack)",
            "SETUP": "🍄 MYCELIUM NETWORK (Setup)",
            "STRUCTURE": "📁 FOREST UNDERGROWTH (Structure)"
        }
    },
    "Sunday": {
        "name": "Ocean",
        "primary_color": "00E5FF",  # Ocean Blue
        "bg_color": "000000",
        "border_color": "0052d4",
        "title_color": "6fb1fc",
        "icon_color": "4364f7",
        "text_color": "ffffff",
        "gradient": "0052d4,4364f7,6fb1fc",
        "banner_type": "waving",
        "font": "Architects Daughter",
        "emojis": ["🌊", "🐳", "⚓", "🐠", "🐙", "🐬"],
        "typing_lines": [
            "🌊 Riding the Dev Waves...",
            "🐳 Deep Sea Performance",
            "⚓ Anchored in Reliability"
        ],
        "profile_typing_lines": [
            "🌊 Sailing the Seas of Software 🌊",
            "🐳 Scale Infinite • Dive Deep • Docker Expert 🐳",
            "⚓ Anchor Secure | DevSecOps Ship Captain"
        ],
        "headers": {
            "ABOUT": "🌊 THE DEEP BLUE (About)",
            "FEATURES": "🐳 WAVE RIDERS (Features)",
            "COMMANDS": "⚓ STEERING THE SHIP (Usage)",
            "TECH_STACK": "🐠 SEA BED (Tech Stack)",
            "SETUP": "🐙 PORT HARBOR (Setup)",
            "STRUCTURE": "📁 SHIP CARGO (Structure)"
        }
    }
}

def make_request(url, method="GET", body=None):
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json",
        "Content-Type": "application/json",
        "User-Agent": "Rotator-Bot"
    }
    
    data = None
    if body is not None:
        data = json.dumps(body).encode("utf-8")
        
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    
    try:
        with urllib.request.urlopen(req) as resp:
            content_type = resp.headers.get("Content-Type", "")
            if "application/json" in content_type:
                return json.loads(resp.read().decode("utf-8")), resp.status
            else:
                return resp.read().decode("utf-8"), resp.status
    except urllib.error.HTTPError as e:
        return e.read().decode("utf-8", errors="ignore"), e.code
    except Exception as e:
        return str(e), 500

def get_all_repositories():
    repos = []
    page = 1
    while True:
        print(f"Fetching public repositories - Page {page}...")
        url = f"https://api.github.com/user/repos?visibility=public&per_page=100&page={page}"
        data, status = make_request(url)
        if status != 200:
            print(f"Error fetching repos: {data} (Status: {status})")
            break
        if not data:
            break
        repos.extend(data)
        if len(data) < 100:
            break
        page += 1
    return repos

def get_readme(repo_name):
    url = f"https://api.github.com/repos/{GITHUB_USERNAME}/{repo_name}/contents/README.md"
    data, status = make_request(url)
    if status == 200:
        content_b64 = data.get("content", "")
        content_clean = content_b64.replace("\n", "").replace("\r", "")
        content = base64.b64decode(content_clean).decode("utf-8", errors="ignore")
        return content, data.get("sha")
    elif status == 404:
        return None, None
    else:
        print(f"Failed to fetch README for {repo_name}: status {status}")
        return None, None

def update_readme(repo_name, new_content, sha=None, theme_name=""):
    url = f"https://api.github.com/repos/{GITHUB_USERNAME}/{repo_name}/contents/README.md"
    body = {
        "message": f"docs: rotate to daily themed README ({theme_name}) 🎭",
        "content": base64.b64encode(new_content.encode("utf-8")).decode("utf-8"),
    }
    if sha:
        body["sha"] = sha
        
    data, status = make_request(url, method="PUT", body=body)
    if status in [200, 201]:
        print(f"[SUCCESS] Updated README for '{repo_name}'")
        return True
    else:
        print(f"[FAILED] Could not update README for '{repo_name}': {data} (Status: {status})")
        return False

def parse_existing_readme(content):
    if not content:
        return {}
        
    sections = {}
    lines = content.split('\n')
    current_section = None
    section_lines = []
    
    # Check for legacy and custom markdown header formats
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('## ') or (stripped.startswith('<h2>') and 'samp' in stripped):
            if current_section:
                sections[current_section] = '\n'.join(section_lines).strip()
            
            # Extract header name
            if stripped.startswith('## '):
                sec_header = stripped[3:].strip().upper()
            else:
                # Extract text inside <samp>
                try:
                    start_samp = stripped.find('&nbsp;')
                    if start_samp == -1:
                        start_samp = stripped.find('>')
                    end_samp = stripped.find('</samp>')
                    sec_header = stripped[start_samp+6:end_samp].strip().upper() if start_samp != -1 and end_samp != -1 else stripped
                except:
                    sec_header = stripped
                    
            sec_header_clean = ''.join(c for c in sec_header if c.isalnum() or c.isspace()).strip()
            current_section = sec_header_clean
            section_lines = []
        elif stripped.startswith('# ') and not current_section:
            # Main title line, ignore it
            pass
        else:
            if current_section:
                section_lines.append(line)
                
    if current_section:
        sections[current_section] = '\n'.join(section_lines).strip()
        
    # Map sections
    mapped = {}
    for sec_name, sec_text in sections.items():
        sec_name_upper = sec_name.upper()
        if any(k in sec_name_upper for k in ["ABOUT", "DESC", "OVERVIEW", "SYSTEM LOG", "PROTOCOL"]):
            mapped["ABOUT"] = sec_text
        elif any(k in sec_name_upper for k in ["FEAT", "OPT", "CAPAB", "MODULE", "SKILL"]):
            mapped["FEATURES"] = sec_text
        elif any(k in sec_name_upper for k in ["COMMAND", "USAGE", "RUN", "API", "CONTROL"]):
            mapped["COMMANDS"] = sec_text
        elif any(k in sec_name_upper for k in ["TECH", "BUILT", "DEPEND", "ARSENAL", "INVENTORY"]):
            mapped["TECH_STACK"] = sec_text
        elif any(k in sec_name_upper for k in ["SETUP", "INSTALL", "START", "BOOT", "SELECT", "HARBOR"]):
            mapped["SETUP"] = sec_text
        elif any(k in sec_name_upper for k in ["STRUCT", "TREE", "MAP"]):
            mapped["STRUCTURE"] = sec_text
            
    return mapped

def generate_themed_repo_readme(repo_name, repo_desc, lang, index, parsed_sections, day_name):
    cfg = THEME_CONFIGS[day_name]
    
    # SVG Elements
    banner_type = cfg["banner_type"]
    banner_color = cfg["gradient"]
    font_face = cfg["font"]
    
    # Setup Typing SVG Lines
    lines = []
    for raw_line in cfg["typing_lines"]:
        if "{}" in raw_line:
            lines.append(raw_line.format(repo_name))
        else:
            lines.append(raw_line)
            
    lines_escaped = ";".join(urllib.parse.quote(line) for line in lines)
    
    # Header components
    header_banner = f'<img src="https://capsule-render.vercel.app/api?type={banner_type}&color={banner_color}&height=180&section=header&text={repo_name}&fontSize=48&fontColor=ffffff&fontAlignY=38&animation=fadeIn" width="100%"/>'
    typing_svg = f'<a href="https://github.com/VarshuAi/{repo_name}"><img src="https://readme-typing-svg.demolab.com?font={urllib.parse.quote(font_face)}&weight=500&size=22&duration=3500&pause=800&color={cfg["primary_color"]}&center=true&vCenter=true&multiline=true&repeat=true&random=false&width=700&height=80&lines={lines_escaped}" alt="Typing SVG"/></a>'
    
    shields = f"""<img src="https://img.shields.io/badge/Version-1.0-{cfg['primary_color']}?style=for-the-badge&logo=github&logoColor=black" alt="Version"/>
<img src="https://img.shields.io/badge/{urllib.parse.quote(lang or 'Code')}-Tech-{cfg['primary_color']}?style=for-the-badge&logo={urllib.parse.quote((lang or 'github').lower())}&logoColor=black" alt="Language"/>
<img src="https://img.shields.io/badge/Status-Active-14354C?style=for-the-badge&logo=git&logoColor=white" alt="Status"/>"""

    small_divider = f'<img src="https://capsule-render.vercel.app/api?type=waving&color={banner_color}&height=60&section=header&text=&fontSize=0" width="100%"/>'

    # Build sections
    # 1. ABOUT
    about_desc = parsed_sections.get("ABOUT", "").strip()
    if not about_desc:
        about_desc = repo_desc or "No description available for this project."
    else:
        # Strip blockquotes or formatting if we want a clean YAML, but let's make it robust
        if about_desc.startswith("```yaml"):
            about_desc = about_desc.replace("```yaml", "").replace("```", "").strip()
            
    # Clean up about text for yaml embedding
    about_yaml_desc = about_desc.replace("\n", " ").strip()
    if about_yaml_desc.startswith(">"):
        about_yaml_desc = about_yaml_desc[1:].strip()
        
    about_yaml = f"""name: {repo_name}
version: 1.0
type: Repository
author: VarshuAi
description: >
  {about_yaml_desc}
primary_tech: {lang or 'Code'}"""

    # 2. FEATURES
    features_text = parsed_sections.get("FEATURES", "").strip()
    if not features_text:
        features_text = f"""- {cfg['emojis'][2]} **Optimized Performance** — Engineered for reliability and high throughput.
- {cfg['emojis'][0]} **Dynamic Design Theme** — Custom day-rotated style implemented.
- {cfg['emojis'][4]} **Zero-Dependency Core** — Ready to boot without complex prerequisites."""

    # 3. COMMANDS
    commands_text = parsed_sections.get("COMMANDS", "").strip()
    if not commands_text:
        lang_lower = (lang or "").lower()
        if "py" in lang_lower:
            commands_text = f"""```bash
# Setup virtual environment & run
python -m venv venv
source venv/bin/activate  # On Windows use: venv\\Scripts\\activate
pip install -r requirements.txt
python main.py
```"""
        elif "js" in lang_lower or "node" in lang_lower:
            commands_text = f"""```bash
# Install package dependencies
npm install

# Boot project module
node index.js
```"""
        else:
            commands_text = f"""```bash
# Clone the repository structure
git clone https://github.com/VarshuAi/{repo_name}.git
cd {repo_name}
```"""

    # 4. TECH STACK
    tech_stack_text = parsed_sections.get("TECH_STACK", "").strip()
    if not tech_stack_text:
        tech_stack_text = f"""<div align="center">

#### `>> SYSTEM INVENTORY`
![{lang or 'Code'}](https://img.shields.io/badge/{urllib.parse.quote(lang or 'Code')}-Primary_Language-{cfg['primary_color']}?style=for-the-badge&logoColor=black)
![Git](https://img.shields.io/badge/Git-VCS-14354C?style=for-the-badge&logo=git&logoColor=white)

</div>"""

    # 5. SETUP
    setup_text = parsed_sections.get("SETUP", "").strip()
    if not setup_text:
        setup_text = f"""```bash
# 1. Clone repository remote
git clone https://github.com/VarshuAi/{repo_name}.git
cd {repo_name}

# 2. Check technical prerequsites
# Ensure runtime matches requirements ({lang or 'Code'})
```"""

    # 6. STRUCTURE
    structure_text = parsed_sections.get("STRUCTURE", "").strip()
    if not structure_text:
        structure_text = f"""```
{repo_name}/
├── src/             # Source code entrypoints
├── docs/            # Project documentation files
├── README.md        # Interactive readme sheet
└── LICENSE          # Permission details
```"""

    # Footer elements
    footer_banner = f'<img src="https://capsule-render.vercel.app/api?type={banner_type}&color={banner_color}&height=80&section=footer&text=&fontSize=0" width="100%"/>'
    footer_typing = f'<a href="https://github.com/VarshuAi"><img src="https://readme-typing-svg.demolab.com?font={urllib.parse.quote(font_face)}&size=14&duration=4000&pause=1000&color={cfg["primary_color"]}&center=true&vCenter=true&width=500&lines=Made+with+%E2%9D%A4%EF%B8%8F+by+VarshuAi;Build+Fast.+Ship+Secure.+Scale+Infinite." alt="Typing SVG"/></a>'

    # Build standard themed readme
    themed_readme = f"""<!-- ========================================================================= -->
<!--                        {repo_name.upper()} — README                            -->
<!--       Theme: {cfg['name']} | Day Rotated | Animated SVGs | Live Badges       -->
<!-- ========================================================================= -->

<div align="center">

<!-- ============================== BANNER ============================== -->

{header_banner}

<!-- ============================== TYPING SVG ============================== -->

<br/>

{typing_svg}

<br/>

{shields}

{small_divider}

</div>

<!-- ============================== ABOUT ============================== -->

<h2>
<img src="https://media.giphy.com/media/WUlplcMpOCEmTGBtBW/giphy.gif" width="30">
<samp>&nbsp;{cfg['headers']['ABOUT']}</samp>
</h2>

```yaml
{about_yaml}
```

<!-- ============================== FEATURES ============================== -->

<h2>
<img src="https://media2.giphy.com/media/QssGEmpkyEOhBCb7e1/giphy.gif" width="28">
<samp>&nbsp;{cfg['headers']['FEATURES']}</samp>
</h2>

{features_text}

<!-- ============================== COMMANDS ============================== -->

<h2>
<img src="https://media.giphy.com/media/iY8CRBdQXODJSCERIr/giphy.gif" width="28">
<samp>&nbsp;{cfg['headers']['COMMANDS']}</samp>
</h2>

{commands_text}

<!-- ============================== TECH STACK ============================== -->

<h2>
<img src="https://media2.giphy.com/media/QssGEmpkyEOhBCb7e1/giphy.gif" width="28">
<samp>&nbsp;{cfg['headers']['TECH_STACK']}</samp>
</h2>

{tech_stack_text}

<!-- ============================== SETUP ============================== -->

<h2>
<img src="https://media.giphy.com/media/LnQjpWaON8nhr21vNW/giphy.gif" width="28">
<samp>&nbsp;{cfg['headers']['SETUP']}</samp>
</h2>

{setup_text}

<!-- ============================== STRUCTURE ============================== -->

<h2>
<samp>&nbsp;{cfg['headers']['STRUCTURE']}</samp>
</h2>

{structure_text}

<!-- ============================== FOOTER ============================== -->

<div align="center">

<br/>

{footer_banner}

<br/>

{footer_typing}

<br/>

<a href="https://github.com/VarshuAi"><img src="https://img.shields.io/badge/VarshuAi-Profile-{cfg['primary_color']}?style=for-the-badge&logo=github&logoColor=black" alt="GitHub Profile"/></a>
<a href="https://github.com/VarshuAi/{repo_name}"><img src="https://img.shields.io/badge/{repo_name}-Repo-{cfg['primary_color']}?style=for-the-badge&logo=github&logoColor=black" alt="Repository"/></a>

<br/>

</div>
"""
    return themed_readme

def parse_profile_readme(content):
    if not content:
        return {}
        
    markers = {
        "ABOUT_ME": "<!-- ============================== ABOUT ME ============================== -->",
        "SNAKE_ANIMATION": "<!-- ============================== SNAKE ANIMATION ============================== -->",
        "TECH_ARSENAL": "<!-- ============================== TECH ARSENAL ============================== -->",
        "GITHUB_STATS": "<!-- ============================== GITHUB STATS ============================== -->",
        "ACHIEVEMENTS": "<!-- ============================== ACHIEVEMENTS ============================== -->",
        "SKILL_PROFICIENCY": "<!-- ============================== SKILL PROFICIENCY ============================== -->",
        "FEATURED_PROJECTS": "<!-- ============================== FEATURED PROJECTS ============================== -->",
        "METRICS": "<!-- ============================== METRICS ============================== -->",
        "CERTIFICATIONS": "<!-- ============================== CERTIFICATIONS ============================== -->",
        "CONNECT": "<!-- ============================== CONNECT ============================== -->",
        "FOOTER_WAVE": "<!-- ============================== FOOTER WAVE ============================== -->"
    }
    
    sections = {}
    keys = list(markers.keys())
    for i in range(len(keys) - 1):
        start_key = keys[i]
        end_key = keys[i + 1]
        
        start_marker = markers[start_key]
        end_marker = markers[end_key]
        
        start_idx = content.find(start_marker)
        end_idx = content.find(end_marker)
        
        if start_idx != -1 and end_idx != -1:
            sections[start_key] = content[start_idx + len(start_marker):end_idx].strip()
            
    # Parse final footer wave section
    footer_marker = markers["FOOTER_WAVE"]
    footer_idx = content.find(footer_marker)
    if footer_idx != -1:
        sections["FOOTER_WAVE"] = content[footer_idx + len(footer_marker):].strip()
        
    return sections

def generate_themed_profile_readme(day_name, profile_sections):
    cfg = THEME_CONFIGS[day_name]
    
    banner_type = cfg["banner_type"]
    banner_color = cfg["gradient"]
    font_face = cfg["font"]
    
    lines_escaped = ";".join(urllib.parse.quote(line) for line in cfg["profile_typing_lines"])
    
    # 1. BANNER & TYPING SVG (Animated Header)
    header_banner = f'<img src="https://capsule-render.vercel.app/api?type={banner_type}&color={banner_color}&height=180&section=header&text=VarshuAi&fontSize=50&fontColor=ffffff&fontAlignY=38&animation=fadeIn" width="100%"/>'
    typing_svg = f'<a href="https://github.com/VarshuAi"><img src="https://readme-typing-svg.demolab.com?font={urllib.parse.quote(font_face)}&weight=500&size=22&duration=3500&pause=800&color={cfg["primary_color"]}&center=true&vCenter=true&multiline=true&repeat=true&random=false&width=700&height=80&lines={lines_escaped}" alt="Typing SVG"/></a>'
    small_divider = f'<img src="https://capsule-render.vercel.app/api?type=waving&color={banner_color}&height=80&section=header&text=&fontSize=0" width="100%"/>'

    # Re-extract and format about me
    about_me_raw = profile_sections.get("ABOUT_ME", "")
    # Extract YAML block if present
    yaml_start = about_me_raw.find("```yaml")
    yaml_end = about_me_raw.find("```", yaml_start + 7) if yaml_start != -1 else -1
    if yaml_start != -1 and yaml_end != -1:
        yaml_content = about_me_raw[yaml_start + 7:yaml_end].strip()
    else:
        # Fallback values
        yaml_content = """name: VarshuAi
title: System Architect & Security Researcher
location: Planet Earth
status: Always Shipping Code
specializations:
  - Full-Stack Development (React, Next.js, Node, Python, Go)
  - Security Research & Ethical Hacking
  - Cloud Architecture (AWS, GCP, Azure)
  - DevSecOps & Infrastructure Automation
  - AI/ML Engineering
motto: "Build Fast. Ship Secure. Scale Infinite." """

    # Formatting customized dividers for section breaks
    section_divider = f'<img src="https://capsule-render.vercel.app/api?type=rect&color=0:{cfg["bg_color"]},50:{cfg["primary_color"]},100:{cfg["bg_color"]}&height=2&section=header" width="100%"/>'

    # Customized statistics cards
    stats_card = f'https://github-readme-stats-sigma-five.vercel.app/api?username=VarshuAi&show_icons=true&bg_color={cfg["bg_color"]}&border_color={cfg["primary_color"]}&title_color={cfg["title_color"]}&icon_color={cfg["icon_color"]}&text_color={cfg["text_color"]}&count_private=true&include_all_commits=true'
    langs_card = f'https://github-readme-stats-sigma-five.vercel.app/api/top-langs/?username=VarshuAi&layout=compact&bg_color={cfg["bg_color"]}&border_color={cfg["primary_color"]}&title_color={cfg["title_color"]}&text_color={cfg["text_color"]}&langs_count=10&card_width=400'
    streak_card = f'https://streak-stats.demolab.com?user=VarshuAi&background={cfg["bg_color"]}&border={cfg["primary_color"]}&ring={cfg["title_color"]}&fire={cfg["primary_color"]}&currStreakLabel={cfg["text_color"]}&sideLabels={cfg["text_color"]}&currStreakNum={cfg["title_color"]}&sideNums={cfg["title_color"]}&dates={cfg["icon_color"]}'
    activity_card = f'https://github-readme-activity-graph.vercel.app/graph?username=VarshuAi&bg_color={cfg["bg_color"]}&color={cfg["primary_color"]}&line={cfg["primary_color"]}&point={cfg["title_color"]}&area_color={cfg["icon_color"]}&area=true&hide_border=true&custom_title=%3E_%20VarshuAi%20//%20Contribution%20Log'

    # Helper to clean section text by stripping heading elements and redundant animated header GIFs
    def clean_section_text(text):
        clean_lines = []
        for line in text.split('\n'):
            s_line = line.strip()
            # Skip HTML heading tags, legacy headers, break lines, and section header Giphy gifs
            if (s_line.startswith('<h2>') or 
                s_line.startswith('## ') or 
                s_line.startswith('</h') or 
                s_line.startswith('<samp>') or 
                s_line.startswith('<br') or
                (s_line.startswith('<img') and 'giphy.com' in s_line and ('width="28"' in s_line or 'width="30"' in s_line))):
                continue
            clean_lines.append(line)
        return '\n'.join(clean_lines).strip()

    # Re-extract and clean other sections
    tech_arsenal_text = clean_section_text(profile_sections.get("TECH_ARSENAL", ""))
    achievements_text = clean_section_text(profile_sections.get("ACHIEVEMENTS", ""))
    skills_text = clean_section_text(profile_sections.get("SKILL_PROFICIENCY", ""))
    projects_text = clean_section_text(profile_sections.get("FEATURED_PROJECTS", ""))

    # Update project stats card color queries in projects HTML table
    # We can replace URLs of readme stats pin cards dynamically
    import re
    pin_pattern = r'https://github-readme-stats-sigma-five\.vercel\.app/api/pin/\?username=VarshuAi&repo=[a-zA-Z0-9_-]+(&[a-zA-Z0-9_=&%-]+)*'
    def replace_pin(match):
        orig_url = match.group(0)
        # Extract repo name
        repo_match = re.search(r'repo=([a-zA-Z0-9_-]+)', orig_url)
        if repo_match:
            repo = repo_match.group(1)
            return f'https://github-readme-stats-sigma-five.vercel.app/api/pin/?username=VarshuAi&repo={repo}&bg_color={cfg["bg_color"]}&border_color={cfg["primary_color"]}&title_color={cfg["title_color"]}&icon_color={cfg["icon_color"]}&text_color={cfg["text_color"]}'
        return orig_url
    projects_text = re.sub(pin_pattern, replace_pin, projects_text)

    metrics_text = clean_section_text(profile_sections.get("METRICS", ""))
    certifications_text = clean_section_text(profile_sections.get("CERTIFICATIONS", ""))
    connect_text = clean_section_text(profile_sections.get("CONNECT", ""))

    # Rebuild profile README
    themed_profile = f"""<!-- ========================================================================= -->
<!--                          VARSHUAI — PROFILE README                        -->
<!--       Theme: {cfg['name']} | Day Rotated | Animated SVGs | Live Badges       -->
<!-- ========================================================================= -->

<div align="center">

<!-- ============================== BANNER ============================== -->

{header_banner}

<!-- ============================== TYPING SVG ============================== -->

<br/>

{typing_svg}

<!-- ============================== WAVE DIVIDER ============================== -->

{small_divider}

</div>

<!-- ============================== ABOUT ME ============================== -->

<h2>
<img src="https://media.giphy.com/media/WUlplcMpOCEmTGBtBW/giphy.gif" width="30"> 
<samp>&nbsp;{cfg['emojis'][0]} ABOUT ME</samp>
</h2>

```yaml
{yaml_content}
```

<!-- ============================== SNAKE ANIMATION ============================== -->

<div align="center">
<br>
<img src="https://raw.githubusercontent.com/platane/snk/output/github-contribution-grid-snake-dark.svg" alt="Snake animation" width="100%"/>
<br>
</div>

<!-- ============================== TECH ARSENAL ============================== -->

<h2>
<img src="https://media2.giphy.com/media/QssGEmpkyEOhBCb7e1/giphy.gif" width="28">
<samp>&nbsp;{cfg['emojis'][1]} TECH ARSENAL</samp>
</h2>

{tech_arsenal_text}

<!-- ============================== ANIMATED DIVIDER ============================== -->

{section_divider}

<!-- ============================== GITHUB STATS ============================== -->

<h2>
<img src="https://media.giphy.com/media/iY8CRBdQXODJSCERIr/giphy.gif" width="30">
<samp>&nbsp;{cfg['emojis'][2]} PERFORMANCE METRICS</samp>
</h2>

<div align="center">

<table align="center" border="0" cellpadding="0" cellspacing="0">
  <tr>
    <td align="center" valign="middle">
      <a href="https://github.com/VarshuAi">
        <img src="{stats_card}" alt="GitHub Stats" height="195px" />
      </a>
    </td>
    <td align="center" valign="middle">
      <a href="https://github.com/VarshuAi">
        <img src="{langs_card}" alt="Top Languages" height="195px" />
      </a>
    </td>
  </tr>
  <tr>
    <td align="center" valign="middle" colspan="2">
      <br/>
      <img src="{streak_card}" alt="GitHub Streak" height="195px" />
    </td>
  </tr>
</table>

<br/><br/>

<!-- Activity Graph -->
<img src="{activity_card}" alt="Activity Graph" width="98%"/>

</div>

<!-- ============================== ANIMATED DIVIDER ============================== -->

{section_divider}

<!-- ============================== ACHIEVEMENTS ============================== -->

<h2>
<img src="https://media.giphy.com/media/IdyAQJVN2kVPNUrojM/giphy.gif" width="28">
<samp>&nbsp;{cfg['emojis'][3]} ACHIEVEMENTS</samp>
</h2>

{achievements_text}

<!-- ============================== ANIMATED DIVIDER ============================== -->

{section_divider}

<!-- ============================== SKILL PROFICIENCY ============================== -->

<h2>
<img src="https://media.giphy.com/media/uhQuegHFqkVYuFMXMQ/giphy.gif" width="28">
<samp>&nbsp;{cfg['emojis'][4]} SKILL PROFICIENCY</samp>
</h2>

{skills_text}

<!-- ============================== ANIMATED DIVIDER ============================== -->

{section_divider}

<!-- ============================== FEATURED PROJECTS ============================== -->

<h2>
<img src="https://media.giphy.com/media/du3J3cXyzhj75IOgvA/giphy.gif" width="28">
<samp>&nbsp;{cfg['emojis'][0]} FEATURED PROJECTS</samp>
</h2>

{projects_text}

<!-- ============================== ANIMATED DIVIDER ============================== -->

{section_divider}

<!-- ============================== METRICS ============================== -->

<h2>
<img src="https://media.giphy.com/media/W5eoZHPpUx9sapR0eu/giphy.gif" width="28">
<samp>&nbsp;{cfg['emojis'][5]} SYSTEM DIAGNOSTICS</samp>
</h2>

{metrics_text}

<!-- ============================== ANIMATED DIVIDER ============================== -->

{section_divider}

<!-- ============================== CERTIFICATIONS ============================== -->

<h2>
<img src="https://media.giphy.com/media/3oKIPEqDGUULpEU0aQ/giphy.gif" width="28">
<samp>&nbsp;{cfg['emojis'][1]} DOMAINS OF EXPERTISE</samp>
</h2>

{certifications_text}

<!-- ============================== ANIMATED DIVIDER ============================== -->

{section_divider}

<!-- ============================== CONNECT ============================== -->

<br/>

<h2>
<img src="https://media.giphy.com/media/LnQjpWaON8nhr21vNW/giphy.gif" width="28">
<samp>&nbsp;{cfg['emojis'][2]} CONNECT</samp>
</h2>

{connect_text}

<!-- ============================== FOOTER WAVE ============================== -->

<br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color={banner_color}&height=100&section=footer&text=&fontSize=0" width="100%"/>

<div align="center">

<img src="https://img.shields.io/badge/BUILT_WITH-OBSESSION-{cfg['primary_color']}?style=flat-square&labelColor=000000"/>
<img src="https://img.shields.io/badge/POWERED_BY-CAFFEINE-{cfg['primary_color']}?style=flat-square&labelColor=000000"/>
<img src="https://img.shields.io/badge/SECURED_BY-PARANOIA-{cfg['primary_color']}?style=flat-square&labelColor=000000"/>

<br/><br/>

<samp>
<sub>// Every line of code is a step toward the future.</sub>
</samp>

</div>
"""
    return themed_profile

def main():
    # Verify GITHUB_TOKEN is set
    if not GITHUB_TOKEN:
        print("Error: GITHUB_TOKEN environment variable not set.")
        print("Please set it in your environment before running, e.g.:")
        print("  PowerShell: $env:GITHUB_TOKEN=\"your_token\"")
        print("  Bash: export GITHUB_TOKEN=\"your_token\"")
        sys.exit(1)

    # Parsing commands
    target_day = None
    target_repo = None
    dry_run = False
    
    if len(sys.argv) > 1:
        args = sys.argv[1:]
        for idx, arg in enumerate(args):
            if arg == "--dry-run":
                dry_run = True
            elif arg == "--day" and idx + 1 < len(args):
                target_day = args[idx + 1]
            elif arg == "--repo" and idx + 1 < len(args):
                target_repo = args[idx + 1]
                
    # Calculate day of week
    if target_day:
        # Match day name
        matched_day = None
        for k, v in DAYS_MAP.items():
            if v.lower() == target_day.lower():
                matched_day = v
                break
        if not matched_day:
            print(f"Error: Invalid day '{target_day}'. Must be one of Monday-Sunday.")
            sys.exit(1)
        day_name = matched_day
    else:
        # Get current day of week (0=Monday, ..., 6=Sunday)
        day_num = datetime.now().weekday()
        day_name = DAYS_MAP[day_num]
        
    theme_name = THEME_CONFIGS[day_name]["name"]
    print(f"🎭 Current Rotator Target Day: {day_name} | Theme: {theme_name} 🎭")
    if dry_run:
        print("⚠️ Running in DRY-RUN mode. No changes will be pushed to GitHub. ⚠️")

    # 1. Fetch repositories
    repos = get_all_repositories()
    total_repos = len(repos)
    print(f"Found {total_repos} public repositories in account '{GITHUB_USERNAME}'")
    
    success_count = 0
    skip_count = 0
    failed_count = 0
    
    if target_repo:
        repos = [r for r in repos if r.get("name", "").lower() == target_repo.lower()]
        total_repos = len(repos)
        print(f"Filtering run to repository: '{target_repo}' (Count: {total_repos})")

    for idx, repo in enumerate(repos):
        repo_name = repo.get("name", "")
        repo_desc = repo.get("description", "") or ""
        lang = repo.get("language", "") or "Code"
        
        print(f"\n[{idx + 1}/{total_repos}] Processing: {repo_name} ({lang})")
        
        # Check if this is the special profile README repository
        is_profile_repo = (repo_name.lower() == GITHUB_USERNAME.lower())
        
        # Fetch current README
        readme_content, sha = get_readme(repo_name)
        if not readme_content:
            print(f"No README found or error fetching README for '{repo_name}'")
            if not is_profile_repo:
                # We will create a fresh themed one
                readme_content = ""
            else:
                failed_count += 1
                continue
                
        if is_profile_repo:
            print(f"Generating SPECIAL PROFILE README for '{repo_name}' under theme '{theme_name}'...")
            # Parse sections of profile
            profile_sections = parse_profile_readme(readme_content)
            new_readme = generate_themed_profile_readme(day_name, profile_sections)
        else:
            # Standard repo
            parsed_sections = parse_existing_readme(readme_content)
            new_readme = generate_themed_repo_readme(repo_name, repo_desc, lang, idx, parsed_sections, day_name)
            
        if dry_run:
            print(f"--- DRY RUN: Generated README for '{repo_name}' ---")
            print(new_readme[:800] + "\n... [TRUNCATED] ...")
            print("--------------------------------------------------")
            success_count += 1
            continue
            
        # Push to GitHub
        success = update_readme(repo_name, new_readme, sha, theme_name=theme_name)
        if success:
            success_count += 1
        else:
            failed_count += 1
            
        # Throttle to avoid rate limits (0.5s)
        time.sleep(0.5)

    print("\n" + "="*50)
    print("ROTATOR RUN COMPLETE")
    print(f"Total Repositories Processed: {total_repos}")
    print(f"Successfully Themed/Rotated: {success_count}")
    print(f"Skipped: {skip_count}")
    print(f"Failed Updates: {failed_count}")
    print("="*50)

if __name__ == "__main__":
    main()
