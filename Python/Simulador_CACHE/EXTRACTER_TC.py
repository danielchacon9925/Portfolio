############
# Extracter#
############

# Se van realizando extracciones según tamaño secuencialmente

# Extrae datos y adjunta en dataframe
import re

# Librerías ustilizadas
import re
import math
import numpy as np
import cmath
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gmean


##########################################
# Extractor para experimento con tamaño 8#
##########################################


# Creación de tablas para adjuntar valores
# Una tabla por tamaño
tabla_TC8 = pd.DataFrame(index=[
    '400.perlbench-41B', '401.bzip2-226B', '403.gcc-16B', '410.bwaves-1963B', '416.gamess-875B', '429.mcf-184B', '433.milc-127B',
    '435.gromacs-111B', '436.cactusADM-1804B', '437.leslie3d-134B', '444.namd-120B', '445.gobmk-17B',
    '450.soplex-247B', '453.povray-887B', '454.calculix-104B', '456.hmmer-191B', '458.sjeng-1088B', '459.GemsFDTD-1169B',
    '462.libquantum-1343B', '464.h264ref-30B', '465.tonto-1769B', '470.lbm-1274B', '471.omnetpp-188B', '473.astar-153B', '481.wrf-1170B',
    '482.sphinx3-1100B', '483.xalancbmk-127B'], columns=[
    'App', 'Total Misses', 'Miss rate total [%]', 'Misses lectura', 'Miss rate lectura [%]', 'Misses escritura', 'Miss rate escritura [%]'])
tabla_TC8['App'] = tabla_TC8.index

# Files paths
filename_1 = "RESULTS_TC/400TC8.txt"
filename_2 = "RESULTS_TC/401TC8.txt"
filename_3 = "RESULTS_TC/403TC8.txt"
filename_4 = "RESULTS_TC/410TC8.txt"
filename_5 = "RESULTS_TC/416TC8.txt"
filename_6 = "RESULTS_TC/429TC8.txt"
filename_7 = "RESULTS_TC/433TC8.txt"
filename_8 = "RESULTS_TC/435TC8.txt"
filename_9 = "RESULTS_TC/436TC8.txt"
filename_10 = "RESULTS_TC/437TC8.txt"
filename_11 = "RESULTS_TC/444TC8.txt"
filename_12 = "RESULTS_TC/445TC8.txt"
filename_13 = "RESULTS_TC/450TC8.txt"
filename_14 = "RESULTS_TC/453TC8.txt"
filename_15 = "RESULTS_TC/454TC8.txt"
filename_16 = "RESULTS_TC/456TC8.txt"
filename_17 = "RESULTS_TC/458TC8.txt"
filename_18 = "RESULTS_TC/459TC8.txt"
filename_19 = "RESULTS_TC/462TC8.txt"
filename_20 = "RESULTS_TC/464TC8.txt"
filename_21 = "RESULTS_TC/465TC8.txt"
filename_22 = "RESULTS_TC/470TC8.txt"
filename_23 = "RESULTS_TC/471TC8.txt"
filename_24 = "RESULTS_TC/473TC8.txt"
filename_25 = "RESULTS_TC/481TC8.txt"
filename_26 = "RESULTS_TC/482TC8.txt"
filename_27 = "RESULTS_TC/483TC8.txt"


# Content file extracter
with open(filename_1, 'r') as file:
    content_400TC8 = file.read()
with open(filename_2, 'r') as file:
    content_401TC8 = file.read()
with open(filename_3, 'r') as file:
    content_403TC8 = file.read()
with open(filename_4, 'r') as file:
    content_410TC8 = file.read()
with open(filename_5, 'r') as file:
    content_416TC8 = file.read()
with open(filename_6, 'r') as file:
    content_429TC8 = file.read()
with open(filename_7, 'r') as file:
    content_433TC8 = file.read()
with open(filename_8, 'r') as file:
    content_435TC8 = file.read()
with open(filename_9, 'r') as file:
    content_436TC8 = file.read()
with open(filename_10, 'r') as file:
    content_437TC8 = file.read()
with open(filename_11, 'r') as file:
    content_444TC8 = file.read()
with open(filename_12, 'r') as file:
    content_445TC8 = file.read()
with open(filename_13, 'r') as file:
    content_450TC8 = file.read()
with open(filename_14, 'r') as file:
    content_453TC8 = file.read()
with open(filename_15, 'r') as file:
    content_454TC8 = file.read()
with open(filename_16, 'r') as file:
    content_456TC8 = file.read()
with open(filename_17, 'r') as file:
    content_458TC8 = file.read()
with open(filename_18, 'r') as file:
    content_459TC8 = file.read()
with open(filename_19, 'r') as file:
    content_462TC8 = file.read()
with open(filename_20, 'r') as file:
    content_464TC8 = file.read()
with open(filename_21, 'r') as file:
    content_465TC8 = file.read()
with open(filename_22, 'r') as file:
    content_470TC8 = file.read()
with open(filename_23, 'r') as file:
    content_471TC8 = file.read()
with open(filename_24, 'r') as file:
    content_473TC8 = file.read()
with open(filename_25, 'r') as file:
    content_481TC8 = file.read()
with open(filename_26, 'r') as file:
    content_482TC8 = file.read()
with open(filename_27, 'r') as file:
    content_483TC8 = file.read()


# Variables según aplicación

# 400.pearlbench-41B
total_misses_400TC8 = re.search(r"Total_misses (\d+)", content_400TC8).group(1)
total_miss_rate_400TC8 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_400TC8).group(1)
total_read_misses_400TC8 = re.search(
    r"Total_read_misses (\d+)", content_400TC8).group(1)
total_read_miss_rate_400TC8 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_400TC8).group(1)
total_write_misses_400TC8 = re.search(
    r"Total_write_misses (\d+)", content_400TC8).group(1)
total_write_miss_rate_400TC8 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_400TC8).group(1)
print(">>>>>All TC8 400.pearlbench-41B variables where obtained successfully")

# 401.bzip2-226B
total_misses_401TC8 = re.search(r"Total_misses (\d+)", content_401TC8).group(1)
total_miss_rate_401TC8 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_401TC8).group(1)
total_read_misses_401TC8 = re.search(
    r"Total_read_misses (\d+)", content_401TC8).group(1)
total_read_miss_rate_401TC8 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_401TC8).group(1)
total_write_misses_401TC8 = re.search(
    r"Total_write_misses (\d+)", content_401TC8).group(1)
total_write_miss_rate_401TC8 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_401TC8).group(1)
print(">>>>>All TC8 401.bzip2-226B variables where obtained successfully")

# 403.gcc-16B
total_misses_403TC8 = re.search(r"Total_misses (\d+)", content_403TC8).group(1)
total_miss_rate_403TC8 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_403TC8).group(1)
total_read_misses_403TC8 = re.search(
    r"Total_read_misses (\d+)", content_403TC8).group(1)
total_read_miss_rate_403TC8 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_403TC8).group(1)
total_write_misses_403TC8 = re.search(
    r"Total_write_misses (\d+)", content_403TC8).group(1)
total_write_miss_rate_403TC8 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_403TC8).group(1)
print(">>>>>All TC8 403.gcc-16B variables where obtained successfully")

# 410.bwaves-1963B
total_misses_410TC8 = re.search(r"Total_misses (\d+)", content_410TC8).group(1)
total_miss_rate_410TC8 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_410TC8).group(1)
total_read_misses_410TC8 = re.search(
    r"Total_read_misses (\d+)", content_410TC8).group(1)
total_read_miss_rate_410TC8 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_410TC8).group(1)
total_write_misses_410TC8 = re.search(
    r"Total_write_misses (\d+)", content_410TC8).group(1)
total_write_miss_rate_410TC8 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_410TC8).group(1)
print(">>>>>All TC8 410.bwaves-1963B variables where obtained successfully")

# 416.gamess-875B
total_misses_416TC8 = re.search(r"Total_misses (\d+)", content_416TC8).group(1)
total_miss_rate_416TC8 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_416TC8).group(1)
total_read_misses_416TC8 = re.search(
    r"Total_read_misses (\d+)", content_416TC8).group(1)
total_read_miss_rate_416TC8 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_416TC8).group(1)
total_write_misses_416TC8 = re.search(
    r"Total_write_misses (\d+)", content_416TC8).group(1)
total_write_miss_rate_416TC8 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_416TC8).group(1)
print(">>>>>All TC8 416.gamess-875B variables where obtained successfully")

# 429.mcf-184B
total_misses_429TC8 = re.search(r"Total_misses (\d+)", content_429TC8).group(1)
total_miss_rate_429TC8 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_429TC8).group(1)
total_read_misses_429TC8 = re.search(
    r"Total_read_misses (\d+)", content_429TC8).group(1)
total_read_miss_rate_429TC8 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_429TC8).group(1)
total_write_misses_429TC8 = re.search(
    r"Total_write_misses (\d+)", content_429TC8).group(1)
total_write_miss_rate_429TC8 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_429TC8).group(1)
print(">>>>>All TC8 429.mcf-184B variables where obtained successfully")

# 433.milc-127B
total_misses_433TC8 = re.search(r"Total_misses (\d+)", content_433TC8).group(1)
total_miss_rate_433TC8 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_433TC8).group(1)
total_read_misses_433TC8 = re.search(
    r"Total_read_misses (\d+)", content_433TC8).group(1)
total_read_miss_rate_433TC8 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_433TC8).group(1)
total_write_misses_433TC8 = re.search(
    r"Total_write_misses (\d+)", content_433TC8).group(1)
total_write_miss_rate_433TC8 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_433TC8).group(1)
print(">>>>>All TC8 433.milc-127B variables where obtained successfully")

# 435.gromacs-111B
total_misses_435TC8 = re.search(r"Total_misses (\d+)", content_435TC8).group(1)
total_miss_rate_435TC8 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_435TC8).group(1)
total_read_misses_435TC8 = re.search(
    r"Total_read_misses (\d+)", content_435TC8).group(1)
total_read_miss_rate_435TC8 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_435TC8).group(1)
total_write_misses_435TC8 = re.search(
    r"Total_write_misses (\d+)", content_435TC8).group(1)
total_write_miss_rate_435TC8 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_435TC8).group(1)
print(">>>>>All TC8 435.gromacs-111B variables where obtained successfully")

# 436.cactusADM-1804B
total_misses_436TC8 = re.search(r"Total_misses (\d+)", content_436TC8).group(1)
total_miss_rate_436TC8 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_436TC8).group(1)
total_read_misses_436TC8 = re.search(
    r"Total_read_misses (\d+)", content_436TC8).group(1)
total_read_miss_rate_436TC8 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_436TC8).group(1)
total_write_misses_436TC8 = re.search(
    r"Total_write_misses (\d+)", content_436TC8).group(1)
total_write_miss_rate_436TC8 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_436TC8).group(1)
print(">>>>>All TC8 436.cactusADM-1804B variables where obtained successfully")

# 437.leslie3d-134B
total_misses_437TC8 = re.search(r"Total_misses (\d+)", content_437TC8).group(1)
total_miss_rate_437TC8 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_437TC8).group(1)
total_read_misses_437TC8 = re.search(
    r"Total_read_misses (\d+)", content_437TC8).group(1)
total_read_miss_rate_437TC8 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_437TC8).group(1)
total_write_misses_437TC8 = re.search(
    r"Total_write_misses (\d+)", content_437TC8).group(1)
total_write_miss_rate_437TC8 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_437TC8).group(1)
print(">>>>>All TC8 437.leslie3d-134B variables where obtained successfully")

# 444.namd-120B
total_misses_444TC8 = re.search(r"Total_misses (\d+)", content_444TC8).group(1)
total_miss_rate_444TC8 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_444TC8).group(1)
total_read_misses_444TC8 = re.search(
    r"Total_read_misses (\d+)", content_444TC8).group(1)
total_read_miss_rate_444TC8 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_444TC8).group(1)
total_write_misses_444TC8 = re.search(
    r"Total_write_misses (\d+)", content_444TC8).group(1)
total_write_miss_rate_444TC8 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_444TC8).group(1)
print(">>>>>All TC8 444.namd-120B variables where obtained successfully")

# 445.gobmk-17B
total_misses_445TC8 = re.search(r"Total_misses (\d+)", content_445TC8).group(1)
total_miss_rate_445TC8 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_445TC8).group(1)
total_read_misses_445TC8 = re.search(
    r"Total_read_misses (\d+)", content_445TC8).group(1)
total_read_miss_rate_445TC8 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_445TC8).group(1)
total_write_misses_445TC8 = re.search(
    r"Total_write_misses (\d+)", content_445TC8).group(1)
total_write_miss_rate_445TC8 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_445TC8).group(1)
print(">>>>>All TC8 445.gobmk-17B variables where obtained successfully")

# 450.soplex-247B
total_misses_450TC8 = re.search(r"Total_misses (\d+)", content_450TC8).group(1)
total_miss_rate_450TC8 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_450TC8).group(1)
total_read_misses_450TC8 = re.search(
    r"Total_read_misses (\d+)", content_450TC8).group(1)
total_read_miss_rate_450TC8 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_450TC8).group(1)
total_write_misses_450TC8 = re.search(
    r"Total_write_misses (\d+)", content_450TC8).group(1)
total_write_miss_rate_450TC8 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_450TC8).group(1)
print(">>>>>All TC8 450.soplex-247B variables where obtained successfully")

# 453.povray-887B
total_misses_453TC8 = re.search(r"Total_misses (\d+)", content_453TC8).group(1)
total_miss_rate_453TC8 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_453TC8).group(1)
total_read_misses_453TC8 = re.search(
    r"Total_read_misses (\d+)", content_453TC8).group(1)
total_read_miss_rate_453TC8 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_453TC8).group(1)
total_write_misses_453TC8 = re.search(
    r"Total_write_misses (\d+)", content_453TC8).group(1)
total_write_miss_rate_453TC8 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_453TC8).group(1)
print(">>>>>All TC8 453.povray-887B variables where obtained successfully")

# 454.calculix-104B
total_misses_454TC8 = re.search(r"Total_misses (\d+)", content_454TC8).group(1)
total_miss_rate_454TC8 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_454TC8).group(1)
total_read_misses_454TC8 = re.search(
    r"Total_read_misses (\d+)", content_454TC8).group(1)
total_read_miss_rate_454TC8 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_454TC8).group(1)
total_write_misses_454TC8 = re.search(
    r"Total_write_misses (\d+)", content_454TC8).group(1)
total_write_miss_rate_454TC8 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_454TC8).group(1)
print(">>>>>All TC8 454.calculix-104B variables where obtained successfully")

# 456.hmmer-191B
total_misses_456TC8 = re.search(r"Total_misses (\d+)", content_456TC8).group(1)
total_miss_rate_456TC8 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_456TC8).group(1)
total_read_misses_456TC8 = re.search(
    r"Total_read_misses (\d+)", content_456TC8).group(1)
total_read_miss_rate_456TC8 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_456TC8).group(1)
total_write_misses_456TC8 = re.search(
    r"Total_write_misses (\d+)", content_456TC8).group(1)
total_write_miss_rate_456TC8 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_456TC8).group(1)
print(">>>>>All TC8 456.hmmer-191B variables where obtained successfully")

# 458.sjeng-1088B
total_misses_458TC8 = re.search(r"Total_misses (\d+)", content_458TC8).group(1)
total_miss_rate_458TC8 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_458TC8).group(1)
total_read_misses_458TC8 = re.search(
    r"Total_read_misses (\d+)", content_458TC8).group(1)
total_read_miss_rate_458TC8 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_458TC8).group(1)
total_write_misses_458TC8 = re.search(
    r"Total_write_misses (\d+)", content_458TC8).group(1)
total_write_miss_rate_458TC8 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_458TC8).group(1)
print(">>>>>All TC8 458.sjeng-1088B variables where obtained successfully")

# 459.GemsFDTD-1169B
total_misses_459TC8 = re.search(r"Total_misses (\d+)", content_459TC8).group(1)
total_miss_rate_459TC8 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_459TC8).group(1)
total_read_misses_459TC8 = re.search(
    r"Total_read_misses (\d+)", content_459TC8).group(1)
total_read_miss_rate_459TC8 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_459TC8).group(1)
total_write_misses_459TC8 = re.search(
    r"Total_write_misses (\d+)", content_459TC8).group(1)
total_write_miss_rate_459TC8 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_459TC8).group(1)
print(">>>>>All TC8 459.GemsFDTD-1169B variables where obtained successfully")

# 462.libquantum-1343B
total_misses_462TC8 = re.search(r"Total_misses (\d+)", content_462TC8).group(1)
total_miss_rate_462TC8 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_462TC8).group(1)
total_read_misses_462TC8 = re.search(
    r"Total_read_misses (\d+)", content_462TC8).group(1)
total_read_miss_rate_462TC8 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_462TC8).group(1)
total_write_misses_462TC8 = re.search(
    r"Total_write_misses (\d+)", content_462TC8).group(1)
total_write_miss_rate_462TC8 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_462TC8).group(1)
print(">>>>>All TC8 462.libquantum-1343B variables where obtained successfully")

# 464.h264ref-30B
total_misses_464TC8 = re.search(r"Total_misses (\d+)", content_464TC8).group(1)
total_miss_rate_464TC8 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_464TC8).group(1)
total_read_misses_464TC8 = re.search(
    r"Total_read_misses (\d+)", content_464TC8).group(1)
total_read_miss_rate_464TC8 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_464TC8).group(1)
total_write_misses_464TC8 = re.search(
    r"Total_write_misses (\d+)", content_464TC8).group(1)
total_write_miss_rate_464TC8 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_464TC8).group(1)
print(">>>>>All TC8 464.h264ref-30B variables where obtained successfully")

# 465.tonto-1769B
total_misses_465TC8 = re.search(r"Total_misses (\d+)", content_465TC8).group(1)
total_miss_rate_465TC8 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_465TC8).group(1)
total_read_misses_465TC8 = re.search(
    r"Total_read_misses (\d+)", content_465TC8).group(1)
total_read_miss_rate_465TC8 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_465TC8).group(1)
total_write_misses_465TC8 = re.search(
    r"Total_write_misses (\d+)", content_465TC8).group(1)
total_write_miss_rate_465TC8 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_465TC8).group(1)
print(">>>>>All TC8 465.tonto-1769B variables where obtained successfully")

# 470.lbm-1274B
total_misses_470TC8 = re.search(r"Total_misses (\d+)", content_470TC8).group(1)
total_miss_rate_470TC8 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_470TC8).group(1)
total_read_misses_470TC8 = re.search(
    r"Total_read_misses (\d+)", content_470TC8).group(1)
total_read_miss_rate_470TC8 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_470TC8).group(1)
total_write_misses_470TC8 = re.search(
    r"Total_write_misses (\d+)", content_470TC8).group(1)
total_write_miss_rate_470TC8 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_470TC8).group(1)
print(">>>>>All TC8 470.lbm-1274B variables where obtained successfully")

# 471.omnetpp-188B
total_misses_471TC8 = re.search(r"Total_misses (\d+)", content_471TC8).group(1)
total_miss_rate_471TC8 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_471TC8).group(1)
total_read_misses_471TC8 = re.search(
    r"Total_read_misses (\d+)", content_471TC8).group(1)
total_read_miss_rate_471TC8 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_471TC8).group(1)
total_write_misses_471TC8 = re.search(
    r"Total_write_misses (\d+)", content_471TC8).group(1)
total_write_miss_rate_471TC8 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_471TC8).group(1)
print(">>>>>All TC8 471.omnetpp-188B variables where obtained successfully")

# 473.astar-153B
total_misses_473TC8 = re.search(r"Total_misses (\d+)", content_473TC8).group(1)
total_miss_rate_473TC8 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_473TC8).group(1)
total_read_misses_473TC8 = re.search(
    r"Total_read_misses (\d+)", content_473TC8).group(1)
total_read_miss_rate_473TC8 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_473TC8).group(1)
total_write_misses_473TC8 = re.search(
    r"Total_write_misses (\d+)", content_473TC8).group(1)
total_write_miss_rate_473TC8 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_473TC8).group(1)
print(">>>>>All TC8 473.astar-153B variables where obtained successfully")

# 481.wrf-1170B
total_misses_481TC8 = re.search(r"Total_misses (\d+)", content_481TC8).group(1)
total_miss_rate_481TC8 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_481TC8).group(1)
total_read_misses_481TC8 = re.search(
    r"Total_read_misses (\d+)", content_481TC8).group(1)
total_read_miss_rate_481TC8 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_481TC8).group(1)
total_write_misses_481TC8 = re.search(
    r"Total_write_misses (\d+)", content_481TC8).group(1)
total_write_miss_rate_481TC8 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_481TC8).group(1)
print(">>>>>All TC8 481.wrf-1170B variables where obtained successfully")

# 482.sphinx3-1100B
total_misses_482TC8 = re.search(r"Total_misses (\d+)", content_482TC8).group(1)
total_miss_rate_482TC8 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_482TC8).group(1)
total_read_misses_482TC8 = re.search(
    r"Total_read_misses (\d+)", content_482TC8).group(1)
total_read_miss_rate_482TC8 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_482TC8).group(1)
total_write_misses_482TC8 = re.search(
    r"Total_write_misses (\d+)", content_482TC8).group(1)
total_write_miss_rate_482TC8 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_482TC8).group(1)
print(">>>>>All TC8 482.sphinx3-1100B variables where obtained successfully")

# 483.xalancbmk-127B
total_misses_483TC8 = re.search(r"Total_misses (\d+)", content_483TC8).group(1)
total_miss_rate_483TC8 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_483TC8).group(1)
total_read_misses_483TC8 = re.search(
    r"Total_read_misses (\d+)", content_483TC8).group(1)
total_read_miss_rate_483TC8 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_483TC8).group(1)
total_write_misses_483TC8 = re.search(
    r"Total_write_misses (\d+)", content_483TC8).group(1)
total_write_miss_rate_483TC8 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_483TC8).group(1)
print(">>>>>All TC8 483.xalancbmk-127B variables where obtained successfully")


#############################
# Adjunta datos a dataframe #
#############################

# **400.perlbench-41B**

tabla_TC8.at['400.perlbench-41B', 'Total Misses'] = total_misses_400TC8

tabla_TC8.at['400.perlbench-41B',
             'Miss rate total [%]'] = total_miss_rate_400TC8

tabla_TC8.at['400.perlbench-41B', 'Misses lectura'] = total_read_misses_400TC8

tabla_TC8.at['400.perlbench-41B',
             'Miss rate lectura [%]'] = total_read_miss_rate_400TC8

tabla_TC8.at['400.perlbench-41B',
             'Misses escritura'] = total_write_misses_400TC8

tabla_TC8.at['400.perlbench-41B',
             'Miss rate escritura [%]'] = total_write_miss_rate_400TC8

# **401.bzip2-226B**

tabla_TC8.at['401.bzip2-226B', 'Total Misses'] = total_misses_401TC8

tabla_TC8.at['401.bzip2-226B', 'Miss rate total [%]'] = total_miss_rate_401TC8

tabla_TC8.at['401.bzip2-226B', 'Misses lectura'] = total_read_misses_401TC8

tabla_TC8.at['401.bzip2-226B',
             'Miss rate lectura [%]'] = total_read_miss_rate_401TC8

tabla_TC8.at['401.bzip2-226B',
             'Misses escritura'] = total_write_misses_401TC8

tabla_TC8.at['401.bzip2-226B',
             'Miss rate escritura [%]'] = total_write_miss_rate_401TC8

# **403.gcc-16B**

tabla_TC8.at['403.gcc-16B', 'Total Misses'] = total_misses_403TC8

tabla_TC8.at['403.gcc-16B', 'Miss rate total [%]'] = total_miss_rate_403TC8

tabla_TC8.at['403.gcc-16B', 'Misses lectura'] = total_read_misses_403TC8

tabla_TC8.at['403.gcc-16B',
             'Miss rate lectura [%]'] = total_read_miss_rate_403TC8

tabla_TC8.at['403.gcc-16B',
             'Misses escritura'] = total_write_misses_403TC8

tabla_TC8.at['403.gcc-16B',
             'Miss rate escritura [%]'] = total_write_miss_rate_403TC8

# **410.bwaves-1963B**

tabla_TC8.at['410.bwaves-1963B', 'Total Misses'] = total_misses_410TC8

tabla_TC8.at['410.bwaves-1963B',
             'Miss rate total [%]'] = total_miss_rate_410TC8

tabla_TC8.at['410.bwaves-1963B', 'Misses lectura'] = total_read_misses_410TC8

tabla_TC8.at['410.bwaves-1963B',
             'Miss rate lectura [%]'] = total_read_miss_rate_410TC8

tabla_TC8.at['410.bwaves-1963B',
             'Misses escritura'] = total_write_misses_410TC8

tabla_TC8.at['410.bwaves-1963B',
             'Miss rate escritura [%]'] = total_write_miss_rate_410TC8

# **416.gamess-875B**

tabla_TC8.at['416.gamess-875B', 'Total Misses'] = total_misses_416TC8

tabla_TC8.at['416.gamess-875B', 'Miss rate total [%]'] = total_miss_rate_416TC8

tabla_TC8.at['416.gamess-875B', 'Misses lectura'] = total_read_misses_416TC8

tabla_TC8.at['416.gamess-875B',
             'Miss rate lectura [%]'] = total_read_miss_rate_416TC8

tabla_TC8.at['416.gamess-875B',
             'Misses escritura'] = total_write_misses_416TC8

tabla_TC8.at['416.gamess-875B',
             'Miss rate escritura [%]'] = total_write_miss_rate_416TC8

# **429.mcf-184B**

tabla_TC8.at['429.mcf-184B', 'Total Misses'] = total_misses_429TC8

tabla_TC8.at['429.mcf-184B', 'Miss rate total [%]'] = total_miss_rate_429TC8

tabla_TC8.at['429.mcf-184B', 'Misses lectura'] = total_read_misses_429TC8

tabla_TC8.at['429.mcf-184B',
             'Miss rate lectura [%]'] = total_read_miss_rate_429TC8

tabla_TC8.at['429.mcf-184B',
             'Misses escritura'] = total_write_misses_429TC8

tabla_TC8.at['429.mcf-184B',
             'Miss rate escritura [%]'] = total_write_miss_rate_429TC8

# **433.milc-127B**

tabla_TC8.at['433.milc-127B', 'Total Misses'] = total_misses_433TC8

tabla_TC8.at['433.milc-127B', 'Miss rate total [%]'] = total_miss_rate_433TC8

