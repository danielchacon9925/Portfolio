import sys
from abc import  ABCMeta, abstractmethod

class UsuarioBase(metaclass=ABCMeta):
    def __init__(self,propietario,MontoDisponible=0.0):
        # Nombre del propietario de la cuenta
        self.__propietario = propietario
        # Dinero disponible en la cuenta
        self.__MontoDisponible = MontoDisponible
    
    #Métodos polimórficos.
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
        salida="Propietario: %s\nMonto Disponible: %f\n" % (self.__propietario,
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
    def propietario(self,propietario):
       self.__propietario = propietario
        
    # Devuelve monto disponible
    @property
    def MontoDisponible(self):
       return self.__MontoDisponible
    
    # Asigna monto disponible
    @MontoDisponible.setter
    def MontoDisponible(self,MontoDisponible):
        self.__MontoDisponible = MontoDisponible