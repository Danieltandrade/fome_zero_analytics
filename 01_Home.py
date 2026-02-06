from utils import create_sidebar
from utils import df_cleaning
from pathlib import Path

import streamlit as st

IMAGE_PATH = Path.cwd()/'images'/'image1.png'
DATA_PATH = Path.cwd()/'data'/'raw'/'dataset.csv'

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
        ##### Fome Zero Dashboard foi construído para acompanhar as métricas gerais da empresa!

        ---

        ### Como utilizar esse Fome Zero Dashboard?
        - Página General KPIs:
            - Indicadores gerais de Restaurantes, Países, Cidades, Avaliações e Culinárias.
            - Mapa mundial com posicionamento dos restaurantes.
        - Página Countries:
            - Quantidade de Restaurantes Registrados por País.
            - Quantidade de Cidades Registradas por País.
            - Média de Avaliações por Páis.
            - Média de Preços de um Prato para Duas Pessoas por País.
        - Página Cities:
            - Top 20 Cidades com mais Restaurantes.
            - Top 10 Cidades com Avaliação Média Acima de 4.
            - Top 10 Cidades com Avaliação Média Abaixo de 2.5.
            _ Top 20 Cidades com Restaurantes com Culinárias Distintas.
        - Página Cuisines:
            - Indicadores Referentes a Culinária Italiana.
            - Planilha com Dados de Restaurantes.
            - Top Melhores Culinárias.
            - Top Piores Culinárias.

        ### Ask for Help:
            danieltorresandrade@gmail.com
    """)


if __name__ == "__main__":
    main()
