# src/prompts.py

STYLE_TEMPLATES = {
    "Photorealistic": "highly detailed, ultra realistic, 4k, DSLR photography, sharp focus",
    "Artistic": "digital art, highly detailed, concept art, matte painting",
    "Cartoon": "cartoon style, 2D illustration, bold outlines, flat colors",
}

def build_prompt(user_prompt: str, style: str | None = None) -> str:
    base = user_prompt.strip()
    style_descriptor = STYLE_TEMPLATES.get(style, "")
    if style_descriptor:
        return f"{base}, {style_descriptor}"
    return base

def build_negative_prompt(user_negative: str = "") -> str:
    base_negative = "low quality, blurry, deformed, bad anatomy, distorted, watermark, text"
    if user_negative:
        return base_negative + ", " + user_negative
    return base_negative
