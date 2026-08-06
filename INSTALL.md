# 🚀 Deploy Your Profile README — 5 minutes

## What's in this package
```
github-profile/
├── README.md                  ← the profile page
├── assets/
│   ├── header.png             ← custom banner (gradient Raaga style)
│   ├── raaga-card.png         ← featured project card w/ real screenshot
│   ├── divider.png            ← gradient hairline dividers
│   └── footer.png             ← footer art
└── .github/workflows/snake.yml ← auto-generates the 🐍 daily
```

## Step 1 — Create the special profile repo
1. Go to <https://github.com/new>
2. Repository name: **VarshuAi** (exactly your username — GitHub shows a ✨ hint)
3. Public ✅ · *Do NOT* click "Add a README" (we upload our own)
4. Create repository

## Step 2 — Upload the files (web UI, no git needed)
1. On the empty repo page click **"uploading an existing file"**
2. Upload `README.md`
3. Upload the entire `assets/` folder contents (GitHub keeps the folder path)
4. Upload `.github/workflows/snake.yml` — GitHub auto-creates the `.github/workflows/` path when you drag the file in with its folders preserved
5. **Commit changes**

👉 Done — visit <https://github.com/VarshuAi> and enjoy.

## Step 3 — Turn on the snake (optional, 1 minute)
1. Repo → **Actions** tab → click **"I understand my workflows, go ahead and enable them"**
2. Click **Generate Snake** (left sidebar) → **Run workflow** → Run workflow
3. Wait ~30s. The snake image appears on your profile once the `output` branch exists.
   (It then refreshes itself every midnight.)

## Customize later
- Email badge: replace `YOUR-EMAIL-HERE` in README.md Connect row
- Add skills: edit the `skillicons.dev/icons?i=` list ([full icon list](https://skillicons.dev))
- Regenerate graphics with different text: ask me anytime ✌️

## Note
Stats widgets (readme-stats, streak, trophy, activity-graph, typing-svg) load from
popular free services — they need no setup and work immediately with your username.
The custom banner/card/divider/footer images live inside your repo, so they can never break.
