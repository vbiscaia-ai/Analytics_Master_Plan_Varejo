Processo ETL
📌 Visão Geral

O processo de ETL (Extract, Transform, Load) foi desenvolvido para simular um pipeline de dados utilizado em ambientes reais de Business Intelligence no varejo.

O pipeline tem como objetivo garantir:

Padronização dos dados

Qualidade e consistência das informações

Aplicação de regras de negócio

Preparação dos dados para consumo analítico

🏗️ Arquitetura do Pipeline

O fluxo de dados segue a seguinte estrutura:

RAW → STAGING → BI

🔹 RAW

Camada responsável por armazenar os dados brutos, simulando extrações de sistemas transacionais e e-commerce.

Características:

Dados sem tratamento

Possibilidade de valores nulos

Inconsistências de formatação

Preservação da estrutura original da fonte

🔹 STAGING

Camada intermediária onde ocorre todo o tratamento e validação dos dados.

Nesta etapa são aplicadas:

Limpezas estruturais

Padronizações textuais

Tratamento de valores nulos

Aplicação de regras de negócio

Enriquecimento analítico

🧩 Extração dos Dados

A extração foi simulada através da leitura de arquivos CSV armazenados na camada RAW.

Principais etapas:

Leitura dos arquivos utilizando Pandas

Normalização dos nomes das colunas

Preparação dos dados para transformação

Exemplo das operações realizadas:

Conversão de colunas para minúsculo

Remoção de espaços em branco

Garantia de consistência estrutural

🔧 Transformações Aplicadas

Cada tabela passou por transformações específicas baseadas em regras de negócio e boas práticas de modelagem dimensional.

👤 Dimensão Customer

Transformações realizadas:

Padronização de textos

Tratamento de valores nulos

Validação de atributos demográficos

Remoção de duplicidades

Garantia de consistência nos identificadores de cliente

Objetivo:

Garantir uma base confiável para análise de comportamento do consumidor.

🛍️ Dimensão Product

Transformações realizadas:

Padronização de nomes de produtos e marcas

Conversão de preços para formato numérico

Exclusão de valores inválidos ou negativos

Mapeamento de subcategorias baseado em domínio de negócio

Validação hierárquica entre categoria e subcategoria

Tratamento de subcategorias não classificadas

Objetivo:

Criar uma estrutura categórica confiável para análise de mix de produtos e performance comercial.

🏬 Dimensão Store

Transformações realizadas:

Padronização de nomes de lojas

Mapeamento de regiões para estados válidos

Associação de estados às respectivas capitais

Exclusão de registros sem localização válida

Padronização de nomenclaturas geográficas

Objetivo:

Permitir análises regionais e geográficas consistentes.

📅 Dimensão Date

Transformações realizadas:

Criação de chaves substitutas baseadas na data

Extração de atributos temporais

Inclusão de indicadores analíticos como:

Nome do mês

Trimestre

Dia da semana

Identificação de finais de semana

Número da semana do ano

Objetivo:

Facilitar análises temporais e identificação de sazonalidades.

💰 Tabela Fato Sales

Transformações realizadas:

Remoção de registros com valores nulos

Validação de métricas financeiras

Garantia de integridade referencial com dimensões

Monitoramento e registro da quantidade de valores descartados

Padronização de tipos numéricos

Objetivo:

Garantir confiabilidade nas métricas utilizadas nos dashboards.

🧪 Qualidade dos Dados

Durante o processo ETL foram implementadas verificações para garantir integridade e consistência dos dados, incluindo:

Validação de tipos de dados

Exclusão de registros inválidos

Monitoramento de valores nulos

Padronização textual

Remoção de duplicidades

⚙️ Orquestração do Pipeline

Todas as transformações são executadas por uma função central responsável por coordenar o fluxo ETL.

Essa função executa as transformações de forma sequencial, garantindo que todas as dimensões e tabelas fato sejam processadas corretamente antes do consumo analítico.

💾 Carregamento dos Dados

Após o tratamento, os dados são exportados para a camada STAGING, onde ficam disponíveis para consumo em ferramentas de Business Intelligence.

Formato de saída:

Arquivos CSV estruturados

Dados prontos para modelagem e visualização

📊 Benefícios do Processo

O pipeline desenvolvido permite:

Simulação de ambiente corporativo real

Melhoria na confiabilidade dos dados

Base estruturada para análises estratégicas

Escalabilidade para inclusão de novas fontes

Durante o desenvolvimento do dashboard no Tableau, foi realizada uma etapa de normalização e padronização das colunas métricas para garantir consistência e confiabilidade nas análises.

Apesar dos dados já estarem estruturados em banco e exportados para CSV, algumas colunas numéricas foram reconhecidas pelo Tableau como texto, o que poderia comprometer cálculos e indicadores. Para resolver esse cenário, foram criados campos calculados aplicando funções de limpeza e conversão de tipo, como TRIM() para remover possíveis espaços ocultos e FLOAT() para garantir o correto tratamento numérico.

Essa abordagem permitiu padronizar métricas como receita, custo e valores financeiros, assegurando que os KPIs fossem calculados corretamente. Além disso, foi feita uma validação criteriosa para identificar quais colunas realmente necessitavam de tratamento, evitando transformações desnecessárias e mantendo a eficiência do modelo analítico.

Esse processo reforça a importância da qualidade e governança dos dados como etapa fundamental antes da construção de visualizações e geração de insights para o negócio.