tabla_TC8.at['433.milc-127B', 'Misses lectura'] = total_read_misses_433TC8

tabla_TC8.at['433.milc-127B',
             'Miss rate lectura [%]'] = total_read_miss_rate_433TC8

tabla_TC8.at['433.milc-127B',
             'Misses escritura'] = total_write_misses_433TC8

tabla_TC8.at['433.milc-127B',
             'Miss rate escritura [%]'] = total_write_miss_rate_433TC8

# **435.gromacs-111B**

tabla_TC8.at['435.gromacs-111B', 'Total Misses'] = total_misses_435TC8

tabla_TC8.at['435.gromacs-111B',
             'Miss rate total [%]'] = total_miss_rate_435TC8

tabla_TC8.at['435.gromacs-111B', 'Misses lectura'] = total_read_misses_435TC8

tabla_TC8.at['435.gromacs-111B',
             'Miss rate lectura [%]'] = total_read_miss_rate_435TC8

tabla_TC8.at['435.gromacs-111B',
             'Misses escritura'] = total_write_misses_435TC8

tabla_TC8.at['435.gromacs-111B',
             'Miss rate escritura [%]'] = total_write_miss_rate_435TC8

# **436.cactusADM-1804B**

tabla_TC8.at['436.cactusADM-1804B', 'Total Misses'] = total_misses_436TC8

tabla_TC8.at['436.cactusADM-1804B',
             'Miss rate total [%]'] = total_miss_rate_436TC8

tabla_TC8.at['436.cactusADM-1804B',
             'Misses lectura'] = total_read_misses_436TC8

tabla_TC8.at['436.cactusADM-1804B',
             'Miss rate lectura [%]'] = total_read_miss_rate_436TC8

tabla_TC8.at['436.cactusADM-1804B',
             'Misses escritura'] = total_write_misses_436TC8

tabla_TC8.at['436.cactusADM-1804B',
             'Miss rate escritura [%]'] = total_write_miss_rate_436TC8

# **437.leslie3d-134B**

tabla_TC8.at['437.leslie3d-134B', 'Total Misses'] = total_misses_437TC8

tabla_TC8.at['437.leslie3d-134B',
             'Miss rate total [%]'] = total_miss_rate_437TC8

tabla_TC8.at['437.leslie3d-134B', 'Misses lectura'] = total_read_misses_437TC8

tabla_TC8.at['437.leslie3d-134B',
             'Miss rate lectura [%]'] = total_read_miss_rate_437TC8

tabla_TC8.at['437.leslie3d-134B',
             'Misses escritura'] = total_write_misses_437TC8

tabla_TC8.at['437.leslie3d-134B',
             'Miss rate escritura [%]'] = total_write_miss_rate_437TC8

# **444.namd-120B**

tabla_TC8.at['444.namd-120B', 'Total Misses'] = total_misses_444TC8

tabla_TC8.at['444.namd-120B', 'Miss rate total [%]'] = total_miss_rate_444TC8

tabla_TC8.at['444.namd-120B', 'Misses lectura'] = total_read_misses_444TC8

tabla_TC8.at['444.namd-120B',
             'Miss rate lectura [%]'] = total_read_miss_rate_444TC8

tabla_TC8.at['444.namd-120B',
             'Misses escritura'] = total_write_misses_444TC8

tabla_TC8.at['444.namd-120B',
             'Miss rate escritura [%]'] = total_write_miss_rate_444TC8

# **445.gobmk-17B**

tabla_TC8.at['445.gobmk-17B', 'Total Misses'] = total_misses_445TC8

tabla_TC8.at['445.gobmk-17B', 'Miss rate total [%]'] = total_miss_rate_445TC8

tabla_TC8.at['445.gobmk-17B', 'Misses lectura'] = total_read_misses_445TC8

tabla_TC8.at['445.gobmk-17B',
             'Miss rate lectura [%]'] = total_read_miss_rate_445TC8

tabla_TC8.at['445.gobmk-17B',
             'Misses escritura'] = total_write_misses_445TC8

tabla_TC8.at['445.gobmk-17B',
             'Miss rate escritura [%]'] = total_write_miss_rate_445TC8

# **450.soplex-247B**

tabla_TC8.at['450.soplex-247B', 'Total Misses'] = total_misses_450TC8

tabla_TC8.at['450.soplex-247B', 'Miss rate total [%]'] = total_miss_rate_450TC8

tabla_TC8.at['450.soplex-247B', 'Misses lectura'] = total_read_misses_450TC8

tabla_TC8.at['450.soplex-247B',
             'Miss rate lectura [%]'] = total_read_miss_rate_450TC8

tabla_TC8.at['450.soplex-247B',
             'Misses escritura'] = total_write_misses_450TC8

tabla_TC8.at['450.soplex-247B',
             'Miss rate escritura [%]'] = total_write_miss_rate_450TC8

# **453.povray-887B**

tabla_TC8.at['453.povray-887B', 'Total Misses'] = total_misses_453TC8

tabla_TC8.at['453.povray-887B', 'Miss rate total [%]'] = total_miss_rate_453TC8

tabla_TC8.at['453.povray-887B', 'Misses lectura'] = total_read_misses_453TC8

tabla_TC8.at['453.povray-887B',
             'Miss rate lectura [%]'] = total_read_miss_rate_453TC8

tabla_TC8.at['453.povray-887B',
             'Misses escritura'] = total_write_misses_453TC8

tabla_TC8.at['453.povray-887B',
             'Miss rate escritura [%]'] = total_write_miss_rate_453TC8

# **454.calculix-104B**

tabla_TC8.at['454.calculix-104B', 'Total Misses'] = total_misses_454TC8

tabla_TC8.at['454.calculix-104B',
             'Miss rate total [%]'] = total_miss_rate_454TC8

tabla_TC8.at['454.calculix-104B', 'Misses lectura'] = total_read_misses_454TC8

tabla_TC8.at['454.calculix-104B',
             'Miss rate lectura [%]'] = total_read_miss_rate_454TC8

tabla_TC8.at['454.calculix-104B',
             'Misses escritura'] = total_write_misses_454TC8

tabla_TC8.at['454.calculix-104B',
             'Miss rate escritura [%]'] = total_write_miss_rate_454TC8

# **456.hmmer-191B**

tabla_TC8.at['456.hmmer-191B', 'Total Misses'] = total_misses_456TC8

tabla_TC8.at['456.hmmer-191B', 'Miss rate total [%]'] = total_miss_rate_456TC8

tabla_TC8.at['456.hmmer-191B', 'Misses lectura'] = total_read_misses_456TC8

tabla_TC8.at['456.hmmer-191B',
             'Miss rate lectura [%]'] = total_read_miss_rate_456TC8

tabla_TC8.at['456.hmmer-191B',
             'Misses escritura'] = total_write_misses_456TC8

tabla_TC8.at['456.hmmer-191B',
             'Miss rate escritura [%]'] = total_write_miss_rate_456TC8

# **458.sjeng-1088B**

tabla_TC8.at['458.sjeng-1088B', 'Total Misses'] = total_misses_458TC8

tabla_TC8.at['458.sjeng-1088B', 'Miss rate total [%]'] = total_miss_rate_458TC8

tabla_TC8.at['458.sjeng-1088B', 'Misses lectura'] = total_read_misses_458TC8

tabla_TC8.at['458.sjeng-1088B',
             'Miss rate lectura [%]'] = total_read_miss_rate_458TC8

tabla_TC8.at['458.sjeng-1088B',
             'Misses escritura'] = total_write_misses_458TC8

tabla_TC8.at['458.sjeng-1088B',
             'Miss rate escritura [%]'] = total_write_miss_rate_458TC8

# **459.GemsFDTD-1169B**

tabla_TC8.at['459.GemsFDTD-1169B', 'Total Misses'] = total_misses_459TC8

tabla_TC8.at['459.GemsFDTD-1169B',
             'Miss rate total [%]'] = total_miss_rate_459TC8

tabla_TC8.at['459.GemsFDTD-1169B', 'Misses lectura'] = total_read_misses_459TC8

tabla_TC8.at['459.GemsFDTD-1169B',
             'Miss rate lectura [%]'] = total_read_miss_rate_459TC8

tabla_TC8.at['459.GemsFDTD-1169B',
             'Misses escritura'] = total_write_misses_459TC8

tabla_TC8.at['459.GemsFDTD-1169B',
             'Miss rate escritura [%]'] = total_write_miss_rate_459TC8

# **462.libquantum-1343B**

tabla_TC8.at['462.libquantum-1343B', 'Total Misses'] = total_misses_462TC8

tabla_TC8.at['462.libquantum-1343B',
             'Miss rate total [%]'] = total_miss_rate_462TC8

tabla_TC8.at['462.libquantum-1343B',
             'Misses lectura'] = total_read_misses_462TC8

tabla_TC8.at['462.libquantum-1343B',
             'Miss rate lectura [%]'] = total_read_miss_rate_462TC8

tabla_TC8.at['462.libquantum-1343B',
             'Misses escritura'] = total_write_misses_462TC8

tabla_TC8.at['462.libquantum-1343B',
             'Miss rate escritura [%]'] = total_write_miss_rate_462TC8

# **464.h264ref-30B**

tabla_TC8.at['464.h264ref-30B', 'Total Misses'] = total_misses_464TC8

tabla_TC8.at['464.h264ref-30B', 'Miss rate total [%]'] = total_miss_rate_464TC8

tabla_TC8.at['464.h264ref-30B', 'Misses lectura'] = total_read_misses_464TC8

tabla_TC8.at['464.h264ref-30B',
             'Miss rate lectura [%]'] = total_read_miss_rate_464TC8

tabla_TC8.at['464.h264ref-30B',
             'Misses escritura'] = total_write_misses_464TC8

tabla_TC8.at['464.h264ref-30B',
             'Miss rate escritura [%]'] = total_write_miss_rate_464TC8

# **465.tonto-1769B**

tabla_TC8.at['465.tonto-1769B', 'Total Misses'] = total_misses_465TC8

tabla_TC8.at['465.tonto-1769B', 'Miss rate total [%]'] = total_miss_rate_465TC8

tabla_TC8.at['465.tonto-1769B', 'Misses lectura'] = total_read_misses_465TC8

tabla_TC8.at['465.tonto-1769B',
             'Miss rate lectura [%]'] = total_read_miss_rate_465TC8

tabla_TC8.at['465.tonto-1769B',
             'Misses escritura'] = total_write_misses_465TC8

tabla_TC8.at['465.tonto-1769B',
             'Miss rate escritura [%]'] = total_write_miss_rate_465TC8

# **470.lbm-1274B**

tabla_TC8.at['470.lbm-1274B', 'Total Misses'] = total_misses_470TC8

tabla_TC8.at['470.lbm-1274B', 'Miss rate total [%]'] = total_miss_rate_470TC8

tabla_TC8.at['470.lbm-1274B', 'Misses lectura'] = total_read_misses_470TC8

tabla_TC8.at['470.lbm-1274B',
             'Miss rate lectura [%]'] = total_read_miss_rate_470TC8

tabla_TC8.at['470.lbm-1274B',
             'Misses escritura'] = total_write_misses_470TC8

tabla_TC8.at['470.lbm-1274B',
             'Miss rate escritura [%]'] = total_write_miss_rate_470TC8

# **471.omnetpp-188B**

tabla_TC8.at['471.omnetpp-188B', 'Total Misses'] = total_misses_471TC8

tabla_TC8.at['471.omnetpp-188B',
             'Miss rate total [%]'] = total_miss_rate_471TC8

tabla_TC8.at['471.omnetpp-188B', 'Misses lectura'] = total_read_misses_471TC8

tabla_TC8.at['471.omnetpp-188B',
             'Miss rate lectura [%]'] = total_read_miss_rate_471TC8

tabla_TC8.at['471.omnetpp-188B',
             'Misses escritura'] = total_write_misses_471TC8

tabla_TC8.at['471.omnetpp-188B',
             'Miss rate escritura [%]'] = total_write_miss_rate_471TC8

# **473.astar-153B**

tabla_TC8.at['473.astar-153B', 'Total Misses'] = total_misses_473TC8

tabla_TC8.at['473.astar-153B', 'Miss rate total [%]'] = total_miss_rate_473TC8

tabla_TC8.at['473.astar-153B', 'Misses lectura'] = total_read_misses_473TC8

tabla_TC8.at['473.astar-153B',
             'Miss rate lectura [%]'] = total_read_miss_rate_473TC8

tabla_TC8.at['473.astar-153B',
             'Misses escritura'] = total_write_misses_473TC8

tabla_TC8.at['473.astar-153B',
             'Miss rate escritura [%]'] = total_write_miss_rate_473TC8

# **481.wrf-1170B**

tabla_TC8.at['481.wrf-1170B', 'Total Misses'] = total_misses_481TC8

tabla_TC8.at['481.wrf-1170B', 'Miss rate total [%]'] = total_miss_rate_481TC8

tabla_TC8.at['481.wrf-1170B', 'Misses lectura'] = total_read_misses_481TC8

tabla_TC8.at['481.wrf-1170B',
             'Miss rate lectura [%]'] = total_read_miss_rate_481TC8

tabla_TC8.at['481.wrf-1170B',
             'Misses escritura'] = total_write_misses_481TC8

tabla_TC8.at['481.wrf-1170B',
             'Miss rate escritura [%]'] = total_write_miss_rate_481TC8

# **482.sphinx3-1100B**

tabla_TC8.at['482.sphinx3-1100B', 'Total Misses'] = total_misses_482TC8

tabla_TC8.at['482.sphinx3-1100B',
             'Miss rate total [%]'] = total_miss_rate_482TC8

tabla_TC8.at['482.sphinx3-1100B', 'Misses lectura'] = total_read_misses_482TC8

tabla_TC8.at['482.sphinx3-1100B',
             'Miss rate lectura [%]'] = total_read_miss_rate_482TC8

tabla_TC8.at['482.sphinx3-1100B',
             'Misses escritura'] = total_write_misses_482TC8

tabla_TC8.at['482.sphinx3-1100B',
             'Miss rate escritura [%]'] = total_write_miss_rate_482TC8

# **483.xalancbmk-127B**

tabla_TC8.at['483.xalancbmk-127B', 'Total Misses'] = total_misses_483TC8

tabla_TC8.at['483.xalancbmk-127B',
             'Miss rate total [%]'] = total_miss_rate_483TC8

tabla_TC8.at['483.xalancbmk-127B', 'Misses lectura'] = total_read_misses_483TC8

tabla_TC8.at['483.xalancbmk-127B',
             'Miss rate lectura [%]'] = total_read_miss_rate_483TC8

tabla_TC8.at['483.xalancbmk-127B',
             'Misses escritura'] = total_write_misses_483TC8

tabla_TC8.at['483.xalancbmk-127B',
             'Miss rate escritura [%]'] = total_write_miss_rate_483TC8

print(">>>>>All TC8 data has been uploaded successfully")

##########################################
# Extractor para experimento con tamaño 16#
##########################################


# Creación de tablas para adjuntar valores
# Una tabla por tamaño
tabla_TC16 = pd.DataFrame(index=[
    '400.perlbench-41B', '401.bzip2-226B', '403.gcc-16B', '410.bwaves-1963B', '416.gamess-875B', '429.mcf-184B', '433.milc-127B',
    '435.gromacs-111B', '436.cactusADM-1804B', '437.leslie3d-134B', '444.namd-120B', '445.gobmk-17B',
    '450.soplex-247B', '453.povray-887B', '454.calculix-104B', '456.hmmer-191B', '458.sjeng-1088B', '459.GemsFDTD-1169B',
    '462.libquantum-1343B', '464.h264ref-30B', '465.tonto-1769B', '470.lbm-1274B', '471.omnetpp-188B', '473.astar-153B', '481.wrf-1170B',
    '482.sphinx3-1100B', '483.xalancbmk-127B'], columns=[
    'App', 'Total Misses', 'Miss rate total [%]', 'Misses lectura', 'Miss rate lectura [%]', 'Misses escritura', 'Miss rate escritura [%]'])
tabla_TC16['App'] = tabla_TC16.index

# Files paths
filename_28 = "RESULTS_TC/400TC16.txt"
filename_29 = "RESULTS_TC/401TC16.txt"
filename_30 = "RESULTS_TC/403TC16.txt"
filename_31 = "RESULTS_TC/410TC16.txt"
filename_32 = "RESULTS_TC/416TC16.txt"
filename_33 = "RESULTS_TC/429TC16.txt"
filename_34 = "RESULTS_TC/433TC16.txt"
filename_35 = "RESULTS_TC/435TC16.txt"
filename_36 = "RESULTS_TC/436TC16.txt"
filename_37 = "RESULTS_TC/437TC16.txt"
filename_38 = "RESULTS_TC/444TC16.txt"
filename_39 = "RESULTS_TC/445TC16.txt"
filename_40 = "RESULTS_TC/450TC16.txt"
filename_41 = "RESULTS_TC/453TC16.txt"
filename_42 = "RESULTS_TC/454TC16.txt"
filename_43 = "RESULTS_TC/456TC16.txt"
filename_44 = "RESULTS_TC/458TC16.txt"
filename_45 = "RESULTS_TC/459TC16.txt"
filename_46 = "RESULTS_TC/462TC16.txt"
filename_47 = "RESULTS_TC/464TC16.txt"
filename_48 = "RESULTS_TC/465TC16.txt"
filename_49 = "RESULTS_TC/470TC16.txt"
filename_50 = "RESULTS_TC/471TC16.txt"
filename_51 = "RESULTS_TC/473TC16.txt"
filename_52 = "RESULTS_TC/481TC16.txt"
filename_53 = "RESULTS_TC/482TC16.txt"
filename_54 = "RESULTS_TC/483TC16.txt"


# Content file extracter
with open(filename_28, 'r') as file:
    content_400TC16 = file.read()
with open(filename_29, 'r') as file:
    content_401TC16 = file.read()
with open(filename_30, 'r') as file:
    content_403TC16 = file.read()
with open(filename_31, 'r') as file:
    content_410TC16 = file.read()
with open(filename_32, 'r') as file:
    content_416TC16 = file.read()
with open(filename_33, 'r') as file:
    content_429TC16 = file.read()
with open(filename_34, 'r') as file:
    content_433TC16 = file.read()
with open(filename_35, 'r') as file:
    content_435TC16 = file.read()
with open(filename_36, 'r') as file:
    content_436TC16 = file.read()
with open(filename_37, 'r') as file:
    content_437TC16 = file.read()
with open(filename_38, 'r') as file:
    content_444TC16 = file.read()
with open(filename_39, 'r') as file:
    content_445TC16 = file.read()
with open(filename_40, 'r') as file:
    content_450TC16 = file.read()
with open(filename_41, 'r') as file:
    content_453TC16 = file.read()
with open(filename_42, 'r') as file:
    content_454TC16 = file.read()
with open(filename_43, 'r') as file:
    content_456TC16 = file.read()
with open(filename_44, 'r') as file:
    content_458TC16 = file.read()
with open(filename_45, 'r') as file:
    content_459TC16 = file.read()
with open(filename_46, 'r') as file:
    content_462TC16 = file.read()
with open(filename_47, 'r') as file:
    content_464TC16 = file.read()
with open(filename_48, 'r') as file:
    content_465TC16 = file.read()
with open(filename_49, 'r') as file:
    content_470TC16 = file.read()
with open(filename_50, 'r') as file:
    content_471TC16 = file.read()
with open(filename_51, 'r') as file:
    content_473TC16 = file.read()
with open(filename_52, 'r') as file:
    content_481TC16 = file.read()
with open(filename_53, 'r') as file:
    content_482TC16 = file.read()
with open(filename_54, 'r') as file:
    content_483TC16 = file.read()


# Variables según aplicación

# 400.pearlbench-41B
total_misses_400TC16 = re.search(
    r"Total_misses (\d+)", content_400TC16).group(1)
total_miss_rate_400TC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_400TC16).group(1)
total_read_misses_400TC16 = re.search(
    r"Total_read_misses (\d+)", content_400TC16).group(1)
total_read_miss_rate_400TC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_400TC16).group(1)
total_write_misses_400TC16 = re.search(
    r"Total_write_misses (\d+)", content_400TC16).group(1)
total_write_miss_rate_400TC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_400TC16).group(1)
print(">>>>>All TC16 400.pearlbench-41B variables where obtained successfully")

# 401.bzip2-226B
total_misses_401TC16 = re.search(
    r"Total_misses (\d+)", content_401TC16).group(1)
total_miss_rate_401TC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_401TC16).group(1)
total_read_misses_401TC16 = re.search(
    r"Total_read_misses (\d+)", content_401TC16).group(1)
total_read_miss_rate_401TC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_401TC16).group(1)
total_write_misses_401TC16 = re.search(
    r"Total_write_misses (\d+)", content_401TC16).group(1)
total_write_miss_rate_401TC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_401TC16).group(1)
print(">>>>>All TC16 401.bzip2-226B variables where obtained successfully")

# 403.gcc-16B
total_misses_403TC16 = re.search(
    r"Total_misses (\d+)", content_403TC16).group(1)
total_miss_rate_403TC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_403TC16).group(1)
total_read_misses_403TC16 = re.search(
    r"Total_read_misses (\d+)", content_403TC16).group(1)
total_read_miss_rate_403TC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_403TC16).group(1)
total_write_misses_403TC16 = re.search(
    r"Total_write_misses (\d+)", content_403TC16).group(1)
total_write_miss_rate_403TC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_403TC16).group(1)
print(">>>>>All TC16 403.gcc-16B variables where obtained successfully")

# 410.bwaves-1963B
total_misses_410TC16 = re.search(
    r"Total_misses (\d+)", content_410TC16).group(1)
total_miss_rate_410TC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_410TC16).group(1)
total_read_misses_410TC16 = re.search(
    r"Total_read_misses (\d+)", content_410TC16).group(1)
total_read_miss_rate_410TC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_410TC16).group(1)
total_write_misses_410TC16 = re.search(
    r"Total_write_misses (\d+)", content_410TC16).group(1)
total_write_miss_rate_410TC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_410TC16).group(1)
print(">>>>>All TC16 410.bwaves-1963B variables where obtained successfully")

# 416.gamess-875B
total_misses_416TC16 = re.search(
    r"Total_misses (\d+)", content_416TC16).group(1)
total_miss_rate_416TC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_416TC16).group(1)
total_read_misses_416TC16 = re.search(
    r"Total_read_misses (\d+)", content_416TC16).group(1)
total_read_miss_rate_416TC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_416TC16).group(1)
total_write_misses_416TC16 = re.search(
    r"Total_write_misses (\d+)", content_416TC16).group(1)
total_write_miss_rate_416TC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_416TC16).group(1)
print(">>>>>All TC16 416.gamess-875B variables where obtained successfully")

# 429.mcf-184B
total_misses_429TC16 = re.search(
    r"Total_misses (\d+)", content_429TC16).group(1)
total_miss_rate_429TC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_429TC16).group(1)
total_read_misses_429TC16 = re.search(
    r"Total_read_misses (\d+)", content_429TC16).group(1)
total_read_miss_rate_429TC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_429TC16).group(1)
total_write_misses_429TC16 = re.search(
    r"Total_write_misses (\d+)", content_429TC16).group(1)
total_write_miss_rate_429TC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_429TC16).group(1)
print(">>>>>All TC16 429.mcf-184B variables where obtained successfully")

# 433.milc-127B
total_misses_433TC16 = re.search(
    r"Total_misses (\d+)", content_433TC16).group(1)
total_miss_rate_433TC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_433TC16).group(1)
total_read_misses_433TC16 = re.search(
    r"Total_read_misses (\d+)", content_433TC16).group(1)
total_read_miss_rate_433TC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_433TC16).group(1)
total_write_misses_433TC16 = re.search(
    r"Total_write_misses (\d+)", content_433TC16).group(1)
total_write_miss_rate_433TC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_433TC16).group(1)
print(">>>>>All TC16 433.milc-127B variables where obtained successfully")

# 435.gromacs-111B
total_misses_435TC16 = re.search(
    r"Total_misses (\d+)", content_435TC16).group(1)
total_miss_rate_435TC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_435TC16).group(1)
total_read_misses_435TC16 = re.search(
    r"Total_read_misses (\d+)", content_435TC16).group(1)
total_read_miss_rate_435TC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_435TC16).group(1)
total_write_misses_435TC16 = re.search(
    r"Total_write_misses (\d+)", content_435TC16).group(1)
total_write_miss_rate_435TC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_435TC16).group(1)
print(">>>>>All TC16 435.gromacs-111B variables where obtained successfully")

# 436.cactusADM-1804B
total_misses_436TC16 = re.search(
    r"Total_misses (\d+)", content_436TC16).group(1)
total_miss_rate_436TC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_436TC16).group(1)
total_read_misses_436TC16 = re.search(
    r"Total_read_misses (\d+)", content_436TC16).group(1)
total_read_miss_rate_436TC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_436TC16).group(1)
total_write_misses_436TC16 = re.search(
    r"Total_write_misses (\d+)", content_436TC16).group(1)
total_write_miss_rate_436TC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_436TC16).group(1)
print(">>>>>All TC16 436.cactusADM-1804B variables where obtained successfully")

# 437.leslie3d-134B
total_misses_437TC16 = re.search(
    r"Total_misses (\d+)", content_437TC16).group(1)
total_miss_rate_437TC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_437TC16).group(1)
total_read_misses_437TC16 = re.search(
    r"Total_read_misses (\d+)", content_437TC16).group(1)
total_read_miss_rate_437TC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_437TC16).group(1)
total_write_misses_437TC16 = re.search(
    r"Total_write_misses (\d+)", content_437TC16).group(1)
total_write_miss_rate_437TC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_437TC16).group(1)
print(">>>>>All TC16 437.leslie3d-134B variables where obtained successfully")

# 444.namd-120B
total_misses_444TC16 = re.search(
    r"Total_misses (\d+)", content_444TC16).group(1)
total_miss_rate_444TC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_444TC16).group(1)
total_read_misses_444TC16 = re.search(
    r"Total_read_misses (\d+)", content_444TC16).group(1)
total_read_miss_rate_444TC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_444TC16).group(1)
total_write_misses_444TC16 = re.search(
    r"Total_write_misses (\d+)", content_444TC16).group(1)
total_write_miss_rate_444TC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_444TC16).group(1)
print(">>>>>All TC16 444.namd-120B variables where obtained successfully")

# 445.gobmk-17B
total_misses_445TC16 = re.search(
    r"Total_misses (\d+)", content_445TC16).group(1)
