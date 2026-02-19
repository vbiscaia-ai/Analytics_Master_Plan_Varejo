import pandas as pd
import os

# =====================================================
# DEFINIÇÃO DE DIRETÓRIOS
# =====================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RAW_DIR = os.path.join(BASE_DIR, "data", "raw")
STAGING_DIR = os.path.join(BASE_DIR, "data", "staging")

os.makedirs(STAGING_DIR, exist_ok=True)


# =====================================================
# TRANSFORMAÇÃO DIM CUSTOMER
# =====================================================

def transform_dim_customer():

    print("\n========== Iniciando transformação dim_customer ==========")

    file_path = os.path.join(RAW_DIR, "dim_customer_raw.csv")

    df = pd.read_csv(file_path)

    # -------------------------
    # PADRONIZAÇÃO DE COLUNAS
    # -------------------------

    df.columns = df.columns.str.lower().str.strip()

    # -------------------------
    # LIMPEZA DE TEXTOS
    # -------------------------

    colunas_texto = df.select_dtypes(include=["object"]).columns

    for col in colunas_texto:
        df[col] = df[col].str.strip()

    # -------------------------
    # LOG DE NULOS ANTES DO TRATAMENTO
    # -------------------------

    print("\nQuantidade de nulos antes do tratamento:")
    print(df.isnull().sum())

    # =====================================================
    # CUSTOMER ID - GERAR SE NULO
    # =====================================================

    if df["customer_id"].isnull().any():

        max_id = df["customer_id"].dropna().max()

        if pd.isnull(max_id):
            max_id = 0

        novos_ids = range(
            int(max_id) + 1,
            int(max_id) + 1 + df["customer_id"].isnull().sum()
        )

        df.loc[df["customer_id"].isnull(), "customer_id"] = list(novos_ids)

    df["customer_id"] = df["customer_id"].astype(int)

    # =====================================================
    # GENDER - PADRONIZAÇÃO
    # =====================================================

    df["gender"] = df["gender"].str.upper()
    df["gender"] = df["gender"].replace("", None)
    df["gender"] = df["gender"].fillna("Indefinido")

    valores_validos_genero = ["M", "F", "Indefinido"]

    df["gender"] = df["gender"].where(
        df["gender"].isin(valores_validos_genero),
        "Indefinido"
    )

    # =====================================================
    # AGE GROUP - VALIDAÇÃO
    # =====================================================

    faixas_validas = ["18-25", "26-35", "36-50", "50+"]

    df["age_group"] = df["age_group"].where(
        df["age_group"].isin(faixas_validas),
        "Não Informado"
    )

    # =====================================================
    # LOYALTY FLAG - BOOLEAN
    # =====================================================

    df["loyalty_flag"] = df["loyalty_flag"].fillna(0)
    df["loyalty_flag"] = df["loyalty_flag"].astype(int)
    df["loyalty_flag"] = df["loyalty_flag"].astype(bool)

    # =====================================================
    # REMOÇÃO DE DUPLICADOS
    # =====================================================

    before = len(df)
    df = df.drop_duplicates()
    after = len(df)

    print(f"\nDuplicados removidos: {before - after}")

    # -------------------------
    # LOG FINAL DE NULOS
    # -------------------------

    print("\nQuantidade de nulos após tratamento:")
    print(df.isnull().sum())

    # =====================================================
    # EXPORTAÇÃO STAGING
    # =====================================================

    output_path = os.path.join(STAGING_DIR, "dim_customer_stg.csv")
    df.to_csv(output_path, index=False)

    print("\nArquivo salvo em:", output_path)
    print("dim_customer transformado com sucesso!")


# =====================================================
# EXECUÇÃO PRINCIPAL
# =====================================================

if __name__ == "__main__":
    transform_dim_customer()
