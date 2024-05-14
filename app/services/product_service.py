from app.models import product
from app.db import product_repository
from typing import List

async def list_products() -> List[product]:
    return await product_repository.list_products()

async def create_product(product: product):
    return await product_repository.create_product(product)
