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

vacunas = pd.read_csv("https://raw.githubusercontent.com/fdealbam/Vacunas/main/Arribo%20250321.csv", encoding= "Latin-1")
vacunas.rename(columns={'FarmacÃ©utica': 'Farmacéutica' },inplace=True,
                                   errors='ignore')
df = vacunas
Farmacéuticas = df.Farmacéutica.unique()

app = dash.Dash(__name__)

body = html.Div([
# Cintillo 000
        dbc.Row(
           [
               dbc.Col(dbc.CardImg(src="https://github.com/fdealbam/Vacunas/blob/main/SALUD.JPG?raw=true"),
                        width={'size': 1,  "offset": 1}),
               dbc.Col(html.H2("ARIBO DE VACUNAS"),
                        width={'offset' : 2}),
           ]),
# Top Banner

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
    ),
    dcc.Graph(id="bar-chart"),
]),
    
])

@app.callback(
    Output("bar-chart", "figure"), 
    [Input("dropdown", "value")])
def update_bar_chart(Farmacéutica):
    mask = df["Farmacéutica"] == Farmacéutica
    fig = px.bar(df[mask], x="Fecha", y="Cantidad", 
                 color="Arribo", barmode="group",
                 color_continuous_scale=px.colors.sequential.Inferno)
    return fig
    
    
app.layout = html.Div([body])
app.run_server()
