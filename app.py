import streamlit as st
import pandas as pd
import plotly.express as px
import openpyxl as op
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.title('Métricas :red[DeLeña] y :red[Arracház]')
# orden meses
orden_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
# cargando los datasets
seguidores = pd.read_excel('./datasets/metricas restaurantes.xlsx', sheet_name=0)
ctr = pd.read_excel('./datasets/metricas restaurantes.xlsx', sheet_name=1)
linea = pd.read_excel('./datasets/metricas restaurantes.xlsx', sheet_name=2)
pedidos = pd.read_excel('./datasets/metricas restaurantes.xlsx', sheet_name=4)
incorrectos = pd.read_excel('./datasets/metricas restaurantes.xlsx', sheet_name=5)
rappi = pd.read_excel('./datasets/metricas restaurantes.xlsx', sheet_name=6)
pedidos['mes'] = pd.Categorical(pedidos['mes'], categories=orden_meses, ordered=True)
seguidores_nvo_delena = pd.read_excel('./datasets/seguidores deleña.xlsx', sheet_name=0)
calif = pd.read_excel('./datasets/metricas restaurantes.xlsx', sheet_name=3)
promo_arrachaz = pd.read_excel('./datasets/promociones.xlsx', sheet_name=1)
platillos_arrachaz = pd.read_excel('./datasets/promociones.xlsx', sheet_name=2)
platillos_delena = pd.read_excel('./datasets/promociones.xlsx', sheet_name=0)
historico = pd.read_excel('./datasets/historico.xlsx', sheet_name=0)

metrica = st.radio("Selecciona el indicador:", 
                   ["Redes Sociales", "Plataformas Delivery", "Control Seguimiento", "Histórico"],
                   captions=["Seguidores, Indicadores de Campañas, Comparativas.",
                             "Top Uber Eats.",
                             "Promociones, platillos",
                             "Ventas Mensuales, Comensales"],
                             horizontal=True)