total_miss_rate_445TC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_445TC16).group(1)
total_read_misses_445TC16 = re.search(
    r"Total_read_misses (\d+)", content_445TC16).group(1)
total_read_miss_rate_445TC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_445TC16).group(1)
total_write_misses_445TC16 = re.search(
    r"Total_write_misses (\d+)", content_445TC16).group(1)
total_write_miss_rate_445TC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_445TC16).group(1)
print(">>>>>All TC16 445.gobmk-17B variables where obtained successfully")

# 450.soplex-247B
total_misses_450TC16 = re.search(
    r"Total_misses (\d+)", content_450TC16).group(1)
total_miss_rate_450TC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_450TC16).group(1)
total_read_misses_450TC16 = re.search(
    r"Total_read_misses (\d+)", content_450TC16).group(1)
total_read_miss_rate_450TC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_450TC16).group(1)
total_write_misses_450TC16 = re.search(
    r"Total_write_misses (\d+)", content_450TC16).group(1)
total_write_miss_rate_450TC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_450TC16).group(1)
print(">>>>>All TC16 450.soplex-247B variables where obtained successfully")

# 453.povray-887B
total_misses_453TC16 = re.search(
    r"Total_misses (\d+)", content_453TC16).group(1)
total_miss_rate_453TC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_453TC16).group(1)
total_read_misses_453TC16 = re.search(
    r"Total_read_misses (\d+)", content_453TC16).group(1)
total_read_miss_rate_453TC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_453TC16).group(1)
total_write_misses_453TC16 = re.search(
    r"Total_write_misses (\d+)", content_453TC16).group(1)
total_write_miss_rate_453TC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_453TC16).group(1)
print(">>>>>All TC16 453.povray-887B variables where obtained successfully")

# 454.calculix-104B
total_misses_454TC16 = re.search(
    r"Total_misses (\d+)", content_454TC16).group(1)
total_miss_rate_454TC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_454TC16).group(1)
total_read_misses_454TC16 = re.search(
    r"Total_read_misses (\d+)", content_454TC16).group(1)
total_read_miss_rate_454TC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_454TC16).group(1)
total_write_misses_454TC16 = re.search(
    r"Total_write_misses (\d+)", content_454TC16).group(1)
total_write_miss_rate_454TC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_454TC16).group(1)
print(">>>>>All TC16 454.calculix-104B variables where obtained successfully")

# 456.hmmer-191B
total_misses_456TC16 = re.search(
    r"Total_misses (\d+)", content_456TC16).group(1)
total_miss_rate_456TC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_456TC16).group(1)
total_read_misses_456TC16 = re.search(
    r"Total_read_misses (\d+)", content_456TC16).group(1)
total_read_miss_rate_456TC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_456TC16).group(1)
total_write_misses_456TC16 = re.search(
    r"Total_write_misses (\d+)", content_456TC16).group(1)
total_write_miss_rate_456TC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_456TC16).group(1)
print(">>>>>All TC16 456.hmmer-191B variables where obtained successfully")

# 458.sjeng-1088B
total_misses_458TC16 = re.search(
    r"Total_misses (\d+)", content_458TC16).group(1)
total_miss_rate_458TC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_458TC16).group(1)
total_read_misses_458TC16 = re.search(
    r"Total_read_misses (\d+)", content_458TC16).group(1)
total_read_miss_rate_458TC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_458TC16).group(1)
total_write_misses_458TC16 = re.search(
    r"Total_write_misses (\d+)", content_458TC16).group(1)
total_write_miss_rate_458TC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_458TC16).group(1)
print(">>>>>All TC16 458.sjeng-1088B variables where obtained successfully")

# 459.GemsFDTD-1169B
total_misses_459TC16 = re.search(
    r"Total_misses (\d+)", content_459TC16).group(1)
total_miss_rate_459TC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_459TC16).group(1)
total_read_misses_459TC16 = re.search(
    r"Total_read_misses (\d+)", content_459TC16).group(1)
total_read_miss_rate_459TC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_459TC16).group(1)
total_write_misses_459TC16 = re.search(
    r"Total_write_misses (\d+)", content_459TC16).group(1)
total_write_miss_rate_459TC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_459TC16).group(1)
print(">>>>>All TC16 459.GemsFDTD-1169B variables where obtained successfully")

# 462.libquantum-1343B
total_misses_462TC16 = re.search(
    r"Total_misses (\d+)", content_462TC16).group(1)
total_miss_rate_462TC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_462TC16).group(1)
total_read_misses_462TC16 = re.search(
    r"Total_read_misses (\d+)", content_462TC16).group(1)
total_read_miss_rate_462TC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_462TC16).group(1)
total_write_misses_462TC16 = re.search(
    r"Total_write_misses (\d+)", content_462TC16).group(1)
total_write_miss_rate_462TC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_462TC16).group(1)
print(">>>>>All TC16 462.libquantum-1343B variables where obtained successfully")

# 464.h264ref-30B
total_misses_464TC16 = re.search(
    r"Total_misses (\d+)", content_464TC16).group(1)
total_miss_rate_464TC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_464TC16).group(1)
total_read_misses_464TC16 = re.search(
    r"Total_read_misses (\d+)", content_464TC16).group(1)
total_read_miss_rate_464TC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_464TC16).group(1)
total_write_misses_464TC16 = re.search(
    r"Total_write_misses (\d+)", content_464TC16).group(1)
total_write_miss_rate_464TC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_464TC16).group(1)
print(">>>>>All TC16 464.h264ref-30B variables where obtained successfully")

# 465.tonto-1769B
total_misses_465TC16 = re.search(
    r"Total_misses (\d+)", content_465TC16).group(1)
total_miss_rate_465TC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_465TC16).group(1)
total_read_misses_465TC16 = re.search(
    r"Total_read_misses (\d+)", content_465TC16).group(1)
total_read_miss_rate_465TC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_465TC16).group(1)
total_write_misses_465TC16 = re.search(
    r"Total_write_misses (\d+)", content_465TC16).group(1)
total_write_miss_rate_465TC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_465TC16).group(1)
print(">>>>>All TC16 465.tonto-1769B variables where obtained successfully")

# 470.lbm-1274B
total_misses_470TC16 = re.search(
    r"Total_misses (\d+)", content_470TC16).group(1)
total_miss_rate_470TC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_470TC16).group(1)
total_read_misses_470TC16 = re.search(
    r"Total_read_misses (\d+)", content_470TC16).group(1)
total_read_miss_rate_470TC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_470TC16).group(1)
total_write_misses_470TC16 = re.search(
    r"Total_write_misses (\d+)", content_470TC16).group(1)
total_write_miss_rate_470TC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_470TC16).group(1)
print(">>>>>All TC16 470.lbm-1274B variables where obtained successfully")

# 471.omnetpp-188B
total_misses_471TC16 = re.search(
    r"Total_misses (\d+)", content_471TC16).group(1)
total_miss_rate_471TC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_471TC16).group(1)
total_read_misses_471TC16 = re.search(
    r"Total_read_misses (\d+)", content_471TC16).group(1)
total_read_miss_rate_471TC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_471TC16).group(1)
total_write_misses_471TC16 = re.search(
    r"Total_write_misses (\d+)", content_471TC16).group(1)
total_write_miss_rate_471TC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_471TC16).group(1)
print(">>>>>All TC16 471.omnetpp-188B variables where obtained successfully")

# 473.astar-153B
total_misses_473TC16 = re.search(
    r"Total_misses (\d+)", content_473TC16).group(1)
total_miss_rate_473TC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_473TC16).group(1)
total_read_misses_473TC16 = re.search(
    r"Total_read_misses (\d+)", content_473TC16).group(1)
total_read_miss_rate_473TC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_473TC16).group(1)
total_write_misses_473TC16 = re.search(
    r"Total_write_misses (\d+)", content_473TC16).group(1)
total_write_miss_rate_473TC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_473TC16).group(1)
print(">>>>>All TC16 473.astar-153B variables where obtained successfully")

# 481.wrf-1170B
total_misses_481TC16 = re.search(
    r"Total_misses (\d+)", content_481TC16).group(1)
total_miss_rate_481TC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_481TC16).group(1)
total_read_misses_481TC16 = re.search(
    r"Total_read_misses (\d+)", content_481TC16).group(1)
total_read_miss_rate_481TC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_481TC16).group(1)
total_write_misses_481TC16 = re.search(
    r"Total_write_misses (\d+)", content_481TC16).group(1)
total_write_miss_rate_481TC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_481TC16).group(1)
print(">>>>>All TC16 481.wrf-1170B variables where obtained successfully")

# 482.sphinx3-1100B
total_misses_482TC16 = re.search(
    r"Total_misses (\d+)", content_482TC16).group(1)
total_miss_rate_482TC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_482TC16).group(1)
total_read_misses_482TC16 = re.search(
    r"Total_read_misses (\d+)", content_482TC16).group(1)
total_read_miss_rate_482TC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_482TC16).group(1)
total_write_misses_482TC16 = re.search(
    r"Total_write_misses (\d+)", content_482TC16).group(1)
total_write_miss_rate_482TC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_482TC16).group(1)
print(">>>>>All TC16 482.sphinx3-1100B variables where obtained successfully")

# 483.xalancbmk-127B
total_misses_483TC16 = re.search(
    r"Total_misses (\d+)", content_483TC16).group(1)
total_miss_rate_483TC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_483TC16).group(1)
total_read_misses_483TC16 = re.search(
    r"Total_read_misses (\d+)", content_483TC16).group(1)
total_read_miss_rate_483TC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_483TC16).group(1)
total_write_misses_483TC16 = re.search(
    r"Total_write_misses (\d+)", content_483TC16).group(1)
total_write_miss_rate_483TC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_483TC16).group(1)
print(">>>>>All TC16 483.xalancbmk-127B variables where obtained successfully")

#############################
# Adjunta datos a dataframe #
#############################

# **400.perlbench-41B**

tabla_TC16.at['400.perlbench-41B', 'Total Misses'] = total_misses_400TC16

tabla_TC16.at['400.perlbench-41B',
              'Miss rate total [%]'] = total_miss_rate_400TC16

tabla_TC16.at['400.perlbench-41B',
              'Misses lectura'] = total_read_misses_400TC16

tabla_TC16.at['400.perlbench-41B',
              'Miss rate lectura [%]'] = total_read_miss_rate_400TC16

tabla_TC16.at['400.perlbench-41B',
              'Misses escritura'] = total_write_misses_400TC16

tabla_TC16.at['400.perlbench-41B',
              'Miss rate escritura [%]'] = total_write_miss_rate_400TC16

# **401.bzip2-226B**

tabla_TC16.at['401.bzip2-226B', 'Total Misses'] = total_misses_401TC16

tabla_TC16.at['401.bzip2-226B',
              'Miss rate total [%]'] = total_miss_rate_401TC16

tabla_TC16.at['401.bzip2-226B', 'Misses lectura'] = total_read_misses_401TC16

tabla_TC16.at['401.bzip2-226B',
              'Miss rate lectura [%]'] = total_read_miss_rate_401TC16

tabla_TC16.at['401.bzip2-226B',
              'Misses escritura'] = total_write_misses_401TC16

tabla_TC16.at['401.bzip2-226B',
              'Miss rate escritura [%]'] = total_write_miss_rate_401TC16

# **403.gcc-16B**

tabla_TC16.at['403.gcc-16B', 'Total Misses'] = total_misses_403TC16

tabla_TC16.at['403.gcc-16B', 'Miss rate total [%]'] = total_miss_rate_403TC16

tabla_TC16.at['403.gcc-16B', 'Misses lectura'] = total_read_misses_403TC16

tabla_TC16.at['403.gcc-16B',
              'Miss rate lectura [%]'] = total_read_miss_rate_403TC16

tabla_TC16.at['403.gcc-16B',
              'Misses escritura'] = total_write_misses_403TC16

tabla_TC16.at['403.gcc-16B',
              'Miss rate escritura [%]'] = total_write_miss_rate_403TC16

# **410.bwaves-1963B**

tabla_TC16.at['410.bwaves-1963B', 'Total Misses'] = total_misses_410TC16

tabla_TC16.at['410.bwaves-1963B',
              'Miss rate total [%]'] = total_miss_rate_410TC16

tabla_TC16.at['410.bwaves-1963B', 'Misses lectura'] = total_read_misses_410TC16

tabla_TC16.at['410.bwaves-1963B',
              'Miss rate lectura [%]'] = total_read_miss_rate_410TC16

tabla_TC16.at['410.bwaves-1963B',
              'Misses escritura'] = total_write_misses_410TC16

tabla_TC16.at['410.bwaves-1963B',
              'Miss rate escritura [%]'] = total_write_miss_rate_410TC16

# **416.gamess-875B**

tabla_TC16.at['416.gamess-875B', 'Total Misses'] = total_misses_416TC16

tabla_TC16.at['416.gamess-875B',
              'Miss rate total [%]'] = total_miss_rate_416TC16

tabla_TC16.at['416.gamess-875B', 'Misses lectura'] = total_read_misses_416TC16

tabla_TC16.at['416.gamess-875B',
              'Miss rate lectura [%]'] = total_read_miss_rate_416TC16

tabla_TC16.at['416.gamess-875B',
              'Misses escritura'] = total_write_misses_416TC16

tabla_TC16.at['416.gamess-875B',
              'Miss rate escritura [%]'] = total_write_miss_rate_416TC16

# **429.mcf-184B**

tabla_TC16.at['429.mcf-184B', 'Total Misses'] = total_misses_429TC16

tabla_TC16.at['429.mcf-184B', 'Miss rate total [%]'] = total_miss_rate_429TC16

tabla_TC16.at['429.mcf-184B', 'Misses lectura'] = total_read_misses_429TC16

tabla_TC16.at['429.mcf-184B',
              'Miss rate lectura [%]'] = total_read_miss_rate_429TC16

tabla_TC16.at['429.mcf-184B',
              'Misses escritura'] = total_write_misses_429TC16

tabla_TC16.at['429.mcf-184B',
              'Miss rate escritura [%]'] = total_write_miss_rate_429TC16

# **433.milc-127B**

tabla_TC16.at['433.milc-127B', 'Total Misses'] = total_misses_433TC16

tabla_TC16.at['433.milc-127B', 'Miss rate total [%]'] = total_miss_rate_433TC16

tabla_TC16.at['433.milc-127B', 'Misses lectura'] = total_read_misses_433TC16

tabla_TC16.at['433.milc-127B',
              'Miss rate lectura [%]'] = total_read_miss_rate_433TC16

tabla_TC16.at['433.milc-127B',
              'Misses escritura'] = total_write_misses_433TC16

tabla_TC16.at['433.milc-127B',
              'Miss rate escritura [%]'] = total_write_miss_rate_433TC16

# **435.gromacs-111B**

tabla_TC16.at['435.gromacs-111B', 'Total Misses'] = total_misses_435TC16

tabla_TC16.at['435.gromacs-111B',
              'Miss rate total [%]'] = total_miss_rate_435TC16

tabla_TC16.at['435.gromacs-111B', 'Misses lectura'] = total_read_misses_435TC16

tabla_TC16.at['435.gromacs-111B',
              'Miss rate lectura [%]'] = total_read_miss_rate_435TC16

tabla_TC16.at['435.gromacs-111B',
              'Misses escritura'] = total_write_misses_435TC16

tabla_TC16.at['435.gromacs-111B',
              'Miss rate escritura [%]'] = total_write_miss_rate_435TC16
# **436.cactusADM-1804B**

tabla_TC16.at['436.cactusADM-1804B', 'Total Misses'] = total_misses_436TC16

tabla_TC16.at['436.cactusADM-1804B',
              'Miss rate total [%]'] = total_miss_rate_436TC16

tabla_TC16.at['436.cactusADM-1804B',
              'Misses lectura'] = total_read_misses_436TC16

tabla_TC16.at['436.cactusADM-1804B',
              'Miss rate lectura [%]'] = total_read_miss_rate_436TC16

tabla_TC16.at['436.cactusADM-1804B',
              'Misses escritura'] = total_write_misses_436TC16

tabla_TC16.at['436.cactusADM-1804B',
              'Miss rate escritura [%]'] = total_write_miss_rate_436TC16

# **437.leslie3d-134B**

tabla_TC16.at['437.leslie3d-134B', 'Total Misses'] = total_misses_437TC16

tabla_TC16.at['437.leslie3d-134B',
              'Miss rate total [%]'] = total_miss_rate_437TC16

tabla_TC16.at['437.leslie3d-134B',
              'Misses lectura'] = total_read_misses_437TC16

tabla_TC16.at['437.leslie3d-134B',
              'Miss rate lectura [%]'] = total_read_miss_rate_437TC16

tabla_TC16.at['437.leslie3d-134B',
              'Misses escritura'] = total_write_misses_437TC16

tabla_TC16.at['437.leslie3d-134B',
              'Miss rate escritura [%]'] = total_write_miss_rate_437TC16

# **444.namd-120B**

tabla_TC16.at['444.namd-120B', 'Total Misses'] = total_misses_444TC16

tabla_TC16.at['444.namd-120B', 'Miss rate total [%]'] = total_miss_rate_444TC16

tabla_TC16.at['444.namd-120B', 'Misses lectura'] = total_read_misses_444TC16

tabla_TC16.at['444.namd-120B',
              'Miss rate lectura [%]'] = total_read_miss_rate_444TC16

tabla_TC16.at['444.namd-120B',
              'Misses escritura'] = total_write_misses_444TC16

tabla_TC16.at['444.namd-120B',
              'Miss rate escritura [%]'] = total_write_miss_rate_444TC16

# **445.gobmk-17B**

tabla_TC16.at['445.gobmk-17B', 'Total Misses'] = total_misses_445TC16

tabla_TC16.at['445.gobmk-17B', 'Miss rate total [%]'] = total_miss_rate_445TC16

tabla_TC16.at['445.gobmk-17B', 'Misses lectura'] = total_read_misses_445TC16

tabla_TC16.at['445.gobmk-17B',
              'Miss rate lectura [%]'] = total_read_miss_rate_445TC16

tabla_TC16.at['445.gobmk-17B',
              'Misses escritura'] = total_write_misses_445TC16

tabla_TC16.at['445.gobmk-17B',
              'Miss rate escritura [%]'] = total_write_miss_rate_445TC16

# **450.soplex-247B**

tabla_TC16.at['450.soplex-247B', 'Total Misses'] = total_misses_450TC16

tabla_TC16.at['450.soplex-247B',
              'Miss rate total [%]'] = total_miss_rate_450TC16

tabla_TC16.at['450.soplex-247B', 'Misses lectura'] = total_read_misses_450TC16

tabla_TC16.at['450.soplex-247B',
              'Miss rate lectura [%]'] = total_read_miss_rate_450TC16

tabla_TC16.at['450.soplex-247B',
              'Misses escritura'] = total_write_misses_450TC16

tabla_TC16.at['450.soplex-247B',
              'Miss rate escritura [%]'] = total_write_miss_rate_450TC16

# **453.povray-887B**

tabla_TC16.at['453.povray-887B', 'Total Misses'] = total_misses_453TC16

tabla_TC16.at['453.povray-887B',
              'Miss rate total [%]'] = total_miss_rate_453TC16

tabla_TC16.at['453.povray-887B', 'Misses lectura'] = total_read_misses_453TC16

tabla_TC16.at['453.povray-887B',
              'Miss rate lectura [%]'] = total_read_miss_rate_453TC16

tabla_TC16.at['453.povray-887B',
              'Misses escritura'] = total_write_misses_453TC16

tabla_TC16.at['453.povray-887B',
              'Miss rate escritura [%]'] = total_write_miss_rate_453TC16

# **454.calculix-104B**

tabla_TC16.at['454.calculix-104B', 'Total Misses'] = total_misses_454TC16

tabla_TC16.at['454.calculix-104B',
              'Miss rate total [%]'] = total_miss_rate_454TC16

tabla_TC16.at['454.calculix-104B',
              'Misses lectura'] = total_read_misses_454TC16

tabla_TC16.at['454.calculix-104B',
              'Miss rate lectura [%]'] = total_read_miss_rate_454TC16

tabla_TC16.at['454.calculix-104B',
              'Misses escritura'] = total_write_misses_454TC16

tabla_TC16.at['454.calculix-104B',
              'Miss rate escritura [%]'] = total_write_miss_rate_454TC16

# **456.hmmer-191B**

tabla_TC16.at['456.hmmer-191B', 'Total Misses'] = total_misses_456TC16

tabla_TC16.at['456.hmmer-191B',
              'Miss rate total [%]'] = total_miss_rate_456TC16

tabla_TC16.at['456.hmmer-191B', 'Misses lectura'] = total_read_misses_456TC16

tabla_TC16.at['456.hmmer-191B',
              'Miss rate lectura [%]'] = total_read_miss_rate_456TC16

tabla_TC16.at['456.hmmer-191B',
              'Misses escritura'] = total_write_misses_456TC16

tabla_TC16.at['456.hmmer-191B',
              'Miss rate escritura [%]'] = total_write_miss_rate_456TC16

# **458.sjeng-1088B**

tabla_TC16.at['458.sjeng-1088B', 'Total Misses'] = total_misses_458TC16

tabla_TC16.at['458.sjeng-1088B',
              'Miss rate total [%]'] = total_miss_rate_458TC16

tabla_TC16.at['458.sjeng-1088B', 'Misses lectura'] = total_read_misses_458TC16

tabla_TC16.at['458.sjeng-1088B',
              'Miss rate lectura [%]'] = total_read_miss_rate_458TC16

tabla_TC16.at['458.sjeng-1088B',
              'Misses escritura'] = total_write_misses_458TC16

tabla_TC16.at['458.sjeng-1088B',
              'Miss rate escritura [%]'] = total_write_miss_rate_458TC16

# **459.GemsFDTD-1169B**

tabla_TC16.at['459.GemsFDTD-1169B', 'Total Misses'] = total_misses_459TC16

tabla_TC16.at['459.GemsFDTD-1169B',
              'Miss rate total [%]'] = total_miss_rate_459TC16

tabla_TC16.at['459.GemsFDTD-1169B',
              'Misses lectura'] = total_read_misses_459TC16

tabla_TC16.at['459.GemsFDTD-1169B',
              'Miss rate lectura [%]'] = total_read_miss_rate_459TC16

tabla_TC16.at['459.GemsFDTD-1169B',
              'Misses escritura'] = total_write_misses_459TC16

tabla_TC16.at['459.GemsFDTD-1169B',
              'Miss rate escritura [%]'] = total_write_miss_rate_459TC16

# **462.libquantum-1343B**

tabla_TC16.at['462.libquantum-1343B', 'Total Misses'] = total_misses_462TC16

tabla_TC16.at['462.libquantum-1343B',
              'Miss rate total [%]'] = total_miss_rate_462TC16

tabla_TC16.at['462.libquantum-1343B',
              'Misses lectura'] = total_read_misses_462TC16

tabla_TC16.at['462.libquantum-1343B',
              'Miss rate lectura [%]'] = total_read_miss_rate_462TC16

tabla_TC16.at['462.libquantum-1343B',
              'Misses escritura'] = total_write_misses_462TC16

tabla_TC16.at['462.libquantum-1343B',
              'Miss rate escritura [%]'] = total_write_miss_rate_462TC16

# **464.h264ref-30B**

tabla_TC16.at['464.h264ref-30B', 'Total Misses'] = total_misses_464TC16

tabla_TC16.at['464.h264ref-30B',
              'Miss rate total [%]'] = total_miss_rate_464TC16

tabla_TC16.at['464.h264ref-30B', 'Misses lectura'] = total_read_misses_464TC16

tabla_TC16.at['464.h264ref-30B',
              'Miss rate lectura [%]'] = total_read_miss_rate_464TC16

tabla_TC16.at['464.h264ref-30B',
              'Misses escritura'] = total_write_misses_464TC16

tabla_TC16.at['464.h264ref-30B',
              'Miss rate escritura [%]'] = total_write_miss_rate_464TC16

# **465.tonto-1769B**

tabla_TC16.at['465.tonto-1769B', 'Total Misses'] = total_misses_465TC16

tabla_TC16.at['465.tonto-1769B',
              'Miss rate total [%]'] = total_miss_rate_465TC16

tabla_TC16.at['465.tonto-1769B', 'Misses lectura'] = total_read_misses_465TC16

tabla_TC16.at['465.tonto-1769B',
              'Miss rate lectura [%]'] = total_read_miss_rate_465TC16

tabla_TC16.at['465.tonto-1769B',
              'Misses escritura'] = total_write_misses_465TC16
tabla_TC16.at['465.tonto-1769B',
              'Miss rate escritura [%]'] = total_write_miss_rate_465TC16

# **470.lbm-1274B**

tabla_TC16.at['470.lbm-1274B', 'Total Misses'] = total_misses_470TC16

tabla_TC16.at['470.lbm-1274B', 'Miss rate total [%]'] = total_miss_rate_470TC16

tabla_TC16.at['470.lbm-1274B', 'Misses lectura'] = total_read_misses_470TC16

tabla_TC16.at['470.lbm-1274B',
              'Miss rate lectura [%]'] = total_read_miss_rate_470TC16

tabla_TC16.at['470.lbm-1274B',
              'Misses escritura'] = total_write_misses_470TC16

tabla_TC16.at['470.lbm-1274B',
              'Miss rate escritura [%]'] = total_write_miss_rate_470TC16

# **471.omnetpp-188B**

tabla_TC16.at['471.omnetpp-188B', 'Total Misses'] = total_misses_471TC16

tabla_TC16.at['471.omnetpp-188B',
              'Miss rate total [%]'] = total_miss_rate_471TC16

tabla_TC16.at['471.omnetpp-188B', 'Misses lectura'] = total_read_misses_471TC16

tabla_TC16.at['471.omnetpp-188B',
              'Miss rate lectura [%]'] = total_read_miss_rate_471TC16

tabla_TC16.at['471.omnetpp-188B',
              'Misses escritura'] = total_write_misses_471TC16

tabla_TC16.at['471.omnetpp-188B',
              'Miss rate escritura [%]'] = total_write_miss_rate_471TC16

# **473.astar-153B**

tabla_TC16.at['473.astar-153B', 'Total Misses'] = total_misses_473TC16

tabla_TC16.at['473.astar-153B',
              'Miss rate total [%]'] = total_miss_rate_473TC16

tabla_TC16.at['473.astar-153B', 'Misses lectura'] = total_read_misses_473TC16

tabla_TC16.at['473.astar-153B',
              'Miss rate lectura [%]'] = total_read_miss_rate_473TC16

