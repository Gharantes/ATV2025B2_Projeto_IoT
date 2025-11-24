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

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],            # use specific origin in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Initialize the SQLite database on startup
@app.on_event("startup")
def startup():
    if os.path.exists("chart.png"):
        os.remove("chart.png")
    init_db()

@app.post("/data")
async def receive_data(request: Request):
    payload = await request.json()
    print(payload)
    timestamp = datetime.now()
    temperatura = payload["data"]["temperatura"]
    humidade = payload["data"]["humidade"]
    insert_record(timestamp, temperatura, humidade)
    fn_build_chart(load_dataframe())
    return
@app.get("/chart")
async def get_chart():
    fn_build_chart(load_dataframe())
    return fn_get_chart()

@app.delete("/clear")
async def clear_chart():
    sql = "DELETE FROM registros"
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(sql)
    if os.path.exists("chart.png"):
        os.remove("chart.png")
