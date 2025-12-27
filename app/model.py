import pickle
from pathlib import Path

import numpy as np


def _load_model():
    model_path = Path(__file__).resolve().parent.parent / "model" / "model.pkl"
    if not model_path.exists():
        raise FileNotFoundError(f"Model file not found at {model_path}")
    with model_path.open("rb") as f:
        return pickle.load(f)


model = _load_model()


def predict_price(area: float, bedrooms: int):
    data = np.array([[area, bedrooms]])
    return float(model.predict(data)[0])
