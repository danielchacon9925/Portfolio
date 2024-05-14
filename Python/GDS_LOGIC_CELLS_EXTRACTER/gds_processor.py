##########################################
######  Procesador de datos de GDS  ######
##########################################

#   Importa archivo designs/---/runs/---/results/final/gds
#   Se busca extraer coordenadas de polígonos

# Documentation

# General 
# https://gdspy.readthedocs.io/en/stable/

# Librería: buscar información de gdspy.Cell()
# https://gdspy.readthedocs.io/en/stable/reference.html

###########################
##  Librerías utilizadas ##
###########################


import numpy as np
import gdspy

#######################
#   Importación de GDS#
#######################

# Open the GDS file

gds_file = gdspy.GdsLibrary()
gdsii=gds_file.read_gds('picorv32.gds')


#######################
# Lista de estructuras#
#######################


# Structure names in library given
#structure_names = [cell for cell in gdsii.cells]

# Print the list of structure names
#print("Available structure names in the GDS file:")
#for name in structure_names:
#    print(name)


##############################
# Análisis de celda principal#
##############################

# El atributo top_level() busca la celda del tope de la herarquía.
# Se encuentra en el top la que no se referencia por ningún celda.

main_cell = gdsii.top_level()[0]  # Assume a single top level cell

# Puntos de polígono top

points = main_cell.polygons[0].polygons[0]

area_polygon=float(main_cell.polygons[0].area(by_spec=False))
#####################################
# Lista de labels en celda principal#
#####################################


# Print the list of polygons
#print("Lista de labels")
#print("Available structure names in the GDS file:")
#for name in main_cell.labels:
#    print(name)

##############################################
# Exploración de atributos de celda principal#
##############################################

'''
print("--------------Exploración de atributos de celdas--------------")

print("Main cell: ",main_cell)

print("Nombre de libería: ", main_cell.name)

print("La cantidad de polígonos son: ", len(main_cell.polygons))

print("Datos de polígono posición inicial[0]: ", main_cell.polygons[0])

print("--- Puntos del polígono top ---")
print(points)

print("La cantidad de labels son: ", len(main_cell.labels))

print("Area de polígono top: ", area_polygon)

print("El ancho de el recuadro de área utilizada es: ", np.sqrt(area_polygon))

print("La letra 3 dentro del picorv32a: ", main_cell.name[2] )

print("Labels de polígono top: ", main_cell.labels[0]," en este label se puede observar el nombre")
print("Labels de polígono 1: ", main_cell.labels[1])
print("Labels de polígono 2: ", main_cell.labels[2])

print("Layer contenidos dentro de picorv32a: ", main_cell.get_layers())

#print("References en main cell: ",main_cell.references)

#print("Impresión de polígonos")
#print("Polígonos en ésta celda: ", main_cell.get_polygons(by_spec=False, depth=None))
print("--------------------------------------------------------------")

'''

print("---------------------------------Tipo de datos---------------------------------")

print("Tipo de dato del main cell: ", type(main_cell))

print("Tipo de datos del polígono: ", type(main_cell.polygons))

print("Tipo de dato del polígono en posición inicial: ",type(main_cell.polygons[0]))

print("Tipo de dato de los labels: ", type(main_cell.labels))

print("Tipo de dato del área: ",type(main_cell.polygons[0].area(by_spec=True)))

print("Tipo de dato de área ",type(area_polygon))

print("Tipo de dato de label de polígono top: ", type(main_cell.labels[0]))

print("Tipo de dato de layers contenidos dentro de picorv32a: ", type(main_cell.get_layers()))

print("Tipo de dato de los references del main cell: ", type(main_cell.references))

print("El tipo de dato de los puntos es: ", type(points))

print("La longitud del array es: ", len(points))

print("Posición 1 del array: ", points[0])

print("Tipo de dato array 1: ", type(points[0]))

print("-------------------------------------------------------------------------------")


############
# Funciones#
############

