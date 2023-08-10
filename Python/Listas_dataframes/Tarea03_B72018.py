from numpy import sort
import numpy
from tomlkit import value
import numpy as np
from statistics import median
import pandas as pd
import datetime
from datetime import timedelta, date
import matplotlib.pyplot as plt

# Asignación(1)

# Función que se encarga de mezclar valores del diccionario y de la lista


def list_dic(a, b):

    # 1.a)
    # Generación de listas
    print("La lista brindada es: ", a)
    print("El diccionario brindado es: ", b)
    # Se crea una variable que es una lista con los valores de b
    list1_dicvalues = list(b.values())
    # Comando sort ordena de menor a mayor
    list2_sumval = sort(a + list1_dicvalues)
    print("-------------------------------------------------------------------")
    print("La lista creada con los valores del diccionario y lista es: ", list2_sumval)
    print("-------------------------------------------------------------------")
    # ////_______________________________________________________________________
    # 1.b)
    # Cálculo de medias
    media_dv = np.mean(numpy.array(list1_dicvalues))
    media_lista = np.mean(numpy.array(a))
    print("-------------------------------------------------------------------")
    print("La media de los valores de diccionario es: ", media_dv)
    print("La media de los valores de la lista es: ", media_lista)
    # ////_______________________________________________________________________

    # Cálculo de desviaciones estandar
    desviacion_dv = np.std(numpy.array(list1_dicvalues))
    desviacion_a = np.std(numpy.array(a))
    print("La desviación estándar de los valores de diccionario es: ", desviacion_dv)
    print("La desviación estándar de los valores de la lista es: ", desviacion_a)

    # Cálculo de medianas
    mediana_dv = median(list1_dicvalues)
    mediana_a = median(a)
    print("La mediana de los valores de diccionario es: ", mediana_dv)
    print("La mediana de los valores de diccionario es: ", mediana_a)
    print("-------------------------------------------------------------------")
    # ////_______________________________________________________________________
    # 1.c)
    # Creación de diccionario con keys de b y valores de lista a
    indice = b.keys()  # Keys del diccionario brindado
    # Se utiliza el comando "zip" para agrupar indice y valor
    diccionario_bk_a = dict(zip(indice, a))
    print("El diccionario que contiene los keys y valores de lista es: ",
          diccionario_bk_a)
    print("-------------------------------------------------------------------")
    # ////_______________________________________________________________________
# //________________________________________________________________________________

# Asignación(2)


def diccionario_to_dataframe(a):
    # 2.a)
    print("El diccionario brindado es: ")
    print("-------------------------------------------------------------------")
    print(a)
    print("-------------------------------------------------------------------")
    # Conversión de diccionario a dataFrame
    df = pd.DataFrame(
        a, index=["est1", "est2", "est3", "est4", "est5", "est6", "est7"])
    print("El diccionario introducido se convierte a tabla(dataframe)")
    print("-------------------------------------------------------------------")
    print(df)
    print("-------------------------------------------------------------------")

    # Conversión de diccionario a dataFrame con indice binario
    df_bi = pd.DataFrame(a, index=[0, 1, 2, 3, 4, 5, 6])
    print("El diccionario introducido se convierte a tabla(dataframe)")
    # ////_______________________________________________________________________

    # 2.c)
    # Ordenar alfabéticamente ascendente A-Z por nombre
    print("Tabla ordenada por nombre ascendentemente")
    print("-------------------------------------------------------------------")
    print(df.sort_values('nombre'))
    print("-------------------------------------------------------------------")
    # ////_______________________________________________________________________

    # 2.d)
    # Ordenar alfabéticamente descendiente Z-A por ciudad
    print("Tabla ordenada por carrera descendientemente")
    print("-------------------------------------------------------------------")
    print(df.sort_values('carrera', ascending=False))
    print("-------------------------------------------------------------------")
    # ////_______________________________________________________________________

    # 2.e)
    # Visualización usando índice binario primer estudiante
    print("Visualizando el primer estudiante por medio del índice binario [0]")
    print(df_bi.loc[0:4])
    # ////_______________________________________________________________________

    # 2.f)
    # Visualización usando indice textual primer estudiante
    print(df_bi.loc['est1':])
    # ////_______________________________________________________________________

    # 2.g)
    # Visualización de estudiantes indice binario 3 solamente datos de carrera y edad
    print(df_bi.loc[3:6])
    # ////_______________________________________________________________________

    # 2.h)
    # Exportar a excel
    print("Exportando dataframe a excel...")
    file_name = "Dataframe.xlsx"
    df.to_excel(file_name)
    print("El dataframe se escribió en un archivo de excel de forma exitosa")
    # ////_______________________________________________________________________
# //________________________________________________________________________________

# Asignación(3)

# Funciones de manejo de archivos csv


