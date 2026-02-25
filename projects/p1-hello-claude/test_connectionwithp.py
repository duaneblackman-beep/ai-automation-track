"""
Quick connection test — run this after creating your .env file.
If it prints a response, you're ready to open the notebook.

Usage:
    python test_connection.py
"""

import os
from urllib import response
from click import prompt
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


client = anthropic.Anthropic(api_key=api_key)
def ask_claude(prompt, system=None, max_tokens=200):
    """Helper function to make a clean API call and return the text."""
    kwargs = {
        "model": "claude-haiku-4-5-20251001",
        "max_tokens": max_tokens,
        "messages": [{"role": "user", "content": prompt＿１}]
    }
    if system:
        kwargs["system"] = system
    response = client.messages.create(**kwargs)
    return response.content[0].text

# --- Experiment 1 ---
prompt_1 = "Explain what an API is in one sentence."
result_1 = ask_claude(prompt_1)
print("Prompt 1:", prompt_1)
print("Result:", result_1)
print()

    # response = client.messages.create(
    #     model="claude-haiku-4-5-20251001",
    #     max_tokens=100,
    #     system=("You are an expert IT support engineer with 15 years of experience in Financial services. "
    #             "You give concise, technical answers. Always ask one clarifying question if you need more info."),
    #     messages=[
    #         {"role": "user", "content": "My laptop won't connect to the VPN. What should I do?"}
    #     ]
             
        
    # )

    # print("Claude says:", response.content[0].text)
    # print(f"\nTokens used — Input: {response.usage.input_tokens} | Output: {response.usage.output_tokens}")
    #print("\n✅ Everything is working. Open the notebook to start Project 1.")


print("❌ Authentication failed — your API key is invalid or expired.")
print("   Double-check it at console.anthropic.com")



# Look at the full response structure
print("Model used:", response.model)
print("Stop reason:", response.stop_reason)
print("\n--- Usage (tokens) ---")
print("Input tokens:", response.usage.input_tokens)
print("Output tokens:", response.usage.output_tokens)
print("\n--- Content ---")
print(response.content)
