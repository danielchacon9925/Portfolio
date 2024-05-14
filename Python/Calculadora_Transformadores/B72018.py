"Aquí va el ejecutable"
from Pruebasdecircuito import *
from ReflexAP import *
from numpy import pi, exp, angle, conj, real, imag


###################################################
# Parámetros para cálculo de impedancia ppt 22 P8 #
###################################################

# Frecuencia
f = 60

# V1 nominal
V1nom = 8000

# V2 nominal
V2nom = 240

# S nominal
Snom = 60*10**(3)

#Factor de potencia
fp = 0.8

# Resistencia R1
Voc = 8000

#Resistencia R2
Ioc = 0.214

# Inductacia L1
Poc = 400

# Inductancia L2
Vsc = 489

# Impedancia del núcleo
Isc = 2.5

# Inductancia de magnetización
Psc = 240


###################################################
# Parámetros para cálculo de parámetros ppt 2 P10 #
###################################################

# Frecuencia
f2 = 50

# V1 nominal
V1nom2 = 220

# V2 nominal
V2nom2 = 380

# S nominal
Snom2 = 10*10**(3)

#Factor de potencia
fp2 = 0.8

# Tensión de circuito abierto
Voc2 = 220

# Corriente de circuito abierto 
Ioc2 = 2

# Potencia de circuito abierto
Poc2 = 150

# Tensión de corto circuito 
Vsc2 = 10

# Corriente de corto circuito 
Isc2 = 26.32

# Potencia de corto circuito
Psc2 = 75

###################################################
# Parámetros para cálculo de parámetros ppt 3 P10 #
###################################################

# Frecuencia
f3 = 50

# V1 nominal
V1nom3 = 3000

# V2 nominal
V2nom3 = 380

# S nominal
Snom3 = 10*10**(3)

#Factor de potencia
#fp3 = 0.8

# Tensión de circuito abierto
Voc3 = 3000

# Corriente de circuito abierto 
Ioc3 = 0.8

# Potencia de circuito abierto
Poc3 = 1000

# Tensión de corto circuito 
Vsc3 = 10

# Corriente de corto circuito 
Isc3 = 300

# Potencia de corto circuito
Psc3 = 750




# Instanciaciones de objeto

######################################################
# Instanciación para cálculo de impedancia ppt 22 P8 #
######################################################
print("\t###################################################################")
print("\t########__Resultado de ejercicio en diapositiva 22, P8__###########")
print("\t###################################################################")

print("\t")
impedancia = calculadoradeimpedancias(float (f),float (V1nom), float (V2nom), float (Snom), float (Voc), float (Ioc), float (Poc), float (Vsc), float (Isc), float (Psc))

impedancia.PruebaOC_Primario()
#impedancia.PruebaOC()
impedancia.PruebaSC()

impedancia.print_stats()

######################################################
# Instanciación para cálculo de parámetros ppt 2 P10 #
######################################################

print("\t###################################################################")
print("\t########__Resultado de ejercicio en diapositiva 2, P10__###########")
print("\t###################################################################")
impedancia2 = calculadoradeimpedancias(float (f2),float (V1nom2), float (V2nom2), float (Snom2), float (Voc2), float (Ioc2), float (Poc2), float (Vsc2), float (Isc2), float (Psc2))
#impedancia2 = calculadoradeimpedancias(50,220, 380, 10*10**(3), 220, 2, 150, 10, 26.32, 75)
impedancia2.PruebaOC()
impedancia2.PruebaSC()
impedancia2.print_stats()

R1 = impedancia2.R1
R2 = impedancia2.R2
X1 = impedancia2.X1
X2 = impedancia2.X2
RFe = impedancia2.RFe
Xu = impedancia2.Xu

parametrosppt2 = modeloreal(float(50), float(220), float(380), float(10*10**(3)), float(R1), float(R2), float(X1), float(X2), float(RFe), float(Xu),float(Isc2))
parametrosppt2.ReflexionenelPrimario()

######################################################
# Instanciación para cálculo de parámetros ppt 3 P10 #
######################################################

print("\t###################################################################")
print("\t########__Resultado de ejercicio en diapositiva 3, P10__###########")
print("\t###################################################################")
impedancia3 = calculadoradeimpedancias(float (f3),float (V1nom3), float (V2nom3), float (Snom3), float (Voc3), float (Ioc3), float (Poc3), float (Vsc3), float (Isc3), float (Psc3))
#impedancia2 = calculadoradeimpedancias(50,220, 380, 10*10**(3), 220, 2, 150, 10, 26.32, 75)
impedancia3.PruebaOC_Primario()
impedancia3.PruebaSC_Secundario()
impedancia3.print_stats()

R1 = impedancia3.R1
R2 = impedancia3.R2
X1 = impedancia3.X1
X2 = impedancia3.X2
RFe = impedancia3.RFe
Xu = impedancia3.Xu

parametrosppt3 = modeloreal(float(f3), float(V1nom3), float(V2nom3), float(Snom3), float(R1), float(R2), float(X1), float(X2), float(RFe), float(Xu),float(Isc3))
parametrosppt3.ReflexionenelPrimario()