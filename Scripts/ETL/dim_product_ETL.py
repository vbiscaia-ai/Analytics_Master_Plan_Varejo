import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RAW_DIR = os.path.join(BASE_DIR, "data", "raw")
STAGING_DIR = os.path.join(BASE_DIR, "data", "staging")

os.makedirs(STAGING_DIR, exist_ok=True)


def transform_dim_product():

    print("\nIniciando transformação dim_product...")

    caminho = os.path.join(RAW_DIR, "dim_product_raw.csv")

    if not os.path.exists(caminho):
        print("Arquivo dim_product_raw.csv não encontrado")
        return

    df = pd.read_csv(caminho)

    # -------------------------
    # PADRONIZAR COLUNAS
    # -------------------------
    df.columns = df.columns.str.lower().str.strip()

    # -------------------------
    # LIMPEZA TEXTO
    # -------------------------
    df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)

    # -------------------------
    # TRATAR NULLS
    # -------------------------
    df["product_name"] = df["product_name"].fillna("Produto Desconhecido")
    df["brand"] = df["brand"].fillna("Marca Desconhecida")
    df["category"] = df["category"].fillna("Não Classificado")
    df["subcategory"] = df["subcategory"].fillna("Sem Subcategoria")

    # =====================================================
    # DOMÍNIO DE NEGÓCIO
    # =====================================================

    dominio_subcategorias = {

        "Perfume": [
            "Floral",
            "Amadeirado",
            "Oriental",
            "Cítrico",
            "Gourmand"
        ],

        "Maquiagem": [
            "Base",
            "Batom",
            "Olhos",
            "Corretivo",
            "Pó Facial"
        ],

        "Skincare": [
            "Limpeza",
            "Hidratação",
            "Anti-idade",
            "Proteção Solar",
            "Tratamento Facial"
        ]
    }

    # =====================================================
    # FUNÇÃO DE MAPEAMENTO
    # =====================================================

    def mapear_subcategoria(row):

        categoria = row["category"]
        sub = row["subcategory"]

        if categoria not in dominio_subcategorias:
            return "Não Classificado"

        lista_subs = dominio_subcategorias[categoria]

        # Converter "Subcat X"
        if isinstance(sub, str) and "Subcat" in sub:

            try:
                numero = int(sub.split(" ")[1]) - 1

                if 0 <= numero < len(lista_subs):
                    return lista_subs[numero]

            except:
                return "Não Classificado"

        # Validar coerência categoria x subcategoria
        if sub not in lista_subs:
            return "Não Classificado"

        return sub


    df["subcategory"] = df.apply(mapear_subcategoria, axis=1)

    # -------------------------
    # PADRONIZAÇÃO FINAL TEXTO
    # -------------------------
    df["product_name"] = df["product_name"].str.title()
    df["brand"] = df["brand"].str.title()
    df["category"] = df["category"].str.title()
    df["subcategory"] = df["subcategory"].str.title()

    # -------------------------
    # VALIDAR PREÇO
    # -------------------------
    df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce")

    # tratar null preço
    df = df[df["unit_price"].notnull()]

    # remover preços inválidos
    df = df[df["unit_price"] > 0]

    # -------------------------
    # REMOVER DUPLICADOS
    # -------------------------
    df = df.drop_duplicates()

    # -------------------------
    # SALVAR STAGING
    # -------------------------
    saida = os.path.join(STAGING_DIR, "dim_product_stg.csv")

    df.to_csv(saida, index=False)

    print("dim_product transformado com sucesso!")
    print(f"Arquivo salvo em: {saida}")


# =========================
# EXECUÇÃO
# =========================

if __name__ == "__main__":
    transform_dim_product()