tabla_TC16.at['473.astar-153B',
              'Misses escritura'] = total_write_misses_473TC16

tabla_TC16.at['473.astar-153B',
              'Miss rate escritura [%]'] = total_write_miss_rate_473TC16

# **481.wrf-1170B**

tabla_TC16.at['481.wrf-1170B', 'Total Misses'] = total_misses_481TC16

tabla_TC16.at['481.wrf-1170B', 'Miss rate total [%]'] = total_miss_rate_481TC16

tabla_TC16.at['481.wrf-1170B', 'Misses lectura'] = total_read_misses_481TC16

tabla_TC16.at['481.wrf-1170B',
              'Miss rate lectura [%]'] = total_read_miss_rate_481TC16

tabla_TC16.at['481.wrf-1170B',
              'Misses escritura'] = total_write_misses_481TC16

tabla_TC16.at['481.wrf-1170B',
              'Miss rate escritura [%]'] = total_write_miss_rate_481TC16

# **482.sphinx3-1100B**

tabla_TC16.at['482.sphinx3-1100B', 'Total Misses'] = total_misses_482TC16

tabla_TC16.at['482.sphinx3-1100B',
              'Miss rate total [%]'] = total_miss_rate_482TC16

tabla_TC16.at['482.sphinx3-1100B',
              'Misses lectura'] = total_read_misses_482TC16

tabla_TC16.at['482.sphinx3-1100B',
              'Miss rate lectura [%]'] = total_read_miss_rate_482TC16

tabla_TC16.at['482.sphinx3-1100B',
              'Misses escritura'] = total_write_misses_482TC16

tabla_TC16.at['482.sphinx3-1100B',
              'Miss rate escritura [%]'] = total_write_miss_rate_482TC16

# **483.xalancbmk-127B**

tabla_TC16.at['483.xalancbmk-127B', 'Total Misses'] = total_misses_483TC16

tabla_TC16.at['483.xalancbmk-127B',
              'Miss rate total [%]'] = total_miss_rate_483TC16

tabla_TC16.at['483.xalancbmk-127B',
              'Misses lectura'] = total_read_misses_483TC16

tabla_TC16.at['483.xalancbmk-127B',
              'Miss rate lectura [%]'] = total_read_miss_rate_483TC16

tabla_TC16.at['483.xalancbmk-127B',
              'Misses escritura'] = total_write_misses_483TC16

tabla_TC16.at['483.xalancbmk-127B',
              'Miss rate escritura [%]'] = total_write_miss_rate_483TC16

print(">>>>>All TC16 data has been uploaded successfully")

###########################################
# Extractor para experimento con tamaño 32#
###########################################

# Creación de tablas para adjuntar valores
# Una tabla por tamaño
tabla_TC32 = pd.DataFrame(index=[
    '400.perlbench-41B', '401.bzip2-226B', '403.gcc-16B', '410.bwaves-1963B', '416.gamess-875B', '429.mcf-184B', '433.milc-127B',
    '435.gromacs-111B', '436.cactusADM-1804B', '437.leslie3d-134B', '444.namd-120B', '445.gobmk-17B',
    '450.soplex-247B', '453.povray-887B', '454.calculix-104B', '456.hmmer-191B', '458.sjeng-1088B', '459.GemsFDTD-1169B',
    '462.libquantum-1343B', '464.h264ref-30B', '465.tonto-1769B', '470.lbm-1274B', '471.omnetpp-188B', '473.astar-153B', '481.wrf-1170B',
    '482.sphinx3-1100B', '483.xalancbmk-127B'], columns=[
    'App', 'Total Misses', 'Miss rate total [%]', 'Misses lectura', 'Miss rate lectura [%]', 'Misses escritura', 'Miss rate escritura [%]'])
tabla_TC32['App'] = tabla_TC32.index

# Files paths
filename_55 = "RESULTS_TC/400TC32.txt"
filename_56 = "RESULTS_TC/401TC32.txt"
filename_57 = "RESULTS_TC/403TC32.txt"
filename_58 = "RESULTS_TC/410TC32.txt"
filename_59 = "RESULTS_TC/416TC32.txt"
filename_60 = "RESULTS_TC/429TC32.txt"
filename_61 = "RESULTS_TC/433TC32.txt"
filename_62 = "RESULTS_TC/435TC32.txt"
filename_63 = "RESULTS_TC/436TC32.txt"
filename_64 = "RESULTS_TC/437TC32.txt"
filename_65 = "RESULTS_TC/444TC32.txt"
filename_66 = "RESULTS_TC/445TC32.txt"
filename_67 = "RESULTS_TC/450TC32.txt"
filename_68 = "RESULTS_TC/453TC32.txt"
filename_69 = "RESULTS_TC/454TC32.txt"
filename_70 = "RESULTS_TC/456TC32.txt"
filename_71 = "RESULTS_TC/458TC32.txt"
filename_72 = "RESULTS_TC/459TC32.txt"
filename_73 = "RESULTS_TC/462TC32.txt"
filename_74 = "RESULTS_TC/464TC32.txt"
filename_75 = "RESULTS_TC/465TC32.txt"
filename_76 = "RESULTS_TC/470TC32.txt"
filename_77 = "RESULTS_TC/471TC32.txt"
filename_78 = "RESULTS_TC/473TC32.txt"
filename_79 = "RESULTS_TC/481TC32.txt"
filename_80 = "RESULTS_TC/482TC32.txt"
filename_81 = "RESULTS_TC/483TC32.txt"

# Content file extracter
with open(filename_55, 'r') as file:
    content_400TC32 = file.read()
with open(filename_56, 'r') as file:
    content_401TC32 = file.read()
with open(filename_57, 'r') as file:
    content_403TC32 = file.read()
with open(filename_58, 'r') as file:
    content_410TC32 = file.read()
with open(filename_59, 'r') as file:
    content_416TC32 = file.read()
with open(filename_60, 'r') as file:
    content_429TC32 = file.read()
with open(filename_61, 'r') as file:
    content_433TC32 = file.read()
with open(filename_62, 'r') as file:
    content_435TC32 = file.read()
with open(filename_63, 'r') as file:
    content_436TC32 = file.read()
with open(filename_64, 'r') as file:
    content_437TC32 = file.read()
with open(filename_65, 'r') as file:
    content_444TC32 = file.read()
with open(filename_66, 'r') as file:
    content_445TC32 = file.read()
with open(filename_67, 'r') as file:
    content_450TC32 = file.read()
with open(filename_68, 'r') as file:
    content_453TC32 = file.read()
with open(filename_69, 'r') as file:
    content_454TC32 = file.read()
with open(filename_70, 'r') as file:
    content_456TC32 = file.read()
with open(filename_71, 'r') as file:
    content_458TC32 = file.read()
with open(filename_72, 'r') as file:
    content_459TC32 = file.read()
with open(filename_73, 'r') as file:
    content_462TC32 = file.read()
with open(filename_74, 'r') as file:
    content_464TC32 = file.read()
with open(filename_75, 'r') as file:
    content_465TC32 = file.read()
with open(filename_76, 'r') as file:
    content_470TC32 = file.read()
with open(filename_77, 'r') as file:
    content_471TC32 = file.read()
with open(filename_78, 'r') as file:
    content_473TC32 = file.read()
with open(filename_79, 'r') as file:
    content_481TC32 = file.read()
with open(filename_80, 'r') as file:
    content_482TC32 = file.read()
with open(filename_81, 'r') as file:
    content_483TC32 = file.read()

# Variables según aplicación

# 400.pearlbench-41B
total_misses_400TC32 = re.search(
    r"Total_misses (\d+)", content_400TC32).group(1)
total_miss_rate_400TC32 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_400TC32).group(1)
total_read_misses_400TC32 = re.search(
    r"Total_read_misses (\d+)", content_400TC32).group(1)
total_read_miss_rate_400TC32 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_400TC32).group(1)
total_write_misses_400TC32 = re.search(
    r"Total_write_misses (\d+)", content_400TC32).group(1)
total_write_miss_rate_400TC32 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_400TC32).group(1)
print(">>>>>All TC32 400.pearlbench-41B variables where obtained successfully")

# 401.bzip2-226B
total_misses_401TC32 = re.search(
    r"Total_misses (\d+)", content_401TC32).group(1)
total_miss_rate_401TC32 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_401TC32).group(1)
total_read_misses_401TC32 = re.search(
    r"Total_read_misses (\d+)", content_401TC32).group(1)
total_read_miss_rate_401TC32 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_401TC32).group(1)
total_write_misses_401TC32 = re.search(
    r"Total_write_misses (\d+)", content_401TC32).group(1)
total_write_miss_rate_401TC32 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_401TC32).group(1)
print(">>>>>All TC32 401.bzip2-226B variables where obtained successfully")

# 403.gcc-16B
total_misses_403TC32 = re.search(
    r"Total_misses (\d+)", content_403TC32).group(1)
total_miss_rate_403TC32 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_403TC32).group(1)
total_read_misses_403TC32 = re.search(
    r"Total_read_misses (\d+)", content_403TC32).group(1)
total_read_miss_rate_403TC32 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_403TC32).group(1)
total_write_misses_403TC32 = re.search(
    r"Total_write_misses (\d+)", content_403TC32).group(1)
total_write_miss_rate_403TC32 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_403TC32).group(1)
print(">>>>>All TC32 403.gcc-16B variables where obtained successfully")

# 410.bwaves-1963B
total_misses_410TC32 = re.search(
    r"Total_misses (\d+)", content_410TC32).group(1)
total_miss_rate_410TC32 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_410TC32).group(1)
total_read_misses_410TC32 = re.search(
    r"Total_read_misses (\d+)", content_410TC32).group(1)
total_read_miss_rate_410TC32 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_410TC32).group(1)
total_write_misses_410TC32 = re.search(
    r"Total_write_misses (\d+)", content_410TC32).group(1)
total_write_miss_rate_410TC32 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_410TC32).group(1)
print(">>>>>All TC32 410.bwaves-1963B variables where obtained successfully")

# 416.gamess-875B
total_misses_416TC32 = re.search(
    r"Total_misses (\d+)", content_416TC32).group(1)
total_miss_rate_416TC32 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_416TC32).group(1)
total_read_misses_416TC32 = re.search(
    r"Total_read_misses (\d+)", content_416TC32).group(1)
total_read_miss_rate_416TC32 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_416TC32).group(1)
total_write_misses_416TC32 = re.search(
    r"Total_write_misses (\d+)", content_416TC32).group(1)
total_write_miss_rate_416TC32 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_416TC32).group(1)
print(">>>>>All TC32 416.gamess-875B variables where obtained successfully")

# 429.mcf-184B
total_misses_429TC32 = re.search(
    r"Total_misses (\d+)", content_429TC32).group(1)
total_miss_rate_429TC32 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_429TC32).group(1)
total_read_misses_429TC32 = re.search(
    r"Total_read_misses (\d+)", content_429TC32).group(1)
total_read_miss_rate_429TC32 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_429TC32).group(1)
total_write_misses_429TC32 = re.search(
    r"Total_write_misses (\d+)", content_429TC32).group(1)
total_write_miss_rate_429TC32 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_429TC32).group(1)
print(">>>>>All TC32 429.mcf-184B variables where obtained successfully")

# 433.milc-127B
total_misses_433TC32 = re.search(
    r"Total_misses (\d+)", content_433TC32).group(1)
total_miss_rate_433TC32 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_433TC32).group(1)
total_read_misses_433TC32 = re.search(
    r"Total_read_misses (\d+)", content_433TC32).group(1)
total_read_miss_rate_433TC32 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_433TC32).group(1)
total_write_misses_433TC32 = re.search(
    r"Total_write_misses (\d+)", content_433TC32).group(1)
total_write_miss_rate_433TC32 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_433TC32).group(1)
print(">>>>>All TC32 433.milc-127B variables where obtained successfully")

# 435.gromacs-111B
total_misses_435TC32 = re.search(
    r"Total_misses (\d+)", content_435TC32).group(1)
total_miss_rate_435TC32 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_435TC32).group(1)
total_read_misses_435TC32 = re.search(
    r"Total_read_misses (\d+)", content_435TC32).group(1)
total_read_miss_rate_435TC32 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_435TC32).group(1)
total_write_misses_435TC32 = re.search(
    r"Total_write_misses (\d+)", content_435TC32).group(1)
total_write_miss_rate_435TC32 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_435TC32).group(1)
print(">>>>>All TC32 435.gromacs-111B variables where obtained successfully")

# 436.cactusADM-1804B
total_misses_436TC32 = re.search(
    r"Total_misses (\d+)", content_436TC32).group(1)
total_miss_rate_436TC32 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_436TC32).group(1)
total_read_misses_436TC32 = re.search(
    r"Total_read_misses (\d+)", content_436TC32).group(1)
total_read_miss_rate_436TC32 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_436TC32).group(1)
total_write_misses_436TC32 = re.search(
    r"Total_write_misses (\d+)", content_436TC32).group(1)
total_write_miss_rate_436TC32 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_436TC32).group(1)
print(">>>>>All TC32 436.cactusADM-1804B variables where obtained successfully")

# 437.leslie3d-134B
total_misses_437TC32 = re.search(
    r"Total_misses (\d+)", content_437TC32).group(1)
total_miss_rate_437TC32 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_437TC32).group(1)
total_read_misses_437TC32 = re.search(
    r"Total_read_misses (\d+)", content_437TC32).group(1)
total_read_miss_rate_437TC32 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_437TC32).group(1)
total_write_misses_437TC32 = re.search(
    r"Total_write_misses (\d+)", content_437TC32).group(1)
total_write_miss_rate_437TC32 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_437TC32).group(1)
print(">>>>>All TC32 437.leslie3d-134B variables where obtained successfully")

# 444.namd-120B
total_misses_444TC32 = re.search(
    r"Total_misses (\d+)", content_444TC32).group(1)
total_miss_rate_444TC32 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_444TC32).group(1)
total_read_misses_444TC32 = re.search(
    r"Total_read_misses (\d+)", content_444TC32).group(1)
total_read_miss_rate_444TC32 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_444TC32).group(1)
total_write_misses_444TC32 = re.search(
    r"Total_write_misses (\d+)", content_444TC32).group(1)
total_write_miss_rate_444TC32 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_444TC32).group(1)
print(">>>>>All TC32 444.namd-120B variables where obtained successfully")

# 445.gobmk-17B
total_misses_445TC32 = re.search(
    r"Total_misses (\d+)", content_445TC32).group(1)
total_miss_rate_445TC32 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_445TC32).group(1)
total_read_misses_445TC32 = re.search(
    r"Total_read_misses (\d+)", content_445TC32).group(1)
total_read_miss_rate_445TC32 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_445TC32).group(1)
total_write_misses_445TC32 = re.search(
    r"Total_write_misses (\d+)", content_445TC32).group(1)
total_write_miss_rate_445TC32 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_445TC32).group(1)
print(">>>>>All TC32 445.gobmk-17B variables where obtained successfully")

# 450.soplex-247B
total_misses_450TC32 = re.search(
    r"Total_misses (\d+)", content_450TC32).group(1)
total_miss_rate_450TC32 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_450TC32).group(1)
total_read_misses_450TC32 = re.search(
    r"Total_read_misses (\d+)", content_450TC32).group(1)
total_read_miss_rate_450TC32 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_450TC32).group(1)
total_write_misses_450TC32 = re.search(
    r"Total_write_misses (\d+)", content_450TC32).group(1)
total_write_miss_rate_450TC32 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_450TC32).group(1)
print(">>>>>All TC32 450.soplex-247B variables where obtained successfully")

# 453.povray-887B
total_misses_453TC32 = re.search(
    r"Total_misses (\d+)", content_453TC32).group(1)
total_miss_rate_453TC32 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_453TC32).group(1)
total_read_misses_453TC32 = re.search(
    r"Total_read_misses (\d+)", content_453TC32).group(1)
total_read_miss_rate_453TC32 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_453TC32).group(1)
total_write_misses_453TC32 = re.search(
    r"Total_write_misses (\d+)", content_453TC32).group(1)
total_write_miss_rate_453TC32 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_453TC32).group(1)
print(">>>>>All TC32 453.povray-887B variables where obtained successfully")

# 454.calculix-104B
total_misses_454TC32 = re.search(
    r"Total_misses (\d+)", content_454TC32).group(1)
total_miss_rate_454TC32 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_454TC32).group(1)
total_read_misses_454TC32 = re.search(
    r"Total_read_misses (\d+)", content_454TC32).group(1)
total_read_miss_rate_454TC32 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_454TC32).group(1)
total_write_misses_454TC32 = re.search(
    r"Total_write_misses (\d+)", content_454TC32).group(1)
total_write_miss_rate_454TC32 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_454TC32).group(1)
print(">>>>>All TC32 454.calculix-104B variables where obtained successfully")

# 456.hmmer-191B
total_misses_456TC32 = re.search(
    r"Total_misses (\d+)", content_456TC32).group(1)
total_miss_rate_456TC32 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_456TC32).group(1)
total_read_misses_456TC32 = re.search(
    r"Total_read_misses (\d+)", content_456TC32).group(1)
total_read_miss_rate_456TC32 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_456TC32).group(1)
total_write_misses_456TC32 = re.search(
    r"Total_write_misses (\d+)", content_456TC32).group(1)
total_write_miss_rate_456TC32 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_456TC32).group(1)
print(">>>>>All TC32 456.hmmer-191B variables where obtained successfully")

# 458.sjeng-1088B
total_misses_458TC32 = re.search(
    r"Total_misses (\d+)", content_458TC32).group(1)
total_miss_rate_458TC32 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_458TC32).group(1)
total_read_misses_458TC32 = re.search(
    r"Total_read_misses (\d+)", content_458TC32).group(1)
total_read_miss_rate_458TC32 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_458TC32).group(1)
total_write_misses_458TC32 = re.search(
    r"Total_write_misses (\d+)", content_458TC32).group(1)
total_write_miss_rate_458TC32 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_458TC32).group(1)
print(">>>>>All TC32 458.sjeng-1088B variables where obtained successfully")

# 459.GemsFDTD-1169B
total_misses_459TC32 = re.search(
    r"Total_misses (\d+)", content_459TC32).group(1)
total_miss_rate_459TC32 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_459TC32).group(1)
total_read_misses_459TC32 = re.search(
    r"Total_read_misses (\d+)", content_459TC32).group(1)
total_read_miss_rate_459TC32 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_459TC32).group(1)
total_write_misses_459TC32 = re.search(
    r"Total_write_misses (\d+)", content_459TC32).group(1)
total_write_miss_rate_459TC32 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_459TC32).group(1)
print(">>>>>All TC32 459.GemsFDTD-1169B variables where obtained successfully")

# 462.libquantum-1343B
total_misses_462TC32 = re.search(
    r"Total_misses (\d+)", content_462TC32).group(1)
total_miss_rate_462TC32 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_462TC32).group(1)
total_read_misses_462TC32 = re.search(
    r"Total_read_misses (\d+)", content_462TC32).group(1)
total_read_miss_rate_462TC32 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_462TC32).group(1)
total_write_misses_462TC32 = re.search(
    r"Total_write_misses (\d+)", content_462TC32).group(1)
total_write_miss_rate_462TC32 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_462TC32).group(1)
print(">>>>>All TC32 462.libquantum-1343B variables where obtained successfully")

# 464.h264ref-30B
total_misses_464TC32 = re.search(
    r"Total_misses (\d+)", content_464TC32).group(1)
total_miss_rate_464TC32 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_464TC32).group(1)
total_read_misses_464TC32 = re.search(
    r"Total_read_misses (\d+)", content_464TC32).group(1)
total_read_miss_rate_464TC32 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_464TC32).group(1)
total_write_misses_464TC32 = re.search(
    r"Total_write_misses (\d+)", content_464TC32).group(1)
total_write_miss_rate_464TC32 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_464TC32).group(1)
print(">>>>>All TC32 464.h264ref-30B variables where obtained successfully")

# 465.tonto-1769B
total_misses_465TC32 = re.search(
    r"Total_misses (\d+)", content_465TC32).group(1)
total_miss_rate_465TC32 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_465TC32).group(1)
total_read_misses_465TC32 = re.search(
    r"Total_read_misses (\d+)", content_465TC32).group(1)
total_read_miss_rate_465TC32 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_465TC32).group(1)
total_write_misses_465TC32 = re.search(
    r"Total_write_misses (\d+)", content_465TC32).group(1)
total_write_miss_rate_465TC32 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_465TC32).group(1)
print(">>>>>All TC32 465.tonto-1769B variables where obtained successfully")

# 470.lbm-1274B
total_misses_470TC32 = re.search(
    r"Total_misses (\d+)", content_470TC32).group(1)
total_miss_rate_470TC32 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_470TC32).group(1)
total_read_misses_470TC32 = re.search(
    r"Total_read_misses (\d+)", content_470TC32).group(1)
total_read_miss_rate_470TC32 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_470TC32).group(1)
total_write_misses_470TC32 = re.search(
    r"Total_write_misses (\d+)", content_470TC32).group(1)
total_write_miss_rate_470TC32 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_470TC32).group(1)
print(">>>>>All TC32 470.lbm-1274B variables where obtained successfully")

# 471.omnetpp-188B
total_misses_471TC32 = re.search(
    r"Total_misses (\d+)", content_471TC32).group(1)
total_miss_rate_471TC32 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_471TC32).group(1)
total_read_misses_471TC32 = re.search(
    r"Total_read_misses (\d+)", content_471TC32).group(1)
total_read_miss_rate_471TC32 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_471TC32).group(1)
total_write_misses_471TC32 = re.search(
    r"Total_write_misses (\d+)", content_471TC32).group(1)
total_write_miss_rate_471TC32 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_471TC32).group(1)
print(">>>>>All TC32 471.omnetpp-188B variables where obtained successfully")

# 473.astar-153B
total_misses_473TC32 = re.search(
    r"Total_misses (\d+)", content_473TC32).group(1)
total_miss_rate_473TC32 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_473TC32).group(1)
total_read_misses_473TC32 = re.search(
    r"Total_read_misses (\d+)", content_473TC32).group(1)
total_read_miss_rate_473TC32 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_473TC32).group(1)
total_write_misses_473TC32 = re.search(
    r"Total_write_misses (\d+)", content_473TC32).group(1)
total_write_miss_rate_473TC32 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_473TC32).group(1)
print(">>>>>All TC32 473.astar-153B variables where obtained successfully")

# 481.wrf-1170B
total_misses_481TC32 = re.search(
    r"Total_misses (\d+)", content_481TC32).group(1)
total_miss_rate_481TC32 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_481TC32).group(1)
total_read_misses_481TC32 = re.search(
    r"Total_read_misses (\d+)", content_481TC32).group(1)
total_read_miss_rate_481TC32 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_481TC32).group(1)
total_write_misses_481TC32 = re.search(
    r"Total_write_misses (\d+)", content_481TC32).group(1)
total_write_miss_rate_481TC32 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_481TC32).group(1)
print(">>>>>All TC32 481.wrf-1170B variables where obtained successfully")

# 482.sphinx3-1100B
total_misses_482TC32 = re.search(
    r"Total_misses (\d+)", content_482TC32).group(1)
total_miss_rate_482TC32 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_482TC32).group(1)
total_read_misses_482TC32 = re.search(
    r"Total_read_misses (\d+)", content_482TC32).group(1)
total_read_miss_rate_482TC32 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_482TC32).group(1)
total_write_misses_482TC32 = re.search(
    r"Total_write_misses (\d+)", content_482TC32).group(1)
total_write_miss_rate_482TC32 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_482TC32).group(1)
print(">>>>>All TC32 482.sphinx3-1100B variables where obtained successfully")

# 483.xalancbmk-127B
total_misses_483TC32 = re.search(
    r"Total_misses (\d+)", content_483TC32).group(1)
total_miss_rate_483TC32 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_483TC32).group(1)
total_read_misses_483TC32 = re.search(
    r"Total_read_misses (\d+)", content_483TC32).group(1)
total_read_miss_rate_483TC32 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_483TC32).group(1)
total_write_misses_483TC32 = re.search(
    r"Total_write_misses (\d+)", content_483TC32).group(1)
total_write_miss_rate_483TC32 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_483TC32).group(1)
print(">>>>>All TC32 483.xalancbmk-127B variables where obtained successfully")

#############################
# Adjunta datos a dataframe #
#############################

# **400.perlbench-41B**

tabla_TC32.at['400.perlbench-41B', 'Total Misses'] = total_misses_400TC32

tabla_TC32.at['400.perlbench-41B',
              'Miss rate total [%]'] = total_miss_rate_400TC32

tabla_TC32.at['400.perlbench-41B',
              'Misses lectura'] = total_read_misses_400TC32

tabla_TC32.at['400.perlbench-41B',
              'Miss rate lectura [%]'] = total_read_miss_rate_400TC32

tabla_TC32.at['400.perlbench-41B',
              'Misses escritura'] = total_write_misses_400TC32

tabla_TC32.at['400.perlbench-41B',
              'Miss rate escritura [%]'] = total_write_miss_rate_400TC32

# **401.bzip2-226B**

tabla_TC32.at['401.bzip2-226B', 'Total Misses'] = total_misses_401TC32

tabla_TC32.at['401.bzip2-226B',
              'Miss rate total [%]'] = total_miss_rate_401TC32

tabla_TC32.at['401.bzip2-226B', 'Misses lectura'] = total_read_misses_401TC32

tabla_TC32.at['401.bzip2-226B',
              'Miss rate lectura [%]'] = total_read_miss_rate_401TC32

tabla_TC32.at['401.bzip2-226B',
              'Misses escritura'] = total_write_misses_401TC32

tabla_TC32.at['401.bzip2-226B',
              'Miss rate escritura [%]'] = total_write_miss_rate_401TC32

# **403.gcc-16B**

tabla_TC32.at['403.gcc-16B', 'Total Misses'] = total_misses_403TC32

tabla_TC32.at['403.gcc-16B', 'Miss rate total [%]'] = total_miss_rate_403TC32

tabla_TC32.at['403.gcc-16B', 'Misses lectura'] = total_read_misses_403TC32

tabla_TC32.at['403.gcc-16B',
              'Miss rate lectura [%]'] = total_read_miss_rate_403TC32

tabla_TC32.at['403.gcc-16B',
              'Misses escritura'] = total_write_misses_403TC32

tabla_TC32.at['403.gcc-16B',
              'Miss rate escritura [%]'] = total_write_miss_rate_403TC32

# **410.bwaves-1963B**

