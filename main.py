import os
import argparse
import numpy as np
import cv2
from config.settings import SAMPLE_DATA_DIR, KNOWN_TIGER_PROFILES, MATCH_THRESHOLD
from src.detector import AnimalDetector
from src.feature_extractor import FeatureExtractor
from src.matcher import PatternMatcher

def run_pipeline(image_path):
    print("==================================================")
    print(" WILDLIFE RE-IDENTIFICATION PIPELINE ")
    print("==================================================")
    print(f"[+] Processing Input Image: {image_path}")

    # 1. Detection & Crop
    detector = AnimalDetector()
    original, cropped = detector.preprocess_and_crop(image_path)
    print("[+] Step 1: Target animal detected & pattern region cropped.")

    # 2. Pattern Feature Extraction
    extractor = FeatureExtractor()
    pattern_vec = extractor.extract_pattern_vector(cropped)
    print(f"[+] Step 2: Extracted Stripe Feature Vector: {np.round(pattern_vec, 3)}")

    # 3. Matching
    matcher = PatternMatcher(KNOWN_TIGER_PROFILES, threshold=MATCH_THRESHOLD)
    identity, score = matcher.identify_individual(pattern_vec)
    
    print("\n---------------- RESULTS ----------------")
    print(f" Identified Individual ID : {identity}")
    print(f" Pattern Match Score      : {score:.4f}")
    print("------------------------------------------\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="WildID CLI Pipeline")
    parser.add_argument("--image", type=str, help="Path to input image")
    args = parser.parse_args()

    # Create dummy sample image if none provided
    if not args.image or not os.path.exists(args.image):
        dummy_path = os.path.join(SAMPLE_DATA_DIR, "test_tiger.jpg")
        os.makedirs(SAMPLE_DATA_DIR, exist_ok=True)
        dummy_img = np.random.randint(0, 256, (400, 600, 3), dtype=np.uint8)
        cv2.imwrite(dummy_path, dummy_img)
        target_file = dummy_path
    else:
        target_file = args.image

    run_pipeline(target_file)