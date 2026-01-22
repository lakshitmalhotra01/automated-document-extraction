import time

from utils.ocr import run_ocr
from utils.extract_fields import extract_fields
from utils.signature_stamp import detect_signature_stamp
from utils.helpers import pdf_to_images, build_output_json


def main(pdf_path):
    """
    Main pipeline:
    PDF -> Images -> OCR -> Field Extraction -> JSON Output
    """
    start_time = time.time()

    # 1. Convert PDF to images
    images = pdf_to_images(pdf_path)

    # 2. Run OCR on images
    ocr_results = run_ocr(images)

    # 3. Extract required fields
    fields = extract_fields(ocr_results)

    # 4. Detect signature and stamp
    sign_stamp = detect_signature_stamp(images)

    # 5. Build final output
    output = build_output_json(
        doc_id=pdf_path,
        fields=fields,
        sign_stamp=sign_stamp,
        processing_time=time.time() - start_time
    )

    return output


if __name__ == "__main__":
    # Example run (organizers will replace this PDF)
    result = main("sample_invoice.pdf")
    print(result)
