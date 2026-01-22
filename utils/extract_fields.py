import re
from rapidfuzz import process

# Example master list (in real system this comes from bank DB)
MODEL_MASTER = [
    "Mahindra 575 DI",
    "Swaraj 744",
    "John Deere 5050D",
    "New Holland 3630"
]


def extract_fields(ocr_results):
    """
    Extract required fields from OCR output using
    simple rules + fuzzy matching.
    """

    # Collect all detected text
    texts = []
    for item in ocr_results:
        texts.append(item[1][0])

    full_text = " ".join(texts)

    # -------- Horse Power Extraction --------
    hp_match = re.search(r'(\d{2,3})\s*HP', full_text, re.IGNORECASE)
    horse_power = int(hp_match.group(1)) if hp_match else None

    # -------- Asset Cost Extraction --------
    cost_match = re.search(r'₹?\s?(\d{5,7})', full_text)
    asset_cost = int(cost_match.group(1)) if cost_match else None

    # -------- Model Name Extraction --------
    model_match = process.extractOne(full_text, MODEL_MASTER)
    model_name = model_match[0] if model_match else None

    # -------- Dealer Name (basic placeholder) --------
    dealer_name = "Dealer Name Not Found"

    return {
        "dealer_name": dealer_name,
        "model_name": model_name,
        "horse_power": horse_power,
        "asset_cost": asset_cost
    }