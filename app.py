import streamlit as st
import pandas as pd
import plotly.express as px
import openpyxl as op

st.title('Métricas :red[DeLeña] y :red[Arracház]')

metrica = st.radio("Selecciona el indicador:", 
                   ["Redes Sociales", "*Plataformas Delivery*"],
                   captions=["Seguidores, Indicadores de Campañas, Comparativas.",
                             "Top Uber Eats."],
                             horizontal=True)

if metrica == "Redes Sociales":
    st.header("Seguidores")
    st.divider()
    st.header("Indicadores de Campañas: :green[CTR]")
    ctr = pd.read_excel('./datasets/excel.xlsx', sheet_name='ctr')
    #ctr['ctr'] = ctr['ctr'].apply(lambda x: f"{x:.2%}")
    #ctr
    orden_meses = ["Julio", "Agosto", "Septiembre", "Octubre", "Noviembre"]
    ctr['mes'] = pd.Categorical(ctr['mes'], categories=orden_meses, ordered=True)
    ctr_pivot = pd.pivot_table(ctr,
                               index='mes',
                               columns='restaurante',
                               values='ctr',
                               aggfunc='sum')
    fig1 = px.bar(ctr_pivot, barmode='group')
    fig1.update_traces(textposition='outside')
    fig1.update_layout(yaxis=dict(ticksuffix="%"))
    fig1.update_traces(textposition='outside')
    st.plotly_chart(fig1)
    st.divider()
    st.header("Comparativa: :blue[Campaña vs Venta]")