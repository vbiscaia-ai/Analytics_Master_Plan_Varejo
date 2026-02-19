📊 Master Plan — Performance de Varejo & Comunicação
Diagnóstico de Campanhas, KPIs e Portfólio | SQL • Python • Tableau

Este projeto simula um ecossistema real de dados do setor de beleza e venda direta, com foco em performance comercial, CRM e impacto de comunicações sazonais.

O objetivo é demonstrar domínio técnico e visão de negócio nas frentes de:

Estruturação e modelagem de dados (SQL)

Automação e tratamento de dados (Python)

Análise de KPIs e experimentação (A/B Testing)

Construção de dashboards executivos (Tableau)

Storytelling orientado à decisão

🚀 Objetivo do Projeto

Construir um pipeline analítico completo para:

Diagnosticar a performance comercial

Avaliar impacto de campanhas sazonais

Identificar oportunidades de CRM e fidelização

Apoiar decisões estratégicas com base em dados

Este projeto foi estruturado simulando o contexto de uma grande empresa de varejo com múltiplos canais (lojas físicas, e-commerce e venda direta).

🏗️ Arquitetura de Dados

O pipeline foi estruturado em camadas, seguindo boas práticas de governança e rastreabilidade.

🔄 Camadas do Processo ETL
🟤 RAW (Dados Brutos)

Armazenamento de arquivos CSV extraídos de sistemas transacionais

Preservação do dado original para auditoria

🟡 STAGING / TRUSTED

Tratamento via Python (Pandas):

Padronização de textos

Tratamento de nulos

Conversão de tipos

Validação de métricas financeiras

Exclusão de registros inconsistentes

🔵 BI (Camada Analítica)

Modelagem dimensional (Star Schema)

Criação de chaves substitutas

Normalização adicional via campos calculados no Tableau

Base final otimizada para consumo executivo

🗄️ Modelagem Dimensional

Foi adotado o padrão Star Schema para garantir:

Performance nas consultas

Clareza analítica

Escalabilidade do modelo

📌 Tabelas Fato

fact_sales

📌 Dimensões

dim_product

dim_customer

dim_date

dim_channel

dim_region

🔧 Transformações por Dimensão
🧴 Dimensão Produto

Padronização de nomes

Conversão de preços

Hierarquia Categoria → Subcategoria

Aplicação de Curva ABC (Window Functions)

👤 Dimensão Cliente

Deduplicação

Tratamento de clientes "Não Identificados"

Criação de flag de fidelização (Loyalty)

📅 Dimensão Data

Criação de chave substituta

Atributos temporais (mês, trimestre, dia da semana)

Identificação de sazonalidade

💰 Fato Vendas

Validação de integridade referencial

Monitoramento de descartes

Garantia de métricas financeiras invioláveis (Receita, Custo, Margem)

📊 Principais KPIs Analisados

Receita

Margem

Ticket Médio

Receita por Canal

Receita por Categoria

Receita por Perfil de Cliente

Retenção e Fidelização

Curva ABC de Produtos

Performance por Região

Impacto de Datas Sazonais

📈 Principais Insights Estratégicos
💎 1. Gestão de CRM

Clientes "Não Identificados" representam 32,3% da receita, indicando:

Oportunidade de melhoria na captura de dados

Potencial de aumento de LTV

Prioridade para testes de fidelização

💰 2. Crescimento Sustentado

A performance geral indica:

Crescimento sustentado impulsionado pelo aumento do ticket médio, mantendo margem saudável mesmo com variação no volume de vendas.

🎯 3. Oportunidade de Fidelização

Clientes não fidelizados representam a maior parte da receita

Não identificados têm percentual próximo aos fidelizados

Recomendação estratégica:
Ações de fidelização + melhoria no registro de clientes para aumento de recorrência.

🌸 4. Sazonalidade

Dia das Mães é a principal alavanca de vendas

Ticket elevado no Dia dos Namorados (R$ 608,36 para não identificados)

Indicação clara de oportunidade para:

Campanhas personalizadas

Fluxos de boas-vindas segmentados

🧴 5. Mix de Portfólio

Skincare representa 36,8% da receita

Categoria ideal para estratégias de recorrência e reposição automática

🌎 6. Regionalidade

Sudeste concentra maior maturidade

Potencial de expansão regional via estratégia de canais

🧪 Aplicação de Conceitos Estatísticos
📌 LTV & Retenção

Fidelizados apresentam maior recorrência

LTV utilizado como base para priorização de investimento

⚖️ Teste A/B (Hipótese Simulada)

Hipótese:
Fluxos de boas-vindas personalizados aumentam conversão de clientes não identificados.

Grupo Prioritário:
Clientes com alto ticket sazonal.

Objetivo:
Validar aumento de conversão e retenção via CRM estruturado.

📊 Dashboard Executivo

Construído com foco em:

Poder de síntese

Storytelling orientado à decisão

Material executivo para liderança

Visão consolidada de performance e oportunidades

Estrutura do dashboard:

Visão Geral (KPIs & Receita)

CRM & Fidelização

Sazonalidade & Campanhas

Performance por Categoria

Regionalidade & Canais

🛠️ Tecnologias Utilizadas
Tecnologia	Aplicação
SQL	Modelagem dimensional, Window Functions, Curva ABC, métricas CRM
Python (Pandas)	ETL, limpeza, automações
Tableau	Visualização e Storytelling
Markdown	Documentação e governança
🎯 Competências Demonstradas

✔ Estruturação e cruzamento de dados via SQL
✔ Criação de novas tabelas e modelagem dimensional
✔ Automação de ETL com Python
✔ Aplicação de testes A/B
✔ Construção de dashboards executivos
✔ Storytelling orientado a negócio
✔ Diagnóstico de KPIs e metas
✔ Interface entre áreas (CRM, Marketing, Produto, Comercial)
✔ Abstração de regras de negócio em métricas

🧠 Perfil Profissional Evidenciado

Este projeto demonstra alinhamento com posições de:

Analista de Performance

Business Intelligence

Product Analytics

Data Product Specialist

Brandformance / Marketing Analytics

Com forte foco em:

Autonomia técnica

Capacidade analítica

Comunicação executiva

Influência estratégica

Mentalidade data-driven

📎 Próximos Passos (Evoluções Possíveis)

Implementação de modelo preditivo de churn

Clusterização de clientes (RFM ou K-Means)

Automação de pipeline via Airflow

Integração com BigQuery

Deploy de dashboard em ambiente cloud

👨‍💻 Autor: Victor Biscaia
Linkedin: https://www.linkedin.com/in/victor-biscaia/

Projeto desenvolvido com foco em simulação real de ambiente corporativo de varejo e beleza, demonstrando maturidade técnica e visão estratégica orientada a performance.