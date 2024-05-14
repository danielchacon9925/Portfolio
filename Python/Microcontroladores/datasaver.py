import serial

baud = 9600

# Crear el archivo CSV y cerrarlo inmediatamente
file_path = "datos.csv"
with open(file_path, 'w') as file:
    pass

print("Se creó el archivo CSV")

# Establecer la comunicación con Arduino en el puerto ttyS1
ser = serial.Serial("/tmp/ttyS1", baudrate=baud, timeout=1)

# Imprimir un mensaje indicando el puerto al que se ha conectado
print("Puerto conectado: " + ser.portstr)
print("Conexión exitosa")

# Abrir el archivo CSV para escritura de datos
with open(file_path, 'w') as file:
    print("CSV abierto para escritura de datos")

    # Indicar canales escritos
    contador = 0

    while True:
        # Obtener datos del puerto serie
        getData = str(ser.readline())
        data = getData[2:][:-5]
        print(data)

        if contador == 4:
            # Si se escribieron los datos de los 4 canales, empezar nueva línea
            file.write(data + "\n")
            contador = 0
        else:
            file.write(data + ",")
            # Indicar número de canal de dato escrito
            contador += 1
