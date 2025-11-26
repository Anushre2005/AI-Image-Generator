# app.py
import time
import streamlit as st
from src.pipeline import TextToImageGenerator
from src.prompts import build_prompt, build_negative_prompt
from src.utils import get_run_dir, save_images_with_metadata

BANNED_CATEGORIES = {
    "sexual_content": [
        "nude", "naked", "porn", "sex", "erotic", "explicit"
    ],
    "violence": [
        "gore", "murder", "kill", "torture", "beheading"
    ],
    "illegal_activities": [
        "bomb", "drug dealing", "counterfeit", "terrorist", "hack bank"
    ],
    "hate_speech": [
        "genocide", "nazi", "supremacist", "ethnic cleansing"
    ],
    "weapons": [
        "gun", "rifle", "grenade", "explosive", "weapon"
    ],
    "self_harm": [
        "suicide", "self harm", "cutting", "overdose"
    ]
}

INSTRUCTION_PHRASES = [
    "how to make",
    "how to build",
    "step by step",
    "tutorial for",
    "instructions for"
]

def is_prompt_allowed(prompt: str) -> bool:
    prompt_lower = prompt.lower()

    # Collect all harmful words
    harmful_keywords = sum(BANNED_CATEGORIES.values(), [])

    # If instruction phrase AND harmful content → BLOCK
    if any(phrase in prompt_lower for phrase in INSTRUCTION_PHRASES):
        if any(bad in prompt_lower for bad in harmful_keywords):
            return False

    # Also block direct harmful content in general
    if any(bad in prompt_lower for bad in harmful_keywords):
        return False

    return True


st.set_page_config(page_title="AI Image Generator", layout="wide")

@st.cache_resource
def load_generator():
    return TextToImageGenerator()

def main():
    st.title("AI-Powered Text-to-Image Generator 🎨")
    st.warning("""
                ⚠ Responsible AI Use Guidelines:
                - Do not generate harmful, explicit, violent, or misleading content.
                - This tool is for educational and creative purposes only.
                - All images are AI-generated and watermarked accordingly.
                """)

    with st.sidebar:
        
        st.header("Generation Settings")
        mode = st.selectbox(
            "Generation Mode",
            ["Turbo (Fast)", "Quality (High Accuracy)"]
        )

        num_images = st.slider("Number of images", 1, 4, 1)
        style = st.selectbox("Style guidance", ["Photorealistic", "Artistic", "Cartoon"])
        if mode == "Turbo (Fast)":
            steps = st.slider("Inference Steps (Turbo)", 1, 6, 4, 1)
            guidance_scale = 0.0
            st.info("Turbo mode uses fixed guidance scale = 0.0 for maximum speed.")
        else:
            steps = st.slider("Inference Steps (Quality)", 20, 50, 30, 5)
            guidance_scale = st.slider("Guidance Scale (CFG)", 5.0, 12.0, 8.0, 0.5)

        use_seed = st.checkbox("Use fixed seed", value=False)
        if use_seed:
            seed = st.number_input("Seed value", min_value=0, max_value=999999, value=42)
        else:
            seed = None

        st.markdown("### Negative Prompt")
        user_negative = st.text_area("Additional negative prompt", value="", height=60)

    prompt = st.text_area("Enter your prompt:", "a futuristic city at sunset, flying cars", height=100)
    custom_filename = st.text_input("Custom filename (without extension)", value="my_image")

    generate_btn = st.button("Generate Images")

    if generate_btn and prompt.strip():

        if not is_prompt_allowed(prompt):
            st.error("This prompt violates ethical content guidelines. Please modify it.")
            return
        generator = load_generator()

        full_prompt = build_prompt(prompt, style)
        negative_prompt = build_negative_prompt(user_negative)

        st.info(f"Final prompt used:\n\n`{full_prompt}`")
        st.info(f"Negative prompt:\n\n`{negative_prompt}`")

        progress = st.progress(0)
        status_text = st.empty()
        eta_text = st.empty()

        start_time = time.time()

        for i in range(steps):
            progress.progress(int((i + 1) / steps * 100))

            elapsed = time.time() - start_time
            avg_step_time = elapsed / (i + 1)
            remaining_steps = steps - (i + 1)

            eta = avg_step_time * remaining_steps

            status_text.text("Generating images...")
            eta_text.text(f"Estimated time remaining: {eta:.1f} seconds")



        images = generator.generate(
            prompt=full_prompt,
            negative_prompt=negative_prompt,
            num_images=num_images,
            guidance_scale=guidance_scale,
            num_inference_steps=steps,
            seed=seed if use_seed else None,
            mode=mode
        )


        end_time = time.time()
        elapsed = end_time - start_time
        status_text.text(f"Generation completed in {elapsed:.1f} seconds")
        eta_text.text("Estimated time remaining: 0 seconds")


        run_dir = get_run_dir()
        params = {
            "num_images": num_images,
            "guidance_scale": guidance_scale,
            "steps": steps,
            "style": style,
            "seed": seed if use_seed else None,
        }

        saved_paths = save_images_with_metadata(
            images,
            run_dir,
            full_prompt,
            negative_prompt,
            params,
            base_filename=custom_filename
        )

        st.subheader("Generated Images")

        cols = st.columns(num_images)
        for i, img in enumerate(images):
            with cols[i]:
                st.image(img, caption=f"Image {i+1}")
                st.write("Download:")
                st.download_button(
                    label="Download PNG",
                    data=open(saved_paths[i]["png"], "rb").read(),
                    file_name=f"generated_{i+1}.png",
                    mime="image/png",
                )
                st.download_button(
                    label="Download JPEG",
                    data=open(saved_paths[i]["jpg"], "rb").read(),
                    file_name=f"generated_{i+1}.jpg",
                    mime="image/jpeg",
                )

if __name__ == "__main__":
    main()
