import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
st.title("App")
bnrp = pd.read_csv("banrep.csv")
merge= gpd.read_parquet("resultado_merge.parquet")

bnrp["Fecha"]=pd.to_datetime(bnrp["Fecha"])
tab1, tab2 = st.tabs(["Tab1","Tab2"])
variables = ['Tasa de política monetaria', 'PIB', 'Inflación', 'Tasa Desempleo']
with tab1:
    
    for var in variables:
        fig=plt.figure(figsize=(10, 5))
        sns.lineplot(data=bnrp, x='Fecha', y=var)
        plt.title(f'{var} a lo largo del tiempo')
        plt.xlabel('Fecha')
        plt.ylabel(var)
        plt.grid(True)
        plt.tight_layout()
        st.pyplot(fig)

with tab2:
    fig, ax = plt.subplots(1,1, figsize=(10, 4))
    merge.plot(column="Valor", cmap="winter", legend=True,ax=ax)
    plt.axis('off')

    st.pyplot(fig)