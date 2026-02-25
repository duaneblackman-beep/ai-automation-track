"""
Quick connection test — run this after creating your .env file.
If it prints a response, you're ready to open the notebook.

Usage:
    python test_connection.py
"""

import os
from dotenv import load_dotenv
import anthropic

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")

if not api_key or api_key == "sk-ant-your-key-here":
    print("❌ No API key found.")
    print("   Create a .env file in this folder with:")
    print("   ANTHROPIC_API_KEY=sk-ant-...")
    print("   Get your key at: console.anthropic.com")
    exit(1)

print(f"✅ API key loaded — starts with: {api_key[:14]}...")
print("   Sending test message to Claude...\n")

try:
    client = anthropic.Anthropic(api_key=api_key)

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",  # fastest and cheapest model — good for experiments
        max_tokens=256,
        system="You are an expert IT support engineer with 15 years of experience in financial services. "
            "You give concise, technical answers. Always ask one clarifying question if you need more info.",

        messages=[
            {"role": "user", "content": "Hello! Who are you and what can you do?"}
        ]
    )

    print("Claude says:", response.content[0].text)

except anthropic.AuthenticationError:
    print("❌ Authentication failed — your API key is invalid or expired.")
    print("   Double-check it at console.anthropic.com")

except Exception as e:
    print(f"❌ Unexpected error: {e}")
    # Look at the full response structure
print("Model used:", response.model)
print("Stop reason:", response.stop_reason)
print("\n--- Usage (tokens) ---")
print("Input tokens:", response.usage.input_tokens)
print("Output tokens:", response.usage.output_tokens)
print("\n--- Content ---")
print(response.content)
