import os

# Base paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SAMPLE_DATA_DIR = os.path.join(BASE_DIR, "sample_data")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

# Detection Parameters
IMAGE_SIZE = (224, 224)
MATCH_THRESHOLD = 0.75  # Cosine similarity threshold for individual matching

# Predefined Tiger ID Profiles (Mock Database Embeddings)
KNOWN_TIGER_PROFILES = {
    "Tiger_Alpha": [0.85, 0.12, 0.43, 0.91, 0.05],
    "Tiger_Beta":  [0.10, 0.95, 0.22, 0.08, 0.88],
}
