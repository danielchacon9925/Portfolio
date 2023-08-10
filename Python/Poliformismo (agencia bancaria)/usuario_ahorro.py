import sys
from usuario_base import *
from abc import  ABCMeta, abstractmethod

class UsuarioAhorro(UsuarioBase):
    def __init__(self,propietario,MontoDisponible=100.0,Porcentaje=1):
        # Se llama al constructor de la clase padre
        super().__init__(propietario,MontoDisponible)
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
        return self.__MontoDisponible
        
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
        resultado = "Porcentaje ahorro: " + str(self.__Porcentaje) + "\nMonto Ahorro: " + str(self.__MontoAhorro)
        return resultado
      
    def CapturaInformacion(self):
        pass
    
    # Devuelve el porcentaje de inversion
    @property
    def Porcentaje(self):
        return self.__Porcentaje
    
    # Setea Porcentaje de Inversion
    @Porcentaje.setter
    def Porcentaje(self,Nuevo_Porcentaje):
        self.__Porcentaje = Nuevo_Porcentaje/100   
        