tabla_TC32.at['410.bwaves-1963B', 'Total Misses'] = total_misses_410TC32

tabla_TC32.at['410.bwaves-1963B',
              'Miss rate total [%]'] = total_miss_rate_410TC32

tabla_TC32.at['410.bwaves-1963B', 'Misses lectura'] = total_read_misses_410TC32

tabla_TC32.at['410.bwaves-1963B',
              'Miss rate lectura [%]'] = total_read_miss_rate_410TC32

tabla_TC32.at['410.bwaves-1963B',
              'Misses escritura'] = total_write_misses_410TC32

tabla_TC32.at['410.bwaves-1963B',
              'Miss rate escritura [%]'] = total_write_miss_rate_410TC32

# **416.gamess-875B**

tabla_TC32.at['416.gamess-875B', 'Total Misses'] = total_misses_416TC32

tabla_TC32.at['416.gamess-875B',
              'Miss rate total [%]'] = total_miss_rate_416TC32

tabla_TC32.at['416.gamess-875B', 'Misses lectura'] = total_read_misses_416TC32

tabla_TC32.at['416.gamess-875B',
              'Miss rate lectura [%]'] = total_read_miss_rate_416TC32

tabla_TC32.at['416.gamess-875B',
              'Misses escritura'] = total_write_misses_416TC32

tabla_TC32.at['416.gamess-875B',
              'Miss rate escritura [%]'] = total_write_miss_rate_416TC32

# **429.mcf-184B**

tabla_TC32.at['429.mcf-184B', 'Total Misses'] = total_misses_429TC32

tabla_TC32.at['429.mcf-184B', 'Miss rate total [%]'] = total_miss_rate_429TC32

tabla_TC32.at['429.mcf-184B', 'Misses lectura'] = total_read_misses_429TC32

tabla_TC32.at['429.mcf-184B',
              'Miss rate lectura [%]'] = total_read_miss_rate_429TC32

tabla_TC32.at['429.mcf-184B',
              'Misses escritura'] = total_write_misses_429TC32

tabla_TC32.at['429.mcf-184B',
              'Miss rate escritura [%]'] = total_write_miss_rate_429TC32

# **433.milc-127B**

tabla_TC32.at['433.milc-127B', 'Total Misses'] = total_misses_433TC32

tabla_TC32.at['433.milc-127B', 'Miss rate total [%]'] = total_miss_rate_433TC32

tabla_TC32.at['433.milc-127B', 'Misses lectura'] = total_read_misses_433TC32

tabla_TC32.at['433.milc-127B',
              'Miss rate lectura [%]'] = total_read_miss_rate_433TC32

tabla_TC32.at['433.milc-127B',
              'Misses escritura'] = total_write_misses_433TC32

tabla_TC32.at['433.milc-127B',
              'Miss rate escritura [%]'] = total_write_miss_rate_433TC32

# **435.gromacs-111B**

tabla_TC32.at['435.gromacs-111B', 'Total Misses'] = total_misses_435TC32

tabla_TC32.at['435.gromacs-111B',
              'Miss rate total [%]'] = total_miss_rate_435TC32

tabla_TC32.at['435.gromacs-111B', 'Misses lectura'] = total_read_misses_435TC32

tabla_TC32.at['435.gromacs-111B',
              'Miss rate lectura [%]'] = total_read_miss_rate_435TC32

tabla_TC32.at['435.gromacs-111B',
              'Misses escritura'] = total_write_misses_435TC32

tabla_TC32.at['435.gromacs-111B',
              'Miss rate escritura [%]'] = total_write_miss_rate_435TC32
# **436.cactusADM-1804B**

tabla_TC32.at['436.cactusADM-1804B', 'Total Misses'] = total_misses_436TC32

tabla_TC32.at['436.cactusADM-1804B',
              'Miss rate total [%]'] = total_miss_rate_436TC32

tabla_TC32.at['436.cactusADM-1804B',
              'Misses lectura'] = total_read_misses_436TC32

tabla_TC32.at['436.cactusADM-1804B',
              'Miss rate lectura [%]'] = total_read_miss_rate_436TC32

tabla_TC32.at['436.cactusADM-1804B',
              'Misses escritura'] = total_write_misses_436TC32

tabla_TC32.at['436.cactusADM-1804B',
              'Miss rate escritura [%]'] = total_write_miss_rate_436TC32

# **437.leslie3d-134B**

tabla_TC32.at['437.leslie3d-134B', 'Total Misses'] = total_misses_437TC32

tabla_TC32.at['437.leslie3d-134B',
              'Miss rate total [%]'] = total_miss_rate_437TC32

tabla_TC32.at['437.leslie3d-134B',
              'Misses lectura'] = total_read_misses_437TC32

tabla_TC32.at['437.leslie3d-134B',
              'Miss rate lectura [%]'] = total_read_miss_rate_437TC32

tabla_TC32.at['437.leslie3d-134B',
              'Misses escritura'] = total_write_misses_437TC32

tabla_TC32.at['437.leslie3d-134B',
              'Miss rate escritura [%]'] = total_write_miss_rate_437TC32

# **444.namd-120B**

tabla_TC32.at['444.namd-120B', 'Total Misses'] = total_misses_444TC32

tabla_TC32.at['444.namd-120B', 'Miss rate total [%]'] = total_miss_rate_444TC32

tabla_TC32.at['444.namd-120B', 'Misses lectura'] = total_read_misses_444TC32

tabla_TC32.at['444.namd-120B',
              'Miss rate lectura [%]'] = total_read_miss_rate_444TC32

tabla_TC32.at['444.namd-120B',
              'Misses escritura'] = total_write_misses_444TC32

tabla_TC32.at['444.namd-120B',
              'Miss rate escritura [%]'] = total_write_miss_rate_444TC32

# **445.gobmk-17B**

tabla_TC32.at['445.gobmk-17B', 'Total Misses'] = total_misses_445TC32

tabla_TC32.at['445.gobmk-17B', 'Miss rate total [%]'] = total_miss_rate_445TC32

tabla_TC32.at['445.gobmk-17B', 'Misses lectura'] = total_read_misses_445TC32

tabla_TC32.at['445.gobmk-17B',
              'Miss rate lectura [%]'] = total_read_miss_rate_445TC32

tabla_TC32.at['445.gobmk-17B',
              'Misses escritura'] = total_write_misses_445TC32

tabla_TC32.at['445.gobmk-17B',
              'Miss rate escritura [%]'] = total_write_miss_rate_445TC32

# **450.soplex-247B**

tabla_TC32.at['450.soplex-247B', 'Total Misses'] = total_misses_450TC32

tabla_TC32.at['450.soplex-247B',
              'Miss rate total [%]'] = total_miss_rate_450TC32

tabla_TC32.at['450.soplex-247B', 'Misses lectura'] = total_read_misses_450TC32

tabla_TC32.at['450.soplex-247B',
              'Miss rate lectura [%]'] = total_read_miss_rate_450TC32

tabla_TC32.at['450.soplex-247B',
              'Misses escritura'] = total_write_misses_450TC32

tabla_TC32.at['450.soplex-247B',
              'Miss rate escritura [%]'] = total_write_miss_rate_450TC32

# **453.povray-887B**

tabla_TC32.at['453.povray-887B', 'Total Misses'] = total_misses_453TC32

tabla_TC32.at['453.povray-887B',
              'Miss rate total [%]'] = total_miss_rate_453TC32

tabla_TC32.at['453.povray-887B', 'Misses lectura'] = total_read_misses_453TC32

tabla_TC32.at['453.povray-887B',
              'Miss rate lectura [%]'] = total_read_miss_rate_453TC32

tabla_TC32.at['453.povray-887B',
              'Misses escritura'] = total_write_misses_453TC32

tabla_TC32.at['453.povray-887B',
              'Miss rate escritura [%]'] = total_write_miss_rate_453TC32

# **454.calculix-104B**

tabla_TC32.at['454.calculix-104B', 'Total Misses'] = total_misses_454TC32

tabla_TC32.at['454.calculix-104B',
              'Miss rate total [%]'] = total_miss_rate_454TC32

tabla_TC32.at['454.calculix-104B',
              'Misses lectura'] = total_read_misses_454TC32

tabla_TC32.at['454.calculix-104B',
              'Miss rate lectura [%]'] = total_read_miss_rate_454TC32

tabla_TC32.at['454.calculix-104B',
              'Misses escritura'] = total_write_misses_454TC32

tabla_TC32.at['454.calculix-104B',
              'Miss rate escritura [%]'] = total_write_miss_rate_454TC32

# **456.hmmer-191B**

tabla_TC32.at['456.hmmer-191B', 'Total Misses'] = total_misses_456TC32

tabla_TC32.at['456.hmmer-191B',
              'Miss rate total [%]'] = total_miss_rate_456TC32

tabla_TC32.at['456.hmmer-191B', 'Misses lectura'] = total_read_misses_456TC32

tabla_TC32.at['456.hmmer-191B',
              'Miss rate lectura [%]'] = total_read_miss_rate_456TC32

tabla_TC32.at['456.hmmer-191B',
              'Misses escritura'] = total_write_misses_456TC32

tabla_TC32.at['456.hmmer-191B',
              'Miss rate escritura [%]'] = total_write_miss_rate_456TC32

# **458.sjeng-1088B**

tabla_TC32.at['458.sjeng-1088B', 'Total Misses'] = total_misses_458TC32

tabla_TC32.at['458.sjeng-1088B',
              'Miss rate total [%]'] = total_miss_rate_458TC32

tabla_TC32.at['458.sjeng-1088B', 'Misses lectura'] = total_read_misses_458TC32

tabla_TC32.at['458.sjeng-1088B',
              'Miss rate lectura [%]'] = total_read_miss_rate_458TC32

tabla_TC32.at['458.sjeng-1088B',
              'Misses escritura'] = total_write_misses_458TC32

tabla_TC32.at['458.sjeng-1088B',
              'Miss rate escritura [%]'] = total_write_miss_rate_458TC32

# **459.GemsFDTD-1169B**

tabla_TC32.at['459.GemsFDTD-1169B', 'Total Misses'] = total_misses_459TC32

tabla_TC32.at['459.GemsFDTD-1169B',
              'Miss rate total [%]'] = total_miss_rate_459TC32

tabla_TC32.at['459.GemsFDTD-1169B',
              'Misses lectura'] = total_read_misses_459TC32

tabla_TC32.at['459.GemsFDTD-1169B',
              'Miss rate lectura [%]'] = total_read_miss_rate_459TC32

tabla_TC32.at['459.GemsFDTD-1169B',
              'Misses escritura'] = total_write_misses_459TC32

tabla_TC32.at['459.GemsFDTD-1169B',
              'Miss rate escritura [%]'] = total_write_miss_rate_459TC32

# **462.libquantum-1343B**

tabla_TC32.at['462.libquantum-1343B', 'Total Misses'] = total_misses_462TC32

tabla_TC32.at['462.libquantum-1343B',
              'Miss rate total [%]'] = total_miss_rate_462TC32

tabla_TC32.at['462.libquantum-1343B',
              'Misses lectura'] = total_read_misses_462TC32

tabla_TC32.at['462.libquantum-1343B',
              'Miss rate lectura [%]'] = total_read_miss_rate_462TC32

tabla_TC32.at['462.libquantum-1343B',
              'Misses escritura'] = total_write_misses_462TC32

tabla_TC32.at['462.libquantum-1343B',
              'Miss rate escritura [%]'] = total_write_miss_rate_462TC32

# **464.h264ref-30B**

tabla_TC32.at['464.h264ref-30B', 'Total Misses'] = total_misses_464TC32

tabla_TC32.at['464.h264ref-30B',
              'Miss rate total [%]'] = total_miss_rate_464TC32

tabla_TC32.at['464.h264ref-30B', 'Misses lectura'] = total_read_misses_464TC32

tabla_TC32.at['464.h264ref-30B',
              'Miss rate lectura [%]'] = total_read_miss_rate_464TC32

tabla_TC32.at['464.h264ref-30B',
              'Misses escritura'] = total_write_misses_464TC32

tabla_TC32.at['464.h264ref-30B',
              'Miss rate escritura [%]'] = total_write_miss_rate_464TC32

# **465.tonto-1769B**

tabla_TC32.at['465.tonto-1769B', 'Total Misses'] = total_misses_465TC32

tabla_TC32.at['465.tonto-1769B',
              'Miss rate total [%]'] = total_miss_rate_465TC32

tabla_TC32.at['465.tonto-1769B', 'Misses lectura'] = total_read_misses_465TC32

tabla_TC32.at['465.tonto-1769B',
              'Miss rate lectura [%]'] = total_read_miss_rate_465TC32

tabla_TC32.at['465.tonto-1769B',
              'Misses escritura'] = total_write_misses_465TC32
tabla_TC32.at['465.tonto-1769B',
              'Miss rate escritura [%]'] = total_write_miss_rate_465TC32

# **470.lbm-1274B**

tabla_TC32.at['470.lbm-1274B', 'Total Misses'] = total_misses_470TC32

tabla_TC32.at['470.lbm-1274B', 'Miss rate total [%]'] = total_miss_rate_470TC32

tabla_TC32.at['470.lbm-1274B', 'Misses lectura'] = total_read_misses_470TC32

tabla_TC32.at['470.lbm-1274B',
              'Miss rate lectura [%]'] = total_read_miss_rate_470TC32

tabla_TC32.at['470.lbm-1274B',
              'Misses escritura'] = total_write_misses_470TC32

tabla_TC32.at['470.lbm-1274B',
              'Miss rate escritura [%]'] = total_write_miss_rate_470TC32

# **471.omnetpp-188B**

tabla_TC32.at['471.omnetpp-188B', 'Total Misses'] = total_misses_471TC32

tabla_TC32.at['471.omnetpp-188B',
              'Miss rate total [%]'] = total_miss_rate_471TC32

tabla_TC32.at['471.omnetpp-188B', 'Misses lectura'] = total_read_misses_471TC32

tabla_TC32.at['471.omnetpp-188B',
              'Miss rate lectura [%]'] = total_read_miss_rate_471TC32

tabla_TC32.at['471.omnetpp-188B',
              'Misses escritura'] = total_write_misses_471TC32

tabla_TC32.at['471.omnetpp-188B',
              'Miss rate escritura [%]'] = total_write_miss_rate_471TC32

# **473.astar-153B**

tabla_TC32.at['473.astar-153B', 'Total Misses'] = total_misses_473TC32

tabla_TC32.at['473.astar-153B',
              'Miss rate total [%]'] = total_miss_rate_473TC32

tabla_TC32.at['473.astar-153B', 'Misses lectura'] = total_read_misses_473TC32

tabla_TC32.at['473.astar-153B',
              'Miss rate lectura [%]'] = total_read_miss_rate_473TC32

tabla_TC32.at['473.astar-153B',
              'Misses escritura'] = total_write_misses_473TC32

tabla_TC32.at['473.astar-153B',
              'Miss rate escritura [%]'] = total_write_miss_rate_473TC32

# **481.wrf-1170B**

tabla_TC32.at['481.wrf-1170B', 'Total Misses'] = total_misses_481TC32

tabla_TC32.at['481.wrf-1170B', 'Miss rate total [%]'] = total_miss_rate_481TC32

tabla_TC32.at['481.wrf-1170B', 'Misses lectura'] = total_read_misses_481TC32

tabla_TC32.at['481.wrf-1170B',
              'Miss rate lectura [%]'] = total_read_miss_rate_481TC32

tabla_TC32.at['481.wrf-1170B',
              'Misses escritura'] = total_write_misses_481TC32

tabla_TC32.at['481.wrf-1170B',
              'Miss rate escritura [%]'] = total_write_miss_rate_481TC32

# **482.sphinx3-1100B**

tabla_TC32.at['482.sphinx3-1100B', 'Total Misses'] = total_misses_482TC32

tabla_TC32.at['482.sphinx3-1100B',
              'Miss rate total [%]'] = total_miss_rate_482TC32

tabla_TC32.at['482.sphinx3-1100B',
              'Misses lectura'] = total_read_misses_482TC32

tabla_TC32.at['482.sphinx3-1100B',
              'Miss rate lectura [%]'] = total_read_miss_rate_482TC32

tabla_TC32.at['482.sphinx3-1100B',
              'Misses escritura'] = total_write_misses_482TC32

tabla_TC32.at['482.sphinx3-1100B',
              'Miss rate escritura [%]'] = total_write_miss_rate_482TC32

# **483.xalancbmk-127B**

tabla_TC32.at['483.xalancbmk-127B', 'Total Misses'] = total_misses_483TC32

tabla_TC32.at['483.xalancbmk-127B',
              'Miss rate total [%]'] = total_miss_rate_483TC32

tabla_TC32.at['483.xalancbmk-127B',
              'Misses lectura'] = total_read_misses_483TC32

tabla_TC32.at['483.xalancbmk-127B',
              'Miss rate lectura [%]'] = total_read_miss_rate_483TC32

tabla_TC32.at['483.xalancbmk-127B',
              'Misses escritura'] = total_write_misses_483TC32

tabla_TC32.at['483.xalancbmk-127B',
              'Miss rate escritura [%]'] = total_write_miss_rate_483TC32

print(">>>>>All TC32 data has been uploaded successfully")

###########################################
# Extractor para experimento con tamaño 64#
###########################################

# Creación de tablas para adjuntar valores
# Una tabla por tamaño
tabla_TC64 = pd.DataFrame(index=[
    '400.perlbench-41B', '401.bzip2-226B', '403.gcc-16B', '410.bwaves-1963B', '416.gamess-875B', '429.mcf-184B', '433.milc-127B',
    '435.gromacs-111B', '436.cactusADM-1804B', '437.leslie3d-134B', '444.namd-120B', '445.gobmk-17B',
    '450.soplex-247B', '453.povray-887B', '454.calculix-104B', '456.hmmer-191B', '458.sjeng-1088B', '459.GemsFDTD-1169B',
    '462.libquantum-1343B', '464.h264ref-30B', '465.tonto-1769B', '470.lbm-1274B', '471.omnetpp-188B', '473.astar-153B', '481.wrf-1170B',
    '482.sphinx3-1100B', '483.xalancbmk-127B'], columns=[
    'App', 'Total Misses', 'Miss rate total [%]', 'Misses lectura', 'Miss rate lectura [%]', 'Misses escritura', 'Miss rate escritura [%]'])
tabla_TC64['App'] = tabla_TC64.index

# Files paths
filename_82 = "RESULTS_TC/400TC64.txt"
filename_83 = "RESULTS_TC/401TC64.txt"
filename_84 = "RESULTS_TC/403TC64.txt"
filename_85 = "RESULTS_TC/410TC64.txt"
filename_86 = "RESULTS_TC/416TC64.txt"
filename_87 = "RESULTS_TC/429TC64.txt"
filename_88 = "RESULTS_TC/433TC64.txt"
filename_89 = "RESULTS_TC/435TC64.txt"
filename_90 = "RESULTS_TC/436TC64.txt"
filename_91 = "RESULTS_TC/437TC64.txt"
filename_92 = "RESULTS_TC/444TC64.txt"
filename_93 = "RESULTS_TC/445TC64.txt"
filename_94 = "RESULTS_TC/450TC64.txt"
filename_95 = "RESULTS_TC/453TC64.txt"
filename_96 = "RESULTS_TC/454TC64.txt"
filename_97 = "RESULTS_TC/456TC64.txt"
filename_98 = "RESULTS_TC/458TC64.txt"
filename_99 = "RESULTS_TC/459TC64.txt"
filename_100 = "RESULTS_TC/462TC64.txt"
filename_101 = "RESULTS_TC/464TC64.txt"
filename_102 = "RESULTS_TC/465TC64.txt"
filename_103 = "RESULTS_TC/470TC64.txt"
filename_104 = "RESULTS_TC/471TC64.txt"
filename_105 = "RESULTS_TC/473TC64.txt"
filename_106 = "RESULTS_TC/481TC64.txt"
filename_107 = "RESULTS_TC/482TC64.txt"
filename_108 = "RESULTS_TC/483TC64.txt"

# Content file extracter
with open(filename_82, 'r') as file:
    content_400TC64 = file.read()
with open(filename_83, 'r') as file:
    content_401TC64 = file.read()
with open(filename_84, 'r') as file:
    content_403TC64 = file.read()
with open(filename_85, 'r') as file:
    content_410TC64 = file.read()
with open(filename_86, 'r') as file:
    content_416TC64 = file.read()
with open(filename_87, 'r') as file:
    content_429TC64 = file.read()
with open(filename_88, 'r') as file:
    content_433TC64 = file.read()
with open(filename_89, 'r') as file:
    content_435TC64 = file.read()
with open(filename_90, 'r') as file:
    content_436TC64 = file.read()
with open(filename_91, 'r') as file:
    content_437TC64 = file.read()
with open(filename_92, 'r') as file:
    content_444TC64 = file.read()
with open(filename_93, 'r') as file:
    content_445TC64 = file.read()
with open(filename_94, 'r') as file:
    content_450TC64 = file.read()
with open(filename_95, 'r') as file:
    content_453TC64 = file.read()
with open(filename_96, 'r') as file:
    content_454TC64 = file.read()
with open(filename_97, 'r') as file:
    content_456TC64 = file.read()
with open(filename_98, 'r') as file:
    content_458TC64 = file.read()
with open(filename_99, 'r') as file:
    content_459TC64 = file.read()
with open(filename_100, 'r') as file:
    content_462TC64 = file.read()
with open(filename_101, 'r') as file:
    content_464TC64 = file.read()
with open(filename_102, 'r') as file:
    content_465TC64 = file.read()
with open(filename_103, 'r') as file:
    content_470TC64 = file.read()
with open(filename_104, 'r') as file:
    content_471TC64 = file.read()
with open(filename_105, 'r') as file:
    content_473TC64 = file.read()
with open(filename_106, 'r') as file:
    content_481TC64 = file.read()
with open(filename_107, 'r') as file:
    content_482TC64 = file.read()
with open(filename_108, 'r') as file:
    content_483TC64 = file.read()

# Variables según aplicación

# 400.pearlbench-41B
total_misses_400TC64 = re.search(
    r"Total_misses (\d+)", content_400TC64).group(1)
total_miss_rate_400TC64 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_400TC64).group(1)
total_read_misses_400TC64 = re.search(
    r"Total_read_misses (\d+)", content_400TC64).group(1)
total_read_miss_rate_400TC64 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_400TC64).group(1)
total_write_misses_400TC64 = re.search(
    r"Total_write_misses (\d+)", content_400TC64).group(1)
total_write_miss_rate_400TC64 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_400TC64).group(1)
print(">>>>>All TC64 400.pearlbench-41B variables where obtained successfully")

# 401.bzip2-226B
total_misses_401TC64 = re.search(
    r"Total_misses (\d+)", content_401TC64).group(1)
total_miss_rate_401TC64 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_401TC64).group(1)
total_read_misses_401TC64 = re.search(
    r"Total_read_misses (\d+)", content_401TC64).group(1)
total_read_miss_rate_401TC64 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_401TC64).group(1)
total_write_misses_401TC64 = re.search(
    r"Total_write_misses (\d+)", content_401TC64).group(1)
total_write_miss_rate_401TC64 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_401TC64).group(1)
print(">>>>>All TC64 401.bzip2-226B variables where obtained successfully")

# 403.gcc-16B
total_misses_403TC64 = re.search(
    r"Total_misses (\d+)", content_403TC64).group(1)
total_miss_rate_403TC64 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_403TC64).group(1)
total_read_misses_403TC64 = re.search(
    r"Total_read_misses (\d+)", content_403TC64).group(1)
total_read_miss_rate_403TC64 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_403TC64).group(1)
total_write_misses_403TC64 = re.search(
    r"Total_write_misses (\d+)", content_403TC64).group(1)
total_write_miss_rate_403TC64 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_403TC64).group(1)
print(">>>>>All TC64 403.gcc-16B variables where obtained successfully")

# 410.bwaves-1963B
total_misses_410TC64 = re.search(
    r"Total_misses (\d+)", content_410TC64).group(1)
total_miss_rate_410TC64 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_410TC64).group(1)
total_read_misses_410TC64 = re.search(
    r"Total_read_misses (\d+)", content_410TC64).group(1)
total_read_miss_rate_410TC64 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_410TC64).group(1)
total_write_misses_410TC64 = re.search(
    r"Total_write_misses (\d+)", content_410TC64).group(1)
total_write_miss_rate_410TC64 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_410TC64).group(1)
print(">>>>>All TC64 410.bwaves-1963B variables where obtained successfully")

# 416.gamess-875B
total_misses_416TC64 = re.search(
    r"Total_misses (\d+)", content_416TC64).group(1)
total_miss_rate_416TC64 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_416TC64).group(1)
total_read_misses_416TC64 = re.search(
    r"Total_read_misses (\d+)", content_416TC64).group(1)
total_read_miss_rate_416TC64 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_416TC64).group(1)
total_write_misses_416TC64 = re.search(
    r"Total_write_misses (\d+)", content_416TC64).group(1)
total_write_miss_rate_416TC64 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_416TC64).group(1)
print(">>>>>All TC64 416.gamess-875B variables where obtained successfully")

# 429.mcf-184B
total_misses_429TC64 = re.search(
    r"Total_misses (\d+)", content_429TC64).group(1)
total_miss_rate_429TC64 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_429TC64).group(1)
total_read_misses_429TC64 = re.search(
    r"Total_read_misses (\d+)", content_429TC64).group(1)
total_read_miss_rate_429TC64 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_429TC64).group(1)
total_write_misses_429TC64 = re.search(
    r"Total_write_misses (\d+)", content_429TC64).group(1)
total_write_miss_rate_429TC64 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_429TC64).group(1)
print(">>>>>All TC64 429.mcf-184B variables where obtained successfully")

# 433.milc-127B
total_misses_433TC64 = re.search(
    r"Total_misses (\d+)", content_433TC64).group(1)
total_miss_rate_433TC64 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_433TC64).group(1)
total_read_misses_433TC64 = re.search(
    r"Total_read_misses (\d+)", content_433TC64).group(1)
total_read_miss_rate_433TC64 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_433TC64).group(1)
total_write_misses_433TC64 = re.search(
    r"Total_write_misses (\d+)", content_433TC64).group(1)
total_write_miss_rate_433TC64 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_433TC64).group(1)
print(">>>>>All TC64 433.milc-127B variables where obtained successfully")

# 435.gromacs-111B
total_misses_435TC64 = re.search(
    r"Total_misses (\d+)", content_435TC64).group(1)
