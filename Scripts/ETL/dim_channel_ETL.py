import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RAW_DIR = os.path.join(BASE_DIR, "data", "raw")
STAGING_DIR = os.path.join(BASE_DIR, "data", "staging")

os.makedirs(STAGING_DIR, exist_ok=True)

def transform_dim_channel():

    print("Iniciando transformação dim_channel...")

    df = pd.read_csv(os.path.join(RAW_DIR, "dim_channel_raw.csv"))

    print("Quantidade de nulos:")
    print(df.isnull().sum())

    df["channel_name"] = df["channel_name"].fillna("Desconhecido")
    df["channel_name"] = df["channel_name"].replace("", "Desconhecido")

    df = df.dropna(subset=["channel_id"])

    df["channel_id"] = df["channel_id"].astype(int)

    print("Nulos após tratamento:")
    print(df.isnull().sum())

    df.to_csv(os.path.join(STAGING_DIR, "dim_channel_stg.csv"), index=False)

    print("dim_channel transformado com sucesso!")
