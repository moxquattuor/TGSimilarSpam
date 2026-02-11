# Features

## Core Features

### Recursive Channel Discovery
- Starts from seed channels (L0)
- Finds similar channels using Telegram API (L1)
- Goes deeper recursively (L2)
- Exponentially expands search space
- Finds 50-200+ channels from 5 seed channels

### Intelligent Language Detection
- **Two-level detection:**
  1. Analyzes channel description (about)
  2. Analyzes last 5 posts if description unclear
- **Accurate classification:**
  - RU: 30%+ Cyrillic characters
  - EN: <10% Cyrillic characters
  - Can switch mid-search if language changes
- **Fallback to English** if both levels fail

### Owner Identification
- Extracts usernames from channel description
- Returns first found owner/admin username
- Filters out bots and suspicious accounts
- Handles special characters and formatting

### Bilingual Support
- English and Russian interface
- Separate messages for RU/EN audiences
- Language filter: target RU/EN/BOTH
- Automatic message selection based on detected language

### Smart Message Sending
- Only sends if owner hasn't replied to previous message
- Detects and deletes old unsent messages before new ones
- Checks conversation history (30 messages back)
- Returns False if last message was from owner (they replied)

### Spam Protection Features

#### 1. Cooldown System
- 2 days default between messages to same person
- Persistent JSON logging (`sent_log.json`)
- Survives bot restarts
- Prevents repeated messaging

#### 2. Bot Filtering
- Automatically skips accounts ending in "bot"
- Skips: `support_bot`, `itsnoblessebot`, `can_support_bot`, etc.
- Avoids wasting messages on automated accounts

#### 3. Message Rate Limiting
- 15 seconds delay between consecutive messages
- Prevents Telegram "FloodWait" errors
- Configurable (5-300 seconds)
- Automatically backs off if rate-limited

#### 4. History Verification
- Checks conversation before sending
- Won't send if they already replied
- Deletes old unsent messages
- 0.5s pause between deletions (safe)

### Data Logging

#### Excel Report (`contacts_master.xlsx`)
```
| Channel Link | Owner Username | Language | Status | Date |
|---|---|---|---|---|
| https://t.me/channel1 | @owner1 | RU | sent | 2026-02-11 22:37 |
| https://t.me/channel2 | @owner2 | EN | cooldown | 2026-02-11 22:38 |
```

Columns:
- **Channel Link** - Direct link to channel
- **Owner Username** - @username of contact
- **Language** - Detected language (RU/EN)
- **Status** - Result (sent, cooldown, bot, error, etc.)
- **Date** - When processed

#### JSON Log (`sent_log.json`)
```json
{
  "owner1": "2026-02-11T22:37:20.936728",
  "owner2": "2026-02-11T22:38:15.123456"
}
```
- Maps username → ISO timestamp
- Used for 2-day cooldown check
- Survives between runs

#### Session File (`session_PHONE.session`)
- Telegram session (auto-created)
- Prevents re-authentication each run
- Do not delete

## Status Messages

The bot returns these statuses for each contact:

| Status | Meaning |
|---|---|
| `sent` | Message successfully sent |
| `skipped` | Owner already replied to previous message |
| `cooldown` | Too soon since last message (2 days required) |
| `bot_skipped` | Account is a bot (username ends in "bot") |
| `lang_skip_RU` | Language filter: not targeting Russian |
| `lang_skip_EN` | Language filter: not targeting English |
| `timeout` | Message send timeout (>15 seconds) |
| `error` | Generic error during send |

## Advanced Features

### Configurable Parameters
- Max messages per run (1-1000)
- Cooldown days (1-30)
- Message delay (5-300 seconds)
- Target language (RU/EN/BOTH)
- Channel recursion depth (0-2)

### Telegram API Integration
- Uses official `GetChannelRecommendationsRequest`
- Not based on parsing or scraping
- Fast and reliable
- No account risk

### Session Management
- First run creates session (requires SMS code)
- Subsequent runs reuse session
- No need to re-authorize each time
- Can use multiple Telegram accounts

### Error Handling
- Graceful fallback for missing data
- Retry logic for temporary failures
- Timeout protection
- Continues on individual errors

## Performance

### Search Efficiency
- Processes 50-100+ channels per run
- Only fetches necessary data
- Recursive expansion (not brute-force)
- Smart deduplication

### Memory Usage
- Efficient queue-based processing
- Excel incremental saving (not in-memory)
- Handles 1000+ contacts
- Minimal resource footprint

### Speed
- 15-30 seconds per contact (including delays)
- 1 hour for ~100-150 messages
- Parallelization possible (with session management)

## Planned Features

- [ ] Scheduling (cron-based recurring runs)
- [ ] Webhook notifications (Discord/Telegram alerts)
- [ ] Advanced filtering (by subscribers, activity, posting frequency)
- [ ] A/B testing (multiple message variants)
- [ ] Response tracking (mark contacts who replied)
- [ ] Database backend (instead of Excel)
- [ ] Proxy/VPN support
- [ ] Multiple account management

## Limitations

- ⚠️ Single-threaded (one message at a time)
- ⚠️ Max 10 similar channels per API call
- ⚠️ Requires manual message composition
- ⚠️ No inbound message monitoring
- ⚠️ Excel output (not database)
- ⚠️ No scheduled/recurring runs (manual execution)

## Safety & Compliance

✅ **What it does safely:**
- Uses official Telegram API
- Respects rate limits
- No account/password storage
- No session hijacking
- Legitimate business use

⚠️ **What to be careful about:**
- Write honest messages (no spam/scam)
- Respect user privacy
- Follow Telegram ToS
- Use reasonable delays
- Don't blast thousands of people at once

