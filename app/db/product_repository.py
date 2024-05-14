from app.models.product import Product
from app.db import database
from typing import List


async def list_products() -> List[Product]:
    query = "SELECT * FROM products"
    products_records = database.database.fetch_all(query=query)

    products = []
    for product_record in products_records:
        product = Product(
            id=product_record['id'],
            name=product_record['name'],
            description=product_record['description'],
            days_creation_below_operational_hour=product_record['days_creation_below_operational_hour'],
            days_creation_above_operational_hour=product_record['days_creation_above_operational_hour'],
            days_creation_below_operational_hour_reinvestment=product_record[
                'days_creation_below_operational_hour_reinvestment'],
            days_creation_above_operational_hour_reinvestment=product_record[
                'days_creation_above_operational_hour_reinvestment'],
            operational_hour=product_record['operational_hour']
        )
        products.append(product)

    return products


async def create_product(product: Product):
    query = "INSERT INTO products (name, description, days_creation_below_operational_hour, days_creation_above_operational_hour, days_creation_below_operational_hour_reinvestment, days_creation_above_operational_hour_reinvestment, operational_hour) VALUES ($1, $2, $3, $4, $5, $6, $7)"
    try:
        database.database.execute(query=query, values=(
        product.name, product.description, product.days_creation_below_operational_hour,
        product.days_creation_above_operational_hour, product.days_creation_below_operational_hour_reinvestment,
        product.days_creation_above_operational_hour_reinvestment, product.operational_hour))
        return {"message": "Product created successfully"}
    except Exception as e:
        # Handle the error properly (e.g., logging it, returning a specific error message, etc.)
        return {"error": str(e)}
