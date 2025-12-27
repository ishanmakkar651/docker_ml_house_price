from fastapi import FastAPI
from app.model import predict_price   

app = FastAPI()

@app.get("/")
def home():
    return {"message": "ML Docker API Running"}

@app.get("/predict")
def predict(area: float, bedrooms: int):
    price = predict_price(area, bedrooms)
    return {
        "area": area,
        "bedrooms": bedrooms,
        "predicted_price": price
    }
