# Configuration Guide

All settings are stored in `config.json` and created by `setup.py`.

## Config Structure

```json
{
  "interface_lang": "en",
  "phone": "+1234567890",
  "api_id": 123456,
  "api_hash": "your_hash_here",
  "keywords": ["crypto", "trading"],
  "target_language": "BOTH",
  "seed_channels": ["channel1", "channel2"],
  "msg_ru": "Russian message...",
  "msg_en": "English message...",
  "cooldown_days": 2,
  "send_delay_seconds": 15,
  "max_sent_per_run": 50
}
```

## Parameters

### Interface & Auth

- **interface_lang** `"en"` or `"ru"`
  - Language for setup interface
  - Does NOT affect bot's message language

- **phone** `"+1234567890"`
  - Your Telegram phone number (with country code)
  - Used for authentication

- **api_id** `20190360`
  - Your Telegram API ID (optional - defaults to Telethon public ID)
  - Get your own from https://my.telegram.org/apps for production
  - Default works fine for testing

- **api_hash** `"67029a9453eb8a1f64fcead2fb0195b3"`
  - Your Telegram API Hash (optional - defaults to Telethon public hash)
  - Get your own from https://my.telegram.org/apps for production
  - Default works fine for testing

### Search Settings

- **keywords** `["crypto", "trading"]`
  - Search keywords (for reference/filtering)
  - Currently used for logging only

- **seed_channels** `["CryptoPlanetCalls", "channel2"]`
  - Starting channels for recursive search
  - 5-10 channels recommended
  - Must be public channels with >1000 subscribers
  - Format: `channel_username` (without @ or t.me/)

- **target_language** `"RU"` | `"EN"` | `"BOTH"`
  - Which channel language to target
  - `"RU"` - Russian channels only
  - `"EN"` - English channels only
  - `"BOTH"` - Both languages

### Message Settings

- **msg_ru** `"Your Russian message..."`
  - Message text for Russian channels
  - Leave empty if not targeting Russian

- **msg_en** `"Your English message..."`
  - Message text for English channels
  - Leave empty if not targeting English

### Sending Parameters

- **cooldown_days** `2`
  - Minimum days between messages to same person
  - Prevents duplicate/spam messaging
  - Logged in `sent_log.json`
  - Range: 1-30

- **send_delay_seconds** `15`
  - Delay between sending consecutive messages
  - Prevents Telegram spam detection
  - Too low (<5s) = flood-wait errors
  - Too high (>60s) = slower operation
  - Recommended: 10-30 seconds
  - Range: 5-300

- **max_sent_per_run** `50`
  - Maximum messages to send per run
  - Bot stops after reaching this number
  - Does NOT count skipped (cooldown/bot/error)
  - Only counts actually sent messages
  - Range: 1-1000

## Example Configurations

### Conservative (Safe Testing)
```json
{
  "max_sent_per_run": 5,
  "send_delay_seconds": 20,
  "cooldown_days": 2,
  "target_language": "EN"
}
```

### Aggressive (Higher Volume)
```json
{
  "max_sent_per_run": 100,
  "send_delay_seconds": 10,
  "cooldown_days": 1,
  "target_language": "BOTH"
}
```

### Russian Only
```json
{
  "target_language": "RU",
  "msg_en": "",
  "seed_channels": ["channel1", "channel2", "channel3"]
}
```

## Modifying Config

You can edit `config.json` directly with any text editor, or delete it and run `setup.py` again.

### Common Changes

**Increase message limit:**
```json
"max_sent_per_run": 100
```

**Reduce delay for faster sending:**
```json
"send_delay_seconds": 10
```

**Only Russian channels:**
```json
"target_language": "RU"
```

**Add more seed channels:**
```json
"seed_channels": ["channel1", "channel2", "channel3", "channel4"]
```

## Important Notes

⚠️ **Credentials Security**
- Keep `api_id` and `api_hash` private
- Never commit `config.json` to version control
- It's already in `.gitignore` - don't remove it

⚠️ **Message Content**
- Write natural, non-spam messages
- Use proper language (RU/EN)
- Include clear call-to-action
- Avoid links in first contact (can trigger filters)

⚠️ **Rate Limits**
- Telegram has spam detection
- If you get "FloodWait" errors, increase `send_delay_seconds`
- 2 days cooldown prevents ban risk

## File Outputs

After running the bot:

- **contacts_master.xlsx** - All found contacts (channels, owners, language, status)
- **sent_log.json** - Sent messages (username: timestamp) for cooldown tracking
- **session_PHONE.session** - Telegram session (auto-created, do not delete)

