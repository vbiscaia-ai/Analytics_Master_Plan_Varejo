import pandas as pd
import os

# =========================
# DEFINIÇÃO DAS PASTAS
# =========================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RAW_DIR = os.path.join(BASE_DIR, "data", "raw")
STAGING_DIR = os.path.join(BASE_DIR, "data", "staging")

os.makedirs(STAGING_DIR, exist_ok=True)


# =====================================================
# FACT SALES
# =====================================================

def transform_fact_sales():

    print("\nIniciando transformação fact_sales...")

    df = pd.read_csv(os.path.join(RAW_DIR, "fact_sales_raw.csv"))

    # -------------------------
    # PADRONIZAR COLUNAS
    # -------------------------
    df.columns = df.columns.str.lower().str.strip()

    # -------------------------
    # CONVERTER DATA
    # -------------------------
    df["sale_date"] = pd.to_datetime(df["sale_date"], errors="coerce")

    # =====================================================
    # CONTAGEM DE NULOS
    # =====================================================

    print("\nQuantidade de valores nulos por coluna:")
    print(df.isnull().sum())

    # Total de linhas antes
    linhas_antes = len(df)

    # =====================================================
    # REMOVER LINHAS COM QUALQUER NULO
    # =====================================================

    df = df.dropna()

    # Total de linhas depois
    linhas_depois = len(df)

    print(f"\nLinhas removidas por nulos: {linhas_antes - linhas_depois}")

    # =====================================================
    # VALIDAÇÕES DE NEGÓCIO
    # =====================================================

    # remover valores negativos
    df = df[
        (df["quantity"] > 0) &
        (df["gross_revenue"] >= 0) &
        (df["net_revenue"] >= 0) &
        (df["cost"] >= 0)
    ]

    # remover duplicados
    df = df.drop_duplicates()

    # =====================================================
    # SALVAR STAGING
    # =====================================================

    df.to_csv(os.path.join(STAGING_DIR, "fact_sales_stg.csv"), index=False)

    print("fact_sales transformado com sucesso!")


# =====================================================
# ORQUESTRAÇÃO
# =====================================================

def transform_all():

    print("\n========== INICIANDO PIPELINE FACT ==========")

    transform_fact_sales()

    print("\n========== PIPELINE FINALIZADO ==========")


# =====================================================
# EXECUÇÃO PRINCIPAL
# =====================================================

if __name__ == "__main__":
    transform_all()
