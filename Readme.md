


## 📊 Análise Comercial, CRM e Impacto de Campanhas Sazonais

Projeto de Data Analytics com foco em performance comercial, comportamento de consumo e impacto de campanhas sazonais, integrando análise de ticket médio, categorias estratégicas e oportunidades de CRM.

O objetivo central foi transformar dados transacionais em direcionamento estratégico acionável para Marketing, CRM e Planejamento Comercial.

## 🎯 Objetivo do Projeto

Identificar padrões de compra e oportunidades estratégicas para:

Aumentar Ticket Médio

Melhorar conversão em datas sazonais

Otimizar estratégias de CRM

Direcionar investimentos em marketing

Identificar categorias de maior impacto na receita

## 🚀 Visualização do Dashboard
Explore os principais KPIs de Performance, CRM e Portfólio no dashboard interativo.

![Dashboard Preview](./assets/01_print_dashboard.png.png)

🔗 **[Acesse o Dashboard Interativo no Tableau Public](https://public.tableau.com/views/VisoGeraldePerformance/Capa?:language=pt-BR&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)**

## 🏗️ Arquitetura de Dados

O pipeline foi estruturado seguindo o conceito de Multi-hop Architecture (RAW → TRUSTED → GOLD), garantindo rastreabilidade, governança e confiabilidade analítica.

🔄 Processo ETL & Modelagem
1️⃣ RAW — Camada de Dados Brutos

Armazena dados simulando sistemas transacionais (PDV e e-commerce), preservando a integridade original para auditoria.

2️⃣ STAGING / TRUSTED — Camada Tratada

Transformações realizadas via Python (Pandas):

Padronização de textos

Tratamento de valores nulos

Conversão de tipos numéricos

Validação de métricas financeiras

Remoção de inconsistências

3️⃣ GOLD — Camada Analítica

Consolidação das dimensões e fato em uma tabela denormalizada:

sales_complete_clean

Foco em:

Integridade referencial

Padronização financeira

Reprodutibilidade

Performance analítica

## 🛠️ Engenharia de Dados com SQL

A camada analítica foi construída com foco em:

Validação de hipóteses de negócio

Uso de CTEs

Window Functions

Curva ABC de produtos

Segmentação de clientes

Análise de CRM e fidelização

## 🧩 Metodologia Analítica

O projeto foi estruturado em quatro frentes:

1️⃣ Tratamento e Qualidade de Dados

Garantia de consistência antes da análise.

2️⃣ Modelagem de Métricas

Construção de KPIs alinhados ao impacto comercial real.

3️⃣ Segmentação Comportamental

Análise por canal, sazonalidade e fidelização.

4️⃣ Geração de Insights Estratégicos

## Transformação de dados em recomendações acionáveis.

📊 Performance Sazonal — Impacto por Canal
🛍️ E-commerce

Dia das Mães — R$ 408,57 (maior média diária do canal)

Indica forte intenção de compra qualificada no online, especialmente associada a kits e produtos premium.

Black Friday — R$ 285,74 (pior desempenho entre campanhas no canal online)

🏬 Loja Física

Black Friday — R$ 493,76 (maior média diária entre campanhas)

🔎 Gap Estratégico Black Friday

A média diária da Loja Física na Black Friday (R$ 493,76) é aproximadamente:

R$ 208,02 superior ao E-commerce

72,8% acima do desempenho do canal online

O E-commerce performa 42,1% abaixo da loja física

## 🎯 Interpretação Estratégica

Existe um desalinhamento entre estímulo promocional e captura de valor no canal digital.

Enquanto a loja física captura compras de maior valor agregado e comportamento oportunista presencial, o e-commerce apresenta:

Maior fragmentação de compra

Maior sensibilidade a preço

Menor aproveitamento de bundles

Isso representa uma oportunidade clara de otimização estratégica.

## 📲 Estratégia Recomendada — Mensageria para Aumentar Ticket Médio no E-commerce

Dado o gap de 42% entre canais, recomenda-se ativação de mensageria personalizada pré e durante a Black Friday:

1️⃣ WhatsApp / SMS Personalizado

Acesso antecipado exclusivo

Kits recomendados com base no histórico

Benefício progressivo por faixa de valor

2️⃣ Upsell Automatizado

Bundle complementar no carrinho

Frete grátis acima de ticket alvo

Brinde premium para pedidos acima de determinado valor

3️⃣ Segmentação Inteligente

Clientes premium → foco em kits exclusivos

Clientes sensíveis a preço → progressão de desconto

Não fidelizados → incentivo de recompra

Objetivo:

Reduzir o gap entre canais

Aumentar ticket médio digital

Melhorar margem via bundles

Reduzir dependência do canal físico

## 👥 Análise da Base de Clientes

Clientes não fidelizados representam 34,9% da base ativa.

🔎 Implicações Estratégicas

Alta oportunidade de retenção

Potencial aumento de LTV

Redução da dependência de aquisição paga

Espaço para campanhas de reengajamento

## 🎁 Conceito Estratégico: Gift-Giving

Datas como Dia das Mães e Natal seguem padrão de compra emocional:

Maior disposição a pagar

Menor sensibilidade a preço

Busca por kits e embalagens especiais

Compra orientada a presente

## 💄 Performance por Categoria — Skincare

Em 2025:

44,3% da receita total

58,9% concentrada em produtos Classe A

🔎 Interpretação

Forte posicionamento premium

Indício de elasticidade controlada

Potencial de cross-sell e recorrência

## 🔍 Aprendizado Técnico — Controle de Granularidade na Métrica

Durante a construção do dashboard, identifiquei uma inconsistência na métrica de Receita Média Diária por Campanha.

Inicialmente, o cálculo utilizava:

SUM(Receita) / COUNTD(Sale Date)

Ao segmentar por tipo de cliente, o denominador variava conforme os dias em que cada grupo realizou vendas, gerando distorção na comparação.

✅ Correção Aplicada

A métrica foi reestruturada utilizando LOD no Tableau:

{ FIXED [Season] : COUNTD(DATETRUNC('day',[Sale Date])) }

Passando a utilizar:

SUM(Receita) / SUM([Dias Totais da Campanha])

Com isso:

O denominador ficou fixo por campanha

Considerando os dois anos da base

Garantindo comparabilidade real entre segmentos

Esse ajuste reforçou a importância do controle de granularidade na modelagem de KPIs estratégicos.

## 🛠️ Stack Utilizada

Python (ETL e tratamento de dados)

SQL (Modelagem analítica e hipóteses estratégicas)

Tableau (Visualização e Storytelling)

Arquitetura Multi-hop (RAW → TRUSTED → GOLD)

## 🚀 Conclusão

O projeto demonstra como dados transacionais podem ser transformados em direcionamento estratégico real para:

Marketing

CRM

Precificação

Planejamento sazonal

Gestão de portfólio

Mais do que visualizar números, o foco foi construir métricas robustas, comparáveis e acionáveis, com impacto comercial direto.


## 👨‍💻 Autor
**Victor Biscaia**
* [![Linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/victor-biscaia/)
* [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/vbiscaia-ai)

---
*Projeto desenvolvido com visão estratégica voltada para desafios reais de performance no varejo de beleza.*
