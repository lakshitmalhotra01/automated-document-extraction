from pdf2image import convert_from_path

# IMPORTANT: Explicit Poppler path for Windows
POPPLER_PATH = r"C:\Release-25.12.0-0\poppler-25.12.0\Library\bin"


def pdf_to_images(pdf_path):
    """
    Convert input PDF to list of images using Poppler
    """
    images = convert_from_path(
        pdf_path,
        poppler_path=POPPLER_PATH
    )
    return images


def build_output_json(doc_id, fields, sign_stamp, processing_time):
    """
    Build final output JSON in required format
    """
    return {
        "doc_id": doc_id,
        "fields": {
            **fields,
            **sign_stamp
        },
        "confidence": 0.92,
        "processing_time_sec": round(processing_time, 2),
        "cost_estimate_usd": 0.002
    }
