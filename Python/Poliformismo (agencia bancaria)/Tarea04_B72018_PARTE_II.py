import sys
from abc import ABCMeta, abstractmethod
from Tarea04_B72018_PARTE_I import *


class agenciabancaria(UsuarioBase):

    def __init__(self):
        self.__facturas = list()

    def __menu(self):
        print(" ==================================================== ")
        print(" [1] Agregar UsuarioAhorro")
        print(" [2] Agregar UsuarioTasaCero")
        print(" [3] Agregar UsuariosPagoServicios")
        print(" [4] Mostrar lista de usuarios")
        print(" [5] Asignar operaciones")
        print(" ==================================================== ")
        return self.Input("> ")

    def __AgregarCompras(self, numero_factura):
        lista = list()
        respuesta = ""
        while respuesta != "0":
            respuesta = self.__menuCompras()
            if respuesta == "1":
                print("Agregando compra a factura número %s" % numero_factura)
                compra = Compra()
                compra.Captura()
                lista.append(compra)

            elif respuesta == "2":
                print("Mostrando todas las compras de factura número %s" %
                      numero_factura)
                for i in range(len(lista)):
                    print(lista[i])
                self.Input("Digite cualquier tecla para continuar")

            elif respuesta == "3":
                print(
                    "Se ha borrado la lista de pasajeros del local número %s" % numero_factura)
                lista.clear()
                self.Input("Digite cualquier tecla para continuar")

        return lista
