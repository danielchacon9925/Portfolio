import sys
from abc import ABCMeta, abstractmethod


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

    # Base inicializadora


# class BaseIO(object):
#    def Input(self, info=""):
#        return input(info)


'''
+++++++++++++++++++
+ Class UsuarioAhorro
+++++++++++++++++++
'''


class UsuarioAhorro(UsuarioBase):
    def __init__(self, propietario, MontoDisponible=100.0, Porcentaje=1):
        # Propietario
        self.__propietario = propietario
    # Monto disponible de la clase hija
        self.__MontoDisponible = MontoDisponible
    # Porcentaje de ahorro
        self.__Porcentaje = Porcentaje/100
    # Monto que se debe calcular para quitar a monto disponible
        self.__MontoAhorro = 0
    # Se llama al constructor de la clase padre
        super().__init__(propietario, MontoDisponible)

    # def __init__(self, Porcentaje=1):
    #    # Nombre del Propietario
    #    self.__propietario = ""
        # Monto disponible de la clase hija
    #    self.__MontoDisponible = 0
        # Porcentaje de ahorro
    #    self.__Porcentaje = Porcentaje/100
        # Monto que se debe calcular para quitar a monto disponible
    #    self.__MontoAhorro = 0

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
        self.__propietario = input("Nombre del propietario")
        self.__MontoDisponible = input("Monto Disponible")
        self.__PorcentajeAhorro = float(input("Porcentaje de ahorro:\n"))/100
        usuario = UsuarioAhorro(
            self.__propietario, self.__MontoDisponible, self.__PorcentajeAhorro)

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
        self.__propietario = input("Nombre del propietario:\n")
        self.__MontoDisponible = input("Monto Disponible:\n")
        self.__Plazo = input("Plazo:\n")
        UsuarioTasaCero1 = UsuarioTasaCero(
            self.__propietario, self.__MontoDisponible, self.__Plazo)

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

    # def __init__(self, servicio=[]):
        # Nombre del Propietario
    #    self.__propietario = ""
        # Monto disponible de la clase hija
    #    self.__MontoDisponible = 0
        # Lista de servicios publicos de la clase ServicioPublico
    #    self.__servicios = servicio
        # Cargos automaticos obtenidos de la clase ServicioPublico
    #    self.__CargoAutomatico = 0
        # Operacion Vigente
    #    self.__OperacionVigente = False

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

    # Imprime la informacion de la persona, los servicios y saldos pendientes

    # def Print(self):
    #    salida = ""
    #    print("Propietario:" + str(self.__propietario) +
    #          "\nMonto Disponible:" + str(self.__MontoDisponible))
        # Contador para ciclo
    #    i = 0
        # Ciclo para imprimir cada servicio
    #    for servicio in self.__servicios:
    #        servicio = str(self.__servicios[i])
    #        i += 1
    #        print(servicio)
    #        print("Cargo Automatico: " + str(self.__CargoAutomatico))
    #        print("------------------------------------")

    #    if(self.__CargoAutomatico == 0):
    #        print("\nNo hay Saldo Pendiente")
        # Si hay saldo pendiente
    #    else:
    #        print("\nSaldo Pendiente")
    #    return salida

    def CapturaInformacion(self):
        self.__propietario = input("Nombre del propietario\n")
        self.__MontoDisponible = input("Monto disponible\n")
        self.__CargoAutomatico = input("Cargo Automatico:\n")

    @property
    def Servicios(self):
        return self.__servicios

    @Servicios.setter
    def Servicios(self, NuevoServicio):
        self.__servicios.append(NuevoServicio)
        print("El servicio {} ha sido añadido a la lista de servicios: {}".format(
            NuevoServicio, self.__servicios))

    @Servicios.setter
    def Servicios(self, NuevoServicio):
        self.Servicios = NuevoServicio

     # Getter del Cargo Automatico
    @property
    def CargoAutomatico(self):
        return self.__CargoAutomatico

    # Setter del Cargo automatico
    @CargoAutomatico.setter
    def CargoAutomatico(self, CargoAutomatico):
        self.__CargoAutomatico = CargoAutomatico

    # @property
    # def OperacionVigente(self):
    #    return self.__OperacionVigente

    # Setter de la operacion Vigente
    # @OperacionVigente.setter
    # def OperacionVigente(self, OperacionVigente):
    #    self.__OperacionVigente = OperacionVigente


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
        # print("Se ha añadido {} a los servicios públicos".format(
        #    EmpresaServicioPublico))

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

