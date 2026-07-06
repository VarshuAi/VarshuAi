"""
VarshuOS — Daily Theme Rotator for ALL Repos
=============================================
Called by GitHub Actions every day.
Updates the themed banner at the top of every repo's README
except the protected VarshuAi profile repo.

Requires env var: GH_PAT (GitHub Personal Access Token with repo scope)
"""

import requests
import sys
import time
import base64
import os
import datetime

# ─── CONFIG ────────────────────────────────────────────────────────────────────
GITHUB_USERNAME = "VarshuAi"

# These repos are NEVER modified
PROTECTED_REPOS = {"VarshuAi"}

# Theme config — must match generate_readme.py
IST = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
today = datetime.datetime.now(IST)
DAY = today.strftime("%A")
DATE = today.strftime("%d %b %Y")

DISTROS = {
    "Monday":    {"distro": "RedStrike OS",  "accent": "#FF0000", "accent2": "#FF6B6B", "codename": "Inferno",  "motd": "New week. New exploits. No mercy."},
    "Tuesday":   {"distro": "DeepBlue OS",   "accent": "#0074D9", "accent2": "#7FDBFF", "codename": "Abyss",    "motd": "Silence the noise. Enter the flow."},
    "Wednesday": {"distro": "NeonArc OS",    "accent": "#FF00FF", "accent2": "#DA70D6", "codename": "Glitch",   "motd": "Midweek. Maximum output."},
    "Thursday":  {"distro": "ForestRoot OS", "accent": "#00FF41", "accent2": "#A8E6CF", "codename": "Banyan",   "motd": "Grow one commit at a time."},
    "Friday":    {"distro": "GoldRush OS",   "accent": "#FFD700", "accent2": "#FFE066", "codename": "Midas",    "motd": "Ship it. Its Friday. YOLO."},
    "Saturday":  {"distro": "CyberKali OS",  "accent": "#00FFFF", "accent2": "#FF1493", "codename": "Phantom",  "motd": "No rules. No deadlines. Pure chaos."},
    "Sunday":    {"distro": "ZenMint OS",    "accent": "#FF6347", "accent2": "#FF8C00", "codename": "Satori",   "motd": "Rest day. Opens laptop anyway."},
}

d = DISTROS[DAY]

# The banner block injected/updated at the top of every repo README
BANNER = f"""\
<!-- VARSHUOS-THEME-START -->
<div align="center">

<img src="https://raw.githubusercontent.com/VarshuAi/VarshuAi/main/assets/boot.svg" width="100%"/>

![Theme](https://img.shields.io/badge/{DAY}-{d['distro'].replace(' ', '_')}-{d['accent'].replace('#', '')}?style=flat-square&labelColor=0D1117)
![Distro](https://img.shields.io/badge/VarshuOS-{d['codename']}-{d['accent2'].replace('#', '')}?style=flat-square&labelColor=0D1117)

</div>

<!-- VARSHUOS-THEME-END -->
"""

THEME_START = "<!-- VARSHUOS-THEME-START -->"
THEME_END   = "<!-- VARSHUOS-THEME-END -->"
# ───────────────────────────────────────────────────────────────────────────────


def api_headers(pat):
    return {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {pat}",
        "X-GitHub-Api-Version": "2022-11-28"
    }


def get_all_repos(pat):
    repos = []
    page = 1
    while True:
        url = f"https://api.github.com/user/repos?per_page=100&page={page}&type=owner"
        r = requests.get(url, headers=api_headers(pat))
        if r.status_code != 200:
            print(f"Error fetching repos: {r.status_code}")
            sys.exit(1)
        data = r.json()
        if not data:
            break
        repos.extend(data)
        if len(data) < 100:
            break
        page += 1
    return repos


def get_readme(repo_name, pat):
    url = f"https://api.github.com/repos/{GITHUB_USERNAME}/{repo_name}/contents/README.md"
    r = requests.get(url, headers=api_headers(pat))
    if r.status_code == 200:
        data = r.json()
        content = base64.b64decode(data['content']).decode('utf-8', errors='replace')
        return content, data['sha']
    return None, None


def update_readme(repo_name, new_content, sha, pat):
    url = f"https://api.github.com/repos/{GITHUB_USERNAME}/{repo_name}/contents/README.md"
    payload = {
        "message": f"theme: {DAY} — {d['distro']} | VarshuOS auto-rotation",
        "content": base64.b64encode(new_content.encode('utf-8')).decode('utf-8'),
        "sha": sha
    }
    r = requests.put(url, headers=api_headers(pat), json=payload)
    return r.status_code in (200, 201)


def create_readme(repo_name, pat):
    url = f"https://api.github.com/repos/{GITHUB_USERNAME}/{repo_name}/contents/README.md"
    default = BANNER + f"\n# {repo_name}\n\n> Built by [{GITHUB_USERNAME}](https://github.com/{GITHUB_USERNAME})\n"
    payload = {
        "message": f"theme: VarshuOS daily banner added",
        "content": base64.b64encode(default.encode('utf-8')).decode('utf-8')
    }
    r = requests.put(url, headers=api_headers(pat), json=payload)
    return r.status_code in (200, 201)


def inject_banner(content):
    if THEME_START in content and THEME_END in content:
        start = content.index(THEME_START)
        end   = content.index(THEME_END) + len(THEME_END)
        return content[:start] + BANNER + content[end:].lstrip('\n')
    return BANNER + "\n" + content


def main():
    pat = os.environ.get("GH_PAT", "").strip()
    if not pat:
        print("Error: GH_PAT environment variable not set.")
        sys.exit(1)

    print(f"VarshuOS Theme Rotator — {DAY} | {d['distro']} | {DATE}")
    print("=" * 60)

    repos = get_all_repos(pat)
    total = len(repos)
    print(f"Found {total} repos. Starting update...\n")

    updated = skipped = failed = created = 0

    for idx, repo_data in enumerate(repos, 1):
        name       = repo_data['name']
        is_fork    = repo_data.get('fork', False)
        is_archive = repo_data.get('archived', False)

        # Skip protected, forks, archived
        if name in PROTECTED_REPOS or is_fork or is_archive:
            reason = "protected" if name in PROTECTED_REPOS else ("fork" if is_fork else "archived")
            print(f"[{idx}/{total}] SKIP  '{name}' ({reason})")
            skipped += 1
            continue

        print(f"[{idx}/{total}] '{name}'... ", end="", flush=True)

        content, sha = get_readme(name, pat)

        if content is not None:
            new_content = inject_banner(content)
            if new_content == content:
                print("already up to date.")
                skipped += 1
            else:
                ok = update_readme(name, new_content, sha, pat)
                print("updated ✓" if ok else "FAILED ✗")
                updated += ok
                failed += not ok
        else:
            ok = create_readme(name, pat)
            print("created ✓" if ok else "FAILED ✗")
            created += ok
            failed += not ok

        time.sleep(0.8)   # avoid secondary rate limits

    print(f"""
{'=' * 60}
Done! Updated: {updated} | Created: {created} | Skipped: {skipped} | Failed: {failed}
{'=' * 60}
""")


if __name__ == "__main__":
    main()
