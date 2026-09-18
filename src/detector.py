import cv2
import numpy as np

class AnimalDetector:
    """Module 1: Preprocesses camera trap image and detects target ROI."""
    def __init__(self, target_size=(224, 224)):
        self.target_size = target_size

    def preprocess_and_crop(self, image_path):
        image = cv2.imread(image_path)
        if image is None:
            raise FileNotFoundError(f"Could not read image from {image_path}")
        
        # Convert color space and crop central region (Animal flank pattern)
        h, w, _ = image.shape
        crop = image[int(h*0.2):int(h*0.8), int(w*0.2):int(w*0.8)]
        resized = cv2.resize(crop, self.target_size)
        return image, resized