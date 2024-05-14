from numpy import pi, exp, angle, conj, real, imag

class calculadoradeimpedancias:
    def __init__(self, f, V1nom, V2nom, Snom, Voc, Ioc, Poc, Vsc, Isc, Psc):
        # Pruebas hechas en el primario
        self.Voc=Voc
        self.Ioc=Ioc
        self.Poc=Poc
        self.Vsc=Vsc
        self.Isc=Isc
        self.Psc=Psc


        # Frecuencia
        self.f = f
        # Tensión en primario
        self.V1nom=V1nom
        # Tensión en secundario
        self.V2nom=V2nom
        # Potencia aparente de carga
        self.Snom=Snom

        # Relación de transformación
        self.a=V1nom/V2nom
        
        # Inicialización de variables
        self.Xcc = 0
        self.Rcc = 0


        self.R1 = 0
        self.R1p = 0
        self.R2p = 0
        self.R2 = 0

        self.Xu = 0
        self.RFe = 0
        self.RFep = 0

        self.X1 = 0
        self.X1p = 0
        self.X2p = 0
        self.X2 = 0       

    def PruebaOC_Primario(self):
         # Q = (VI)²-P²)^(1/2)
         Q = ((self.Voc*self.Ioc)**2 - self.Poc**2)**(1/2)
         self.Xu = (self.Voc**2)/(Q)
         self.RFe = (self.Voc**2)/(self.Poc)

    def PruebaOC(self):
         # Q = (VI)²-P²)^(1/2)
         Q = ((self.Voc*self.Ioc)**2 - self.Poc**2)**(1/2)
         #print("Q",Q)
         self.Xup = (self.Voc**2)/(Q)
         self.Xu = (self.Xup)*(self.a**2)
         #print("Xup",self.Xup)
         self.RFep = (self.Voc**2)/(self.Poc)
         #print("RFep",self.RFep)
         self.RFe = (self.RFep)*(self.a**2)

    def PruebaSC(self):

         Q = ((self.Vsc*self.Isc)**2 - self.Psc**2)**(1/2)
         self.Xcc = Q/(self.Isc**2)
         self.Rcc = (self.Psc)/(self.Isc**2)

         self.R1 = self.Rcc/2
         self.R2p = self.Rcc/2
         self.R2 = self.R2p/(self.a**2)

         self.X1 = self.Xcc/2
         self.X2p = self.Xcc/2
         self.X2 = self.X2p/(self.a**2) 
         
    def PruebaSC_Secundario(self):

         Q = ((self.Vsc*self.Isc)**2 - self.Psc**2)**(1/2)
         self.Xcc = Q/(self.Isc**2)
         self.Rcc = (self.Psc)/(self.Isc**2)

         self.R1p = self.Rcc/2
         self.R1 = self.R1p*(self.a**2)
         self.R2 = self.Rcc/2

         self.X1p = self.Xcc/2
         self.X1 = self.X1p*(self.a**2)
         self.X2 = self.Xcc/2

    def print_stats(self):
         print("\t#############____Resultados de simulación___#######################")

         print("\t# Resistencia R1:\t\t"+str(self.R1)+"\t\t\t\t[ohms]\t")
         print("\t# Resistencia R2:\t\t"+str(self.R2)+"\t\t[ohms]\t")
         print("\t# Resistencia R2p:\t\t"+str(self.R2p)+"\t\t\t\t[ohms]\t")

         print("\t# Reactancia X1:\t\t"+str(self.X1)+"\t\t[H]\t")
         print("\t# Reactancia X2:\t\t"+str(self.X2)+"\t\t[H]\t")
         print("\t# Reactancia X2p:\t\t"+str(self.X2p)+"\t\t[H]\t")
         print("\t# Reactancia Xu:\t\t"+str(self.Xu)+"\t\t[H]\t")
         print("\t# Resistencia RFe:\t\t"+str(self.RFe)+"\t\t\t[ohms]\t")
         print("\t# Resistencia Xcc:\t\t"+str(self.Xcc)+"\t\t\t[ohms]\t")
         print("\t# Resistencia Rcc:\t\t"+str(self.Rcc)+"\t\t\t[ohms]\t")

