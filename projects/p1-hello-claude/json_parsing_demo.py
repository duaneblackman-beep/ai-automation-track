"""
JSON Parsing Demo — Why backticks break json.loads() and how to fix it.
"""

import sys
import json
import os
from dotenv import load_dotenv
import anthropic

sys.stdout.reconfigure(encoding='utf-8')
load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

TICKET = "User on the trading desk can't log into Okta. MFA loop error. Down 20 minutes."

# ---------------------------------------------------------------
# STEP 1 — See exactly what Claude returns (the raw string)
# ---------------------------------------------------------------
print("=" * 60)
print("STEP 1 — The raw string Claude returns")
print("=" * 60)

response = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=300,
    messages=[{
        "role": "user",
        "content": f"""Analyze this IT ticket. Respond with ONLY a JSON object, no other text.
Use exactly these keys: severity, category, summary, affects_trading

Ticket: {TICKET}"""
    }]
)

raw = response.content[0].text
print(repr(raw))  # repr() shows the string EXACTLY as Python sees it — escape chars and all
print()
print("Visible output:")
print(raw)


# ---------------------------------------------------------------
# STEP 2 — Try json.loads() on the raw string — watch it fail
# ---------------------------------------------------------------
print("\n" + "=" * 60)
print("STEP 2 — What happens when you run json.loads() on the raw string")
print("=" * 60)

print("Running: json.loads(raw)")
print()
try:
    data = json.loads(raw)
    print("It worked! (Claude returned clean JSON this time)")
except json.JSONDecodeError as e:
    print(f"JSONDecodeError: {e}")
    print()
    print("Why it failed:")
    print("  json.loads() expects the string to START with { or [")
    print("  If Claude wrapped it in ```json ... ``` the string starts with a backtick")
    print("  A backtick is not valid JSON — so it crashes immediately")


# ---------------------------------------------------------------
# STEP 3 — The fix: strip the markdown fences before parsing
# ---------------------------------------------------------------
print("\n" + "=" * 60)
print("STEP 3 — The fix: strip the fences")
print("=" * 60)

def extract_json(text):
    """
    Strip markdown code fences from a string and return clean JSON.

    Claude sometimes wraps JSON in:
        ```json
        { ... }
        ```
    or just:
        ```
        { ... }
        ```

    This function handles both cases.
    """
    text = text.strip()

    # If it starts with a backtick fence, remove the first and last lines
    if text.startswith("```"):
        lines = text.split("\n")
        # Remove the opening fence (```json or ```)
        lines = lines[1:]
        # Remove the closing fence (```)
        if lines[-1].strip() == "```":
            lines = lines[:-1]
        text = "\n".join(lines).strip()

    return text

cleaned = extract_json(raw)

print("Raw string (first 60 chars):", repr(raw[:60]))
print("Cleaned string (first 60 chars):", repr(cleaned[:60]))
print()

try:
    data = json.loads(cleaned)
    print("json.loads() succeeded!")
    print()
    print("Python dictionary:")
    print("  severity      :", data.get("severity"))
    print("  category      :", data.get("category"))
    print("  summary       :", data.get("summary"))
    print("  affects_trading:", data.get("affects_trading"))
except json.JSONDecodeError as e:
    print(f"Still failed: {e}")
    print("Claude may have returned something unexpected. Print raw to debug.")


# ---------------------------------------------------------------
# STEP 4 — The professional pattern: always use extract_json()
# ---------------------------------------------------------------
print("\n" + "=" * 60)
print("STEP 4 — The professional pattern going forward")
print("=" * 60)
print("""
In every project from here on, whenever you ask Claude for JSON:

    raw     = response.content[0].text     # what Claude returned
    cleaned = extract_json(raw)            # strip fences if present
    data    = json.loads(cleaned)          # now safely parse it

Three lines. Always. Whether Claude wraps it or not, extract_json()
handles it cleanly either way.

This is the fix you'll put into Project 2 (Ticket Triage Bot)
so the program never crashes on a real ticket.
""")