'''
+++++++++++++++++++++++++++++++++
+ Aplicación de agencia bancaria+ 
+++++++++++++++++++++++++++++++++
'''


class agenciabancaria():

    def __init__(self):
        self.__lista = list()

    def __menu_usuarios(self):
        print(" ==================================================== ")
        print(" [1] Agregar UsuarioAhorro")
        print(" [2] Agregar UsuarioTasaCero")
        print(" [3] Agregar UsuariosPagoServicios")
        print(" [4] Mostrar lista de usuarios")
        print(" [5] Asignar fondos")
        print(" [6] Asignar operaciones")
        print(" [7] Procesar Inversiones")
        print(" [8] Finalizar")
        print(" ==================================================== ")
        return input("> ")

    # def __agregarusuarios(self, UsuarioBase):
    def RUN(self):
        lista = []
        respuesta = ""
        while respuesta != "0":
            respuesta = self.__menu_usuarios()
            if respuesta == "1":
                print("Agregando un UsuarioAhorro")
                usuario = UsuarioAhorro()
                usuario.CapturaInformacion()
                # self.__lista.append(usuario)
                lista.append(usuario)

            elif respuesta == "2":
                # print("Asigando un UsuarioTasaCero %s" % UsuarioBase)
                UsuarioTasaCero1 = UsuarioTasaCero()
                UsuarioTasaCero1.CapturaInformacion()
                # self.__lista.append(UsuarioTasaCero1)
                lista.append(UsuarioTasaCero1)

            elif respuesta == "3":
                # print("Asigando un UsuarioPagoServicios %s" % UsuarioBase)
                # propietario = self.Input("Nombre del propietario")
                # MontoDisponible = self.Input("Monto disponible")
                # U1 = UsuarioPagoServicios(propietario, MontoDisponible, lista)
                # lista.append(U1)
                print("Agregando Usuario Pago Servicios")
                servicio = []
                i = [1, 2, 3]
                for iteracion in i:
                    print(
                        "Escriba el Servicio a debitar. Presione algun numero para finalizar\n")
                    servicios = input()
                    servicio.append(servicios)
                    iteracion += 1
                usuario = UsuarioPagoServicios(servicio)
                lista.append(usuario)
                print("Agregando Usuario Pago Servicios")
                usuario.CapturaInformacion()

            elif respuesta == "4":
                # print("Mostrando lista de usuarios %s" % UsuarioBase)
                for i in range(len(lista)):
                    print(str(lista[i]))

            elif respuesta == "5":
                for usuario in lista:
                    # Metodo Asignar para Usuario Ahorro
                    if usuario == UsuarioAhorro():
                        usuario.Asignar()
                    # Metodo Asignar para Usuario Tasa Cero
                    elif usuario == UsuarioTasaCero():
                        usuario.Asignar()
                    # Metodo Asignar para Usuario Pago Servicios
                    elif usuario == UsuarioPagoServicios():
                        usuario.Asignar()

            # Asignar Fondos
            elif respuesta == "6":
                for usuario in lista:
                    # Metodo Asignar para Usuario Ahorro
                    if usuario == UsuarioAhorro():
                        usuario.Aplicar()
                    # Metodo Asignar para Usuario Tasa Cero
                    elif usuario == UsuarioTasaCero():
                        usuario.Aplicar()
                    # Metodo Asignar para Usuario Pago Servicios
                    elif usuario == UsuarioPagoServicios():
                        usuario.Aplicar()
        return lista

    def __mostrarLista(self):
        for i in range(len(self.__lista)):
            print(self.__lista[i])


Test = agenciabancaria()
Test.RUN()
