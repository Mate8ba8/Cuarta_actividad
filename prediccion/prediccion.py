from BD.baseDatos import *
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas as pd

#creamos la funcion con la predicción de deformación a 3000 kN
def gr_con_prediccion_3000(prediction):
  plt.figure(figsize=(15, 6))#definimos tamaño del grafico
  plt.plot(	data_teorico['Esfuerzo[kN]'] , data_teorico['Deformacion[mm]'])#trazamos la linea de los datos teoricos
  plt.scatter(	db['Esfuerzo[kN]'] , db['Deformacion[mm]'], color='red')#graficamos los puntos de la data real en rojo
  plt.plot(np.linspace(0,1000).reshape(-1,1),model.predict(np.linspace(0,1000).reshape(-1,1)),'m')#creamos la linea de predicción y la agregamos al grafico
  plt.scatter(	3000 , prediction, color='green')#agregamos la prediciond e la deformación a 3000 kN
  plt.xlabel('Esfuerzo [kN]')#etiqueta del eje x
  plt.ylabel('Deformación [mm]')#etiqueta del eje y
  plt.title('Gráfica 3: Predicción a una carga de 3000 kN')#titulo del grafico
  plt.xlim(0, 3000)#limite del eje x del grafico
  plt.ylim(0, 45)#limite del eje y del grafico
  plt.grid()#agregamos la grilla
  plt.gca().invert_yaxis()#invertimos el eje "y", ubicando los valores de forma descendente

#creamos la funcion de los datos sin predicción
def gr_sin_prediccion():
  plt.figure(figsize=(15, 6))#definimos tamaño del grafico
  plt.plot(	data_teorico['Esfuerzo[kN]'] , data_teorico['Deformacion[mm]'])#trazamos la linea de los datos teoricos
  plt.scatter(	db['Esfuerzo[kN]'] , db['Deformacion[mm]'], color='red')#graficamos los puntos de la data real en rojo
  plt.xlabel('Esfuerzo [kN]')#etiqueta del eje x
  plt.ylabel('Deformación [mm]')#etiqueta del eje y
  plt.title('Gráfica 1: teórico versus real')#titulo del grafico
  plt.grid()#agregamos la grilla
  plt.gca().invert_yaxis()#invertimos el eje "y", ubicando los valores de forma descendente