def extraer_coordenadas_X_Y(array):
    # Inicializa las variables para el ancho y el alto con valores mínimos posibles
    # -float('inf') indica que cualquier valor en array será mayor
    ancho_maximo = -float('inf')
    alto_maximo = -float('inf')
    
    # Itera sobre las coordenadas en el array para encontrar los máximos
    for coordenada in array:
        # Se asume que coordenada[x,y]
        x, y = coordenada
        if x > ancho_maximo:
            ancho_maximo = x
        if y > alto_maximo:
            alto_maximo = y
    
    # Devuelve los valores máximos de x e y como un array de NumPy
    return np.array([ancho_maximo, alto_maximo])

def extraer_coordenadas_2X_2Y(array):
    # Inicializa las variables para el ancho y el alto con valores máximos y mínimos posibles
    ancho_maximo = -float('inf')
    alto_maximo = -float('inf')
    ancho_minimo = float('inf')
    alto_minimo = float('inf')
    
    # Itera sobre las coordenadas en el array para encontrar los máximos y mínimos
    for coordenada in array:
        # Se asume que coordenada[x, y]
        x, y = coordenada
        if x > ancho_maximo:
            ancho_maximo = x
        if y > alto_maximo:
            alto_maximo = y
        if x < ancho_minimo:
            ancho_minimo = x
        if y < alto_minimo:
            alto_minimo = y
    
    # Devuelve los valores máximos y mínimos de x e y como un array de NumPy
    return np.array([ancho_maximo, alto_maximo, ancho_minimo, alto_minimo])

def generar_matrix(ancho,alto,resolucion):

    # Crear una matriz vacía con la resolución deseada
    matriz = np.zeros((resolucion*int(ancho), resolucion*int(alto)))

    return matriz

def llenar_matriz(matriz, coordenadas):
    alto, ancho = len(matriz), len(matriz[0])
    
    for x, y in coordenadas:
        x, y = round(x), round(y)  # Redondear las coordenadas a los enteros más cercanos
        if 0 <= x < ancho and 0 <= y < alto:
            matriz[x][y] = 1
            return matriz
        else:
            print(f"Coordenadas ({x}, {y}) están fuera de los límites de la matriz.")


def encontrar_celdas_ocupadas(matriz):
    ocupadas = []  # Lista para almacenar las coordenadas de las celdas ocupadas

    # Obtener las dimensiones de la matriz
    filas, columnas = matriz.shape

    # Iterar sobre la matriz para encontrar celdas ocupadas
    for fila in range(filas):
        for columna in range(columnas):
            if matriz[fila, columna] == 1:
                ocupadas.append((fila, columna))
    #print("Posiciones ocupadas: ",ocupadas)
    return ocupadas

def imprimir_matriz(matriz):
    for fila in matriz:
        for valor in fila:
            print(valor, end=" ")  # Imprime el valor seguido de un espacio en la misma línea
        print()  # Salto de línea al final de cada fila


def calculate_occupancy(array, coordinates):
    total_cells = len(array) * len(array[0])
    occupied_cells = 0

    for coord in coordinates:
        x, y = int(coord[0]), int(coord[1])  # Convertir los valores flotantes a enteros
        if 0 <= x < len(array) and 0 <= y < len(array[0]):
            if array[x][y] != 0:  # Ajusta esta condición según la representación de ocupación en el array
                occupied_cells += 1

    occupancy_percentage = (occupied_cells / total_cells) * 100
    print(occupancy_percentage)
    return occupancy_percentage

# Ejemplo de uso
# array = [[0] * 1000 for _ in range(1000)]  # Ejemplo de un array de 1000x1000 inicializado con ceros
# coordinates = [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]  # Reemplaza con tus propias coordenadas
# occupancy = calculate_occupancy(array, coordinates)
# print(f"Porcentaje de ocupación: {occupancy}%")


print("------------------------TESTING FUNCTIONS------------------------")

print("Recuadro: ", main_cell.polygons[1].polygons[0])

print("Type recuadro: ", type(main_cell.polygons[1].polygons[0]))


coordenadas_picorv32a=extraer_coordenadas_X_Y(points)

print("Las coordenadas del picorv32a son: ", coordenadas_picorv32a)

