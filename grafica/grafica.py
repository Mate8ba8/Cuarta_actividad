#graficamos la data del ingeniero, definimos los nombres de los ejes de la grafica , el titulo, etc.
from BD.baseDatos import *
from prediccion.prediccion import *
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def data_teo():
    data_teorico = pd.read_csv("C:\\Users\\Mateo Bohorquez Angu\\Desktop\\TRABAJOS U DISTRITAL\\Tercer semestre\\Programación II\\Actividad4\\BD\\Data ingeniero.CSV")
    plt.plot(	data_teorico['Esfuerzo[kN]'] , data_teorico['Deformacion[mm]'])
    plt.xlabel('Esfuerzo [kN]')
    plt.ylabel('Deformación [mm]')
    plt.title('Asentamiento inmediato')
    plt.grid()
    plt.gca().invert_yaxis()


# utilizamos esta funcion para crear la grafica que compara los datos teoricos con los reales
def gr_con_prediccion(x_lim,y_lim):
  plt.figure(figsize=(15, 6))#definimos tamaño del grafico
  plt.plot(	data_teorico['Esfuerzo[kN]'] , data_teorico['Deformacion[mm]'])#trazamos la linea de los datos teoricos
  plt.scatter(	db['Esfuerzo[kN]'] , db['Deformacion[mm]'], color='red')#graficamos los puntos en rojo
  plt.xlabel('Esfuerzo [kN]')#etiqueta del eje x
  plt.ylabel('Deformación [mm]')#etiqueta del eje y
  plt.title('Gráfica 2: teórico versus real [ZOOM]')#titulo del grafico
  plt.xlim(0, x_lim)#limite del eje x del grafico
  plt.ylim(0, y_lim)#limite del eje y del grafico
  plt.grid()#agregamos la grilla
  plt.gca().invert_yaxis()#invertimos el eje "y", ubicando los valores de forma descendente



def predic_calculo():
# creamos los gráficos utilizando los datos y predicciones calculados anteriormente con las funciones que creamos antes
    gr_sin_prediccion()
    gr_con_prediccion(x_lim,y_lim)
    gr_con_prediccion_3000(prediction)
