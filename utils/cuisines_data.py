
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

def top_cuisines(df: pd.DataFrame):

    target_cuisines = ["Italian", "American", "Arabian", "Japanese", "Brazilian"]

    results = {}

    cols = [
        "restaurant_id", "restaurant_name", "country_name", "city",
        "cuisines", "average_cost_for_two", "currency",
        "aggregate_rating", "votes"
    ]

    for cuisine in target_cuisines:
        # Nota: Cuidado aqui. df["cuisines"] == key busca correspondência EXATA.
        # Se o restaurante tiver "Italian, Pizza", essa lógica vai ignorá-lo.
        lines = df["cuisines"] == cuisine

        # Verifica se encontrou algo para evitar erro no iloc[0]
        if not lines.any():
            continue

        results[cuisine] = (
            df.loc[lines, cols]
            .sort_values(["aggregate_rating", "restaurant_id"], ascending=[False, True])
            .iloc[0] # iloc[0] já retorna uma Series, não precisa de [:, :]
            .to_dict()
        )

    return results

def write_metrics(df: pd.DataFrame):

    cuisines = top_cuisines(df)

    italian, american, arabian, japonese, brazilian = st.columns(len(cuisines))

    with italian:
        st.metric(
            label=f'Italiana: {cuisines["Italian"]["restaurant_name"]}',
            value=f'{cuisines["Italian"]["aggregate_rating"]}/5.0',
            help=f"""
            País: {cuisines["Italian"]['country_name']}\n
            Cidade: {cuisines["Italian"]['city']}\n
            Média Prato para dois: {cuisines["Italian"]['average_cost_for_two']} ({cuisines["Italian"]['currency']})
            """,
        )

    with american:
        st.metric(
            label=f'Italiana: {cuisines["American"]["restaurant_name"]}',
            value=f'{cuisines["American"]["aggregate_rating"]}/5.0',
            help=f"""
            País: {cuisines["American"]['country_name']}\n
            Cidade: {cuisines["American"]['city']}\n
            Média Prato para dois: {cuisines["American"]['average_cost_for_two']} ({cuisines["American"]['currency']})
            """,
        )

    with arabian:
        st.metric(
            label=f'Italiana: {cuisines["Arabian"]["restaurant_name"]}',
            value=f'{cuisines["Arabian"]["aggregate_rating"]}/5.0',
            help=f"""
            País: {cuisines["Arabian"]['country_name']}\n
            Cidade: {cuisines["Arabian"]['city']}\n
            Média Prato para dois: {cuisines["Arabian"]['average_cost_for_two']} ({cuisines["Arabian"]['currency']})
            """,
        )

    with japonese:
        st.metric(
            label=f'Italiana: {cuisines["Japanese"]["restaurant_name"]}',
            value=f'{cuisines["Japanese"]["aggregate_rating"]}/5.0',
            help=f"""
            País: {cuisines["Japanese"]['country_name']}\n
            Cidade: {cuisines["Japanese"]['city']}\n
            Média Prato para dois: {cuisines["Japanese"]['average_cost_for_two']} ({cuisines["Japanese"]['currency']})
            """,
        )

    with brazilian:
        st.metric(
            label=f'Italiana: {cuisines["Brazilian"]["restaurant_name"]}',
            value=f'{cuisines["Brazilian"]["aggregate_rating"]}/5.0',
            help=f"""
            País: {cuisines["Brazilian"]['country_name']}\n
            Cidade: {cuisines["Brazilian"]['city']}\n
            Média Prato para dois: {cuisines["Brazilian"]['average_cost_for_two']} ({cuisines["Brazilian"]['currency']})
            """,
        )

    return None

def top_restaurants(df, countries, cuisines, top_n):
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
