"""
DEVUP AI — Streaming Responses
================================
Real-time token streaming — tokens appear as they're generated.

Install:
    pip install openai
    
Usage:
    export DEVUPAI_API_KEY="dvup_your_key_here"
    python streaming.py
"""

import os
import sys
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("DEVUPAI_API_KEY"),
    base_url="https://api.devupai.com/v1",
)


def stream_chat(
    prompt: str,
    model: str = "meta-llama/Llama-3.3-70B-Instruct-Turbo",
    system: str = "You are a helpful assistant.",
) -> str:
    """
    Stream a chat completion, printing tokens as they arrive.
    Returns the full assembled response.
    """
    print(f"\n🤖 [{model}]\n", flush=True)

    full_response = []

    with client.chat.completions.stream(
        model=model,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ],
        max_tokens=2048,
        temperature=0.7,
    ) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)
            full_response.append(text)

    print("\n")  # newline after stream ends
    return "".join(full_response)


def stream_code_generation(task: str) -> str:
    """Specialized streaming for code generation tasks."""
    return stream_chat(
        prompt=task,
        model="Qwen/Qwen2.5-Coder-32B-Instruct",
        system=(
            "You are an expert software engineer. "
            "Write clean, well-documented, production-ready code. "
            "Always include error handling and type hints."
        ),
    )


# ── Entry point ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=== Streaming Chat Example ===")
    stream_chat(
        prompt="Explain how neural networks learn in simple terms.",
        model="meta-llama/Llama-3.3-70B-Instruct",
    )

    print("=== Streaming Code Generation ===")
    stream_code_generation(
        task="Write a Python function that validates an Algerian phone number (starts with 05, 06, or 07, followed by 8 digits)."
    )
