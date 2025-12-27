# ML House Price Predictor (Dockerized FastAPI)

## Overview
- FastAPI service that predicts house prices from `area` and `bedrooms`.
- Model trained with scikit-learn; packaged into a Docker image with the model baked in.

## Project Layout
- app/main.py — FastAPI endpoints (`/` health, `/predict`).
- app/model.py — Loads the trained sklearn model and exposes `predict_price`.
- training/train.py — Trains LinearRegression on `training/data.csv` and saves `model/model.pkl`.
- model/ — Stores the trained `model.pkl` after build.
- Dockerfile — Builds image, installs deps, trains model, runs uvicorn.
- requirements.txt — Python dependencies.

## Quickstart (Docker)
1) Build image:
	- `docker build -t ml-house-price .`
2) Run container:
	- `docker run -p 8000:8000 ml-house-price`
3) Test API:
	- Root health: `curl http://localhost:8000/`
	- Swagger UI: http://localhost:8000/docs
	- Prediction: `curl "http://localhost:8000/predict?area=1200&bedrooms=3"`

## Local (without Docker)
1) Create venv and install deps: `python -m venv .venv && .venv\Scripts\activate && pip install -r requirements.txt`
2) Train model: `python training/train.py`
3) Run API: `uvicorn app.main:app --reload`

## How to Train with New Data
1) Update `training/data.csv` with new rows (columns: `area,bedrooms,price`).
2) Re-train: `python training/train.py` (or rebuild Docker image).
3) Restart the API container to pick up the new `model.pkl`.

## Publishing to GitHub (manual steps)
1) Initialize repo (if not already): `git init`.
2) Add files: `git add .`
3) Commit: `git commit -m "Add ML house price API"`
4) Create a GitHub repo (via UI) named `ml-house-price` (or your choice).
5) Add remote: `git remote add origin https://github.com/<your-username>/<repo>.git`
6) Push: `git push -u origin main` (create `main` if prompted: `git branch -M main`).

## Notes
- Container publishes port 8000; adjust mapping with `-p <host_port>:8000` as needed.
- Model is baked at image build time; rebuild image whenever training data changes.