total_miss_rate_435TC64 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_435TC64).group(1)
total_read_misses_435TC64 = re.search(
    r"Total_read_misses (\d+)", content_435TC64).group(1)
total_read_miss_rate_435TC64 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_435TC64).group(1)
total_write_misses_435TC64 = re.search(
    r"Total_write_misses (\d+)", content_435TC64).group(1)
total_write_miss_rate_435TC64 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_435TC64).group(1)
print(">>>>>All TC64 435.gromacs-111B variables where obtained successfully")

# 436.cactusADM-1804B
total_misses_436TC64 = re.search(
    r"Total_misses (\d+)", content_436TC64).group(1)
total_miss_rate_436TC64 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_436TC64).group(1)
total_read_misses_436TC64 = re.search(
    r"Total_read_misses (\d+)", content_436TC64).group(1)
total_read_miss_rate_436TC64 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_436TC64).group(1)
total_write_misses_436TC64 = re.search(
    r"Total_write_misses (\d+)", content_436TC64).group(1)
total_write_miss_rate_436TC64 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_436TC64).group(1)
print(">>>>>All TC64 436.cactusADM-1804B variables where obtained successfully")

# 437.leslie3d-134B
total_misses_437TC64 = re.search(
    r"Total_misses (\d+)", content_437TC64).group(1)
total_miss_rate_437TC64 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_437TC64).group(1)
total_read_misses_437TC64 = re.search(
    r"Total_read_misses (\d+)", content_437TC64).group(1)
total_read_miss_rate_437TC64 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_437TC64).group(1)
total_write_misses_437TC64 = re.search(
    r"Total_write_misses (\d+)", content_437TC64).group(1)
total_write_miss_rate_437TC64 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_437TC64).group(1)
print(">>>>>All TC64 437.leslie3d-134B variables where obtained successfully")

# 444.namd-120B
total_misses_444TC64 = re.search(
    r"Total_misses (\d+)", content_444TC64).group(1)
total_miss_rate_444TC64 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_444TC64).group(1)
total_read_misses_444TC64 = re.search(
    r"Total_read_misses (\d+)", content_444TC64).group(1)
total_read_miss_rate_444TC64 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_444TC64).group(1)
total_write_misses_444TC64 = re.search(
    r"Total_write_misses (\d+)", content_444TC64).group(1)
total_write_miss_rate_444TC64 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_444TC64).group(1)
print(">>>>>All TC64 444.namd-120B variables where obtained successfully")

# 445.gobmk-17B
total_misses_445TC64 = re.search(
    r"Total_misses (\d+)", content_445TC64).group(1)
total_miss_rate_445TC64 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_445TC64).group(1)
total_read_misses_445TC64 = re.search(
    r"Total_read_misses (\d+)", content_445TC64).group(1)
total_read_miss_rate_445TC64 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_445TC64).group(1)
total_write_misses_445TC64 = re.search(
    r"Total_write_misses (\d+)", content_445TC64).group(1)
total_write_miss_rate_445TC64 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_445TC64).group(1)
print(">>>>>All TC64 445.gobmk-17B variables where obtained successfully")

# 450.soplex-247B
total_misses_450TC64 = re.search(
    r"Total_misses (\d+)", content_450TC64).group(1)
total_miss_rate_450TC64 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_450TC64).group(1)
total_read_misses_450TC64 = re.search(
    r"Total_read_misses (\d+)", content_450TC64).group(1)
total_read_miss_rate_450TC64 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_450TC64).group(1)
total_write_misses_450TC64 = re.search(
    r"Total_write_misses (\d+)", content_450TC64).group(1)
total_write_miss_rate_450TC64 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_450TC64).group(1)
print(">>>>>All TC64 450.soplex-247B variables where obtained successfully")

# 453.povray-887B
total_misses_453TC64 = re.search(
    r"Total_misses (\d+)", content_453TC64).group(1)
total_miss_rate_453TC64 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_453TC64).group(1)
total_read_misses_453TC64 = re.search(
    r"Total_read_misses (\d+)", content_453TC64).group(1)
total_read_miss_rate_453TC64 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_453TC64).group(1)
total_write_misses_453TC64 = re.search(
    r"Total_write_misses (\d+)", content_453TC64).group(1)
total_write_miss_rate_453TC64 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_453TC64).group(1)
print(">>>>>All TC64 453.povray-887B variables where obtained successfully")

# 454.calculix-104B
total_misses_454TC64 = re.search(
    r"Total_misses (\d+)", content_454TC64).group(1)
total_miss_rate_454TC64 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_454TC64).group(1)
total_read_misses_454TC64 = re.search(
    r"Total_read_misses (\d+)", content_454TC64).group(1)
total_read_miss_rate_454TC64 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_454TC64).group(1)
total_write_misses_454TC64 = re.search(
    r"Total_write_misses (\d+)", content_454TC64).group(1)
total_write_miss_rate_454TC64 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_454TC64).group(1)
print(">>>>>All TC64 454.calculix-104B variables where obtained successfully")

# 456.hmmer-191B
total_misses_456TC64 = re.search(
    r"Total_misses (\d+)", content_456TC64).group(1)
total_miss_rate_456TC64 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_456TC64).group(1)
total_read_misses_456TC64 = re.search(
    r"Total_read_misses (\d+)", content_456TC64).group(1)
total_read_miss_rate_456TC64 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_456TC64).group(1)
total_write_misses_456TC64 = re.search(
    r"Total_write_misses (\d+)", content_456TC64).group(1)
total_write_miss_rate_456TC64 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_456TC64).group(1)
print(">>>>>All TC64 456.hmmer-191B variables where obtained successfully")

# 458.sjeng-1088B
total_misses_458TC64 = re.search(
    r"Total_misses (\d+)", content_458TC64).group(1)
total_miss_rate_458TC64 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_458TC64).group(1)
total_read_misses_458TC64 = re.search(
    r"Total_read_misses (\d+)", content_458TC64).group(1)
total_read_miss_rate_458TC64 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_458TC64).group(1)
total_write_misses_458TC64 = re.search(
    r"Total_write_misses (\d+)", content_458TC64).group(1)
total_write_miss_rate_458TC64 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_458TC64).group(1)
print(">>>>>All TC64 458.sjeng-1088B variables where obtained successfully")

# 459.GemsFDTD-1169B
total_misses_459TC64 = re.search(
    r"Total_misses (\d+)", content_459TC64).group(1)
total_miss_rate_459TC64 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_459TC64).group(1)
total_read_misses_459TC64 = re.search(
    r"Total_read_misses (\d+)", content_459TC64).group(1)
total_read_miss_rate_459TC64 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_459TC64).group(1)
total_write_misses_459TC64 = re.search(
    r"Total_write_misses (\d+)", content_459TC64).group(1)
total_write_miss_rate_459TC64 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_459TC64).group(1)
print(">>>>>All TC64 459.GemsFDTD-1169B variables where obtained successfully")

# 462.libquantum-1343B
total_misses_462TC64 = re.search(
    r"Total_misses (\d+)", content_462TC64).group(1)
total_miss_rate_462TC64 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_462TC64).group(1)
total_read_misses_462TC64 = re.search(
    r"Total_read_misses (\d+)", content_462TC64).group(1)
total_read_miss_rate_462TC64 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_462TC64).group(1)
total_write_misses_462TC64 = re.search(
    r"Total_write_misses (\d+)", content_462TC64).group(1)
total_write_miss_rate_462TC64 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_462TC64).group(1)
print(">>>>>All TC64 462.libquantum-1343B variables where obtained successfully")

# 464.h264ref-30B
total_misses_464TC64 = re.search(
    r"Total_misses (\d+)", content_464TC64).group(1)
total_miss_rate_464TC64 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_464TC64).group(1)
total_read_misses_464TC64 = re.search(
    r"Total_read_misses (\d+)", content_464TC64).group(1)
total_read_miss_rate_464TC64 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_464TC64).group(1)
total_write_misses_464TC64 = re.search(
    r"Total_write_misses (\d+)", content_464TC64).group(1)
total_write_miss_rate_464TC64 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_464TC64).group(1)
print(">>>>>All TC64 464.h264ref-30B variables where obtained successfully")

# 465.tonto-1769B
total_misses_465TC64 = re.search(
    r"Total_misses (\d+)", content_465TC64).group(1)
total_miss_rate_465TC64 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_465TC64).group(1)
total_read_misses_465TC64 = re.search(
    r"Total_read_misses (\d+)", content_465TC64).group(1)
total_read_miss_rate_465TC64 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_465TC64).group(1)
total_write_misses_465TC64 = re.search(
    r"Total_write_misses (\d+)", content_465TC64).group(1)
total_write_miss_rate_465TC64 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_465TC64).group(1)
print(">>>>>All TC64 465.tonto-1769B variables where obtained successfully")

# 470.lbm-1274B
total_misses_470TC64 = re.search(
    r"Total_misses (\d+)", content_470TC64).group(1)
total_miss_rate_470TC64 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_470TC64).group(1)
total_read_misses_470TC64 = re.search(
    r"Total_read_misses (\d+)", content_470TC64).group(1)
total_read_miss_rate_470TC64 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_470TC64).group(1)
total_write_misses_470TC64 = re.search(
    r"Total_write_misses (\d+)", content_470TC64).group(1)
total_write_miss_rate_470TC64 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_470TC64).group(1)
print(">>>>>All TC64 470.lbm-1274B variables where obtained successfully")

# 471.omnetpp-188B
total_misses_471TC64 = re.search(
    r"Total_misses (\d+)", content_471TC64).group(1)
total_miss_rate_471TC64 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_471TC64).group(1)
total_read_misses_471TC64 = re.search(
    r"Total_read_misses (\d+)", content_471TC64).group(1)
total_read_miss_rate_471TC64 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_471TC64).group(1)
total_write_misses_471TC64 = re.search(
    r"Total_write_misses (\d+)", content_471TC64).group(1)
total_write_miss_rate_471TC64 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_471TC64).group(1)
print(">>>>>All TC64 471.omnetpp-188B variables where obtained successfully")

# 473.astar-153B
total_misses_473TC64 = re.search(
    r"Total_misses (\d+)", content_473TC64).group(1)
total_miss_rate_473TC64 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_473TC64).group(1)
total_read_misses_473TC64 = re.search(
    r"Total_read_misses (\d+)", content_473TC64).group(1)
total_read_miss_rate_473TC64 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_473TC64).group(1)
total_write_misses_473TC64 = re.search(
    r"Total_write_misses (\d+)", content_473TC64).group(1)
total_write_miss_rate_473TC64 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_473TC64).group(1)
print(">>>>>All TC64 473.astar-153B variables where obtained successfully")

# 481.wrf-1170B
total_misses_481TC64 = re.search(
    r"Total_misses (\d+)", content_481TC64).group(1)
total_miss_rate_481TC64 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_481TC64).group(1)
total_read_misses_481TC64 = re.search(
    r"Total_read_misses (\d+)", content_481TC64).group(1)
total_read_miss_rate_481TC64 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_481TC64).group(1)
total_write_misses_481TC64 = re.search(
    r"Total_write_misses (\d+)", content_481TC64).group(1)
total_write_miss_rate_481TC64 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_481TC64).group(1)
print(">>>>>All TC64 481.wrf-1170B variables where obtained successfully")

# 482.sphinx3-1100B
total_misses_482TC64 = re.search(
    r"Total_misses (\d+)", content_482TC64).group(1)
total_miss_rate_482TC64 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_482TC64).group(1)
total_read_misses_482TC64 = re.search(
    r"Total_read_misses (\d+)", content_482TC64).group(1)
total_read_miss_rate_482TC64 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_482TC64).group(1)
total_write_misses_482TC64 = re.search(
    r"Total_write_misses (\d+)", content_482TC64).group(1)
total_write_miss_rate_482TC64 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_482TC64).group(1)
print(">>>>>All TC64 482.sphinx3-1100B variables where obtained successfully")

# 483.xalancbmk-127B
total_misses_483TC64 = re.search(
    r"Total_misses (\d+)", content_483TC64).group(1)
total_miss_rate_483TC64 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_483TC64).group(1)
total_read_misses_483TC64 = re.search(
    r"Total_read_misses (\d+)", content_483TC64).group(1)
total_read_miss_rate_483TC64 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_483TC64).group(1)
total_write_misses_483TC64 = re.search(
    r"Total_write_misses (\d+)", content_483TC64).group(1)
total_write_miss_rate_483TC64 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_483TC64).group(1)
print(">>>>>All TC64 483.xalancbmk-127B variables where obtained successfully")

#############################
# Adjunta datos a dataframe #
#############################

# **400.perlbench-41B**

tabla_TC64.at['400.perlbench-41B', 'Total Misses'] = total_misses_400TC64

tabla_TC64.at['400.perlbench-41B',
              'Miss rate total [%]'] = total_miss_rate_400TC64

tabla_TC64.at['400.perlbench-41B',
              'Misses lectura'] = total_read_misses_400TC64

tabla_TC64.at['400.perlbench-41B',
              'Miss rate lectura [%]'] = total_read_miss_rate_400TC64

tabla_TC64.at['400.perlbench-41B',
              'Misses escritura'] = total_write_misses_400TC64

tabla_TC64.at['400.perlbench-41B',
              'Miss rate escritura [%]'] = total_write_miss_rate_400TC64

# **401.bzip2-226B**

tabla_TC64.at['401.bzip2-226B', 'Total Misses'] = total_misses_401TC64

tabla_TC64.at['401.bzip2-226B',
              'Miss rate total [%]'] = total_miss_rate_401TC64

tabla_TC64.at['401.bzip2-226B', 'Misses lectura'] = total_read_misses_401TC64

tabla_TC64.at['401.bzip2-226B',
              'Miss rate lectura [%]'] = total_read_miss_rate_401TC64

tabla_TC64.at['401.bzip2-226B',
              'Misses escritura'] = total_write_misses_401TC64

tabla_TC64.at['401.bzip2-226B',
              'Miss rate escritura [%]'] = total_write_miss_rate_401TC64

# **403.gcc-16B**

tabla_TC64.at['403.gcc-16B', 'Total Misses'] = total_misses_403TC64

tabla_TC64.at['403.gcc-16B', 'Miss rate total [%]'] = total_miss_rate_403TC64

tabla_TC64.at['403.gcc-16B', 'Misses lectura'] = total_read_misses_403TC64

tabla_TC64.at['403.gcc-16B',
              'Miss rate lectura [%]'] = total_read_miss_rate_403TC64

tabla_TC64.at['403.gcc-16B',
              'Misses escritura'] = total_write_misses_403TC64

tabla_TC64.at['403.gcc-16B',
              'Miss rate escritura [%]'] = total_write_miss_rate_403TC64

# **410.bwaves-1963B**

tabla_TC64.at['410.bwaves-1963B', 'Total Misses'] = total_misses_410TC64

tabla_TC64.at['410.bwaves-1963B',
              'Miss rate total [%]'] = total_miss_rate_410TC64

tabla_TC64.at['410.bwaves-1963B', 'Misses lectura'] = total_read_misses_410TC64

tabla_TC64.at['410.bwaves-1963B',
              'Miss rate lectura [%]'] = total_read_miss_rate_410TC64

tabla_TC64.at['410.bwaves-1963B',
              'Misses escritura'] = total_write_misses_410TC64

tabla_TC64.at['410.bwaves-1963B',
              'Miss rate escritura [%]'] = total_write_miss_rate_410TC64

# **416.gamess-875B**

tabla_TC64.at['416.gamess-875B', 'Total Misses'] = total_misses_416TC64

tabla_TC64.at['416.gamess-875B',
              'Miss rate total [%]'] = total_miss_rate_416TC64

tabla_TC64.at['416.gamess-875B', 'Misses lectura'] = total_read_misses_416TC64

tabla_TC64.at['416.gamess-875B',
              'Miss rate lectura [%]'] = total_read_miss_rate_416TC64

tabla_TC64.at['416.gamess-875B',
              'Misses escritura'] = total_write_misses_416TC64

tabla_TC64.at['416.gamess-875B',
              'Miss rate escritura [%]'] = total_write_miss_rate_416TC64

# **429.mcf-184B**

tabla_TC64.at['429.mcf-184B', 'Total Misses'] = total_misses_429TC64

tabla_TC64.at['429.mcf-184B', 'Miss rate total [%]'] = total_miss_rate_429TC64

tabla_TC64.at['429.mcf-184B', 'Misses lectura'] = total_read_misses_429TC64

tabla_TC64.at['429.mcf-184B',
              'Miss rate lectura [%]'] = total_read_miss_rate_429TC64

tabla_TC64.at['429.mcf-184B',
              'Misses escritura'] = total_write_misses_429TC64

tabla_TC64.at['429.mcf-184B',
              'Miss rate escritura [%]'] = total_write_miss_rate_429TC64

# **433.milc-127B**

tabla_TC64.at['433.milc-127B', 'Total Misses'] = total_misses_433TC64

tabla_TC64.at['433.milc-127B', 'Miss rate total [%]'] = total_miss_rate_433TC64

tabla_TC64.at['433.milc-127B', 'Misses lectura'] = total_read_misses_433TC64

tabla_TC64.at['433.milc-127B',
              'Miss rate lectura [%]'] = total_read_miss_rate_433TC64

tabla_TC64.at['433.milc-127B',
              'Misses escritura'] = total_write_misses_433TC64

tabla_TC64.at['433.milc-127B',
              'Miss rate escritura [%]'] = total_write_miss_rate_433TC64

# **435.gromacs-111B**

tabla_TC64.at['435.gromacs-111B', 'Total Misses'] = total_misses_435TC64

tabla_TC64.at['435.gromacs-111B',
              'Miss rate total [%]'] = total_miss_rate_435TC64

tabla_TC64.at['435.gromacs-111B', 'Misses lectura'] = total_read_misses_435TC64

tabla_TC64.at['435.gromacs-111B',
              'Miss rate lectura [%]'] = total_read_miss_rate_435TC64

tabla_TC64.at['435.gromacs-111B',
              'Misses escritura'] = total_write_misses_435TC64

tabla_TC64.at['435.gromacs-111B',
              'Miss rate escritura [%]'] = total_write_miss_rate_435TC64
# **436.cactusADM-1804B**

tabla_TC64.at['436.cactusADM-1804B', 'Total Misses'] = total_misses_436TC64

tabla_TC64.at['436.cactusADM-1804B',
              'Miss rate total [%]'] = total_miss_rate_436TC64

tabla_TC64.at['436.cactusADM-1804B',
              'Misses lectura'] = total_read_misses_436TC64

tabla_TC64.at['436.cactusADM-1804B',
              'Miss rate lectura [%]'] = total_read_miss_rate_436TC64

tabla_TC64.at['436.cactusADM-1804B',
              'Misses escritura'] = total_write_misses_436TC64

tabla_TC64.at['436.cactusADM-1804B',
              'Miss rate escritura [%]'] = total_write_miss_rate_436TC64

# **437.leslie3d-134B**

tabla_TC64.at['437.leslie3d-134B', 'Total Misses'] = total_misses_437TC64

tabla_TC64.at['437.leslie3d-134B',
              'Miss rate total [%]'] = total_miss_rate_437TC64

tabla_TC64.at['437.leslie3d-134B',
              'Misses lectura'] = total_read_misses_437TC64

tabla_TC64.at['437.leslie3d-134B',
              'Miss rate lectura [%]'] = total_read_miss_rate_437TC64

tabla_TC64.at['437.leslie3d-134B',
              'Misses escritura'] = total_write_misses_437TC64

tabla_TC64.at['437.leslie3d-134B',
              'Miss rate escritura [%]'] = total_write_miss_rate_437TC64

# **444.namd-120B**

tabla_TC64.at['444.namd-120B', 'Total Misses'] = total_misses_444TC64

tabla_TC64.at['444.namd-120B', 'Miss rate total [%]'] = total_miss_rate_444TC64

tabla_TC64.at['444.namd-120B', 'Misses lectura'] = total_read_misses_444TC64

tabla_TC64.at['444.namd-120B',
              'Miss rate lectura [%]'] = total_read_miss_rate_444TC64

tabla_TC64.at['444.namd-120B',
              'Misses escritura'] = total_write_misses_444TC64

tabla_TC64.at['444.namd-120B',
              'Miss rate escritura [%]'] = total_write_miss_rate_444TC64

# **445.gobmk-17B**

tabla_TC64.at['445.gobmk-17B', 'Total Misses'] = total_misses_445TC64

tabla_TC64.at['445.gobmk-17B', 'Miss rate total [%]'] = total_miss_rate_445TC64

tabla_TC64.at['445.gobmk-17B', 'Misses lectura'] = total_read_misses_445TC64

tabla_TC64.at['445.gobmk-17B',
              'Miss rate lectura [%]'] = total_read_miss_rate_445TC64

tabla_TC64.at['445.gobmk-17B',
              'Misses escritura'] = total_write_misses_445TC64

tabla_TC64.at['445.gobmk-17B',
              'Miss rate escritura [%]'] = total_write_miss_rate_445TC64

# **450.soplex-247B**

tabla_TC64.at['450.soplex-247B', 'Total Misses'] = total_misses_450TC64

tabla_TC64.at['450.soplex-247B',
              'Miss rate total [%]'] = total_miss_rate_450TC64

tabla_TC64.at['450.soplex-247B', 'Misses lectura'] = total_read_misses_450TC64

tabla_TC64.at['450.soplex-247B',
              'Miss rate lectura [%]'] = total_read_miss_rate_450TC64

tabla_TC64.at['450.soplex-247B',
              'Misses escritura'] = total_write_misses_450TC64

tabla_TC64.at['450.soplex-247B',
              'Miss rate escritura [%]'] = total_write_miss_rate_450TC64

# **453.povray-887B**

tabla_TC64.at['453.povray-887B', 'Total Misses'] = total_misses_453TC64

tabla_TC64.at['453.povray-887B',
              'Miss rate total [%]'] = total_miss_rate_453TC64

tabla_TC64.at['453.povray-887B', 'Misses lectura'] = total_read_misses_453TC64

tabla_TC64.at['453.povray-887B',
              'Miss rate lectura [%]'] = total_read_miss_rate_453TC64

tabla_TC64.at['453.povray-887B',
              'Misses escritura'] = total_write_misses_453TC64

tabla_TC64.at['453.povray-887B',
              'Miss rate escritura [%]'] = total_write_miss_rate_453TC64

# **454.calculix-104B**

tabla_TC64.at['454.calculix-104B', 'Total Misses'] = total_misses_454TC64

tabla_TC64.at['454.calculix-104B',
              'Miss rate total [%]'] = total_miss_rate_454TC64

tabla_TC64.at['454.calculix-104B',
              'Misses lectura'] = total_read_misses_454TC64

tabla_TC64.at['454.calculix-104B',
              'Miss rate lectura [%]'] = total_read_miss_rate_454TC64

tabla_TC64.at['454.calculix-104B',
              'Misses escritura'] = total_write_misses_454TC64

tabla_TC64.at['454.calculix-104B',
              'Miss rate escritura [%]'] = total_write_miss_rate_454TC64

# **456.hmmer-191B**

tabla_TC64.at['456.hmmer-191B', 'Total Misses'] = total_misses_456TC64

tabla_TC64.at['456.hmmer-191B',
              'Miss rate total [%]'] = total_miss_rate_456TC64

tabla_TC64.at['456.hmmer-191B', 'Misses lectura'] = total_read_misses_456TC64

tabla_TC64.at['456.hmmer-191B',
              'Miss rate lectura [%]'] = total_read_miss_rate_456TC64

tabla_TC64.at['456.hmmer-191B',
              'Misses escritura'] = total_write_misses_456TC64

tabla_TC64.at['456.hmmer-191B',
              'Miss rate escritura [%]'] = total_write_miss_rate_456TC64

# **458.sjeng-1088B**

tabla_TC64.at['458.sjeng-1088B', 'Total Misses'] = total_misses_458TC64

tabla_TC64.at['458.sjeng-1088B',
              'Miss rate total [%]'] = total_miss_rate_458TC64

tabla_TC64.at['458.sjeng-1088B', 'Misses lectura'] = total_read_misses_458TC64

tabla_TC64.at['458.sjeng-1088B',
              'Miss rate lectura [%]'] = total_read_miss_rate_458TC64

tabla_TC64.at['458.sjeng-1088B',
              'Misses escritura'] = total_write_misses_458TC64

tabla_TC64.at['458.sjeng-1088B',
              'Miss rate escritura [%]'] = total_write_miss_rate_458TC64

# **459.GemsFDTD-1169B**

tabla_TC64.at['459.GemsFDTD-1169B', 'Total Misses'] = total_misses_459TC64

tabla_TC64.at['459.GemsFDTD-1169B',
              'Miss rate total [%]'] = total_miss_rate_459TC64

tabla_TC64.at['459.GemsFDTD-1169B',
              'Misses lectura'] = total_read_misses_459TC64

tabla_TC64.at['459.GemsFDTD-1169B',
              'Miss rate lectura [%]'] = total_read_miss_rate_459TC64

tabla_TC64.at['459.GemsFDTD-1169B',
              'Misses escritura'] = total_write_misses_459TC64

tabla_TC64.at['459.GemsFDTD-1169B',
              'Miss rate escritura [%]'] = total_write_miss_rate_459TC64

# **462.libquantum-1343B**

tabla_TC64.at['462.libquantum-1343B', 'Total Misses'] = total_misses_462TC64

tabla_TC64.at['462.libquantum-1343B',
              'Miss rate total [%]'] = total_miss_rate_462TC64

tabla_TC64.at['462.libquantum-1343B',
              'Misses lectura'] = total_read_misses_462TC64

tabla_TC64.at['462.libquantum-1343B',
              'Miss rate lectura [%]'] = total_read_miss_rate_462TC64

tabla_TC64.at['462.libquantum-1343B',
              'Misses escritura'] = total_write_misses_462TC64

tabla_TC64.at['462.libquantum-1343B',
              'Miss rate escritura [%]'] = total_write_miss_rate_462TC64

# **464.h264ref-30B**

tabla_TC64.at['464.h264ref-30B', 'Total Misses'] = total_misses_464TC64

tabla_TC64.at['464.h264ref-30B',
              'Miss rate total [%]'] = total_miss_rate_464TC64

tabla_TC64.at['464.h264ref-30B', 'Misses lectura'] = total_read_misses_464TC64

tabla_TC64.at['464.h264ref-30B',
              'Miss rate lectura [%]'] = total_read_miss_rate_464TC64

tabla_TC64.at['464.h264ref-30B',
              'Misses escritura'] = total_write_misses_464TC64

