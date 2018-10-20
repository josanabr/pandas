import pandas as pd
import time

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
list_labels = ['age', 'workclass', 'fnlwgt', 'education', 'education_num', 'marital_status', 'occupation', 'relationship', 'race', 'sex', 'capital_gain', 'capital_loss', 'hours_per_week', 'native_country', 'income']
start = time.time()
print("Leyendo archivo CSV desde %s"%(url))
c = pd.read_csv(url, header = None, names = list_labels)
print("Imprimiendo encabezado")
c.head(5)
print(type(c))
print("Caracteristicas del data frame")
print(c.shape)
print("Informacion del data frame")
print(c.info())
end = time.time()
print("Tiempo en segundos: %s"%(end - start))
list(c) # imprime las etiquetas de las columnas
x = c[['age','capital_gain','hours_per_week']] # retr. particular cols
x.count() # arroja agregados
x.sum() # arroja la suma de todos los registros
x[x.age <= 40] # muestra solo los registros con age <= 40
x[x.age <= 40].count() # cuenta el numero de records y edad <= 40
x.age[ x.age <= 40 ] # lo mismo que lo anterior 
x[x.age <= 40].capital_gain.sum() # record <= 40, y suma capital_gain
x[x.age <= 40][['capital_gain']].sum() # lo mismo que el anterior
# otros agregados, min, max, mean, median

