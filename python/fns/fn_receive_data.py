import pandas as pd
from fastapi import Request
from datetime import datetime

async def fn_receive_data(
    request: Request,
    df: pd.DataFrame
):
    new_data = await request.json()
    temperatura = new_data["temperatura"]
    humidade = new_data["humidade"]
    df.loc[len(df)] = {
        "timestamp": pd.Timestamp.now(),
        "temperatura": temperatura,
        "humidade": humidade
    }
    return