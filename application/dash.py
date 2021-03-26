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


#os.chdir(r"C:\Users\PRIME\AnacondaProjects\Project_curso\\")
vvacunas = pd.read_csv("https://raw.githubusercontent.com/fdealbam/Vacunas/main/vacunasreport.csv", encoding= "Latin-1")
vvacunas.rename(columns={'FarmacÃ©utica': 'Farmaceutica' },inplace=True,
                                   errors='ignore')

#vvacunas =pd.read_csv("vacunasreport.csv")

# Dtypes 
vvacunas.astype({'Cantidad': 'int32',
                 #'Fecha': 'date'
                 }).dtypes
vvacunas.Cantidad.index





#################################################  Graph

#figvac = px.bar(df, x="Fecha", y="Cantidad", 
#                 color="Arribo", barmode="group",
#                 color_continuous_scale=px.colors.sequential.Inferno)

#figvac = go.Figure()
#figvac.add_trace(go.Bar(x=vacunas.Fecha, y=vacunas.Cantidad,
#                marker_color='indianred', barmode="group")  # cambiar nuemeritos de rgb
                #color_continuous_scale=px.colors.sequential.Inferno))

figvac = px.bar(vvacunas, x= 'Fecha', y='Cantidad',
                color='Arribo', #barmode="group",  
                width= 10,
                # color_continuous_scale=px.colors.sequential.Inferno
               )

figvac.update_layout( showlegend=True,
    autosize=True,
    width= 2000,
    height=700,
    xaxis_tickangle=-45,
    xaxis_tickfont_size= 18,
    legend=dict(orientation="h",
               yanchor= "top",
               y=0.99,
               #xanchor="center",
               x=0.01,
               font=dict(
               family="Monserrat",
               size=14,
               color="black"
        ),),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    yaxis=dict(
#        #title='Tasa cada 100 000 habitantes',
#        titlefont_size=14,
#        tickfont_size=12,
        titlefont_family= "Monserrat")
                     
)
figvac.update_yaxes(automargin=False)
#    xaxis_tickangle=-45,
#    template = 'simple_white',
#    #title='Tasa feminicidio periodo 2015-2020',
#    xaxis_tickfont_size= 12,
#    yaxis=dict(
#        #title='Tasa cada 100 000 habitantes',
#        titlefont_size=14,
#        tickfont_size=12,
#        titlefont_family= "Monserrat")
#

#################################################

# A P P

##################################################

#df = vacunas
#Farmacéuticas = df.Farmacéutica.unique()

    
server = flask.Flask(__name__)
app = dash.Dash(__name__, external_stylesheets=[dbc.themes. LUX], server=server)

body = html.Div([
# Cintillo 000
       html.Hr(),       
       html.Hr(),    
dbc.Row(
           [
               #dbc.Col(dbc.CardImg(src="https://raw.githubusercontent.com/fdealbam/Vacunas/main/srelogo.png?raw=true"),
               #         lg={'size': 1,  "offset": 1}),
               dbc.Col(html.H5("Subsecretaría de Asuntos Multilaterales"),
                        lg={'size': 6,  'offset' : 1}),
           ],justify="start"),    
    

        dbc.Row(
           [
               dbc.Col(html.H1("ARRIBO DE VACUNAS"),
                        lg={'size': 6, 'offset' : 1 }),
           ],justify="start"),
                   
# Top Banner
        dbc.Row(
            [
               dbc.Col(html.H6(d2),           #Fecha de actualización
                        lg={'size': 6, 'offset' : 1 }),
            ],justify="start"),

    #Cintillo 00    
    

        dbc.Row(
            [
               dbc.Col(dcc.Graph(figure=figvac, config= "autosize")),
                   #lg={'size': 5,  "offset": 0,}),
            ], justify="end", no_gutters=True,),

    
            ])
    
    
app.layout = html.Div([body])

from application.dash import app
from settings import config

if __name__ == "__main__":
    app.run_server()
