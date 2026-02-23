/* ==============================================================================
   PROJETO: MASTER PLAN - GRUPO BOTICÁRIO
   ARQUIVO: 02_data_cleaning_analytics.sql
   DESCRIÇÃO: ETL SQL, Limpeza Avançada e Modelagem Analítica.
   OBJETIVO: Unificar as dimensões (Star Schema) em uma tabela flat otimizada
             e tratar inconsistências de tipos de dados usando REGEXP.
   ============================================================================== */

-- 1. Criação do Schema Analítico (Camada de Consumo)
CREATE SCHEMA IF NOT EXISTS analytics;
USE analytics;

-- 2. Denormalização: Criação da Tabela Flat Unificada
-- Unindo Fato e Dimensões para facilitar o consumo do BI
CREATE TABLE analytics.sales_complete AS
SELECT
    f.sale_id,
    f.sale_date,

    -- Atributos Temporais e Sazonais
    d.year,
    d.month,
    d.month_name,
    d.quarter,
    d.season,
    d.is_weekend,

    -- Atributos de Produto
    p.product_id,
    p.product_name,
    p.brand,
    p.category,
    p.subcategory,

    -- Atributos de Localização (Franchising)
    s.store_id,
    s.store_name,
    s.region,
    s.state,
    s.city,

    -- Atributos de Cliente (CRM)
    c.customer_id,
    c.gender,
    c.age_group,
    c.loyalty_flag,

    -- Atributos de Canal
    ch.channel_id,
    ch.channel_name,

    -- Métricas Brutas
    f.quantity,
    f.gross_revenue,
    f.discount_value,
    f.net_revenue,
    f.cost

FROM boticario_stg.fact_sales_stg f
LEFT JOIN boticario_stg.dim_date_stg d    ON f.sale_date = d.full_date
LEFT JOIN boticario_stg.dim_product_stg p ON f.product_id = p.product_id
LEFT JOIN boticario_stg.dim_store_stg s   ON f.store_id = s.store_id
LEFT JOIN boticario_stg.dim_customer_stg c ON f.customer_id = c.customer_id
LEFT JOIN boticario_stg.dim_channel_stg ch ON f.channel_id = ch.channel_id;

-- 3. Limpeza Avançada e Tipagem (Data Quality)
-- Removendo caracteres especiais e garantindo precisão DECIMAL(12,2) para auditorias.
CREATE TABLE analytics.sales_complete_clean AS
SELECT
    sale_id,
    product_id,
    store_id,
    customer_id,
    channel_id,
    sale_date,
    year,
    month,
    month_name,
    quarter,
    season,
    is_weekend,
    product_name,
    brand,
    category,
    subcategory,
    store_name,
    region,
    state,
    city,
    gender,
    age_group,
    loyalty_flag,
    channel_name,

    -- Tratamento de strings para números inteiros (Quantidade)
    CAST(REGEXP_REPLACE(quantity, '[^0-9]', '') AS SIGNED) AS quantity,

    -- Tratamento de strings para DECIMAL (Financeiro)
    CAST(REGEXP_REPLACE(gross_revenue, '[^0-9.]', '') AS DECIMAL(12,2)) AS gross_revenue,
    CAST(REGEXP_REPLACE(discount_value, '[^0-9.]', '') AS DECIMAL(12,2)) AS discount_value,
    CAST(REGEXP_REPLACE(net_revenue, '[^0-9.]', '') AS DECIMAL(12,2)) AS net_revenue,
    CAST(REGEXP_REPLACE(cost, '[^0-9.]', '') AS DECIMAL(12,2)) AS cost,

    -- Cálculo de Lucro Bruto (Profit)
    CAST(
        REGEXP_REPLACE(net_revenue, '[^0-9.]', '') - 
        REGEXP_REPLACE(cost, '[^0-9.]', '') 
    AS DECIMAL(12,2)) AS profit

FROM analytics.sales_complete;

-- 4. Otimização de Performance (Indexing)
-- Adição de índices para acelerar filtros no Dashboard.
ALTER TABLE analytics.sales_complete_clean
ADD INDEX idx_date (sale_date),
ADD INDEX idx_product (product_id),
ADD INDEX idx_store (store_id),
ADD INDEX idx_customer (customer_id),
ADD INDEX idx_channel (channel_id);

/* Dica Técnica: O uso de REGEXP_REPLACE demonstra domínio de SQL para tratar 
dados que possam vir corrompidos ou com caracteres de moeda das planilhas originais. */