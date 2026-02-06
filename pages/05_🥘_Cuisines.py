"""

"""

import os
import sys
import streamlit as st
import plotly.express as px

# Adiciona a raiz do projeto ao sys.path
project_root = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(project_root)

from utils.cuisines_data import write_metrics
from utils.cuisines_data import top_restaurants
from utils.data_cleaning import df_cleaning
from utils.sidebar import create_cuisines_sidebar

from pathlib import Path

current_dir = Path(__file__).parent
root_dir = current_dir.parent        

IMAGE_PATH = root_dir / 'images' / 'image1.png'
DATA_PATH = root_dir / 'data' / 'raw' / 'dataset.csv'

def main():

    st.set_page_config(
        page_title="Cuisines", 
        page_icon="🥘", 
        layout='wide'
    )

    st.title("🥘 Fome Zero - Cuisines")

    st.markdown("""---""")

    df = df_cleaning(DATA_PATH, df_clean=True)

    countries, top_n, cuisines = create_cuisines_sidebar(IMAGE_PATH, df)

    write_metrics(df)

    st.markdown("""---""")

    df_restaurants = top_restaurants(df, countries, cuisines, top_n)

    st.markdown(f"## Top {top_n} Restaurantes")

    st.dataframe(df_restaurants)

    st.markdown('## Melhores e Piores Culinárias!', text_alignment='center')

    col1, col2 = st.columns(2, border=True)

    with col1:

        top_cuisines = (
            df.loc[
                (df["country_name"].isin(countries)) & (df['aggregate_rating'] > 1.7), 
                ['cuisines', 'aggregate_rating', 'restaurant_id']
            ]
            .groupby('cuisines')
            .agg(mean_rating=('aggregate_rating', 'mean'), rest_id_min=('restaurant_id', 'min'))
            .sort_values(by=['mean_rating', 'rest_id_min'], ascending=[False, True])
            .reset_index()
        ).head(top_n)

        fig = px.bar(
            top_cuisines,
            x='cuisines',
            y='mean_rating',
            text='mean_rating',
            text_auto=True,
            title=f"Top {top_n} Melhores Tipos de Culinárias",
            labels={
                'cuisines': 'Tipo de Culinária',
                'mean_rating': 'Média da Avaliação Média',
            }
        )
        fig.update_traces(texttemplate='%{y:.2f}')
        st.plotly_chart(fig, width='stretch')

    with col2:

        worst_cuisines = (
            df.loc[
                (df["country_name"].isin(countries)) & (df['aggregate_rating'] > 1.7), 
                ['cuisines', 'aggregate_rating', 'restaurant_id']
            ]
            .groupby('cuisines')
            .agg(mean_rating=('aggregate_rating', 'mean'), rest_id_min=('restaurant_id', 'min'))
            .sort_values(by=['mean_rating', 'rest_id_min'], ascending=[True, True])
            .reset_index()
        ).head(top_n)

        fig = px.bar(
            worst_cuisines,
            x='cuisines',
            y='mean_rating',
            text='mean_rating',
            text_auto=True,
            title=f"Top {top_n} Piores Tipos de Culinárias",
            labels={
                'cuisines': 'Tipo de Culinária',
                'mean_rating': 'Média da Avaliação Média',
            }
        )
        fig.update_traces(texttemplate='%{y:.2f}')
        st.plotly_chart(fig, width='stretch')
    
    st.markdown("""---""")


if __name__ == "__main__":
    main()
