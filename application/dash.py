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
############################### Abre archivos

vacunas = pd.read_csv("https://raw.githubusercontent.com/fdealbam/Vacunas/main/vacunasreport.csv", encoding= "Latin-1")
vacunas.rename(columns={'Farmaceutica ': 'Farmaceutica' },inplace=True,
                                   errors='ignore')


# Dtypes 
vacunas['Cantidad']=vacunas['Cantidad'].astype(int)
# convert the 'Date' column to datetime format
format = '%d/%m/%Y'
vacunas['fecha'] = pd.to_datetime(vacunas['fecha'], format=format)
vacunas.info()


#--------------------------------------------------------------------------------Dias
vvacunas = vacunas.groupby(by=["fecha","dia","Farmaceutica"])["Cantidad"].sum()
other_b = pd.DataFrame(vvacunas)
other_b.to_csv('0000procesodi.csv')
vuelve_a_abrir = pd.read_csv('0000procesodi.csv')
format = '%Y-%m-%d'
vuelve_a_abrir['fecha'] = pd.to_datetime(vuelve_a_abrir['fecha'], format=format)


#vacunas.info()
filtrado = vuelve_a_abrir.sort_values('fecha',ascending=False).head(5)
#filtrado.fecha = today.strftime("%d-%m-%Y")
#Identificadores dias
dia_1 = filtrado.iloc[4]['dia']
dia_2 = filtrado.iloc[3]['dia']
dia_3 = filtrado.iloc[2]['dia']
dia_4 = filtrado.iloc[1]['dia']
dia_5 = filtrado.iloc[0]['dia']
#Identificadores fechas
fecha_1 = filtrado.iloc[4]['fecha']
fecha_2 = filtrado.iloc[3]['fecha']
fecha_3 = filtrado.iloc[2]['fecha']
fecha_4 = filtrado.iloc[1]['fecha']
fecha_5 = filtrado.iloc[0]['fecha']
#Identificadores Cantidad
cantidad_1 = filtrado.iloc[4]['Cantidad']
cantidad_2 = filtrado.iloc[3]['Cantidad']
cantidad_3 = filtrado.iloc[2]['Cantidad']
cantidad_4 = filtrado.iloc[1]['Cantidad']
cantidad_5 = filtrado.iloc[0]['Cantidad']
#Identificadores Farmaceutica s
farmaceutica_1 = filtrado.iloc[4]['Farmaceutica']
farmaceutica_2 = filtrado.iloc[3]['Farmaceutica']
farmaceutica_3 = filtrado.iloc[2]['Farmaceutica']
farmaceutica_4 = filtrado.iloc[1]['Farmaceutica']
farmaceutica_5 = filtrado.iloc[0]['Farmaceutica']
#-------------------------------------------------Tabla dias
table_header69 = [
    html.Thead(html.Tr([html.Th(fecha_1.strftime('%d-%B-%y')), html.Th(fecha_2.strftime('%d-%B-%y')),
                        html.Th(fecha_3.strftime('%d-%B-%y')), html.Th(fecha_4.strftime('%d-%B-%y')),
                        html.Th(fecha_5.strftime('%d-%B-%y'))]))
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
tabla2 = vacunas.groupby(by=["Farmaceutica"])["Cantidad"].sum()
patabal2 = pd.DataFrame(tabla2)
patabal2.to_csv('0000procesodi.csv')
patabla2 = pd.read_csv('0000procesodi.csv')
#Total Cantidad
tot_vac = patabla2.Cantidad.sum()
#Identificadores Farmaceuticas
farm_tot1 = patabla2.iloc[0]['Farmaceutica']
farm_tot2 = patabla2.iloc[1]['Farmaceutica']
farm_tot3 = patabla2.iloc[2]['Farmaceutica']
farm_tot4 = patabla2.iloc[3]['Farmaceutica']
#Identificadores Cantidad
cant_tot1 = patabla2.iloc[0]['Cantidad']
cant_tot2 = patabla2.iloc[1]['Cantidad']
cant_tot3 = patabla2.iloc[2]['Cantidad']
cant_tot4 = patabla2.iloc[3]['Cantidad']
# tabla2
table_header = [
    html.Thead(html.Tr([html.Th(), html.Th()]))]
row1 = html.Tr([html.Td(farm_tot1), html.Td(cant_tot1)])
row2 = html.Tr([html.Td(farm_tot2), html.Td(cant_tot2)])
row3 = html.Tr([html.Td(farm_tot3), html.Td(cant_tot3)])
row4 = html.Tr([html.Td(farm_tot4), html.Td(cant_tot4)])
table_body = [html.Tbody([row1, row2, row3, row4])]
#---------------------------------------------------------------------GRAFICA
figvac = px.bar(vacunas, x= 'fecha', y='Cantidad',
                color='Arribo', # barmode="group",  
                
                color_continuous_scale=px.colors.sequential.Inferno
               )

figvac.update_layout( showlegend=True,
    width= 1200,
    height=700,
   # xaxis_tickangle=-45,
   # xaxis_tickfont_size= 18,
    legend=dict(orientation="h",
               yanchor= "top",
               y=0.99,
               #xanchor="center",
               x=0.01 ),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',

                     
)
figvac.update_yaxes(automargin=False)


#Suma semana
tot_sem = filtrado.Cantidad.sum()


server = flask.Flask(__name__)
app = dash.Dash(__name__, external_stylesheets=[dbc.themes. FLATLY], server=server)

body = html.Div([ 
       dbc.Row(
           [dbc.Col(html.H6(d2),           #Fecha de actualización
               width={'size' : "auto",
                      'offset' : 9}), 
           ]),
    
        dbc.Row(
            [
           
           dbc.Col(dbc.CardImg(src="https://github.com/fdealbam/Vacunas/blob/main/SRE.JPG?raw=true?raw=true"),
                        width={'size': 1,  "offset": 1 }),
            dbc.Col(html.H5("Subsecretaría para Asuntos Multilaterales y "
                            "Derechos Humanos"),
                  width={'offset' : 9}), 
        ]),
  
    html.Br(),
      dbc.Row(
           [
               dbc.Col(html.H1(["Esta semana llegaron a México ", 
                       dbc.Badge([str(f"{tot_sem:,d}")],
                                 color="info", className="mr-1"),
                                html.H1(" dosis de vacunas contra COVID-19 "),
                               ],style={'textAlign': 'center'}),
                       width={'size': 11,  "offset":1 },
                      )],justify="start"),
    html.Br(),
    html.Br(),
    html.Br(),
    
      dbc.Row(
           [
               dbc.Col(html.H4(["VACUNAS DE LOS ", 
                       dbc.Badge("ÚLTIMOS CINCO DIAS", color="success", className="mr-1")]), 
                                       width={'size': 11,  "offset":2 })
           
           ]),
    html.Br(),

    dbc.Row([
        dbc.Col(html.H3([" ",dbc.Badge((dia_1), className="ml-1",color="light",),
                             dbc.Badge((dia_2), className="ml-1",color="light",),
                             dbc.Badge((dia_3), className="ml-1",color="light",),
                             dbc.Badge((dia_4), className="ml-1",color="light",),
                             dbc.Badge((dia_5), className="ml-1",color="light",),   
                        ]),
                width={'size': 11,  "offset":5 })]),
    dbc.Row(
        [
            dbc.Col(dbc.Table(table_header69 + table_body69, 
                              bordered=False, 
                              size="sm",
                              style={
            'margin-top': '9px',
            'margin-left': '525px',
            'width': '609px',
            'height': '36px',
            'backgroundColor': 'rgba(0,0,0,0)'
            }
                                     ))
        ]),
    
   
    html.Br(),
     dbc.Row(
           [
               dbc.Col(html.H4(["VACUNAS SEGÚN ", 
                       dbc.Badge("FARMACÉUTICA", color="success", className="mr-1")]), 
                                       width={'size': 11,  "offset":2})
           
           ]),
    dbc.Row(
        [
            dbc.Col(dbc.Table(table_header + table_body, 
                              bordered=False, 
                              size="sm",
                              style={
            'margin-top': '9px',
            'margin-left': '525px',
            'width': '609px',
            'height': '36px',
            'backgroundColor': 'rgba(0,0,0,0)'
            }
                                     ))
        ]),
     dbc.Row(
           [
               dbc.Col(html.H5(["Total",
                                
                       dbc.Badge([str(f"{tot_vac:,d}")], color="warning", className="mr-1")]), 
                                       width={'size': 11,  "offset":7 })
           
           ]),
      dbc.Row(
           [
               dbc.Col(html.H4(["VACUNAS SEGÚN ", 
                       dbc.Badge("LLEGADAS DIARIAS", color="success", className="mr-1")]), 
                                       width={'size': 11,  "offset":2 })
           
           ]),
    html.Br(),
    dbc.Row(
        [dbc.Col(dcc.Graph(figure=figvac, config= "autosize"),
         width={'size': 5,  "offset":1 })],
    ),
])
    
    
app.layout = html.Div([body])

from application.dash import app
from settings import config

if __name__ == "__main__":
    app.run_server()
