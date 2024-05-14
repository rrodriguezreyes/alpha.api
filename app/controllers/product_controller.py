from fastapi import APIRouter, HTTPException, status
from typing import List, Optional
from app.models.product import Product
from app.services.product_service import list_products, create_product

router = APIRouter()


@router.get("/", response_model=List[Product])
async def get_products():
        return await list_products()



@router.post("/")
async def add_product(product: Product):
    try:
        created_product = await create_product(product)
        return created_product
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")
