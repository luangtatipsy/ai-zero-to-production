import pickle
from typing import Tuple

import numpy as np
import pandas as pd
from scipy import sparse
from src.utils.preprocessing import preprocess

tfidf = pickle.load(open("models/tfidf.pickle", 'rb'))

def load_preset(path: str = "logs/train_df.csv") -> Tuple[pd.DataFrame, np.ndarray]:
    df = pd.read_csv(path)
    X_train = sparse.load_npz("models/movie_vectors.npz")
    
    return df, X_train


def vectorize(text: str) -> str:
    return tfidf.transform([text])
