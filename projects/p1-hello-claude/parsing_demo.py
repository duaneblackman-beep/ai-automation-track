"""
Parsing Demo — Why structured output matters in real programs.

Same ticket, three output styles.
Watch what your code can and cannot extract from each.
"""

import os
import sys
import json
from dotenv import load_dotenv
import anthropic

sys.stdout.reconfigure(encoding='utf-8')

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

TICKET = "User on the trading desk can't log into Okta. Getting MFA loop error. Been down 20 minutes."


def ask_claude(prompt, system=None):
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=300,
        system=system or "",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text


# =============================================================
# STYLE 1 — Free-form paragraph (unpredictable)
# =============================================================
print("=" * 60)
print("STYLE 1 — Free-form paragraph")
print("=" * 60)

response_1 = ask_claude(f"Analyze this IT ticket: {TICKET}")
print("Claude said:\n", response_1)

# Try to extract the severity from this...
print("\n--- What your code can extract ---")
print("Severity: ??? (no way to reliably pull this out)")
print("Category: ??? (it's buried somewhere in the paragraph)")
print("Problem: Every response will look different. Your code breaks.")


# =============================================================
# STYLE 2 — Labeled lines (predictable, easy to parse)
# =============================================================
print("\n" + "=" * 60)
print("STYLE 2 — Labeled lines")
print("=" * 60)

response_2 = ask_claude(f"""Analyze this IT ticket and respond in EXACTLY this format, nothing else:
SEVERITY: [LOW, MEDIUM, HIGH, or CRITICAL]
CATEGORY: [one word category]
SUMMARY: [one sentence]
ACTION: [one sentence first step]

Ticket: {TICKET}""")

print("Claude said:\n", response_2)

# Now parse it — split each line on the colon
print("\n--- What your code can extract ---")
parsed = {}
for line in response_2.strip().split("\n"):
    if ":" in line:
        key, value = line.split(":", 1)
        parsed[key.strip()] = value.strip()

print("Severity:", parsed.get("SEVERITY", "not found"))
print("Category:", parsed.get("CATEGORY", "not found"))
print("Summary:", parsed.get("SUMMARY", "not found"))
print("Action:", parsed.get("ACTION", "not found"))
print("✅ Every field extracted reliably. Same code works on any ticket.")


# =============================================================
# STYLE 3 — JSON (most powerful, easiest to work with in code)
# =============================================================
print("\n" + "=" * 60)
print("STYLE 3 — JSON output")
print("=" * 60)

response_3 = ask_claude(f"""Analyze this IT ticket. Respond with ONLY a JSON object, no other text.
Use exactly these keys: severity, category, summary, action, affects_trading

Ticket: {TICKET}""")

print("Claude said:\n", response_3)

# Parse it as JSON — now it's just a Python dictionary
print("\n--- What your code can extract ---")
try:
    ticket_data = json.loads(response_3)
    print("Severity:", ticket_data["severity"])
    print("Category:", ticket_data["category"])
    print("Affects trading:", ticket_data["affects_trading"])
    print("\n✅ It's a Python dictionary. Access any field instantly.")
    print("✅ You could write this to a database, send a Slack alert,")
    print("   or route it to the right team — all automatically.")
except json.JSONDecodeError:
    print("Claude didn't return clean JSON — happens occasionally.")
    print("In real code you'd add a retry or a cleanup step.")


# =============================================================
# THE POINT
# =============================================================
print("\n" + "=" * 60)
print("THE POINT")
print("=" * 60)
print("""
Style 1 (free-form): Great for reading. Useless for code.
Style 2 (labeled):   Reliable. Simple to parse. Good starting point.
Style 3 (JSON):      Best for code. Any field, any time, one line.

In Project 2 (Ticket Triage Bot), you'll use Style 3.
Claude classifies the ticket → your code reads the JSON →
your program takes action based on severity.

That's the pattern behind almost every AI-powered workflow.
""")
