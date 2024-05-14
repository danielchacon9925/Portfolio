##########################
# PERIOD_UTIL_RANDOMIZER #
###################################
# Proyecto Eléctrico-II Ciclo 2023#
###################################

# This code generates random test for clk period or FP CORE UTIL with user interaction
# User provides design and number of test
# Report is generated


# Made by Daniel Chacón Mora


# Libraries
import os
import random
import json
import subprocess
from pathlib import Path

'''
Este código permite encontrar el valor al que se completa el flujo exitosamente.

Usuario indica que experimento desea realizar:
    0. Periodo de clk
    1. Porcentaje de utilización del área del core.


Las funciones solicitan al usuario:
    1. Diseño con el que se desea experimentar.
    2. Cantidad de iteraciones para realizar pruebas.

Se recomienda utilizar gran cantidad de iteraciones diseños grandes (con muchas celdas como el picorv32a)
'''

'''
    Se busca en el archivo config.json si se encuentra la CLOCK_PERIOD para capturar valor, si no
se encuentra le introduce uno de 0.5 ns. Se corre el flujo utilizando entre 5% al 8% del valor 
capturado (o insertado) que fallará. 
    A partir del error de la  ejecución, se correrá el flujo sumando 1ns por iteración hasta que 
el flujo no falle.
    Se escrite un reporte en cada iteración indicando el valor utilizado para poder identificar el 
valor al que el experimento funcionó.
'''

# Función que prueba el periodo del reloj.

def randomizer(variable, cantidad):

    ####################
    # Read config.json #
    ####################
    # Path
    file_path = os.path.join("designs", variable, "config.json")
    # Open Json
    with open(file_path, 'r') as json_file:
        config = json.load(json_file)

    # Extract the value of "CLOCK_PERIOD"
    clock_period = config.get("CLOCK_PERIOD")

    # Check if "CLOCK_PERIOD" exists in config.json
    if clock_period is None:
        clock_period = 0.5
        msj = "No hay clk period fijo. Se procede a añadir uno de 0.5 para posterior escalamiento"
        print(msj)
        # If not, add "CLOCK_PERIOD" with a default value
        config["CLOCK_PERIOD"] = clock_period
        # Save config on dictionary
        with open(file_path, 'w') as json_file:
            json.dump(config, json_file, indent=4)

    # Print the result
    print(f'The value of default "CLOCK_PERIOD" is: {clock_period}')

    # Definir las variables
    COUNTER = 0  # Puedes establecer esto en el valor apropiado

    ################
    # Run directory#
    ################

    # Run directory
    origin_directory = "/home/nephilim/OpenLane/designs"
    latest_run_directory = "runs"
    subdirectory = os.path.join(variable, latest_run_directory)
    run_directory_a = os.path.join(origin_directory, subdirectory)
    run_directory = str(run_directory_a)

    print("run directory: ", run_directory)

    percent = round(random.uniform(0.05, 0.08))

    # Set random initial value
    clock_new = clock_period * percent

    # Report name
    file_name = f"{variable}_{cantidad}_{clock_period}.txt"

    for COUNTER in range(int(cantidad)):

        # Update value on config.json
        config["CLOCK_PERIOD"] = clock_new

        ################################
        # Write configuration in report#
        ################################

        # Build tag
        TAG = f"{variable}_RUN_{COUNTER}_{clock_new}"

        report_msj = f"The TAG {TAG} has been created using the {percent} clk period from the original {clock_period} for {variable} with the new clk period {clock_new}"

        # Write configuration on txt report
        with open(file_name, "a") as txt_file:
            txt_file.write(report_msj + "\n")

        ###################
        # Update dictinary#
        ###################

        # Save config on dictionary
        with open(file_path, 'w') as json_file:
            json.dump(config, json_file, indent=4)

        ################
        # Execute flow #
        ################

        # Command
        command = f"./flow.tcl -design {variable} -tag {TAG}"
        # Execute
        try:
            os.system(command)
        except Exception as e:
            print(f"Ocurrió un error: {e}")

        # Construye la ruta completa al archivo errors.log
        errors_log_path_tag = Path(run_directory) / TAG
        print("Path al TAG: ", errors_log_path_tag)
        errors_log_path_a = errors_log_path_tag / "errors.log"
        errors_log_path = str(errors_log_path_a)
        print("Path al run: ", errors_log_path)

        print("errors_log_path: ", errors_log_path)
        # Verifica si el archivo errors.log existe en el directorio run_directory
        if os.path.exists(errors_log_path):
            print("Falló")
            print("EL clk period con el que falló es: ", clock_new)

            report_msj = f"TAG {TAG} is for failed flow. The clk period is {clock_new}"

            # Write configuration on txt report
            with open(file_name, "a") as txt_file:
                txt_file.write(report_msj + "\n")

            print(f'El archivo errors.log existe en {errors_log_path}')

            clock_new = (clock_new + 1)

            # Update value on config.json
            config["CLOCK_PERIOD"] = clock_new

            print("Nuevo clk period: ", clock_new)

        else:
            print(f'El archivo errors.log no existe en {errors_log_path}')
            print("Flow completo exitoso")
            report_msj = f"TAG {TAG} is for succesful flow. The clk period is {clock_new}"
            # Write configuration on txt report
            with open(file_name, "a") as txt_file:
                txt_file.write(report_msj + "\n")

            print("El reporte del experimento se llama: ", file_name)
            break


