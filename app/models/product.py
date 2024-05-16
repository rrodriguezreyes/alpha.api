from typing import Optional

from pydantic import BaseModel
from datetime import time

class Product(BaseModel):
    id: int
    name: str
    description: Optional[str]
    days_creation_below_operational_hour: int
    days_creation_above_operational_hour: int
    days_creation_below_operational_hour_reinvestment: int
    days_creation_above_operational_hour_reinvestment: int
    operational_hour: time

