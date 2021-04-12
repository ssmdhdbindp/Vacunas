import dash
import matplotlib.pyplot as plt 
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.io as pio
import numpy as np
import dash_table
import sidetable as stb
import datetime
from datetime import datetime, timedelta
from datetime import date
import geopandas as gpd
import flask
import os

yesterday = datetime.now() - timedelta(1)
yea = datetime.strftime(yesterday, '%Y%m%d')

today = date.today()
d2 = today.strftime("Fecha de actualización : %d-%m-%Y")

###############################
# DATABASES
############################### AHre archivos

vacunas = pd.read_csv("https://raw.githubusercontent.com/fdealbam/Vacunas/main/vacunasreport.csv", encoding= "Latin-1")
vacunas.rename(columns={'Farmac�utica': 'Farmaceutica' },inplace=True,
                                   errors='ignore')


# Dtypes 
vacunas['Cantidad']=vacunas['Cantidad'].astype(int)
# convert the 'Date' column to datetime format
format = '%d/%m/%Y'
vacunas['Fecha'] = pd.to_datetime(vacunas['Fecha'], format=format)
vacunas.info()


#--------------------------------------------------------------------------------Dias
vvacunas = vacunas.groupby(by=["Fecha","Farmacéutica"])["Cantidad"].sum()
other_b = pd.DataFrame(vvacunas)
other_b.to_csv('0000procesodi.csv')
vuelve_a_abrir = pd.read_csv('0000procesodi.csv')
format = '%Y-%m-%d'
vuelve_a_abrir['Fecha'] = pd.to_datetime(vuelve_a_abrir['Fecha'], format=format)


#vacunas.info()
filtrado = vuelve_a_abrir.sort_values('Fecha',ascending=False).head(5)
#filtrado.Fecha = today.strftime("%d-%m-%Y")
#Identificadores dias
#dia_1 = filtrado.iloc[4]['dia']
#dia_2 = filtrado.iloc[3]['dia']
#dia_3 = filtrado.iloc[2]['dia']
#dia_4 = filtrado.iloc[1]['dia']
#dia_5 = filtrado.iloc[0]['dia']
##Identificadores Fechas
Fecha_1 = filtrado.iloc[4]['Fecha']
Fecha_2 = filtrado.iloc[3]['Fecha']
Fecha_3 = filtrado.iloc[2]['Fecha']
Fecha_4 = filtrado.iloc[1]['Fecha']
Fecha_5 = filtrado.iloc[0]['Fecha']
#Identificadores Cantidad
cantidad_1 = filtrado.iloc[4]['Cantidad']
cantidad_2 = filtrado.iloc[3]['Cantidad']
cantidad_3 = filtrado.iloc[2]['Cantidad']
cantidad_4 = filtrado.iloc[1]['Cantidad']
cantidad_5 = filtrado.iloc[0]['Cantidad']
#Identificadores Farmaceutica s
farmaceutica_1 = filtrado.iloc[4]['Farmacéutica']
farmaceutica_2 = filtrado.iloc[3]['Farmacéutica']
farmaceutica_3 = filtrado.iloc[2]['Farmacéutica']
farmaceutica_4 = filtrado.iloc[1]['Farmacéutica']
farmaceutica_5 = filtrado.iloc[0]['Farmacéutica']
#-------------------------------------------------Tabla dias
table_header69 = [
    html.Thead(html.Tr(" "))
]

row01 = html.Tr([html.Td([str(f"{cantidad_1:,d}")]), html.Td([str(f"{cantidad_2:,d}")]), 
                 html.Td([str(f"{cantidad_3:,d}")]), html.Td([str(f"{cantidad_4:,d}")]), 
                 html.Td([str(f"{cantidad_1:,d}")])])
row02 = html.Tr([html.Td(farmaceutica_1), html.Td(farmaceutica_2), html.Td(farmaceutica_3), 
                html.Td(farmaceutica_4), html.Td(farmaceutica_5)])

table_body69 = [html.Tbody([row01, row02, #row3, row4
                         ])]

table = dbc.Table(table_header69 + table_body69, bordered=True)
#-------------------------------------------------------------
tabla2 = vacunas.groupby(by=["Farmacéutica"])["Cantidad"].sum()
patabal2 = pd.DataFrame(tabla2)
patabal2.to_csv('0000procesodi.csv')
patabla2 = pd.read_csv('0000procesodi.csv')
#Total Cantidad
tot_vac = patabla2.Cantidad.sum()
#Identificadores Farmaceuticas
farm_tot1 = patabla2.iloc[0]['Farmacéutica']
farm_tot2 = patabla2.iloc[1]['Farmacéutica']
farm_tot3 = patabla2.iloc[2]['Farmacéutica']
farm_tot4 = patabla2.iloc[3]['Farmacéutica']
#Identificadores Cantidad
cant_tot1 = patabla2.iloc[0]['Cantidad']
cant_tot2 = patabla2.iloc[1]['Cantidad']
cant_tot3 = patabla2.iloc[2]['Cantidad']
cant_tot4 = patabla2.iloc[3]['Cantidad']
# tabla2
table_header = [
    html.Thead(html.Tr([html.Th(), html.Th()]))] 