# Función que prueba el porcentaje de utilización.

def randomizer_util(variable, cantidad):

    ####################
    # Read config.json #
    ####################
    # Path
    file_path = os.path.join("designs", variable, "config.json")
    # Open Json
    with open(file_path, 'r') as json_file:
        config = json.load(json_file)

    # Extract the value of "FP_CORE_UTIL"
    util_original = config.get("FP_CORE_UTIL")

    # Check if "CLOCK_PERIOD" exists in config.json
    if util_original is None:
        util_original = 0.20
        msj = "No hay FP_CORE_UTIL fijo. Se procede a añadir uno de 0.05 para posterior escalamiento"
        print(msj)
        # If not, add "CLOCK_PERIOD" with a default value
        config["FP_CORE_UTIL"] = util_original
        # Save config on dictionary
        with open(file_path, 'w') as json_file:
            json.dump(config, json_file, indent=4)

    # Print the result
    print(f'The value of default "FP_CORE_UTIL" is: {util_original}')

    # Definir las variables
    COUNTER = 0  # Puedes establecer esto en el valor apropiado

    ################
    # Run directory#
    ################

    # Run directory
    origin_directory = "/home/nephilim/OpenLane/designs"
    latest_run_directory = "runs"
    subdirectory = os.path.join(variable, latest_run_directory)
    run_directory_a = os.path.join(origin_directory, subdirectory)
    run_directory = str(run_directory_a)

    print("run directory: ", run_directory)

    percent = random.uniform(0.05, 0.10)

    # Set random initial value
    util_new = round(util_original * percent)

    # Report name
    file_name = f"{variable}_COREUTIL_{cantidad}_{util_original}.txt"

    for COUNTER in range(int(cantidad)):

        # Update value on config.json
        config["FP_CORE_UTIL"] = util_new

        ################################
        # Write configuration in report#
        ################################

        # Build tag
        TAG = f"{variable}_COREUTIL_RUN_{COUNTER}_{util_new}"

        report_msj = f"The TAG {TAG} has been created using the {percent} FP CORE UTIL from the original {util_original} for {variable} with the new FP CORE UTIL {util_new}"

        # Write configuration on txt report
        with open(file_name, "a") as txt_file:
            txt_file.write(report_msj + "\n")

        ###################
        # Update dictinary#
        ###################

        # Save config on dictionary
        with open(file_path, 'w') as json_file:
            json.dump(config, json_file, indent=4)

        ################
        # Execute flow #
        ################

        # Command
        command = f"./flow.tcl -design {variable} -tag {TAG}"
        # Execute
        try:
            os.system(command)
        except Exception as e:
            print(f"Ocurrió un error: {e}")

        # Construye la ruta completa al archivo errors.log
        errors_log_path_tag = Path(run_directory) / TAG
        print("Path al TAG: ", errors_log_path_tag)
        errors_log_path_a = errors_log_path_tag / "errors.log"
        errors_log_path = str(errors_log_path_a)
        print("Path al run: ", errors_log_path)

        print("errors_log_path: ", errors_log_path)
        # Verifica si el archivo errors.log existe en el directorio run_directory
        if os.path.exists(errors_log_path):
            print("Falló")
            print("El FP CORE UTIL con el que falló es: ", util_new)

            report_msj = f"TAG {TAG} is for failed flow. The FP CORE UTIL is {util_new}"

            # Write configuration on txt report
            with open(file_name, "a") as txt_file:
                txt_file.write(report_msj + "\n")

            print(f'El archivo errors.log existe en {errors_log_path}')

            # 5% addded to the FP_CORE_UTIL
            util_new = (util_new + 5)

            # Update value on config.json
            config["FP_CORE_UTIL"] = util_new

            print("Nuevo FP CORE UTIL: ", util_new)

        else:
            print(f'El archivo errors.log no existe en {errors_log_path}')
            print("Flow completo exitoso")
            report_msj = f"TAG {TAG} is for succesful flow. The FP CORE UTIL is {util_new}"
            # Write configuration on txt report
            with open(file_name, "a") as txt_file:
                txt_file.write(report_msj + "\n")

            print("El reporte del experimento se llama: ", file_name)
            break


print("Indique 0 si desea evaluar periodo o 1 si desea evaluar porcentaje de utilización")
seleccion = int(input("Seleccione modo de funcionamiento: "))

if seleccion == 0:
    print("Ha escogido evaluar periodo")
    print("Indique el diseño que desea randomizar")
    variable = input("Variable: ")
    print("Indique cantidad de pruebas")
    cantidad = input("Cantidad: ")
    randomizer(variable, cantidad)
elif seleccion == 1:
    print("Ha escogido evaluar utilización")
    print("Indique el diseño que desea randomizar")
    variable = input("Variable: ")
    print("Indique cantidad de pruebas")
    cantidad = input("Cantidad: ")
    randomizer_util(variable, cantidad)
else:
    print("Ha introducido un valor de selección inválido.")
