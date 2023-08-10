import sys
from abc import ABCMeta, abstractmethod
from usuario_base import *


'''
+++++++++++++++++++
+ Class UsuarioBase
+++++++++++++++++++
'''


class UsuarioBase(metaclass=ABCMeta):
    def __init__(self, propietario, MontoDisponible=0.0):
        # Nombre del propietario de la cuenta
        self.__propietario = propietario
        # Dinero disponible en la cuenta
        self.__MontoDisponible = MontoDisponible

    # Metodo que se utiliza en clases hijas para calcular ahorro
    @abstractmethod
    def AplicarInversion(self):
        pass

    # Metodo que se usa en clases hijas para asignar operacion como true o false
    @abstractmethod
    def AsignarOperacion(self):
        pass

    # Metodo para imprimir resultados
    @abstractmethod
    def Print(self):
        pass

    # Metodo para capturar informacion
    @abstractmethod
    def CapturaInformacion(self):
        pass

    # Getter de aplicar inversion
    def Aplicar(self):
        self.AplicarInversion()

    # Getter de asignar operacion
    def Asignar(self):
        self.AsignarOperacion()

    def __str__(self):
        salida = "Propietario: %s\nMonto Disponible: %f\n" % (self.__propietario,
                                                              self.__MontoDisponible)
        return salida+self.Print()

    # Getter de capturar informacion
    def Captura(self):
        self.CapturaInformacion()

    # Devuelve nombre de propietario
    @property
    def propietario(self):
        return self.__propietario

    # Asigna nombre de propietario
    @propietario.setter
    def propietario(self, propietario):
        self.__propietario = propietario

    # Devuelve monto disponible
    @property
    def MontoDisponible(self):
        return self.__MontoDisponible

    # Asigna monto disponible
    @MontoDisponible.setter
    def MontoDisponible(self, MontoDisponible):
        self.__MontoDisponible = MontoDisponible


'''
+++++++++++++++++++
+ Class UsuarioAhorro
+++++++++++++++++++
'''


class UsuarioAhorro(UsuarioBase):
    def __init__(self, propietario, MontoDisponible=100.0, Porcentaje=1):
        # Se llama al constructor de la clase padre
        super().__init__(propietario, MontoDisponible)
        # Nombre del Propietario
        self.__propietario = propietario
        # Monto disponible de la clase hija
        self.__MontoDisponible = MontoDisponible
        # Porcentaje de ahorro
        self.__Porcentaje = Porcentaje/100
        # Monto que se debe calcular para quitar a monto disponible
        self.__MontoAhorro = 0

    # Se calcula la inversion y se devuelve el monto de ahorro y el monto disponible
    def AplicarInversion(self):
        self.__MontoAhorro = self.__MontoDisponible * self.__Porcentaje
        self.__MontoDisponible = self.__MontoDisponible - self.__MontoAhorro
        MontoDisponible = self.__MontoDisponible
        return self.__MontoDisponible, MontoDisponible

    # Getter de aplicar inversion

    def Aplicar(self):
        self.AplicarInversion()

    # Metodo vacio para esta clase hija
    def AsignarOperacion(self):
        pass

    # Getter vacio para esta clase fija
    def Asignar(self):
        pass

     # Devuelve monto de ahorro
    @property
    def MontoAhorro(self):
        return self.__MontoAhorro

    def Print(self):
        resultado = "Porcentaje ahorro: " + \
            str(self.__Porcentaje) + "\nMonto Ahorro: " + \
            str(self.__MontoAhorro)
        return resultado

    def CapturaInformacion(self):
        pass

    # Devuelve el porcentaje de inversion
    @property
    def Porcentaje(self):
        return self.__Porcentaje

    # Set Porcentaje de Inversion
    @Porcentaje.setter
    def Porcentaje(self, Nuevo_Porcentaje):
        self.__Porcentaje = Nuevo_Porcentaje/100


'''
+++++++++++++++++++
+ Class TasaCero
+++++++++++++++++++
'''


