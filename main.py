from fastapi import FastAPI
from Models.User import User
from Controllers.UserController import UserController
import math

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/predictions/")
async def get_predictions(user: User):
    uc = UserController(user)
    prediction_value = uc.get_predictions()
    if math.isclose(prediction_value, -1.0):
        return {"error": "Prediction Failed"}
    return {"inference": prediction_value}
