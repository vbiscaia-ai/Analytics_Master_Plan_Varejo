/* ==============================================================================
   PROJETO: MASTER PLAN - GRUPO BOTICÁRIO
   ARQUIVO: 01_setup_stg.sql
   DESCRIÇÃO: Criação do ambiente de Staging (Camada Trusted).
   OBJETIVO: Definir a estrutura física das tabelas de Dimensões e Fato 
             para recepção dos dados sintéticos via Python.
   ============================================================================== */

-- 1. Criação do Banco de Dados
CREATE DATABASE IF NOT EXISTS boticario_stg;
USE boticario_stg;

-- 2. Dimensão: Canais de Venda (E-commerce vs Loja Física)
CREATE TABLE IF NOT EXISTS dim_channel_stg (
    channel_id     INT PRIMARY KEY,
    channel_name   VARCHAR(50)
);

-- 3. Dimensão: Clientes e Perfil de Fidelidade (CRM)
CREATE TABLE IF NOT EXISTS dim_customer_stg (
    customer_id    INT PRIMARY KEY,
    gender         VARCHAR(5),
    age_group      VARCHAR(20),
    loyalty_flag   VARCHAR(20) -- Fidelizado, Não Fidelizado, Não Identificado
);

-- 4. Dimensão: Calendário e Sazonalidade
-- Importante para análise de "Vencedores Sazonais" (Dia das Mães, Natal, etc.)
CREATE TABLE IF NOT EXISTS dim_date_stg (
    full_date      DATE PRIMARY KEY,
    date_id        INT,
    day            INT,
    month          INT,
    month_name     VARCHAR(20),
    year           INT,
    quarter        INT,
    day_name       VARCHAR(20),
    week_of_year   INT,
    week_of_month  INT,
    is_weekend     VARCHAR(20),
    is_month_start VARCHAR(20),
    is_month_end   VARCHAR(20),
    year_month     VARCHAR(20),
    quarter_name   VARCHAR(2),
    month_number   INT,
    season         VARCHAR(20) -- Ex: Black Friday, Dia dos Namorados
);

-- 5. Dimensão: Portfólio de Produtos e Categorias
CREATE TABLE IF NOT EXISTS dim_product_stg (
    product_id     INT PRIMARY KEY,
    product_name   VARCHAR(100),
    brand          VARCHAR(100),
    category       VARCHAR(100),
    subcategory    VARCHAR(100),
    unit_price     DECIMAL(10,2) -- Uso de DECIMAL para precisão financeira
);

-- 6. Dimensão: Lojas e Regionalidade (Franchising)
CREATE TABLE IF NOT EXISTS dim_store_stg (
    store_id       INT PRIMARY KEY,
    store_name     VARCHAR(100),
    region         VARCHAR(50),
    state          VARCHAR(10),
    city           VARCHAR(100)
);

-- 7. Tabela Fato: Transações de Vendas
-- Estrutura central para cálculo de Receita, Custo e Margem
CREATE TABLE IF NOT EXISTS fact_sales_stg (
    sale_id         INT PRIMARY KEY,
    sale_date       DATE,
    product_id      INT,
    store_id        INT,
    channel_id      INT,
    customer_id     INT,
    quantity        INT,
    gross_revenue   DECIMAL(10,2),
    discount_value  DECIMAL(10,2),
    net_revenue     DECIMAL(10,2),
    cost            DECIMAL(10,2),
    
    -- Chaves Estrangeiras para Integridade dos Dados
    FOREIGN KEY (sale_date)   REFERENCES dim_date_stg(full_date),
    FOREIGN KEY (product_id)  REFERENCES dim_product_stg(product_id),
    FOREIGN KEY (store_id)    REFERENCES dim_store_stg(store_id),
    FOREIGN KEY (channel_id)  REFERENCES dim_channel_stg(channel_id),
    FOREIGN KEY (customer_id) REFERENCES dim_customer_stg(customer_id)
);

/* Dica Técnica: O uso de PRIMARY KEY e FOREIGN KEY garante que o Star Schema 
não possua dados órfãos, facilitando a manutenção e auditoria do dashboard.
*/