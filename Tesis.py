import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

path='C:/Users/Pelusa/Google Drive/Semestre 2022-0/Tesis/Gráficos'
os.chdir(path)
df= pd.read_excel('Precios.xlsx')
df.columns
'''
serie_1 = [406, 387, 442, 457, 485]
serie_2 = [421, 453, 435, 478, 512]
 
 
numero_de_grupos = len(serie_1)
indice_barras = np.arange(numero_de_grupos) # me genera 
ancho_barras =0.35
 
plt.bar(indice_barras, serie_1, width=ancho_barras, label='Hombres')
plt.bar(indice_barras + ancho_barras, serie_2, width=ancho_barras, label='Mujeres')
plt.legend(loc='best')
## Se colocan los indicadores en el eje x
plt.xticks(indice_barras + ancho_barras, ('2017', '2018', '2019', '2020','2021'))
 
plt.ylabel('Numero de habitantes')
plt.xlabel('Año')
plt.title('Numero de habitantes por genero')
 
plt.show()


serie1 = df['2018(huayro)']
serie2 = df['2019(huayro)']
serie3 = df['2020(huayro)']
meses=['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
                                          'Julio', 'Agosto', 'Setiembre', 'Octubre', 'Noviembre', 'Diciembre']
 
numero_de_grupos = len(serie1)
indice_barras = np.arange(numero_de_grupos) # me genera 
ancho_barras =0.2

plt.figure(figsize=(15,8), constrained_layout=True) 
plt.bar(indice_barras, serie1, width=ancho_barras, label='2018')
plt.bar(indice_barras + ancho_barras, serie2, width=ancho_barras, label='2019')
plt.bar(indice_barras + 2*ancho_barras, serie3, width=ancho_barras, label='2020')

plt.legend(loc='best')
## Se colocan los indicadores en el eje x
plt.xticks(indice_barras + ancho_barras, ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
                                          'Julio', 'Agosto', 'Setiembre', 'Octubre', 'Noviembre', 'Diciembre'))
 
plt.ylabel('Precio (S/.)')
plt.xlabel('Mes')
plt.title('Precio promedio mensual (soles por Kg) de la papa Huayro')
plt.show()
plt.savefig('my_plot.png')
# OTRA FORMA

anio= [2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]
pobreza=[58.7,55.6,49.1,42.4,37.3,33.5,30.8,27.8,25.8,23.9,22.7,21.8,20.7,21.7,20.5,20.2,30.1]

plt.plot(anio,pobreza) #Muestra que vas a dibujar y como 
plt.show() #Muestra el grafico final
'''

# GRÁFICA LÍNEAS PAPA HUAYRO
serie1 = df['2018(huayro)']
serie2 = df['2019(huayro)']
serie3 = df['2020(huayro)']
meses=['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
                                          'Julio', 'Agosto', 'Setiembre', 'Octubre', 'Noviembre', 'Diciembre']
 
plt.figure(figsize=(15,8), constrained_layout=True) 
plt.plot(meses,serie1, label='2018', marker = 'o')
plt.plot(meses,serie2, label='2019', marker = 'o')
plt.plot(meses,serie3, label='2020',marker = 'o')

plt.legend(loc='best')
## Se colocan los indicadores en el eje x
 
plt.ylabel('Precio (S/.)')
plt.xlabel('Mes')
plt.title('Precio promedio mensual (soles por Kg) de la papa huayro')
plt.show()

# GRÁFICA LÍNEAS PAPA BLANCA
serie4 = df['2018(blanca)']
serie5 = df['2019(blanca)']
serie6 = df['2020(blanca)']

plt.figure(figsize=(15,8), constrained_layout=True) 
plt.plot(meses,serie4, label='2018',marker = 'o')
plt.plot(meses,serie5, label='2019', marker = 'o')
plt.plot(meses,serie6, label='2020', marker = 'o')

plt.legend(loc='best')
## Se colocan los indicadores en el eje x
 
plt.ylabel('Precio (S/.)')
plt.xlabel('Mes')
plt.title('Precio promedio mensual (soles por Kg) de la papa blanca')
plt.show()
