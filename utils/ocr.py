from paddleocr import PaddleOCR

# Initialize OCR model (English + layout handling)
ocr_model = PaddleOCR(
    use_angle_cls=True,
    lang="en"
)


def run_ocr(images):
    """
    Runs OCR on a list of images and returns extracted text
    along with bounding boxes.
    """
    ocr_results = []

    for img in images:
        result = ocr_model.ocr(img)

        # Each result contains [box, (text, confidence)]
        for line in result:
            ocr_results.append(line)

    return ocr_results
