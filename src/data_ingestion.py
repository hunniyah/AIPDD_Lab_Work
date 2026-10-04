import cv2

class DataIngestion:
    """Handles continuous video/image stream ingestion from RTSP or local sources."""
    def __init__(self, source: str | int = 0):
        self.source = source
        self.cap = cv2.VideoCapture(source)

    def read_frame(self) -> tuple[bool, any]:
        """Captures next frame from input source."""
        return self.cap.read()

    def release(self) -> None:
        """Releases capture resources."""
        if self.cap.isOpened():
            self.cap.release()