if metrica == "Redes Sociales":
    restaurante = st.radio("Selecciona Restaurante",
                            ["De Leña", "Arracház"],
                            horizontal=True)
    if restaurante == "Arracház":
        st.header("Seguidores :blue[Facebook] & :orange[Instagram] - Arracház")
        # seguidores
        seguidores_arrachaz = seguidores[seguidores['restaurante'] == "Arracház"]
        seguidores_arrachaz_nvo = seguidores_nvo_delena[seguidores_nvo_delena['restaurante'] == "Arracház"]

        followers_fb_arrachaz = seguidores_arrachaz_nvo[seguidores_arrachaz_nvo['red_social'] == 'Facebook']

        fig3ereje = go.Figure()
        # añadir la primera serie de datos
        fig3ereje.add_trace(go.Scatter(x=followers_fb_arrachaz['mes'], 
                                        y=followers_fb_arrachaz['nuevos'],  
                                        mode='lines+text',
                                        text=followers_fb_arrachaz['nuevos'],
                                        textposition='top center',
                                        name='Nuevos Seguidores',
                                        line=dict(color='royalblue',
                                                    dash='dash')))
        fig3ereje.add_trace(go.Scatter(x=followers_fb_arrachaz['mes'],
                                        y=followers_fb_arrachaz['seguidores_totales'],
                                        mode='lines+text',
                                        text=followers_fb_arrachaz['seguidores_totales'],
                                        textposition='top center',
                                        name='Seguidores Acumulados',
                                        yaxis='y2',
                                        line=dict(color='deepskyblue')))
        # configura los ejes
        fig3ereje.update_layout(
            title='Seguidores - Facebook',
            xaxis_title='Seguidores',
            yaxis_title='Nuevos Seguidores',
            yaxis2=dict(
                title='Seguidores Acumulados',
                overlaying='y',
                side='right'
            )
        )
        st.plotly_chart(fig3ereje)
        #seguidores_arrachaz
        # gráfica IG
        followers_ig = seguidores_arrachaz_nvo[seguidores_arrachaz_nvo['red_social'] == 'Instagram']
        # crear la figura con el primer eje y 
        fig4doeje = go.Figure()
        # añadir la primera serie de datos
        fig4doeje.add_trace(go.Scatter(x=followers_ig['mes'], 
                                        y=followers_ig['nuevos'],  
                                        mode='lines+text',
                                        text=followers_ig['nuevos'],
                                        textposition='top center',
                                        name='Nuevos Seguidores',
                                        line=dict(color='salmon',
                                                    dash='dash')))
        fig4doeje.add_trace(go.Scatter(x=followers_ig['mes'],
                                        y=followers_ig['seguidores_totales'],
                                        mode='lines+text',
                                        text=followers_ig['seguidores_totales'],
                                        textposition='top center',
                                        name='Seguidores Acumulados',
                                        yaxis='y2',
                                        line=dict(color='darksalmon')))
        # configura los ejes
        fig4doeje.update_layout(
            title='Seguidores - Instagram',
            xaxis_title='Seguidores',
            yaxis_title='Nuevos Seguidores',
            yaxis2=dict(
                title='Seguidores Acumulados',
                overlaying='y',
                side='right'
            )
        )
        st.plotly_chart(fig4doeje)
        fig2 = px.bar(seguidores_arrachaz, 
                        x='mes', 
                        y='seguidores', 
                        #pattern_shape='red_social', 
                        barmode='group', 
                        color='red_social',
                        color_discrete_sequence=['blue', 'darkmagenta'],
                        text_auto=True,
                        title="Seguidores - Arracház")
        fig2.update_traces(textposition='outside')
        fig2.update_layout(yaxis=dict(showgrid=False),
                                title = dict(
                                        x=0.3,
                                        y=0.9,
                                        font=dict(size=20)))
        st.plotly_chart(fig2)
        st.divider()
        st.header("Indicadores de Campañas: :green[CTR] - Arracház")
        ctr['mes'] = pd.Categorical(ctr['mes'], categories=orden_meses, ordered=True)
        #ctr['ctr'] = ctr['ctr'].apply(lambda x: f"{x:.2%}")
        #ctr
        # gráfico impresiones
        ctr_arrachaz = ctr[ctr['restaurante'] == 'Arracház']
        #ctr_arrachaz
        # gráfica impresiones y clicks arracház
        fig25 = px.bar(ctr_arrachaz,
                        x='mes',
                        y=['impresiones', 'clicks'],
                        barmode='group',
                        text_auto=True,
                        title='Impresiones y Clicks - Arracház',
                        labels={'value': 'Impresiones/Clicks',
                                'mes': 'Mes'})
        fig25.update_layout(yaxis=dict(showgrid=False),
                                title = dict(
                                        x=0.3,
                                        y=0.9,
                                        font=dict(size=20)))
        fig25.update_traces(textposition='outside')
        st.plotly_chart(fig25)
        #orden_meses = ["Julio", "Agosto", "Septiembre", "Octubre", "Noviembre"]
        #ctr['mes'] = pd.Categorical(ctr['mes'], categories=orden_meses, ordered=True)
        fig1 = px.bar(ctr_arrachaz,
                        x='mes',
                        y='ctr',
                        barmode='group',
                        text = ctr_arrachaz['ctr'].apply(lambda p: f"{p:.3f}%"),
                        title='CTR - Arracház',
                        color_discrete_sequence=['mediumseagreen'])
        fig1.update_layout(yaxis=dict(showgrid=False),
                                title = dict(
                                        x=0.3,
                                        y=0.9,
                                        font=dict(size=20)))
        fig1.update_traces(textposition='outside')
        #fig1.update_layout(yaxis=dict(ticksuffix="%"))
        st.plotly_chart(fig1)
        st.divider()
        st.header("Comparativa: :blue[Campaña vs Venta] - Arracház")
    if restaurante == 'De Leña':
        st.header("Seguidores :blue[Facebook] & :orange[Instagram] - De Leña")
        seguidores_delena = seguidores[seguidores['restaurante'] == "DeLeña"]
        #seguidores_delena
        # gráfica seguidores de leña
        # gráfica con eje secundario
        seguidores_delena_nvo = seguidores_nvo_delena[seguidores_nvo_delena['restaurante'] == 'DeLeña']
        followers_fb = seguidores_delena_nvo[seguidores_delena_nvo['red_social'] == 'Facebook']
        # crear la figura con el primer eje y 
        fig1ereje = go.Figure()
        # añadir la primera serie de datos
        fig1ereje.add_trace(go.Scatter(x=followers_fb['mes'], 
                                        y=followers_fb['nuevos'],  
                                        mode='lines+text',
                                        text=followers_fb['nuevos'],
                                        textposition='top center',
                                        name='Nuevos Seguidores',
                                        line=dict(color='royalblue',
                                                    dash='dash')))
        fig1ereje.add_trace(go.Scatter(x=followers_fb['mes'],
                                        y=followers_fb['seguidores_totales'],
                                        mode='lines+text',
                                        text=followers_fb['seguidores_totales'],
                                        textposition='top center',
                                        name='Seguidores Acumulados',
                                        yaxis='y2',
                                        line=dict(color='deepskyblue')))
        # configura los ejes
        fig1ereje.update_layout(
            title='Seguidores - Facebook',
            xaxis_title='Seguidores',
            yaxis_title='Nuevos Seguidores',
            yaxis2=dict(
                title='Seguidores Acumulados',
                overlaying='y',
                side='right'
            )
        )
        st.plotly_chart(fig1ereje)
        followers_ig = seguidores_delena_nvo[seguidores_delena_nvo['red_social'] == 'Instagram']
        # crear la figura con el primer eje y 
        fig2doeje = go.Figure()
        # añadir la primera serie de datos
        fig2doeje.add_trace(go.Scatter(x=followers_ig['mes'], 
                                        y=followers_ig['nuevos'],  
                                        mode='lines+text',
                                        text=followers_ig['nuevos'],
                                        textposition='top center',
                                        name='Nuevos Seguidores',
                                        line=dict(color='salmon',
                                                    dash='dash')))
        fig2doeje.add_trace(go.Scatter(x=followers_ig['mes'],
                                        y=followers_ig['seguidores_totales'],
                                        mode='lines+text',
                                        text=followers_ig['seguidores_totales'],
                                        textposition='top center',
                                        name='Seguidores Acumulados',
                                        yaxis='y2',
                                        line=dict(color='darksalmon')))
        # configura los ejes
        fig2doeje.update_layout(
            title='Seguidores - Instagram',
            xaxis_title='Seguidores',
            yaxis_title='Nuevos Seguidores',
            yaxis2=dict(
                title='Seguidores Acumulados',
                overlaying='y',
                side='right'
            )
        )
        st.plotly_chart(fig2doeje)
        fig26 = px.bar(seguidores_delena, 
                        x='mes', 
                        y='seguidores', 
                        #pattern_shape='red_social', 
                        barmode='group', 
                        color='red_social',
                        color_discrete_sequence=['blue', 'darkmagenta'],
                        text_auto=True,
                        title="Seguidores - De Leña")
        fig26.update_traces(textposition='outside')
        fig26.update_layout(yaxis=dict(showgrid=False),
                                title = dict(
                                        x=0.3,
                                        y=0.9,
                                        font=dict(size=20)))
        st.plotly_chart(fig26)
        st.divider()
        st.header("Indicadores de Campañas: :green[CTR] - De Leña")
        ctr_delena = ctr[ctr['restaurante'] == 'DeLeña']
        ctr_delena['mes'] = pd.Categorical(ctr_delena['mes'], categories=orden_meses, ordered=True)
        fig28 = px.bar(ctr_delena,
                        x='mes',
                        y=['impresiones', 'clicks'],
                        barmode='group',
                        text_auto=True,
                        title='Impresiones y Clicks - Arracház',
                        labels={'value': 'Impresiones/Clicks',
                                'mes': 'Mes'})
        fig28.update_layout(yaxis=dict(showgrid=False),
                                title = dict(
                                        x=0.3,
                                        y=0.9,
                                        font=dict(size=20)))
        fig28.update_traces(textposition='outside')
        st.plotly_chart(fig28)
        # crt de leña
        fig27 = px.bar(ctr_delena,
                        x='mes',
                        y='ctr',
                        barmode='group',
                        text = ctr_delena['ctr'].apply(lambda p: f"{p:.3f}%"),
                        title='CTR - De Leña',
                        color_discrete_sequence=['mediumseagreen'])
        fig27.update_layout(yaxis=dict(showgrid=False),
                                title = dict(
                                        x=0.3,
                                        y=0.9,
                                        font=dict(size=20)))
        fig27.update_traces(textposition='outside')
        #fig1.update_layout(yaxis=dict(ticksuffix="%"))
        st.plotly_chart(fig27)
        st.divider()
        st.header("Comparativa: :blue[Campaña vs Venta] - De Leña")
