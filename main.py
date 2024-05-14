from fastapi import FastAPI, HTTPException, APIRouter, Depends
from app.controllers import product_controller, investment_controller

from app.auth import AuthHandler
from app.db import database

app = FastAPI()

app.include_router(product_controller.router, prefix="/products", tags=["products"])
app.include_router(investment_controller.router, prefix="/investments", tags=["investments"])

router = APIRouter()
auth_handler = AuthHandler()


@router.post("/register")
async def register(username: str, password: str):
    query = "SELECT * FROM users WHERE username= %s"
    query_insert = "INSERT INTO users (username, password) VALUES (%s, %s) RETURNING id"
    # Verificar si el usuario ya está registrado
    existing_user =  database.database.fetch_one(query, (username,))
    if existing_user:
        raise HTTPException(status_code=400, detail="El usuario ya está registrado")

     # Crear un nuevo usuario
    auth_handler = AuthHandler()  # Asegúrate de tener una instancia de AuthHandler
    hashed_password = auth_handler.get_password_hash(password)
    new_user_id = database.database.execute(query_insert, (username, hashed_password))
    return {"mensaje": "Usuario creado correctamente"}

@router.post("/login")
async def login(username: str, password: str):
    # Verificar si el usuario existe
    query = "SELECT * FROM users WHERE username= %s"
    user =    database.database.fetch_one(query, (username,))
    if not user:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

    # Verificar la contraseña
    if not auth_handler.verify_password(password, user['password']):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

    # Generar un token de acceso
    token = auth_handler.encode_token(user['id'])
    return {"token": token}

app.include_router(router)
