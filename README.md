# AlpaCare Medical Instruction Assistant

This project fine-tunes **TinyLlama-1.1B-Chat-v1.0** using the **lavita/AlpaCare-MedInstruct-52k** dataset to build a safe, educational, and non-diagnostic medical instruction assistant.  
The model employs **LoRA (Low-Rank Adaptation)** with **PEFT (Parameter-Efficient Fine-Tuning)** for efficient resource use and includes strict safety measures.

---

## 🧠 Project Overview
- Base Model: `TinyLlama/TinyLlama-1.1B-Chat-v1.0`
- Dataset: `lavita/AlpaCare-MedInstruct-52k`
- Fine-tuning: LoRA + PEFT (8-bit quantization)
- Safety: All responses include the disclaimer —  
  *"This is educational only — consult a qualified clinician."*

---

## ⚙️ Setup in Google Colab
Mount Google Drive and navigate to your project:
```python
from google.colab import drive
drive.mount('/content/drive')
%cd /content/drive/MyDrive/AlpaCare-MedInstruct-Assistant
