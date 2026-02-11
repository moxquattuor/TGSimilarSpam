# How to Upload to GitHub

## Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. Fill in the form:
   - **Repository name:** `TGSimilarSpam`
   - **Description:** `TGSimilarSpam - Recursive Telegram channel discovery and BD messaging`
   - **Public** (if you want others to see it)
   - ✅ Add README (we already have one)
   - ✅ Add .gitignore → Python
   - ✅ Add license → MIT

3. Click "Create repository"

## Step 2: Local Git Setup

In the `github_repo` folder:

```bash
git init
git config user.name "Your Name"
git config user.email "your.email@gmail.com"
git add .
git commit -m "Initial commit: Telegram BD Bot"
```

## Step 3: Push to GitHub

```bash
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/TGSimilarSpam.git
git push -u origin main
```

(Replace `YOUR_USERNAME` with your actual GitHub username)

## If you created the repo with README first:

```bash
git pull origin main
git add .
git commit -m "Add: main bot code, setup, and documentation"
git push
```

## Step 4: Verify

Visit `https://github.com/YOUR_USERNAME/telegram-bd-bot` and confirm:
- ✅ All files are visible
- ✅ README.md shows nicely
- ✅ No `config.json` or session files (in .gitignore)
- ✅ LICENSE shows MIT

## Update Later

```bash
git add .
git commit -m "Update: fix bot filter"
git push
```

## Important: Don't Commit

Make sure these files are **NOT** pushed:
- `config.json` (has your credentials!)
- `sent_log.json` (has contact history)
- `*.xlsx` (has contact data)
- `session_*.session` (Telegram session)
- `.env` (has API credentials)

All are already in `.gitignore` ✅

## Next: Make it Public

Once uploaded, you can:
- ⭐ Add GitHub topics: `telegram`, `bot`, `crypto`, `business-development`
- 📝 Add description/badges to README
- 🔗 Add GitHub link to your portfolio
- 🎯 Share with others (it's open source!)

