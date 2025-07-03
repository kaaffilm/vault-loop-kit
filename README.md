# Vault Loop Kit

1. Copy `.env.example` → `.env`, fill values
2. `pip install pygithub requests openai`
3. Test: `python watcher.py` → prints working endpoints
4. `python validator.py` → returns GPT score
5. Deploy to Railway with cron naming steps same as files
6. Connect Airtable, Pipedream, Stripe & Softr per previous instructions
