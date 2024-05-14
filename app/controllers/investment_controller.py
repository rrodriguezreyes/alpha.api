# app/api/controllers/investment_controller.py

from fastapi import APIRouter, HTTPException
from app.models.investment import InvestmentRequest, InvestmentResponse
from app.services.investment_service import calculate_investment_dates

router = APIRouter()


@router.post("/investment-dates", response_model=InvestmentResponse)
async def calculate_investment(request: InvestmentRequest):
        investment_dates = await calculate_investment_dates(request)
        return investment_dates

