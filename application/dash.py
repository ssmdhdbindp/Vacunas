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
vacunas.rename(columns={'FarmacÃ©utica': 'Farmacéutica' },inplace=True,
                                   errors='ignore')


dosis = pd.read_csv("https://raw.githubusercontent.com/fdealbam/Vacunas/main/Dosis%20envasadas.csv", encoding= "Latin-1")
dosis.rename(columns={'FarmacÃ©utica': 'Farmacéutica' },inplace=True,
                                   errors='ignore')

dosis_a = pd.read_csv("https://raw.githubusercontent.com/fdealbam/Vacunas/main/Dosis%20promedio%20a%20envasar.csv", encoding= "Latin-1")
dosis_a.rename(columns={'FarmacÃ©utica': 'Farmacéutica' },inplace=True,
                                   errors='ignore')
# Dtypes 
vacunas['Cantidad']=vacunas['Cantidad'].astype(int)
# convert the 'Date' column to datetime format
format = '%d/%m/%Y'
vacunas['Fecha'] = pd.to_datetime(vacunas['Fecha'], format=format)
#vacunas.info()


#--------------------------------------------------------------------------------Dias
vvacunas = vacunas.groupby(by=["Fecha","Farmacéutica"])["Cantidad"].sum()
other_b = pd.DataFrame(vvacunas)
other_b.to_csv('0000procesodi.csv')
vuelve_a_abrir = pd.read_csv('0000procesodi.csv')
format = '%Y-%m-%d'
vuelve_a_abrir['Fecha'] = pd.to_datetime(vuelve_a_abrir['Fecha'], format=format)


#vacunas.info()
filtrado = vuelve_a_abrir.sort_values('Fecha',ascending=False).head(5)
#Suma semana
tot_sem = filtrado.Cantidad.sum()
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
row00 = html.Tr([html.Td(Fecha_1.strftime('%d-%B-%y')), html.Td(Fecha_2.strftime('%d-%B-%y')), 
                 html.Td(Fecha_3.strftime('%d-%B-%y')), html.Td(Fecha_4.strftime('%d-%B-%y')), 
                 html.Td(Fecha_5.strftime('%d-%B-%y')),html.Td("Total")])

row01 = html.Tr([html.Td([str(f"{cantidad_1:,d}")]), html.Td([str(f"{cantidad_2:,d}")]), 
                 html.Td([str(f"{cantidad_3:,d}")]), html.Td([str(f"{cantidad_4:,d}")]), 
                 html.Td([str(f"{cantidad_5:,d}")]), html.Td([str(f"{tot_sem:,d}")])])
row02 = html.Tr([html.Td(farmaceutica_1), html.Td(farmaceutica_2), html.Td(farmaceutica_3), 
                html.Td(farmaceutica_4), html.Td(farmaceutica_5)])

table_body69 = [html.Tbody([row00, row01, row02,
                         ])]

#table = dbc.Table(table_header69 + table_body69, bordered=True)
#-------------------------------------------------------------
tabla2 = vacunas.groupby(by=["Farmacéutica"])["Cantidad"].sum()
patabal2 = pd.DataFrame(tabla2)
patabal2.to_csv('0000procesodi.csv')
patabla1 = pd.read_csv('0000procesodi.csv')
patabla2 = patabla1.sort_values(by='Cantidad', ascending=False)
#Total Cantidad
tot_vac = patabla2.Cantidad.sum()
#Identificadores Farmaceuticas
farm_tot1 = patabla2.iloc[0]['Farmacéutica']
farm_tot2 = patabla2.iloc[1]['Farmacéutica']
farm_tot3 = patabla2.iloc[2]['Farmacéutica']
farm_tot4 = patabla2.iloc[3]['Farmacéutica']
farm_tot5 = patabla2.iloc[4]['Farmacéutica']
#farm_tot6 = patabla2.iloc[5]['Farmacéutica']

#Identificadores Cantidad
cant_tot1 = patabla2.iloc[0]['Cantidad']
cant_tot2 = patabla2.iloc[1]['Cantidad']
cant_tot3 = patabla2.iloc[2]['Cantidad']
cant_tot4 = patabla2.iloc[3]['Cantidad']
cant_tot5 = patabla2.iloc[4]['Cantidad']
#cant_tot6 = patabla2.iloc[5]['Cantidad']
# tabla2

table_header = [
    html.Thead(html.Tr([html.Th(), html.Th()]))] 