tabla_TC64.at['464.h264ref-30B',
              'Miss rate escritura [%]'] = total_write_miss_rate_464TC64

# **465.tonto-1769B**

tabla_TC64.at['465.tonto-1769B', 'Total Misses'] = total_misses_465TC64

tabla_TC64.at['465.tonto-1769B',
              'Miss rate total [%]'] = total_miss_rate_465TC64

tabla_TC64.at['465.tonto-1769B', 'Misses lectura'] = total_read_misses_465TC64

tabla_TC64.at['465.tonto-1769B',
              'Miss rate lectura [%]'] = total_read_miss_rate_465TC64

tabla_TC64.at['465.tonto-1769B',
              'Misses escritura'] = total_write_misses_465TC64
tabla_TC64.at['465.tonto-1769B',
              'Miss rate escritura [%]'] = total_write_miss_rate_465TC64

# **470.lbm-1274B**

tabla_TC64.at['470.lbm-1274B', 'Total Misses'] = total_misses_470TC64

tabla_TC64.at['470.lbm-1274B', 'Miss rate total [%]'] = total_miss_rate_470TC64

tabla_TC64.at['470.lbm-1274B', 'Misses lectura'] = total_read_misses_470TC64

tabla_TC64.at['470.lbm-1274B',
              'Miss rate lectura [%]'] = total_read_miss_rate_470TC64

tabla_TC64.at['470.lbm-1274B',
              'Misses escritura'] = total_write_misses_470TC64

tabla_TC64.at['470.lbm-1274B',
              'Miss rate escritura [%]'] = total_write_miss_rate_470TC64

# **471.omnetpp-188B**

tabla_TC64.at['471.omnetpp-188B', 'Total Misses'] = total_misses_471TC64

tabla_TC64.at['471.omnetpp-188B',
              'Miss rate total [%]'] = total_miss_rate_471TC64

tabla_TC64.at['471.omnetpp-188B', 'Misses lectura'] = total_read_misses_471TC64

tabla_TC64.at['471.omnetpp-188B',
              'Miss rate lectura [%]'] = total_read_miss_rate_471TC64

tabla_TC64.at['471.omnetpp-188B',
              'Misses escritura'] = total_write_misses_471TC64

tabla_TC64.at['471.omnetpp-188B',
              'Miss rate escritura [%]'] = total_write_miss_rate_471TC64

# **473.astar-153B**

tabla_TC64.at['473.astar-153B', 'Total Misses'] = total_misses_473TC64

tabla_TC64.at['473.astar-153B',
              'Miss rate total [%]'] = total_miss_rate_473TC64

tabla_TC64.at['473.astar-153B', 'Misses lectura'] = total_read_misses_473TC64

tabla_TC64.at['473.astar-153B',
              'Miss rate lectura [%]'] = total_read_miss_rate_473TC64

tabla_TC64.at['473.astar-153B',
              'Misses escritura'] = total_write_misses_473TC64

tabla_TC64.at['473.astar-153B',
              'Miss rate escritura [%]'] = total_write_miss_rate_473TC64

# **481.wrf-1170B**

tabla_TC64.at['481.wrf-1170B', 'Total Misses'] = total_misses_481TC64

tabla_TC64.at['481.wrf-1170B', 'Miss rate total [%]'] = total_miss_rate_481TC64

tabla_TC64.at['481.wrf-1170B', 'Misses lectura'] = total_read_misses_481TC64

tabla_TC64.at['481.wrf-1170B',
              'Miss rate lectura [%]'] = total_read_miss_rate_481TC64

tabla_TC64.at['481.wrf-1170B',
              'Misses escritura'] = total_write_misses_481TC64

tabla_TC64.at['481.wrf-1170B',
              'Miss rate escritura [%]'] = total_write_miss_rate_481TC64

# **482.sphinx3-1100B**

tabla_TC64.at['482.sphinx3-1100B', 'Total Misses'] = total_misses_482TC64

tabla_TC64.at['482.sphinx3-1100B',
              'Miss rate total [%]'] = total_miss_rate_482TC64

tabla_TC64.at['482.sphinx3-1100B',
              'Misses lectura'] = total_read_misses_482TC64

tabla_TC64.at['482.sphinx3-1100B',
              'Miss rate lectura [%]'] = total_read_miss_rate_482TC64

tabla_TC64.at['482.sphinx3-1100B',
              'Misses escritura'] = total_write_misses_482TC64

tabla_TC64.at['482.sphinx3-1100B',
              'Miss rate escritura [%]'] = total_write_miss_rate_482TC64

# **483.xalancbmk-127B**

tabla_TC64.at['483.xalancbmk-127B', 'Total Misses'] = total_misses_483TC64

tabla_TC64.at['483.xalancbmk-127B',
              'Miss rate total [%]'] = total_miss_rate_483TC64

tabla_TC64.at['483.xalancbmk-127B',
              'Misses lectura'] = total_read_misses_483TC64

tabla_TC64.at['483.xalancbmk-127B',
              'Miss rate lectura [%]'] = total_read_miss_rate_483TC64

tabla_TC64.at['483.xalancbmk-127B',
              'Misses escritura'] = total_write_misses_483TC64

tabla_TC64.at['483.xalancbmk-127B',
              'Miss rate escritura [%]'] = total_write_miss_rate_483TC64

print(">>>>>All TC64 data has been uploaded successfully")

###########################################
# Extractor para experimento con tamaño 64#
###########################################

# Creación de tablas para adjuntar valores
# Una tabla por tamaño
tabla_TC128 = pd.DataFrame(index=[
    '400.perlbench-41B', '401.bzip2-226B', '403.gcc-16B', '410.bwaves-1963B', '416.gamess-875B', '429.mcf-184B', '433.milc-127B',
    '435.gromacs-111B', '436.cactusADM-1804B', '437.leslie3d-134B', '444.namd-120B', '445.gobmk-17B',
    '450.soplex-247B', '453.povray-887B', '454.calculix-104B', '456.hmmer-191B', '458.sjeng-1088B', '459.GemsFDTD-1169B',
    '462.libquantum-1343B', '464.h264ref-30B', '465.tonto-1769B', '470.lbm-1274B', '471.omnetpp-188B', '473.astar-153B', '481.wrf-1170B',
    '482.sphinx3-1100B', '483.xalancbmk-127B'], columns=[
    'App', 'Total Misses', 'Miss rate total [%]', 'Misses lectura', 'Miss rate lectura [%]', 'Misses escritura', 'Miss rate escritura [%]'])
tabla_TC128['App'] = tabla_TC128.index

# Files paths
filename_109 = "RESULTS_TC/400TC128.txt"
filename_110 = "RESULTS_TC/401TC128.txt"
filename_111 = "RESULTS_TC/403TC128.txt"
filename_112 = "RESULTS_TC/410TC128.txt"
filename_113 = "RESULTS_TC/416TC128.txt"
filename_114 = "RESULTS_TC/429TC128.txt"
filename_115 = "RESULTS_TC/433TC128.txt"
filename_116 = "RESULTS_TC/435TC128.txt"
filename_117 = "RESULTS_TC/436TC128.txt"
filename_118 = "RESULTS_TC/437TC128.txt"
filename_119 = "RESULTS_TC/444TC128.txt"
filename_120 = "RESULTS_TC/445TC128.txt"
filename_121 = "RESULTS_TC/450TC128.txt"
filename_122 = "RESULTS_TC/453TC128.txt"
filename_123 = "RESULTS_TC/454TC128.txt"
filename_124 = "RESULTS_TC/456TC128.txt"
filename_125 = "RESULTS_TC/458TC128.txt"
filename_126 = "RESULTS_TC/459TC128.txt"
filename_127 = "RESULTS_TC/462TC128.txt"
filename_128 = "RESULTS_TC/464TC128.txt"
filename_129 = "RESULTS_TC/465TC128.txt"
filename_130 = "RESULTS_TC/470TC128.txt"
filename_131 = "RESULTS_TC/471TC128.txt"
filename_132 = "RESULTS_TC/473TC128.txt"
filename_133 = "RESULTS_TC/481TC128.txt"
filename_134 = "RESULTS_TC/482TC128.txt"
filename_135 = "RESULTS_TC/483TC128.txt"

# Content file extracter
with open(filename_109, 'r') as file:
    content_400TC128 = file.read()
with open(filename_110, 'r') as file:
    content_401TC128 = file.read()
with open(filename_111, 'r') as file:
    content_403TC128 = file.read()
with open(filename_112, 'r') as file:
    content_410TC128 = file.read()
with open(filename_113, 'r') as file:
    content_416TC128 = file.read()
with open(filename_114, 'r') as file:
    content_429TC128 = file.read()
with open(filename_115, 'r') as file:
    content_433TC128 = file.read()
with open(filename_116, 'r') as file:
    content_435TC128 = file.read()
with open(filename_117, 'r') as file:
    content_436TC128 = file.read()
with open(filename_118, 'r') as file:
    content_437TC128 = file.read()
with open(filename_119, 'r') as file:
    content_444TC128 = file.read()
with open(filename_120, 'r') as file:
    content_445TC128 = file.read()
with open(filename_121, 'r') as file:
    content_450TC128 = file.read()
with open(filename_122, 'r') as file:
    content_453TC128 = file.read()
with open(filename_123, 'r') as file:
    content_454TC128 = file.read()
with open(filename_124, 'r') as file:
    content_456TC128 = file.read()
with open(filename_125, 'r') as file:
    content_458TC128 = file.read()
with open(filename_126, 'r') as file:
    content_459TC128 = file.read()
with open(filename_127, 'r') as file:
    content_462TC128 = file.read()
with open(filename_128, 'r') as file:
    content_464TC128 = file.read()
with open(filename_129, 'r') as file:
    content_465TC128 = file.read()
with open(filename_130, 'r') as file:
    content_470TC128 = file.read()
with open(filename_131, 'r') as file:
    content_471TC128 = file.read()
with open(filename_132, 'r') as file:
    content_473TC128 = file.read()
with open(filename_133, 'r') as file:
    content_481TC128 = file.read()
with open(filename_134, 'r') as file:
    content_482TC128 = file.read()
with open(filename_135, 'r') as file:
    content_483TC128 = file.read()

# Variables según aplicación

# 400.pearlbench-41B
total_misses_400TC128 = re.search(
    r"Total_misses (\d+)", content_400TC128).group(1)
total_miss_rate_400TC128 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_400TC128).group(1)
total_read_misses_400TC128 = re.search(
    r"Total_read_misses (\d+)", content_400TC128).group(1)
total_read_miss_rate_400TC128 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_400TC128).group(1)
total_write_misses_400TC128 = re.search(
    r"Total_write_misses (\d+)", content_400TC128).group(1)
total_write_miss_rate_400TC128 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_400TC128).group(1)
print(">>>>>All TC128 400.pearlbench-41B variables where obtained successfully")

# 401.bzip2-226B
total_misses_401TC128 = re.search(
    r"Total_misses (\d+)", content_401TC128).group(1)
total_miss_rate_401TC128 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_401TC128).group(1)
total_read_misses_401TC128 = re.search(
    r"Total_read_misses (\d+)", content_401TC128).group(1)
total_read_miss_rate_401TC128 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_401TC128).group(1)
total_write_misses_401TC128 = re.search(
    r"Total_write_misses (\d+)", content_401TC128).group(1)
total_write_miss_rate_401TC128 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_401TC128).group(1)
print(">>>>>All TC128 401.bzip2-226B variables where obtained successfully")

# 403.gcc-16B
total_misses_403TC128 = re.search(
    r"Total_misses (\d+)", content_403TC128).group(1)
total_miss_rate_403TC128 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_403TC128).group(1)
total_read_misses_403TC128 = re.search(
    r"Total_read_misses (\d+)", content_403TC128).group(1)
total_read_miss_rate_403TC128 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_403TC128).group(1)
total_write_misses_403TC128 = re.search(
    r"Total_write_misses (\d+)", content_403TC128).group(1)
total_write_miss_rate_403TC128 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_403TC128).group(1)
print(">>>>>All TC128 403.gcc-16B variables where obtained successfully")

# 410.bwaves-1963B
total_misses_410TC128 = re.search(
    r"Total_misses (\d+)", content_410TC128).group(1)
total_miss_rate_410TC128 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_410TC128).group(1)
total_read_misses_410TC128 = re.search(
    r"Total_read_misses (\d+)", content_410TC128).group(1)
total_read_miss_rate_410TC128 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_410TC128).group(1)
total_write_misses_410TC128 = re.search(
    r"Total_write_misses (\d+)", content_410TC128).group(1)
total_write_miss_rate_410TC128 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_410TC128).group(1)
print(">>>>>All TC128 410.bwaves-1963B variables where obtained successfully")

# 416.gamess-875B
total_misses_416TC128 = re.search(
    r"Total_misses (\d+)", content_416TC128).group(1)
total_miss_rate_416TC128 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_416TC128).group(1)
total_read_misses_416TC128 = re.search(
    r"Total_read_misses (\d+)", content_416TC128).group(1)
total_read_miss_rate_416TC128 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_416TC128).group(1)
total_write_misses_416TC128 = re.search(
    r"Total_write_misses (\d+)", content_416TC128).group(1)
total_write_miss_rate_416TC128 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_416TC128).group(1)
print(">>>>>All TC128 416.gamess-875B variables where obtained successfully")

# 429.mcf-184B
total_misses_429TC128 = re.search(
    r"Total_misses (\d+)", content_429TC128).group(1)
total_miss_rate_429TC128 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_429TC128).group(1)
total_read_misses_429TC128 = re.search(
    r"Total_read_misses (\d+)", content_429TC128).group(1)
total_read_miss_rate_429TC128 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_429TC128).group(1)
total_write_misses_429TC128 = re.search(
    r"Total_write_misses (\d+)", content_429TC128).group(1)
total_write_miss_rate_429TC128 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_429TC128).group(1)
print(">>>>>All TC128 429.mcf-184B variables where obtained successfully")

# 433.milc-127B
total_misses_433TC128 = re.search(
    r"Total_misses (\d+)", content_433TC128).group(1)
total_miss_rate_433TC128 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_433TC128).group(1)
total_read_misses_433TC128 = re.search(
    r"Total_read_misses (\d+)", content_433TC128).group(1)
total_read_miss_rate_433TC128 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_433TC128).group(1)
total_write_misses_433TC128 = re.search(
    r"Total_write_misses (\d+)", content_433TC128).group(1)
total_write_miss_rate_433TC128 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_433TC128).group(1)
print(">>>>>All TC128 433.milc-127B variables where obtained successfully")

# 435.gromacs-111B
total_misses_435TC128 = re.search(
    r"Total_misses (\d+)", content_435TC128).group(1)
total_miss_rate_435TC128 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_435TC128).group(1)
total_read_misses_435TC128 = re.search(
    r"Total_read_misses (\d+)", content_435TC128).group(1)
total_read_miss_rate_435TC128 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_435TC128).group(1)
total_write_misses_435TC128 = re.search(
    r"Total_write_misses (\d+)", content_435TC128).group(1)
total_write_miss_rate_435TC128 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_435TC128).group(1)
print(">>>>>All TC128 435.gromacs-111B variables where obtained successfully")

# 436.cactusADM-1804B
total_misses_436TC128 = re.search(
    r"Total_misses (\d+)", content_436TC128).group(1)
total_miss_rate_436TC128 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_436TC128).group(1)
total_read_misses_436TC128 = re.search(
    r"Total_read_misses (\d+)", content_436TC128).group(1)
total_read_miss_rate_436TC128 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_436TC128).group(1)
total_write_misses_436TC128 = re.search(
    r"Total_write_misses (\d+)", content_436TC128).group(1)
total_write_miss_rate_436TC128 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_436TC128).group(1)
print(">>>>>All TC128 436.cactusADM-1804B variables where obtained successfully")

# 437.leslie3d-134B
total_misses_437TC128 = re.search(
    r"Total_misses (\d+)", content_437TC128).group(1)
total_miss_rate_437TC128 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_437TC128).group(1)
total_read_misses_437TC128 = re.search(
    r"Total_read_misses (\d+)", content_437TC128).group(1)
total_read_miss_rate_437TC128 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_437TC128).group(1)
total_write_misses_437TC128 = re.search(
    r"Total_write_misses (\d+)", content_437TC128).group(1)
total_write_miss_rate_437TC128 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_437TC128).group(1)
print(">>>>>All TC128 437.leslie3d-134B variables where obtained successfully")

# 444.namd-120B
total_misses_444TC128 = re.search(
    r"Total_misses (\d+)", content_444TC128).group(1)
total_miss_rate_444TC128 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_444TC128).group(1)
total_read_misses_444TC128 = re.search(
    r"Total_read_misses (\d+)", content_444TC128).group(1)
total_read_miss_rate_444TC128 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_444TC128).group(1)
total_write_misses_444TC128 = re.search(
    r"Total_write_misses (\d+)", content_444TC128).group(1)
total_write_miss_rate_444TC128 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_444TC128).group(1)
print(">>>>>All TC128 444.namd-120B variables where obtained successfully")

# 445.gobmk-17B
total_misses_445TC128 = re.search(
    r"Total_misses (\d+)", content_445TC128).group(1)
total_miss_rate_445TC128 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_445TC128).group(1)
total_read_misses_445TC128 = re.search(
    r"Total_read_misses (\d+)", content_445TC128).group(1)
total_read_miss_rate_445TC128 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_445TC128).group(1)
total_write_misses_445TC128 = re.search(
    r"Total_write_misses (\d+)", content_445TC128).group(1)
total_write_miss_rate_445TC128 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_445TC128).group(1)
print(">>>>>All TC128 445.gobmk-17B variables where obtained successfully")

# 450.soplex-247B
total_misses_450TC128 = re.search(
    r"Total_misses (\d+)", content_450TC128).group(1)
total_miss_rate_450TC128 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_450TC128).group(1)
total_read_misses_450TC128 = re.search(
    r"Total_read_misses (\d+)", content_450TC128).group(1)
total_read_miss_rate_450TC128 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_450TC128).group(1)
total_write_misses_450TC128 = re.search(
    r"Total_write_misses (\d+)", content_450TC128).group(1)
total_write_miss_rate_450TC128 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_450TC128).group(1)
print(">>>>>All TC128 450.soplex-247B variables where obtained successfully")

# 453.povray-887B
total_misses_453TC128 = re.search(
    r"Total_misses (\d+)", content_453TC128).group(1)
total_miss_rate_453TC128 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_453TC128).group(1)
total_read_misses_453TC128 = re.search(
    r"Total_read_misses (\d+)", content_453TC128).group(1)
total_read_miss_rate_453TC128 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_453TC128).group(1)
total_write_misses_453TC128 = re.search(
    r"Total_write_misses (\d+)", content_453TC128).group(1)
total_write_miss_rate_453TC128 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_453TC128).group(1)
print(">>>>>All TC128 453.povray-887B variables where obtained successfully")

# 454.calculix-104B
total_misses_454TC128 = re.search(
    r"Total_misses (\d+)", content_454TC128).group(1)
total_miss_rate_454TC128 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_454TC128).group(1)
total_read_misses_454TC128 = re.search(
    r"Total_read_misses (\d+)", content_454TC128).group(1)
total_read_miss_rate_454TC128 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_454TC128).group(1)
total_write_misses_454TC128 = re.search(
    r"Total_write_misses (\d+)", content_454TC128).group(1)
total_write_miss_rate_454TC128 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_454TC128).group(1)
print(">>>>>All TC128 454.calculix-104B variables where obtained successfully")

# 456.hmmer-191B
total_misses_456TC128 = re.search(
    r"Total_misses (\d+)", content_456TC128).group(1)
total_miss_rate_456TC128 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_456TC128).group(1)
total_read_misses_456TC128 = re.search(
    r"Total_read_misses (\d+)", content_456TC128).group(1)
total_read_miss_rate_456TC128 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_456TC128).group(1)
total_write_misses_456TC128 = re.search(
    r"Total_write_misses (\d+)", content_456TC128).group(1)
total_write_miss_rate_456TC128 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_456TC128).group(1)
print(">>>>>All TC128 456.hmmer-191B variables where obtained successfully")

# 458.sjeng-1088B
total_misses_458TC128 = re.search(
    r"Total_misses (\d+)", content_458TC128).group(1)
total_miss_rate_458TC128 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_458TC128).group(1)
total_read_misses_458TC128 = re.search(
    r"Total_read_misses (\d+)", content_458TC128).group(1)
total_read_miss_rate_458TC128 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_458TC128).group(1)
total_write_misses_458TC128 = re.search(
    r"Total_write_misses (\d+)", content_458TC128).group(1)
total_write_miss_rate_458TC128 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_458TC128).group(1)
print(">>>>>All TC128 458.sjeng-1088B variables where obtained successfully")

# 459.GemsFDTD-1169B
total_misses_459TC128 = re.search(
    r"Total_misses (\d+)", content_459TC128).group(1)
total_miss_rate_459TC128 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_459TC128).group(1)
total_read_misses_459TC128 = re.search(
    r"Total_read_misses (\d+)", content_459TC128).group(1)
total_read_miss_rate_459TC128 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_459TC128).group(1)
total_write_misses_459TC128 = re.search(
    r"Total_write_misses (\d+)", content_459TC128).group(1)
total_write_miss_rate_459TC128 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_459TC128).group(1)
print(">>>>>All TC128 459.GemsFDTD-1169B variables where obtained successfully")

# 462.libquantum-1343B
total_misses_462TC128 = re.search(
    r"Total_misses (\d+)", content_462TC128).group(1)
total_miss_rate_462TC128 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_462TC128).group(1)
total_read_misses_462TC128 = re.search(
    r"Total_read_misses (\d+)", content_462TC128).group(1)
total_read_miss_rate_462TC128 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_462TC128).group(1)
total_write_misses_462TC128 = re.search(
    r"Total_write_misses (\d+)", content_462TC128).group(1)
total_write_miss_rate_462TC128 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_462TC128).group(1)
print(">>>>>All TC128 462.libquantum-1343B variables where obtained successfully")

# 464.h264ref-30B
total_misses_464TC128 = re.search(
    r"Total_misses (\d+)", content_464TC128).group(1)
total_miss_rate_464TC128 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_464TC128).group(1)
total_read_misses_464TC128 = re.search(
    r"Total_read_misses (\d+)", content_464TC128).group(1)
total_read_miss_rate_464TC128 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_464TC128).group(1)
total_write_misses_464TC128 = re.search(
    r"Total_write_misses (\d+)", content_464TC128).group(1)
total_write_miss_rate_464TC128 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_464TC128).group(1)
print(">>>>>All TC128 464.h264ref-30B variables where obtained successfully")

# 465.tonto-1769B
total_misses_465TC128 = re.search(
    r"Total_misses (\d+)", content_465TC128).group(1)
total_miss_rate_465TC128 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_465TC128).group(1)
total_read_misses_465TC128 = re.search(
    r"Total_read_misses (\d+)", content_465TC128).group(1)
total_read_miss_rate_465TC128 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_465TC128).group(1)
total_write_misses_465TC128 = re.search(
    r"Total_write_misses (\d+)", content_465TC128).group(1)
total_write_miss_rate_465TC128 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_465TC128).group(1)
print(">>>>>All TC128 465.tonto-1769B variables where obtained successfully")

# 470.lbm-1274B
total_misses_470TC128 = re.search(
    r"Total_misses (\d+)", content_470TC128).group(1)
total_miss_rate_470TC128 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_470TC128).group(1)
total_read_misses_470TC128 = re.search(
    r"Total_read_misses (\d+)", content_470TC128).group(1)
total_read_miss_rate_470TC128 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_470TC128).group(1)
total_write_misses_470TC128 = re.search(
    r"Total_write_misses (\d+)", content_470TC128).group(1)
total_write_miss_rate_470TC128 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_470TC128).group(1)
print(">>>>>All TC128 470.lbm-1274B variables where obtained successfully")

# 471.omnetpp-188B
total_misses_471TC128 = re.search(
    r"Total_misses (\d+)", content_471TC128).group(1)
total_miss_rate_471TC128 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_471TC128).group(1)
total_read_misses_471TC128 = re.search(
    r"Total_read_misses (\d+)", content_471TC128).group(1)
total_read_miss_rate_471TC128 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_471TC128).group(1)
total_write_misses_471TC128 = re.search(
    r"Total_write_misses (\d+)", content_471TC128).group(1)
total_write_miss_rate_471TC128 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_471TC128).group(1)
print(">>>>>All TC128 471.omnetpp-188B variables where obtained successfully")

# 473.astar-153B
total_misses_473TC128 = re.search(
    r"Total_misses (\d+)", content_473TC128).group(1)
total_miss_rate_473TC128 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_473TC128).group(1)
total_read_misses_473TC128 = re.search(
    r"Total_read_misses (\d+)", content_473TC128).group(1)
total_read_miss_rate_473TC128 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_473TC128).group(1)
total_write_misses_473TC128 = re.search(
    r"Total_write_misses (\d+)", content_473TC128).group(1)
total_write_miss_rate_473TC128 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_473TC128).group(1)
print(">>>>>All TC128 473.astar-153B variables where obtained successfully")

# 481.wrf-1170B
total_misses_481TC128 = re.search(
    r"Total_misses (\d+)", content_481TC128).group(1)
total_miss_rate_481TC128 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_481TC128).group(1)
total_read_misses_481TC128 = re.search(
    r"Total_read_misses (\d+)", content_481TC128).group(1)
total_read_miss_rate_481TC128 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_481TC128).group(1)
total_write_misses_481TC128 = re.search(
    r"Total_write_misses (\d+)", content_481TC128).group(1)
total_write_miss_rate_481TC128 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_481TC128).group(1)
print(">>>>>All TC128 481.wrf-1170B variables where obtained successfully")

# 482.sphinx3-1100B
total_misses_482TC128 = re.search(
    r"Total_misses (\d+)", content_482TC128).group(1)
total_miss_rate_482TC128 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_482TC128).group(1)
total_read_misses_482TC128 = re.search(
    r"Total_read_misses (\d+)", content_482TC128).group(1)
total_read_miss_rate_482TC128 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_482TC128).group(1)
total_write_misses_482TC128 = re.search(
    r"Total_write_misses (\d+)", content_482TC128).group(1)
total_write_miss_rate_482TC128 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_482TC128).group(1)
print(">>>>>All TC128 482.sphinx3-1100B variables where obtained successfully")

# 483.xalancbmk-127B
total_misses_483TC128 = re.search(
    r"Total_misses (\d+)", content_483TC128).group(1)
