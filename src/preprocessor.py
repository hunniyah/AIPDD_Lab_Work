import cv2
import numpy as np

class ImagePreprocessor:
    """Preprocesses raw images into standardized neural network input tensors."""
    def resize_and_normalize(self, image: np.ndarray, target_size=(640, 640)) -> np.ndarray:
        """Resizes image to target dimensions and normalizes pixel values to [0.0, 1.0]."""
        resized = cv2.resize(image, target_size)
        normalized = resized.astype(np.float32) / 255.0
        return normalized
