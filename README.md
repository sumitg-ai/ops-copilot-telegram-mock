---

# Ops Co-Pilot — Telegram MVP (Slack + Notion Digest, Mock Mode)

This project demonstrates a Telegram MVP bot that integrates Slack + Notion and produces a daily digest.

This **mock version** runs without any Slack or Notion credentials — it uses hardcoded data to simulate API responses.
Useful for:

* **Demos / Walkthroughs**
* **IT team onboarding**
* **Testing the end-to-end flow without external dependencies**

---

## Run in Mock Mode (No Credentials Needed)

### Setup

1. Create and activate a virtual environment:

   ```bash
   python -m venv .venv && source .venv/bin/activate
   ```
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Start the server:

   ```bash
   uvicorn app.main:app --reload --port 8000
   ```
4. Verify health check:

   ```bash
   curl http://localhost:8000/healthz
   ```

---

### Bot Commands (Mock Mode)

These are the commands that mimic real functionality but return **simulated results**:

* `/slacktest` → shows 10 fake Slack messages
* `/notiontest` → shows 5 fake Notion tasks
* `/promises` → detects commitments in mock Slack messages
* `/digest today` → shows a mock digest summary

---

### Curl Test Commands (Developer Only)

These commands are for developers/IT to test the mock backend locally.

**1. `/start` — sanity check**

```bash
curl -s -X POST http://127.0.0.1:8000/telegram/webhook \
  -H "Content-Type: application/json" \
  -d '{"message":{"chat":{"id":"123"},"text":"/start"}}' \
  | jq -r '.message'
```

**2. `/slacktest` — last 10 fake Slack messages**

```bash
curl -s -X POST http://127.0.0.1:8000/telegram/webhook \
  -H "Content-Type: application/json" \
  -d '{"message":{"chat":{"id":"123"},"text":"/slacktest"}}' \
  | jq -r '.message'
```

**3. `/notiontest` — last 5 fake Notion tasks**

```bash
curl -s -X POST http://127.0.0.1:8000/telegram/webhook \
  -H "Content-Type: application/json" \
  -d '{"message":{"chat":{"id":"123"},"text":"/notiontest"}}' \
  | jq -r '.message'
```

**4. `/promises` — detect commitments in fake Slack messages**

```bash
curl -s -X POST http://127.0.0.1:8000/telegram/webhook \
  -H "Content-Type: application/json" \
  -d '{"message":{"chat":{"id":"123"},"text":"/promises"}}' \
  | jq -r '.message'
```

**5. `/digest today` — daily digest summary (mock)**

```bash
curl -s -X POST http://127.0.0.1:8000/telegram/webhook \
  -H "Content-Type: application/json" \
  -d '{"message":{"chat":{"id":"123"},"text":"/digest today"}}' \
  | jq -r '.message'
```

Example output:

```
*Digest (Today)*

- Slack Promises: 10
   • @user1: I'll ship the PR by Friday
   • @user2: I'll ship the PR by Friday
   • @user3: I'll ship the PR by Friday
   … and 7 more

- Overdue Notion Tasks: 3
   • Task 1 (due: mock-date)
   • Task 3 (due: mock-date)
   … and 1 more

- Recent #Kandy messages:
   • @user1: I'll ship the PR by Friday
   • @user2: I'll ship the PR by Friday
   • @user3: I'll ship the PR by Friday
   … and 7 more
```

---

### End-to-End Flow (Mock Mode)

The mock backend simulates what the real bot will do in production:

1. User runs a command (e.g., `/digest today`).
2. FastAPI server responds with **fake Slack messages + fake Notion tasks**.
3. The flow mirrors the real system, but no external credentials are needed.

---

### Purpose of Mock Mode

* Provides a **safe sandbox** to demo the MVP flow without depending on Slack/Notion APIs.
* Helps IT/dev teams understand the bot’s behavior before configuring real integrations.
* Useful for **walkthroughs with stakeholders** to validate UX.

---