if metrica == "Plataformas Delivery":
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
                            title="Tasa en Línea - De Leña",
                            text = 'tasa en línea',
                            line_dash='año')
            fig6.update_traces(textposition='top center',
                               )
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
            calif_delena = calif[calif['restaurante'] == 'DeLeña']
            fig29 = px.line(calif_delena,
                            x='mes',
                            y='calificación',
                            color='sucursal',
                            line_shape='spline',
                            markers=True,
                            title='Calificación Promedio 3 Meses',
                            text='calificación')
            fig29.update_traces(textposition='top center')
            fig29.update_layout(title = dict(
                                        x=0.3,
                                        y=0.9,
                                        font=dict(size=20)
                                ),
                                yaxis=dict(showgrid=False))
            st.plotly_chart(fig29)
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
                            line_dash='año',
                            color_discrete_sequence=['indianred', 'orchid', 'palegreen'],
                            text='pedidos')
            fig8.update_traces(textposition='bottom center')
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
                            line_dash='año',
                            color_discrete_sequence=['indianred', 'orchid', 'palegreen'],
                            #line_dash_sequence=['dashdot'],
                            text='ticket promedio')
            #for trace in fig9.data:
                #if trace.name == "Américas, 2024":
                    #trace.text = [f"${v:,.0f}" for v in pedidos_delena[pedidos_delena['sucursal'] == 'Américas']["ticket promedio"]]
                    #trace.textposition = 'top center'
                #elif trace.name == 'Américas, 2023':
                    #trace.text = [f"${v:,.0f}" for v in pedidos_delena[pedidos_delena["sucursal"] == "Américas"]["ticket promedio"]]
                    #trace.textposition = 'bottom center'
            fig9.update_traces(textposition='top center',
                               )
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
                            line_dash='año',
                            color_discrete_sequence=['indianred', 'orchid', 'palegreen'],
                            text='ventas')
            # función para poner unas etiquetas de datos abajo y otras arriba
            for trace in fig10.data:
                if trace.name == "Américas":
                    trace.text = [f"${v:,.0f}" for v in pedidos_delena[pedidos_delena['sucursal'] == 'Américas']["ventas"]]
                    trace.textposition = 'top center'
                elif trace.name == 'Plaza W':
                    trace.text = [f"${v:,.0f}" for v in pedidos_delena[pedidos_delena["sucursal"] == "Plaza W"]["ventas"]]
                    trace.textposition = 'bottom center'
                elif trace.name == 'Altacia':
                    trace.text = [f"${v:,.0f}" for v in pedidos_delena[pedidos_delena["sucursal"] == "Altacia"]["ventas"]]
                    trace.textposition = 'bottom center'
            #fig10.update_traces(text=pedidos_delena['ventas'].apply(lambda x: f"${x:,.0f}"),
                                #textposition='top center')
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
                            title='Pedidos Incorrectos',
                            text='pedidos incorrectos',
                            color_discrete_sequence=['indianred', 'orchid', 'palegreen'],
                            line_dash='año')
            fig11.update_traces(textposition='top center')
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
                            title='Pedidos No Completados',
                            text='no completados',
                            color_discrete_sequence=['indianred', 'orchid', 'palegreen'],
                            line_dash='año')
            fig12.update_traces(textposition='top center')
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
                            markers=True,
                            color_discrete_sequence=['orange', 'orangered'],
                            line_dash='año')
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
                            color_discrete_sequence=['orange', 'orangered'],
                            line_dash='año')
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
                            color_discrete_sequence=['orange', 'orangered'],
                            line_dash='año')
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
                            title='Tasa en Línea - Arracház',
                            color='sucursal',
                            text='tasa en línea',
                            line_dash='año')
            fig13.update_traces(textposition='top center')
            fig13.update_layout(yaxis=dict(showgrid=False),
                                title = dict(
                                    x=0.3,
                                    y=.9,
                                    font=dict(size=20)))
            st.plotly_chart(fig13)
            st.subheader('Calificación', divider=True)
            calif_arrachaz = calif[calif['restaurante'] == 'Arracház']
            fig30 = px.line(calif_arrachaz,
                            x='mes',
                            y='calificación',
                            color='sucursal',
                            line_shape='spline',
                            markers=True,
                            title='Calificación Promedio 3 Meses',
                            text='calificación')
            fig30.update_traces(textposition='top center')
            fig30.update_layout(title = dict(
                                        x=0.3,
                                        y=0.9,
                                        font=dict(size=20)
                                ),
                                yaxis=dict(showgrid=False))
            st.plotly_chart(fig30)
            st.subheader('Pedidos', divider=True)
            pedidos_arrachaz = pedidos[pedidos['restaurante'] == 'Arracház']
            # pedidos_arrachaz
            fig14 = px.line(pedidos_arrachaz,
                            x='mes',
                            y='pedidos',
                            line_shape='spline',
                            markers=True,
                            title='# Pedidos - Arracház',
                            color='sucursal',
                            text='pedidos',
                            line_dash='año')
            fig14.update_traces(textposition='top center')
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
                            color='sucursal',
                            text='ticket promedio',
                            line_dash='año')
            fig16.update_traces(textposition='top center')
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
                            color='sucursal',
                            text='ventas',
                            line_dash='año')
            fig15.update_traces(textposition='top center')
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
                            color='sucursal',
                            text='pedidos incorrectos',
                            line_dash='año')
            fig17.update_traces(textposition='top center')
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
                            text='no completados',
                            line_dash='año')
            fig18.update_traces(textposition='top center')
            fig18.update_layout(yaxis=dict(showgrid=False),
                                title = dict(
                                    x=0.3,
                                    y=.9,
                                    font=dict(size=20)))
            st.plotly_chart(fig18)
        else:
            st.header(':orange[Rappi] Arracház')
            st.subheader('Pedidos', divider=True)
            rappi_arrachaz = rappi[rappi['restaurante'] == 'Arracház']
            #rappi_arrachaz
            # gráfico pedidos arracház rappi
            fig22 = px.line(rappi_arrachaz,
                            x='mes',
                            y='pedidos',
                            line_shape='spline',
                            title='# Pedidos - Arracház',
                            color='sucursal',
                            text='pedidos',
                            color_discrete_sequence=['darkorange'],
                            line_dash='año')
            fig22.update_layout(yaxis=dict(showgrid=False),
                                title = dict(
                                    x=0.3,
                                    y=.9,
                                    font=dict(size=20)))
            fig22.update_traces(textposition='top center')
            st.plotly_chart(fig22)
            st.subheader('Ventas', divider=True)
            # gráfico ticket promedio arrachaz rappi
            fig23 = px.line(rappi_arrachaz,
                            x='mes',
                            y='ticket promedio',
                            line_shape='spline',
                            title='Ticket Promedio - Arracház',
                            color='sucursal',
                            text='ticket promedio',
                            color_discrete_sequence=['darkorange'])
            fig23.update_layout(yaxis=dict(showgrid=False),
                                title=dict(
                                    x=0.3,
                                    y=0.9,
                                    font=dict(size=20)))
            fig23.update_traces(textposition='top center')
            st.plotly_chart(fig23)
            # gráfico ventas por mes arracház rappi
            fig24 = px.line(rappi_arrachaz,
                            x='mes',
                            y='ventas',
                            line_shape='spline',
                            title='Ventas Totales por Mes - Arracház',
                            color='sucursal',
                            text='ventas',
                            color_discrete_sequence=['darkorange'])
            fig24.update_layout(yaxis=dict(showgrid=False),
                                title=dict(
                                    x=0.3,
                                    y=0.9,
                                    font=dict(size=20)))
            fig24.update_traces(textposition='top center')
            st.plotly_chart(fig24)
