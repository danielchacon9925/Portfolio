"AQuí va ejecutable"
from numpy import pi, exp, angle, conj, real, imag
import math

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
.
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


    
