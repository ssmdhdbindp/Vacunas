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


#os.chdir(r"C:\Users\PRIME\AnacondaProjects\Project_curso\\")

vacunas = pd.read_csv("https://raw.githubusercontent.com/fdealbam/Vacunas/main/vacunasreport.csv", encoding= "Latin-1")
vacunas.rename(columns={'FarmacÃ©utica': 'Farmacéutica' },inplace=True,
                                   errors='ignore')

# Dtypes 
vacunas.astype({'Cantidad': 'int32',
                 #'Fecha': 'date'
                 }).dtypes
vacunas.Cantidad.index



#df = vacunas
Farmacéuticas = vacunas.Farmaceutica.unique()

server = flask.Flask(__name__)
app = dash.Dash(__name__, external_stylesheets=[dbc.themes. LUX], server=server)

body = html.Div([
# Cintillo 000
        dbc.Row(
           [
               dbc.Col(dbc.CardImg(src="https://github.com/Aeelen-Miranda/Vacunas/blob/main/SRE.JPG?raw=true"),
                       lg={'size': 1.5,  "offset": 10}),
               dbc.Col(
                   html.H5("Subsecretaría de Asuntos Multilaterales"),
                        lg={'size': 6,  'offset' : 1}),
           ],justify="start"),    
    

        dbc.Row(
           [
               dbc.Col(html.H1("ARRIBO DE VACUNAS"),
                        lg={'size': 6, 'offset' : 1 }),
           ],justify="start"),

       html.Hr(),
    dbc.Row(
           [
               dbc.Col(html.H4(d2),           #Fecha de actualización
               width={'size' : "auto",
                      'offset' : 4}), 
           ]),
#Cintillo 00    
    dbc.Row(
           [dcc.Dropdown(
        id="dropdown",
        options=[{"label": x, "value": x} for x in Farmacéuticas],
        value=Farmacéuticas[0],
        clearable=False,
               #width={'size' : 6,'offset' : 1 },
                  style={'width': '100%', 'display': 'inline-block','text-size': 28}),

   
    dcc.Graph(id="bar-chart", figure={},
              className="top_metrics",
                      style={'width': '100%', 'display': 'inline-block',
                            'align': 'center'}),
]),
   
])

@app.callback(
    Output("bar-chart", "figure"), 
    [Input("dropdown", "value")])
def update_bar_chart(Farmaceutica):
    mask = vacunas["Farmaceutica"] == Farmaceutica
    fig = px.bar(vacunas[mask], x="Fecha", y="Cantidad", 
                 color="Arribo",) #barmode="group",
                 #color_continuous_scale=px.colors.sequential.Inferno)
               
    return fig
    
    
app.layout = html.Div([body])

from application.dash import app
from settings import config

if __name__ == "__main__":
    app.run_server()
