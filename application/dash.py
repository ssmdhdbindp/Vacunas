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

   

dosis_a = pd.read_csv("https://raw.githubusercontent.com/fdealbam/Vacunas/main/Dosis%20promedio%20a%20envasar.csv", encoding= "Latin-1")
dosis_a.rename(columns={'FarmacÃ©utica': 'Farmacéutica' },inplace=True,
                                   errors='ignore')
# Dtypes 
vacunas['Cantidad']=vacunas['Cantidad'].astype(int)
#Total Cantidad
tot_vac = vacunas.Cantidad.sum()
# convert the 'Date' column to datetime format
format = '%d/%m/%Y'
vacunas['Fecha'] = pd.to_datetime(vacunas['Fecha'], format=format)
#vacunas.info()




###############################
# TRATAMIENTO
############################### 


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



###################################################################### 
#-------------------------------------Tratamiento de tabla Farmacéutica TABLA1

tabla2 = vacunas.groupby(by=["Farmacéutica"])["Cantidad"].sum()
patabal2 = pd.DataFrame(tabla2)
patabal2.to_csv('0000procesodi.csv')
patabla1 = pd.read_csv('0000procesodi.csv')
patabla2 = patabla1.sort_values(by='Cantidad', ascending=False)




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



############################################### Tratamiento TABLA meses 
vac_meses=vacunas

vac_meses['Year'] = vac_meses['Fecha'].dt.year
#vac_meses=vac_meses[vac_meses.Year!='nan']
vac_meses.dropna(inplace=True)
vac_meses['Year']=vac_meses['Year'].astype(int)
vac_meses['Year']=vac_meses['Year'].astype(str)

vac_meses['Mes'] = vac_meses['Fecha'].dt.month

vac_meses['Mes'].replace(1.0,'Enero',inplace=True)
vac_meses['Mes'].replace(2.0,'Febrero',inplace=True)
vac_meses['Mes'].replace(3.0,'Marzo',inplace=True)
vac_meses['Mes'].replace(4.0,'Abril',inplace=True)
vac_meses['Mes'].replace(5.0,'Mayo',inplace=True)
vac_meses['Mes'].replace(6.0,'Junio',inplace=True)
vac_meses['Mes'].replace(7.0,'Julio',inplace=True)
vac_meses['Mes'].replace(8.0,'Agosto',inplace=True)
vac_meses['Mes'].replace(9.0,'Septiembre',inplace=True)
vac_meses['Mes'].replace(10.0,'Octubre',inplace=True)
vac_meses['Mes'].replace(12.0,'Noviembre',inplace=True)
vac_meses['Mes'].replace(13.0,'Diciembre',inplace=True)

vac_meses['Mes']=vac_meses['Mes'].astype(str)

vac_meses['Mes_y']=vac_meses['Mes']+vac_meses['Year']
vac_meses_g=vac_meses.groupby('Mes_y')['Cantidad'].sum()
pd.DataFrame(vac_meses_g).to_csv('0000proceso.csv')
vac_meses_g=pd.read_csv('0000proceso.csv')

#Identificadores Cantidad
sumdic_v = vac_meses_g.iloc[4]['Cantidad']
sumene_v = vac_meses_g.iloc[1]['Cantidad']
sumfeb_v = vac_meses_g.iloc[2]['Cantidad']
summar_v = vac_meses_g.iloc[3]['Cantidad']
sumabr_v = vac_meses_g.iloc[0]['Cantidad']





########################################################################## Para la APP 
#-------------------------------------GRAFICA1 DE FARMACEUTICA para TABLA1

figvac0 = px.pie(patabla2, values='Cantidad', names='Farmacéutica',
                color_discrete_sequence=px.colors.sequential.Oranges, hole=.5)

figvac0.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                  plot_bgcolor='rgba(0,0,0,0)',
                  uniformtext_minsize=16,
                  uniformtext_mode='hide',
                  autosize=True,
                  #width= 650,
                  #height=650,
                  title_font_size = 16,
                  font_color="gray",
                  title_font_color="firebrick",
                  margin = dict(autoexpand= True)),
                      #t=0, l=0, r=0, b=0)   
                  
figvac0.update_traces(pull=[0.05, 0.05, 0.05, 0.05, 0.1],
                    rotation=90)
###################################################################### 
#-------------------------------------Tratamiento de tabla CIUDADES TABLA2

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



