"""
IT Ticket Triage Bot — Project 2
AI Automation Track

Usage:
    python ticket_triage.py "User can't log into Okta, getting MFA loop."
    python ticket_triage.py sample_tickets/ticket1.txt
    python ticket_triage.py --batch sample_tickets/

What it does:
    Reads an IT support ticket (text or .txt file) and returns a structured
    triage analysis: severity, category, impact, first response, and next step.
"""

import anthropic
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Search for .env starting from this script's directory, then walk up to repo root
def _find_and_load_env():
    script_dir = Path(__file__).resolve().parent
    for directory in [script_dir] + list(script_dir.parents):
        env_file = directory / ".env"
        if env_file.exists():
            load_dotenv(env_file)
            return
    load_dotenv()  # fallback: let python-dotenv try its default behavior

_find_and_load_env()


# ── System prompt ─────────────────────────────────────────────────────────────

SYSTEM_PROMPT = """You are an expert IT support triage specialist with 15 years of experience
in enterprise environments including financial services, hedge funds, and fintech companies.

Your job is to analyze incoming IT support tickets and return a structured triage assessment.

Always respond in this EXACT format — nothing before or after, no extra text:

SEVERITY: [LOW / MEDIUM / HIGH / CRITICAL]
CATEGORY: [Identity & Access / AV & Conference / Network & VPN / Hardware / Software / Endpoint / Printing / Other]
IMPACT: [brief description of who is affected and business impact]
FIRST RESPONSE: [what to tell the user right now — be specific and actionable]
NEXT STEP: [what IT should do immediately after sending the first response]

Severity guide:
- CRITICAL: Active business disruption, executive impact, trading desk, or time-sensitive meeting in progress
- HIGH: Single user fully blocked from doing their job, or multiple users moderately affected
- MEDIUM: User partially blocked, workaround exists, or issue is not time-sensitive
- LOW: Minor inconvenience, question, or request that can be scheduled

Be concise. Each field should be 1-2 sentences max."""


# ── Core functions ─────────────────────────────────────────────────────────────

def triage_ticket(ticket_text: str) -> dict:
    """
    Sends a ticket to Claude for triage analysis.
    Returns a dict with keys: severity, category, impact, first_response, next_step.
    """
    client = anthropic.Anthropic()

    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=512,
        system=SYSTEM_PROMPT,
        messages=[
            {"role": "user", "content": f"Triage this IT support ticket:\n\n{ticket_text}"}
        ]
    )

    raw_output = message.content[0].text
    return parse_response(raw_output)


def parse_response(raw: str) -> dict:
    """
    Parses Claude's structured text response into a Python dictionary.
    """
    result = {
        "severity": "",
        "category": "",
        "impact": "",
        "first_response": "",
        "next_step": "",
        "raw": raw
    }

    field_map = {
        "SEVERITY:": "severity",
        "CATEGORY:": "category",
        "IMPACT:": "impact",
        "FIRST RESPONSE:": "first_response",
        "NEXT STEP:": "next_step"
    }

    for line in raw.strip().splitlines():
        for prefix, key in field_map.items():
            if line.startswith(prefix):
                result[key] = line[len(prefix):].strip()

    return result


def read_ticket(source: str) -> str:
    """
    Reads ticket text from a .txt file or returns the string directly.
    """
    if source.endswith(".txt") and os.path.isfile(source):
        with open(source, "r", encoding="utf-8") as f:
            return f.read().strip()
    return source.strip()


def print_triage(ticket_text: str, result: dict, label: str = ""):
    """
    Prints a formatted triage result to the terminal.
    """
    divider = "-" * 60
    if label:
        print(f"\n{'=' * 60}")
        print(f"  {label}")
        print(f"{'=' * 60}")

    print(f"\nTICKET:\n  {ticket_text[:120]}{'...' if len(ticket_text) > 120 else ''}\n")
    print(divider)
    print(f"  SEVERITY   : {result['severity']}")
    print(f"  CATEGORY   : {result['category']}")
    print(f"  IMPACT     : {result['impact']}")
    print(f"  FIRST RESP : {result['first_response']}")
    print(f"  NEXT STEP  : {result['next_step']}")
    print(divider)


def run_batch(folder: str):
    """
    Runs triage on all .txt files in a folder.
    """
    txt_files = sorted([f for f in os.listdir(folder) if f.endswith(".txt")])

    if not txt_files:
        print(f"No .txt files found in '{folder}'")
        return

    print(f"\nRunning batch triage on {len(txt_files)} tickets in '{folder}'...")

    for filename in txt_files:
        filepath = os.path.join(folder, filename)
        ticket_text = read_ticket(filepath)
        result = triage_ticket(ticket_text)
        print_triage(ticket_text, result, label=filename)


# ── Entry point ────────────────────────────────────────────────────────────────

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print('  python ticket_triage.py "ticket description here"')
        print("  python ticket_triage.py path/to/ticket.txt")
        print("  python ticket_triage.py --batch path/to/folder/")
        sys.exit(1)

    # Batch mode
    if sys.argv[1] == "--batch":
        if len(sys.argv) < 3:
            print("Error: --batch requires a folder path.")
            sys.exit(1)
        run_batch(sys.argv[2])
        return

    # Single ticket mode
    source = sys.argv[1]
    ticket_text = read_ticket(source)

    if not ticket_text:
        print("Error: ticket is empty.")
        sys.exit(1)

    print("\nAnalyzing ticket...")
    result = triage_ticket(ticket_text)
    print_triage(ticket_text, result)


if __name__ == "__main__":
    main()
