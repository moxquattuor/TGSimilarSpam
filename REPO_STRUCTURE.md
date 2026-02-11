# Repository Structure

Clean, production-ready bot for public use. No personal data.

```
telegram-bd-bot/
├── README.md                      # Main documentation
├── LICENSE                        # MIT License
├── .gitignore                     # Git ignore rules
├── requirements.txt               # Python dependencies (telethon, openpyxl)
├── setup.py                       # Interactive setup (auth, config creation)
├── main_bot.py                    # Main bot (send messages)
│
├── docs/
│   ├── SETUP_GUIDE.md            # Step-by-step installation guide
│   ├── CONFIG.md                 # All configuration parameters explained
│   └── FEATURES.md               # Bot features and capabilities
│
├── examples/
│   └── config.example.json       # Example configuration file
│
├── .env.example                  # Environment variables template
└── GITHUB_UPLOAD.md              # How to upload this to GitHub

Generated at runtime (not in repo):
├── config.json                   # Created by setup.py (YOUR SECRETS - .gitignore)
├── sent_log.json                 # Message log (YOUR DATA - .gitignore)
├── contacts_master.xlsx          # Results (YOUR DATA - .gitignore)
└── session_YOUR_PHONE.session    # Telegram session (AUTO - .gitignore)
```

## Files Explained

### Root Level

| File | Purpose | Edit? |
|---|---|---|
| `README.md` | Main user guide | Yes, customize for your project |
| `LICENSE` | MIT open source license | No |
| `.gitignore` | Don't commit secrets | No (but verify it) |
| `requirements.txt` | Python dependencies | No (unless updating versions) |
| `setup.py` | Interactive configuration | No (it's a template) |
| `main_bot.py` | The actual bot | No (it's production code) |

### docs/ Directory

**SETUP_GUIDE.md**
- Step-by-step installation
- Getting API credentials
- Setting up environment
- Troubleshooting

**CONFIG.md**
- All config.json parameters
- What each setting does
- Example configurations
- How to modify settings

**FEATURES.md**
- Bot capabilities
- Protection systems
- Status messages
- Limitations

### examples/ Directory

**config.example.json**
- Template configuration
- Shows all available settings
- Example seed channels
- Sample messages

### Root Examples

**.env.example**
- Template for environment variables
- How to set API credentials
- Copy to `.env` and fill in

**GITHUB_UPLOAD.md**
- How to push this repo to GitHub
- Git commands
- GitHub setup

## Clean vs Personal Version

### What We Removed (No Secrets!)

❌ Removed:
- Real phone numbers (`+7 991 512 5261`)
- Real API credentials
- Real seed channels
- Real contact lists
- Real messages
- Test files

✅ Replaced with:
- Placeholder instructions
- Example templates
- Generic seed channel names
- Template messages
- Production code only

## For Your GitHub Repository

1. **Fork/Clone this** structure
2. **Update README.md** with your contact info
3. **Customize docs/** if needed
4. **Keep .gitignore** as-is (protects secrets)
5. **Push to GitHub**

## Security Checklist

Before uploading to GitHub:

- ✅ No `config.json` in repo
- ✅ No `sent_log.json` in repo
- ✅ No `.env` file in repo
- ✅ No session files in repo
- ✅ No personal phone numbers
- ✅ No real API credentials
- ✅ No Excel files with real data
- ✅ `.gitignore` is correct

## File Sizes

```
README.md           ~5 KB
setup.py            ~13 KB
main_bot.py         ~15 KB
docs/*.md           ~12 KB
examples/*          ~1 KB
LICENSE             ~1 KB
.gitignore          ~1 KB
requirements.txt    ~100 bytes
```

**Total:** ~48 KB (very lightweight)

## Usage Instructions for Users

When someone clones your repo:

```bash
git clone https://github.com/YOUR_NAME/telegram-bd-bot.git
cd telegram-bd-bot
pip install -r requirements.txt
export TELEGRAM_API_ID=their_id
export TELEGRAM_API_HASH=their_hash
python setup.py        # Creates config.json with their settings
python main_bot.py     # Runs the bot
```

Everything they need is documented!

