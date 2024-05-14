#include <PubSubClient.h>
#include <ESP8266WiFi.h>
#include <stdlib.h>
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>

#define SEALEVELPRESSURE_HPA (1013.25)

// Definición de pin de MQ2
#define sensorPin 0 //D3-Naranja

// Definición de pin para ADC
#define analogPin A0 /* ESP8266 Analog Pin ADC0 = A0 */

/////////////////// DEFINICIÓN PINES DE LOS LEDS ////////////////////
#define LED_BLUE 9 // LED AZUL
#define LED_RED  10 // LED ROJO

// WiFi
// Casa
//const char *ssid =  "REX2.4";    // replace with your wifi ssid and wpa2 key
//const char *pass =  "Daniel0625";//WiFi Password 
// Teléfono
const char *ssid =  "Daniel's Galaxy Note20 Ultra";    // replace with your wifi ssid and wpa2 key
const char *pass =  "19990625";//WiFi Password 
// Buzzer
const unsigned char buzzer= 14; //D5-VERDE KK

// Ventilador
//int MOTOR= 12; //D5-VERDE KK
// Gas
int lpg;
int lpgA;
// Variables de estación de clima
float TEMP;
float HUM;
float PRESS;
float ALT;
// Lectura de ADC
int adcValue = 0;  /* Variable to store Output of ADC */
float BAT;  /* Variable to store Output of ADC */




// BMP280
Adafruit_BME280 bme; // I2C

WiFiClient client;
PubSubClient pubsub_client(client);

void setup() 
{
  pinMode(LED_BUILTIN, OUTPUT);  // Initialize the LED_BUILTIN pin as an output
  pinMode(buzzer, OUTPUT);
  pinMode(LED_RED, OUTPUT); // Configuración LED rojo como salida
  pinMode(LED_BLUE, OUTPUT); // Configuración LED azul como salida
  ///pinMode(MOTOR, OUTPUT);

  Serial.begin(9600);
  delay(10);


  Serial.println(F("BME280 test"));

  bool status;

  // default settings
  // (you can also pass in a Wire library object like &Wire2)
  status = bme.begin(0x76);  
  if (!status) {
    Serial.println("Could not detect a BME280 sensor, Fix wiring Connections!");
    while (1);
  }

  Serial.println("-- Print BME280 readings--");
  Serial.println();


  Serial.println("Connecting to ");
  Serial.println(ssid); 
 
  WiFi.begin(ssid, pass); 
  while (WiFi.status() != WL_CONNECTED) 
    {
      delay(500);
      Serial.print(".");
    }
  Serial.println("");
  Serial.println("WiFi connected"); 

  pubsub_client.setServer("iot.eie.ucr.ac.cr", 1883); // This is default if you are using thingsboard

  while (!pubsub_client.connect ("Lab_04_B72018_B87388","aknw9qgidmkg8t5radyi", NULL)) // This need to be configured by adding a new device and copying the access token
    {
      delay(500);
      Serial.print(".");
    }
    Serial.println("");
    Serial.println("Thingsboard connected"); 
}
 
void loop() 
{   
  lpg = digitalRead(sensorPin);
  Serial.print("Air:");
  Serial.println(lpg);
  digitalWrite(LED_BUILTIN, LOW);  
  delay(1000);                      // Wait for a second
  digitalWrite(LED_BUILTIN, HIGH);  // Turn the LED off by making the voltage HIGH
  delay(2000);  

  adcValue = analogRead(analogPin); /* Read the Analog Input value */
  BAT=(((float)adcValue/920)*100);
  Serial.print("Bateria = ");
  Serial.print(BAT);
  Serial.println("%");

  Serial.print("Temperature = ");
  TEMP=bme.readTemperature();
  Serial.print(TEMP);
  Serial.println(" *C");
  
  Serial.print("Pressure = ");
  PRESS=(bme.readPressure() / 100.0F);
  Serial.print(PRESS);
  Serial.println(" hPa");

  Serial.print("Approx. Altitude = ");
  ALT=(bme.readAltitude(SEALEVELPRESSURE_HPA));
  Serial.print(ALT);
  Serial.println(" m");

  Serial.print("Humidity = ");
  HUM=bme.readHumidity();
  Serial.print(HUM);
  Serial.println(" %");

  Serial.println();
  delay(1000);

  // Encender el LED rojo si la batería está baja
  if (BAT < 20) { // Valor menor a 20
    digitalWrite(LED_RED, HIGH); // Encender el LED rojo
  }
  
  if (lpg == 0)
  {
  Serial.println("Smoke: Detected!");
  digitalWrite(LED_BLUE, HIGH); // Encender el LED AZUL cuando se detecte humo
  // Se enciende motor
  //digitalWrite(MOTOR, HIGH);
  tone(buzzer, 1000); // Enviar señal de sonido a 1KHz
  delay(1000);        // Durante 1 segundo
  noTone(buzzer);     // Detener el sonido
  delay(1000);        // Esperar 1 segundo             
  }
  // Motor apagado
  //digitalWrite(MOTOR, LOW);
  // Crear el payload JSON con todas las variables
  String payload = "{";
  payload += "\"lpg\":"; payload += !lpg;
  payload += ",\"temperature\":"; payload += TEMP;
  payload += ",\"pressure\":"; payload += PRESS;
  payload += ",\"altitude\":"; payload += ALT;
  payload += ",\"humidity\":"; payload += HUM;
  payload += ",\"BAT\":"; payload += BAT;
  payload += "}";
  Serial.println(payload);

  // Publicar el payload en ThingsBoard
  if(pubsub_client.publish("v1/devices/me/telemetry", payload.c_str())) 
    Serial.println("Published");  

  else {
    digitalWrite(LED_BLUE, LOW); // Apagar el LED AZUL si no se ha detectado humo
    digitalWrite(LED_RED, LOW); // Apagar el LED ROJO si la batería no está baja
  }
}