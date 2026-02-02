"""
Docstring for pages.02_Dados_Gerais
"""
import folium
import os
import sys
import streamlit as st
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium

# Adiciona a raiz do projeto ao sys.path
project_root = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(project_root)

from utils.sidebar import create_sidebar
from utils.data_cleaning import df_cleaning
from pathlib import Path


# Como fazer caminhos à prova de falhas:
current_dir = Path(__file__).parent  # Pega a pasta onde ESTE arquivo está (pages/)
root_dir = current_dir.parent        # Pega a pasta pai (raiz do projeto)

IMAGE_PATH = root_dir / 'images' / 'image1.png'
DATA_PATH = root_dir / 'data' / 'raw' / 'dataset.csv'

def create_map(df):

    # MUDANÇA 2: Removemos 'folium.Figure'. O st_folium gerencia o tamanho melhor.
    mapa = folium.Map(max_bounds=True)

    marker_cluster = MarkerCluster().add_to(mapa)

    for _, line in df.iterrows():
        name = line["restaurant_name"]
        price_for_two = line["average_cost_for_two"]
        cuisine = line["cuisines"]
        currency = line["currency"]
        rating = line["aggregate_rating"]
        color = f'{line["color_name"]}'

        # MUDANÇA 3: Melhoria na formatação do HTML (f-strings diretas são mais limpas)
        html = f"""
            <p><strong>{name}</strong></p>
            <p>Price: {price_for_two},00 ({currency}) para dois<br />
            Type: {cuisine}<br />
            Aggregate Rating: {rating}/5.0</p>
        """

        popup = folium.Popup(
            folium.Html(html, script=True),
            max_width=500,
        )

        folium.Marker(
            [line["latitude"], line["longitude"]],
            popup=popup,
            icon=folium.Icon(color=color, icon="home", prefix="fa"),
        ).add_to(marker_cluster)

    st_folium(
        mapa, 
        width=1360,   # Você pode ajustar ou usar 'use_container_width=True' se preferir
        height=760,
        returned_objects=[] # CRUCIAL para performance
    )

def main():

    st.set_page_config(
        page_title="General KPIs", 
        page_icon="📊", 
        layout='wide'
    )

    st.title("📊 Fome Zero - KPIs Gerais")

    df = df_cleaning(DATA_PATH, df_clean=True)

    #selected_countries = create_sidebar(df)
    selected_countries = create_sidebar(IMAGE_PATH, df)

    with st.container():
        col1, col2, col3, col4, col5 = st.columns(5, border=True)

        col1.metric('Restaurantes Cadastrados:', df['restaurant_id'].nunique())
        col2.metric('Países Cadastrados:', df['country_name'].nunique())
        col3.metric('Cidades Cadastradas:', df['city'].nunique())
        col4.metric('Avaliações Feitas na Plataforma:', f"{df['votes'].sum():,}".replace(",", "."))
        col5.metric('Tidpos de Culinárias Oferecidas:', df['cuisines'].nunique())

    with st.container():
        # Filtro de segurança: Se a lista de países estiver vazia, não tenta plotar
        if selected_countries:
            map_df = df.loc[df["country_name"].isin(selected_countries), :]
            create_map(map_df)
        else:
            st.warning("Selecione pelo menos um país na barra lateral para visualizar o mapa.")

if __name__ == "__main__":
    main()