row1 = html.Tr([html.Td(farm_tot1), html.Td([str(f"{cant_tot1:,d}")])])
row2 = html.Tr([html.Td(farm_tot2), html.Td([str(f"{cant_tot2:,d}")])])
row3 = html.Tr([html.Td(farm_tot3), html.Td([str(f"{cant_tot3:,d}")])])
row4 = html.Tr([html.Td(farm_tot4), html.Td([str(f"{cant_tot4:,d}")])])
row5 = html.Tr([html.Td(farm_tot5), html.Td([str(f"{cant_tot5:,d}")])])
#row6 = html.Tr([html.Td(farm_tot6), html.Td([str(f"{cant_tot6:,d}")])])
row7 = html.Tr([html.Td("Total"), html.Td([str(f"{tot_vac:,d}")])])
table_body = [html.Tbody([row1, row2, row3, row4, row5,# row6,
                          row7])]
#---------------------------------------------------------------------GRAFICA
figvac0 = px.pie(patabla2, values='Cantidad', names='Farmacéutica',
             color_discrete_sequence=px.colors.sequential.Oranges, hole=.5)

figvac0.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                  plot_bgcolor='rgba(0,0,0,0)',
                  uniformtext_minsize=16,
                  uniformtext_mode='hide',
                  autosize=False,
                  width= 650,
                  height=650,
                  title_font_size = 16,
                  font_color="gray",
                  title_font_color="firebrick",
                  margin = dict(autoexpand= True,
                      t=0.1, l=0, r=0, b=0.1)   
                  )
######################################################################
figvac = px.pie(vacunas, values='Cantidad', names='Arribo',
             color_discrete_sequence=px.colors.sequential.Oranges, hole=.5)

figvac.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                  plot_bgcolor='rgba(0,0,0,0)',
                  uniformtext_minsize=16,
                  uniformtext_mode='hide',
                  autosize=False,
                  width= 650,
                  height=650,
                  title_font_size = 16,
                  font_color="gray",
                  title_font_color="firebrick",
                  margin = dict(autoexpand= True,
                      t=0.1, l=0, r=0, b=0.1)   
                  )


###################################################################### TABLA CIUDADES

vacunas_citys=vacunas.groupby('Arribo')['Cantidad'].sum()
pd.DataFrame(vacunas_citys).to_csv('0000proceso.csv')
vacunas_citys=pd.read_csv('0000proceso.csv').sort_values('Cantidad', ascending=False)
vacunas_citys.Arribo.replace('Ciudad de MÃ©xico','Ciudad de México', inplace=True)
vacunas_citys.Arribo.replace('QuerÃ©taro','Querétaro', inplace=True)

#Total by city
tot_vac_citys=vacunas_citys.Cantidad.sum()

# Ciudad
city1=vacunas_citys.iloc[0]['Arribo']
city2=vacunas_citys.iloc[1]['Arribo']
city3=vacunas_citys.iloc[2]['Arribo']
city4=vacunas_citys.iloc[3]['Arribo']
# Valores
city1_v=vacunas_citys.iloc[0]['Cantidad']
city2_v=vacunas_citys.iloc[1]['Cantidad']
city3_v=vacunas_citys.iloc[2]['Cantidad']
city4_v=vacunas_citys.iloc[3]['Cantidad']

# Tabla
table_headerciti = [
    html.Thead(html.Tr([html.Th(), html.Th()]))] 
row1 = html.Tr([html.Td(city1), html.Td([str(f"{city1_v:,d}")])])
row2 = html.Tr([html.Td(city2), html.Td([str(f"{city2_v:,d}")])])
row3 = html.Tr([html.Td(city3), html.Td([str(f"{city3_v:,d}")])])
row4 = html.Tr([html.Td(city4), html.Td([str(f"{city4_v:,d}")])])
row7 = html.Tr([html.Td("Total"), html.Td([str(f"{tot_vac_citys:,d}")])])
table_bodyciti = [html.Tbody([row1, row2, row3, row4, 
                          row7])]
#---------------------------------


#########################################################

# A P P

#########################################################





server = flask.Flask(__name__)
app = dash.Dash(__name__, external_stylesheets=[dbc.themes. LUX], server=server)