row1 = html.Tr([html.Td(farm_tot1), html.Td([str(f"{cant_tot1:,d}")])])
row2 = html.Tr([html.Td(farm_tot2), html.Td([str(f"{cant_tot2:,d}")])])
row3 = html.Tr([html.Td(farm_tot3), html.Td([str(f"{cant_tot3:,d}")])])
row4 = html.Tr([html.Td(farm_tot4), html.Td([str(f"{cant_tot4:,d}")])])
table_body = [html.Tbody([row1, row2, row3, row4])]
#---------------------------------------------------------------------GRAFICA
#figvac = px.bar(vacunas, x= 'Fecha', y='Cantidad',
#                color='Arribo', 
#                 barmode="overlay",  
#                
#                color_continuous_scale=px.colors.sequential.Inferno
#               )
#
#figvac.update_layout( showlegend=True,
#    width= 1200,
#    height=700,
#   # xaxis_tickangle=-45,
#   # xaxis_tickfont_size= 18,
#    #legend=dict(orientation="h",
#     #          yanchor= "top",
#      #         y=0.99,
#               #xanchor="center",
#       #        x=0.01 ),
#    paper_bgcolor='rgba(0,0,0,0)',
#    plot_bgcolor='rgba(0,0,0,0)',
#
#                     
#)
#figvac.update_yaxes(automargin=False)
  
#igvac = go.Figure()
#igvac.add_trace(go.Bar(x=vacunas['Fecha'],y=vacunas['Cantidad'],
#               marker_color='indianred'  # cambiar nuemeritos de rgb
#               ))
#igvac.update_layout(
#   paper_bgcolor='rgba(0,0,0,0)',
#   plot_bgcolor='rgba(0,0,0,0)',
#   xaxis_tickangle=-45,
#   template = 'simple_white',
#   title='',
#   xaxis_tickfont_size= 12,
#   yaxis=dict(
#       title='Acumulados mensuales',
#       titlefont_size=14,
#       tickfont_size=12,
#       titlefont_family= "Monserrat"),
#   #autosize=False,
#   #width=1000,
#   #height=400
#   )




figvac = go.Figure()
figvac.add_trace(go.Bar(x=vacunas['Fecha'],y=vacunas['Cantidad'],
                marker_color= "chocolate",  # cambiar nuemeritos de rgb
                ))
figvac.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis_tickangle=-45,
    
    template = 'simple_white',
    title='',
    xaxis_tickfont_size= 12,
    yaxis=dict(
        #title='Acumulados mensuales',
        titlefont_size=14,
        tickfont_size=12,
        titlefont_family= "Monserrat"),
    autosize=True,
    #width=1000,
    #height=400
    )



#figvac = go.Figure()
#figvac = px.bar(vacunas, x="Fecha", y="Cantidad", 
#                 color="Arribo", )
#figvac.update_layout(
#    paper_bgcolor='rgba(0,0,0,0)',
#    plot_bgcolor='rgba(0,0,0,0)',)




#Suma semana
tot_sem = filtrado.Cantidad.sum()


server = flask.Flask(__name__)
app = dash.Dash(__name__, external_stylesheets=[dbc.themes. LUX], server=server)

