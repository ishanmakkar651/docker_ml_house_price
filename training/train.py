import pickle
from pathlib import Path

import pandas as pd
from sklearn.linear_model import LinearRegression

# Resolve paths relative to this file so it works no matter the CWD
BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data.csv"
MODEL_DIR = BASE_DIR.parent / "model"
MODEL_PATH = MODEL_DIR / "model.pkl"

df = pd.read_csv(DATA_PATH)

X = df[["area", "bedrooms"]]
y = df["price"]

model = LinearRegression()
model.fit(X, y)

MODEL_DIR.mkdir(parents=True, exist_ok=True)
with MODEL_PATH.open("wb") as f:
    pickle.dump(model, f)

print(f"Model trained & saved successfully to {MODEL_PATH}")