body = html.Div([ 
      
    html.Br(),
    
        dbc.Row(
            [
           
           dbc.Col(dbc.CardImg(src="https://github.com/fdealbam/Vacunas/blob/main/SRE.JPG?raw=true?raw=true"),
                        width={'size': 1,  "offset": 1 }),
            dbc.Col(html.H5("Secretaría de Relaciones Exteriores, "
                            "Subsecretaría para Asuntos Multilaterales y "
                            "Derechos Humanos"),
                  width={'size': 6, 'offset' : 0}), 
        ],justify="start"),
    dbc.Row(
           [dbc.Col(html.H6(d2),           #Fecha de actualización
               width={'size' : "auto",
                      'offset' : 2}), 
           ]),
  
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),

    dbc.Row([
        dbc.Col(html.H1('¿Cuántas vacunas han llegado a México?',
                        className='card-title',style={'textAlign': 'center'} ),
                style={"color": "red", 'text-transform': "uppercase", 
                       "font-weight": 'bolder', "font-stretch": "condensed",
                      "font-size": "x-large" },
                width={ "offset":2 },
                 ),
    ]),
   
        
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    dbc.Row([
        dbc.Col(html.H3('¿De qué farmacéutica provienen?',
                        className='card-title',style={'textAlign': 'start'} ),
                style={"color": "#91210C", },
                width={ "offset":1 },),

                
                
    ]),
    #html.Hr(style={'borderWidth': "0.3vh", "width": "25%", "color": "#1B5244"}),
    dbc.Row(
        [
            dbc.Col(dbc.Table(table_header + table_body, 
                              bordered=False, 
                              dark=False,
                              hover=True,
                              #responsive=True,
                              striped=True,
                              #size="sm",
                              #style_header={'backgroundColor': 'rgb(30, 30, 30)'},
                              style={
            'margin-top': '9px',
            'margin-left': '130px',
            'width': '509px',
            'height': '46px',
             "font-size": "large"                      
            #'backgroundColor': 'rgba(0,0,0,0)',
            }
                                     )),
            dbc.Col(dcc.Graph(figure=figvac0),
                    width={"size":1, "offset":2}
            )
        ]),
       dbc.Row(
           [
               dbc.Col(html.H6(["Hasta el 9 de abril, nuestro país ha recibido o envasado  ", 
                                str(f"{tot_vac:,d} dosis de vacunas contra COVID-19 listas para aplicarse "),
                               ],style={'textAlign': 'left'}),
                       width={'size': 5,  "offset":1 },
                      )],justify="start"),
    
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    

         
    dbc.Row([
          dbc.Col(html.H3('¿A qué ciudad arriban las vacunas?',
                        className='card-title',style={'textAlign': 'left'} ),
                style={"color": "#91210C", },
                width={ "offset":1 },
                 ),
    ]),

       # Grafica     
       dbc.Row([
           dbc.Col(dbc.Table(table_headerciti + table_bodyciti, 
                              bordered=False, 
                              dark=False,
                              hover=True,
                              #responsive=True,
                              striped=True,
                              #size="sm",
                              #style_header={'backgroundColor': 'rgb(30, 30, 30)'},
                              style={
            'margin-top': '9px',
            'margin-left': '130px',
            'width': '509px',
            'height': '46px',
             "font-size": "large"                      
            #'backgroundColor': 'rgba(0,0,0,0)',
            })),
           
           
           dbc.Col(dcc.Graph(figure=figvac), #config= "autosize"), 
                              width={'size': 6,  "offset":1 }   )
               ]),#,justify="center"),

    
    
    
#    #html.Hr(style={'borderWidth': "0.3vh", "width": "25%", "color": "#1B5244"}),
#     dbc.Row([
#        dbc.Col(html.H3('Arribos Recientes',
#                        className='card-title',style={'textAlign': 'start'} ),
#                style={"color": "#91210C", },
#                width={ "offset":1 },),
#
#                
#                
#    ]),
#
#     
#
#    dbc.Row(
#        [
#            dbc.Col(dbc.Table(table_header69 + table_body69, 
#                              bordered=False, 
#                              dark=False,
#                              hover=True,
#                              #responsive=True,
#                              striped=True,
#                              #size="sm",
#                              #style_header={'backgroundColor': 'rgb(30, 30, 30)'},
#                              style={
#            'margin-top': '9px',
#            'margin-left': '130px',
#            'width': '509px',
#            'height': '46px',
#             "font-size": "large"                      
#            #'backgroundColor': 'rgba(0,0,0,0)',
#            }
#                                     ))
#        ],justify="start"),
#    
#      dbc.Row(
#           [
#               dbc.Col(html.H6(["Entre el 1 y el 9 de abril, nuestro país recibió  ", 
#                                str(f"{tot_sem:,d} dosis, listas para aplicarse "),
#                               ],style={'textAlign': 'left'}),
#                       width={'size': 5,  "offset":1 },
#                      )],justify="start"),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
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
   # # dbc.Row([dbc.Col(dcc.Graph(figure=aa), 
   #                   style={'width': '100%', 'display': 'inline-block',
   #                         'align': 'center'}),
   #            ]),#,justify="center"),
   
   
    
     dbc.Row([                          #https://github.com/fdealbam/Vacunas/blob/main/application/static/mapa.JPG
               dbc.Col(dbc.CardImg(src="https://github.com/fdealbam/Vacunas/blob/main/application/static/mapa.JPG?raw=true"),
                      lg={'size': 6,  "offset": 3, }),
            
           ]),
    
    html.Hr(),
    html.Hr(),

    #html.Hr(style={'borderWidth': "0.3vh", "width": "25%", "color": "#1B5244"}),      

    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    
])
    
    
app.layout = html.Div([body])

from application.dash import app
from settings import config

if __name__ == "__main__":
    app.run_server()
