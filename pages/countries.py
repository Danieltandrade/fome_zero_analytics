"""
Análise por Países (Country Analytics)

Este módulo foca na comparação de métricas entre os diferentes países cadastrados
na base de dados.

Objetivos da Análise:
    - Identificar a distribuição de restaurantes e cidades por país.
    - Comparar a média de avaliações (ratings) entre nações.
    - Analisar o custo médio de um prato para duas pessoas em diferentes moedas/países.
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

    st.title("🌎 Fome Zero - Countries")

    st.markdown("""---""")

    df = df_cleaning(DATA_PATH, df_clean=True)

    countries = create_sidebar(IMAGE_PATH, df)

    with st.container(border=True):
        df_rest = (
            df.loc[df["country_name"].isin(countries), ['restaurant_id', 'country_name']]
            .groupby('country_name')
            .count()
            .sort_values(by='restaurant_id', ascending=False)
            .reset_index()
        )

        fig = px.bar(
            df_rest, 
            x='country_name', 
            y='restaurant_id',
            text="restaurant_id",
            title="Quantidade de Restaurantes Registrados por País",
            labels={
                "country_name": "Paises",
                "restaurant_id": "Quantidade de Restaurantes",
            }
        )
        st.plotly_chart(fig, width='stretch')

    with st.container(border=True):
        df_name = (
            df.loc[df["country_name"].isin(countries), ['city', 'country_name']]
            .groupby('country_name')
            .nunique()
            .sort_values(by='city', ascending=False)
            .reset_index()
        )

        fig = px.bar(
            df_name, 
            x='country_name', 
            y='city',
            text="city",
            title="Quantidade de Cidades Registrados por País",
            labels={
                "country_name": "Paises",
                "city": "Quantidade de Cidades",
            }
        )
        st.plotly_chart(fig, width='stretch')

    with st.container():
        col1, col2 = st.columns(2, border=True)

        with col1:
            country_mean_votes = (
                df.loc[df["country_name"].isin(countries), ['country_name', 'votes', 'restaurant_id']]
                .groupby('country_name')
                .agg(mean_votes=('votes', 'mean'), rest_id_min=('restaurant_id', 'min'))
                .sort_values(by=['mean_votes', 'rest_id_min'], ascending=[False, True])
                .reset_index()
            ).head(7)

            fig = px.bar(
                country_mean_votes,
                x="country_name",
                y="mean_votes",
                text_auto=True,
                title="Média de Avaliações feitas por País",
                labels={
                    "country_name": "Paises",
                    "mean_votes": "Quantidade de Avaliações",
                }
            )
            fig.update_traces(texttemplate='%{y:.2f}', textposition='inside')
            st.plotly_chart(fig, width='stretch')

        with col2:
            mean_price = (
                df.loc[df["country_name"].isin(countries), ['country_name', 'average_cost_for_two']]
                .groupby('country_name')
                .mean()
                .sort_values('average_cost_for_two', ascending=False)
                .reset_index()
            ).head(7)

            fig = px.bar(
                mean_price,
                x='country_name',
                y='average_cost_for_two',
                text_auto=True,
                title='Média de Preços de um Prato para Duas Pessoas',
                labels={
                    'country_name': 'Paises',
                    'average_cost_for_two': 'Peço do Prato para Duas Pessoas'
                }
            )
            fig.update_traces(texttemplate='%{y:.2f}')
            st.plotly_chart(fig, width='stretch')

if __name__ == "__main__":
    main()
