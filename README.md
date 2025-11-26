# AI-Powered Image Generator 🎨

An open-source, AI-powered text-to-image generation system that transforms user prompts into high-quality images using state-of-the-art diffusion models. This project was developed as part of the ML Internship Task Assessment for Talrn and focuses on performance, flexibility, ethical AI usage, and user-friendly interaction.

---

## 📌 Project Overview

This application allows users to generate images from textual descriptions using advanced open-source diffusion models such as Stable Diffusion XL and SDXL-Turbo. It provides a web-based interface where users can:

* Enter descriptive text prompts
* Select generation mode (Turbo or Quality)
* Control inference steps and style guidance
* Apply negative prompts for better image control
* View and download AI-generated images
* Automatically store images with metadata and watermark

The system emphasizes:

* Ethical AI usage
* Prompt engineering techniques
* Efficient performance optimization

---

## 🧠 System Architecture

```
User (Browser)
     ↓
Streamlit UI (app.py)
     ↓
Prompt Processing (prompts.py)
     ↓
TextToImage Pipeline (pipeline.py)
     ↓
Diffusers + SDXL / Turbo Model
     ↓
Image Post-Processing (utils.py)
     ↓
Storage + Metadata + Watermark
```

### Core Components

* **app.py** – Streamlit UI and control logic
* **pipeline.py** – Handles model loading and image generation
* **prompts.py** – Prompt enhancement and negative prompt handling
* **utils.py** – Image saving, watermarking, metadata storage
* **config.py** – Model configuration and device setup

---

## 🛠 Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Anushre2005/AI-Image-Generator.git
cd AI-Image-Generator
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Model Download

The model downloads automatically on first run from HuggingFace. Ensure stable internet.

Default model:

```python
MODEL_ID = "stabilityai/sdxl-turbo"
```

### 5. Run Application

```bash
streamlit run app.py
```

---

## 💻 Hardware Requirements

| Configuration  | Recommended Specification         |
| -------------- | --------------------------------- |
| CPU Only       | 8GB RAM minimum                   |
| GPU (Optional) | NVIDIA GPU with 6GB+ VRAM         |
| Storage        | 10GB free (model + cache)         |
| Internet       | Required for first model download |

GPU significantly improves generation speed.

---

## 🚀 Usage Instructions

1. Enter a text prompt (e.g.):

```
A futuristic city at sunset with flying cars
```

2. Select generation mode:

* Turbo (Fast)
* Quality (High Accuracy)

3. Adjust settings:

* Inference steps
* Style guidance
* Number of images

4. Click "Generate Images"

5. Download images in PNG or JPEG format

---

## 🧾 Sample Prompts

* "A fluffy orange cat wearing a wizard hat"
* "Cyberpunk city skyline at night"
* "A robot painting a landscape"

---

## 🧰 Technology Stack

* Python
* Streamlit (UI)
* PyTorch
* Diffusers
* HuggingFace Hub
* Stable Diffusion SDXL / SDXL-Turbo

---

## 🎯 Prompt Engineering Techniques

To improve image quality, the system:

* Appends descriptors like:

  * highly detailed
  * ultra realistic
  * 4k
  * professional photography

* Implements negative prompts to remove:

  * blur
  * distortion
  * artifacts

### Example

Input Prompt:

```
A tiger in a snowy forest
```

Enhanced Prompt:

```
A tiger in a snowy forest, highly detailed, ultra realistic, 4k, professional photography
```

---

## ⚠️ Ethical AI Safeguards

* Image watermark: "AI Generated"
* Category-based content filtering
* Responsible AI usage notice
* Blocks:

  * Explicit content
  * Violence
  * Hate speech
  * Illegal requests

---

## 📂 Storage Structure

Generated images are stored as:

```
outputs/
  └── 20251126_221234/
      ├── image_1.png
      ├── image_1.jpg
      └── metadata.json
```

Metadata includes:

* Prompt
* Negative prompt
* Timestamp
* Parameters

---

## ⏳ Limitations

* Slower generation on CPU
* Limited control over complex object positioning
* High VRAM requirement for quality mode
* Initial model download time

---

## 🔮 Future Improvements

* Fine-tuning on custom datasets
* ControlNet integration for better structure
* Style transfer options
* Resolution selector
* Image-to-image generation
* Gallery history view

---

## ✅ Deliverables Checklist

* ✅ Complete source code
* ✅ Open-source AI model
* ✅ Working Streamlit interface
* ✅ Metadata + export system
* ✅ Ethical AI safeguards
* ✅ Documentation and README

---

## 📬 Contact & Submission

Please email the repository link to:
**[intern@talrn.com](mailto:intern@talrn.com)**

Include:

* Full name
* Contact number
* Availability date

---

## 🙏 Acknowledgements

* HuggingFace Diffusers
* Stability AI
* Streamlit Community

---

### ⭐ If you like this project, give it a star on GitHub!
