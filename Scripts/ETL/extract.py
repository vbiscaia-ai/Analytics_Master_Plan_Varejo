import pandas as pd
import numpy as np
from datetime import datetime
import random
import os

# -------------------------------
# DEFINE O DIRETÓRIO DO SCRIPT
# -------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def save_csv(df, filename):
    path = os.path.join(BASE_DIR, filename)
    df.to_csv(path, index=False)
    print(f"Arquivo criado em: {path}")

np.random.seed(42)

# ---------- DIM DATE ----------
dates = pd.date_range(start="2024-01-01", end="2025-12-31")
dim_date = pd.DataFrame({"full_date": dates})
dim_date["date_id"] = dim_date["full_date"].dt.strftime("%Y%m%d").astype(int)
dim_date["day"] = dim_date["full_date"].dt.day
dim_date["month"] = dim_date["full_date"].dt.month
dim_date["month_name"] = dim_date["full_date"].dt.month_name()
dim_date["year"] = dim_date["full_date"].dt.year
dim_date["quarter"] = dim_date["full_date"].dt.quarter

save_csv(dim_date, "dim_date_raw.csv")

# ---------- DIM PRODUCT ----------
products = []
brands = ["O Boticário", "Eudora", "Quem Disse Berenice"]
categories = ["Perfume", "Maquiagem", "Skincare"]

for i in range(1, 51):
    products.append({
        "product_id": i,
        "product_name": f"Produto {i}",
        "brand": random.choice(brands),
        "category": random.choice(categories),
        "subcategory": None if i % 7 == 0 else f"Subcat {random.randint(1,5)}",
        "unit_price": round(random.uniform(30, 250), 2)
    })

dim_product = pd.DataFrame(products)
save_csv(dim_product, "dim_product_raw.csv")

# ---------- DIM STORE ----------
stores = []
regions = ["Sudeste", "Sul", "Nordeste"]

for i in range(1, 16):
    stores.append({
        "store_id": i,
        "store_name": f"Loja {i}",
        "region": random.choice(regions),
        "state": None if i % 5 == 0 else f"ST{i}",
        "city": f"Cidade {i}"
    })

dim_store = pd.DataFrame(stores)
save_csv(dim_store, "dim_store_raw.csv")

# ---------- DIM CHANNEL ----------
dim_channel = pd.DataFrame({
    "channel_id": [1, 2],
    "channel_name": ["Loja Física", "E-commerce"]
})

save_csv(dim_channel, "dim_channel_raw.csv")

# ---------- DIM CUSTOMER ----------
customers = []
for i in range(1, 501):
    customers.append({
        "customer_id": i,
        "gender": random.choice(["F", "M", None]),
        "age_group": random.choice(["18-25", "26-35", "36-50", "50+"]),
        "loyalty_flag": random.choice([0, 1])
    })

dim_customer = pd.DataFrame(customers)
save_csv(dim_customer, "dim_customer_raw.csv")

# ---------- FACT SALES ----------
sales = []

for i in range(1, 5001):
    quantity = random.randint(1, 5)
    price = round(random.uniform(30, 250), 2)
    cost = round(price * random.uniform(0.4, 0.7), 2)
    discount = round(random.choice([0, price * 0.1, price * 0.2]), 2)

    sales.append({
        "sale_id": i,
        "sale_date": random.choice(dates),
        "product_id": random.randint(1, 50),
        "store_id": random.randint(1, 15),
        "channel_id": random.randint(1, 2),
        "customer_id": random.randint(1, 500),
        "quantity": quantity,
        "gross_revenue": round(quantity * price, 2),
        "discount_value": discount,
        "net_revenue": round((quantity * price) - discount, 2),
        "cost": round(quantity * cost, 2)
    })

fact_sales = pd.DataFrame(sales)
save_csv(fact_sales, "fact_sales_raw.csv")

print("✅ Todos os arquivos CSV foram gerados com sucesso.")
