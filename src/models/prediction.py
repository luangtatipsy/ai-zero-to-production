import pickle
from typing import Dict

import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_distances
from src.features.build_features import load_preset

clf = pickle.load(open("models/classifier.pickle", "rb"))
df, movie_vectors = load_preset()


def predict(x: np.ndarray) -> str:
    return clf.predict(x)[0]


def recommend(x: np.ndarray) -> pd.DataFrame:
    similarities = cosine_distances(movie_vectors, x)
    min_idx = np.argmin(similarities)
    similar_rows = df.loc[[min_idx]]
    similar_rows["similarity"] = similarities[min_idx]

    return similar_rows