body = html.Div([ 
      
    
        dbc.Row(
            [
           
           dbc.Col(dbc.CardImg(src="https://github.com/fdealbam/Vacunas/blob/main/SRE.JPG?raw=true?raw=true"),
                        width={'size': 1,  "offset": 1 }),
            dbc.Col(html.H5("Secretaría de Relaciones Exteriores, "
                            "Subsecretaría para Asuntos Multilaterales y "
                            "Derechos Humanos"),
                  width={'size': 3, 'offset' : 0}), 
        ],justify="start"),
  
    html.Hr(),
    dbc.Row([
        dbc.Col(html.H1('¿Cuántas vacunas han llegado a México?',
                        className='card-title',style={'textAlign': 'center'} ),
                style={"color": "black", 'text-transform': "uppercase", 
                       "font-weight": 'bolder', "font-stretch": "condensed",
                      "font-size": "x-large" },
                width={ "offset":2 },
                 ),
    ]),
    #html.Hr(style={'borderWidth': "0.3vh", "width": "25%", "color": "#1B5244"}),
    dbc.Row(
           [dbc.Col(html.H6(d2),           #Fecha de actualización
               width={'size' : "auto",
                      'offset' : 5}), 
           ]),
        
    html.Hr(),
    html.Hr(),
    html.Hr(),
    html.Hr(),
    html.Hr(),
    html.Hr(),
    dbc.Row([
        dbc.Col(html.H2('Dosis según farmacéutica',
                        className='card-title',style={'textAlign': 'start'} ),
                style={"color": "#91210C", },
                width={ "offset":1 },),

                
                
    ]),
    #html.Hr(style={'borderWidth': "0.3vh", "width": "25%", "color": "#1B5244"}),
       dbc.Row(
           [
               dbc.Col(html.H5(["Hasta el 9 de abril, nuestro país ha recibido o envasado  ", 
                                str(f"{tot_vac:,d} dosis de vacunas contra COVID-19 listas para aplicarse: "),
                               ],style={'textAlign': 'left'}),
                       width={'size': 6,  "offset":1 },
                      )],justify="start"),
    dbc.Row(
        [
            dbc.Col(dbc.Table(table_header + table_body, 
                              bordered=False, 
                              dark=False,
                              hover=True,
                              #responsive=True,
                              striped=True,
                              size="sm",
                              #style_header={'backgroundColor': 'rgb(30, 30, 30)'},
                              style={
            'margin-top': '9px',
            'margin-left': '130px',
            'width': '509px',
            'height': '46px',
             "font-size": "large"                      
            #'backgroundColor': 'rgba(0,0,0,0)',
            }
                                     ))
        ],justify="center"),
    html.Hr(),
    html.Hr(),
    html.Hr(),
     html.Hr(),
    html.Hr(),
    #html.Hr(style={'borderWidth': "0.3vh", "width": "25%", "color": "#1B5244"}),
    dbc.Row([
        dbc.Col(html.H2('Arribos recientes ',
                        className='card-title',style={'textAlign': 'left'} ),
                style={"color": "#91210C", },
                width={ "offset":1 },
                 ),
    ]),

      dbc.Row(
           [

               dbc.Col(html.H5(["Entre el 1 y el 9 de abril, nuestro país recibió  ", 
                                str(f"{tot_sem:,d} dosis, listas para aplicarse: "),
                               ],style={'textAlign': 'left'}),
                       width={'size': 6,  "offset":1 },
                      )],justify="align"),
   

   dbc.Row([
        dbc.Col(html.H4([" ",dbc.Badge((Fecha_1.strftime('%d-%B-%y')), className="ml-1",color="light",),
                             dbc.Badge((Fecha_2.strftime('%d-%B-%y')), className="ml-1",color="light",),
                             dbc.Badge((Fecha_3.strftime('%d-%B-%y')), className="ml-1",color="light",),
                             dbc.Badge((Fecha_4.strftime('%d-%B-%y')), className="ml-1",color="light",),
                             dbc.Badge((Fecha_5.strftime('%d-%B-%y')), className="ml-1",color="light",),   
                        ]),
                width={'size': 11,  "offset":3 })]),
    dbc.Row(
        [
            dbc.Col(dbc.Table(table_header69 + table_body69, 
                              bordered=False, 
                              size="sm",
                              style={ #'size': 11,"offset":2,
           'margin-top': '0px',
           'margin-left': '400px',
           'width': '609px',
           'height': '36px',
           'backgroundColor': 'rgba(0,0,0,0)'
                                    }))
        ]),
    html.Hr(),
    html.Hr(),
    html.Hr(),
     html.Hr(),
    html.Hr(),
    #html.Hr(style={'borderWidth': "0.3vh", "width": "25%", "color": "#1B5244"}),
    
    dbc.Row([
          dbc.Col(html.H2('Un portafolio diverso',
                        className='card-title',style={'textAlign': 'left'} ),
                style={"color": "#91210C", },
                width={ "offset":1 },
                 ),
    ]),

      dbc.Row(
           [
           dbc.Col(html.H5(['Hemos recibido vacunas o sustancia activa desde seis paises: Bélica, Argentina, China, India, Rusia y Estados Unidos'
                               ],style={'textAlign': 'left'}),
                       width={'size': 6,  "offset":1 },
                      )],justify="align"),
   
   
    
     dbc.Row([                          #https://github.com/fdealbam/Vacunas/blob/main/application/static/mapa.JPG
               dbc.Col(dbc.CardImg(src="https://github.com/fdealbam/Vacunas/blob/main/application/static/mapa.JPG?raw=true"),
                      lg={'size': 6,  "offset": 3, }),
            
           ]),
    
    html.Hr(),
    html.Hr(),

    html.Hr(style={'borderWidth': "0.3vh", "width": "25%", "color": "#1B5244"}),      

       
    dbc.Row([
          dbc.Col(html.H2('Ciudades de arribo de las dosis',
                        className='card-title',style={'textAlign': 'left'} ),
                style={"color": "#91210C", },
                width={ "offset":1 },
                 ),
    ]),
   
     
       # Grafica     
       dbc.Row([dbc.Col(dcc.Graph(figure=figvac, config= "autosize", ))]),

])
    
    
app.layout = html.Div([body])

from application.dash import app
from settings import config

if __name__ == "__main__":
    app.run_server()

    