total_miss_rate_483TC128 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_483TC128).group(1)
total_read_misses_483TC128 = re.search(
    r"Total_read_misses (\d+)", content_483TC128).group(1)
total_read_miss_rate_483TC128 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_483TC128).group(1)
total_write_misses_483TC128 = re.search(
    r"Total_write_misses (\d+)", content_483TC128).group(1)
total_write_miss_rate_483TC128 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_483TC128).group(1)
print(">>>>>All TC128 483.xalancbmk-127B variables where obtained successfully")

#############################
# Adjunta datos a dataframe #
#############################

# **400.perlbench-41B**

tabla_TC128.at['400.perlbench-41B', 'Total Misses'] = total_misses_400TC128

tabla_TC128.at['400.perlbench-41B',
               'Miss rate total [%]'] = total_miss_rate_400TC128

tabla_TC128.at['400.perlbench-41B',
               'Misses lectura'] = total_read_misses_400TC128

tabla_TC128.at['400.perlbench-41B',
               'Miss rate lectura [%]'] = total_read_miss_rate_400TC128

tabla_TC128.at['400.perlbench-41B',
               'Misses escritura'] = total_write_misses_400TC128

tabla_TC128.at['400.perlbench-41B',
               'Miss rate escritura [%]'] = total_write_miss_rate_400TC128

# **401.bzip2-226B**

tabla_TC128.at['401.bzip2-226B', 'Total Misses'] = total_misses_401TC128

tabla_TC128.at['401.bzip2-226B',
               'Miss rate total [%]'] = total_miss_rate_401TC128

tabla_TC128.at['401.bzip2-226B', 'Misses lectura'] = total_read_misses_401TC128

tabla_TC128.at['401.bzip2-226B',
               'Miss rate lectura [%]'] = total_read_miss_rate_401TC128

tabla_TC128.at['401.bzip2-226B',
               'Misses escritura'] = total_write_misses_401TC128

tabla_TC128.at['401.bzip2-226B',
               'Miss rate escritura [%]'] = total_write_miss_rate_401TC128

# **403.gcc-16B**

tabla_TC128.at['403.gcc-16B', 'Total Misses'] = total_misses_403TC128

tabla_TC128.at['403.gcc-16B', 'Miss rate total [%]'] = total_miss_rate_403TC128

tabla_TC128.at['403.gcc-16B', 'Misses lectura'] = total_read_misses_403TC128

tabla_TC128.at['403.gcc-16B',
               'Miss rate lectura [%]'] = total_read_miss_rate_403TC128

tabla_TC128.at['403.gcc-16B',
               'Misses escritura'] = total_write_misses_403TC128

tabla_TC128.at['403.gcc-16B',
               'Miss rate escritura [%]'] = total_write_miss_rate_403TC128

# **410.bwaves-1963B**

tabla_TC128.at['410.bwaves-1963B', 'Total Misses'] = total_misses_410TC128

tabla_TC128.at['410.bwaves-1963B',
               'Miss rate total [%]'] = total_miss_rate_410TC128

tabla_TC128.at['410.bwaves-1963B',
               'Misses lectura'] = total_read_misses_410TC128

tabla_TC128.at['410.bwaves-1963B',
               'Miss rate lectura [%]'] = total_read_miss_rate_410TC128

tabla_TC128.at['410.bwaves-1963B',
               'Misses escritura'] = total_write_misses_410TC128

tabla_TC128.at['410.bwaves-1963B',
               'Miss rate escritura [%]'] = total_write_miss_rate_410TC128

# **416.gamess-875B**

tabla_TC128.at['416.gamess-875B', 'Total Misses'] = total_misses_416TC128

tabla_TC128.at['416.gamess-875B',
               'Miss rate total [%]'] = total_miss_rate_416TC128

tabla_TC128.at['416.gamess-875B',
               'Misses lectura'] = total_read_misses_416TC128

tabla_TC128.at['416.gamess-875B',
               'Miss rate lectura [%]'] = total_read_miss_rate_416TC128

tabla_TC128.at['416.gamess-875B',
               'Misses escritura'] = total_write_misses_416TC128

tabla_TC128.at['416.gamess-875B',
               'Miss rate escritura [%]'] = total_write_miss_rate_416TC128

# **429.mcf-184B**

tabla_TC128.at['429.mcf-184B', 'Total Misses'] = total_misses_429TC128

tabla_TC128.at['429.mcf-184B',
               'Miss rate total [%]'] = total_miss_rate_429TC128

tabla_TC128.at['429.mcf-184B', 'Misses lectura'] = total_read_misses_429TC128

tabla_TC128.at['429.mcf-184B',
               'Miss rate lectura [%]'] = total_read_miss_rate_429TC128

tabla_TC128.at['429.mcf-184B',
               'Misses escritura'] = total_write_misses_429TC128

tabla_TC128.at['429.mcf-184B',
               'Miss rate escritura [%]'] = total_write_miss_rate_429TC128

# **433.milc-127B**

tabla_TC128.at['433.milc-127B', 'Total Misses'] = total_misses_433TC128

tabla_TC128.at['433.milc-127B',
               'Miss rate total [%]'] = total_miss_rate_433TC128

tabla_TC128.at['433.milc-127B', 'Misses lectura'] = total_read_misses_433TC128

tabla_TC128.at['433.milc-127B',
               'Miss rate lectura [%]'] = total_read_miss_rate_433TC128

tabla_TC128.at['433.milc-127B',
               'Misses escritura'] = total_write_misses_433TC128

tabla_TC128.at['433.milc-127B',
               'Miss rate escritura [%]'] = total_write_miss_rate_433TC128

# **435.gromacs-111B**

tabla_TC128.at['435.gromacs-111B', 'Total Misses'] = total_misses_435TC128

tabla_TC128.at['435.gromacs-111B',
               'Miss rate total [%]'] = total_miss_rate_435TC128

tabla_TC128.at['435.gromacs-111B',
               'Misses lectura'] = total_read_misses_435TC128

tabla_TC128.at['435.gromacs-111B',
               'Miss rate lectura [%]'] = total_read_miss_rate_435TC128

tabla_TC128.at['435.gromacs-111B',
               'Misses escritura'] = total_write_misses_435TC128

tabla_TC128.at['435.gromacs-111B',
               'Miss rate escritura [%]'] = total_write_miss_rate_435TC128
# **436.cactusADM-1804B**

tabla_TC128.at['436.cactusADM-1804B', 'Total Misses'] = total_misses_436TC128

tabla_TC128.at['436.cactusADM-1804B',
               'Miss rate total [%]'] = total_miss_rate_436TC128

tabla_TC128.at['436.cactusADM-1804B',
               'Misses lectura'] = total_read_misses_436TC128

tabla_TC128.at['436.cactusADM-1804B',
               'Miss rate lectura [%]'] = total_read_miss_rate_436TC128

tabla_TC128.at['436.cactusADM-1804B',
               'Misses escritura'] = total_write_misses_436TC128

tabla_TC128.at['436.cactusADM-1804B',
               'Miss rate escritura [%]'] = total_write_miss_rate_436TC128

# **437.leslie3d-134B**

tabla_TC128.at['437.leslie3d-134B', 'Total Misses'] = total_misses_437TC128

tabla_TC128.at['437.leslie3d-134B',
               'Miss rate total [%]'] = total_miss_rate_437TC128

tabla_TC128.at['437.leslie3d-134B',
               'Misses lectura'] = total_read_misses_437TC128

tabla_TC128.at['437.leslie3d-134B',
               'Miss rate lectura [%]'] = total_read_miss_rate_437TC128

tabla_TC128.at['437.leslie3d-134B',
               'Misses escritura'] = total_write_misses_437TC128

tabla_TC128.at['437.leslie3d-134B',
               'Miss rate escritura [%]'] = total_write_miss_rate_437TC128

# **444.namd-120B**

tabla_TC128.at['444.namd-120B', 'Total Misses'] = total_misses_444TC128

tabla_TC128.at['444.namd-120B',
               'Miss rate total [%]'] = total_miss_rate_444TC128

tabla_TC128.at['444.namd-120B', 'Misses lectura'] = total_read_misses_444TC128

tabla_TC128.at['444.namd-120B',
               'Miss rate lectura [%]'] = total_read_miss_rate_444TC128

tabla_TC128.at['444.namd-120B',
               'Misses escritura'] = total_write_misses_444TC128

tabla_TC128.at['444.namd-120B',
               'Miss rate escritura [%]'] = total_write_miss_rate_444TC128

# **445.gobmk-17B**

tabla_TC128.at['445.gobmk-17B', 'Total Misses'] = total_misses_445TC128

tabla_TC128.at['445.gobmk-17B',
               'Miss rate total [%]'] = total_miss_rate_445TC128

tabla_TC128.at['445.gobmk-17B', 'Misses lectura'] = total_read_misses_445TC128

tabla_TC128.at['445.gobmk-17B',
               'Miss rate lectura [%]'] = total_read_miss_rate_445TC128

tabla_TC128.at['445.gobmk-17B',
               'Misses escritura'] = total_write_misses_445TC128

tabla_TC128.at['445.gobmk-17B',
               'Miss rate escritura [%]'] = total_write_miss_rate_445TC128

# **450.soplex-247B**

tabla_TC128.at['450.soplex-247B', 'Total Misses'] = total_misses_450TC128

tabla_TC128.at['450.soplex-247B',
               'Miss rate total [%]'] = total_miss_rate_450TC128

tabla_TC128.at['450.soplex-247B',
               'Misses lectura'] = total_read_misses_450TC128

tabla_TC128.at['450.soplex-247B',
               'Miss rate lectura [%]'] = total_read_miss_rate_450TC128

tabla_TC128.at['450.soplex-247B',
               'Misses escritura'] = total_write_misses_450TC128

tabla_TC128.at['450.soplex-247B',
               'Miss rate escritura [%]'] = total_write_miss_rate_450TC128

# **453.povray-887B**

tabla_TC128.at['453.povray-887B', 'Total Misses'] = total_misses_453TC128

tabla_TC128.at['453.povray-887B',
               'Miss rate total [%]'] = total_miss_rate_453TC128

tabla_TC128.at['453.povray-887B',
               'Misses lectura'] = total_read_misses_453TC128

tabla_TC128.at['453.povray-887B',
               'Miss rate lectura [%]'] = total_read_miss_rate_453TC128

tabla_TC128.at['453.povray-887B',
               'Misses escritura'] = total_write_misses_453TC128

tabla_TC128.at['453.povray-887B',
               'Miss rate escritura [%]'] = total_write_miss_rate_453TC128

# **454.calculix-104B**

tabla_TC128.at['454.calculix-104B', 'Total Misses'] = total_misses_454TC128

tabla_TC128.at['454.calculix-104B',
               'Miss rate total [%]'] = total_miss_rate_454TC128

tabla_TC128.at['454.calculix-104B',
               'Misses lectura'] = total_read_misses_454TC128

tabla_TC128.at['454.calculix-104B',
               'Miss rate lectura [%]'] = total_read_miss_rate_454TC128

tabla_TC128.at['454.calculix-104B',
               'Misses escritura'] = total_write_misses_454TC128

tabla_TC128.at['454.calculix-104B',
               'Miss rate escritura [%]'] = total_write_miss_rate_454TC128

# **456.hmmer-191B**

tabla_TC128.at['456.hmmer-191B', 'Total Misses'] = total_misses_456TC128

tabla_TC128.at['456.hmmer-191B',
               'Miss rate total [%]'] = total_miss_rate_456TC128

tabla_TC128.at['456.hmmer-191B', 'Misses lectura'] = total_read_misses_456TC128

tabla_TC128.at['456.hmmer-191B',
               'Miss rate lectura [%]'] = total_read_miss_rate_456TC128

tabla_TC128.at['456.hmmer-191B',
               'Misses escritura'] = total_write_misses_456TC128

tabla_TC128.at['456.hmmer-191B',
               'Miss rate escritura [%]'] = total_write_miss_rate_456TC128

# **458.sjeng-1088B**

tabla_TC128.at['458.sjeng-1088B', 'Total Misses'] = total_misses_458TC128

tabla_TC128.at['458.sjeng-1088B',
               'Miss rate total [%]'] = total_miss_rate_458TC128

tabla_TC128.at['458.sjeng-1088B',
               'Misses lectura'] = total_read_misses_458TC128

tabla_TC128.at['458.sjeng-1088B',
               'Miss rate lectura [%]'] = total_read_miss_rate_458TC128

tabla_TC128.at['458.sjeng-1088B',
               'Misses escritura'] = total_write_misses_458TC128

tabla_TC128.at['458.sjeng-1088B',
               'Miss rate escritura [%]'] = total_write_miss_rate_458TC128

# **459.GemsFDTD-1169B**

tabla_TC128.at['459.GemsFDTD-1169B', 'Total Misses'] = total_misses_459TC128

tabla_TC128.at['459.GemsFDTD-1169B',
               'Miss rate total [%]'] = total_miss_rate_459TC128

tabla_TC128.at['459.GemsFDTD-1169B',
               'Misses lectura'] = total_read_misses_459TC128

tabla_TC128.at['459.GemsFDTD-1169B',
               'Miss rate lectura [%]'] = total_read_miss_rate_459TC128

tabla_TC128.at['459.GemsFDTD-1169B',
               'Misses escritura'] = total_write_misses_459TC128

tabla_TC128.at['459.GemsFDTD-1169B',
               'Miss rate escritura [%]'] = total_write_miss_rate_459TC128

# **462.libquantum-1343B**

tabla_TC128.at['462.libquantum-1343B', 'Total Misses'] = total_misses_462TC128

tabla_TC128.at['462.libquantum-1343B',
               'Miss rate total [%]'] = total_miss_rate_462TC128

tabla_TC128.at['462.libquantum-1343B',
               'Misses lectura'] = total_read_misses_462TC128

tabla_TC128.at['462.libquantum-1343B',
               'Miss rate lectura [%]'] = total_read_miss_rate_462TC128

tabla_TC128.at['462.libquantum-1343B',
               'Misses escritura'] = total_write_misses_462TC128

tabla_TC128.at['462.libquantum-1343B',
               'Miss rate escritura [%]'] = total_write_miss_rate_462TC128

# **464.h264ref-30B**

tabla_TC128.at['464.h264ref-30B', 'Total Misses'] = total_misses_464TC128

tabla_TC128.at['464.h264ref-30B',
               'Miss rate total [%]'] = total_miss_rate_464TC128

tabla_TC128.at['464.h264ref-30B',
               'Misses lectura'] = total_read_misses_464TC128

tabla_TC128.at['464.h264ref-30B',
               'Miss rate lectura [%]'] = total_read_miss_rate_464TC128

tabla_TC128.at['464.h264ref-30B',
               'Misses escritura'] = total_write_misses_464TC128

tabla_TC128.at['464.h264ref-30B',
               'Miss rate escritura [%]'] = total_write_miss_rate_464TC128

# **465.tonto-1769B**

tabla_TC128.at['465.tonto-1769B', 'Total Misses'] = total_misses_465TC128

tabla_TC128.at['465.tonto-1769B',
               'Miss rate total [%]'] = total_miss_rate_465TC128

tabla_TC128.at['465.tonto-1769B',
               'Misses lectura'] = total_read_misses_465TC128

tabla_TC128.at['465.tonto-1769B',
               'Miss rate lectura [%]'] = total_read_miss_rate_465TC128

tabla_TC128.at['465.tonto-1769B',
               'Misses escritura'] = total_write_misses_465TC128
tabla_TC128.at['465.tonto-1769B',
               'Miss rate escritura [%]'] = total_write_miss_rate_465TC128

# **470.lbm-1274B**

tabla_TC128.at['470.lbm-1274B', 'Total Misses'] = total_misses_470TC128

tabla_TC128.at['470.lbm-1274B',
               'Miss rate total [%]'] = total_miss_rate_470TC128

tabla_TC128.at['470.lbm-1274B', 'Misses lectura'] = total_read_misses_470TC128

tabla_TC128.at['470.lbm-1274B',
               'Miss rate lectura [%]'] = total_read_miss_rate_470TC128

tabla_TC128.at['470.lbm-1274B',
               'Misses escritura'] = total_write_misses_470TC128

tabla_TC128.at['470.lbm-1274B',
               'Miss rate escritura [%]'] = total_write_miss_rate_470TC128

# **471.omnetpp-188B**

tabla_TC128.at['471.omnetpp-188B', 'Total Misses'] = total_misses_471TC128

tabla_TC128.at['471.omnetpp-188B',
               'Miss rate total [%]'] = total_miss_rate_471TC128

tabla_TC128.at['471.omnetpp-188B',
               'Misses lectura'] = total_read_misses_471TC128

tabla_TC128.at['471.omnetpp-188B',
               'Miss rate lectura [%]'] = total_read_miss_rate_471TC128

tabla_TC128.at['471.omnetpp-188B',
               'Misses escritura'] = total_write_misses_471TC128

tabla_TC128.at['471.omnetpp-188B',
               'Miss rate escritura [%]'] = total_write_miss_rate_471TC128

# **473.astar-153B**

tabla_TC128.at['473.astar-153B', 'Total Misses'] = total_misses_473TC128

tabla_TC128.at['473.astar-153B',
               'Miss rate total [%]'] = total_miss_rate_473TC128

tabla_TC128.at['473.astar-153B', 'Misses lectura'] = total_read_misses_473TC128

tabla_TC128.at['473.astar-153B',
               'Miss rate lectura [%]'] = total_read_miss_rate_473TC128

tabla_TC128.at['473.astar-153B',
               'Misses escritura'] = total_write_misses_473TC128

tabla_TC128.at['473.astar-153B',
               'Miss rate escritura [%]'] = total_write_miss_rate_473TC128

# **481.wrf-1170B**

tabla_TC128.at['481.wrf-1170B', 'Total Misses'] = total_misses_481TC128

tabla_TC128.at['481.wrf-1170B',
               'Miss rate total [%]'] = total_miss_rate_481TC128

tabla_TC128.at['481.wrf-1170B', 'Misses lectura'] = total_read_misses_481TC128

tabla_TC128.at['481.wrf-1170B',
               'Miss rate lectura [%]'] = total_read_miss_rate_481TC128

tabla_TC128.at['481.wrf-1170B',
               'Misses escritura'] = total_write_misses_481TC128

tabla_TC128.at['481.wrf-1170B',
               'Miss rate escritura [%]'] = total_write_miss_rate_481TC128

# **482.sphinx3-1100B**

tabla_TC128.at['482.sphinx3-1100B', 'Total Misses'] = total_misses_482TC128

tabla_TC128.at['482.sphinx3-1100B',
               'Miss rate total [%]'] = total_miss_rate_482TC128

tabla_TC128.at['482.sphinx3-1100B',
               'Misses lectura'] = total_read_misses_482TC128

tabla_TC128.at['482.sphinx3-1100B',
               'Miss rate lectura [%]'] = total_read_miss_rate_482TC128

tabla_TC128.at['482.sphinx3-1100B',
               'Misses escritura'] = total_write_misses_482TC128

tabla_TC128.at['482.sphinx3-1100B',
               'Miss rate escritura [%]'] = total_write_miss_rate_482TC128

# **483.xalancbmk-127B**

tabla_TC128.at['483.xalancbmk-127B', 'Total Misses'] = total_misses_483TC128

tabla_TC128.at['483.xalancbmk-127B',
               'Miss rate total [%]'] = total_miss_rate_483TC128

tabla_TC128.at['483.xalancbmk-127B',
               'Misses lectura'] = total_read_misses_483TC128

tabla_TC128.at['483.xalancbmk-127B',
               'Miss rate lectura [%]'] = total_read_miss_rate_483TC128

tabla_TC128.at['483.xalancbmk-127B',
               'Misses escritura'] = total_write_misses_483TC128

tabla_TC128.at['483.xalancbmk-127B',
               'Miss rate escritura [%]'] = total_write_miss_rate_483TC128

print(">>>>>All TC128 data has been uploaded successfully")

###########
# GEO MEAN#
###########

# GEO MEAN Miss rate total TC8
columna_TC8 = tabla_TC8['Miss rate total [%]']
columna_TC8_numpy = columna_TC8.to_numpy(dtype=np.float64)
GEOMEAN_Miss_rate_total_TC8 = gmean(columna_TC8_numpy)

# GEO MEAN Miss rate total TC16
columna_TC16 = tabla_TC16['Miss rate total [%]']
columna_TC16_numpy = columna_TC16.to_numpy(dtype=np.float64)
GEOMEAN_Miss_rate_total_TC16 = gmean(columna_TC16_numpy)

# GEO MEAN Miss rate total TC32
columna_TC32 = tabla_TC32['Miss rate total [%]']
columna_TC32_numpy = columna_TC32.to_numpy(dtype=np.float64)
GEOMEAN_Miss_rate_total_TC32 = gmean(columna_TC32_numpy)

# GEO MEAN Miss rate total TC64
columna_TC64 = tabla_TC64['Miss rate total [%]']
columna_TC64_numpy = columna_TC64.to_numpy(dtype=np.float64)
GEOMEAN_Miss_rate_total_TC64 = gmean(columna_TC64_numpy)

# GEO MEAN Miss rate total TC128
columna_TC128 = tabla_TC128['Miss rate total [%]']
columna_TC128_numpy = columna_TC128.to_numpy(dtype=np.float64)
GEOMEAN_Miss_rate_total_TC128 = gmean(columna_TC128_numpy)


#############################################################################
# Dataframes de resultados: miss rate total, miss rate total 465.tonto-1769B#
#############################################################################

# Creación de tablas para adjuntar valores

# Miss rate
tabla_miss_rate_total = pd.DataFrame(index=[
    'Miss rate total [%]'], columns=[
    'Parámetro', '8kB', '16kB', '32kB', '64kB', '128kB'])
tabla_miss_rate_total['Parámetro'] = tabla_miss_rate_total.index


# Miss rate 465.tonto-1769B
tabla_miss_rate_total_465_tonto_1769B = pd.DataFrame(index=[
    'Miss rate total 465.tonto-1769B [%]'], columns=[
    'Parámetro', '8kB', '16kB', '32kB', '64kB', '128kB'])
tabla_miss_rate_total_465_tonto_1769B['Parámetro'] = tabla_miss_rate_total_465_tonto_1769B.index

##############################
# Adjunta datos en dataframes#
##############################

# Miss rate total
tabla_miss_rate_total.at['Miss rate total [%]',
                         '8kB'] = GEOMEAN_Miss_rate_total_TC8
tabla_miss_rate_total.at['Miss rate total [%]',
                         '16kB'] = GEOMEAN_Miss_rate_total_TC16
tabla_miss_rate_total.at['Miss rate total [%]',
                         '32kB'] = GEOMEAN_Miss_rate_total_TC32
tabla_miss_rate_total.at['Miss rate total [%]',
                         '64kB'] = GEOMEAN_Miss_rate_total_TC64
tabla_miss_rate_total.at['Miss rate total [%]',
                         '128kB'] = GEOMEAN_Miss_rate_total_TC128

# Miss rate total 465.tonto_1769B
tabla_miss_rate_total_465_tonto_1769B.at['Miss rate total 465.tonto-1769B [%]',
                                         '8kB'] = total_miss_rate_465TC8
tabla_miss_rate_total_465_tonto_1769B.at['Miss rate total 465.tonto-1769B [%]',
                                         '16kB'] = total_miss_rate_465TC16
tabla_miss_rate_total_465_tonto_1769B.at['Miss rate total 465.tonto-1769B [%]',
                                         '32kB'] = total_miss_rate_465TC32
tabla_miss_rate_total_465_tonto_1769B.at['Miss rate total 465.tonto-1769B [%]',
                                         '64kB'] = total_miss_rate_465TC64
tabla_miss_rate_total_465_tonto_1769B.at['Miss rate total 465.tonto-1769B [%]',
                                         '128kB'] = total_miss_rate_465TC128


############################################
# Archivo de salida para facilitar gráficos#
############################################

# Create an Excel writer using pandas
output = pd.ExcelWriter('Results_TC.xlsx')

# Write each dataframe to a different sheet in the Excel file
tabla_TC8.to_excel(output, sheet_name='TC8', index=False)
tabla_TC16.to_excel(output, sheet_name='TC16', index=False)
tabla_TC32.to_excel(output, sheet_name='TC32', index=False)
tabla_TC64.to_excel(output, sheet_name='TC64', index=False)
tabla_TC128.to_excel(output, sheet_name='TC128', index=False)
tabla_miss_rate_total.to_excel(
    output, sheet_name='Miss rate total promedio', index=False)
tabla_miss_rate_total_465_tonto_1769B.to_excel(
    output, sheet_name='Miss rate total promedio 465.tonto-1769B', index=False)

# Save the Excel file
output.save()


print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''' Tamaño de caché 8'''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
print(tabla_TC8.to_string(index=False))
print("#################################################################################")
print("El miss rate promedio [%] con un tamaño de caché de 8kB es: ",
      GEOMEAN_Miss_rate_total_TC8, ' #')
print("#################################################################################")
print("")
print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''' Tamaño de caché 16''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
print(tabla_TC16.to_string(index=False))
print("##################################################################################")
print("El miss rate promedio [%] con un tamaño de caché de 16kB es: ",
      GEOMEAN_Miss_rate_total_TC16, '#')
print("")
print("##################################################################################")
print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''' Tamaño de caché 32''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
print(tabla_TC32.to_string(index=False))
print("##################################################################################")
print("El miss rate promedio [%] con un tamaño de caché de 32kB es: ",
      GEOMEAN_Miss_rate_total_TC32, '#')
print("")
print("##################################################################################")
print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''' Tamaño de caché 64''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
print(tabla_TC64.to_string(index=False))
print("##################################################################################")
print("El miss rate promedio [%] con un tamaño de caché de 64kB es: ",
      GEOMEAN_Miss_rate_total_TC64, '#')
print("##################################################################################")
print("")
print("##################################################################################")
print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''' Tamaño de caché 128''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
print(tabla_TC128.to_string(index=False))
print("##################################################################################")
print("El miss rate promedio [%] con un tamaño de caché de 128kB es: ",
      GEOMEAN_Miss_rate_total_TC128, '#')
print("##################################################################################")
print("")
print("##################################################################################")
print("''''''''''''''''''''''''''' Miss rate total'''''''''''''''''''''''''''''")
print(tabla_miss_rate_total.to_string(index=False))
print("")
print("##################################################################################")
print("''''''''''''''''' Miss rate total 465.tonto-1769'''''''''''''''''''''")
print(tabla_miss_rate_total_465_tonto_1769B.to_string(index=False))
