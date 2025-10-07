"""
data_loader.py
-----------------------------------
Utility script for loading and preprocessing the
lavita/AlpaCare-MedInstruct-52k dataset for fine-tuning.
"""

from datasets import load_dataset

def load_medical_dataset():
    """Load and format dataset with disclaimers and splits."""
    print("📥 Loading dataset from Hugging Face...")
    dataset = load_dataset("lavita/AlpaCare-MedInstruct-52k")

    def format_example(example):
        instruction = example.get("instruction", "")
        input_text = example.get("input", "")
        output_text = example.get("output", "")
        return {
            "text": f"### Instruction:\n{instruction}\n\n"
                    f"### Input:\n{input_text}\n\n"
                    f"### Response:\n{output_text}\n\n"
                    f"### Disclaimer:\nThis is educational only — consult a qualified clinician."
        }

    print("⚙️ Formatting examples...")
    formatted_dataset = dataset.map(format_example)

    print("✂️ Splitting dataset...")
    split_dataset = formatted_dataset["train"].train_test_split(test_size=0.1, seed=42)
    val_test_split = split_dataset["test"].train_test_split(test_size=0.5, seed=42)

    train_data = split_dataset["train"]
    val_data = val_test_split["train"]
    test_data = val_test_split["test"]

    print(f"✅ Train: {len(train_data)} | Val: {len(val_data)} | Test: {len(test_data)}")
    return train_data, val_data, test_data
