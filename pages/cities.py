"""
Análise por Cidades (City Analytics)

Este módulo detalha o comportamento dos restaurantes agrupados por cidade.

Visualizações Principais:
    - Top Cidades com maior volume de restaurantes.
    - Cidades com melhores e piores médias de avaliação.
    - Diversidade culinária por cidade (quantidade de tipos de culinária únicos).
"""

import streamlit as st
import plotly.express as px

from utils.sidebar import create_sidebar
from utils.data_cleaning import df_cleaning
from pathlib import Path


# Como fazer caminhos à prova de falhas:
current_dir = Path(__file__).parent  # Pega a pasta onde ESTE arquivo está (pages/)
root_dir = current_dir.parent        # Pega a pasta pai (raiz do projeto)

IMAGE_PATH = root_dir / 'images' / 'image1.png'
DATA_PATH = root_dir / 'data' / 'raw' / 'dataset.csv'

def main():

    st.title("🏙️ Fome Zero - Cities")

    st.markdown("""---""")

    df = df_cleaning(DATA_PATH, df_clean=True)

    countries = create_sidebar(IMAGE_PATH, df)

    with st.container(border=True):
        df_cities = (
            df.loc[
                df["country_name"].isin(countries),
                ["restaurant_id", "country_name", "city"],
            ]
            .groupby(["country_name", "city"])
            .count()
            .sort_values(["restaurant_id", "city"], ascending=[False, True])
            .reset_index()
        )

        fig = px.bar(
            df_cities.head(20), 
            x='city', 
            y='restaurant_id',
            text='restaurant_id',
            color='country_name',
            title="Top 20 Cidades com mais Restaurantes",
            labels={
                "city": "Cidades",
                "restaurant_id": "Quantidade de Restaurantes",
                'country_name': 'Paises'
            }
        )
        st.plotly_chart(fig, width='stretch')

    with st.container():
        col1, col2 = st.columns(2, border=True)

        with col1:
            select_colums = ['country_name', 'city', 'restaurant_id']
            cities_above_four = (
                df.loc[(df['aggregate_rating'] > 4) & (df["country_name"].isin(countries)), select_colums]
                .groupby(['country_name', 'city'])
                .count()
                .sort_values(by=['restaurant_id', 'city'], ascending=[False, True])
                .reset_index()
            ).head(10)

            fig = px.bar(
                cities_above_four,
                x='city',
                y='restaurant_id',
                text='restaurant_id',
                title='Top 10 Cidades com Restaurantes com \nAvaliação Média Acima de 4',
                color='country_name',
                labels={
                    'city': 'Cidades',
                    'restaurant_id': 'Quantidade de Restaurantes',
                    'country_name': 'Paises'
                }
            )
            st.plotly_chart(fig, width='stretch')

        with col2:
            select_colums = ['country_name', 'city', 'restaurant_id']
            cities_below_two = (df.loc[(df['aggregate_rating'] < 2.5) & (df['country_name'].isin(countries)), select_colums]
                .groupby(['country_name', 'city'])
                .count()
                .sort_values(by=['restaurant_id', 'city'], ascending=[False, True])
                .reset_index()
            ).head(10)

            fig = px.bar(
                cities_below_two,
                x='city',
                y='restaurant_id',
                text='restaurant_id',
                title='Top 10 Cidades com Restaurantes com \nAvaliação Média Abaixo de 2.5',
                color='country_name',
                labels={
                    'city': 'Cidades',
                    'restaurant_id': 'Quantidade de Restaurantes',
                    'country_name': 'Paises'
                }
            )
            st.plotly_chart(fig, width='stretch')

    with st.container(border=True):
        select_colums = ['country_name', 'city', 'cuisines', 'restaurant_id']
        cities_dist_cursines_type = (
            df.loc[df['country_name'].isin(countries), select_colums]
            .groupby(['country_name', 'city'])
            .agg(
                cuisines_nunique=('cuisines', 'nunique'), 
                cuisines_min=('cuisines', 'min'), 
                restaurant_id_nunique=('restaurant_id', 'nunique'), 
                restaurant_id_min=('restaurant_id', 'min')
            ).sort_values(by=['cuisines_nunique', 'restaurant_id_min'], ascending=[False, True])
            .reset_index()
        ).head(20)

        fig = px.bar(
            cities_dist_cursines_type,
            x='city',
            y='cuisines_nunique',
            text='cuisines_nunique',
            title='Top 20 Cidades com Restaurantes com \nCulinárias Distintas',
            color='country_name',
            labels={
                'city': 'Cidades',
                'cuisines_nunique': 'Quantidade de Restaurantes',
                'country_name': 'Paises'
            }
        )
        st.plotly_chart(fig, width='stretch')

if __name__ == "__main__":
    main()
