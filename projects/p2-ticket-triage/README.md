# Project 2 — IT Ticket Triage Bot

**Part of:** [AI Automation Track](../../README.md)
**Skills practiced:** Functions, f-strings, file I/O, error handling, sys.argv
**AI concepts:** System prompts, structured output, prompt engineering

---

## What It Does

Takes an IT support ticket (typed text or a `.txt` file) and returns a structured triage assessment using Claude AI:

```
TICKET: User can't log into Okta. Getting stuck in MFA loop. Trading desk. 10 minutes to market open.

────────────────────────────────────────────────────────────
  SEVERITY   : CRITICAL
  CATEGORY   : Identity & Access
  IMPACT     : Trading desk user fully blocked; market open in 10 minutes creates direct business risk
  FIRST RESP : Your Okta session may be stuck. Please clear your browser cache, open an incognito window, and try logging in again. Do not approve any pending push notifications.
  NEXT STEP  : Reset user's Okta session in the admin console. Check MFA policy for recent changes. Escalate to Identity team if not resolved in 5 minutes.
────────────────────────────────────────────────────────────
```

---

## How to Run

**Single ticket (text):**
```bash
python ticket_triage.py "User can't connect to VPN, working from home."
```

**Single ticket (file):**
```bash
python ticket_triage.py sample_tickets/ticket1.txt
```

**Batch mode — triage all tickets in a folder:**
```bash
python ticket_triage.py --batch sample_tickets/
```

---

## Setup

1. Make sure your `.env` file is in the project root (one level up from this folder):
   ```
   ANTHROPIC_API_KEY=sk-ant-...
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## What I Learned

- **System prompts** control Claude's behavior and output format — this is the most important prompt engineering tool
- **Structured output** — asking Claude to respond in a fixed format makes it easy to parse with Python
- **parse_response()** shows how to turn AI text output into a Python dict you can use in code
- **Batch mode** demonstrates how a real IT team could automate ticket pre-triage across a queue
- **Error handling** — wrapping file reads and API calls to fail gracefully

---

## Sample Tickets

Five realistic tickets in `sample_tickets/` covering:
- Identity & Access (Okta MFA loop)
- AV & Conference (Zoom Room before board meeting)
- Network & VPN (remote user, new hire)
- File Access / Permissions
- Printing / Shared device

---

## Key Code Concepts

```python
# Functions with type hints
def triage_ticket(ticket_text: str) -> dict:

# f-strings
{"role": "user", "content": f"Triage this IT support ticket:\n\n{ticket_text}"}

# File I/O
with open(source, "r", encoding="utf-8") as f:
    return f.read().strip()

# sys.argv for CLI arguments
if sys.argv[1] == "--batch":
```
