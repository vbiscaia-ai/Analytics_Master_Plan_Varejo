/* ==============================================================================
   PROJETO: MASTER PLAN - GRUPO BOTICÁRIO
   ARQUIVO: 03_business_hypotheses.sql
   DESCRIÇÃO: Validação de Hipóteses de Negócio e Insights Estratégicos.
   OBJETIVO: Responder perguntas críticas sobre CRM, Sazonalidade, 
             Canais e Performance de Produtos.
   ============================================================================== */

USE analytics;

-- ==============================================================================
-- BLOCO 1: PERFORMANCE TEMPORAL E SAZONALIDADE
-- Foco: Identificar picos de demanda e eficácia de campanhas
-- ==============================================================================

-- HIPÓTESE 1: A receita líquida apresenta tendência de crescimento?
SELECT 
    year, 
    month, 
    month_name, 
    SUM(net_revenue) AS receita_liquida
FROM analytics.sales_complete_clean
GROUP BY year, month, month_name
ORDER BY year, month;

-- HIPÓTESE 2: Campanhas sazonais superam o período regular em Ticket Médio?
SELECT
    CASE 
        WHEN season = 'Regular' THEN 'Período Regular'
        ELSE 'Campanha Sazonal'
    END AS tipo_periodo,
    SUM(net_revenue) AS receita_total,
    COUNT(sale_id) AS total_pedidos,
    SUM(net_revenue) / COUNT(sale_id) AS ticket_medio,
    COUNT(DISTINCT customer_id) AS clientes_unicos
FROM analytics.sales_complete_clean
GROUP BY 1;


-- ==============================================================================
-- BLOCO 2: CRM E FIDELIZAÇÃO (LOYALTY)
-- Foco: Entender o comportamento do consumidor e retenção
-- ==============================================================================

-- HIPÓTESE 3: Clientes fidelizados geram maior Ticket Médio?
SELECT
    loyalty_flag,
    AVG(net_revenue) AS ticket_medio,
    COUNT(sale_id) AS frequencia_pedidos
FROM analytics.sales_complete_clean
GROUP BY loyalty_flag
ORDER BY ticket_medio DESC;

-- HIPÓTESE 4: O perfil de consumidor (Idade/Gênero) muda por Região?
SELECT
    region,
    age_group,
    gender,
    SUM(net_revenue) AS receita
FROM analytics.sales_complete_clean
GROUP BY region, age_group, gender
ORDER BY region, receita DESC;


-- ==============================================================================
-- BLOCO 3: PRODUTOS E MARGEM (PROFITABILITY)
-- Foco: Curva ABC e Trade-off entre Volume e Lucro
-- ==============================================================================

-- HIPÓTESE 5: Análise Curva ABC por Subcategoria (80/20)
SELECT 
    subcategory, 
    SUM(net_revenue) AS receita_liquida,
    SUM(profit) AS lucro_total,
    ROUND(SUM(profit) / SUM(net_revenue) * 100, 2) AS margem_percentual
FROM analytics.sales_complete_clean
GROUP BY subcategory
ORDER BY receita_liquida DESC;

-- HIPÓTESE 6: Categorias Premium geram maior margem média?
SELECT
    category,
    AVG(profit) AS margem_media_absoluta,
    SUM(quantity) AS volume_vendido
FROM analytics.sales_complete_clean
GROUP BY category
ORDER BY margem_media_absoluta DESC;


-- ==============================================================================
-- BLOCO 4: CANAIS E EFICIÊNCIA OPERACIONAL
-- Foco: Omnicanalidade e Impacto de Descontos
-- ==============================================================================

-- HIPÓTESE 7: Existe dependência desigual de descontos por Canal?
SELECT 
    channel_name,
    AVG(discount_value) AS desconto_medio,
    SUM(net_revenue) AS receita_total
FROM analytics.sales_complete_clean
GROUP BY channel_name;

-- HIPÓTESE 8: Performance de Lojas Físicas vs E-commerce (Volume x Receita)
SELECT 
    channel_name,
    SUM(net_revenue) AS receita,
    SUM(quantity) AS volume,
    SUM(net_revenue) / SUM(quantity) AS preco_medio_pago
FROM analytics.sales_complete_clean
GROUP BY channel_name;

/* CONCLUSÃO TÉCNICA:
Estas queries validam a robustez do Star Schema e permitem que o Dashboard 
no Tableau reflita insights acionáveis para a gerência de Comunicação e BI.
*/