# src/config.py
import torch

MODEL_ID = "stabilityai/sdxl-turbo"

TORCH_DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
ENABLE_NSFW_FILTER = True

OUTPUT_DIR = "outputs"
