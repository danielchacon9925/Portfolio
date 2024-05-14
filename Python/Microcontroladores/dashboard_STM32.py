# Laboratorio 4: Daniel Chacón Mora (B72018) - Erick Sancho Alvarado (B87388)

import paho.mqtt.client as mqtt  # Importación de la biblioteca MQTT
import json  # Importación de la biblioteca JSON para manipulación de datos JSON
import time  # Importación de la biblioteca time para gestionar el tiempo
import serial  # Importación de la biblioteca serial para comunicación serial

# Callback para manejar la conexión al broker MQTT
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conexión establecida con el broker MQTT")  # Mensaje de conexión exitosa
    else:
        print("No se pudo establecer la conexión. Código de retorno:", rc)  # Mensaje de fallo en la conexión

def on_disconnect(client, userdata, rc):
    if(rc == 0):
        print("Desconexión exitosa")  # Mensaje de desconexión exitosa
    else:
        print("Sistema desconectado mediante el código: ", rc)  # Mensaje de desconexión con código de error

# Callback para manejar la publicación de mensajes
def on_publish(client, userdata, mid):
    print("Mensaje publicado en el dashboard", mid)  # Mensaje de publicación exitosa

ser = serial.Serial("/dev/ttyACM0", 115200, timeout = 1)  # Inicialización del objeto Serial para comunicación serial
print("Conectado al puerto serial /dev/ttyACM0")  # Mensaje de conexión exitosa al puerto serial

# Configuración del cliente MQTT
client = mqtt.Client("microcontrolador")  # Creación de un cliente MQTT
client.connected = False  # Bandera para indicar si el cliente está conectado o no
client.on_connect = on_connect  # Asignación de la función de callback para la conexión
client.on_disconnect = on_disconnect  # Asignación de la función de callback para la desconexión
client.on_publish = on_publish  # Asignación de la función de callback para la publicación

# Configuración del broker y token de autenticación
broker_address = "iot.eie.ucr.ac.cr"  # Dirección del broker MQTT
port = 1883  # Puerto del broker MQTT
token = "aknw9qgidmkg8t5radyi"  # Token de autenticación
username = "Lab_04_B72018_B87388"  # Nombre de usuario

# Conexión al broker MQTT
client.username_pw_set(token)  # Establecimiento del token de autenticación
client.connect(broker_address, port)  # Conexión al broker MQTT

# Estructura json
dictionary = dict()  # Creación de un diccionario para almacenar los datos

# Rutina de dormir
# while client.connected != True:
while client.connected != True:
    # Espera hasta que el cliente se conecte
    client.loop()  # Manejo de eventos MQTT
    time.sleep(2)  # Espera de 2 segundos

# Bucle principal
    while 1:
        # Lectura de datos del microcontrolador
        data = ser.readline().decode('utf-8')  # Lectura de datos desde el puerto serial y decodificación a cadena UTF-8
        data = data.replace('\r', "").replace('\n', "")  # Eliminación de caracteres de retorno de carro y nueva línea
        data = data.split(',')  # Separación de la cadena en una lista utilizando la coma como delimitador
        if (len(data) == 4):  # Verificación de que se hayan recibido los 4 valores esperados
            dictionary["Eje X"] = data[0]  # Asignación del valor del eje X al diccionario
            dictionary["Eje Y"] = data[1]  # Asignación del valor del eje Y al diccionario
            dictionary["Eje Z"] = data[2]  # Asignación del valor del eje Z al diccionario
            dictionary["Bateria"] = data[3]  # Asignación del valor de la batería al diccionario
            if (float(data[3]) < 7):  # Comprobación del nivel de la batería
                dictionary["Nivel de bateria"] = "Bateria baja"  # Establecimiento del nivel de la batería como bajo
            else:
                dictionary["Nivel de bateria"] = "Bateria alta"  # Establecimiento del nivel de la batería como alto
        payload = json.dumps(dictionary)  # Conversión del diccionario a una cadena JSON
        # Publicación del mensaje en el topic del dashboard
        topic = "v1/devices/me/telemetry"  # Topic del dashboard
        print(payload)  # Impresión del mensaje JSON en consola
        client.publish(topic, payload)  # Publicación del mensaje en el broker MQTT
        # Espera antes de enviar el siguiente mensaje
        time.sleep(1)  # Envío de datos cada 1 segundo
