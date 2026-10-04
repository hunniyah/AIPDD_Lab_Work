import logging
import time

class AlertLogger:
    """Handles incident logging and alert payload dispatches."""
    def __init__(self, log_path: str = "logs/events.log"):
        logging.basicConfig(filename=log_path, level=logging.INFO, format="%(asctime)s - %(message)s")

    def log_event(self, class_name: str, confidence: float, bbox: list) -> None:
        """Records detection entry with timestamp and bounding box coordinates."""
        logging.info(f"Detected: {class_name} | Conf: {confidence:.2f} | BBox: {bbox}")
