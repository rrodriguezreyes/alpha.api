# app/api/controllers/investment_controller.py
from datetime import datetime

from fastapi import APIRouter, HTTPException
from app.models.investment import InvestmentRequest, InvestmentResponse
from app.services.investment_service import calculate_investment_dates

router = APIRouter()


@router.post("/investment-dates", response_model=InvestmentResponse)
async def calculate_investment(request: InvestmentRequest):
        try:
                # Parsear la fecha de creación
                fecha_inicio = datetime.strptime(request.fecha_creacion, "%Y-%m-%d %H:%M:%S")

                # Calcular las fechas de inversión
                investment_dates = await calculate_investment_dates(request)

                return investment_dates

        except ValueError as ve:
                raise HTTPException(status_code=400, detail=str(ve))

