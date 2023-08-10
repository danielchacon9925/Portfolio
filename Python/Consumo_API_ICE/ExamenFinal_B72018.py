# Examen Final-Daniel Chacón Mora-B72018

# /////////////////////////////////////////////////////////////////////////////////////////////////////////
# Parte 1: Conformación de datos

# 1)

# Carga de librerías
import numpy as np
import pandas as pd
import prince
import os

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import dendrogram, ward, single, complete, average, linkage, fcluster
from scipy.spatial.distance import pdist

import datetime
# from datetime import timedelta
# from datetime import _IsoCalendarDate
# //_________________________________________________________________________________________

# 2)
# Carga de archivo principal: EnergíaMensualHorariaPlantasSEN_9_2022.csv

# Dataframe Tabla
Filename = "EnergíaMensualHorariaPlantasSEN_9_2022.csv"
Tabla = pd.read_csv(Filename)


# 2.a)
# Convertir columna de string a datetime
Tabla["Fechas"] = pd.to_datetime(Tabla["Fechas"])

# Se asignan fechas como índice
Tabla.set_index('Fechas', inplace=True)
# //______________________________________________

# 2.b)
# Se imprime Tabla principal
print(Tabla)
# //______________________________________________

# 2.c)
# Se copia Tabla a Tabla_caso1
Tabla_caso1 = Tabla

# 3)
# Se crea columna nueva Semanaldx
Tabla_caso1['SemanaIdx'] = Tabla_caso1.index.isocalendar().week

# Se crea columna nueva Dialdx
Tabla_caso1['DiaIdx'] = Tabla_caso1.index.isocalendar().day

print(Tabla_caso1)
# //_________________________________________________________________________________________

# 4)

# 4.a)
# Arreglo de enteros
indice_semanas = Tabla_caso1.SemanaIdx.unique()
print(indice_semanas)
# //______________________________________________

# 4.b)
# Parámetros a utilizar
SemanaA = 1
SemanaB = 3

print("La semana número {} (A) del mes de su examen corresponde a la semana número {} del año".format(
    SemanaA, indice_semanas[SemanaA-1]))

Tabla_caso1_parte2 = Tabla_caso1[Tabla_caso1['SemanaIdx']
                                 == indice_semanas[SemanaA-1]]
print(Tabla_caso1_parte2)

print("La semana número {} (B) del mes de su examen corresponde a la semana número {} del año".format(
    SemanaB, indice_semanas[SemanaB-1]))
Tabla_caso1_parte3 = Tabla_caso1[Tabla_caso1['SemanaIdx']
                                 == indice_semanas[SemanaB-1]]
print(Tabla_caso1_parte3)

# /////////////////////////////////////////////////////////////////////////////////////////////////////////

# Parte 2: Análisis de datos con plantas de generación como variables

# 1.a.1)
# En la parte anterior habían sido separados lso dataframes. Se copian a nueva variable
Tabla_caso2_semanaA = Tabla_caso1_parte2
del Tabla_caso2_semanaA['SemanaIdx']
print(Tabla_caso2_semanaA)
Tabla_caso2_semanaB = Tabla_caso1_parte3
del Tabla_caso2_semanaB['SemanaIdx']
print(Tabla_caso2_semanaB)
# //______________________________________________

# 1.a.2)
# Días laborales de la semana
dias_laborales = Tabla_caso2_semanaB.apply(
    lambda x: True if (x.DiaIdx in [1, 2, 3, 4, 5]) else False, axis=1)
# Se elimina columna DiaIdx
Tabla_caso2_semanaB = Tabla_caso2_semanaB[dias_laborales].drop(
    ["DiaIdx"], axis=1, inplace=False)
print("Tabla_caso2_semanaB con dias laborales y columna DiaIdx menos")
print(Tabla_caso2_semanaB)

# Se elimina DiaIdx de Tabla_caso2_semanaA
del Tabla_caso2_semanaA['DiaIdx']
print("Tabla caso2_SemanaA con DiaIDx menos")
print(Tabla_caso2_semanaA)
# //______________________________________________