ancho_picorv32a=coordenadas_picorv32a[0]

alto_picorv32a=coordenadas_picorv32a[1]

print("El ancho es: ", ancho_picorv32a)

print("El alto es: ", alto_picorv32a)

resolucion=1000

#matriz_principal=generar_matrix(ancho_picorv32a,alto_picorv32a,resolucion)

matriz_principal=generar_matrix(1,1,resolucion)

print("Matriz principal: ",matriz_principal)

print("Tipo matriz principal: ",type(matriz_principal))

print("Longitud de matriz principal: ", len(matriz_principal))

#ocupacion=calculate_occupancy(matriz_principal, coordinates)


#matriz_principal_ocupada=llenar_matriz(matriz_principal, main_cell.polygons[1].polygons[0])

#print("Matriz ocupada: ", matriz_principal_ocupada)

#ocupacion=encontrar_celdas_ocupadas(matriz_principal_ocupada)

#matriz_con_ocupaciones=imprimir_matriz(matriz_principal_ocupada)
matriz_principal_ocupada_68=calculate_occupancy(matriz_principal, main_cell.polygons[1].polygons[0])

#################################################
# Extracción de polígonos de metales  (layer 68)#
#################################################

print("--------------------Comandos de prueba--------------------")
print("Layers y sus polígonos: ",  main_cell.polygons[1].layers[0])
print("Type layers y sus polígonos: ",  type(main_cell.polygons[1].layers[0]))
print("Layers y sus polígonos: ",  main_cell.polygons[1].properties)
print("----------------------------------------------------------")


count_polygons_metal_1=0
count_polygons_metal_2=0
count_polygons_metal_3=0
count_polygons_metal_4=0
count_polygons_metal_5=0


for i in range(len(main_cell.polygons)):

    # Polígonos en metal 1
    if main_cell.polygons[i].layers[0]==68:
        count_polygons_metal_1 += 1

        #matriz_principal_ocupada_68=calculate_occupancy(matriz_principal, main_cell.polygons[i].polygons[0])

        #ocupacion_68=encontrar_celdas_ocupadas(matriz_principal_ocupada_68)

        #print("Polígono ubicado en metal 1: ", main_cell.polygons[i])
        #print("Polígono ubicado en metal 1: ", main_cell.polygons[i].polygons[0])
    
    # Polígonos en metal 2
    elif main_cell.polygons[i].layers[0]==69:
        count_polygons_metal_2 += 1
        #print("Polígono ubicado en metal 1: ", main_cell.polygons[i])
        #print("Polígono ubicado en metal 1: ", main_cell.polygons[i].polygons[0])
    
    # Polígonos en metal 3
    elif main_cell.polygons[i].layers[0]==70:
        count_polygons_metal_3 += 1
        #print("Polígono ubicado en metal 1: ", main_cell.polygons[i])
        #print("Polígono ubicado en metal 1: ", main_cell.polygons[i].polygons[0])

    # Polígonos en metal 3
    elif main_cell.polygons[i].layers[0]==71:
        count_polygons_metal_4 += 1
        #print("Polígono ubicado en metal 1: ", main_cell.polygons[i])
        #print("Polígono ubicado en metal 1: ", main_cell.polygons[i].polygons[0])

    # Polígonos en metal 3
    elif main_cell.polygons[i].layers[0]==72:
        count_polygons_metal_5 += 1
        #print("Polígono ubicado en metal 1: ", main_cell.polygons[i])
        #print("Polígono ubicado en metal 1: ", main_cell.polygons[i].polygons[0])

#print("Matriz ocupada: ", matriz_principal_ocupada_68)
#print("Ocupación del metal 1: ", ocupacion_68)

print("Cantidad de polígonos en metal 1: ",count_polygons_metal_1)
print("Cantidad de polígonos en metal 2: ",count_polygons_metal_2)
print("Cantidad de polígonos en metal 3: ",count_polygons_metal_3)
print("Cantidad de polígonos en metal 4: ",count_polygons_metal_4)
print("Cantidad de polígonos en metal 5: ",count_polygons_metal_5)


        
