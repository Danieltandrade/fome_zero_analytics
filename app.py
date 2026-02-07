"""
Fome Zero Dashboard - Ponto de Entrada da Aplicação

Este módulo serve como o roteador principal (entry point) da aplicação Streamlit.
Ele define a estrutura de navegação usando `st.navigation`, configura o tema
global da página e gerencia o redirecionamento entre as diferentes visões analíticas
(Home, KPIs, Países, Cidades, Culinárias).

Usage:
    Para executar a aplicação, utilize o comando via terminal:
    $ streamlit run app.py

Author: Daniel Torres de Andrade
Date: 2026
"""

import streamlit as st

# Configuração inicial da página (opcional, mas recomendado)
st.set_page_config(page_title="Fome Zero Dashboard", page_icon="📊", layout="wide")

# Definição das Páginas
# O primeiro argumento é o caminho do arquivo, o title é o que aparece no menu
home = st.Page("home.py", title="Home", icon="🏠", default=True)
kpis = st.Page("pages/general_kpis.py", title="General KPIs", icon="📊")
countries = st.Page("pages/countries.py", title="Countries", icon="🌎")
cities = st.Page("pages/cities.py", title="Cities", icon="🏙️")
cuisines = st.Page("pages/cuisines.py", title="Cuisines", icon="🥘")

# Estrutura de Navegação (Você pode agrupar se quiser)
pg = st.navigation({
    "Principal": [home],
    "Análises Detalhadas": [kpis, countries, cities, cuisines]
})

# Rodar a navegação
pg.run()