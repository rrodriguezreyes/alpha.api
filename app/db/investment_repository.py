from app.db import database


async def get_holidays():
    query = "SELECT holiday_date FROM holidays"
    holidays = await database.database.fetch_all(query)
    return [holiday["holiday_date"] for holiday in holidays]


async def get_configuration(product_id: int):
    query = "SELECT * FROM products WHERE id = $1"
    result = await database.database.fetch_one(query, product_id)
    return result


async def get_closing_hour():
    query = "SELECT closing_hour FROM products"
    return await database.database.fetch_val(query)
