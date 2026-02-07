"""
Módulo para selecionar os melhores restaurantes por culinaria

Este módulo oferece uma função para selecionar os melhores restaurantes por culinaria
e uma função para exibir os melhores restaurantes por culinaria.

Functions:
    top_cuisines(df): Seleciona os melhores restaurantes por culinaria
    write_metrics(df): Exibe os melhores restaurantes por culinaria
    top_restaurants(df, countries, cuisines, top_n): Seleciona os melhores restaurantes por pais e culinaria
"""

import pandas as pd
import streamlit as st

def top_cuisines(df: pd.DataFrame) -> dict:
    """
    Função para selecionar os melhores restaurantes por culinaria

    Args:
        df (pd.DataFrame): Dataframe com os dados dos restaurantes

    Returns:
        dict: Dicionário com os melhores restaurantes por culinaria

    Example:
        top_cuisines(df)
    """

    target_cuisines = ["Italian", "American", "Arabian", "Japanese", "Brazilian"]
    results = {}
    
    # Seleção de colunas otimizada
    cols = [
        "restaurant_id", "restaurant_name", "country_name", "city",
        "cuisines", "average_cost_for_two", "currency",
        "aggregate_rating"
    ]

    for cuisine in target_cuisines:
        # CORREÇÃO: regex=False para ser mais rápido, case=False para ignorar maiúsculas/minúsculas
        # na=False ignora valores nulos sem dar erro
        lines = df["cuisines"].str.contains(cuisine, case=False, na=False, regex=False)

        if not lines.any():
            continue

        top_rest = (
            df.loc[lines, cols]
            .sort_values(["aggregate_rating", "restaurant_id"], ascending=[False, True])
            .iloc[0]
        )
        
        results[cuisine] = top_rest.to_dict()

    return results

def write_metrics(df: pd.DataFrame) -> None:
    """
    Função para exibir os melhores restaurantes por culinaria

    Args:
        df (pd.DataFrame): Dataframe com os dados dos restaurantes

    Returns:
        None

    Example:
        write_metrics(df)
    """

    data = top_cuisines(df)
    
    # Layout dinâmico: cria colunas baseado em quantas culinárias foram encontradas
    cols = st.columns(len(data))
    
    for col, (cuisine, info) in zip(cols, data.items()):
        with col:
            st.metric(
                label=f'{cuisine}: {info["restaurant_name"]}',
                value=f'{info["aggregate_rating"]}/5.0',
                help=f"""
                País: {info['country_name']}
                Cidade: {info['city']}
                Preço: {info['average_cost_for_two']} ({info['currency']})
                """
            )

def top_restaurants(df, countries, cuisines, top_n) -> pd.DataFrame:
    """
    Função para selecionar os melhores restaurantes por país e culinaria

    Args:
        df (pd.DataFrame): Dataframe com os dados dos restaurantes
        countries (list): Lista de paíseses selecionados na sidebar
        cuisines (list): Lista de culinarias selecionadas na sidebar
        top_n (int): Quantidade de restaurantes a serem selecionados

    Returns:
        pd.DataFrame: Dataframe com os melhores restaurantes
    
    Example:
        top_restaurants(df, countries, cuisines, top_n)
    """

    cols = [
        "restaurant_id",
        "restaurant_name",
        "country_name",
        "city",
        "cuisines",
        "average_cost_for_two",
        "aggregate_rating",
        "votes",
    ]

    lines = (df["cuisines"].isin(cuisines)) & (df["country_name"].isin(countries))

    dataframe = df.loc[lines, cols].sort_values(
        ["aggregate_rating", "restaurant_id"], ascending=[False, True]
    )

    return dataframe.head(top_n)
