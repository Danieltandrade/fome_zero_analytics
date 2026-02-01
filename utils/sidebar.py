"""

"""

import pandas as pd
import streamlit as st
from pathlib import Path

def create_sidebar(image_path: Path, df: pd.DataFrame):
    
    st.sidebar.image(image_path)

    st.sidebar.markdown("""---""")

    st.sidebar.markdown("# Filtros:")

    countries = st.sidebar.multiselect(
        "Escolha os Paises que Deseja visualizar os Restaurantes:",
        df.loc[:, "country_name"].unique().tolist(),
        default=["Brazil", "England", "Qatar", "South Africa", "Canada", "Australia"],
    )

    return countries
