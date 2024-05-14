##############################
#-------DATA EXTRACTER-------#
##############################
# Made by: Daniel Chacón Mora#
##############################

# NO NEED TO EDIT
# This code is meant to be use in every run made
# Count directories in picorv32a/run 
# Find latest run and its 2-stat.log

# Librerías ustilizadas
import re
import math
import numpy as np
import cmath
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gmean
import os
import shutil
from pathlib import Path

import os


####################
# Count directories#
####################



# Specify the parent directory
parent_directory = "/home/nephilim/OpenLane/designs/picorv32a/runs"

directory_count = 0

# List all subdirectories and sort by creation time (oldest first)
all_subdirectories = [os.path.join(parent_directory, d) for d in os.listdir(parent_directory) if os.path.isdir(os.path.join(parent_directory, d))]
all_subdirectories.sort(key=lambda x: os.path.getctime(x))

sorted_directories = all_subdirectories

# Loop through the sorted subdirectories
for directory in sorted_directories:
    # Enter each directory (perform your operations here)
    print(f"Entering directory: {directory}")
# Construct the path within the current directory
    synthesis_directory_path = os.path.join(directory, "logs", "synthesis")
    print(f"Synthesis directory path: {synthesis_directory_path}")
    synthesis_directory_path_str=str(synthesis_directory_path)
    
    ##################
    # Stats.log route#
    ##################

    # Search for the 2-sta.log file in the specified directory
    for root, dirs, files in os.walk(synthesis_directory_path_str):
        for file in files:
            if file == '2-sta.log':
                # Create the destination file with a .txt extension
                destination_file = os.path.join(synthesis_directory_path_str, '2-sta.txt')

                # Copy the 2-sta.log file to the destination with a .txt extension
                shutil.copy2(os.path.join(root, file), destination_file)

                print(f'Copied {file} to {destination_file}')
                break  

    print("Txt generado")

    # Read the text from the 2-stat.txt file
    file_path = os.path.join(synthesis_directory_path_str, "2-sta.txt")
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Initialize variables to track the lowest slack MAX and associated data times
    lowest_slack_MAX = None
    lowest_slack_MAX_data_required_time = None
    lowest_slack_MAX_data_arrival_time = None

    # Initialize variables to track the current section
    current_section_MAX = []
    inside_max_section = False  

    # Initialize variables to track the lowest slack MIN and associated data times
    lowest_slack_MIN = None
    lowest_slack_MIN_data_required_time = None
    lowest_slack_MIN_data_arrival_time = None

    # Initialize variables to track the current section
    current_section_MIN = []
    inside_min_section = False  

    ##############################################
    # This section of code analyse Path Type: MAX#
    ##############################################

    for line in lines:
        # Check if the line indicates the start of a "Path Type: max" section
        if line.startswith("Path Type: max"):
            inside_max_section = True  # We are now inside a "Path Type: max" section
            continue  
        
        # Check if the line indicates the start of a "Path Type: min" section
        if line.startswith("Path Type: min"):
            inside_max_section = False  # We are not inside a "Path Type: min" section
            continue  

        if inside_max_section:
            # Check if the line consists of dashes or spaces
            if all(char == '-' or char == ' ' for char in line.strip()):
                continue  # Skip lines with only dashes or spaces

            # Continue adding lines to the current section
            current_section_MAX.append(line)

            # Check if the line indicates the start of a new section
            if line.startswith("Startpoint:"):

                # If we're already inside a section, process the current one
                if current_section_MAX:
                    #print("Section made")
                    # Join the lines in the current section to form the section text
                    section_text = ''.join(current_section_MAX)
                    #print("Section text add")
                    # Use regex to find the slack value for this section
                    slack_match = re.search(r'([-+]?\d*\.\d+|\d+)\s+slack \((?:MET|VIOLATED)\)', section_text)
                    #print("Slack found: ", slack_match)
                    if slack_match:
                        slack_value = float(slack_match.group(1))
                        data_required_time_match = re.search(r'([-+]?\d*\.\d+|\d+)\s+data required time', section_text)
                        data_arrival_time_match = re.search(r'([-+]?\d*\.\d+|\d+)\s+data arrival time', section_text)
                        if data_required_time_match and data_arrival_time_match:
                            if lowest_slack_MAX is None or slack_value < lowest_slack_MAX:
                                lowest_slack_MAX = slack_value
                                lowest_slack_MAX_data_required_time = float(data_required_time_match.group(1))
                                lowest_slack_MAX_data_arrival_time = float(data_arrival_time_match.group(1))

                    # Clear the current section
                    current_section_MAX = []
                
                # Start building the new section
                current_section_MAX.append(line)
            else:
                # Continue adding lines to the current section
                current_section_MAX.append(line)

    ##############################################
    # This section of code analyse Path Type: MIN#
    ##############################################

    for line in lines:
        if line.startswith("Path Type: min"):
            inside_min_section = True  # We are now inside a "Path Type: min" section
            continue  
        
        # Check if the line indicates the start of a "Path Type: min" section
        if line.startswith("Path Type: max"):
            inside_min_section = False  # We are not inside a "Path Type: max" section
            continue  

        # Check if we are inside a "Path Type: min" section
        if inside_min_section:
            # Check if the line consists of dashes or spaces
            if all(char == '-' or char == ' ' for char in line.strip()):
                continue  # Skip lines with only dashes or spaces

            # Continue adding lines to the current section
            current_section_MIN.append(line)

            # Check if the line indicates the start of a new section
            if line.startswith("Startpoint:"):

                # If we're already inside a section, process the current one
                if current_section_MIN:
                    #print("Section made")
                    # Join the lines in the current section to form the section text
                    section_text = ''.join(current_section_MIN)
                    #print("Section text add")
                    # Use regex to find the slack value for this section
                    slack_match = re.search(r'([-+]?\d*\.\d+|\d+)\s+slack \((?:MET|VIOLATED)\)', section_text)
                    #print("Slack found: ", slack_match)
                    if slack_match:
                        slack_value = float(slack_match.group(1))
                        data_required_time_match = re.search(r'([-+]?\d*\.\d+|\d+)\s+data required time', section_text)
                        data_arrival_time_match = re.search(r'([-+]?\d*\.\d+|\d+)\s+data arrival time', section_text)
                        if data_required_time_match and data_arrival_time_match:
                            if lowest_slack_MIN is None or slack_value < lowest_slack_MIN:
                                lowest_slack_MIN = slack_value
                                lowest_slack_MIN_data_required_time = float(data_required_time_match.group(1))
                                lowest_slack_MIN_data_arrival_time = float(data_arrival_time_match.group(1))

                    
                    # Clear the current section
                    current_section_MIN = []
                
                # Start building the new section
                current_section_MIN.append(line)
            else:
                # Continue adding lines to the current section
                current_section_MIN.append(line)

    #################################################
    # This section of code analyse POWER CONSUMPTION#
    #################################################
    #txt_file_path = '/home/nephilim/OpenLane/designs/picorv32a/runs/RUN_2023.08.29_01.47.49/logs/synthesis/2-sta.txt'

    # Initialize variables to store the power values
    total_internal_power = None
    total_switching_power = None
    total_leakage_power = None
    total_power = None

    # Read the .txt file in reverse
    with open(file_path, 'r') as file:
        lines = file.readlines()[::-1]

    # Search for the lines containing the power information
    for line in lines:
        if line.startswith("Total"):
            values = line.split()
            if len(values) >= 5:
                total_internal_power = float(values[1])
                total_switching_power = float(values[2])
                total_leakage_power = float(values[3])
                total_power = float(values[4])
            break  # Stop searching once we find the "Total" line


    #################################
    # Analyze values and prints them#
    #################################

    # Check if any lowest slack MAX was found
    if lowest_slack_MAX is not None:
        print("Lowest Slack MAX:", lowest_slack_MAX)
        print("Data Required Time MAX:", lowest_slack_MAX_data_required_time)
        print("Data Arrival Time MAX:", lowest_slack_MAX_data_arrival_time)
    else:
        print("No data found for the lowest slack.")
    #//______________________________________________________________________
    # Check if any lowest slack MIN was found
    if lowest_slack_MIN is not None:
        print("Lowest Slack MIN:", lowest_slack_MIN)
        print("Data Required Time MIN:", lowest_slack_MIN_data_required_time)
        print("Data Arrival Time MIN:", lowest_slack_MIN_data_arrival_time)
    else:
        print("No data found for the lowest slack.")
    #//______________________________________________________________________
    # Print power values
    print("Total Internal Power:", total_internal_power)
    print("Total Switching Power:", total_switching_power)
    print("Total Leakage Power:", total_leakage_power)
    print("Total Power:", total_power)
    #//______________________________________________________________________
    # End of code.

    ################
    # Append to csv#
    ################
    csv_file_path = '/home/nephilim/OpenLane/designs/picorv32a/runs/tabla_data.csv'
        
    # General data
    df_general = pd.read_csv(csv_file_path)

    # Create a new column with sample data
    new_column_data = [lowest_slack_MAX_data_required_time, lowest_slack_MIN_data_required_time, 
                    lowest_slack_MAX_data_arrival_time,lowest_slack_MIN_data_arrival_time,
                    total_internal_power,total_switching_power,total_leakage_power,
                    total_power]  # Replace with your actual data

    # Add the new column to the DataFrame

    # General
    variable_general = "Test_" + str(directory_count)
    df_general[variable_general] = new_column_data
        
    # Save the updated DataFrame back to the CSV file

    # General
    df_general.to_csv(csv_file_path, index=False)  # Set index=False to avoid saving the index
    print("Nueva columna guardada")

    directory_count+=1