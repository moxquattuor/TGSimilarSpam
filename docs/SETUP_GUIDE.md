# Setup Guide

## Prerequisites

- Python 3.8+
- Telegram account
- Telegram API credentials

## Step 1: Get Telegram API Credentials

1. Go to https://my.telegram.org/apps
2. Log in with your phone number
3. Create a new application (fill in any app name)
4. Copy `API ID` and `API Hash`

## Step 2: Clone Repository

```bash
git clone https://github.com/your-username/telegram-bd-bot.git
cd telegram-bd-bot
```

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 4: (Optional) Set Your API Credentials

The bot uses Telethon's default public credentials and works out of the box.

If you want to use your own credentials (recommended for production/scaling):

### Option A: Environment Variables (Recommended)

**Linux/Mac:**
```bash
export TELEGRAM_API_ID=your_api_id_here
export TELEGRAM_API_HASH=your_api_hash_here
python setup.py
```

**Windows (PowerShell):**
```powershell
$env:TELEGRAM_API_ID="your_api_id_here"
$env:TELEGRAM_API_HASH="your_api_hash_here"
python setup.py
```

### Option B: .env File

Create `.env` in project root:
```
TELEGRAM_API_ID=your_api_id_here
TELEGRAM_API_HASH=your_api_hash_here
```

### Getting Your Own Credentials

1. Go to https://my.telegram.org/apps
2. Log in with your phone
3. Create new app
4. Copy API ID and API Hash
5. Use Option A or B above

## Step 5: Run Interactive Setup

```bash
python setup.py
```

This will guide you through:

1. **Language Selection** - Choose interface language (English/Russian)
2. **Telegram Authorization** - Enter your phone number and SMS code
3. **Keywords** - What to search for (e.g., "crypto trading, bitcoin")
4. **Language Filter** - Target RU/EN/BOTH channels
5. **Seed Channels** - Starting channels for search (5-10 recommended)
6. **Messages** - Your outreach text for RU and EN
7. **Parameters** - Cooldown, delay, max messages

The setup creates `config.json` with your settings.

## Step 6: Run the Bot

```bash
python main_bot.py
```

## Troubleshooting

### Bot works without issues from the start
The bot uses Telethon's default public credentials, so you don't need to set up API keys unless you want your own.

### "Not authorized. Run setup.py first!"
Session file is missing or invalid. Run `setup.py` again to create a new session.

### "FloodWait" errors
Telegram rate-limited your account. The bot automatically waits. Be patient.

### "database is locked"
Kill any other Python processes running the bot, then try again:
```bash
# Linux/Mac
killall python

# Windows - just close the terminal or use Task Manager
```

### Bot doesn't find owners
Make sure seed channels are popular (1000+ subscribers) and have contacts in their description.

## Tips

- **Start small**: Set `max_sent_per_run=5` for testing
- **Popular channels**: Use well-known channels (>10k subscribers) as seeds
- **Keywords**: Use relevant, niche keywords for better results
- **Message timing**: 15 seconds delay is safe; increase if you get FloodWait
- **Cooldown**: 2 days is default; increase if targeting same people multiple times

## Next Steps

After successful run:
1. Check `contacts_master.xlsx` for results
2. Review sent messages in `sent_log.json`
3. Adjust `config.json` for next run
4. Run `python main_bot.py` again for more messages