if metrica == "Control Seguimiento":
    restaurante = st.radio("Selecciona Restaurante",
                            ["De Leña", "Arracház"],
                            horizontal=True)
    if restaurante == 'De Leña':
        st.warning('Promociones De Leña a Marzo 2025')
        # DataFrame platillos DeLeña
        # platillos_delena
        menu_promo_delena = platillos_delena[platillos_delena['GRUPO'] == 'MENU PROMOCIONALES']
        menu_promo_delena = menu_promo_delena.groupby('DESCRIPCION')['CANTIDAD'].sum()
        # DataFrame filtrado por menu promocionales
        # menu_promo_delena
        # gráfico de los menu promocionales
        fig34 = px.line(menu_promo_delena,
                        y='CANTIDAD',
                        markers=True,
                        title='Venta de Menus Promocionales',
                        labels = {'DESCRIPCION' : 'Menu', 'CANTIDAD' : 'Cantidad'},
                        template='plotly_white',
                        line_shape='spline')
        fig34.update_layout(
            hovermode='x unified',
            plot_bgcolor='rgba(0,0,0,0)',
            title_font_size=20,
            xaxis_showgrid=True,
            yaxis_showgrid=True
        )
        # agregando etiquetas de valor
        fig34.update_traces(
            line=dict(width=2.5, color='#4B8BBE',
                      
        ))
        st.plotly_chart(fig34)
        
    if restaurante == 'Arracház':
        st.warning('Promociones Arracház a Marzo 2025')
        # promo_arrachaz
        cupon_altacia = promo_arrachaz[promo_arrachaz['comentariodescuento'] == 'CUPON DE ALTACIA']
        fig31 = px.line(cupon_altacia,
                        x='cierre',
                        y='cantidad',
                        line_group='descripcion',
                        text='descripcion',
                        title='Cupones Canjeados')
        fig31.update_layout(yaxis=dict(showgrid=True),
                                title=dict(
                                    x=0.4,
                                    y=0.9,
                                    font=dict(size=20)),
                            xaxis_showgrid=True)
        fig31.update_traces(textposition='top center')
        st.plotly_chart(fig31)
        st.divider()
        # platillos_arrachaz
        tacos = ['TACO CAMARON CHIMICHURRI', 
                 'TACO DE CAMARON DIABLO',
                 'TACO ENSENADA']
        platillos_arrachaz_cuaresma = platillos_arrachaz[platillos_arrachaz['DESCRIPCION'].str.strip().str.upper().isin(tacos)]
        # platillos_arrachaz_cuaresma
        # ventas de los platillos en promoción
        ventas_totales = platillos_arrachaz_cuaresma['VENTA_TOTAL'].sum()
        #
        tacos_arrachaz = platillos_arrachaz_cuaresma.groupby('DESCRIPCION')['CANTIDAD'].sum()
        # tacos_arrachaz
        fig32 = px.line(tacos_arrachaz,
                        y='CANTIDAD',
                        markers=True,
                        title='Venta de Tacos Promocionales',
                        labels = {'DESCRIPCION' : 'Taco', 'CANTIDAD' : 'Cantidad'},
                        template='plotly_white',
                        line_shape='spline')
        fig32.update_layout(
            hovermode='x unified',
            plot_bgcolor='rgba(0,0,0,0)',
            title_font_size=20,
            xaxis_showgrid=True,
            yaxis_showgrid=True
        )
        # agregando etiquetas de valor
        fig32.update_traces(
            line=dict(width=2.5, color='#4B8BBE',
                      
        ))
        st.plotly_chart(fig32)
        st.write('Ventas Totales por Tacos de Temporada:', ventas_totales)
        menus_promo_arrachaz = platillos_arrachaz[platillos_arrachaz['GRUPO'] == 'MENUS PROMOCIONALES']
        menu_promo_arrachaz = menus_promo_arrachaz.groupby('DESCRIPCION')['CANTIDAD'].sum()
        fig33 = px.line(menu_promo_arrachaz,
                        y='CANTIDAD',
                        markers=True,
                        title='Venta de Menus Ejecutivos',
                        labels = {'DESCRIPCION' : 'Menu', 'CANTIDAD' : 'Cantidad'},
                        template='plotly_white',
                        line_shape='spline')
        fig33.update_layout(
            hovermode='x unified',
            plot_bgcolor='rgba(0,0,0,0)',
            title_font_size=20,
            xaxis_showgrid=True,
            yaxis_showgrid=True
        )
        # agregando etiquetas de valor
        fig33.update_traces(
            line=dict(width=2.5, color='#4B8BBE',
                      
        ))
        st.plotly_chart(fig33)