class UsuarioTasaCero(UsuarioBase):
    def __init__(self, propietario, MontoDisponible=100.0):
        # Nombre del Propietario
        self.__propietario = propietario
        # Monto disponible de la clase hija
        self.__MontoDisponible = MontoDisponible
        # Monto de consumo mes a mes
        self.__MontoConsumoMes = 0
        # Plazo de deuda vigente
        self.__Plazo = 0
        # Indica si se tiene o no una operacion vigente
        self.__OperacionVigente = False
        # Se llama al constructor de la clase padre
        super().__init__(self.__propietario, self.__MontoDisponible)

    # Se realizan los calculos necesarios

    def AplicarInversion(self):
        # Operacion vigente = True y el plazo != 0
        if(self.__OperacionVigente and self.__Plazo != 0):
            self.__MontoDisponible = self.__MontoDisponible - self.__MontoConsumoMes
            self.__Plazo = self.__Plazo - 1

        # Si plazo es cero, operacion vigente == false y el consumo == cero
        else:
            self.__OperacionVigente = False
            self.__MontoConsumoMes = 0

    # Getter de AplicarInversion()
    def Aplicar(self):
        self.AplicarInversion()

    # Asigna si operacion esta en true o false
    def AsignarOperacion(self):
        # Si hay operacion
        if(self.__OperacionVigente == True):
            print("Hay una operación en proceso, no se puede realizar otra")

        # Si no hay operacion y tanto el monto de consumo y el plazo son distintos de cero se pone en true la operacion vigente
        elif(self.__OperacionVigente == False and self.__MontoConsumoMes != 0 and self.__Plazo != 0):
            self.__OperacionVigente = True

    # Getter de AsignarOperacion()
    def Asignar(self):
        self.AsignarOperacion()

    def Print(self):
        if(self.__OperacionVigente == False):
            resultado = "Propietario: %s\nMonto Disponible: %.2f\n" % (self.__propietario,
                                                                       self.__MontoDisponible) + "\nNo hay operación Tasa Cero vigente"
        else:
            resultado = "Propietario: %s\nMonto Disponible: %.2f\n" % (self.__propietario,
                                                                       self.__MontoDisponible) + "Monto Consumo Mes: " + str(self.__MontoConsumoMes) + "\nPlazo: " + str(self.__Plazo)

        return resultado

    def CapturaInformacion(self):
        pass

    # Getter de Plazo
    @property
    def Plazo(self):
        return self.__Plazo

    # Setter de Plazo
    @Plazo.setter
    def Plazo(self, NuevoPlazo):
        self.__Plazo = NuevoPlazo

    # Getter de monto consumo mes
    @property
    def MontoCosumoMes(self):
        return self.__MontoConsumoMes

    # Setter del monto consumo mes
    @MontoCosumoMes.setter
    def MontoCosumoMes(self, NuevoMontoConsumoMes):
        self.__MontoConsumoMes = NuevoMontoConsumoMes


'''
+++++++++++++++++++
+ Class UsuarioPagosServicios
+++++++++++++++++++
'''


class UsuarioPagoServicios(UsuarioBase):
    def __init__(self, propietario, MontoDisponible=100.0, servicio=[], CargoAutomatico=0):
        # Se llama al constructor de la clase padre
        super().__init__(propietario, MontoDisponible)
        # Nombre del Propietario
        self.__propietario = propietario
        # Monto disponible de la clase hija
        self.__MontoDisponible = MontoDisponible
        # Lista de servicios
        self.__servicios = servicio
        # Cargo automático
        self.__CargoAutomatico = CargoAutomatico

    def AplicarInversion(self):
        if self.__MontoDisponible > self.__CargoAutomatico:
            # Se aplica en cada elemento de lista
            i = 0
            for servicio in self.__servicios:
                servicio = str(self.__servicios[i])
                self.__MontoDisponible = self.__MontoDisponible - self.__CargoAutomatico
                # Una vez aplicado el débito, se pone en cero el cargo automático
                i += 1
            self.__CargoAutomatico = 0
        else:
            print("El monto disponible no es suficiente")

    # Getter de AplicarInversion()
    def Aplicar(self):
        self.AplicarInversion()

    def AsignarOperacion(self):
        # Si hay operacion vigente
        if(self.__OperacionVigente == True):
            print("Operación vigente en proceso, no se puede realizar otra")
            # Si no hay operacion y tanto el monto de consumo y el plazo son distintos de cero se pone en true la operacion vigente
        elif(self.__OperacionVigente == False):
            self.__OperacionVigente = True

    # Getter de AsignarOperacion()
    def Asignar(self):
        self.AsignarOperacion()

    def Print(self):
        salida = ""
        print("Propietario: %s\nMonto Disponible: %.2f\n" % (self.__propietario,
                                                             self.__MontoDisponible))
        # Contador para ciclo
        i = 0
        # Ciclo para imprimir cada servicio
        for servicio in self.__servicios:
            servicio = str(self.__servicios[i])
            print(servicio)
            print("Cargo Automatico: " + str(self.__CargoAutomatico))
            print("------------------------------------")
            i += 1

        if(self.__CargoAutomatico == 0):
            print("\nNo hay Saldo Pendiente")
        # Si hay saldo pendiente
        else:
            print("\nSaldo Pendiente")
        return salida

    def CapturaInformacion(self):
        pass

    @property
    def Servicios(self):
        return self.__servicios

    @Servicios.setter
    def Servicios(self, NuevoServicio):
        self.__servicios.append(NuevoServicio)
        print("El servicio {} ha sido añadido a la lista de servicios: {}".format(
            NuevoServicio, self.__servicios))

     # Getter del Cargo Automatico
    @property
    def CargoAutomatico(self):
        return self.__CargoAutomatico

    # Setter del Cargo automatico
    @CargoAutomatico.setter
    def CargoAutomatico(self, CargoAutomatico):
        self.__CargoAutomatico = CargoAutomatico


