# src/utils.py
import os
import json
from datetime import datetime
from typing import Dict, List
from PIL import Image
import numpy as np
import cv2

from .config import OUTPUT_DIR

def ensure_output_dir():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

def get_run_dir() -> str:
    ensure_output_dir()
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    run_dir = os.path.join(OUTPUT_DIR, ts)
    os.makedirs(run_dir, exist_ok=True)
    return run_dir

def add_watermark(pil_img: Image.Image, text: str = "AI Generated"):
    # Convert PIL -> OpenCV
    img = np.array(pil_img)
    if img.ndim == 3 and img.shape[2] == 3:
        pass
    else:
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)

    h, w, _ = img.shape
    overlay = img.copy()

    font = cv2.FONT_HERSHEY_SIMPLEX
    scale = max(w, h) / 1000.0
    thickness = 2
    margin = 10

    text_size, _ = cv2.getTextSize(text, font, scale, thickness)
    text_w, text_h = text_size
    x = w - text_w - margin
    y = h - margin

    cv2.putText(overlay, text, (x, y), font, scale, (255, 255, 255), thickness, cv2.LINE_AA)

    alpha = 0.4
    watermarked = cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0)
    return Image.fromarray(watermarked)

def save_images_with_metadata(
    images: List[Image.Image],
    run_dir: str,
    prompt: str,
    negative_prompt: str,
    params: Dict,
    base_filename: str = "image",
):
    metadata = {
        "prompt": prompt,
        "negative_prompt": negative_prompt,
        "params": params,
        "timestamp": datetime.now().isoformat(),
        "num_images": len(images),
    }

    meta_path = os.path.join(run_dir, "metadata.json")
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=4)

    saved_paths = []
    for i, img in enumerate(images):
        watermarked = add_watermark(img, "AI Generated - Talrn Task")
        # Save as PNG and JPEG
        png_path = os.path.join(run_dir, f"{base_filename}_{i+1}.png")
        jpg_path = os.path.join(run_dir, f"{base_filename}_{i+1}.jpg")

        watermarked.save(png_path, format="PNG")
        watermarked.convert("RGB").save(jpg_path, format="JPEG", quality=95)
        saved_paths.append({"png": png_path, "jpg": jpg_path})

    return saved_paths
