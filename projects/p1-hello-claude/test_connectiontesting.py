"""
Step 7 — Experiment: Change the Prompt, See What Changes

Three experiments using the same helper function.
Run this and observe how the output changes with each prompt style.

Usage:
    python test_connectiontesting.py
"""

import os
from dotenv import load_dotenv
import anthropic

# --- Setup ---
load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")
client = anthropic.Anthropic(api_key=api_key)


def ask_claude(prompt, system=None, max_tokens=200):
    """Send a prompt to Claude and return the response text."""
    kwargs = {
        "model": "claude-haiku-4-5-20251001",
        "max_tokens": max_tokens,
        "messages": [{"role": "user", "content": prompt}]
    }
    if system:
        kwargs["system"] = system

    response = client.messages.create(**kwargs)

    print("Model used:", response.model)
    print("Stop reason:", response.stop_reason)
    print("Input tokens:", response.usage.input_tokens)
    print("Output tokens:", response.usage.output_tokens)
    print("Response:")
    print(response.content[0].text)


 # --- Experiment 1: Simple direct question (no system prompt) ---
# print("=" * 60)
# print("EXPERIMENT 1 — Simple question, no system prompt")
# print("=" * 60)
# ask_claude("What are the top 3 causes of Okta login failures in enterprise environments?")

# # --- Experiment 2: Same question with a system prompt (role-based) ---
print("\n" + "=" * 60)
print("EXPERIMENT 2 — Same question WITH a system prompt")
print("=" * 60)
ask_claude(
     prompt="What are the top 3 causes of Okta login failures in enterprise environments?",
     system="You are a senior identity engineer with 15 years of experience at enterprise companies. "
         "Give direct, technical answers. Use bullet points. Keep it under 150 words."
)

# --- Experiment 3: Ask for structured output ---
# print("\n" + "=" * 60)
# print("EXPERIMENT 3 — Asking for structured output")
# print("=" * 60)
# ask_claude(
#     prompt="""List the top 3 causes of Okta login failures.
# Format your response exactly like this:
# 1. [cause]: [one sentence explanation] — Fix: [one sentence fix]
# 2. [cause]: [one sentence explanation] — Fix: [one sentence fix]
# 3. [cause]: [one sentence explanation] — Fix: [one sentence fix]"""
# )
