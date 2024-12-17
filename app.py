import streamlit as st
import pandas as pd
import plotly.express as px
import openpyxl as op

st.title('Métricas :red[DeLeña] y :red[Arracház]')
# cargando los datasets
seguidores = pd.read_excel('./datasets/metricas restaurantes.xlsx', sheet_name=0)
linea = pd.read_excel('./datasets/metricas restaurantes.xlsx', sheet_name=2)
pedidos = pd.read_excel('./datasets/metricas restaurantes.xlsx', sheet_name=4)
incorrectos = pd.read_excel('./datasets/metricas restaurantes.xlsx', sheet_name=5)
rappi = pd.read_excel('./datasets/metricas restaurantes.xlsx', sheet_name=6)

metrica = st.radio("Selecciona el indicador:", 
                   ["Redes Sociales", "Plataformas Delivery"],
                   captions=["Seguidores, Indicadores de Campañas, Comparativas.",
                             "Top Uber Eats."],
                             horizontal=True)
orden_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

if metrica == "Redes Sociales":
    st.header("Seguidores :blue[Facebook] & :orange[Instagram]")
    # seguidores
    fig2 = px.bar(seguidores, x='mes', y='seguidores', 
                    pattern_shape='red_social', 
                    barmode='group', 
                    color='restaurante',
                    text_auto=True)
    fig2.update_traces(textposition='outside')
    st.plotly_chart(fig2)
    st.divider()
    st.header("Indicadores de Campañas: :green[CTR]")
    ctr = pd.read_excel('./datasets/metricas restaurantes.xlsx', sheet_name=1)
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
else:
    #st.header("Plataformas Delivery")
    restaurante = st.radio("Selecciona Restaurante",
                            ["De Leña", "Arracház"],
                            horizontal=True)
    if restaurante == "De Leña":
        plataforma = st.radio("Selecciona la plataforma Delivery",
                            ["*UberEats*", "*Rappi*"],
                            horizontal=True)
        if plataforma == "*UberEats*":
            st.header(":green[Uber Eats] De Leña")
            st.subheader('Tasa en Línea', divider=True)
            linea_delena = linea[linea['restaurante'] == 'DeLeña']
            # linea_delena
            # gráfico de tasa en línea De Leña
            fig6 = px.line(linea_delena,
                            x='mes',
                            y='tasa en línea',
                            color='sucursal',
                            line_shape='spline',
                            markers=True,
                            range_y=[0.93, 1.01],
                            title="Tasa en Línea - De Leña")
            fig6.update_layout(yaxis=dict(showgrid=False),
                                title = dict(
                                        x=0.3,
                                        y=0.9,
                                        font=dict(size=20)
                                ))
            st.plotly_chart(fig6)
           # gráfico de tiempo sin conexión De Leña
            fig7 = px.line(linea_delena,
                            x='mes',
                            y='sin conexión',
                            line_shape='spline',
                            color='sucursal')
            #st.plotly_chart(fig7)
            st.subheader('Calificación', divider=True)
            st.subheader('Pedidos', divider=True)
            pedidos_delena = pedidos[pedidos['restaurante'] == 'DeLeña']
            # pedidos_delena
            # gráfica de # pedidos DeLeña
            fig8 = px.line(pedidos_delena,
                            x='mes',
                            y='pedidos',
                            color='sucursal',
                            line_shape='spline',
                            markers=True,
                            title='# Pedidos en Ubear Eats - De Leña',
                            line_group='año',
                            color_discrete_sequence=['aqua', 'teal'])
            fig8.update_layout(title = dict(
                                        x=0.3,
                                        y=0.9,
                                        font=dict(size=20)
                                ),
                                yaxis=dict(showgrid=False))
            st.plotly_chart(fig8)
            pedidos_pivot = pd.pivot_table(pedidos,
                                            values='pedidos',
                                            index='mes',
                                            columns='sucursal',
                                            aggfunc='sum')
            pedidos_pivot = pedidos_pivot.reindex(orden_meses)
            # pedidos_pivot
            # gráficas acumuladas diferentes estilos
            #fig4 = px.bar(pedidos_pivot, barmode='group')
            #fig5 = px.bar(pedidos,
                        #x='mes',
                        #y='pedidos',
                        #color='restaurante',
                        #barmode='group',
                        #pattern_shape='sucursal')
            #st.plotly_chart(fig4)
            #st.plotly_chart(fig5)
            st.subheader('Ventas', divider=True)
            # gráfico de ticket promedio
            fig9 = px.line(pedidos_delena,
                            x='mes',
                            y='ticket promedio',
                            color='sucursal',
                            line_shape='spline',
                            markers=True,
                            title='Ticket Promedio',
                            line_group='año',
                            color_discrete_sequence=['aqua', 'teal'],
                            line_dash_sequence=['longdashdot'])
            fig9.update_layout(yaxis=dict(showgrid=False),
                                title = dict(
                                    x=0.3,
                                    y=.9,
                                    font=dict(size=20)))
            st.plotly_chart(fig9)
            # gráfico ventas totales de leña
            fig10 = px.line(pedidos_delena,
                            x='mes',
                            y='ventas',
                            color='sucursal',
                            line_shape='spline',
                            markers=True,
                            title='Ventas por Mes - De Leña',
                            line_group='año',
                            color_discrete_sequence=['white', 'gray'])
            fig10.update_layout(yaxis=dict(showgrid=False),
                                title = dict(
                                    x=0.3,
                                    y=.9,
                                    font=dict(size=20)))
            st.plotly_chart(fig10)
            st.subheader('Incorrectos y/o Perdidos', divider=True)
            incorrectos_deleña = incorrectos[incorrectos['restaurante'] == 'De Leña']
            # incorrectos_deleña
            # gráficos de pedidos incorrectos
            fig11 = px.line(incorrectos_deleña,
                            x='mes',
                            y='pedidos incorrectos',
                            color='sucursal',
                            line_shape='spline',
                            markers=True,
                            title='Pedidos Incorrectos')
            fig11.update_layout(yaxis=dict(showgrid=False),
                                title = dict(
                                    x=0.3,
                                    y=.9,
                                    font=dict(size=20)))
            st.plotly_chart(fig11)
            # gráfico de pedidos no completados
            fig12 = px.line(incorrectos_deleña,
                            x='mes',
                            y='no completados',
                            color='sucursal',
                            line_shape='spline',
                            markers=True,
                            title='Pedidos No Completados')
            fig12.update_layout(yaxis=dict(showgrid=False),
                                title = dict(
                                    x=0.3,
                                    y=.9,
                                    font=dict(size=20)))
            st.plotly_chart(fig12)
        else:
            st.header(':orange[Rappi] DeLeña')
            rappi_delena = rappi[rappi['restaurante'] == 'DeLeña']
            #rappi_delena
            st.header('Pedidos', divider=True)
            # gráfica número pedidos deleña rappi
            fig19 = px.line(rappi_delena,
                            x='mes',
                            y='pedidos',
                            line_shape='spline',
                            color='sucursal',
                            title='Número de Pedidos - De Leña',
                            markers=True)
            fig19.update_layout(yaxis=dict(showgrid=False),
                                title = dict(
                                    x=0.3,
                                    y=.9,
                                    font=dict(size=20)))
            st.plotly_chart(fig19)
            st.header('Ventas', divider=True)
            # gráfica ticket promedio deleña rappi
            fig21 = px.line(rappi_delena,
                            x='mes',
                            y='ticket promedio',
                            line_shape='spline',
                            color='sucursal',
                            title='Ticket Premedio - De Leña',
                            markers=True,
                            color_discrete_sequence=['white', 'yellow'])
            fig21.update_layout(yaxis=dict(showgrid=False),
                                title = dict(
                                    x=0.3,
                                    y=.9,
                                    font=dict(size=20)))
            st.plotly_chart(fig21)
            # ventas totales por mes deleña rappi
            fig20 = px.line(rappi_delena,
                            x='mes',
                            y='ventas',
                            line_shape='spline',
                            color='sucursal',
                            title='Ventas por Mes - De Leña',
                            markers=True,
                            color_discrete_sequence=['white', 'yellow'])
            fig20.update_layout(yaxis=dict(showgrid=False),
                                title = dict(
                                    x=0.3,
                                    y=.9,
                                    font=dict(size=20)))
            st.plotly_chart(fig20)
    else:
        plataforma = st.radio("Selecciona la plataforma Delivery",
                            ["*UberEats*", "*Rappi*"],
                            horizontal=True)
        if plataforma == '*UberEats*':
            st.header(":green[Uber Eats] Arracház")
            st.subheader('Tasa en Línea', divider=True)
            linea_arrachaz = linea[linea['restaurante'] == 'Arracház']
            # linea_arrachaz
            fig13 = px.line(linea_arrachaz,
                            x='mes',
                            y='tasa en línea',
                            line_shape='spline',
                            markers=True,
                            title='Tasa en Línea - Arrachaz',
                            color='sucursal')
            fig13.update_layout(yaxis=dict(showgrid=False),
                                title = dict(
                                    x=0.3,
                                    y=.9,
                                    font=dict(size=20)))
            st.plotly_chart(fig13)
            st.subheader('Calificación', divider=True)
            st.subheader('Pedidos', divider=True)
            pedidos_arrachaz = pedidos[pedidos['restaurante'] == 'Arracház']
            # pedidos_arrachaz
            fig14 = px.line(pedidos_arrachaz,
                            x='mes',
                            y='pedidos',
                            line_shape='spline',
                            markers=True,
                            title='# Pedidos - Arracház',
                            color='sucursal')
            fig14.update_layout(yaxis=dict(showgrid=False),
                                title = dict(
                                    x=0.3,
                                    y=.9,
                                    font=dict(size=20)))
            st.plotly_chart(fig14)
            st.subheader('Ventas', divider=True)
            # gráfica ticket promedio arracház
            fig16 = px.line(pedidos_arrachaz,
                            x='mes',
                            y='ticket promedio',
                            line_shape='spline',
                            markers=True,
                            title='Ticket Promedio - Arracház',
                            color='sucursal')
            fig16.update_layout(yaxis=dict(showgrid=False),
                                title = dict(
                                    x=0.3,
                                    y=.9,
                                    font=dict(size=20)))
            st.plotly_chart(fig16)
            # ventas por mes arracház
            fig15 = px.line(pedidos_arrachaz,
                            x='mes',
                            y='ventas',
                            line_shape='spline',
                            markers=True,
                            title='Ventas Totales por Mes',
                            color='sucursal')
            fig15.update_layout(yaxis=dict(showgrid=False),
                                title = dict(
                                    x=0.3,
                                    y=.9,
                                    font=dict(size=20)))
            st.plotly_chart(fig15)
            st.subheader('Incorrectos y/o Perdidos', divider=True)
            incorrectos_arrachaz = incorrectos[incorrectos['restaurante'] == 'Arracház']
            # incorrectos_arrachaz
            fig17 = px.line(incorrectos_arrachaz,
                            x='mes',
                            y='pedidos incorrectos',
                            line_shape='spline',
                            markers=True,
                            title='# Pedidos Incorrectos - Arracház',
                            color='sucursal')
            fig17.update_layout(yaxis=dict(showgrid=False),
                                title = dict(
                                    x=0.3,
                                    y=.9,
                                    font=dict(size=20)))
            st.plotly_chart(fig17)
            # gráfica pedidos no completados
            fig18 = px.line(incorrectos_arrachaz,
                            x='mes',
                            y='no completados',
                            line_shape='spline',
                            markers=True,
                            title='# Pedidos No Completados - Arracház',
                            color='sucursal',
                            text='no completados')
            fig18.update_layout(yaxis=dict(showgrid=False),
                                title = dict(
                                    x=0.3,
                                    y=.9,
                                    font=dict(size=20)))
            st.plotly_chart(fig18)
        else:
            st.header('Rappi Arracház')