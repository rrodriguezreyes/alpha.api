from pydantic import BaseModel


class InvestmentRequest(BaseModel):
    product_id: int
    en_reinversion: bool
    plazo: int
    fecha_creacion: str


class InvestmentResponse(BaseModel):
    product_id : int
    plazo : int
    fechaInicio: str
    fechaFin: str
    plazoReal: int



