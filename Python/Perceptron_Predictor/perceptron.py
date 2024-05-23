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

import math  # Utilizada únicamente para calcular la parte entera de un número.
import time  # Utilizada únicamente observar tiempo de ejecución.


class perceptron:
    # Inicialización de objeto y atributos
    def __init__(self, bits_to_index, global_history_size):
        self.bits_to_index = bits_to_index
        # Cantidad de filas es brindado por 2**S, con S siendo los bits to index
        self.rows_of_perceptron_table = 2**bits_to_index
        self.global_history_size = global_history_size
        self.max_index_global_history = 2**self.global_history_size

        # El tamaño de los pesos debe ser igual al tamaño de la historia
        self.weight_size = global_history_size

        # Inicio de tabla de perceptrones
        # Esta tabla tiene self.rows_of_perceptron_table filas.
        # Cantidad de columnas es del largo del peso
        self.perceptron_table = [[0 for j in range(
            self.weight_size + 1)] for i in range(self.rows_of_perceptron_table)]

        # Inicio de GHR
        # Su tamaño está definido por el global_history_size
        # if self.global_history_size > self.bits_to_index:
        #    print("El tamaño del registro de historia es mayor que los bits para indexar la tabla se limitará el registro a " +
        #          str(self.bits_to_index) + "bits")
        #    self.global_history_size = self.bits_to_index
        # bias_GHR = "1"

        # Se llena el GHR con el bias de primero, y el resto como Not taken
        self.global_history_reg = "1"
        for i in range(global_history_size):
            self.global_history_reg += "0"

        # Construcción de threshold
        self.threshold = math.floor(1.93*global_history_size + 14)

        # Cambios en perceptrones
        self.perceptronSteps = 0

        self.total_predictions = 0
        self.total_taken_pred_taken = 0
        self.total_taken_pred_not_taken = 0
        self.total_not_taken_pred_taken = 0
        self.total_not_taken_pred_not_taken = 0

        self.start_time = 0
        self.end_time = 0

        self.execution_time = 0

    #################################################
    #### Código para imprimir valores de consola ####
    #################################################

    def print_info(self):
        print("Parámetros del predictor:")
        print("\tTipo de predictor:\t\t\tPerceptron")

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

    ###################################################

    # Predicción
    def predict(self, PC):

        # Se mapea el PC para producir índice en tabla de perceptrones
        perceptron_index = int(PC) % self.rows_of_perceptron_table

        # Inicialización de predicciones
        prediction = 0

        # Se incrementa el valor de la predicción con el valor en la tabla indicado por el índice
        prediction += self.perceptron_table[perceptron_index][0]

        for i in range(self.global_history_size + 1):
            # Si en el GHR el bit es Taken, se incrementa el perceptron

            if self.global_history_reg[i-1] == "1":
                x_i = 1

                # Peso
                w_i = self.perceptron_table[perceptron_index][i]

                # y = w_i*x_1
                prediction += w_i*x_i

            # Si en el GHR el bit es Not Taken, se disminuye el perceptron
            else:
                x_i = -1

                # Peso
                w_i = self.perceptron_table[perceptron_index][i]

                # y = w_i*x_i
                prediction += w_i*x_i

        # Se actualiza el paso del perceptron al valor absoluto de la predicción
        # Con este parámetro puedo saber si se alcanzó el threshold
        self.perceptronSteps = abs(prediction)

        # Si la predicción es mayor a cero, take the branch
        if prediction >= 0:
            return "T"
        # Si la predicción es menor a cero, dont take the branch
        else:
            return "N"

    def update(self, PC, result, prediction):

        # Se mapea el PC para producir índice en tabla de perceptrones
        perceptron_index = int(PC) % self.rows_of_perceptron_table

        # Se mapea el PC para producir índice en tabla de perceptrones
        perceptron_index = int(PC) % self.rows_of_perceptron_table
        if result == "T":
            t = 1
        else:
            t = -1

        # Para poder actualizar el peso, es necesario saber como es la predicción

        # Inicialización de predicciones
        y = 0
        # Se incrementa el valor de la predicción con el valor en la tabla indicado por el índice
        y += self.perceptron_table[perceptron_index][0]

        for i in range(self.global_history_size + 1):
            # Si en el GHR el bit es Taken, se incrementa el perceptron

            if self.global_history_reg[i-1] == "1":
                x_i = 1

                # Peso
                w_i = self.perceptron_table[perceptron_index][i]

                # y = w_i*x_1
                y += w_i*x_i

            # Si en el GHR el bit es Not Taken, se disminuye el perceptron
            else:
                x_i = -1

                # Peso
                w_i = self.perceptron_table[perceptron_index][i]

                # y = w_i*x_i
                y += w_i*x_i

        # Training
        if (y * t) <= 0 or abs(y) <= self.threshold:

            for i in range(self.global_history_size+1):
                if i == 0:
                    # Peso
                    # w_i = self.perceptron_table[perceptron_index][i]

                    # w_i = w_i + t

                    self.perceptron_table[perceptron_index][i] = self.perceptron_table[perceptron_index][i] + t
                else:
                    # Peso
                    # w_i = self.perceptron_table[perceptron_index][i]

                    if int(self.global_history_reg[i-1]) == 1:
                        # Peso
                        # w_i = self.perceptron_table[perceptron_index][i]
                        # w_i = w_i + 1*t
                        self.perceptron_table[perceptron_index][i] = self.perceptron_table[perceptron_index][i] + 1*t
                    else:
                        # Peso
                        # w_i = self.perceptron_table[perceptron_index][i]
                        # w_i = w_i + (-1)*t
                        self.perceptron_table[perceptron_index][i] = self.perceptron_table[perceptron_index][i] + \
                            (-1)*t

        # Update GHR
        if result == "T":
            self.global_history_reg = self.global_history_reg[-self.global_history_size+1:] + "1"
        else:
            self.global_history_reg = self.global_history_reg[-self.global_history_size+1:] + "0"

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
