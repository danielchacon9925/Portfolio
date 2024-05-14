##############
# Randomizer #
##############

# This code generates random test with user interaction
# User provides design and number of test
# Report is generated

# Made by Daniel Chacón Mora


# Libraries
import os
import random
import json
import subprocess

# Main function
def randomizer(variable, cantidad):

    ####################
    # Read config.json #
    ####################
    # Path
    file_path = os.path.join("designs", variable, "config.json")
    # Open Json
    with open(file_path, 'r') as json_file:
        config = json.load(json_file)

    # Definir las variables

    COUNTER = 0  # Puedes establecer esto en el valor apropiado

    # Definir las optimizaciones posibles
    list_optimizations = [
        {"SYNTH_STRATEGY": "DELAY " + str(random.randint(0, 4))},
        {"SYNTH_STRATEGY": "AREA " + str(random.randint(0, 3))},
        {"SYNTH_ADDER_TYPE": random.choice(["YOSYS", "FA", "RCA", "CSA"])},
        {"SYNTH_BUFFERING": str(random.randint(0, 1))},
        {"SYNTH_BUFFER_DIRECT_WIRES": str(random.randint(0, 1))},

        {"FP_CORE_UTIL": str(random.randint(0, 50))},
        {"FP_ASPECT_RATIO": str(random.randint(1, 2))},

        # {"PL_TARGET_DENSITY": str(random.randint(0, 1))},
        {"PL_TARGET_DENSITY": str(1)},
        {"PL_TIME_DRIVEN": str(random.randint(0, 1))},
        {"PL_ROUTABILITY_DRIVEN": str(random.randint(0, 1))},

        {"GLB_RESIZER_TIMING_OPTIMIZATIONS": str(random.randint(0, 1))},
        {"GLB_RESIZER_DESIGN_OPTIMIZATIONS ": str(random.randint(0, 1))},
        {"GLB_RESIZER_MAX_WIRE_LENGTH": str(random.randint(0, 1))},

    ]

    # Report name
    file_name = f"{variable}{cantidad}.txt"

    for COUNTER in range(int(cantidad)):

        ##################################
        # Random configuration selection #
        ##################################

        random_optimization = random.choice(list_optimizations)

        ################################
        # Write configuration in report#
        ################################

        report_msj = f"A new test has been created using the optimization: {random_optimization}. The run is {variable}_RUN_{COUNTER}"

        # Write configuration on txt report
        with open(file_name, "a") as txt_file:
            txt_file.write(report_msj + "\n")

        ###################
        # Update dictinary#
        ###################

        # Add new config
        config.update(random_optimization)

        # Save config on dictionary
        with open(file_path, 'w') as json_file:
            json.dump(config, json_file, indent=4)

        ################
        # Execute flow #
        ################

        # Build tag
        TAG = f"{variable}_RUN_{COUNTER}"
        # Command
        command = f"./flow.tcl -design {variable} -tag {TAG}"
        # Execute
        try:
            os.system(command)
        except Exception as e:
            print(f"Ocurrió un error: {e}")

        ###############
        # Clear config#
        ###############

        # Open Json
        with open(file_path, 'r') as json_file:
            config = json.load(json_file)

        # Pop last item
        config.popitem()

        # Save dictionary
        with open(file_path, 'w') as json_file:
            json.dump(config, json_file, indent=4)

        # Replace 'script.py' with the name of your Python file
        script_file = 'EXTRACTER.py'

        # Execute the Python script
        result = subprocess.run(['python', script_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

        # Increment counter
        COUNTER += 1


print("Indique el diseño que desea randomizar")
variable = input("Variable: ")
print("Indique cantidad de pruebas")
cantidad = input("Cantidad: ")

# Llamar a la función
randomizer(variable, cantidad)
