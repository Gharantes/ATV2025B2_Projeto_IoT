import pandas as pd
import matplotlib.pyplot as plt

def fn_build_chart(df: pd.DataFrame):
    if df.empty: return
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["time_only"] = df["timestamp"].dt.strftime("%d/%m %H:%M:%S")
    df["time_only"] = df["time_only"].astype(str).str.split(".").str[0]


    plt.figure(figsize=(8, 4))
    plt.plot(df["time_only"], df["temperatura"], marker="o", label="Temperatura")
    plt.plot(df["time_only"], df["humidade"], marker="o", label="Humidade")

    plt.xlabel("Tempo")
    plt.xticks(rotation=90)
    plt.legend()
    plt.tight_layout()
    plt.savefig("chart.png")
    plt.close()