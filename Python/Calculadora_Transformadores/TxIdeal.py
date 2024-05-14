from numpy import pi, exp, angle, conj, real, imag

class modeloreal:
    def __init__(self, f, V1nom, V2nom, Snom, fp, R1, R2, L1, L2, RFe, Lu):
        # Impedancias e Inductancias
        self.R1=R1
        self.R2=R2
        self.L1=L1
        self.L2=L2
        self.RFe=RFe
        self.Lu=Lu

        self.R2p = 0

        # Frecuencia
        self.f = f
        # Tensión en primario
        self.V1nom=V1nom
        # Tensión en secundario
        self.V2nom=V2nom
        # Potencia aparente de carga
        self.Snom=Snom
        # Factor de potencia
        self.fp=fp
        # Relación de transformación
        self.a=V1nom/V2nom
        # Potencia real
        self.P=self.Snom*self.fp
        # Potencia reactiva
        self.Q=((self.Snom)**2-(self.P)**2)**(1/2)
        # Potencia compleja
        self.Pcomplex= self.P + 1j*self.Q

        # Tensión de excitación

        self.Vexc = 0

        # Corrientes
        self.I2 = conj(self.Pcomplex/self.V2nom)
        
        self.I1 = 0 

        self.Iexc = 0
        

        # Reactancias
        self.X1=2*pi*self.f*L1


        self.X2=2*pi*self.f*L2
        

        self.Xu=2*pi*self.f*Lu

        # Reflexiones
        
        self.I1p = 0 
        self.I2p = 0
        self.Iexcp = 0

        self.X1p = 0
        self.X2p = 0
        self.Xup = 0

        self.V1p = 0
        self.V2p = 0

        self.R1p = 0
        self.R2p = 0
        self.RFep = 0

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


    def print_stats(self):
        print("Resultados de la simulación")

        print("\t# Frecuencia:\t\t\t"+str(self.f))
        print("\t# Relación a:\t\t\t"+str(self.a))
        print("\t# Potencia real:\t\t"+str(self.P))
        print("\t# Corriente I2:\t\t"+str(self.I2))
        print("\t# Corriente I2p:\t"+str(self.I2p))
        print("\t# Reactancia X2:\t\t"+str(self.X2))
        print("\t# Reactancia X2p:\t\t"+str(self.X2p))

    def ReflexionenelPrimario(self):
        # Parámetros reflejados

        # R2p
        self.R2p=self.R2*self.a**2
        # X2p
        self.X2p=self.X2*self.a**2
        # I2p
        self.I2p=self.I2/self.a
        # V2p
        self.V2p = self.V2nom*self.a
        # Vexc
        self.Vexc = self.V2p + self.I2p*(self.R2p+1j*self.X2p)
        # Iexc
        self.Iexc = (self.Vexc/self.RFe) + (self.Vexc/(1j*self.Xu))

        # I1
        self.I1=self.I2p + self.Iexc
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

        # Prints
        print("\t################Reflexión en el primario##########################")
        print("\t# R2p:\t\t\t"+str(self.R2p)+"\t\t\t[ohms]\t")
        print("\t# X2p:\t\t\t"+str(self.X2p)+"\t\t\t[H]\t")
        print("\t# I2p:\t\t"+str(self.I2p)+"\t\t[A]\t")
        print("\t# V2p:\t\t\t"+str(self.V2p)+"\t\t\t\t\t[V]\t")
        print("\t# Vexc:\t\t"+str(self.Vexc)+"\t\t[V]\t")
        print("\t# Iexc:\t\t"+str(self.Iexc)+"\t[A]\t")
        print("\t# I1:\t\t"+str(self.I1)+"\t\t[A]\t")
        print("\t# V1:\t\t"+str(self.V1)+"\t[V]\t")
        print("\t# S1:\t\t"+str(self.S1)+"\t\t[VA]\t")
        print("\t# magV1:\t\t"+str(self.magV1)+"\t\t\t[V]\t")
        print("\t# angleV1:\t\t"+str(self.angV1)+"\t\t\t[°]\t")
        print("\t# magV1_pu:\t\t"+str(self.magV1_pu)+"\t\t\t[ul]\t")
        print("\t# magV1_perc:\t\t"+str(self.magV1_perc)+"\t\t\t[%]\t")
        print("\t# S2:\t\t"+str(self.S2)+"\t\t\t\t\t[VA]\t")
        print("\t# Sperd:\t"+str(self.Sperd)+"\t\t[VA]\t")
        print("\t# eficiencia:\t\t"+str(self.ef)+"\t\t\t[%]\t")


    def ReflexionenelSecundario(self):
        # Parámetros reflejados

        # RFep
        self.RFep = self.RFe/self.a**2
        # Xup
        self.Xup = self.Xu/self.a**2

        # R1p
        self.R1p=self.R1/self.a**2
        # X1p
        self.X1p=self.X1/self.a**2
        # I1p
        self.I1p=self.I1*self.a
        # V1p
        self.V1p = self.V1nom/self.a
        # Vexcp
        self.Vexcp = (self.V1p + self.I1p*(self.R1p+1j*self.X1p))
        # Iexcp
        self.Iexcp = ((self.Vexcp/self.RFep) + (self.Vexcp/(1j*self.Xup)))

        # I2
        self.I2=self.I1p + self.Iexcp
        # V2
        self.V2 = self.Vexcp+self.I2*(self.R2+1j*self.X2)

        # S2
        self.S2 = self.V2*conj(self.I2)
        self.magV2=abs(self.V2)
        self.angV2=angle(self.V2)*180/pi
        self.magV2_pu= (self.magV2/self.V2nom)
        self.magV2_perc=(self.magV2_pu*100)

        # S2
        self.S1=conj(self.I1)*self.V1nom
        self.Sperd = self.S2-self.S1
        self.ef=(real(self.S1)/real(self.S2))*100

        # Prints
        print("\t################Reflexión en el secundario########################")
        print("\t# R1p:\t\t\t"+str(self.R1p)+"\t\t\t[ohms]\t")
        print("\t# X1p:\t\t\t"+str(self.X1p)+"\t\t\t[H]\t")
        print("\t# I1p:\t\t"+str(self.I1p)+"\t\t[A]\t")
        print("\t# V1p:\t\t\t"+str(self.V1p)+"\t\t\t\t\t[V]\t")
        print("\t# Vexcp:\t"+str(self.Vexcp)+"\t[V]\t")
        print("\t# Iexcp:\t"+str(self.Iexcp)+"\t\t[A]\t")
        print("\t# I2:\t\t"+str(self.I2)+"\t[A]\t")
        print("\t# V2:\t\t"+str(self.V2)+"\t[V]\t")
        print("\t# S2:\t\t"+str(self.S2)+"\t\t[VA]\t")
        print("\t# magV2:\t\t"+str(self.magV2)+"\t\t\t[V]\t")
        print("\t# angleV2:\t\t"+str(self.angV2)+"\t\t\t[°]\t")
        print("\t# magV2_pu:\t\t"+str(self.magV2_pu)+"\t\t\t[ul]\t")
        print("\t# magV2_perc:\t\t"+str(self.magV2_perc)+"\t\t\t[%]\t")
        print("\t# S1:\t\t"+str(self.S1)+"\t\t[VA]\t")
        print("\t# Sperd:\t"+str(self.Sperd)+"\t\t[VA]\t")
        print("\t# eficiencia:\t\t"+str(self.ef)+"\t\t\t[%]\t")

    def ReflexionenelPrimariosinmagnetizacion(self):
        # Parámetros reflejados

        # R2p
        self.R2p=self.R2*self.a**2
        # X2p
        self.X2p=self.X2*self.a**2
        # I2p
        self.I2p=self.I2/self.a
        # V2p
        self.V2p = self.V2nom*self.a

        # I1
        self.I1=self.I2p
        # V1
        self.V1 = self.V2p +self.I1*((self.R2p+1j*self.X2p)+(self.R1+1j*self.X1))

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

        # Prints
        print("\t############__Reflexión en el primario sin magnetización__#########")
        print("\t# R2p:\t\t\t"+str(self.R2p)+"\t\t\t[ohms]\t")
        print("\t# X2p:\t\t\t"+str(self.X2p)+"\t\t\t[H]\t")
        print("\t# I2p:\t\t"+str(self.I2p)+"\t\t[A]\t")
        print("\t# V2p:\t\t\t"+str(self.V2p)+"\t\t\t\t\t[V]\t")
        #print("\t# Vexc:\t\t"+str(self.Vexc)+"\t\t[V]\t")
        #print("\t# Iexc:\t\t"+str(self.Iexc)+"\t[A]\t")
        print("\t# I1:\t\t"+str(self.I1)+"\t\t[A]\t")
        print("\t# V1:\t\t"+str(self.V1)+"\t\t[V]\t")
        print("\t# S1:\t\t"+str(self.S1)+"\t\t[VA]\t")
        print("\t# magV1:\t\t"+str(self.magV1)+"\t\t\t[V]\t")
        print("\t# angleV1:\t\t"+str(self.angV1)+"\t\t\t[°]\t")
        print("\t# magV1_pu:\t\t"+str(self.magV1_pu)+"\t\t\t[ul]\t")
        print("\t# magV1_perc:\t\t"+str(self.magV1_perc)+"\t\t\t[%]\t")
        print("\t# S2:\t\t"+str(self.S2)+"\t\t[VA]\t")
        print("\t# Sperd:\t"+str(self.Sperd)+"\t\t[VA]\t")
        print("\t# eficiencia:\t\t"+str(self.ef)+"\t\t\t[%]\t")

    def ReflexionenelSecundariosinmagnetizacion(self):
        # Parámetros reflejados

        # RFep
        self.RFep = self.RFe/self.a**2
        # Xup
        self.Xup = self.Xu/self.a**2

        # R1p
        self.R1p=self.R1/self.a**2
        # X1p
        self.X1p=self.X1/self.a**2
        # I1p
        self.I1p=self.I1*self.a
        # V1p
        self.V1p = self.V1nom/self.a

        # I2
        self.I2=self.I1p
        # V2
        self.V2 = self.V1p + self.I2*((self.R1p+1j*self.X1p)+(self.R2+1j*self.X2))

        # S2
        self.S2 = self.V2*conj(self.I2)
        self.magV2=abs(self.V2)
        self.angV2=angle(self.V2)*180/pi
        self.magV2_pu= (self.magV2/self.V2nom)
        self.magV2_perc=(self.magV2_pu*100)

        # S2
        self.S1=conj(self.I1)*self.V1nom
        self.Sperd = self.S2-self.S1
        self.ef=(real(self.S1)/real(self.S2))*100

        # Prints
        print("\t############__Reflexión en el primario sin magnetización__#########")
        print("\t# R1p:\t\t\t"+str(self.R1p)+"\t\t\t[ohms]\t")
        print("\t# X1p:\t\t\t"+str(self.X1p)+"\t\t\t[H]\t")
        print("\t# I1p:\t\t"+str(self.I1p)+"\t[A]\t")
        print("\t# V1p:\t\t\t"+str(self.V1p)+"\t\t\t\t\t[V]\t")
        #print("\t# Vexc:\t\t"+str(self.Vexc)+"\t\t[V]\t")
        #print("\t# Iexc:\t\t"+str(self.Iexc)+"\t[A]\t")
        print("\t# I2:\t\t"+str(self.I2)+"\t[A]\t")
        print("\t# V2:\t\t"+str(self.V2)+"\t\t[V]\t")
        print("\t# S2:\t\t"+str(self.S2)+"\t\t[VA]\t")
        print("\t# magV2:\t\t"+str(self.magV2)+"\t\t\t[V]\t")
        print("\t# angleV2:\t\t"+str(self.angV2)+"\t\t\t[°]\t")
        print("\t# magV2_pu:\t\t"+str(self.magV2_pu)+"\t\t\t[ul]\t")
        print("\t# magV2_perc:\t\t"+str(self.magV2_perc)+"\t\t\t[%]\t")
        print("\t# S1:\t\t"+str(self.S1)+"\t\t[VA]\t")
        print("\t# Sperd:\t"+str(self.Sperd)+"\t\t[VA]\t")
        print("\t# eficiencia:\t\t"+str(self.ef)+"\t\t\t[%]\t")