########################################################################## Para la APP 
#-------------------------------------GRAFICA DE CIUDADES para TABLA2

figvac = px.pie(vacunas_citys, values='Cantidad', names='Arribo',
             color_discrete_sequence=px.colors.sequential.Oranges, hole=.5)

figvac.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                  plot_bgcolor='rgba(0,0,0,0)',
                  uniformtext_minsize=22,
                  uniformtext_mode='hide',
                  autosize=True,
                  #width= 650,
                  #height=650,
                  title_font_size = 22,
                  font_color="gray",
                  title_font_color="firebrick",
                  margin = dict(autoexpand= True)),
                      #t=0, l=0, r=0, b=0)   
                  #)
figvac.update_traces(pull=[0.05, 0.05, 0.05, 0.05, 0.1],
                    rotation=300)




########################################################################## Para la APP 
#-------------------------------------Calculo para completar 126millions

day_min = vacunas.Fecha.min()
day_max = vacunas.Fecha.max()
days_passed= (day_max-day_min).days


days_passed= (day_max-day_min).days

# Días, Meses y Años restantes para cubrir 126M vacunas
days_rest=(((126000000-tot_vac)*days_passed)/tot_vac).round()
month_rest=(days_rest/30).round()
year_rest=month_rest/12

print("Para cubrir 126M de vacunas se requieren: ",int(days_rest)," Dias ")
print("Para cubrir 126M de vacunas se requieren: ",int(month_rest)," Meses ")
print("Para cubrir 126M de vacunas se requieren: ",year_rest," Años ")
#
print()
#
from datetime import timedelta, date
date_126M = date.today() + timedelta(days=int(days_rest))
query= date_126M.strftime("Se estima que tendríamos 126 millones de dosis el día %d de %B de %Y")



#########################################################
# A P P
#########################################################


######################################################### Para la APP 
#-------------------------------------Tratamiento de tabla farmaceutica TABLA1

table_header = [
    html.Thead(html.Tr([html.Th(), html.Th()]))] 

row1 = html.Tr([html.Td(farm_tot1), html.Td([str(f"{cant_tot1:,d}")])])
row2 = html.Tr([html.Td(farm_tot2), html.Td([str(f"{cant_tot2:,d}")])])
row3 = html.Tr([html.Td(farm_tot3), html.Td([str(f"{cant_tot3:,d}")])])
row4 = html.Tr([html.Td(farm_tot4), html.Td([str(f"{cant_tot4:,d}")])])
row5 = html.Tr([html.Td(farm_tot5), html.Td([str(f"{cant_tot5:,d}")])])
#row6 = html.Tr([html.Td(farm_tot6), html.Td([str(f"{cant_tot6:,d}")])])
row7 = html.Tr([html.Td("Total"), html.Td([str(f"{tot_vac:,d}")])])
                    
row7 = html.Tr([html.Th("Total", style={"offset": 3, "color": "black",
                                                 'fontWeight': 'bold',
                                                 'fontSize':20,}),
                html.Th([str(f"{tot_vac:,d}")], 
                                          style={"color": "red",
                                                 'fontWeight': 'bold',
                                                 'fontSize':20,})])

table_body = [html.Tbody([row1, row2, row3, row4, row5,# row6,
                          row7])]


######################################################### Para la APP 
#-------------------------------------TABLA CIUDADES TABLA2

table_headerciti = [
    html.Thead(html.Tr([html.Th(), html.Th()]))] 
row1 = html.Tr([html.Td(city1), html.Td([str(f"{city1_v:,d}")])])
row2 = html.Tr([html.Td(city2), html.Td([str(f"{city2_v:,d}")])])
row3 = html.Tr([html.Td(city3), html.Td([str(f"{city3_v:,d}")])])
row4 = html.Tr([html.Td(city4), html.Td([str(f"{city4_v:,d}")])])
row7 = html.Tr([html.Td("Total"), html.Td([str(f"{tot_vac_citys:,d}")])])
#row7 = html.Tr([html.Th("Total"), html.Td([str(f"{tot_vac_citys:,d}")]),


row7 = html.Tr([html.Th("Total", style={"offset": 3, "color": "black",
                                                 'fontWeight': 'bold',
                                                 'fontSize':20,}),
                html.Th([str(f"{tot_vac_citys:,d}")], 
                                          style={"color": "red",
                                                 'fontWeight': 'bold',
                                                 'fontSize':20,})])