if metrica == "Histórico":
    restaurante = st.radio("Selecciona Restaurante",
                            ["De Leña", "Arracház"],
                            horizontal=True)
    if restaurante == 'De Leña':
        # historico dataset
        delena_historico = historico[historico['restaurante'] == 'DeLeña']
        
        # delena_historico
        # gráfica prueba
        fig37 = make_subplots(
            rows=4, cols=1,
            subplot_titles=("Altacia", "Acueducto", "Amércias", "Plaza W"),
            vertical_spacing=0.15,
            specs=[
                [{"secondary_y": True}],
                [{"secondary_y": True}],
                [{"secondary_y": True}],
                [{"secondary_y": True}],
            ]
        )
        colores = {
            'Altacia': '#1f77b4',
            'Acueducto': '#2ca02c',
            'Américas': '#ff7f0e',
            'Plaza W': '#d62728'
        }

        # Añadir datos para cada sucursal
        for i, sucursal in enumerate(['Altacia', 'Acueducto', 'Américas', 'Plaza W'], 1):
            df_sucursal = delena_historico[delena_historico['sucursal'] == sucursal]

            fig37.add_trace(
                go.Bar(
                    x=df_sucursal['mes'],
                    y=df_sucursal['comensales'],
                    name=f'Comensales {sucursal}',
                    opacity=0.6,
                    showlegend=False
                ),
                row=i, col=1,
                secondary_y=False
            )

            # Líneas para ticket promedio
            fig37.add_trace(
                go.Scatter(
                    x=df_sucursal['mes'],
                    y=df_sucursal['chequepromedio'],
                    name=f'Ticket {sucursal}',
                    line=dict(color=colores[sucursal], width=2.5),
                    mode='lines+markers',
                    marker=dict(size=8, symbol='diamond')
                ),
                row=i, col=1,
                secondary_y=True
            )

        # Configuración del layout
        fig37.update_layout(
            title_text="Métricas por Sucursal - 2025",
            height=1200,
            hovermode='x unified',
            margin=dict(t=100, b=50),
            legend=dict(
                orientation='h',
                yanchor='bottom',
                y=1.02,
                xanchor='center',
                x=0.5
            )
        )

        # Configurar ejes para cada subgráfico
        for i, sucursal in enumerate(['Altacia', 'Acueducto', 'Américas', 'Plaza W'], 1):
            fig37.update_yaxes(
                title_text="Comensales",
                title_font=dict(color=colores[sucursal]),
                secondary_y=False,
                row=i, col=1
            )
            
            fig37.update_yaxes(
                title_text="Ticket Promedio",
                title_font=dict(color=colores[sucursal]),
                secondary_y=True,
                row=i, col=1
            )

            fig37.update_xaxes(title_text="Mes", row=i, col=1)

        # Añadir anotaciones personalizadas
        fig37.add_annotation(
            text="Datos mensuales por sucursal",
            xref="paper", yref="paper",
            x=0.5, y=1.1,
            showarrow=False,
            font=dict(size=20, color='White')
        )

        # Mostrar en Streamlit
        st.title('Análisis Comparativo - 4 Sucursales')
        st.plotly_chart(fig37, use_container_width=True)
    if restaurante == 'Arracház':
        arrachaz_hist = historico[historico['restaurante'] == 'Arracház']
        arrachaz_hist
        arrachaz_hist_pivot = pd.pivot_table(arrachaz_hist,
                                            values='venta',
                                            index='mes',
                                            columns='sucursal')
        fig36 = px.line(arrachaz_hist_pivot,
                        markers=True,
                        title='Ventas por Mes',
                        template='plotly_white',
                        labels = {'value' : 'Venta', 'mes' : 'Mes'},
                        line_shape='spline')
        st.plotly_chart(fig36)
        # historico