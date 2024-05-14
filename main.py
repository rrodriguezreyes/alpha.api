from fastapi import FastAPI
from app.controllers import product_controller ,  investment_controller

app = FastAPI()

app.include_router(product_controller.router, prefix="/products", tags=["products"])
app.include_router(investment_controller.router, prefix="/investments", tags=["investments"])

