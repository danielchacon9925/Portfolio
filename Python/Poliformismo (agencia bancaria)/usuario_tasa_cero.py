import sys
from usuario_base import *
from abc import  ABCMeta, abstractmethod

class UsuarioTasaCero(UsuarioBase):
    def __init__(self,propietario,MontoDisponible=100.0):
        # Nombre del Propietario
        self.__propietario = propietario
        # Monto disponible de la clase hija
        self.__MontoDisponible = MontoDisponible
        # Monto de consumo mes a mes
        self.__MontoConsumoMes = 0
        # Meses que debe
        self.__Plazo = 0
        # Indica si se tiene o no una operacion vigente
        self.__OperacionVigente = False
        # Se llama al constructor de la clase padre
        super().__init__(self.__propietario, self.__MontoDisponible)
        
        
    # Se realizan los calculos necesarios
    def AplicarInversion(self):
        # Si hay operacion vigente y el plazo es distinto de cero
        if(self.__OperacionVigente and self.__Plazo != 0):
            self.__MontoDisponible = self.__MontoDisponible - self.__MontoConsumoMes
            self.__Plazo = self.__Plazo - 1
                
        # Si el plazo es cero, operacion vigente es falso y el consumo se pone en cero
        else:
            self.__OperacionVigente = False
            self.__MontoConsumoMes = 0
                
    
    # Getter de AplicarInversion()
    def Aplicar(self):
        self.AplicarInversion() 
                
    # Asigna si operacion esta en true o false    
    def AsignarOperacion(self):
        # Si hay operacion
        if(self.__OperacionVigente):
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
    def Plazo(self,NuevoPlazo):
        self.__Plazo = NuevoPlazo
         
    # Getter de monto consumo mes   
    @property
    def MontoCosumoMes(self):
        return self.__MontoConsumoMes
    
    # Setter del monto consumo mes
    @MontoCosumoMes.setter
    def MontoCosumoMes(self,NuevoMontoConsumoMes):
        self.__MontoConsumoMes = NuevoMontoConsumoMes

UsuarioTasaCero1=UsuarioTasaCero("Marco Valverde",100000.0)
UsuarioTasaCero1.MontoCosumoMes=35000.0
UsuarioTasaCero1.Plazo=3
UsuarioTasaCero1.Asignar()
print(UsuarioTasaCero1)
UsuarioTasaCero1.Aplicar()
print(UsuarioTasaCero1)