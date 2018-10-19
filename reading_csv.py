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
