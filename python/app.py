import sqlite3
import pandas as pd
from fastapi import FastAPI, Request
import os
from starlette.middleware.cors import CORSMiddleware
from datetime import datetime
from database import init_db, load_dataframe, insert_record, DB_PATH
from fns.fn_build_chart import fn_build_chart
from fns.fn_get_chart import fn_get_chart
from fns.fn_receive_data import fn_receive_data
# Acima, importa bibliotecas e funções necessários para o Backend.

# Instância o FastAPI
app = FastAPI()
# Adiciona middleware. Precisa disso para não 
# dar erro de CORs no Localhost.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ao iniciar backend
@app.on_event("startup")
def startup():
    # Caso o gráfico já exista no sistema
    if os.path.exists("chart.png"):
        # Deleta gráfico.
        os.remove("chart.png")
    # Inicia banco sqlite
    init_db()

@app.post("/data")
async def receive_data(request: Request):
    # Recebe payload como json.
    payload = await request.json()
    timestamp = datetime.now()
    # Obtem temperatura e umidade do payload.
    temperatura = payload["data"]["temperatura"]
    humidade = payload["data"]["humidade"]
    # Insere no banco,
    insert_record(timestamp, temperatura, humidade)
    # Constrói Gráfico.
    fn_build_chart(load_dataframe())
    return

@app.get("/chart")
async def get_chart():
    # Constrói Gráfico.
    fn_build_chart(load_dataframe())
    # Retorna bytes do gráfico criado.
    return fn_get_chart()

@app.delete("/clear")
async def clear_chart():
    # Deleta registros do banco.
    sql = "DELETE FROM registros"
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(sql)
    # Caso o gráfico exista no sistema, deleta ele.
    if os.path.exists("chart.png"):
        os.remove("chart.png")
