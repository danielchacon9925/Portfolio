############################################################
#####  Predictor de branches utilizando perceptrones. ######
############################################################
####                                                    ####
####                                                    ####
###### Estudiante: Daniel Chacón Mora                   ####
####                                                    ####
###### Carné: B72018                                    ####
############################################################


# Librerías

from math import floor
from gshared import *
from perceptron import *


class ie0521_bp:
    def __init__(self, bits_to_index, global_history_size):
        self.bits_to_index = bits_to_index
        self.size_of_branch_table = 2**bits_to_index
        self.global_history_size = global_history_size
        self.local_history_size = global_history_size

        # Valor de balance que indicará cuál predictor usar.
        # Representa la tendencia que tiene el resultado por un predictor u otro.
        # Comportamiento similar a un contador saturable.

        self.balance = 0

        #########################
        # Predictores utilizados#
        #########################

        # Instanciamos predictor de Perceptrones como predictor Local
        self.pred_local = perceptron(bits_to_index, global_history_size)

        # Instancio predictor de G_Shared como predictor global
        self.pred_global = gshared(bits_to_index, global_history_size)

        # Guarda el resultado del predictor global
        self.global_predic = 0
        # Guarda el resultado del predictor local
        self.local_predic = 0

        # Escriba aquí el init de la clase
        self.total_predictions = 0
        self.total_taken_pred_taken = 0
        self.total_taken_pred_not_taken = 0
        self.total_not_taken_pred_taken = 0
        self.total_not_taken_pred_not_taken = 0

        # Cantidad de veces que se utilizan los predictores
        self.perceptron_use = 0
        self.gshare_use = 0

    # //___________________________________________________________

    #################################################
    #### Código para imprimir valores de consola ####
    #################################################

    def print_info(self):
        print("Parámetros del predictor:")
        print("\tTipo de predictor:\t\t\tHybrid Perceptron + GShare")

    def print_stats(self):
        print("Resultados de la simulación")
        print("\t# branches:\t\t\t\t\t\t"+str(self.total_predictions))
        print("\t# branches tomados predichos correctamente:\t\t" +
              str(self.total_taken_pred_taken))
        print("\t# branches tomados predichos incorrectamente:\t\t" +
              str(self.total_taken_pred_not_taken))
        print("\t# branches no tomados predichos correctamente:\t\t" +
              str(self.total_not_taken_pred_not_taken))
        print("\t# branches no tomados predichos incorrectamente:\t" +
              str(self.total_not_taken_pred_taken))
        perc_correct = 100*(self.total_taken_pred_taken +
                            self.total_not_taken_pred_not_taken)/self.total_predictions
        formatted_perc = "{:.3f}".format(perc_correct)
        print("\t% predicciones correctas:\t\t\t\t"+str(formatted_perc)+"%")
        print("\t# Veces que se utilizó predictor de perceptrones:\t" +
              str(self.perceptron_use))
        print("\t# Veces que se utilizó predictor GShare:\t" +
              str(self.gshare_use))
    # //___________________________________________________________

    def predict(self, PC):

        # Función encargada de predecir el predictor

        # Predice con el metodo local(Perceptrons)
        self.local_predic = self.pred_local.predict(int(PC))

        # Predice con el metodo global(GShare)
        self.global_predic = self.pred_global.predict(int(PC))

        # Decide cual predictor se utiliza
        if self.balance in [0, 1]:
            # self.balance = 0
            mejor = self.local_predic

        else:
            # self.balance = 1
            mejor = self.global_predic
        return mejor
    # //___________________________________________________________

    def update(self, PC, result, prediction):

        # Actualiza mi predictor de predictores

        self.pred_global.update(PC, result, prediction)
        self.pred_local.update(PC, result, prediction)

        # Update balance
        if self.local_predic == result and self.global_predic != result:

            # Si el Gshare falla, se disminuye el balance en 1.
            # Haciendo uso de de la función max, se logra que el balance no sea negativo.

            self.balance = max(0, self.balance - 1)

            self.perceptron_use += 1

        elif self.local_predic != result and self.global_predic == result:

            # Si el de perceptrones falla, se incrementa en 1
            # Haciendo uso de la función min se logra que no se supere el 3.

            self.balance = min(3, self.balance + 1)

            self.gshare_use += 1

        # Update stats

        if result == "T" and result == prediction:
            self.total_taken_pred_taken += 1
        elif result == "T" and result != prediction:
            self.total_taken_pred_not_taken += 1
        elif result == "N" and result == prediction:
            self.total_not_taken_pred_not_taken += 1
        else:
            self.total_not_taken_pred_taken += 1

        self.total_predictions += 1
