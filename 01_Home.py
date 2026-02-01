from utils import create_sidebar
from utils import df_cleaning
from pathlib import Path

import streamlit as st

IMAGE_PATH = str(Path.cwd()/'images'/'image1.png')
DATA_PATH = str(Path.cwd()/'data'/'raw'/'dataset.csv')

def main():

    st.set_page_config(
        page_title="Home", 
        page_icon="🏠", 
        layout='wide'
    )

    df = df_cleaning(DATA_PATH, df_clean=True)

    create_sidebar(IMAGE_PATH, df)

    st.markdown("# Fome Zero Dashboard")
    
    st.markdown("## O Melhor lugar para encontrar seu mais novo restaurante favorito!")

    st.markdown("""---""")

    st.markdown("""
        ##### Fome Zero Dashboard foi construído para acompanhar as métricas de crescimento dos Entregadores e Restaurantes.

        ---

        ### Como utilizar esse Fome Zero Dashboard?
        - Visão Empresa:
            - Visão Gerencial: Métricas gerais de comportamento.
            - Visão Tática: Indicadores semanais de crescimento.
            - Visão Geográfica: Insights de geolocalização.
        - Visão Entregadores:
            - Acompanhamento dos indicadores semanais de crescimento.
        - Visão Restaurantes:
            - Indicadores semanais de crescimento dos restaurantes.

        ---

        ### Ask for Help:
            danieltorresandrade@gmail.com
    """)


if __name__ == "__main__":
    main()
