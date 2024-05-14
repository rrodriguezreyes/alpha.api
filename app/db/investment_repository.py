from app.db import database


async def get_holidays():
    query = "SELECT holiday_date FROM holidays"
    holidays = database.database.fetch_all(query)
    return [holiday["holiday_date"] for holiday in holidays]


async def get_configuration(product_id: int):
    query = "SELECT * FROM products WHERE id = %s"
    result = database.database.fetch_one(query, (product_id,))
    return result


async def get_closing_hour():
    query = "SELECT closing_hour FROM products"
    return  database.database.fetch_val(query)