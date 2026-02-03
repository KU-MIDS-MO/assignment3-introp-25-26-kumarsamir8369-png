import numpy as np

def clean_and_scale_scores(scores, min_score, max_score):
    scores = np.array(scores, dtype=float)

    # Step 1 & 2: clip values
    clipped = np.clip(scores, min_score, max_score)

    # Step 3: scale to [0, 1]
    scaled = (clipped - min_score) / (max_score - min_score)

    return scaled
