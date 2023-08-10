import sys
from usuario_base import *
from abc import ABCMeta, abstractmethod


class UsuarioTasaCero(UsuarioBase):
    def __init__(self, propietario, MontoDispoble=100.0):
        # Se llama al constructor de la clase padre
        super().__init__(propietario, MontoDisponible=100.0, Porcentaje=1)
        # Nombre del Propietario
        self.__propietario = propietario
        # Monto disponible de la clase hija
        self.__MontoDisponible = MontoDispoble

        # Porcentaje de ahorro
        #self.__Porcentaje = Porcentaje/100
        # Monto que se debe calcular para quitar a monto disponible
        #self.__MontoAhorro = MontoAhorro

        # Número de meses en que debe pagar
        self.__Plazo = 0
        # Booleano que indica cuando se tiene vigente operación tasa cero
        self.__OperacionVigente = False

    def AplicarInversion(self):
        pass

    def AsignarOperacion(self):
        pass

    def Print(self):
        pass

    def CapturaInformacion(self):
        pass

    @property
    def Plazo(self):
        pass

    @Plazo.setter
    def Plazo(self, NuevoPlazo):
        pass

    @property
    def MontoCosumoMes(self):
        pass

    @MontoCosumoMes.setter
    def MontoCosumoMes(self, NuevoMontoConsumoMes):
        pass
