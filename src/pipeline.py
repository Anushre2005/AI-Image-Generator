# src/pipeline.py
import torch
from diffusers import StableDiffusionXLPipeline


from .config import MODEL_ID, TORCH_DEVICE, ENABLE_NSFW_FILTER



class TextToImageGenerator:
    def __init__(self):
        self.device = TORCH_DEVICE
        self.pipe = StableDiffusionXLPipeline.from_pretrained(
            MODEL_ID,
            torch_dtype=torch.float16 if "cuda" in self.device else torch.float32,
            use_safetensors=True,
            variant="fp16" if "cuda" in self.device else None
        )

        self.pipe.to(self.device)
        self.pipe.enable_attention_slicing()
        self.pipe.enable_vae_slicing()
   


    def generate(
        self,
        prompt: str,
        negative_prompt: str = "",
        num_images: int = 1,
        guidance_scale: float = 7.5,
        num_inference_steps: int = 30,
        seed: int | None = None,
        mode: str = "Turbo (Fast)",
    ):
        generator = torch.Generator(device=self.device)
        if seed is not None:
            generator = generator.manual_seed(seed)

        if mode == "Turbo (Fast)":
            images = self.pipe(
                prompt=prompt,
                num_images_per_prompt=num_images,
                num_inference_steps=num_inference_steps,
                guidance_scale=0.0,
                generator=generator,
            ).images
        else:
            images = self.pipe(
                prompt=prompt,
                negative_prompt=negative_prompt,
                num_images_per_prompt=num_images,
                num_inference_steps=num_inference_steps,
                guidance_scale=guidance_scale,
                generator=generator,
            ).images

        return images
