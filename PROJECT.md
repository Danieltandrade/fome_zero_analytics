# 🍽️ Fome Zero Analytics

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/DanielTorresAndrade)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Python Version](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/)
[![Versão do Projeto](https://img.shields.io/badge/Vers%C3%A3o-1.0-blue?style=for-the-badge)](https://github.com/DanielTorresAndrade)

## 📄 Sobre o Projeto

O **Fome Zero Analytics** é um painel de inteligência de dados desenvolvido para analisar o mercado de restaurantes global. O objetivo principal é simular um cenário corporativo onde um CEO precisa de visibilidade sobre os dados da plataforma para tomar decisões estratégicas.

O projeto processa um conjunto de dados global, realiza a limpeza e tratamento das informações e as apresenta através de um dashboard interativo web, permitindo a exploração de métricas por diferentes perspectivas de negócio: Visão Geral, Países, Cidades e Culinárias.

O dataset original foi obtido no Kaggle e contém informações sobre milhares de restaurantes, incluindo localização, tipos de culinária, custos e avaliações de clientes.

## 🎯 Objetivos

- **Consolidar Métricas:** Fornecer uma visão macro do negócio (KPIs globais).
- **Análise Geográfica:** Identificar oportunidades e comportamentos em diferentes países e cidades.
- **Segmentação Culinária:** Avaliar o desempenho de diferentes tipos de cozinha e identificar nichos de alta performance.
- **Democratização de Dados:** Disponibilizar os dados de forma visual e acessível para times de negócio através de uma aplicação Web.

## 🛠️ Tecnologias e Bibliotecas

- **Python 3.13:** Linguagem base do projeto.
- **Streamlit:** Framework para construção do dashboard interativo e estrutura de navegação (`st.navigation`).
- **Pandas:** Manipulação, limpeza e agregação de dados.
- **Plotly Express:** Criação de gráficos interativos (barras, dispersão, etc).
- **Folium:** Visualização de mapas geoespaciais e clusters de restaurantes.
- **UV:** Gerenciamento moderno e ultrarrápido de dependências e ambientes virtuais.

## 📂 Estrutura do Projeto

A arquitetura do projeto foi organizada para garantir escalabilidade e manutenção, separando a lógica de processamento (`utils`), as interfaces de visualização (`pages`) e os notebooks de exploração.

```bash
project_root
├── app.py                   # Arquivo principal (Entry Point) da aplicação
├── home.py                  # Conteúdo da página inicial (Landing Page)
├── pyproject.toml           # Configuração de dependências (UV)
├── requirements.txt         # Lista de dependências para deploy (PIP)
├── README.md                # Documentação do projeto
├── uv.lock                  # Lockfile para garantir reprodutibilidade
├── data
│   ├── processed            # Dados tratados (opcional)
│   └── raw                  # Dados brutos
├── images
│   └── image1.png           # Assets visuais
├── notebooks                # Análises exploratórias e rascunhos
│   ├── limpeza_dados.ipynb
│   ├── visao_cidade.ipynb
│   ├── visao_culinaria.ipynb
│   ├── visao_geral.ipynb
│   ├── visao_pais.ipynb
│   └── visao_restaurantes.ipynb
├── pages                    # Módulos das páginas do Dashboard
│   ├── cities.py
│   ├── countries.py
│   ├── cuisines.py
│   └── general_kpis.py
└── utils                    # Funções auxiliares e compartilhadas
    ├── __init__.py
    ├── cuisines_data.py     # Lógica específica de culinárias
    ├── data_cleaning.py     # Pipeline de limpeza de dados (ETL)
    └── sidebar.py           # Componentes de UI reutilizáveis
```

## 🚀 Funcionalidades do Dashboard

O painel é dividido em 4 visões principais:

1. **General KPIs:** Visão executiva com totais de restaurantes, países, cidades e um mapa interativo global.
2. **Countries:** Comparativo entre países (quantidade de restaurantes, média de avaliações e custo médio).
3. **Cities:** Ranking das cidades com mais restaurantes, melhores avaliações e diversidade culinária.
4. **Cuisines:** Análise profunda dos tipos de culinária, destacando os melhores restaurantes e categorias.

## ⚙️ Como Executar o Projeto

### Pré-requisitos

- Git
- Python 3.10 ou superior
- Recomendado: [uv](https://github.com/astral-sh/uv) instalado.

### Passo 1: Clone o Repositório

```bash
git clone [https://github.com/Danieltandrade/fome_zero_analytics.git](https://github.com/Danieltandrade/fome_zero_analytics.git)
cd fome_zero_analytics
```

### Passo 2: Instalação e Execução

#### Opção A: Usando UV (Recomendado)

O `uv` gerencia o ambiente virtual e as dependências automaticamente de forma muito mais rápida.

```bash
# Sincroniza as dependências e cria o ambiente virtual
uv sync

# Ativa o ambiente virtual
source .venv/bin/activate  # Linux/Mac
# ou
.venv\Scripts\activate     # Windows

# Executa o dashboard
streamlit run app.py
```

#### Opção B: Usando PIP (Padrão)

```bash
# Crie e ative um ambiente virtual
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# ou
.venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt

# Executa o dashboard
streamlit run app.py
```

## 🧠 Habilidades Demonstradas

- **Engenharia de Dados:** Criação de scripts modularizados em Python e pipelines de limpeza de dados (`utils/data_cleaning.py`).
- **Visualização de Dados:** Uso avançado de Plotly e Folium para transformar dados brutos em insights visuais.
- **Desenvolvimento Web (Low-code):** Domínio do framework Streamlit, incluindo recursos novos como `st.navigation`.
- **Boas Práticas:** Uso de Type Hints, Docstrings, estrutura modular e gerenciamento profissional de dependências.

## 📝 Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.

## 📧 Contato

**Daniel Torres Andrade**
- ✉️ Email: danieltorresandrade@gmail.com
- 💼 LinkedIn: [Seu LinkedIn](https://www.linkedin.com/in/daniel-torres-de-andrade-19a4742b4)
- 🐙 GitHub: [DanielTorresAndrade](https://github.com/DanielTorresAndrade)

---
*Projeto desenvolvido como parte do portfólio de Ciência de Dados.*