# 📊 Master Plan — Performance de Varejo & Comunicação
> **Diagnóstico de Campanhas, KPIs e Portfólio | SQL • Python • Tableau**

Este projeto simula um ecossistema analítico completo do setor de varejo de beleza e venda direta, com foco em performance comercial, CRM e impacto de comunicações sazonais. O objetivo é demonstrar maturidade técnica em **Engenharia de Dados** e **Business Intelligence**.

---

## 🚀 Visualização do Dashboard
Explore os principais KPIs de Performance, CRM e Portfólio no dashboard interativo.

![Dashboard Preview](./assets/01_print_dashboard.png)

🔗 **[Acesse o Dashboard Interativo no Tableau Public](https://public.tableau.com/views/VisoGeraldePerformance/Capa?:language=pt-BR&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)**

---

## 🏗️ Arquitetura de Dados
O pipeline foi estruturado seguindo o conceito de **Multi-hop Architecture** (RAW → TRUSTED → GOLD), garantindo governança e confiabilidade analítica.

### 🔄 Fluxo de Processamento (ETL)

* **1️⃣ Camada RAW (Bronze):** Armazena dados brutos sintéticos simulando sistemas transacionais (PDV e e-commerce).
* **2️⃣ Camada TRUSTED (Silver):** Transformações via **Python (Pandas)** para padronização de textos, tratamento de nulos e validação de métricas financeiras.
* **3️⃣ Camada CLEAN (Analytics):** Consolidação em uma **tabela denormalizada (`sales_complete_clean`)** para alta performance no Tableau.

---

## 💾 Engenharia de Dados com SQL
A camada analítica foi construída com foco em integridade referencial e reprodutibilidade.

### 📁 Organização dos Scripts SQL
1.  **`01_setup_stg.sql`**: DDL, Primary/Foreign Keys e precisão decimal para finanças.
2.  **`02_data_cleaning_analytics.sql`**: Limpeza via **Regex** e criação da tabela Gold consolidada.
3.  **`03_business_hypotheses.sql`**: Validação de 10+ hipóteses usando **CTEs**, **Window Functions** e Curva ABC.

---

## 📊 Insights Estratégicos (Diagnóstico)

### 💎 1. Gestão de CRM
* **Insight**: Clientes "Não Identificados" representam **32,3% da receita total**.
* **Estratégia**: Oportunidade crítica de expansão de **LTV** através de programas de fidelização.

### 🌸 2. Sazonalidade
* **Insight**: O **Dia das Mães** lidera em volume, mas o **Dia dos Namorados** entrega o maior ticket médio (**R$ 608,36**).
* **Estratégia**: Segmentação para campanhas de "Gift-Giving" e reativação de clientes sazonais.

### 🧴 3. Portfólio & Margem
* **Insight**: **Skincare** domina com **36,8% da receita**, apresentando a melhor margem média.
* **Estratégia**: Categoria prioritária para modelos de recorrência e reposição automática.

---

## 🛠️ Tecnologias & Ferramentas
| Tecnologia | Aplicação Principal |
| :--- | :--- |
| **SQL Avançado** | Modelagem, Window Functions, Denormalização |
| **Python (Pandas)** | ETL, limpeza de dados e automações |
| **Tableau** | Dashboards executivos e Data Storytelling |
| **Markdown** | Documentação técnica e governança |

---

## 👨‍💻 Autor
**Victor Biscaia**
* [![Linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/victor-biscaia/)
* [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/vbiscaia-ai)

---
*Projeto desenvolvido com visão estratégica voltada para desafios reais de performance no varejo de beleza.*