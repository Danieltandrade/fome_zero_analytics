"""

"""

import os
import inflection
import pandas as pd
from pathlib import Path


def country_name(country_id: int) -> str:
    """
    Função para converter o código do país no nome do país.

    Args:
        country_id (int): Número que representa do código do país

    Returns:
        str: String com o nome do país.

    Examples:
        print(country_name(30))
        Output: 'Brazil'
    """

    COUNTRIES = {
    1: "India",
    14: "Australia",
    30: "Brazil",
    37: "Canada",
    94: "Indonesia",
    148: "New Zeland",
    162: "Philippines",
    166: "Qatar",
    184: "Singapure",
    189: "South Africa",
    191: "Sri Lanka",
    208: "Turkey",
    214: "United Arab Emirates",
    215: "England",
    216: "United States of America",
    }

    return COUNTRIES[country_id]

def create_price_tye(price_range: int) -> str:
    """
    Função para converter um código no tipo de preço da comida.

    Args:
        price_range (int): Número de 1 a 4 que representa o tipo de preço.

    Returns:
        str: String com o tipo de preço

    Examples:
        print(create_price_tye(2))
        Output: 'normal'
    """
    
    if price_range == 1:
        return "cheap"
    elif price_range == 2:
        return "normal"
    elif price_range == 3:
        return "expensive"
    else:
        return "gourmet"

def color_name(color_code: str) -> str:
    """
    Função para converter o código de cor para nome da cor.

    Args:
        color_code (str): String com o código da cor a ser convertido

    Returns:
        str: String com a cor convertida

    Example:
        print(color_name("FFBA00"))
        Output: 'red'
    """
    COLORS = {
    "3F7E00": "darkgreen",
    "5BA829": "green",
    "9ACD32": "lightgreen",
    "CDD614": "orange",
    "FFBA00": "red",
    "CBCBC8": "darkred",
    "FF7800": "darkred",
    }

    return COLORS[color_code]

def rename_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Função para renomear colunas do Dataframe

    Args:
        df (pd.DataFrame): Dataframe de entrada.

    Returns:
        pd.DataFrame: Dataframe com colunas renomeadas.
    
    Example:
        df_rename = rename_columns(df)
    """

    title = lambda x: inflection.titleize(x)
    snakecase = lambda x: inflection.underscore(x)
    spaces = lambda x: x.replace(" ", "")
    cols_old = list(df.columns)
    cols_old = list(map(title, cols_old))
    cols_old = list(map(spaces, cols_old))
    cols_new = list(map(snakecase, cols_old))
    df.columns = cols_new

    return df

def clean_cuisines_column(df: pd.DataFrame) -> pd.DataFrame:
    """
    Função para limpar e excluir as linhas vazias da coluna 'cuisines'
    Etapas:
        1. Limpeza a padronização dos nomes dos nomes do tipos de cozinhas, 
        pegando apenas o primeiro nome da String
        2. Remoção das linhas vazias

    Args:
        df (pd.DataFrame): Dataframe de entrada contendo a coluna 'cuisines'

    Returns:
        pd.DataFrame: Dataframe com a coluna limpa
    """

    # Pega apenas o primeiro item da lista de culinárias
    df['cuisines'] = df['cuisines'].str.split(',').str[0]

    # Remove as linhas vazias
    df = df.dropna(subset=['cuisines'])

    return df

def clean_rating_text(text: str) -> str | None:
    """
    Função para limpar a coluna 'rating_text' e padronizar suas notas, com nomes
    no idioma Inglês.

    Args:
        text (str): String de entreda com categoria da nota para padronização

    Returns:
        str | None: Retorna o valor padronizado.
    """

    # Criando um dicionário com a tradução/padronização
    mapping = {
        # Categoria: Excellent
        'Excellent': 'Excellent',
        'Excelente': 'Excellent',
        'Eccellente': 'Excellent', # Italiano
        'Vynikajúce': 'Excellent', # Eslovaco
        'Skvělá volba': 'Excellent', # Tcheco (Ótima escolha)
        'Skvělé': 'Excellent',       # Tcheco
        'Wybitnie': 'Excellent',     # Polonês (Excepcional)
        'Harika': 'Excellent',       # Turco (Maravilhoso)
        'Terbaik': 'Excellent',      # Indonésio (O melhor)

        # Categoria: Very Good
        'Very Good': 'Very Good',
        'Muito bom': 'Very Good',
        'Muito Bom': 'Very Good',    # Variação de caixa
        'Bardzo dobrze': 'Very Good',# Polonês
        'Muy Bueno': 'Very Good',    # Espanhol
        'Velmi dobré': 'Very Good',  # Tcheco
        'Veľmi dobré': 'Very Good',  # Eslovaco
        'Çok iyi': 'Very Good',      # Turco
        'Sangat Baik': 'Very Good',  # Indonésio

        # Categoria: Good
        'Good': 'Good',
        'Bueno': 'Good',             # Espanhol
        'Bom': 'Good',               # Português
        'Buono': 'Good',             # Italiano
        'Baik': 'Good',              # Indonésio
        'İyi': 'Good',               # Turco

        # Categoria: Average
        'Average': 'Average',
        'Biasa': 'Average',          # Indonésio (Comum/Médio)

        # Categoria: Poor
        'Poor': 'Poor',

        # Categoria: Not Rated
        'Not rated': 'Not rated'
    }

    # Retorna o valor padronizado.
    # O comando .get(text, text) tenta achar no dicionário;
    # se não achar, mantém o texto original (segurança).
    return mapping.get(text, text)

def df_cleaning(path: Path, df_clean: bool = True) -> pd.DataFrame:

    # 1. Verificação de segurança
    if not os.path.exists(path):
        raise FileNotFoundError(f"Arquivo não encontrado: {path}")

    # Criando Dataframe
    df = pd.read_csv(path)

    if not df_clean:
            return df

    # Elimininando coluna 'Switch to order menu' contento apenas um valor único
    df = df.drop(columns=['Switch to order menu'])

    # Renomeia colunas
    df = rename_columns(df)

    # Criando coluna com nome do país
    df['country_name'] = df['country_code'].apply(lambda x: country_name(x))

    # Criando coluna com código do preço da comida
    df['price_type'] = df['price_range'].apply(lambda x: create_price_tye(x))

    # Criando coluna com nome da cor
    df['color_name'] = df['rating_color'].apply(lambda x: color_name(x))

    # Limpeza e remoção de linhas vazias da coluna 'cuisines'
    df = clean_cuisines_column(df)

    # Renomeado as linhas da coluna 'rating_text' de forma padronizada
    df['rating_text'] = df['rating_text'].apply(clean_rating_text)

    # Tratando outlier presente na coluna 'average_cost_for_two' para o país 'Australian'
    df.loc[df[(df['country_name'] == 'Australia') & (df['average_cost_for_two'] > 250)].index, 'average_cost_for_two'] = 250
    df.reset_index(drop=True)

    return df