'''
+++++++++++++++++++
+ Class ServicioPublico
+++++++++++++++++++
'''


class ServicioPublico(object):
    def __init__(self, EmpresaServicioPublico, CargoAutomatico, OperacionVigente):
        self.__EmpresaServicioPublico = EmpresaServicioPublico
        # Indica el valor default de CArgo Automático
        self.__CargoAutomatico = CargoAutomatico
        # Indica si tiene o no una operación vigente
        self.__OperacionVigente = OperacionVigente

    @property
    def EmpresaServicioPublico(self):
        return self.__EmpresaServicioPublico

    @EmpresaServicioPublico.setter
    def EmpresaServicioPublico(self, EmpresaServicioPublico):
        self.__EmpresaServicioPublico = EmpresaServicioPublico
        print("Se ha añadido {} a los servicios públicos".format(
            EmpresaServicioPublico))

    @property
    def CargoAutomatico(self):
        return self.__CargoAutomatico

    @CargoAutomatico.setter
    def CargoAutomatico(self, CargoAutomatico):
        # Se define el valor del cargo automático
        self.__CargoAutomatico = CargoAutomatico

    @property
    def OperacionVigente(self):
        if (self.__OperacionVigente == True):
            print("Se tiene una operación de tasa cero vigente")
        else:
            print("No hay operación de tasa cero vigente")

    @OperacionVigente.setter
    def OperacionVigente(self, OperacionVigente):
        self.__OperacionVigente = OperacionVigente

    def __str__(self):
        salida = "Empresa:" + str(self.__EmpresaServicioPublico)
        return salida

    def CapturaInformacion(self):
        pass


print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# Prueba de funcionamiento
print("Prueba de funcionamiento de pago de servicios públicos")
lista = []
S1 = ServicioPublico("AyA", True, True)
S2 = ServicioPublico("Cable", True, False)
S3 = ServicioPublico("CNFL", True, False)
lista.append(S1)
lista.append(S2)
lista.append(S3)
U1 = UsuarioPagoServicios("Daniel", 150000, lista)
U1.CargoAutomatico = 5500
print(U1)
U1.Aplicar()
print(U1)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# Prueba de funcionamiento
print("Prueba de usuarios tasa cero")
UsuarioTasaCero1 = UsuarioTasaCero("Osvaldo Valerín", 150000.0)
UsuarioTasaCero1.MontoCosumoMes = 35000.0
UsuarioTasaCero1.Plazo = 3
UsuarioTasaCero1.Asignar()
print(UsuarioTasaCero1)
UsuarioTasaCero1.Aplicar()
print(UsuarioTasaCero1)
UsuarioTasaCero1.Aplicar()
print(UsuarioTasaCero1)
UsuarioTasaCero1.Aplicar()
print(UsuarioTasaCero1)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# Prueba de funcionamiento
print("Prueba de funcionamiento para usuarios de ahorro")
# Prueba de funcionamiento
usuario_1 = UsuarioAhorro('Daniel', 100000, 50)
print(usuario_1)
usuario_1.Aplicar()
print(usuario_1)
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
