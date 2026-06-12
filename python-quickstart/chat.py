"""
DEVUP AI — Chat Completions Quickstart
=======================================
Drop-in replacement for OpenAI. Just change the base_url.

Install:
    pip install openai
    
Usage:
    export DEVUPAI_API_KEY="dvup_your_key_here"
    python chat.py
"""

import os
from openai import OpenAI

# ── Client setup ──────────────────────────────────────────────────────────────
client = OpenAI(
    api_key=os.environ.get("DEVUPAI_API_KEY"),
    base_url="https://api.devupai.com/v1",
)

# ── Simple chat completion ────────────────────────────────────────────────────
def chat(prompt: str, model: str = "meta-llama/Llama-3.3-70B-Instruct-Turbo") -> str:
    """Send a single message and return the response text."""
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant. Answer concisely and clearly.",
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        max_tokens=1024,
        temperature=0.7,
    )
    return response.choices[0].message.content


# ── Multi-turn conversation ───────────────────────────────────────────────────
def multi_turn_chat(model: str = "meta-llama/Llama-3.3-70B-Instruct-Turbo") -> None:
    """Interactive multi-turn conversation in the terminal."""
    print(f"\n🤖 DEVUP AI Chat — Model: {model}")
    print("Type 'exit' to quit, 'clear' to reset conversation.\n")

    history: list[dict] = [
        {
            "role": "system",
            "content": "You are a helpful AI assistant powered by DEVUP AI.",
        }
    ]

    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        if user_input.lower() == "clear":
            history = [history[0]]  # keep system message
            print("✓ Conversation cleared.\n")
            continue

        history.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model=model,
            messages=history,
            max_tokens=1024,
            temperature=0.7,
        )

        assistant_message = response.choices[0].message.content
        history.append({"role": "assistant", "content": assistant_message})

        # Print billing metadata from DEVUP AI
        devup_meta = getattr(response, "_devup", None)
        cost_info = ""
        if devup_meta:
            cost_info = f" | Cost: {devup_meta.get('cost_dzd', '?')} DZD | Balance: {devup_meta.get('balance_dzd', '?')} DZD"

        print(f"\nAssistant: {assistant_message}{cost_info}\n")


# ── Entry point ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Quick single-shot example
    print("=== Single Chat Example ===")
    result = chat("What are the top 3 AI models available today?")
    print(f"Response: {result}\n")

    # Interactive multi-turn
    print("=== Multi-turn Chat ===")
    multi_turn_chat()
