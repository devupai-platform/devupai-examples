"""
DEVUP AI — Image Generation
=============================
Generate images using FLUX and other image models.

Install:
    pip install openai requests Pillow
    
Usage:
    export DEVUPAI_API_KEY="dvup_your_key_here"
    python image_generation.py
"""

import os
import base64
import requests
from pathlib import Path
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("DEVUPAI_API_KEY"),
    base_url="https://api.devupai.com/v1",
)

# Available image models on DEVUP AI
IMAGE_MODELS = {
    "flux-schnell": "black-forest-labs/FLUX.1-schnell",   # Fast, good quality
    "flux-dev":     "black-forest-labs/FLUX.1-dev",       # High quality
    "flux-pro":     "black-forest-labs/FLUX.1-pro",       # Best quality
}


def generate_image(
    prompt: str,
    model: str = "black-forest-labs/FLUX.1-schnell",
    width: int = 1024,
    height: int = 1024,
    steps: int = 4,
    output_path: str | None = None,
) -> str:
    """
    Generate an image from a text prompt.
    Returns the image URL or saves to output_path if provided.
    """
    print(f"🎨 Generating image with {model}...")
    print(f"   Prompt: {prompt[:80]}{'...' if len(prompt) > 80 else ''}")

    response = client.images.generate(
        model=model,
        prompt=prompt,
        size=f"{width}x{height}",
        n=1,
        extra_body={"num_inference_steps": steps},
    )

    image_url = response.data[0].url
    print(f"✓ Image generated: {image_url}\n")

    # Optionally download and save locally
    if output_path:
        _save_image(image_url, output_path)

    return image_url


def generate_image_b64(
    prompt: str,
    model: str = "black-forest-labs/FLUX.1-schnell",
    width: int = 1024,
    height: int = 1024,
) -> bytes:
    """Generate an image and return raw bytes (base64 decoded)."""
    response = client.images.generate(
        model=model,
        prompt=prompt,
        size=f"{width}x{height}",
        response_format="b64_json",
        n=1,
    )
    return base64.b64decode(response.data[0].b64_json)


def _save_image(url: str, path: str) -> None:
    """Download image from URL and save to disk."""
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    Path(path).write_bytes(response.content)
    print(f"✓ Saved to: {path}")


# ── Entry point ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Example 1: Generate a landscape
    url = generate_image(
        prompt="A stunning aerial view of Algiers at sunset, the Mediterranean Sea glistening, modern city skyline, photorealistic, 8K",
        model=IMAGE_MODELS["flux-schnell"],
        width=1024,
        height=768,
        output_path="algiers_sunset.jpg",
    )

    # Example 2: Generate a logo concept
    generate_image(
        prompt="Minimalist tech startup logo, geometric shapes, dark background, neon blue and purple gradient, professional, vector style",
        model=IMAGE_MODELS["flux-dev"],
        width=1024,
        height=1024,
        output_path="logo_concept.jpg",
    )

    print("Done! Check the generated images in your current directory.")
