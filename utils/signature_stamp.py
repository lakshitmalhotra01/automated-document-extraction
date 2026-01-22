def detect_signature_stamp(images):
    """
    Dummy signature and stamp detection.
    In real systems, this can be replaced by
    contour analysis or object detection (YOLO).
    """

    signature_present = True
    stamp_present = False

    return {
        "signature": {
            "present": signature_present,
            "bbox": [100, 200, 300, 250]
        },
        "stamp": {
            "present": stamp_present,
            "bbox": []
        }
    }