table_bodyciti = [html.Tbody([row1, row2, row3, row4, 
                          row7])]

#-------------------------------------TABLAS MESES TABLA2
table_sumameses = [
    html.Thead(html.Tr([html.Th(), html.Th(), html.Th(), html.Th(), html.Th()]))] 
row1 = html.Tr([html.Td("Diciembre"),html.Td("Enero"), html.Td("Febrero"),  html.Td("Marzo"), html.Td("Abril")])

row2 = html.Tr([html.Td([str(f"{sumdic_v:,d}")]), html.Td([str(f"{sumene_v:,d}")]), html.Td([str(f"{sumfeb_v:,d}")]), html.Td([str(f"{summar_v:,d}")]), html.Td([str(f"{sumabr_v:,d}")])])

table_bodymeses = [html.Tbody([row1, row2])]


######################################################### Dias transcurridos




#########################################################
#------------------------------------------------------------------------DOSIS A ENVASAR

format = '%d/%m/%Y'
dosis_a['Fecha'] = pd.to_datetime(dosis_a['Fecha'], format=format)

dosis_a_ = dosis_a.sort_values('Fecha',ascending=True).head(5)
#Suma semana
dosis_tot_a = dosis_a_["Dosis promedio a envasar"].sum()
#
fech_1_d = dosis_a_.iloc[0]['Fecha']
fech_2_d = dosis_a_.iloc[1]['Fecha']
fech_3_d = dosis_a_.iloc[2]['Fecha']
fech_4_d = dosis_a_.iloc[3]['Fecha']
#
lug_1_d = dosis_a_.iloc[0]['Arribo']
lug_2_d = dosis_a_.iloc[1]['Arribo']
lug_3_d = dosis_a_.iloc[2]['Arribo']
lug_4_d = dosis_a_.iloc[3]['Arribo']
#
denv_1_d = dosis_a_.iloc[0]['Dosis promedio a envasar']
denv_2_d = dosis_a_.iloc[1]['Dosis promedio a envasar']
denv_3_d = dosis_a_.iloc[2]['Dosis promedio a envasar']
denv_4_d = dosis_a_.iloc[3]['Dosis promedio a envasar']
#
farm_1_d = dosis_a_.iloc[0]['Farmacéutica']
farm_2_d = dosis_a_.iloc[1]['Farmacéutica']
farm_3_d = dosis_a_.iloc[2]['Farmacéutica']
farm_4_d = dosis_a_.iloc[3]['Farmacéutica']

table_headerDOSISe = [
    html.Thead(html.Tr([html.Td(), html.Td(), 
                        html.Td(), html.Td()],
                      # style={merge_duplicate_headers=True}
                      ))] 

#d2 = today.strftime("Fecha de actualización : %d-%m-%Y")

row1de = html.Tr([html.Td(fech_1_d.strftime('%d-%m-%Y')), html.Td(fech_2_d.strftime('%d-%m-%Y')), html.Td(fech_3_d.strftime('%d-%m-%Y')), html.Td(fech_4_d.strftime('%d-%m-%Y'))])
row2de = html.Tr([html.Td(f"{int(denv_1_d):,}"), 
                  html.Td(f"{int(denv_2_d):,}"), 
                  html.Td(f"{int(denv_3_d):,}"), 
                  html.Td(f"{int(denv_4_d):,}")])
row3de = html.Tr([html.Td(farm_1_d), html.Td(farm_2_d), html.Td(farm_3_d), html.Td(farm_4_d)])
#row4de = html.Tr([html.Td(lug_3_d), html.Td(lug_4_d), html.Td(denv_4_d), html.Td(farm_4_d)])
#row5de = html.Tr([html.Td(lug_4_d), html.Td("Total"), html.Td(dosis_tot_a), html.Td(" ")])

table_bodyDOSISe = [html.Tbody([row1de, row2de, row3de, #row4de,row5de
                               ])]

#---------------------------------------------------------------------GRAFICA PIE DOSIS a ENVASAR
figvacdosis = px.pie(dosis_a, values='Dosis promedio a envasar', names='Farmacéutica',
             color_discrete_sequence=px.colors.sequential.Oranges, hole=.5)

