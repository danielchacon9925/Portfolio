"Aquí va el objeto"
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
         
