from ultralytics import YOLO
import numpy as np

class ModelInferenceEngine:
    """Manages model loading, object detection inference, and bounding box extraction."""
    def __init__(self, model_path: str = "yolov8n.pt"):
        self.model = YOLO(model_path)

    def predict(self, frame: np.ndarray, conf_threshold: float = 0.5):
        """Runs object detection pipeline on preprocessed input frame."""
        return self.model.predict(source=frame, conf=conf_threshold)
