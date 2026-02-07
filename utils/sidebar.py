"""
Módulo de Componentes da Barra Lateral (Sidebar)

Este módulo contém funções reutilizáveis para a construção da barra lateral
do Streamlit. Ele centraliza a lógica de filtros e upload de imagens para garantir
consistência visual e funcional em todas as páginas do dashboard.

Functions:
    create_sidebar(image_path, df): Gera a sidebar padrão com filtro de países.
    create_cuisines_sidebar(image_path, df): Gera sidebar estendida com filtros de culinária e slider.
"""

import streamlit as st
import pandas as pd
from pathlib import Path
from typing import List, Tuple

def create_sidebar(image_path: Path, df: pd.DataFrame) -> List[str]:
    # Centraliza a imagem e usa use_container_width para responsividade
    st.sidebar.image(str(image_path), width=270) 

    st.sidebar.markdown("---")
    st.sidebar.markdown("## Filtros")

    # Pre-seleção mais robusta (garante que os países existem no DF)
    all_countries = df["country_name"].unique().tolist()
    default_countries = ["Brazil", "England", "Qatar", "South Africa", "Canada", "Australia"]
    
    # Interseção para garantir que não dê erro se um país sumir do CSV
    valid_defaults = [c for c in default_countries if c in all_countries]

    countries = st.sidebar.multiselect(
        "Escolha os Países:",
        all_countries,
        default=valid_defaults,
    )

    return list(countries)

def create_cuisines_sidebar(image_path: Path, df: pd.DataFrame) -> Tuple[List[str], int, List[str]]:
    # Reutiliza a lógica visual
    st.sidebar.image(str(image_path), width=270)
    st.sidebar.markdown("---")
    st.sidebar.markdown("## Filtros")

    # Filtro de Países
    all_countries = df["country_name"].unique().tolist()
    default_countries = ["Brazil", "England", "Qatar", "South Africa", "Canada", "Australia"]
    valid_defaults = [c for c in default_countries if c in all_countries]

    countries = st.sidebar.multiselect(
        "Escolha os Países:",
        all_countries,
        default=valid_defaults,
    )

    st.sidebar.markdown("---")

    # Filtro Top N
    top_n = st.sidebar.slider(
        "Quantidade de Restaurantes:", 1, 20, 10
    )

    st.sidebar.markdown("---")

    # Filtro Culinária
    all_cuisines = df["cuisines"].unique().tolist()
    default_cuisines = ["Home-made", "BBQ", "Japanese", "Brazilian", "Arabian", "American", "Italian"]
    valid_cuisines_default = [c for c in default_cuisines if c in all_cuisines]

    cuisines = st.sidebar.multiselect(
        "Escolha os Tipos de Culinária:",
        all_cuisines,
        default=valid_cuisines_default,
    )

    return list(countries), top_n, list(cuisines)
