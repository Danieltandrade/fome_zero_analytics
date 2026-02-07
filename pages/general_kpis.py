"""
Visão Geral e Mapa (General KPIs)

Este módulo apresenta os Indicadores Chave de Desempenho (KPIs) consolidados
da plataforma Fome Zero.

Visualizações Principais:
    - Cartões de métricas globais (Total de Restaurantes, Países, Cidades, Avaliações).
    - Mapa interativo (Folium) com clusterização de restaurantes por geolocalização.
    - Filtros laterais aplicados ao contexto global.
"""

import folium
import pandas as pd
import streamlit as st
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium

from utils.sidebar import create_sidebar
from utils.data_cleaning import df_cleaning
from pathlib import Path

# Criando caminho para os arquivos da app
current_dir = Path(__file__).parent
root_dir = current_dir.parent

IMAGE_PATH = root_dir / 'images' / 'image1.png'
DATA_PATH = root_dir / 'data' / 'raw' / 'dataset.csv'

def create_map(df: pd.DataFrame) -> None:
    """
    Cria um mapa com os restaurantes selecionados por país na sidebar

    Args:
        df (pd.DataFrame): Dataframe com os dados dos restaurantes
    
    Returns:
        None

    Example:
        mapa = create_map(df)
    """

    mapa = folium.Map(
        location=[df['latitude'].mean(), df['longitude'].mean()],
        zoom_start=2,
        max_bounds=True
    )

    marker_cluster = MarkerCluster().add_to(mapa)

    # Preparando dados em lote é mais rápido que acessar o DF linha a linha
    for name, lat, lon, price, curr, cuis, rate, color in zip(
        df['restaurant_name'], df['latitude'], df['longitude'], 
        df['average_cost_for_two'], df['currency'], df['cuisines'], 
        df['aggregate_rating'], df['color_name']
    ):
        html = f"""
            <div style="font-family: sans-serif; width: 200px;">
                <h4 style="margin-bottom:5px;">{name}</h4>
                <b>Preço:</b> {price} {curr} (para dois)<br>
                <b>Culinária:</b> {cuis}<br>
                <b>Avaliação:</b> {rate}/5.0
            </div>
        """
        
        folium.Marker(
            [lat, lon],
            popup=folium.Popup(html, max_width=300),
            icon=folium.Icon(color=color, icon="home", prefix="fa")
        ).add_to(marker_cluster)

    st_folium(mapa, width=1360 , height=700, returned_objects=[])

def main() -> None:
    """
    Função principal da app

    Args:
        None

    Returns:
        None

    Example:
        main()
    """

    st.title("📊 Fome Zero - KPIs Gerais")

    df = df_cleaning(DATA_PATH, df_clean=True)

    selected_countries = create_sidebar(IMAGE_PATH, df)

    st.markdown("""---""")

    st.markdown("## Mapa com os Restaurantes Registrados")

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
