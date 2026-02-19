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
# DIM DATE
# =====================================================

def transform_dim_date():

    print("\nIniciando transformação dim_date...")

    df = pd.read_csv(os.path.join(RAW_DIR, "dim_date_raw.csv"))

    # -------------------------
    # PADRONIZAR COLUNAS
    # -------------------------
    df.columns = df.columns.str.lower().str.strip()

    df["full_date"] = pd.to_datetime(df["full_date"])

    # =====================================================
    # CAMPOS ANALÍTICOS
    # =====================================================

    # Nome do dia
    df["day_name"] = df["full_date"].dt.day_name()

    # Semana do ano
    df["week_of_year"] = df["full_date"].dt.isocalendar().week

    # Semana do mês
    df["week_of_month"] = df["full_date"].dt.day.apply(lambda x: (x - 1) // 7 + 1)

    # Flag fim de semana
    df["is_weekend"] = df["full_date"].dt.weekday >= 5

    # Início / fim do mês
    df["is_month_start"] = df["full_date"].dt.is_month_start
    df["is_month_end"] = df["full_date"].dt.is_month_end

    # Year Month
    df["year_month"] = df["full_date"].dt.strftime("%Y-%m")

    # Quarter nomeado
    df["quarter_name"] = "Q" + df["quarter"].astype(str)

    # Número do mês com padding (evita erro no Tableau)
    df["month_number"] = df["month"].astype(str).str.zfill(2)

    # =====================================================
    # SAZONALIDADE VAREJO
    # =====================================================

    def definir_sazonalidade(row):

        mes = row["month"]

        if mes == 3:
            return "Dia da Mulher"
        elif mes == 5:
            return "Dia das Mães"
        elif mes == 6:
            return "Dia dos Namorados"
        elif mes == 11:
            return "Black Friday"
        elif mes == 12:
            return "Natal"
        else:
            return "Regular"

    df["season"] = df.apply(definir_sazonalidade, axis=1)

    # =====================================================
    # PADRONIZAÇÃO TEXTO
    # =====================================================

    df["month_name"] = df["month_name"].str.title()
    df["day_name"] = df["day_name"].str.title()

    # =====================================================
    # REMOVER DUPLICADOS
    # =====================================================

    df = df.drop_duplicates()

    # =====================================================
    # SALVAR STAGING
    # =====================================================

    df.to_csv(os.path.join(STAGING_DIR, "dim_date_stg.csv"), index=False)

    print("dim_date transformado com sucesso!")


# =====================================================
# ORQUESTRAÇÃO
# =====================================================

def transform_all():

    print("\n========== INICIANDO PIPELINE DIM_DATE ==========")

    transform_dim_date()

    print("\n========== PIPELINE FINALIZADO ==========")


# =====================================================
# EXECUÇÃO PRINCIPAL
# =====================================================

if __name__ == "__main__":
    transform_all()