class modeloreal:
    def __init__(self, f, V1nom, V2nom, Snom, R1, R2, X1, X2, RFe, Xu, Isc):
        # Impedancias e Inductancias
        self.R1=R1
        self.R2=R2
        self.X1=X1
        self.X2=X2
        self.RFe=RFe
        self.Xu=Xu

        self.R2p = 0

        self.Isc = Isc

        # Frecuencia
        self.f = f
        # Tensión en primario
        self.V1nom=V1nom
        # Tensión en secundario
        self.V2nom=V2nom
        # Potencia aparente de carga
        self.Snom=Snom
        # Relación de transformación
        self.a=V1nom/V2nom

        # Pérdidas en el hierro = 0
        self.SFe = 0
        self.PFe = 0

        # Pérdidas en el cobre
        self.SCu = 0
        self.PCu = 0


        # Tensión de excitación

        self.Vexc = 0


        # Corrientes
        self.I2p = 0
        
        self.I1 = 0 

        self.Iexc = 0


        # Impedancias 

        self.Zcc = 0

        # Reflexiones
        
        self.I1p = 0 
        self.I2 = 0
        self.Iexcp = 0

        self.X1p = 0
        self.X2p = 0
        self.Xup = 0

        self.V1p = 0
        self.V2p = 0

        self.R1p = 0
        self.R2p = 0
        self.RFep = 0

        self.IFe = 0
        self.IXu = 0.

        # Potencia
        self.S1 = 0

        self.magV1 = 0

        self.angV1 = 0

        self.magV1_pu = 0

        self.magV1_perc = 0


        self.S2 = 0

        self.magV2 = 0

        self.angV2 = 0

        self.magV2_pu = 0

        self.magV2_perc = 0

        self.Sperd = 0

        self.ef = 0

    def ReflexionenelPrimario(self):
        # Parámetros reflejados

        # R2p
        self.R2p=self.R2*self.a**2
        # X2p
        self.X2p=self.X2*self.a**2

        # V2p
        self.V2p = self.V2nom*self.a

        # Zcc
        self.Zcc = (self.R1+self.R2p) + 1j*(self.X1 + self.X2p)

        #self.Isc = (self.V1nom)/(self.Zcc)

        # I2p
        self.I2p = self.Isc

        # Vexc
        self.Vexc = self.V2p + self.I2p*(self.R2p+1j*self.X2p)
        
        # Iexc
        self.Iexc = (self.Vexc/self.RFe) + (self.Vexc/(1j*self.Xu))

        # I2

        self.I2 = self.I2p*self.a

        # I1
        self.I1=self.I2p + self.Iexc

        # IFe
        self.IFe = self.Xu/(self.RFe + self.Xu)

        # IXu
        self.IXu = self.RFe/(self.RFe + self.Xu)

        # V1
        self.V1 = self.Vexc+self.I1*(self.R1+1j*self.X1)

        # S1
        self.S1 = self.V1*conj(self.I1)
        self.magV1=abs(self.V1)
        self.angV1=angle(self.V1)*180/pi
        self.magV1_pu= (self.magV1/self.V1nom)
        self.magV1_perc=(self.magV1_pu*100)

        # S2
        self.S2=conj(self.I2)*self.V2nom
        self.Sperd = self.S1-self.S2
        self.ef=(real(self.S2)/real(self.S1))*100

        # Pérdidas en el hierro y cobre

        self.SFe = self.Iexc*(1/self.RFe + 1/(1j*self.Xu))**(-1)
        self.PFe = self.SFe.real


        self.SCu = ((self.Isc**2)*(self.R1+1j*self.X1) + ((self.Isc**2)*(self.R2p+1j*self.X2p)))
        self.PCu = self.SCu.real

        # Prints
        print("\t################Reflexión en el primario##########################")
        print("\t# R2p:\t\t\t"+str(self.R2p)+"\t\t\t[ohms]\t")
        print("\t# X2p:\t\t\t"+str(self.X2p)+"\t\t\t[ohms]\t")
        print("\t# I2p:\t\t"+str(self.I2p)+"\t\t[A]\t")
        print("\t# V2p:\t\t\t"+str(self.V2p)+"\t\t\t\t\t[V]\t")
        print("\t# Vexc:\t\t"+str(self.Vexc)+"\t\t[V]\t")
        print("\t# Iexc:\t\t"+str(self.Iexc)+"\t[A]\t")
        print("\t# I1:\t\t"+str(self.I1)+"\t\t[A]\t")
        print("\t# I2:\t\t"+str(self.I2)+"\t\t[A]\t")
        print("\t# Isc:\t\t"+str(self.Isc)+"\t\t[A]\t")
        print("\t# I2p:\t\t"+str(self.I2p)+"\t\t[A]\t")
        print("\t# V1:\t\t"+str(self.V1)+"\t[V]\t")
        print("\t# S1:\t\t"+str(self.S1)+"\t\t[VA]\t")
        print("\t# Pérdidas en el hierro:\t\t"+str(self.PFe)+"\t\t[W]\t")
        print("\t# Pérdidas en el cobre:\t\t"+str(self.PCu)+"\t\t[W]\t")

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