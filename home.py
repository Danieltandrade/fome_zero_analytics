"""
Home Page - Fome Zero Dashboard

Este módulo renderiza a página inicial (Landing Page) do dashboard.
Ele fornece uma visão geral do projeto, instruções de uso para o usuário final,
links úteis e informações de contato da equipe de dados.

Esta página não contém visualizações analíticas pesadas, servindo apenas
como guia de navegação e boas-vindas.
"""

import streamlit as st
from pathlib import Path

from utils.data_cleaning import df_cleaning 


current_dir = Path(__file__).parent

IMAGE_PATH = current_dir / 'images' / 'image1.png'
DATA_PATH = current_dir / 'data' / 'raw' / 'dataset.csv'

def main():
    df = df_cleaning(DATA_PATH, df_clean=True)
    
    # Sidebar apenas com imagem, sem filtros na Home (Filtros globais confundem na Home)
    st.sidebar.image(str(IMAGE_PATH), width=270)
    st.sidebar.markdown("# Fome Zero")
    st.sidebar.markdown("---")
    st.sidebar.write("Powered by Streamlit")

    # --- CORPO DA PÁGINA ---
    st.write("# 🍽️ Fome Zero Dashboard")
    
    st.markdown(
        """
        O **Fome Zero** é uma plataforma de inteligência de dados para o mercado gastronômico. 
        Acompanhe métricas de crescimento, descubra novos restaurantes e analise tendências culinárias.
        """
    )

    st.markdown("---")

    # Usando Colunas para criar "Cartões" de navegação
    st.subheader("📊 Painéis Disponíveis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("**General KPIs**")
        st.markdown("Visão macro do negócio: total de restaurantes, países atendidos e mapa global.")
        
    with col2:
        st.info("**Countries & Cities**")
        st.markdown("Análise geográfica: onde estão os melhores restaurantes e quais cidades têm mais opções.")

    col3, col4 = st.columns(2)

    with col3:
        st.info("**Cuisines**")
        st.markdown("Métricas por tipo de culinária: Italiana, Japonesa, Brasileira e mais.")
        
    with col4:
        st.success("**Dica de Uso**")
        st.markdown("Utilize a barra lateral nas outras páginas para filtrar países e datas.")

    st.markdown("---")
    
    # Rodapé com contato melhorado
    st.markdown("### 📬 Precisa de ajuda?")
    st.markdown(
        """
        Entre em contato com o time de Data Science:
        - **Lead:** Daniel Torres de Andrade
        - **Email:** danieltorresandrade@gmail.com
        - **Links:** [Documentação do Projeto](https://github.com/Danieltandrade/fome_zero_analytics)
        """
    )

if __name__ == "__main__":
    main()
