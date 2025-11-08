---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Create a comprehensive evaluator for math problems

rft_evaluator_code = '''
import re
from reward_kit import reward_function
from reward_kit.models import EvaluateResult

@reward_function
def evaluate(messages: list[dict], **kwargs) -> EvaluateResult:
    """
    RFT Evaluator: Compare model answer with ground truth
    Optimized for [WORK]/[RESULT] format from SFT stage
    """

    # Get ground truth from dataset

    ground_truth_answer = kwargs.get('ground_truth')
    if not ground_truth_answer:
        return EvaluateResult(score=0.0, reason="No ground truth found in dataset")

    # Get the model's generated response (last message)

    model_response = messages[-1]["content"]

    # Extract model's answer using multiple methods

    model_answer = extract_model_answer(model_response)

    if not model_answer:
        return EvaluateResult(score=0.0, reason="No answer extracted from model response")

    # Clean and compare answers

    ground_truth_clean = clean_answer(ground_truth_answer)
    model_answer_clean = clean_answer(model_answer)

    if model_answer_clean == ground_truth_clean:
        return EvaluateResult(score=1.0, reason=f"Correct: {model_answer_clean}")
    else:
        return EvaluateResult(score=0.0, reason=f"Wrong: {model_answer_clean} vs {ground_truth_clean}")

def extract_model_answer(text: str) -> str:
    """Extract answer from model response, prioritizing our learned format"""

    # Method 1: [RESULT] tags (primary method for our SFT model)

    result_match = re.search(r'\\[RESULT\\](.*?)\\[/RESULT\\]', text, re.DOTALL)
    if result_match:
        return result_match.group(1).strip()

    # Method 2: \\boxed{} format (fallback)

    boxed_match = re.search(r'\\\\boxed\\{([^}]+)\\}', text)
    if boxed_match:
        return boxed_match.group(1).strip()

    # Method 3: Last significant number in text

    numbers = re.findall(r'\\b(\\d+(?:,\\d{3})*(?:\\.\\d+)?)\\b', text)
    if numbers:
        significant_numbers = [n for n in numbers if float(n.replace(',', '')) >= 1]
        if significant_numbers:
            return significant_numbers[-1]

    return None

def clean_answer(answer_str: str) -> str:
    """Clean and normalize answer"""
    if not answer_str:
        return ""

    # Remove whitespace, commas, dollar signs

    cleaned = re.sub(r'[,$\\s]', '', str(answer_str).strip())

    # Convert to int if whole number

    try:
        if '.' in cleaned:
            float_val = float(cleaned)
            if float_val.is_integer():
                return str(int(float_val))
            else:
                return str(float_val)
        else:
            return str(int(cleaned))
    except ValueError:
        return cleaned
'''

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
