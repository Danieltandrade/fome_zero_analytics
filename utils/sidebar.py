"""

"""

import pandas as pd
import streamlit as st
from pathlib import Path

def create_sidebar(image_path: Path, df: pd.DataFrame):
    
    st.sidebar.image(image_path)

    st.sidebar.markdown("""---""")

    st.sidebar.markdown("# Filtros:")

    countries = st.sidebar.multiselect(
        "Escolha os Paises que Deseja visualizar as Informações:",
        df.loc[:, "country_name"].unique().tolist(),
        default=["Brazil", "England", "Qatar", "South Africa", "Canada", "Australia"],
    )

    return countries

def create_cuisines_sidebar(image_path: Path, df: pd.DataFrame):
    st.sidebar.image(image_path)

    st.sidebar.markdown("""---""")

    st.sidebar.markdown("# Filtros:")

    countries = st.sidebar.multiselect(
        "Escolha os Paises que Deseja visualizar as Informações:",
        df.loc[:, "country_name"].unique().tolist(),
        default=["Brazil", "England", "Qatar", "South Africa", "Canada", "Australia"],
    )

    top_n = st.sidebar.slider(
        "Selecione a quantidade de Restaurantes que deseja visualizar", 1, 20, 10
    )

    cuisines = st.sidebar.multiselect(
        "Escolha os Tipos de Culinária ",
        df.loc[:, "cuisines"].unique().tolist(),
        default=[
            "Home-made",
            "BBQ",
            "Japanese",
            "Brazilian",
            "Arabian",
            "American",
            "Italian",
        ],
    )

    return list(countries), top_n, list(cuisines)