def CargarArchivo():

    # Función solicitada para definir columnas como índices
    # Completamente innecesaria porque sirve .set_idex por si solo y hasta se ve mejor

    def ChangeIndex(a):
        a.set_index('fechas', inplace=True)
        a.to_csv("dataframe_index_fechas.csv", header=True, index=True)

    # 3.a)
    # Cargar CSV a dataframe
    df = pd.read_csv("time_series_covid19_confirmed_ready.csv")
    # ////_______________________________________________________________________

    # 3.b)
    # Cambiar indice por medio de función
    ChangeIndex(df)

    # Dataframe generado apartir de función ChangeIndex
    df_f = pd.read_csv("dataframe_index_fechas.csv")
    #df_f.set_index('fechas', inplace=True)
    print(df_f)
    # ////_______________________________________________________________________

    # 3.c)
    # Panama, Uruguay, Costa Rica y España del 01/09/2020 al 25/09/2020

    a = "2020-09-01"
    Panama = df_f[["fechas", "Panama"]]
    Uruguay = df_f[["fechas", "Uruguay"]]
    Costa_Rica = df_f[["fechas", "Costa.Rica"]]
    España = df_f[["fechas", "Spain"]]

    # Contador para creación de dataframes
    cont = 1

    # Creo DataFrame con primer valor

    # Panama
    dt_primera_fecha_Panama = Panama[Panama["fechas"] == a]
    dt_primera_fecha_Panama.to_csv("fechas_casos_Panama.csv", index=False)

    # Uruguay
    dt_primera_fecha_Uruguay = Uruguay[Uruguay["fechas"] == a]
    dt_primera_fecha_Uruguay.to_csv("fechas_casos_Uruguay.csv", index=False)

    # Costa Rica
    dt_primera_fecha_CostaRica = Costa_Rica[Costa_Rica["fechas"] == a]
    dt_primera_fecha_CostaRica.to_csv(
        "fechas_casos_CostaRica.csv", index=False)

    # España
    dt_primera_fecha_España = España[España["fechas"] == a]
    dt_primera_fecha_España.to_csv("fechas_casos_Espana.csv", index=False)

    # Objeto de inicio y formato de fecha
    out = datetime.datetime.strptime(a, "%Y-%m-%d")

    # Ciclo generador de fechas
    while cont <= 24:

        # Generador de fechas por ciclo
        out_plus = out + timedelta(cont)
        fechas = out_plus.strftime("%Y-%m-%d")

        # Panama
        dt_fechas_Panama = Panama[Panama["fechas"] == fechas]
        dt_fechas_Panama.to_csv("fechas_casos_Panama.csv",
                                mode='a', header=False, index=False)

        # Uruguay
        dt_fechas_Uruguay = Uruguay[Uruguay["fechas"] == fechas]
        dt_fechas_Uruguay.to_csv(
            "fechas_casos_Uruguay.csv", mode='a', header=False, index=False)

        # Costa Rica
        dt_fechas_CostaRica = Costa_Rica[Costa_Rica["fechas"] == fechas]
        dt_fechas_CostaRica.to_csv(
            "fechas_casos_CostaRica.csv", mode='a', header=False, index=False)

        # España
        dt_fechas_España = España[España["fechas"] == fechas]
        dt_fechas_España.to_csv("fechas_casos_Espana.csv",
                                mode='a', header=False, index=False)

        cont += 1
        if cont == 24:
            break

    # Datos de paises

        # Panama
    Setiembre_Panama = pd.read_csv("fechas_casos_Panama.csv")
    #Setiembre_Panama.set_index('fechas', inplace=True)
    print(Setiembre_Panama)

    # Uruguay
    Setiembre_Uruguay = pd.read_csv("fechas_casos_Uruguay.csv")
    #Setiembre_Uruguay.set_index('fechas', inplace=True)
    print(Setiembre_Uruguay)

    # Costa Rica
    Setiembre_CostaRica = pd.read_csv("fechas_casos_CostaRica.csv")
    #Setiembre_CostaRica.set_index('fechas', inplace=True)
    print(Setiembre_CostaRica)

    # España
    Setiembre_España = pd.read_csv("fechas_casos_Espana.csv")
    #Setiembre_España.set_index('fechas', inplace=True)
    print(Setiembre_España)
    # ////_______________________________________________________________________

    # 3.d)
    # Gráfico de trazo fijo para Costa Rica

    # Obtener eje
    ax = plt.gca()
    # Se especifica dentro de los parámetos el tipo del gráfico, sus ejes y color
    ax.set_xlim([0, 500])
    ax.set_ylim([0, 3200])
    df_f.plot(kind='line', x='fechas', y='Costa.Rica', color='red', ax=ax)
    plt.show()
    # ////_______________________________________________________________________

    # 3.e)
    # Gráfico de trazo fijo para España, Italia y Francia
    # Obtener eje
    ax = plt.gca()
    # Se especifica dentro de los parámetos el tipo del gráfico, sus ejes y color
    ax.set_xlim([0, 500])
    ax.set_ylim([0, 110000])
    df_f.plot(kind='line', x='fechas', y='Spain', color='blue', ax=ax)
    df_f.plot(kind='line', x='fechas', y='Italy', color='red', ax=ax)
    df_f.plot(kind='line', x='fechas', y='France', color='green', ax=ax)
    plt.show()
    # ////_______________________________________________________________________
# //________________________________________________________________________________________________________________


# Dato brindado para asignación(1): Lista y diccionario de enunciado
d = {0: 20, 1: 320, 2: 90, 3: 147, 4: 122, 5: 717,
     6: 2, 7: 77, 8: 112, 9: 14, 10: 17, 11: 24}
list1 = [13, 2, 104, 36, 9, 120, 29, 500, 89, 41, 65, 7]

# Dato brindado para asignación(2): Diccionario brindado
data = {'nombre': ["Marco", "Francisco", "Roberto", "Mariel", "Sonia", "John", "Charles"],
        'carrera': ["Ing. Eléctrica", "Educacion Física", "Matemáticas", "Ing. Mecánica", "Derecho", "Idiiomas", "Ing. Civil"],
        'Edad': [21, 20, 19, 29, 22, 21, 22]
        }

# Llamado a funciones

# Punto(1)
list_dic(list1, d)
# Punto(2)
diccionario_to_dataframe(data)
# Punto(3)
CargarArchivo()
