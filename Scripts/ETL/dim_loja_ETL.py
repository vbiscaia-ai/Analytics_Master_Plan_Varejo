import pandas as pd
import os
import random

# =========================
# DEFINIÇÃO DAS PASTAS
# =========================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RAW_DIR = os.path.join(BASE_DIR, "data", "raw")
STAGING_DIR = os.path.join(BASE_DIR, "data", "staging")

os.makedirs(STAGING_DIR, exist_ok=True)

# =====================================================
# DIM STORE
# =====================================================

def transform_dim_store():

    print("\nIniciando transformação dim_store...")

    df = pd.read_csv(os.path.join(RAW_DIR, "dim_store_raw.csv"))

    # -------------------------
    # PADRONIZAR COLUNAS
    # -------------------------
    df.columns = df.columns.str.lower().str.strip()

    # -------------------------
    # LIMPEZA DE TEXTO
    # -------------------------
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    # =====================================================
    # DOMÍNIO REGIÃO → ESTADOS
    # =====================================================

    dominio_regioes = {
        "Nordeste": ["BA", "CE", "SE", "PE"],
        "Sudeste": ["SP", "RJ", "MG"],
        "Sul": ["PR", "RS", "SC", "MS"]
    }

    # =====================================================
    # DOMÍNIO ESTADO → CAPITAL
    # =====================================================

    capitais = {
        "BA": "Salvador",
        "CE": "Fortaleza",
        "SE": "Aracaju",
        "PE": "Recife",
        "SP": "São Paulo",
        "RJ": "Rio de Janeiro",
        "MG": "Belo Horizonte",
        "PR": "Curitiba",
        "RS": "Porto Alegre",
        "SC": "Florianópolis",
        "MS": "Campo Grande"
    }

    # =====================================================
    # MAPEAR ESTADO
    # =====================================================

    def mapear_estado(row):

        estado = str(row["state"])
        regiao = row["region"]

        if pd.isnull(row["state"]) or estado.startswith("ST"):
            if regiao in dominio_regioes:
                return random.choice(dominio_regioes[regiao])

        return estado

    df["state"] = df.apply(mapear_estado, axis=1)

    # =====================================================
    # MAPEAR CIDADE
    # =====================================================

    def mapear_cidade(row):

        cidade = str(row["city"])
        estado = row["state"]

        if pd.isnull(row["city"]) or "Cidade" in cidade:
            return capitais.get(estado)

        return cidade

    df["city"] = df.apply(mapear_cidade, axis=1)

    # =====================================================
    # REMOVER LOJAS SEM CIDADE
    # =====================================================

    df = df.dropna(subset=["city"])

    # =====================================================
    # PADRONIZAÇÃO FINAL
    # =====================================================

    df["store_name"] = df["store_name"].str.title()
    df["region"] = df["region"].str.title()
    df["state"] = df["state"].str.upper()
    df["city"] = df["city"].str.title()

    # =====================================================
    # REMOVER DUPLICADOS
    # =====================================================

    df = df.drop_duplicates()

    # =====================================================
    # SALVAR STAGING
    # =====================================================

    df.to_csv(os.path.join(STAGING_DIR, "dim_store_stg.csv"), index=False)

    print("dim_store transformado com sucesso!")


# =====================================================
# ORQUESTRAÇÃO
# =====================================================

def transform_all():

    print("\n========== INICIANDO PIPELINE DIM_STORE ==========")

    transform_dim_store()

    print("\n========== PIPELINE FINALIZADO ==========")


# =====================================================
# EXECUÇÃO PRINCIPAL
# =====================================================

if __name__ == "__main__":
    transform_all()
