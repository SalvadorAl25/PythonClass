import pandas as pd
import random

# los datos que se manejaran en este ejemplo sera con un archivo CSV

df = pd.read_csv("dataset.csv", index_col="id")

df.head()  #pandas solo te muestras las 5 primeras filas de la tabla
df.tail()    #pandas solo te muestra las 5 ultimas filas de la tabla y se puede redefinir enviandole el numero en elparametro 
df.describe()  #te permite sacar calculos estadisticos dentro del dataframe, devolvera estadistica descriptiva del df original

#--------------------Limpiza de datos
# hay una manera de limpiar el df de espacios con NaN
df.dropna()
# hay otra alternativa que es remplazar un dato con ese NaN
df_filtrado = df.fillna(0)
df_filtrado.head()
# algo ya mas especifico sera
df.filtrado = df.fillna({"retweets": 0, "mentions": -1})
df_filtrado.head()

#------------Filtrados
df["favorites"] # ---> por columnas
df[["favorites","full_text"]] #----> trae por multiples columnas

# traer un rango de filas 
df.iloc[0:3]  #---> traera las primeras 3 filas
df.iloc[0,1,3,4,6] #----> trae filas especificas
df.loc[183721,183723]  #---> trae por identificador

df.loc[[183721,183723], ["favorites","full_text"]]

# traer filtrado por condicion
df[df["favorites"] > 400]
df[(df["favorites"] > 400) & (df["mentions"]>20)]
df[df["full_text"].str.contains("Programming")]

#-------------------transformacion

def calcularGanancias(retweets):
    ganancia = retweets * random.randint(3,5)
    return ganancia

df["ganancias"] = df["retweets"].apply(calcularGanancias)

def popularidad(fila):
    res = fila["followees"]/fila["followers"]
    return res

df["popularidad"] = df.apply(popularidad,axis=1)


# print(df) 