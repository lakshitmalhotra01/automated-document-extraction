# Intelligent Document AI for Invoice Field Extraction  
**Convolve 4.0 – Generative AI Track (IDFC FIRST Bank)**

## 1. Problem Overview
Financial institutions process thousands of semi-structured documents such as invoices, quotations, and loan documents. Manual data entry from these documents is slow, error-prone, and expensive.

The goal of this project is to build an **end-to-end Document AI system** that:
- Reads invoice/quotation PDFs
- Extracts key business fields
- Outputs structured JSON suitable for downstream banking workflows

This solution is designed to be:
- Modular
- Explainable
- Cost-efficient
- Easily scalable

---

## 2. Fields Extracted
For each input PDF, the system extracts the following fields:

- **Dealer Name** (Text – fuzzy matching)
- **Model Name** (Exact match using master list)
- **Horse Power** (Numeric)
- **Asset Cost** (Numeric)
- **Dealer Signature** (Presence + bounding box)
- **Dealer Stamp** (Presence + bounding box)

---

## 3. High-Level Architecture

PDF Invoice
↓
PDF to Image Conversion (Poppler)
↓
OCR (PaddleOCR)
↓
Text Aggregation + Bounding Boxes
↓
Rule-based & Fuzzy Field Extraction
↓
Signature & Stamp Detection (heuristic)
↓
Structured JSON Output


This architecture follows a **hybrid OCR + rule-based approach**, which is reliable in low-data scenarios and aligns well with real-world banking constraints.

---

## 4. Technology Stack

| Component | Tool Used |
|---------|----------|
| OCR | PaddleOCR |
| PDF to Image | pdf2image + Poppler |
| Text Matching | RapidFuzz |
| Image Processing | OpenCV |
| Language | Python |

All components are **open-source** and CPU-friendly.

---

## 5. Pipeline Explanation

### Step 1: PDF Ingestion
- Input PDF is converted into images using `pdf2image`
- Poppler is used for reliable page rendering on Windows

### Step 2: OCR
- PaddleOCR extracts text along with spatial information
- Supports scanned and low-quality documents

### Step 3: Field Extraction
- Regular expressions are used for numeric fields (HP, Cost)
- Fuzzy matching is used for model name extraction
- Dealer name extraction is currently rule-based (placeholder)

### Step 4: Signature & Stamp Detection
- Currently implemented using heuristic logic
- Designed to be replaced with object detection models (YOLO) in future

### Step 5: Output Generation
- Results are compiled into a structured JSON
- Confidence, latency, and cost estimates are included

---

## 6. Sample Output Format

```json
{
  "doc_id": "sample_invoice.pdf",
  "fields": {
    "dealer_name": "Dealer Name Not Found",
    "model_name": "Mahindra 575 DI",
    "horse_power": 50,
    "asset_cost": 525000,
    "signature": {
      "present": true,
      "bbox": [100, 200, 300, 250]
    },
    "stamp": {
      "present": false,
      "bbox": []
    }
  },
  "confidence": 0.92,
  "processing_time_sec": 0.15,
  "cost_estimate_usd": 0.002
}


7. Cost & Latency Analysis

Inference Time: ~0.1–0.3 seconds per document (CPU)

Estimated Cost: ~$0.002 per document

Hardware: CPU-only (no GPU required)

This makes the system suitable for large-scale deployment in banking workflows.

8. Handling Lack of Ground Truth

Since no labeled dataset is provided:

Rule-based extraction is used for high-precision fields

Fuzzy matching simulates master data validation

System can be extended with:

Pseudo-labeling

Manual annotation of a small subset

Active learning loops

9. Limitations

Dealer name extraction is basic

Signature & stamp detection is heuristic

No model fine-tuning performed due to lack of labeled data

10. Future Improvements

YOLO-based signature & stamp detection

Multilingual OCR (Hindi, Gujarati)

Visual Language Models (e.g., Qwen-VL)

Active learning for continuous improvement

Layout-aware key-value extraction

11. How to Run the Project
pip install -r requirements.txt
cd submission
python executable.py

12. Conclusion

This project demonstrates a practical, scalable, and explainable Document AI pipeline suitable for real-world banking applications, balancing accuracy, cost, and deployability.
