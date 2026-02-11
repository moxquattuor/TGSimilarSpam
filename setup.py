#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Setup script for TGSimilarSpam
Interactive configuration & Telegram authorization
"""

import json
import os
import sys
import asyncio
from telethon import TelegramClient

# Get API credentials from environment, or use Telethon default
# Users can override with their own credentials for better rate limits
API_ID = int(os.getenv('TELEGRAM_API_ID', '20190360'))  # Telethon default
API_HASH = os.getenv('TELEGRAM_API_HASH', '67029a9453eb8a1f64fcead2fb0195b3')  # Telethon default

# Note: These are public Telethon defaults used by many bots
# For production, users should get their own credentials from https://my.telegram.org/apps

async def check_existing_session(phone):
    """Check if session exists and is authorized"""
    session_file = f'session_{phone}.session'
    if not os.path.exists(session_file):
        return None, None
    
    try:
        client = TelegramClient(session_file, API_ID, API_HASH)
        await client.connect()
        
        if await client.is_user_authorized():
            me = await client.get_me()
            await client.disconnect()
            return True, me.first_name
        else:
            await client.disconnect()
            return False, None
    except:
        return False, None

async def authorize_telegram(phone):
    """Authorize user in Telegram"""
    print()
    print("TELEGRAM AUTHORIZATION")
    print("-" * 70)
    
    try:
        client = TelegramClient(f'session_{phone}', API_ID, API_HASH)
        await client.connect()
        
        # Check if already authorized
        if await client.is_user_authorized():
            print(f"[OK] Already authorized!")
            me = await client.get_me()
            print(f"[OK] Account: {me.first_name}")
            await client.disconnect()
            return True
        
        # Send code
        print(f"[*] Sending code to {phone}...")
        await client.send_code_request(phone)
        
        # Request code
        code = input("Enter confirmation code from SMS: ").strip()
        
        # Sign in
        print("[*] Authenticating...")
        await client.sign_in(phone, code)
        
        # Check success
        if await client.is_user_authorized():
            me = await client.get_me()
            print(f"[OK] Authorization successful!")
            print(f"[OK] Name: {me.first_name}")
            print(f"[OK] Session saved: session_{phone}.session")
            await client.disconnect()
            return True
        else:
            print("[ERROR] Authorization failed")
            await client.disconnect()
            return False
    
    except Exception as e:
        print(f"[ERROR] Authorization error: {e}")
        return False

def setup():
    """Interactive setup"""
    print("=" * 70)
    print("Telegram BD Bot - Setup")
    print("=" * 70)
    print()
    
    # Choose interface language
    print("Choose interface language:")
    print("1. English")
    print("2. Russian (Русский)")
    lang_choice = input("Enter choice (1 or 2): ").strip()
    
    interface_lang = 'en' if lang_choice == '1' else 'ru'
    
    # Text dictionary
    texts = {
        'ru': {
            'title': 'TGSimilarSpam - Setup',
            'auth': 'АВТОРИЗАЦИЯ В TELEGRAM',
            'phone_prompt': 'Введи номер телефона (с +, например +1234567890): ',
            'phone_ok': 'Номер: ',
            'keywords': 'КЛЮЧЕВЫЕ СЛОВА ДЛЯ ПОИСКА',
            'keywords_example': "Пример: 'crypto trading, bitcoin, exchange'",
            'keywords_prompt': 'Введи ключевые слова (через запятую): ',
            'keywords_ok': 'Ключевые слова: ',
            'lang_filter': 'ФИЛЬТР ЯЗЫКОВ КАНАЛОВ',
            'lang_filter_question': 'Какие каналы искать?',
            'lang_ru': 'RU - Русские каналы',
            'lang_en': 'EN - Английские каналы',
            'lang_both': 'BOTH - Оба языка',
            'lang_filter_prompt': 'Выбери (RU/EN/BOTH): ',
            'lang_ok': 'Выбран язык: ',
            'seeds': 'SEED-КАНАЛЫ (5-10 штук)',
            'seeds_example': 'Пример: channel1, channel2, channel3',
            'seeds_prompt': 'Введи seed-каналы (через запятую): ',
            'seeds_ok': 'Seed-каналы: ',
            'ru_text': 'РУССКИЙ ТЕКСТ СООБЩЕНИЯ',
            'ru_text_prompt': 'Введи текст (Enter дважды для окончания):',
            'en_text': 'АНГЛИЙСКИЙ ТЕКСТ СООБЩЕНИЯ',
            'en_text_prompt': 'Введи текст (Enter дважды для окончания):',
            'params': 'ПАРАМЕТРЫ (опционально)',
            'cooldown': 'Cooldown дней (по умолчанию 2): ',
            'delay': 'Задержка между отправками сек (по умолчанию 15): ',
            'max_sent': 'Макс. отправок за запуск (по умолчанию 50): ',
            'params_ok': 'Параметры установлены',
            'complete': 'SETUP ЗАВЕРШЕН!',
            'next': 'Следующий шаг: python main_bot.py',
        },
        'en': {
            'auth': 'TELEGRAM AUTHORIZATION',
            'phone_prompt': 'Enter phone number (with +, e.g., +1234567890): ',
            'phone_ok': 'Phone: ',
            'keywords': 'SEARCH KEYWORDS',
            'keywords_example': "Example: 'crypto trading, bitcoin, exchange'",
            'keywords_prompt': 'Enter keywords (comma-separated): ',
            'keywords_ok': 'Keywords: ',
            'lang_filter': 'CHANNEL LANGUAGE FILTER',
            'lang_filter_question': 'Which channels to search?',
            'lang_ru': 'RU - Russian channels',
            'lang_en': 'EN - English channels',
            'lang_both': 'BOTH - Both languages',
            'lang_filter_prompt': 'Choose (RU/EN/BOTH): ',
            'lang_ok': 'Language selected: ',
            'seeds': 'SEED CHANNELS (5-10 channels)',
            'seeds_example': 'Example: channel1, channel2, channel3',
            'seeds_prompt': 'Enter seed channels (comma-separated): ',
            'seeds_ok': 'Seed channels: ',
            'ru_text': 'RUSSIAN MESSAGE TEXT',
            'ru_text_prompt': 'Enter text (press Enter twice to finish):',
            'en_text': 'ENGLISH MESSAGE TEXT',
            'en_text_prompt': 'Enter text (press Enter twice to finish):',
            'params': 'PARAMETERS (optional)',
            'cooldown': 'Cooldown days (default 2): ',
            'delay': 'Delay between messages sec (default 15): ',
            'max_sent': 'Max messages per run (default 50): ',
            'params_ok': 'Parameters set',
            'complete': 'SETUP COMPLETE!',
            'next': 'Next step: python main_bot.py',
        }
    }
    
    t = texts[interface_lang]
    config = {}
    config['interface_lang'] = interface_lang
    config['api_id'] = API_ID
    config['api_hash'] = API_HASH
    
    # 1. Telegram Authorization
    print(f"\n=== {t['auth']} ===")
    print("-" * 70)
    
    # Check for existing sessions
    existing_sessions = [f[8:-8] for f in os.listdir('.') if f.startswith('session_') and f.endswith('.session')]
    
    phone = None
    if existing_sessions:
        print("Found existing sessions:")
        for i, sess_phone in enumerate(existing_sessions, 1):
            print(f"  {i}. {sess_phone}")
        print(f"  0. Use new number")
        
        choice = input("Select session (0-{}): ".format(len(existing_sessions))).strip()
        
        try:
            choice_idx = int(choice)
            if 1 <= choice_idx <= len(existing_sessions):
                phone = existing_sessions[choice_idx - 1]
                print(f"[OK] Using session: {phone}")
                
                try:
                    is_auth, name = asyncio.run(check_existing_session(phone))
                    if is_auth:
                        print(f"[OK] Session is valid: {name}")
                        config['phone'] = phone
                        print()
                    else:
                        print("[ERROR] Session is invalid. Need to re-authorize.")
                        phone = None
                except Exception as e:
                    print(f"[ERROR] Error checking session: {e}")
                    phone = None
            elif choice_idx == 0:
                phone = None
        except ValueError:
            phone = None
    
    # If no session, ask for phone
    if not phone:
        phone = input(t['phone_prompt']).strip()
        config['phone'] = phone
        print(f"[OK] {t['phone_ok']}{phone}")
        
        try:
            auth_result = asyncio.run(authorize_telegram(phone))
            if not auth_result:
                print("[ERROR] Authorization failed. Aborting.")
                sys.exit(1)
        except Exception as e:
            print(f"[ERROR] Authorization error: {e}")
            sys.exit(1)
    
    # 2. Keywords
    print(f"\n=== {t['keywords']} ===")
    print("-" * 70)
    print(t['keywords_example'])
    keywords = input(t['keywords_prompt']).strip()
    config['keywords'] = [k.strip() for k in keywords.split(',')]
    print(f"[OK] {t['keywords_ok']}{config['keywords']}")
    
    # 3. Language filter
    print(f"\n=== {t['lang_filter']} ===")
    print("-" * 70)
    print(t['lang_filter_question'])
    print(f"  1. {t['lang_ru']}")
    print(f"  2. {t['lang_en']}")
    print(f"  3. {t['lang_both']}")
    lang_choice = input(t['lang_filter_prompt']).strip()
    
    lang_map = {'1': 'RU', 'RU': 'RU', 'ru': 'RU',
                '2': 'EN', 'EN': 'EN', 'en': 'EN',
                '3': 'BOTH', 'BOTH': 'BOTH', 'both': 'BOTH'}
    
    config['target_language'] = lang_map.get(lang_choice, 'BOTH')
    print(f"[OK] {t['lang_ok']}{config['target_language']}")
    
    # 4. Seed channels
    print(f"\n=== {t['seeds']} ===")
    print("-" * 70)
    print(t['seeds_example'])
    seed_channels = input(t['seeds_prompt']).strip()
    # Normalize channel names: remove t.me/ and @
    config['seed_channels'] = []
    for ch in seed_channels.split(','):
        ch = ch.strip()
        if ch.startswith('t.me/'):
            ch = ch[5:]
        if ch.startswith('@'):
            ch = ch[1:]
        if ch:
            config['seed_channels'].append(ch)
    print(f"[OK] {t['seeds_ok']}{config['seed_channels']}")
    
    # 5. Russian text
    if config['target_language'] in ['RU', 'BOTH']:
        print(f"\n=== {t['ru_text']} ===")
        print("-" * 70)
        print(t['ru_text_prompt'])
        ru_text_lines = []
        while True:
            line = input()
            if line == "":
                if ru_text_lines and ru_text_lines[-1] == "":
                    ru_text_lines.pop()
                    break
                ru_text_lines.append(line)
            else:
                ru_text_lines.append(line)
        config['msg_ru'] = "\n".join(ru_text_lines)
        print(f"[OK] Russian text ({len(config['msg_ru'])} chars)")
    else:
        config['msg_ru'] = ""
    
    # 6. English text
    if config['target_language'] in ['EN', 'BOTH']:
        print(f"\n=== {t['en_text']} ===")
        print("-" * 70)
        print(t['en_text_prompt'])
        en_text_lines = []
        while True:
            line = input()
            if line == "":
                if en_text_lines and en_text_lines[-1] == "":
                    en_text_lines.pop()
                    break
                en_text_lines.append(line)
            else:
                en_text_lines.append(line)
        config['msg_en'] = "\n".join(en_text_lines)
        print(f"[OK] English text ({len(config['msg_en'])} chars)")
    else:
        config['msg_en'] = ""
    
    # 7. Parameters
    print(f"\n=== {t['params']} ===")
    print("-" * 70)
    cooldown = input(t['cooldown']).strip() or "2"
    delay = input(t['delay']).strip() or "15"
    max_sent = input(t['max_sent']).strip() or "50"
    
    config['cooldown_days'] = int(cooldown)
    config['send_delay_seconds'] = int(delay)
    config['max_sent_per_run'] = int(max_sent)
    print(f"[OK] {t['params_ok']}")
    
    # Save config
    config_file = os.path.join(os.path.dirname(__file__), 'config.json')
    with open(config_file, 'w', encoding='utf-8') as f:
        json.dump(config, f, ensure_ascii=False, indent=2)
    
    print("\n" + "=" * 70)
    print(f"[OK] {t['complete']}")
    print("=" * 70)
    print()
    print(f"{t['next']}")
    print()

if __name__ == '__main__':
    try:
        setup()
    except KeyboardInterrupt:
        print("\n[ERROR] Setup cancelled")
        sys.exit(1)
    except Exception as e:
        print(f"\n[ERROR] {e}")
        sys.exit(1)