figvacdosis.update_layout(paper_bgcolor='rgba(0,0,0,0)',
                  plot_bgcolor='rgba(0,0,0,0)',
                  uniformtext_minsize=22,
                  uniformtext_mode='hide',
                  autosize=True,
                  #width= 650,
                  #height=650,
                  title_font_size = 22,
                  font_color="gray",
                  title_font_color="firebrick",
                  margin = dict(autoexpand= True)),
                      #t=0, l=0, r=0, b=0)   
                  #)
figvacdosis.update_traces(pull=[0.05, 0.05, 0.05, 0.05, 0.1],
                    rotation=75)

######################################################### Codigo del dashboard

server = flask.Flask(__name__)
app = dash.Dash(__name__, external_stylesheets=[dbc.themes. LUX], server=server)

body = html.Div([ 
      
    html.Br(),
    
        dbc.Row(
            [dbc.Col(dbc.CardImg(src="https://github.com/fdealbam/Vacunas/blob/main/SRE.JPG?raw=true?raw=true"),
                        width={'size': 1,  "offset": 1 }),
             dbc.Col(html.H5("Secretaría de Relaciones Exteriores, "
                            "Subsecretaría para Asuntos Multilaterales y "
                            "Derechos Humanos"),
                        width={'size': 6, 'offset' : 0}), 
        ],justify="start"),
    
    dbc.Row(
           [dbc.Col(html.H6(d2),           #Fecha de actualización
               width={'size' : "auto", 'offset' : 2})]),
  
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),

    dbc.Row(
        [dbc.Col(html.H1(['¿Cuántas vacunas han llegado a México?    ', 
                         dbc.Badge(f"{int(tot_vac):,}", color="danger", className="mr-1")]),
                style={"color": "red", 'text-transform': "uppercase", 
                       "font-weight": 'bolder', "font-stretch": "condensed",
                      "font-size": "x-large" },
                width={ "offset":2 }),
    ]),
    
        #dbc.Alert("", color="warning"),
    
#    html.Br(),
    html.Br(),
  
# ###################### SECCION . DIAS TRANSCURRIDOS
  
  dbc.Row(
           [dbc.Col(html.H6(["Desde el día de importación del primer lote de vacunas contra el COVID-19 han trascurrido ",days_passed," días"]
                            ,style={'textAlign': 'left'}),
                       width={'size': 10,  "offset":1 },
                      )],justify="center"),
    
    html.Br(),
    html.Br(),
  
# ###################### SECCION . MESES

     dbc.Row(
           [dbc.Col(html.H5("Diciembre")),
                  # width={'size' : "auto", "offset":1}),
            dbc.Col(html.H5("Enero")),
                  # width={'size' : "auto","offset":1}),
            dbc.Col(html.H5("Febrero")),
                  # width={'size' : "auto","offset":1}),
            dbc.Col(html.H5("Marzo")),
                  # width={'size' : "auto","offset":1}),
            dbc.Col(html.H5("Abril")),
                  # width={'size' : "auto", "offset":1}),

           ], justify="around"),
    
#Cintillo 1
    dbc.Row(
           [
               dbc.Col(html.H1(str(f'{sumdic_v:,d}'))),
                    #   width={'size' : "auto", "offset":1}),
               dbc.Col(html.H1(str(f'{sumene_v:,d}'))),
                     #  width={'size' : "auto", "offset":1}),
               dbc.Col(html.H1(str(f'{sumfeb_v:,d}'))),
                      # width={'size' : "auto", "offset":1}),
               dbc.Col(html.H1(str(f'{summar_v:,d}'))),
                      #width={'size' : "auto", "offset":1}),
               dbc.Col(html.H1(str(f'{sumabr_v:,d}'))),
                      #width={'size' : "auto", "offset":1}),
            ],justify= "around"),
    
    
    
        
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    
    
# ###################### SECCION 1. FARMACEUTICAS
        
    dbc.Row(
        [dbc.Col(html.H2('¿De qué farmacéutica provienen?',className='card-title',
                         style={'textAlign': 'start', "color": "#91210C",}),
                 width={ "offset":1 }),

            ]),
    
    
####################### TABLA 1
    dbc.Row(
        [dbc.Col(dbc.Table(table_header + table_body, 
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
            'margin-right': '0px',
            'width': '509px',
            'height': '46px',
            "font-size": "large" }
                                     )),

            
####################### GRAFICA 1
            dbc.Col(dcc.Graph(figure=figvac0),
                    width={'size' : "auto", "offset":0}), ]),
    
       dbc.Row(
           [dbc.Col(html.H6(["Hasta el 15 de abril, nuestro país ha recibido o envasado  ", 
                                str(f"{tot_vac:,d} dosis de vacunas contra COVID-19 listas para aplicarse "),
                               ],style={'textAlign': 'left'}),
                       width={'size': 10,  "offset":1 },
                      )],justify="align"),
    
        
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    
# ###################### SECCION 2. CIUDADES
        
    dbc.Row(
        [dbc.Col(html.H2('¿A qué ciudad arriban las vacunas?',
                        className='card-title',style={'textAlign': 'left',"color": "#91210C"}),
                 width={ "offset":1 }),
    ]),



    
