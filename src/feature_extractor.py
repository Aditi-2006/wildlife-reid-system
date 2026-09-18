import numpy as np

class FeatureExtractor:
    """Module 2: Extracts lightweight feature vector representing stripe patterns."""
    def __init__(self):
        pass

    def extract_pattern_vector(self, cropped_img):
        # Convert to grayscale to highlight stripe intensity patterns
        gray = np.mean(cropped_img, axis=2)
        # Compute histogram features as lightweight pattern descriptor
        hist, _ = np.histogram(gray, bins=5, range=(0, 255))
        norm_hist = hist / np.linalg.norm(hist)
        return norm_hist.tolist()