# 2)
# Analisis de H Clustering usando método "Ward" a partir de Tabla_caso2_semanaA
grupos = fcluster(linkage(pdist(Tabla_caso2_semanaA),
                  method='ward'), 4, criterion='maxclust')
print(grupos)

# 2.b)
Tabla_caso2_semanaA_ext = Tabla_caso2_semanaA.copy()
Tabla_caso2_semanaA_ext["cluster"] = grupos

centros = Tabla_caso2_semanaA_ext.groupby("cluster").mean()
print(centros)

# 2.c)

# Plotea Centro 1
y = centros.iloc[0].tolist()

N = len(y)

x = range(N)

width = 1/1.5
colores_1 = ['#CF8EF8', '#523C81', '#D2D132', '#59C951', '#E5826C']
null = plt.bar(x, y, width, color=colores_1)
null = plt.xticks(range(centros.shape[1]),
                  centros.columns, rotation=90, size=6)
plt.show()

plt.close()


# Plotea Centro 2
y = centros.iloc[2].tolist()

N = len(y)

x = range(N)

width = 1/1.5
colores_1 = ['#CF8EF8', '#523C81', '#D2D132', '#59C951', '#E5826C']
null = plt.bar(x, y, width, color=colores_1)
null = plt.xticks(range(centros.shape[1]),
                  centros.columns, rotation=90, size=6)
plt.show()

plt.close()

# Plotea Centro 3
y = centros.iloc[0].tolist()

N = len(y)

x = range(N)

width = 1/1.5
colores_1 = ['#CF8EF8', '#523C81', '#D2D132', '#59C951', '#E5826C']
null = plt.bar(x, y, width, color=colores_1)
null = plt.xticks(range(centros.shape[1]),
                  centros.columns, rotation=90, size=6)
plt.show()

plt.close()

# Plotea Centro 4
y = centros.iloc[3].tolist()

N = len(y)

x = range(N)

width = 1/1.5
colores_1 = ['#CF8EF8', '#523C81', '#D2D132', '#59C951', '#E5826C']
null = plt.bar(x, y, width, color=colores_1)
null = plt.xticks(range(centros.shape[1]),
                  centros.columns, rotation=90, size=6)
plt.show()

plt.close()

# //////////////////////////////////////////////////////////////////////////////
# ////////////////////---------------OBSERVACIONES---------------///////////////
# //////////////////////////////////////////////////////////////////////////////
# ///////               Comentario sobre lo obtenido        ////////////////////
# //// Se observan datos negativos en Intercambio Norte, lo cuál indica que ////
# //// para este cluster, su centro se parece más a otro cluster que a si   ////
# //// lo cuál muestra como sus datos cada vez se parecen menos entre ellos ////
# //////////////////////////////////////////////////////////////////////////////

# /////////////////////////////////////////////////////////////////////////////////////////////////////////

# Parte 3: Análisis de datos detallados con plantas de generación como observaciones

# Se copia contenido de Tabla_caso2_semanaA a Tabla_caso3
Tabla_caso3 = Tabla_caso2_semanaA.copy()

# Tabla_caso3 traspuesta
Tabla_caso3 = Tabla_caso3.T
print(Tabla_caso3)

# Análisis de K medias a partir de datos contenidos en Tabla_caso3 para cuatro grupos

# 4.a) Presenta los clusters restantes con el decorador labels_ y centros estudiantiles
kmeans2 = KMeans(n_clusters=4)
kmeans2.fit(Tabla_caso3.values)

# labels
cluster2 = kmeans2.labels_
print(cluster2)

# centros
centros2 = np.array(kmeans2.cluster_centers_)
print(centros2)

# 4.b)

# Gráfico lineal con los trazos de 4 centros
null = plt.plot(Tabla_caso3.columns, centros2[0])
null = plt.plot(Tabla_caso3.columns, centros2[1])
null = plt.plot(Tabla_caso3.columns, centros2[2])
null = plt.plot(Tabla_caso3.columns, centros2[3])
null = plt.xticks(rotation=90)
plt.show()