####################### TABLA 2
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
           
           
####################### GRAFICA 2
           dbc.Col(dcc.Graph(figure=figvac), #config= "autosize"), 
                    width={'size' : "auto", "offset":0}),
               ]),#,justify="center"),
    
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    
# ###################### SECCION 3. MAPA

    dbc.Row([
          dbc.Col(html.H2('Un portafolio diverso',
                        className='card-title',style={'textAlign': 'left',"color": "#91210C"}),
               
                width={ "offset":1 }),
    ]),

      dbc.Row(
           [
           dbc.Col(html.H5(['Hemos recibido vacunas o sustancia activa desde seis paises: Bélica, Argentina, China, India, Rusia y Estados Unidos'
                               ],style={'textAlign': 'left'}),
                       width={'size': 10,  "offset":1 },
                      )],justify="align"),
   # # dbc.Row([dbc.Col(dcc.Graph(figure=aa), 
   #                   style={'width': '100%', 'display': 'inline-block',
   #                         'align': 'center'}),
   #            ]),#,justify="center"),
   
   
    
     dbc.Row([                          #https://github.com/fdealbam/Vacunas/blob/main/application/static/mapa.JPG
               dbc.Col(dbc.CardImg(src=" https://github.com/fdealbam/Vacunas/blob/main/imagenmundi.jpg?raw=true"),
                       #https://github.com/fdealbam/Vacunas/blob/main/imagenmundi.jpg
                      lg={'size': "autosize",  "offset": 1, }),
            
           ]),
    
    
  html.Br(),
    html.Br(),
    html.Br(),
    
     dbc.Row([
        dbc.Col(html.H3('Dosis a envasar',
                        className='card-title',style={'textAlign': 'start'} ),
                style={"color": "#91210C", },
                width={ "offset":1 },),

                
                
    ]),
     dbc.Row(
        [
            dbc.Col(dbc.Table(table_headerDOSISe + table_bodyDOSISe, 
                              bordered=False, 
                              dark=False,
                              hover=True,
                              #responsive=True,
                              striped=True,
                              #size="sm",
                              #style_header={'backgroundColor': 'rgb(30, 30, 30)'},
                              style={
            'margin-top': '9px',
            'margin-left': '60px',
            'width': '409px',
            'height': '46px',
             "font-size": "large"                      
            #'backgroundColor': 'rgba(0,0,0,0)',
            }
                                     )),
            dbc.Col(dcc.Graph(figure=figvacdosis),
                     width={'size' : "auto", "offset":0}),
            
        ]),
      
    
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),

    dbc.Row([
        dbc.Col(html.H3('¿Cuando se habrán recibido las dosis necesarias?',
                        className='card-title',style={'textAlign': 'start'} ),
                style={"color": "#91210C", },
                width={ "offset":1 },),
            ]),
    
    html.Br(),
    html.Br(),
        
    dbc.Row([
        dbc.Col(html.H4("En 100 días se han recibido 30 millones (dosis y sustancia activa) aproximadamente. Así, si se aplica un crecimiento de 20% en ese monto, el día 200 tendríamos 63 millones de dosis, el día 300 tendríamos 98.6 millones, el día 400 tendríamos 133 millones", 
                        className='card-title',style={'textAlign': 'start'} ),
                style={"color": "#91210C", },
                width={ "offset":1 },),
            ]),
        
#    dbc.Row(
#           [dbc.Col(html.H4([query
#                            ],style={'textAlign': 'left'}),
#                       width={'size': 11,  "offset":1 },
#                      )],justify="start"),                
#    ]),
#
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

