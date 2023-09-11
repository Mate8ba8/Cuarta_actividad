from sklearn.linear_model import LinearRegression
from pymongo.mongo_client import MongoClient
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



from pymongo.mongo_client import MongoClient
uri = "mongodb+srv://cagomezj:1234@cluster0.cgumkrz.mongodb.net/?retryWrites=true&w=majority"
    # Create a new client and connect to the server
client = MongoClient(uri)
    # Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    
db = client.actividad4.data_real

data = {
         "Esfuerzo[kN]": 45,
        "Deformacion[mm]": 0.6
    }
db.insert_one(data)
for x in db.find():
        print(x)



data_teorico = pd.read_csv("C:\\Users\\Mateo Bohorquez Angu\\Desktop\\TRABAJOS U DISTRITAL\\Tercer semestre\\Programación II\\Actividad4\\BD\\Data ingeniero.csv")
data_teorico


#Creamos una lista para almacenar los datos
data_list = []
#creamos un bucle con el "for", que itera los datos de la base de datos db que creamos antes
for data_real_bd in db.find():
    data_list.append(data_real_bd)#En cada iteración del bucle, los datos recuperados se agregan a la lista

#creamos un dataframe en pandas con los datos de la lista, para poder trabajar con ellos de manera más sencilla
data_real = pd.DataFrame(data_list)
data_real_fit = data_real#creamos una copia del dataframe
X = data_real_fit['Esfuerzo[kN]'].values.reshape(-1, 1)#creamos una matriz con los datos de esfuerzo del dataframe y los organizamos en una columna
y = data_real_fit['Deformacion[mm]'].values.reshape(-1, 1)#creamos una matriz con los datos de deformación del dataframe y los organizamos en una columna
x_lim = data_real['Esfuerzo[kN]'].iloc[-1]#establecemos el limite del eje x con el úlitmo valor de esfuerzo
y_lim = data_real['Deformacion[mm]'].iloc[-1]#establecemos el limite del eje y con el último valor de deformación
model = LinearRegression()#creamos el modelo de regresion lineal
model.fit(X, y)#ajustamos el modelo a los datos de "X" y "y"
prediction = round(model.predict(np.array([3000]).reshape(-1, 1))[0][0],1)#realizamos una predicción con el modelo entrenado, para una carga de 3000 kN

