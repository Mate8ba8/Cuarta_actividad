import matplotlib.pyplot as plt
from BD.baseDatos import *
from grafica.grafica import *
from prediccion.prediccion import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



from grafica.grafica import data_teo
data_teo()
plt.show

from grafica.grafica import gr_con_prediccion
gr_con_prediccion(4,5)

from prediccion.prediccion import gr_con_prediccion_3000
gr_con_prediccion_3000()

from prediccion.prediccion import gr_sin_prediccion
gr_sin_prediccion()

from grafica.grafica import predic_calculo
predic_calculo()

print('la predicción a 3000 kN es de: ', prediction ,'mm')#imprimimos el resultado