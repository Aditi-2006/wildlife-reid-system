import numpy as np

class PatternMatcher:
    """Module 3: Performs similarity search against known database profiles."""
    def __init__(self, database_profiles, threshold=0.75):
        self.database = database_profiles
        self.threshold = threshold

    def _cosine_similarity(self, vec_a, vec_b):
        a = np.array(vec_a)
        b = np.array(vec_b)
        return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

    def identify_individual(self, feature_vector):
        best_match = "Unknown_New_Individual"
        highest_score = -1.0

        for animal_id, ref_vector in self.database.items():
            score = self._cosine_similarity(feature_vector, ref_vector)
            if score > highest_score:
                highest_score = score
                best_match = animal_id

        if highest_score < self.threshold:
            return "New_Tiger_Registration", highest_score
        return best_match, highest_score