# Se cierra plot
plt.close()

# 4.c)

# Lista de las plantas que corresponden a cada cluster


Tabla_caso3_ext = Tabla_caso3.copy()
Tabla_caso3_ext["cluster"] = cluster2

print("Plantas de generación en grupo 1")
print(Tabla_caso3_ext.index[Tabla_caso3_ext["cluster"] == 0].tolist())

print("Plantas de generación en grupo 2")
print(Tabla_caso3_ext.index[Tabla_caso3_ext["cluster"] == 1].tolist())

print("Plantas de generación en grupo 3")
print(Tabla_caso3_ext.index[Tabla_caso3_ext["cluster"] == 2].tolist())

print("Plantas de generación en grupo 4")
print(Tabla_caso3_ext.index[Tabla_caso3_ext["cluster"] == 3].tolist())

# 5)

# Dendograma

# Clustering Jerarquico
ward_res = ward(Tabla_caso3_ext)  # Ward

# Dentograma
null = dendrogram(ward_res, color_threshold=3, labels=Tabla_caso3_ext.index.tolist(
), leaf_rotation=30, leaf_font_size=5)
ax = plt.gca()
limites = ax.get_xbound()

ax.plot(limites, [60, 60], '--', c='k')
ax.text(limites[1], 60, ' dos clústeres', va='center', fontdict={'size': 8})

ax.plot(limites, [40, 40], '--', c='k')
ax.text(limites[1], 40, ' tres clústeres', va='center', fontdict={'size': 8})

ax.plot(limites, [30, 30], '--', c='k')
ax.text(limites[1], 30, ' cuatro clústeres', va='center', fontdict={'size': 8})

plt.show()
plt.close()

# 6)

# Análisis ACP

# 6.a)

# Análisis por componentes principales sobre el dataframe Tabla_caso3 para 3 grupos
pca = prince.PCA(n_components=2, n_iter=0, rescale_with_mean=True,
                 rescale_with_std=True, copy=True, check_input=True, engine='auto', random_state=42)
pca = pca.fit(Tabla_caso3.values)
transformacion = pca.transform(Tabla_caso3.values)
print(transformacion)

# 6.b)

# Gráfico de posiciones de la plantas de generación

y = pd.Series(cluster2).map(
    {0: 'Grupo1', 1: 'Grupo2', 2: 'Grupo3', 3: 'Grupo4'})

ax = pca.plot_row_coordinates(Tabla_caso3, ax=None, figsize=(15, 15), x_component=0, y_component=1,
                              labels=Tabla_caso3.index, color_labels=y, ellipse_outline=False, ellipse_fill=False, show_points=True)
plt.show()

plt.close()

# 6.c)

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////--COMPARACIÓN ACP/DENDOGRAMA--/////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# //// El dendograma permite observar el nivel de similitud entre los diferentes grupos. Se puede ver como 3 grupos guardan/////
# //// similutud entre ellos, algunos con un nivel mayor y otro menos pero tanto en el ACP como en dendograma se observa   /////
# //// como "Itercambio norte" siempre se mantiene en un extremo alejado de los demás, esto porque es el que tiene la mayor/////
# //// diferencia con respecto a las otras plantas de generación eléctrica del país.                                       /////
# ////                                                                                                                     /////
# //// El ACP se emplea en el análisis exploratorio de datos, como una de las técnicas de minería para identificar         /////
# //// agrupaciones de variables, a partir de los cuales se pueden construir modelos predictivos. En ACP se hace el cálculo/////
# //// y la descomposición en autovalores de la matriz de covarianza, y normalmente se hace tras centrar los datos en la   /////
# //// media de cada atributo.El gráfico ACP muestra de una forma más clara la similitud por medio de agrupación de los    /////
# //// diferentes grupos de los datos analizados.                                                                          /////                                                                                            /////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# /////////////////////////////////////////////////////////////////////////////////////////////////////////
