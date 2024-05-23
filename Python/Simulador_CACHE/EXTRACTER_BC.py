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


#######################################################
# Extractor para experimento con tamaño de bloque 16kB#
#######################################################


# Creación de tablas para adjuntar valores
# Una tabla por tamaño
tabla_BC16 = pd.DataFrame(index=[
    '400.perlbench-41B', '401.bzip2-226B', '403.gcc-16B', '410.bwaves-1963B', '416.gamess-875B', '429.mcf-184B', '433.milc-127B',
    '435.gromacs-111B', '436.cactusADM-1804B', '437.leslie3d-134B', '444.namd-120B', '445.gobmk-17B',
    '450.soplex-247B', '453.povray-887B', '454.calculix-104B', '456.hmmer-191B', '458.sjeng-1088B', '459.GemsFDTD-1169B',
    '462.libquantum-1343B', '464.h264ref-30B', '465.tonto-1769B', '470.lbm-1274B', '471.omnetpp-188B', '473.astar-153B', '481.wrf-1170B',
    '482.sphinx3-1100B', '483.xalancbmk-127B'], columns=[
    'App', 'Total Misses', 'Miss rate total [%]', 'Misses lectura', 'Miss rate lectura [%]', 'Misses escritura', 'Miss rate escritura [%]'])
tabla_BC16['App'] = tabla_BC16.index

# Files paths
filename_1 = "RESULTS_BC/400BC16.txt"
filename_2 = "RESULTS_BC/401BC16.txt"
filename_3 = "RESULTS_BC/403BC16.txt"
filename_4 = "RESULTS_BC/410BC16.txt"
filename_5 = "RESULTS_BC/416BC16.txt"
filename_6 = "RESULTS_BC/429BC16.txt"
filename_7 = "RESULTS_BC/433BC16.txt"
filename_8 = "RESULTS_BC/435BC16.txt"
filename_9 = "RESULTS_BC/436BC16.txt"
filename_10 = "RESULTS_BC/437BC16.txt"
filename_11 = "RESULTS_BC/444BC16.txt"
filename_12 = "RESULTS_BC/445BC16.txt"
filename_13 = "RESULTS_BC/450BC16.txt"
filename_14 = "RESULTS_BC/453BC16.txt"
filename_15 = "RESULTS_BC/454BC16.txt"
filename_16 = "RESULTS_BC/456BC16.txt"
filename_17 = "RESULTS_BC/458BC16.txt"
filename_18 = "RESULTS_BC/459BC16.txt"
filename_19 = "RESULTS_BC/462BC16.txt"
filename_20 = "RESULTS_BC/464BC16.txt"
filename_21 = "RESULTS_BC/465BC16.txt"
filename_22 = "RESULTS_BC/470BC16.txt"
filename_23 = "RESULTS_BC/471BC16.txt"
filename_24 = "RESULTS_BC/473BC16.txt"
filename_25 = "RESULTS_BC/481BC16.txt"
filename_26 = "RESULTS_BC/482BC16.txt"
filename_27 = "RESULTS_BC/483BC16.txt"


# Content file extracter
with open(filename_1, 'r') as file:
    content_400BC16 = file.read()
with open(filename_2, 'r') as file:
    content_401BC16 = file.read()
with open(filename_3, 'r') as file:
    content_403BC16 = file.read()
with open(filename_4, 'r') as file:
    content_410BC16 = file.read()
with open(filename_5, 'r') as file:
    content_416BC16 = file.read()
with open(filename_6, 'r') as file:
    content_429BC16 = file.read()
with open(filename_7, 'r') as file:
    content_433BC16 = file.read()
with open(filename_8, 'r') as file:
    content_435BC16 = file.read()
with open(filename_9, 'r') as file:
    content_436BC16 = file.read()
with open(filename_10, 'r') as file:
    content_437BC16 = file.read()
with open(filename_11, 'r') as file:
    content_444BC16 = file.read()
with open(filename_12, 'r') as file:
    content_445BC16 = file.read()
with open(filename_13, 'r') as file:
    content_450BC16 = file.read()
with open(filename_14, 'r') as file:
    content_453BC16 = file.read()
with open(filename_15, 'r') as file:
    content_454BC16 = file.read()
with open(filename_16, 'r') as file:
    content_456BC16 = file.read()
with open(filename_17, 'r') as file:
    content_458BC16 = file.read()
with open(filename_18, 'r') as file:
    content_459BC16 = file.read()
with open(filename_19, 'r') as file:
    content_462BC16 = file.read()
with open(filename_20, 'r') as file:
    content_464BC16 = file.read()
with open(filename_21, 'r') as file:
    content_465BC16 = file.read()
with open(filename_22, 'r') as file:
    content_470BC16 = file.read()
with open(filename_23, 'r') as file:
    content_471BC16 = file.read()
with open(filename_24, 'r') as file:
    content_473BC16 = file.read()
with open(filename_25, 'r') as file:
    content_481BC16 = file.read()
with open(filename_26, 'r') as file:
    content_482BC16 = file.read()
with open(filename_27, 'r') as file:
    content_483BC16 = file.read()

# Variables según aplicación

# 400.pearlbench-41B
total_misses_400BC16 = re.search(
    r"Total_misses (\d+)", content_400BC16).group(1)
total_miss_rate_400BC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_400BC16).group(1)
total_read_misses_400BC16 = re.search(
    r"Total_read_misses (\d+)", content_400BC16).group(1)
total_read_miss_rate_400BC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_400BC16).group(1)
total_write_misses_400BC16 = re.search(
    r"Total_write_misses (\d+)", content_400BC16).group(1)
total_write_miss_rate_400BC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_400BC16).group(1)
print(">>>>>All BC16 400.pearlbench-41B variables where obtained successfully")

# 401.bzip2-226B
total_misses_401BC16 = re.search(
    r"Total_misses (\d+)", content_401BC16).group(1)
total_miss_rate_401BC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_401BC16).group(1)
total_read_misses_401BC16 = re.search(
    r"Total_read_misses (\d+)", content_401BC16).group(1)
total_read_miss_rate_401BC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_401BC16).group(1)
total_write_misses_401BC16 = re.search(
    r"Total_write_misses (\d+)", content_401BC16).group(1)
total_write_miss_rate_401BC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_401BC16).group(1)
print(">>>>>All BC16 401.bzip2-226B variables where obtained successfully")

# 403.gcc-16B
total_misses_403BC16 = re.search(
    r"Total_misses (\d+)", content_403BC16).group(1)
total_miss_rate_403BC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_403BC16).group(1)
total_read_misses_403BC16 = re.search(
    r"Total_read_misses (\d+)", content_403BC16).group(1)
total_read_miss_rate_403BC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_403BC16).group(1)
total_write_misses_403BC16 = re.search(
    r"Total_write_misses (\d+)", content_403BC16).group(1)
total_write_miss_rate_403BC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_403BC16).group(1)
print(">>>>>All BC16 403.gcc-16B variables where obtained successfully")

# 410.bwaves-1963B
total_misses_410BC16 = re.search(
    r"Total_misses (\d+)", content_410BC16).group(1)
total_miss_rate_410BC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_410BC16).group(1)
total_read_misses_410BC16 = re.search(
    r"Total_read_misses (\d+)", content_410BC16).group(1)
total_read_miss_rate_410BC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_410BC16).group(1)
total_write_misses_410BC16 = re.search(
    r"Total_write_misses (\d+)", content_410BC16).group(1)
total_write_miss_rate_410BC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_410BC16).group(1)
print(">>>>>All BC16 410.bwaves-1963B variables where obtained successfully")

# 416.gamess-875B
total_misses_416BC16 = re.search(
    r"Total_misses (\d+)", content_416BC16).group(1)
total_miss_rate_416BC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_416BC16).group(1)
total_read_misses_416BC16 = re.search(
    r"Total_read_misses (\d+)", content_416BC16).group(1)
total_read_miss_rate_416BC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_416BC16).group(1)
total_write_misses_416BC16 = re.search(
    r"Total_write_misses (\d+)", content_416BC16).group(1)
total_write_miss_rate_416BC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_416BC16).group(1)
print(">>>>>All BC16 416.gamess-875B variables where obtained successfully")

# 429.mcf-184B
total_misses_429BC16 = re.search(
    r"Total_misses (\d+)", content_429BC16).group(1)
total_miss_rate_429BC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_429BC16).group(1)
total_read_misses_429BC16 = re.search(
    r"Total_read_misses (\d+)", content_429BC16).group(1)
total_read_miss_rate_429BC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_429BC16).group(1)
total_write_misses_429BC16 = re.search(
    r"Total_write_misses (\d+)", content_429BC16).group(1)
total_write_miss_rate_429BC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_429BC16).group(1)
print(">>>>>All BC16 429.mcf-184B variables where obtained successfully")

# 433.milc-127B
total_misses_433BC16 = re.search(
    r"Total_misses (\d+)", content_433BC16).group(1)
total_miss_rate_433BC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_433BC16).group(1)
total_read_misses_433BC16 = re.search(
    r"Total_read_misses (\d+)", content_433BC16).group(1)
total_read_miss_rate_433BC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_433BC16).group(1)
total_write_misses_433BC16 = re.search(
    r"Total_write_misses (\d+)", content_433BC16).group(1)
total_write_miss_rate_433BC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_433BC16).group(1)
print(">>>>>All BC16 433.milc-127B variables where obtained successfully")

# 435.gromacs-111B
total_misses_435BC16 = re.search(
    r"Total_misses (\d+)", content_435BC16).group(1)
total_miss_rate_435BC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_435BC16).group(1)
total_read_misses_435BC16 = re.search(
    r"Total_read_misses (\d+)", content_435BC16).group(1)
total_read_miss_rate_435BC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_435BC16).group(1)
total_write_misses_435BC16 = re.search(
    r"Total_write_misses (\d+)", content_435BC16).group(1)
total_write_miss_rate_435BC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_435BC16).group(1)
print(">>>>>All BC16 435.gromacs-111B variables where obtained successfully")

# 436.cactusADM-1804B
total_misses_436BC16 = re.search(
    r"Total_misses (\d+)", content_436BC16).group(1)
total_miss_rate_436BC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_436BC16).group(1)
total_read_misses_436BC16 = re.search(
    r"Total_read_misses (\d+)", content_436BC16).group(1)
total_read_miss_rate_436BC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_436BC16).group(1)
total_write_misses_436BC16 = re.search(
    r"Total_write_misses (\d+)", content_436BC16).group(1)
total_write_miss_rate_436BC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_436BC16).group(1)
print(">>>>>All BC16 436.cactusADM-1804B variables where obtained successfully")

# 437.leslie3d-134B
total_misses_437BC16 = re.search(
    r"Total_misses (\d+)", content_437BC16).group(1)
total_miss_rate_437BC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_437BC16).group(1)
total_read_misses_437BC16 = re.search(
    r"Total_read_misses (\d+)", content_437BC16).group(1)
total_read_miss_rate_437BC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_437BC16).group(1)
total_write_misses_437BC16 = re.search(
    r"Total_write_misses (\d+)", content_437BC16).group(1)
total_write_miss_rate_437BC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_437BC16).group(1)
print(">>>>>All BC16 437.leslie3d-134B variables where obtained successfully")

# 444.namd-120B
total_misses_444BC16 = re.search(
    r"Total_misses (\d+)", content_444BC16).group(1)
total_miss_rate_444BC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_444BC16).group(1)
total_read_misses_444BC16 = re.search(
    r"Total_read_misses (\d+)", content_444BC16).group(1)
total_read_miss_rate_444BC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_444BC16).group(1)
total_write_misses_444BC16 = re.search(
    r"Total_write_misses (\d+)", content_444BC16).group(1)
total_write_miss_rate_444BC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_444BC16).group(1)
print(">>>>>All BC16 444.namd-120B variables where obtained successfully")

# 445.gobmk-17B
total_misses_445BC16 = re.search(
    r"Total_misses (\d+)", content_445BC16).group(1)
total_miss_rate_445BC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_445BC16).group(1)
total_read_misses_445BC16 = re.search(
    r"Total_read_misses (\d+)", content_445BC16).group(1)
total_read_miss_rate_445BC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_445BC16).group(1)
total_write_misses_445BC16 = re.search(
    r"Total_write_misses (\d+)", content_445BC16).group(1)
total_write_miss_rate_445BC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_445BC16).group(1)
print(">>>>>All BC16 445.gobmk-17B variables where obtained successfully")

# 450.soplex-247B
total_misses_450BC16 = re.search(
    r"Total_misses (\d+)", content_450BC16).group(1)
total_miss_rate_450BC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_450BC16).group(1)
total_read_misses_450BC16 = re.search(
    r"Total_read_misses (\d+)", content_450BC16).group(1)
total_read_miss_rate_450BC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_450BC16).group(1)
total_write_misses_450BC16 = re.search(
    r"Total_write_misses (\d+)", content_450BC16).group(1)
total_write_miss_rate_450BC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_450BC16).group(1)
print(">>>>>All BC16 450.soplex-247B variables where obtained successfully")

# 453.povray-887B
total_misses_453BC16 = re.search(
    r"Total_misses (\d+)", content_453BC16).group(1)
total_miss_rate_453BC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_453BC16).group(1)
total_read_misses_453BC16 = re.search(
    r"Total_read_misses (\d+)", content_453BC16).group(1)
total_read_miss_rate_453BC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_453BC16).group(1)
total_write_misses_453BC16 = re.search(
    r"Total_write_misses (\d+)", content_453BC16).group(1)
total_write_miss_rate_453BC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_453BC16).group(1)
print(">>>>>All BC16 453.povray-887B variables where obtained successfully")

# 454.calculix-104B
total_misses_454BC16 = re.search(
    r"Total_misses (\d+)", content_454BC16).group(1)
total_miss_rate_454BC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_454BC16).group(1)
total_read_misses_454BC16 = re.search(
    r"Total_read_misses (\d+)", content_454BC16).group(1)
total_read_miss_rate_454BC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_454BC16).group(1)
total_write_misses_454BC16 = re.search(
    r"Total_write_misses (\d+)", content_454BC16).group(1)
total_write_miss_rate_454BC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_454BC16).group(1)
print(">>>>>All BC16 454.calculix-104B variables where obtained successfully")

# 456.hmmer-191B
total_misses_456BC16 = re.search(
    r"Total_misses (\d+)", content_456BC16).group(1)
total_miss_rate_456BC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_456BC16).group(1)
total_read_misses_456BC16 = re.search(
    r"Total_read_misses (\d+)", content_456BC16).group(1)
total_read_miss_rate_456BC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_456BC16).group(1)
total_write_misses_456BC16 = re.search(
    r"Total_write_misses (\d+)", content_456BC16).group(1)
total_write_miss_rate_456BC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_456BC16).group(1)
print(">>>>>All BC16 456.hmmer-191B variables where obtained successfully")

# 458.sjeng-1088B
total_misses_458BC16 = re.search(
    r"Total_misses (\d+)", content_458BC16).group(1)
total_miss_rate_458BC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_458BC16).group(1)
total_read_misses_458BC16 = re.search(
    r"Total_read_misses (\d+)", content_458BC16).group(1)
total_read_miss_rate_458BC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_458BC16).group(1)
total_write_misses_458BC16 = re.search(
    r"Total_write_misses (\d+)", content_458BC16).group(1)
total_write_miss_rate_458BC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_458BC16).group(1)
print(">>>>>All BC16 458.sjeng-1088B variables where obtained successfully")

# 459.GemsFDTD-1169B
total_misses_459BC16 = re.search(
    r"Total_misses (\d+)", content_459BC16).group(1)
total_miss_rate_459BC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_459BC16).group(1)
total_read_misses_459BC16 = re.search(
    r"Total_read_misses (\d+)", content_459BC16).group(1)
total_read_miss_rate_459BC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_459BC16).group(1)
total_write_misses_459BC16 = re.search(
    r"Total_write_misses (\d+)", content_459BC16).group(1)
total_write_miss_rate_459BC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_459BC16).group(1)
print(">>>>>All BC16 459.GemsFDTD-1169B variables where obtained successfully")

# 462.libquantum-1343B
total_misses_462BC16 = re.search(
    r"Total_misses (\d+)", content_462BC16).group(1)
total_miss_rate_462BC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_462BC16).group(1)
total_read_misses_462BC16 = re.search(
    r"Total_read_misses (\d+)", content_462BC16).group(1)
total_read_miss_rate_462BC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_462BC16).group(1)
total_write_misses_462BC16 = re.search(
    r"Total_write_misses (\d+)", content_462BC16).group(1)
total_write_miss_rate_462BC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_462BC16).group(1)
print(">>>>>All BC16 462.libquantum-1343B variables where obtained successfully")

# 464.h264ref-30B
total_misses_464BC16 = re.search(
    r"Total_misses (\d+)", content_464BC16).group(1)
total_miss_rate_464BC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_464BC16).group(1)
total_read_misses_464BC16 = re.search(
    r"Total_read_misses (\d+)", content_464BC16).group(1)
total_read_miss_rate_464BC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_464BC16).group(1)
total_write_misses_464BC16 = re.search(
    r"Total_write_misses (\d+)", content_464BC16).group(1)
total_write_miss_rate_464BC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_464BC16).group(1)
print(">>>>>All BC16 464.h264ref-30B variables where obtained successfully")

# 465.tonto-1769B
total_misses_465BC16 = re.search(
    r"Total_misses (\d+)", content_465BC16).group(1)
total_miss_rate_465BC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_465BC16).group(1)
total_read_misses_465BC16 = re.search(
    r"Total_read_misses (\d+)", content_465BC16).group(1)
total_read_miss_rate_465BC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_465BC16).group(1)
total_write_misses_465BC16 = re.search(
    r"Total_write_misses (\d+)", content_465BC16).group(1)
total_write_miss_rate_465BC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_465BC16).group(1)
print(">>>>>All BC16 465.tonto-1769B variables where obtained successfully")

# 470.lbm-1274B
total_misses_470BC16 = re.search(
    r"Total_misses (\d+)", content_470BC16).group(1)
total_miss_rate_470BC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_470BC16).group(1)
total_read_misses_470BC16 = re.search(
    r"Total_read_misses (\d+)", content_470BC16).group(1)
total_read_miss_rate_470BC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_470BC16).group(1)
total_write_misses_470BC16 = re.search(
    r"Total_write_misses (\d+)", content_470BC16).group(1)
total_write_miss_rate_470BC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_470BC16).group(1)
print(">>>>>All BC16 470.lbm-1274B variables where obtained successfully")

# 471.omnetpp-188B
total_misses_471BC16 = re.search(
    r"Total_misses (\d+)", content_471BC16).group(1)
total_miss_rate_471BC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_471BC16).group(1)
total_read_misses_471BC16 = re.search(
    r"Total_read_misses (\d+)", content_471BC16).group(1)
total_read_miss_rate_471BC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_471BC16).group(1)
total_write_misses_471BC16 = re.search(
    r"Total_write_misses (\d+)", content_471BC16).group(1)
total_write_miss_rate_471BC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_471BC16).group(1)
print(">>>>>All BC16 471.omnetpp-188B variables where obtained successfully")

# 473.astar-153B
total_misses_473BC16 = re.search(
    r"Total_misses (\d+)", content_473BC16).group(1)
total_miss_rate_473BC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_473BC16).group(1)
total_read_misses_473BC16 = re.search(
    r"Total_read_misses (\d+)", content_473BC16).group(1)
total_read_miss_rate_473BC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_473BC16).group(1)
total_write_misses_473BC16 = re.search(
    r"Total_write_misses (\d+)", content_473BC16).group(1)
total_write_miss_rate_473BC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_473BC16).group(1)
print(">>>>>All BC16 473.astar-153B variables where obtained successfully")

# 481.wrf-1170B
total_misses_481BC16 = re.search(
    r"Total_misses (\d+)", content_481BC16).group(1)
total_miss_rate_481BC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_481BC16).group(1)
total_read_misses_481BC16 = re.search(
    r"Total_read_misses (\d+)", content_481BC16).group(1)
total_read_miss_rate_481BC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_481BC16).group(1)
total_write_misses_481BC16 = re.search(
    r"Total_write_misses (\d+)", content_481BC16).group(1)
total_write_miss_rate_481BC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_481BC16).group(1)
print(">>>>>All BC16 481.wrf-1170B variables where obtained successfully")

# 482.sphinx3-1100B
total_misses_482BC16 = re.search(
    r"Total_misses (\d+)", content_482BC16).group(1)
total_miss_rate_482BC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_482BC16).group(1)
total_read_misses_482BC16 = re.search(
    r"Total_read_misses (\d+)", content_482BC16).group(1)
total_read_miss_rate_482BC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_482BC16).group(1)
total_write_misses_482BC16 = re.search(
    r"Total_write_misses (\d+)", content_482BC16).group(1)
total_write_miss_rate_482BC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_482BC16).group(1)
print(">>>>>All BC16 482.sphinx3-1100B variables where obtained successfully")

# 483.xalancbmk-127B
total_misses_483BC16 = re.search(
    r"Total_misses (\d+)", content_483BC16).group(1)
total_miss_rate_483BC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_483BC16).group(1)
total_read_misses_483BC16 = re.search(
    r"Total_read_misses (\d+)", content_483BC16).group(1)
total_read_miss_rate_483BC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_483BC16).group(1)
total_write_misses_483BC16 = re.search(
    r"Total_write_misses (\d+)", content_483BC16).group(1)
total_write_miss_rate_483BC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_483BC16).group(1)
print(">>>>>All BC16 483.xalancbmk-127B variables where obtained successfully")


#############################
# Adjunta datos a dataframe #
#############################

# **400.perlbench-41B**

tabla_BC16.at['400.perlbench-41B', 'Total Misses'] = total_misses_400BC16

tabla_BC16.at['400.perlbench-41B',
              'Miss rate total [%]'] = total_miss_rate_400BC16

tabla_BC16.at['400.perlbench-41B',
              'Misses lectura'] = total_read_misses_400BC16

tabla_BC16.at['400.perlbench-41B',
              'Miss rate lectura [%]'] = total_read_miss_rate_400BC16

tabla_BC16.at['400.perlbench-41B',
              'Misses escritura'] = total_write_misses_400BC16

tabla_BC16.at['400.perlbench-41B',
              'Miss rate escritura [%]'] = total_write_miss_rate_400BC16

# **401.bzip2-226B**

tabla_BC16.at['401.bzip2-226B', 'Total Misses'] = total_misses_401BC16

tabla_BC16.at['401.bzip2-226B',
              'Miss rate total [%]'] = total_miss_rate_401BC16

tabla_BC16.at['401.bzip2-226B', 'Misses lectura'] = total_read_misses_401BC16

tabla_BC16.at['401.bzip2-226B',
              'Miss rate lectura [%]'] = total_read_miss_rate_401BC16

tabla_BC16.at['401.bzip2-226B',
              'Misses escritura'] = total_write_misses_401BC16

tabla_BC16.at['401.bzip2-226B',
              'Miss rate escritura [%]'] = total_write_miss_rate_401BC16

# **403.gcc-16B**

tabla_BC16.at['403.gcc-16B', 'Total Misses'] = total_misses_403BC16

tabla_BC16.at['403.gcc-16B', 'Miss rate total [%]'] = total_miss_rate_403BC16

tabla_BC16.at['403.gcc-16B', 'Misses lectura'] = total_read_misses_403BC16

tabla_BC16.at['403.gcc-16B',
              'Miss rate lectura [%]'] = total_read_miss_rate_403BC16

tabla_BC16.at['403.gcc-16B',
              'Misses escritura'] = total_write_misses_403BC16

tabla_BC16.at['403.gcc-16B',
              'Miss rate escritura [%]'] = total_write_miss_rate_403BC16

# **410.bwaves-1963B**

tabla_BC16.at['410.bwaves-1963B', 'Total Misses'] = total_misses_410BC16

tabla_BC16.at['410.bwaves-1963B',
              'Miss rate total [%]'] = total_miss_rate_410BC16

tabla_BC16.at['410.bwaves-1963B', 'Misses lectura'] = total_read_misses_410BC16

tabla_BC16.at['410.bwaves-1963B',
              'Miss rate lectura [%]'] = total_read_miss_rate_410BC16

tabla_BC16.at['410.bwaves-1963B',
              'Misses escritura'] = total_write_misses_410BC16

tabla_BC16.at['410.bwaves-1963B',
              'Miss rate escritura [%]'] = total_write_miss_rate_410BC16

# **416.gamess-875B**

tabla_BC16.at['416.gamess-875B', 'Total Misses'] = total_misses_416BC16

tabla_BC16.at['416.gamess-875B',
              'Miss rate total [%]'] = total_miss_rate_416BC16

tabla_BC16.at['416.gamess-875B', 'Misses lectura'] = total_read_misses_416BC16

tabla_BC16.at['416.gamess-875B',
              'Miss rate lectura [%]'] = total_read_miss_rate_416BC16

tabla_BC16.at['416.gamess-875B',
              'Misses escritura'] = total_write_misses_416BC16

tabla_BC16.at['416.gamess-875B',
              'Miss rate escritura [%]'] = total_write_miss_rate_416BC16

# **429.mcf-184B**

tabla_BC16.at['429.mcf-184B', 'Total Misses'] = total_misses_429BC16

tabla_BC16.at['429.mcf-184B', 'Miss rate total [%]'] = total_miss_rate_429BC16

tabla_BC16.at['429.mcf-184B', 'Misses lectura'] = total_read_misses_429BC16

tabla_BC16.at['429.mcf-184B',
              'Miss rate lectura [%]'] = total_read_miss_rate_429BC16

tabla_BC16.at['429.mcf-184B',
              'Misses escritura'] = total_write_misses_429BC16

tabla_BC16.at['429.mcf-184B',
              'Miss rate escritura [%]'] = total_write_miss_rate_429BC16

# **433.milc-127B**

tabla_BC16.at['433.milc-127B', 'Total Misses'] = total_misses_433BC16

tabla_BC16.at['433.milc-127B', 'Miss rate total [%]'] = total_miss_rate_433BC16

tabla_BC16.at['433.milc-127B', 'Misses lectura'] = total_read_misses_433BC16

tabla_BC16.at['433.milc-127B',
              'Miss rate lectura [%]'] = total_read_miss_rate_433BC16

tabla_BC16.at['433.milc-127B',
              'Misses escritura'] = total_write_misses_433BC16

tabla_BC16.at['433.milc-127B',
              'Miss rate escritura [%]'] = total_write_miss_rate_433BC16

# **435.gromacs-111B**

tabla_BC16.at['435.gromacs-111B', 'Total Misses'] = total_misses_435BC16

tabla_BC16.at['435.gromacs-111B',
              'Miss rate total [%]'] = total_miss_rate_435BC16

tabla_BC16.at['435.gromacs-111B', 'Misses lectura'] = total_read_misses_435BC16

tabla_BC16.at['435.gromacs-111B',
              'Miss rate lectura [%]'] = total_read_miss_rate_435BC16

tabla_BC16.at['435.gromacs-111B',
              'Misses escritura'] = total_write_misses_435BC16

tabla_BC16.at['435.gromacs-111B',
              'Miss rate escritura [%]'] = total_write_miss_rate_435BC16

# **436.cactusADM-1804B**

tabla_BC16.at['436.cactusADM-1804B', 'Total Misses'] = total_misses_436BC16

tabla_BC16.at['436.cactusADM-1804B',
              'Miss rate total [%]'] = total_miss_rate_436BC16

tabla_BC16.at['436.cactusADM-1804B',
              'Misses lectura'] = total_read_misses_436BC16

tabla_BC16.at['436.cactusADM-1804B',
              'Miss rate lectura [%]'] = total_read_miss_rate_436BC16

tabla_BC16.at['436.cactusADM-1804B',
              'Misses escritura'] = total_write_misses_436BC16

tabla_BC16.at['436.cactusADM-1804B',
              'Miss rate escritura [%]'] = total_write_miss_rate_436BC16

# **437.leslie3d-134B**

tabla_BC16.at['437.leslie3d-134B', 'Total Misses'] = total_misses_437BC16

tabla_BC16.at['437.leslie3d-134B',
              'Miss rate total [%]'] = total_miss_rate_437BC16

tabla_BC16.at['437.leslie3d-134B',
              'Misses lectura'] = total_read_misses_437BC16

tabla_BC16.at['437.leslie3d-134B',
              'Miss rate lectura [%]'] = total_read_miss_rate_437BC16

tabla_BC16.at['437.leslie3d-134B',
              'Misses escritura'] = total_write_misses_437BC16

tabla_BC16.at['437.leslie3d-134B',
              'Miss rate escritura [%]'] = total_write_miss_rate_437BC16

# **444.namd-120B**

tabla_BC16.at['444.namd-120B', 'Total Misses'] = total_misses_444BC16

tabla_BC16.at['444.namd-120B', 'Miss rate total [%]'] = total_miss_rate_444BC16

tabla_BC16.at['444.namd-120B', 'Misses lectura'] = total_read_misses_444BC16

tabla_BC16.at['444.namd-120B',
              'Miss rate lectura [%]'] = total_read_miss_rate_444BC16

tabla_BC16.at['444.namd-120B',
              'Misses escritura'] = total_write_misses_444BC16

tabla_BC16.at['444.namd-120B',
              'Miss rate escritura [%]'] = total_write_miss_rate_444BC16

# **445.gobmk-17B**

tabla_BC16.at['445.gobmk-17B', 'Total Misses'] = total_misses_445BC16

tabla_BC16.at['445.gobmk-17B', 'Miss rate total [%]'] = total_miss_rate_445BC16

tabla_BC16.at['445.gobmk-17B', 'Misses lectura'] = total_read_misses_445BC16

tabla_BC16.at['445.gobmk-17B',
              'Miss rate lectura [%]'] = total_read_miss_rate_445BC16

tabla_BC16.at['445.gobmk-17B',
              'Misses escritura'] = total_write_misses_445BC16

tabla_BC16.at['445.gobmk-17B',
              'Miss rate escritura [%]'] = total_write_miss_rate_445BC16

# **450.soplex-247B**

tabla_BC16.at['450.soplex-247B', 'Total Misses'] = total_misses_450BC16

tabla_BC16.at['450.soplex-247B',
              'Miss rate total [%]'] = total_miss_rate_450BC16

tabla_BC16.at['450.soplex-247B', 'Misses lectura'] = total_read_misses_450BC16

tabla_BC16.at['450.soplex-247B',
              'Miss rate lectura [%]'] = total_read_miss_rate_450BC16

tabla_BC16.at['450.soplex-247B',
              'Misses escritura'] = total_write_misses_450BC16

tabla_BC16.at['450.soplex-247B',
              'Miss rate escritura [%]'] = total_write_miss_rate_450BC16

# **453.povray-887B**

tabla_BC16.at['453.povray-887B', 'Total Misses'] = total_misses_453BC16

tabla_BC16.at['453.povray-887B',
              'Miss rate total [%]'] = total_miss_rate_453BC16

tabla_BC16.at['453.povray-887B', 'Misses lectura'] = total_read_misses_453BC16

tabla_BC16.at['453.povray-887B',
              'Miss rate lectura [%]'] = total_read_miss_rate_453BC16

tabla_BC16.at['453.povray-887B',
              'Misses escritura'] = total_write_misses_453BC16

tabla_BC16.at['453.povray-887B',
              'Miss rate escritura [%]'] = total_write_miss_rate_453BC16

# **454.calculix-104B**

tabla_BC16.at['454.calculix-104B', 'Total Misses'] = total_misses_454BC16

tabla_BC16.at['454.calculix-104B',
              'Miss rate total [%]'] = total_miss_rate_454BC16

tabla_BC16.at['454.calculix-104B',
              'Misses lectura'] = total_read_misses_454BC16

tabla_BC16.at['454.calculix-104B',
              'Miss rate lectura [%]'] = total_read_miss_rate_454BC16

tabla_BC16.at['454.calculix-104B',
              'Misses escritura'] = total_write_misses_454BC16

tabla_BC16.at['454.calculix-104B',
              'Miss rate escritura [%]'] = total_write_miss_rate_454BC16

# **456.hmmer-191B**

tabla_BC16.at['456.hmmer-191B', 'Total Misses'] = total_misses_456BC16

tabla_BC16.at['456.hmmer-191B',
              'Miss rate total [%]'] = total_miss_rate_456BC16

tabla_BC16.at['456.hmmer-191B', 'Misses lectura'] = total_read_misses_456BC16

tabla_BC16.at['456.hmmer-191B',
              'Miss rate lectura [%]'] = total_read_miss_rate_456BC16

tabla_BC16.at['456.hmmer-191B',
              'Misses escritura'] = total_write_misses_456BC16

tabla_BC16.at['456.hmmer-191B',
              'Miss rate escritura [%]'] = total_write_miss_rate_456BC16

# **458.sjeng-1088B**

tabla_BC16.at['458.sjeng-1088B', 'Total Misses'] = total_misses_458BC16

tabla_BC16.at['458.sjeng-1088B',
              'Miss rate total [%]'] = total_miss_rate_458BC16

tabla_BC16.at['458.sjeng-1088B', 'Misses lectura'] = total_read_misses_458BC16

tabla_BC16.at['458.sjeng-1088B',
              'Miss rate lectura [%]'] = total_read_miss_rate_458BC16

tabla_BC16.at['458.sjeng-1088B',
              'Misses escritura'] = total_write_misses_458BC16

tabla_BC16.at['458.sjeng-1088B',
              'Miss rate escritura [%]'] = total_write_miss_rate_458BC16

# **459.GemsFDTD-1169B**

tabla_BC16.at['459.GemsFDTD-1169B', 'Total Misses'] = total_misses_459BC16

tabla_BC16.at['459.GemsFDTD-1169B',
              'Miss rate total [%]'] = total_miss_rate_459BC16

tabla_BC16.at['459.GemsFDTD-1169B',
              'Misses lectura'] = total_read_misses_459BC16

tabla_BC16.at['459.GemsFDTD-1169B',
              'Miss rate lectura [%]'] = total_read_miss_rate_459BC16

tabla_BC16.at['459.GemsFDTD-1169B',
              'Misses escritura'] = total_write_misses_459BC16

tabla_BC16.at['459.GemsFDTD-1169B',
              'Miss rate escritura [%]'] = total_write_miss_rate_459BC16

# **462.libquantum-1343B**

tabla_BC16.at['462.libquantum-1343B', 'Total Misses'] = total_misses_462BC16

tabla_BC16.at['462.libquantum-1343B',
              'Miss rate total [%]'] = total_miss_rate_462BC16

tabla_BC16.at['462.libquantum-1343B',
              'Misses lectura'] = total_read_misses_462BC16

tabla_BC16.at['462.libquantum-1343B',
              'Miss rate lectura [%]'] = total_read_miss_rate_462BC16

tabla_BC16.at['462.libquantum-1343B',
              'Misses escritura'] = total_write_misses_462BC16

tabla_BC16.at['462.libquantum-1343B',
              'Miss rate escritura [%]'] = total_write_miss_rate_462BC16

# **464.h264ref-30B**

tabla_BC16.at['464.h264ref-30B', 'Total Misses'] = total_misses_464BC16

tabla_BC16.at['464.h264ref-30B',
              'Miss rate total [%]'] = total_miss_rate_464BC16

tabla_BC16.at['464.h264ref-30B', 'Misses lectura'] = total_read_misses_464BC16

tabla_BC16.at['464.h264ref-30B',
              'Miss rate lectura [%]'] = total_read_miss_rate_464BC16

tabla_BC16.at['464.h264ref-30B',
              'Misses escritura'] = total_write_misses_464BC16

tabla_BC16.at['464.h264ref-30B',
              'Miss rate escritura [%]'] = total_write_miss_rate_464BC16

# **465.tonto-1769B**

tabla_BC16.at['465.tonto-1769B', 'Total Misses'] = total_misses_465BC16

tabla_BC16.at['465.tonto-1769B',
              'Miss rate total [%]'] = total_miss_rate_465BC16

tabla_BC16.at['465.tonto-1769B', 'Misses lectura'] = total_read_misses_465BC16

tabla_BC16.at['465.tonto-1769B',
              'Miss rate lectura [%]'] = total_read_miss_rate_465BC16

tabla_BC16.at['465.tonto-1769B',
              'Misses escritura'] = total_write_misses_465BC16

tabla_BC16.at['465.tonto-1769B',
              'Miss rate escritura [%]'] = total_write_miss_rate_465BC16

# **470.lbm-1274B**

tabla_BC16.at['470.lbm-1274B', 'Total Misses'] = total_misses_470BC16

tabla_BC16.at['470.lbm-1274B', 'Miss rate total [%]'] = total_miss_rate_470BC16

tabla_BC16.at['470.lbm-1274B', 'Misses lectura'] = total_read_misses_470BC16

tabla_BC16.at['470.lbm-1274B',
              'Miss rate lectura [%]'] = total_read_miss_rate_470BC16

tabla_BC16.at['470.lbm-1274B',
              'Misses escritura'] = total_write_misses_470BC16

tabla_BC16.at['470.lbm-1274B',
              'Miss rate escritura [%]'] = total_write_miss_rate_470BC16

# **471.omnetpp-188B**

tabla_BC16.at['471.omnetpp-188B', 'Total Misses'] = total_misses_471BC16

tabla_BC16.at['471.omnetpp-188B',
              'Miss rate total [%]'] = total_miss_rate_471BC16

tabla_BC16.at['471.omnetpp-188B', 'Misses lectura'] = total_read_misses_471BC16

tabla_BC16.at['471.omnetpp-188B',
              'Miss rate lectura [%]'] = total_read_miss_rate_471BC16

tabla_BC16.at['471.omnetpp-188B',
              'Misses escritura'] = total_write_misses_471BC16

tabla_BC16.at['471.omnetpp-188B',
              'Miss rate escritura [%]'] = total_write_miss_rate_471BC16

# **473.astar-153B**

tabla_BC16.at['473.astar-153B', 'Total Misses'] = total_misses_473BC16

tabla_BC16.at['473.astar-153B',
              'Miss rate total [%]'] = total_miss_rate_473BC16

tabla_BC16.at['473.astar-153B', 'Misses lectura'] = total_read_misses_473BC16

tabla_BC16.at['473.astar-153B',
              'Miss rate lectura [%]'] = total_read_miss_rate_473BC16

tabla_BC16.at['473.astar-153B',
              'Misses escritura'] = total_write_misses_473BC16

tabla_BC16.at['473.astar-153B',
              'Miss rate escritura [%]'] = total_write_miss_rate_473BC16

# **481.wrf-1170B**

tabla_BC16.at['481.wrf-1170B', 'Total Misses'] = total_misses_481BC16

tabla_BC16.at['481.wrf-1170B', 'Miss rate total [%]'] = total_miss_rate_481BC16

tabla_BC16.at['481.wrf-1170B', 'Misses lectura'] = total_read_misses_481BC16

tabla_BC16.at['481.wrf-1170B',
              'Miss rate lectura [%]'] = total_read_miss_rate_481BC16

tabla_BC16.at['481.wrf-1170B',
              'Misses escritura'] = total_write_misses_481BC16

tabla_BC16.at['481.wrf-1170B',
              'Miss rate escritura [%]'] = total_write_miss_rate_481BC16

# **482.sphinx3-1100B**

tabla_BC16.at['482.sphinx3-1100B', 'Total Misses'] = total_misses_482BC16

tabla_BC16.at['482.sphinx3-1100B',
              'Miss rate total [%]'] = total_miss_rate_482BC16

tabla_BC16.at['482.sphinx3-1100B',
              'Misses lectura'] = total_read_misses_482BC16

tabla_BC16.at['482.sphinx3-1100B',
              'Miss rate lectura [%]'] = total_read_miss_rate_482BC16

tabla_BC16.at['482.sphinx3-1100B',
              'Misses escritura'] = total_write_misses_482BC16

tabla_BC16.at['482.sphinx3-1100B',
              'Miss rate escritura [%]'] = total_write_miss_rate_482BC16

# **483.xalancbmk-127B**

tabla_BC16.at['483.xalancbmk-127B', 'Total Misses'] = total_misses_483BC16

tabla_BC16.at['483.xalancbmk-127B',
              'Miss rate total [%]'] = total_miss_rate_483BC16

tabla_BC16.at['483.xalancbmk-127B',
              'Misses lectura'] = total_read_misses_483BC16

tabla_BC16.at['483.xalancbmk-127B',
              'Miss rate lectura [%]'] = total_read_miss_rate_483BC16

tabla_BC16.at['483.xalancbmk-127B',
              'Misses escritura'] = total_write_misses_483BC16

tabla_BC16.at['483.xalancbmk-127B',
              'Miss rate escritura [%]'] = total_write_miss_rate_483BC16

print(">>>>>All BC16 data has been uploaded successfully")

#######################################################
# Extractor para experimento con tamaño de bloque 32kB#
#######################################################

# Creación de tablas para adjuntar valores
# Una tabla por tamaño
tabla_BC32 = pd.DataFrame(index=[
    '400.perlbench-41B', '401.bzip2-226B', '403.gcc-16B', '410.bwaves-1963B', '416.gamess-875B', '429.mcf-184B', '433.milc-127B',
    '435.gromacs-111B', '436.cactusADM-1804B', '437.leslie3d-134B', '444.namd-120B', '445.gobmk-17B',
    '450.soplex-247B', '453.povray-887B', '454.calculix-104B', '456.hmmer-191B', '458.sjeng-1088B', '459.GemsFDTD-1169B',
    '462.libquantum-1343B', '464.h264ref-30B', '465.tonto-1769B', '470.lbm-1274B', '471.omnetpp-188B', '473.astar-153B', '481.wrf-1170B',
    '482.sphinx3-1100B', '483.xalancbmk-127B'], columns=[
    'App', 'Total Misses', 'Miss rate total [%]', 'Misses lectura', 'Miss rate lectura [%]', 'Misses escritura', 'Miss rate escritura [%]'])
tabla_BC32['App'] = tabla_BC32.index

# Files paths
filename_28 = "RESULTS_BC/400BC32.txt"
filename_29 = "RESULTS_BC/401BC32.txt"
filename_30 = "RESULTS_BC/403BC32.txt"
filename_31 = "RESULTS_BC/410BC32.txt"
filename_32 = "RESULTS_BC/416BC32.txt"
filename_33 = "RESULTS_BC/429BC32.txt"
filename_34 = "RESULTS_BC/433BC32.txt"
filename_35 = "RESULTS_BC/435BC32.txt"
filename_36 = "RESULTS_BC/436BC32.txt"
filename_37 = "RESULTS_BC/437BC32.txt"
filename_38 = "RESULTS_BC/444BC32.txt"
filename_39 = "RESULTS_BC/445BC32.txt"
filename_40 = "RESULTS_BC/450BC32.txt"
filename_41 = "RESULTS_BC/453BC32.txt"
filename_42 = "RESULTS_BC/454BC32.txt"
filename_43 = "RESULTS_BC/456BC32.txt"
filename_44 = "RESULTS_BC/458BC32.txt"
filename_45 = "RESULTS_BC/459BC32.txt"
filename_46 = "RESULTS_BC/462BC32.txt"
filename_47 = "RESULTS_BC/464BC32.txt"
filename_48 = "RESULTS_BC/465BC32.txt"
filename_49 = "RESULTS_BC/470BC32.txt"
filename_50 = "RESULTS_BC/471BC32.txt"
filename_51 = "RESULTS_BC/473BC32.txt"
filename_52 = "RESULTS_BC/481BC32.txt"
filename_53 = "RESULTS_BC/482BC32.txt"
filename_54 = "RESULTS_BC/483BC32.txt"


# Content file extracter
with open(filename_28, 'r') as file:
    content_400BC32 = file.read()
with open(filename_29, 'r') as file:
    content_401BC32 = file.read()
with open(filename_30, 'r') as file:
    content_403BC32 = file.read()
with open(filename_31, 'r') as file:
    content_410BC32 = file.read()
with open(filename_32, 'r') as file:
    content_416BC32 = file.read()
with open(filename_33, 'r') as file:
    content_429BC32 = file.read()
with open(filename_34, 'r') as file:
    content_433BC32 = file.read()
with open(filename_35, 'r') as file:
    content_435BC32 = file.read()
with open(filename_36, 'r') as file:
    content_436BC32 = file.read()
with open(filename_37, 'r') as file:
    content_437BC32 = file.read()
with open(filename_38, 'r') as file:
    content_444BC32 = file.read()
with open(filename_39, 'r') as file:
    content_445BC32 = file.read()
with open(filename_40, 'r') as file:
    content_450BC32 = file.read()
with open(filename_41, 'r') as file:
    content_453BC32 = file.read()
with open(filename_42, 'r') as file:
    content_454BC32 = file.read()
with open(filename_43, 'r') as file:
    content_456BC32 = file.read()
with open(filename_44, 'r') as file:
    content_458BC32 = file.read()
with open(filename_45, 'r') as file:
    content_459BC32 = file.read()
with open(filename_46, 'r') as file:
    content_462BC32 = file.read()
with open(filename_47, 'r') as file:
    content_464BC32 = file.read()
with open(filename_48, 'r') as file:
    content_465BC32 = file.read()
with open(filename_49, 'r') as file:
    content_470BC32 = file.read()
with open(filename_50, 'r') as file:
    content_471BC32 = file.read()
with open(filename_51, 'r') as file:
    content_473BC32 = file.read()
with open(filename_52, 'r') as file:
    content_481BC32 = file.read()
with open(filename_53, 'r') as file:
    content_482BC32 = file.read()
with open(filename_54, 'r') as file:
    content_483BC32 = file.read()


# Variables según aplicación

# 400.pearlbench-41B
total_misses_400BC32 = re.search(
    r"Total_misses (\d+)", content_400BC32).group(1)
total_miss_rate_400BC32 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_400BC32).group(1)
total_read_misses_400BC32 = re.search(
    r"Total_read_misses (\d+)", content_400BC32).group(1)
total_read_miss_rate_400BC32 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_400BC32).group(1)
total_write_misses_400BC32 = re.search(
    r"Total_write_misses (\d+)", content_400BC32).group(1)
total_write_miss_rate_400BC32 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_400BC32).group(1)
print(">>>>>All BC32 400.pearlbench-41B variables where obtained successfully")

# 401.bzip2-226B
total_misses_401BC32 = re.search(
    r"Total_misses (\d+)", content_401BC32).group(1)
total_miss_rate_401BC32 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_401BC32).group(1)
total_read_misses_401BC32 = re.search(
    r"Total_read_misses (\d+)", content_401BC32).group(1)
total_read_miss_rate_401BC32 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_401BC32).group(1)
total_write_misses_401BC32 = re.search(
    r"Total_write_misses (\d+)", content_401BC32).group(1)
total_write_miss_rate_401BC32 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_401BC32).group(1)
print(">>>>>All BC32 401.bzip2-226B variables where obtained successfully")

# 403.gcc-16B
total_misses_403BC32 = re.search(
    r"Total_misses (\d+)", content_403BC32).group(1)
total_miss_rate_403BC32 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_403BC32).group(1)
total_read_misses_403BC32 = re.search(
    r"Total_read_misses (\d+)", content_403BC32).group(1)
total_read_miss_rate_403BC32 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_403BC32).group(1)
total_write_misses_403BC32 = re.search(
    r"Total_write_misses (\d+)", content_403BC32).group(1)
total_write_miss_rate_403BC32 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_403BC32).group(1)
print(">>>>>All BC32 403.gcc-16B variables where obtained successfully")

# 410.bwaves-1963B
total_misses_410BC32 = re.search(
    r"Total_misses (\d+)", content_410BC32).group(1)
total_miss_rate_410BC32 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_410BC32).group(1)
total_read_misses_410BC32 = re.search(
    r"Total_read_misses (\d+)", content_410BC32).group(1)
total_read_miss_rate_410BC32 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_410BC32).group(1)
total_write_misses_410BC32 = re.search(
    r"Total_write_misses (\d+)", content_410BC32).group(1)
total_write_miss_rate_410BC32 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_410BC32).group(1)
print(">>>>>All BC32 410.bwaves-1963B variables where obtained successfully")

# 416.gamess-875B
total_misses_416BC32 = re.search(
    r"Total_misses (\d+)", content_416BC32).group(1)
total_miss_rate_416BC32 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_416BC32).group(1)
total_read_misses_416BC32 = re.search(
    r"Total_read_misses (\d+)", content_416BC32).group(1)
total_read_miss_rate_416BC32 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_416BC32).group(1)
total_write_misses_416BC32 = re.search(
    r"Total_write_misses (\d+)", content_416BC32).group(1)
total_write_miss_rate_416BC32 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_416BC32).group(1)
print(">>>>>All BC32 416.gamess-875B variables where obtained successfully")

# 429.mcf-184B
total_misses_429BC32 = re.search(
    r"Total_misses (\d+)", content_429BC32).group(1)
total_miss_rate_429BC32 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_429BC32).group(1)
total_read_misses_429BC32 = re.search(
    r"Total_read_misses (\d+)", content_429BC32).group(1)
total_read_miss_rate_429BC32 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_429BC32).group(1)
total_write_misses_429BC32 = re.search(
    r"Total_write_misses (\d+)", content_429BC32).group(1)
total_write_miss_rate_429BC32 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_429BC32).group(1)
print(">>>>>All BC32 429.mcf-184B variables where obtained successfully")

# 433.milc-127B
total_misses_433BC32 = re.search(
    r"Total_misses (\d+)", content_433BC32).group(1)
total_miss_rate_433BC32 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_433BC32).group(1)
total_read_misses_433BC32 = re.search(
    r"Total_read_misses (\d+)", content_433BC32).group(1)
total_read_miss_rate_433BC32 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_433BC32).group(1)
total_write_misses_433BC32 = re.search(
    r"Total_write_misses (\d+)", content_433BC32).group(1)
total_write_miss_rate_433BC32 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_433BC32).group(1)
print(">>>>>All BC32 433.milc-127B variables where obtained successfully")

# 435.gromacs-111B
total_misses_435BC32 = re.search(
    r"Total_misses (\d+)", content_435BC32).group(1)
total_miss_rate_435BC32 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_435BC32).group(1)
total_read_misses_435BC32 = re.search(
    r"Total_read_misses (\d+)", content_435BC32).group(1)
total_read_miss_rate_435BC32 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_435BC32).group(1)
total_write_misses_435BC32 = re.search(
    r"Total_write_misses (\d+)", content_435BC32).group(1)
total_write_miss_rate_435BC32 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_435BC32).group(1)
print(">>>>>All BC32 435.gromacs-111B variables where obtained successfully")

# 436.cactusADM-1804B
total_misses_436BC32 = re.search(
    r"Total_misses (\d+)", content_436BC32).group(1)
total_miss_rate_436BC32 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_436BC32).group(1)
total_read_misses_436BC32 = re.search(
    r"Total_read_misses (\d+)", content_436BC32).group(1)
total_read_miss_rate_436BC32 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_436BC32).group(1)
total_write_misses_436BC32 = re.search(
    r"Total_write_misses (\d+)", content_436BC32).group(1)
total_write_miss_rate_436BC32 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_436BC32).group(1)
print(">>>>>All BC32 436.cactusADM-1804B variables where obtained successfully")

# 437.leslie3d-134B
total_misses_437BC32 = re.search(
    r"Total_misses (\d+)", content_437BC32).group(1)
total_miss_rate_437BC32 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_437BC32).group(1)
total_read_misses_437BC32 = re.search(
    r"Total_read_misses (\d+)", content_437BC32).group(1)
total_read_miss_rate_437BC32 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_437BC32).group(1)
total_write_misses_437BC32 = re.search(
    r"Total_write_misses (\d+)", content_437BC32).group(1)
total_write_miss_rate_437BC32 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_437BC32).group(1)
print(">>>>>All BC32 437.leslie3d-134B variables where obtained successfully")

# 444.namd-120B
total_misses_444BC32 = re.search(
    r"Total_misses (\d+)", content_444BC32).group(1)
total_miss_rate_444BC32 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_444BC32).group(1)
total_read_misses_444BC32 = re.search(
    r"Total_read_misses (\d+)", content_444BC32).group(1)
total_read_miss_rate_444BC32 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_444BC32).group(1)
total_write_misses_444BC32 = re.search(
    r"Total_write_misses (\d+)", content_444BC32).group(1)
total_write_miss_rate_444BC32 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_444BC32).group(1)
print(">>>>>All BC32 444.namd-120B variables where obtained successfully")

# 445.gobmk-17B
total_misses_445BC32 = re.search(
    r"Total_misses (\d+)", content_445BC32).group(1)
total_miss_rate_445BC32 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_445BC32).group(1)
total_read_misses_445BC32 = re.search(
    r"Total_read_misses (\d+)", content_445BC32).group(1)
total_read_miss_rate_445BC32 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_445BC32).group(1)
total_write_misses_445BC32 = re.search(
    r"Total_write_misses (\d+)", content_445BC32).group(1)
total_write_miss_rate_445BC32 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_445BC32).group(1)
print(">>>>>All BC32 445.gobmk-17B variables where obtained successfully")

# 450.soplex-247B
total_misses_450BC32 = re.search(
    r"Total_misses (\d+)", content_450BC32).group(1)
total_miss_rate_450BC32 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_450BC32).group(1)
total_read_misses_450BC32 = re.search(
    r"Total_read_misses (\d+)", content_450BC32).group(1)
total_read_miss_rate_450BC32 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_450BC32).group(1)
total_write_misses_450BC32 = re.search(
    r"Total_write_misses (\d+)", content_450BC32).group(1)
total_write_miss_rate_450BC32 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_450BC32).group(1)
print(">>>>>All BC32 450.soplex-247B variables where obtained successfully")

# 453.povray-887B
total_misses_453BC32 = re.search(
    r"Total_misses (\d+)", content_453BC32).group(1)
total_miss_rate_453BC32 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_453BC32).group(1)
total_read_misses_453BC32 = re.search(
    r"Total_read_misses (\d+)", content_453BC32).group(1)
total_read_miss_rate_453BC32 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_453BC32).group(1)
total_write_misses_453BC32 = re.search(
    r"Total_write_misses (\d+)", content_453BC32).group(1)
total_write_miss_rate_453BC32 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_453BC32).group(1)
print(">>>>>All BC32 453.povray-887B variables where obtained successfully")

# 454.calculix-104B
total_misses_454BC32 = re.search(
    r"Total_misses (\d+)", content_454BC32).group(1)
total_miss_rate_454BC32 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_454BC32).group(1)
total_read_misses_454BC32 = re.search(
    r"Total_read_misses (\d+)", content_454BC32).group(1)
total_read_miss_rate_454BC32 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_454BC32).group(1)
total_write_misses_454BC32 = re.search(
    r"Total_write_misses (\d+)", content_454BC32).group(1)
total_write_miss_rate_454BC32 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_454BC32).group(1)
print(">>>>>All BC32 454.calculix-104B variables where obtained successfully")

# 456.hmmer-191B
total_misses_456BC32 = re.search(
    r"Total_misses (\d+)", content_456BC32).group(1)
total_miss_rate_456BC32 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_456BC32).group(1)
total_read_misses_456BC32 = re.search(
    r"Total_read_misses (\d+)", content_456BC32).group(1)
total_read_miss_rate_456BC32 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_456BC32).group(1)
total_write_misses_456BC32 = re.search(
    r"Total_write_misses (\d+)", content_456BC32).group(1)
total_write_miss_rate_456BC32 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_456BC32).group(1)
print(">>>>>All BC32 456.hmmer-191B variables where obtained successfully")

# 458.sjeng-1088B
total_misses_458BC32 = re.search(
    r"Total_misses (\d+)", content_458BC32).group(1)
total_miss_rate_458BC32 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_458BC32).group(1)
total_read_misses_458BC32 = re.search(
    r"Total_read_misses (\d+)", content_458BC32).group(1)
total_read_miss_rate_458BC32 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_458BC32).group(1)
total_write_misses_458BC32 = re.search(
    r"Total_write_misses (\d+)", content_458BC32).group(1)
total_write_miss_rate_458BC32 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_458BC32).group(1)
print(">>>>>All BC32 458.sjeng-1088B variables where obtained successfully")

# 459.GemsFDTD-1169B
total_misses_459BC32 = re.search(
    r"Total_misses (\d+)", content_459BC32).group(1)
total_miss_rate_459BC32 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_459BC32).group(1)
total_read_misses_459BC32 = re.search(
    r"Total_read_misses (\d+)", content_459BC32).group(1)
total_read_miss_rate_459BC32 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_459BC32).group(1)
total_write_misses_459BC32 = re.search(
    r"Total_write_misses (\d+)", content_459BC32).group(1)
total_write_miss_rate_459BC32 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_459BC32).group(1)
print(">>>>>All BC32 459.GemsFDTD-1169B variables where obtained successfully")

# 462.libquantum-1343B
total_misses_462BC32 = re.search(
    r"Total_misses (\d+)", content_462BC32).group(1)
total_miss_rate_462BC32 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_462BC32).group(1)
total_read_misses_462BC32 = re.search(
    r"Total_read_misses (\d+)", content_462BC32).group(1)
total_read_miss_rate_462BC32 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_462BC32).group(1)
total_write_misses_462BC32 = re.search(
    r"Total_write_misses (\d+)", content_462BC32).group(1)
total_write_miss_rate_462BC32 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_462BC32).group(1)
print(">>>>>All BC32 462.libquantum-1343B variables where obtained successfully")

# 464.h264ref-30B
total_misses_464BC32 = re.search(
    r"Total_misses (\d+)", content_464BC32).group(1)
total_miss_rate_464BC32 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_464BC32).group(1)
total_read_misses_464BC32 = re.search(
    r"Total_read_misses (\d+)", content_464BC32).group(1)
total_read_miss_rate_464BC32 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_464BC32).group(1)
total_write_misses_464BC32 = re.search(
    r"Total_write_misses (\d+)", content_464BC32).group(1)
total_write_miss_rate_464BC32 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_464BC32).group(1)
print(">>>>>All BC32 464.h264ref-30B variables where obtained successfully")

# 465.tonto-1769B
total_misses_465BC32 = re.search(
    r"Total_misses (\d+)", content_465BC32).group(1)
total_miss_rate_465BC32 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_465BC32).group(1)
total_read_misses_465BC32 = re.search(
    r"Total_read_misses (\d+)", content_465BC32).group(1)
total_read_miss_rate_465BC32 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_465BC32).group(1)
total_write_misses_465BC32 = re.search(
    r"Total_write_misses (\d+)", content_465BC32).group(1)
total_write_miss_rate_465BC32 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_465BC32).group(1)
print(">>>>>All BC32 465.tonto-1769B variables where obtained successfully")

# 470.lbm-1274B
total_misses_470BC32 = re.search(
    r"Total_misses (\d+)", content_470BC32).group(1)
total_miss_rate_470BC32 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_470BC32).group(1)
total_read_misses_470BC32 = re.search(
    r"Total_read_misses (\d+)", content_470BC32).group(1)
total_read_miss_rate_470BC32 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_470BC32).group(1)
total_write_misses_470BC32 = re.search(
    r"Total_write_misses (\d+)", content_470BC32).group(1)
total_write_miss_rate_470BC32 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_470BC32).group(1)
print(">>>>>All BC32 470.lbm-1274B variables where obtained successfully")

# 471.omnetpp-188B
total_misses_471BC32 = re.search(
    r"Total_misses (\d+)", content_471BC32).group(1)
total_miss_rate_471BC32 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_471BC32).group(1)
total_read_misses_471BC32 = re.search(
    r"Total_read_misses (\d+)", content_471BC32).group(1)
total_read_miss_rate_471BC32 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_471BC32).group(1)
total_write_misses_471BC32 = re.search(
    r"Total_write_misses (\d+)", content_471BC32).group(1)
total_write_miss_rate_471BC32 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_471BC32).group(1)
print(">>>>>All BC32 471.omnetpp-188B variables where obtained successfully")

# 473.astar-153B
total_misses_473BC32 = re.search(
    r"Total_misses (\d+)", content_473BC32).group(1)
total_miss_rate_473BC32 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_473BC32).group(1)
total_read_misses_473BC32 = re.search(
    r"Total_read_misses (\d+)", content_473BC32).group(1)
total_read_miss_rate_473BC32 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_473BC32).group(1)
total_write_misses_473BC32 = re.search(
    r"Total_write_misses (\d+)", content_473BC32).group(1)
total_write_miss_rate_473BC32 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_473BC32).group(1)
print(">>>>>All BC32 473.astar-153B variables where obtained successfully")

# 481.wrf-1170B
total_misses_481BC32 = re.search(
    r"Total_misses (\d+)", content_481BC32).group(1)
total_miss_rate_481BC32 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_481BC32).group(1)
total_read_misses_481BC32 = re.search(
    r"Total_read_misses (\d+)", content_481BC32).group(1)
total_read_miss_rate_481BC32 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_481BC32).group(1)
total_write_misses_481BC32 = re.search(
    r"Total_write_misses (\d+)", content_481BC32).group(1)
total_write_miss_rate_481BC32 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_481BC32).group(1)
print(">>>>>All BC32 481.wrf-1170B variables where obtained successfully")

# 482.sphinx3-1100B
total_misses_482BC32 = re.search(
    r"Total_misses (\d+)", content_482BC32).group(1)
total_miss_rate_482BC32 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_482BC32).group(1)
total_read_misses_482BC32 = re.search(
    r"Total_read_misses (\d+)", content_482BC32).group(1)
total_read_miss_rate_482BC32 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_482BC32).group(1)
total_write_misses_482BC32 = re.search(
    r"Total_write_misses (\d+)", content_482BC32).group(1)
total_write_miss_rate_482BC32 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_482BC32).group(1)
print(">>>>>All BC32 482.sphinx3-1100B variables where obtained successfully")

# 483.xalancbmk-127B
total_misses_483BC32 = re.search(
    r"Total_misses (\d+)", content_483BC32).group(1)
total_miss_rate_483BC32 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_483BC32).group(1)
total_read_misses_483BC32 = re.search(
    r"Total_read_misses (\d+)", content_483BC32).group(1)
total_read_miss_rate_483BC32 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_483BC32).group(1)
total_write_misses_483BC32 = re.search(
    r"Total_write_misses (\d+)", content_483BC32).group(1)
total_write_miss_rate_483BC32 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_483BC32).group(1)
print(">>>>>All BC32 483.xalancbmk-127B variables where obtained successfully")

#############################
# Adjunta datos a dataframe #
#############################

# **400.perlbench-41B**

tabla_BC32.at['400.perlbench-41B', 'Total Misses'] = total_misses_400BC32

tabla_BC32.at['400.perlbench-41B',
              'Miss rate total [%]'] = total_miss_rate_400BC32

tabla_BC32.at['400.perlbench-41B',
              'Misses lectura'] = total_read_misses_400BC32

tabla_BC32.at['400.perlbench-41B',
              'Miss rate lectura [%]'] = total_read_miss_rate_400BC32

tabla_BC32.at['400.perlbench-41B',
              'Misses escritura'] = total_write_misses_400BC32

tabla_BC32.at['400.perlbench-41B',
              'Miss rate escritura [%]'] = total_write_miss_rate_400BC32

# **401.bzip2-226B**

tabla_BC32.at['401.bzip2-226B', 'Total Misses'] = total_misses_401BC32

tabla_BC32.at['401.bzip2-226B',
              'Miss rate total [%]'] = total_miss_rate_401BC32

tabla_BC32.at['401.bzip2-226B', 'Misses lectura'] = total_read_misses_401BC32

tabla_BC32.at['401.bzip2-226B',
              'Miss rate lectura [%]'] = total_read_miss_rate_401BC32

tabla_BC32.at['401.bzip2-226B',
              'Misses escritura'] = total_write_misses_401BC32

tabla_BC32.at['401.bzip2-226B',
              'Miss rate escritura [%]'] = total_write_miss_rate_401BC32

# **403.gcc-16B**

tabla_BC32.at['403.gcc-16B', 'Total Misses'] = total_misses_403BC32

tabla_BC32.at['403.gcc-16B', 'Miss rate total [%]'] = total_miss_rate_403BC32

tabla_BC32.at['403.gcc-16B', 'Misses lectura'] = total_read_misses_403BC32

tabla_BC32.at['403.gcc-16B',
              'Miss rate lectura [%]'] = total_read_miss_rate_403BC32

tabla_BC32.at['403.gcc-16B',
              'Misses escritura'] = total_write_misses_403BC32

tabla_BC32.at['403.gcc-16B',
              'Miss rate escritura [%]'] = total_write_miss_rate_403BC32

# **410.bwaves-1963B**

tabla_BC32.at['410.bwaves-1963B', 'Total Misses'] = total_misses_410BC32

tabla_BC32.at['410.bwaves-1963B',
              'Miss rate total [%]'] = total_miss_rate_410BC32

tabla_BC32.at['410.bwaves-1963B', 'Misses lectura'] = total_read_misses_410BC32

tabla_BC32.at['410.bwaves-1963B',
              'Miss rate lectura [%]'] = total_read_miss_rate_410BC32

tabla_BC32.at['410.bwaves-1963B',
              'Misses escritura'] = total_write_misses_410BC32

tabla_BC32.at['410.bwaves-1963B',
              'Miss rate escritura [%]'] = total_write_miss_rate_410BC32

# **416.gamess-875B**

tabla_BC32.at['416.gamess-875B', 'Total Misses'] = total_misses_416BC32

tabla_BC32.at['416.gamess-875B',
              'Miss rate total [%]'] = total_miss_rate_416BC32

tabla_BC32.at['416.gamess-875B', 'Misses lectura'] = total_read_misses_416BC32

tabla_BC32.at['416.gamess-875B',
              'Miss rate lectura [%]'] = total_read_miss_rate_416BC32

tabla_BC32.at['416.gamess-875B',
              'Misses escritura'] = total_write_misses_416BC32

tabla_BC32.at['416.gamess-875B',
              'Miss rate escritura [%]'] = total_write_miss_rate_416BC32

# **429.mcf-184B**

tabla_BC32.at['429.mcf-184B', 'Total Misses'] = total_misses_429BC32

tabla_BC32.at['429.mcf-184B', 'Miss rate total [%]'] = total_miss_rate_429BC32

tabla_BC32.at['429.mcf-184B', 'Misses lectura'] = total_read_misses_429BC32

tabla_BC32.at['429.mcf-184B',
              'Miss rate lectura [%]'] = total_read_miss_rate_429BC32

tabla_BC32.at['429.mcf-184B',
              'Misses escritura'] = total_write_misses_429BC32

tabla_BC32.at['429.mcf-184B',
              'Miss rate escritura [%]'] = total_write_miss_rate_429BC32

# **433.milc-127B**

tabla_BC32.at['433.milc-127B', 'Total Misses'] = total_misses_433BC32

tabla_BC32.at['433.milc-127B', 'Miss rate total [%]'] = total_miss_rate_433BC32

tabla_BC32.at['433.milc-127B', 'Misses lectura'] = total_read_misses_433BC32

tabla_BC32.at['433.milc-127B',
              'Miss rate lectura [%]'] = total_read_miss_rate_433BC32

tabla_BC32.at['433.milc-127B',
              'Misses escritura'] = total_write_misses_433BC32

tabla_BC32.at['433.milc-127B',
              'Miss rate escritura [%]'] = total_write_miss_rate_433BC32

# **435.gromacs-111B**

tabla_BC32.at['435.gromacs-111B', 'Total Misses'] = total_misses_435BC32

tabla_BC32.at['435.gromacs-111B',
              'Miss rate total [%]'] = total_miss_rate_435BC32

tabla_BC32.at['435.gromacs-111B', 'Misses lectura'] = total_read_misses_435BC32

tabla_BC32.at['435.gromacs-111B',
              'Miss rate lectura [%]'] = total_read_miss_rate_435BC32

tabla_BC32.at['435.gromacs-111B',
              'Misses escritura'] = total_write_misses_435BC32

tabla_BC32.at['435.gromacs-111B',
              'Miss rate escritura [%]'] = total_write_miss_rate_435BC32
# **436.cactusADM-1804B**

tabla_BC32.at['436.cactusADM-1804B', 'Total Misses'] = total_misses_436BC32

tabla_BC32.at['436.cactusADM-1804B',
              'Miss rate total [%]'] = total_miss_rate_436BC32

tabla_BC32.at['436.cactusADM-1804B',
              'Misses lectura'] = total_read_misses_436BC32

tabla_BC32.at['436.cactusADM-1804B',
              'Miss rate lectura [%]'] = total_read_miss_rate_436BC32

tabla_BC32.at['436.cactusADM-1804B',
              'Misses escritura'] = total_write_misses_436BC32

tabla_BC32.at['436.cactusADM-1804B',
              'Miss rate escritura [%]'] = total_write_miss_rate_436BC32

# **437.leslie3d-134B**

tabla_BC32.at['437.leslie3d-134B', 'Total Misses'] = total_misses_437BC32

tabla_BC32.at['437.leslie3d-134B',
              'Miss rate total [%]'] = total_miss_rate_437BC32

tabla_BC32.at['437.leslie3d-134B',
              'Misses lectura'] = total_read_misses_437BC32

tabla_BC32.at['437.leslie3d-134B',
              'Miss rate lectura [%]'] = total_read_miss_rate_437BC32

tabla_BC32.at['437.leslie3d-134B',
              'Misses escritura'] = total_write_misses_437BC32

tabla_BC32.at['437.leslie3d-134B',
              'Miss rate escritura [%]'] = total_write_miss_rate_437BC32

# **444.namd-120B**

tabla_BC32.at['444.namd-120B', 'Total Misses'] = total_misses_444BC32

tabla_BC32.at['444.namd-120B', 'Miss rate total [%]'] = total_miss_rate_444BC32

tabla_BC32.at['444.namd-120B', 'Misses lectura'] = total_read_misses_444BC32

tabla_BC32.at['444.namd-120B',
              'Miss rate lectura [%]'] = total_read_miss_rate_444BC32

tabla_BC32.at['444.namd-120B',
              'Misses escritura'] = total_write_misses_444BC32

tabla_BC32.at['444.namd-120B',
              'Miss rate escritura [%]'] = total_write_miss_rate_444BC32

# **445.gobmk-17B**

tabla_BC32.at['445.gobmk-17B', 'Total Misses'] = total_misses_445BC32

tabla_BC32.at['445.gobmk-17B', 'Miss rate total [%]'] = total_miss_rate_445BC32

tabla_BC32.at['445.gobmk-17B', 'Misses lectura'] = total_read_misses_445BC32

tabla_BC32.at['445.gobmk-17B',
              'Miss rate lectura [%]'] = total_read_miss_rate_445BC32

tabla_BC32.at['445.gobmk-17B',
              'Misses escritura'] = total_write_misses_445BC32

tabla_BC32.at['445.gobmk-17B',
              'Miss rate escritura [%]'] = total_write_miss_rate_445BC32

# **450.soplex-247B**

tabla_BC32.at['450.soplex-247B', 'Total Misses'] = total_misses_450BC32

tabla_BC32.at['450.soplex-247B',
              'Miss rate total [%]'] = total_miss_rate_450BC32

tabla_BC32.at['450.soplex-247B', 'Misses lectura'] = total_read_misses_450BC32

tabla_BC32.at['450.soplex-247B',
              'Miss rate lectura [%]'] = total_read_miss_rate_450BC32

tabla_BC32.at['450.soplex-247B',
              'Misses escritura'] = total_write_misses_450BC32

tabla_BC32.at['450.soplex-247B',
              'Miss rate escritura [%]'] = total_write_miss_rate_450BC32

# **453.povray-887B**

tabla_BC32.at['453.povray-887B', 'Total Misses'] = total_misses_453BC32

tabla_BC32.at['453.povray-887B',
              'Miss rate total [%]'] = total_miss_rate_453BC32

tabla_BC32.at['453.povray-887B', 'Misses lectura'] = total_read_misses_453BC32

tabla_BC32.at['453.povray-887B',
              'Miss rate lectura [%]'] = total_read_miss_rate_453BC32

tabla_BC32.at['453.povray-887B',
              'Misses escritura'] = total_write_misses_453BC32

tabla_BC32.at['453.povray-887B',
              'Miss rate escritura [%]'] = total_write_miss_rate_453BC32

# **454.calculix-104B**

tabla_BC32.at['454.calculix-104B', 'Total Misses'] = total_misses_454BC32

tabla_BC32.at['454.calculix-104B',
              'Miss rate total [%]'] = total_miss_rate_454BC32

tabla_BC32.at['454.calculix-104B',
              'Misses lectura'] = total_read_misses_454BC32

tabla_BC32.at['454.calculix-104B',
              'Miss rate lectura [%]'] = total_read_miss_rate_454BC32

tabla_BC32.at['454.calculix-104B',
              'Misses escritura'] = total_write_misses_454BC32

tabla_BC32.at['454.calculix-104B',
              'Miss rate escritura [%]'] = total_write_miss_rate_454BC32

# **456.hmmer-191B**

tabla_BC32.at['456.hmmer-191B', 'Total Misses'] = total_misses_456BC32

tabla_BC32.at['456.hmmer-191B',
              'Miss rate total [%]'] = total_miss_rate_456BC32

tabla_BC32.at['456.hmmer-191B', 'Misses lectura'] = total_read_misses_456BC32

tabla_BC32.at['456.hmmer-191B',
              'Miss rate lectura [%]'] = total_read_miss_rate_456BC32

tabla_BC32.at['456.hmmer-191B',
              'Misses escritura'] = total_write_misses_456BC32

tabla_BC32.at['456.hmmer-191B',
              'Miss rate escritura [%]'] = total_write_miss_rate_456BC32

# **458.sjeng-1088B**

tabla_BC32.at['458.sjeng-1088B', 'Total Misses'] = total_misses_458BC32

tabla_BC32.at['458.sjeng-1088B',
              'Miss rate total [%]'] = total_miss_rate_458BC32

tabla_BC32.at['458.sjeng-1088B', 'Misses lectura'] = total_read_misses_458BC32

tabla_BC32.at['458.sjeng-1088B',
              'Miss rate lectura [%]'] = total_read_miss_rate_458BC32

tabla_BC32.at['458.sjeng-1088B',
              'Misses escritura'] = total_write_misses_458BC32

tabla_BC32.at['458.sjeng-1088B',
              'Miss rate escritura [%]'] = total_write_miss_rate_458BC32

# **459.GemsFDTD-1169B**

tabla_BC32.at['459.GemsFDTD-1169B', 'Total Misses'] = total_misses_459BC32

tabla_BC32.at['459.GemsFDTD-1169B',
              'Miss rate total [%]'] = total_miss_rate_459BC32

tabla_BC32.at['459.GemsFDTD-1169B',
              'Misses lectura'] = total_read_misses_459BC32

tabla_BC32.at['459.GemsFDTD-1169B',
              'Miss rate lectura [%]'] = total_read_miss_rate_459BC32

tabla_BC32.at['459.GemsFDTD-1169B',
              'Misses escritura'] = total_write_misses_459BC32

tabla_BC32.at['459.GemsFDTD-1169B',
              'Miss rate escritura [%]'] = total_write_miss_rate_459BC32

# **462.libquantum-1343B**

tabla_BC32.at['462.libquantum-1343B', 'Total Misses'] = total_misses_462BC32

tabla_BC32.at['462.libquantum-1343B',
              'Miss rate total [%]'] = total_miss_rate_462BC32

tabla_BC32.at['462.libquantum-1343B',
              'Misses lectura'] = total_read_misses_462BC32

tabla_BC32.at['462.libquantum-1343B',
              'Miss rate lectura [%]'] = total_read_miss_rate_462BC32

tabla_BC32.at['462.libquantum-1343B',
              'Misses escritura'] = total_write_misses_462BC32

tabla_BC32.at['462.libquantum-1343B',
              'Miss rate escritura [%]'] = total_write_miss_rate_462BC32

# **464.h264ref-30B**

tabla_BC32.at['464.h264ref-30B', 'Total Misses'] = total_misses_464BC32

tabla_BC32.at['464.h264ref-30B',
              'Miss rate total [%]'] = total_miss_rate_464BC32

tabla_BC32.at['464.h264ref-30B', 'Misses lectura'] = total_read_misses_464BC32

tabla_BC32.at['464.h264ref-30B',
              'Miss rate lectura [%]'] = total_read_miss_rate_464BC32

tabla_BC32.at['464.h264ref-30B',
              'Misses escritura'] = total_write_misses_464BC32

tabla_BC32.at['464.h264ref-30B',
              'Miss rate escritura [%]'] = total_write_miss_rate_464BC32

# **465.tonto-1769B**

tabla_BC32.at['465.tonto-1769B', 'Total Misses'] = total_misses_465BC32

tabla_BC32.at['465.tonto-1769B',
              'Miss rate total [%]'] = total_miss_rate_465BC32

tabla_BC32.at['465.tonto-1769B', 'Misses lectura'] = total_read_misses_465BC32

tabla_BC32.at['465.tonto-1769B',
              'Miss rate lectura [%]'] = total_read_miss_rate_465BC32

tabla_BC32.at['465.tonto-1769B',
              'Misses escritura'] = total_write_misses_465BC32
tabla_BC32.at['465.tonto-1769B',
              'Miss rate escritura [%]'] = total_write_miss_rate_465BC32

# **470.lbm-1274B**

tabla_BC32.at['470.lbm-1274B', 'Total Misses'] = total_misses_470BC32

tabla_BC32.at['470.lbm-1274B', 'Miss rate total [%]'] = total_miss_rate_470BC32

tabla_BC32.at['470.lbm-1274B', 'Misses lectura'] = total_read_misses_470BC32

tabla_BC32.at['470.lbm-1274B',
              'Miss rate lectura [%]'] = total_read_miss_rate_470BC32

tabla_BC32.at['470.lbm-1274B',
              'Misses escritura'] = total_write_misses_470BC32

tabla_BC32.at['470.lbm-1274B',
              'Miss rate escritura [%]'] = total_write_miss_rate_470BC32

# **471.omnetpp-188B**

tabla_BC32.at['471.omnetpp-188B', 'Total Misses'] = total_misses_471BC32

tabla_BC32.at['471.omnetpp-188B',
              'Miss rate total [%]'] = total_miss_rate_471BC32

tabla_BC32.at['471.omnetpp-188B', 'Misses lectura'] = total_read_misses_471BC32

tabla_BC32.at['471.omnetpp-188B',
              'Miss rate lectura [%]'] = total_read_miss_rate_471BC32

tabla_BC32.at['471.omnetpp-188B',
              'Misses escritura'] = total_write_misses_471BC32

tabla_BC32.at['471.omnetpp-188B',
              'Miss rate escritura [%]'] = total_write_miss_rate_471BC32

# **473.astar-153B**

tabla_BC32.at['473.astar-153B', 'Total Misses'] = total_misses_473BC32

tabla_BC32.at['473.astar-153B',
              'Miss rate total [%]'] = total_miss_rate_473BC32

tabla_BC32.at['473.astar-153B', 'Misses lectura'] = total_read_misses_473BC32

tabla_BC32.at['473.astar-153B',
              'Miss rate lectura [%]'] = total_read_miss_rate_473BC32

tabla_BC32.at['473.astar-153B',
              'Misses escritura'] = total_write_misses_473BC32

tabla_BC32.at['473.astar-153B',
              'Miss rate escritura [%]'] = total_write_miss_rate_473BC32

# **481.wrf-1170B**

tabla_BC32.at['481.wrf-1170B', 'Total Misses'] = total_misses_481BC32

tabla_BC32.at['481.wrf-1170B', 'Miss rate total [%]'] = total_miss_rate_481BC32

tabla_BC32.at['481.wrf-1170B', 'Misses lectura'] = total_read_misses_481BC32

tabla_BC32.at['481.wrf-1170B',
              'Miss rate lectura [%]'] = total_read_miss_rate_481BC32

tabla_BC32.at['481.wrf-1170B',
              'Misses escritura'] = total_write_misses_481BC32

tabla_BC32.at['481.wrf-1170B',
              'Miss rate escritura [%]'] = total_write_miss_rate_481BC32

# **482.sphinx3-1100B**

tabla_BC32.at['482.sphinx3-1100B', 'Total Misses'] = total_misses_482BC32

tabla_BC32.at['482.sphinx3-1100B',
              'Miss rate total [%]'] = total_miss_rate_482BC32

tabla_BC32.at['482.sphinx3-1100B',
              'Misses lectura'] = total_read_misses_482BC32

tabla_BC32.at['482.sphinx3-1100B',
              'Miss rate lectura [%]'] = total_read_miss_rate_482BC32

tabla_BC32.at['482.sphinx3-1100B',
              'Misses escritura'] = total_write_misses_482BC32

tabla_BC32.at['482.sphinx3-1100B',
              'Miss rate escritura [%]'] = total_write_miss_rate_482BC32

# **483.xalancbmk-127B**

tabla_BC32.at['483.xalancbmk-127B', 'Total Misses'] = total_misses_483BC32

tabla_BC32.at['483.xalancbmk-127B',
              'Miss rate total [%]'] = total_miss_rate_483BC32

tabla_BC32.at['483.xalancbmk-127B',
              'Misses lectura'] = total_read_misses_483BC32

tabla_BC32.at['483.xalancbmk-127B',
              'Miss rate lectura [%]'] = total_read_miss_rate_483BC32

tabla_BC32.at['483.xalancbmk-127B',
              'Misses escritura'] = total_write_misses_483BC32

tabla_BC32.at['483.xalancbmk-127B',
              'Miss rate escritura [%]'] = total_write_miss_rate_483BC32

print(">>>>>All BC32 data has been uploaded successfully")

#######################################################
# Extractor para experimento con tamaño de bloque 64kB#
#######################################################

# Creación de tablas para adjuntar valores
# Una tabla por tamaño
tabla_BC64 = pd.DataFrame(index=[
    '400.perlbench-41B', '401.bzip2-226B', '403.gcc-16B', '410.bwaves-1963B', '416.gamess-875B', '429.mcf-184B', '433.milc-127B',
    '435.gromacs-111B', '436.cactusADM-1804B', '437.leslie3d-134B', '444.namd-120B', '445.gobmk-17B',
    '450.soplex-247B', '453.povray-887B', '454.calculix-104B', '456.hmmer-191B', '458.sjeng-1088B', '459.GemsFDTD-1169B',
    '462.libquantum-1343B', '464.h264ref-30B', '465.tonto-1769B', '470.lbm-1274B', '471.omnetpp-188B', '473.astar-153B', '481.wrf-1170B',
    '482.sphinx3-1100B', '483.xalancbmk-127B'], columns=[
    'App', 'Total Misses', 'Miss rate total [%]', 'Misses lectura', 'Miss rate lectura [%]', 'Misses escritura', 'Miss rate escritura [%]'])
tabla_BC64['App'] = tabla_BC64.index

# Files paths
filename_55 = "RESULTS_BC/400BC64.txt"
filename_56 = "RESULTS_BC/401BC64.txt"
filename_57 = "RESULTS_BC/403BC64.txt"
filename_58 = "RESULTS_BC/410BC64.txt"
filename_59 = "RESULTS_BC/416BC64.txt"
filename_60 = "RESULTS_BC/429BC64.txt"
filename_61 = "RESULTS_BC/433BC64.txt"
filename_62 = "RESULTS_BC/435BC64.txt"
filename_63 = "RESULTS_BC/436BC64.txt"
filename_64 = "RESULTS_BC/437BC64.txt"
filename_65 = "RESULTS_BC/444BC64.txt"
filename_66 = "RESULTS_BC/445BC64.txt"
filename_67 = "RESULTS_BC/450BC64.txt"
filename_68 = "RESULTS_BC/453BC64.txt"
filename_69 = "RESULTS_BC/454BC64.txt"
filename_70 = "RESULTS_BC/456BC64.txt"
filename_71 = "RESULTS_BC/458BC64.txt"
filename_72 = "RESULTS_BC/459BC64.txt"
filename_73 = "RESULTS_BC/462BC64.txt"
filename_74 = "RESULTS_BC/464BC64.txt"
filename_75 = "RESULTS_BC/465BC64.txt"
filename_76 = "RESULTS_BC/470BC64.txt"
filename_77 = "RESULTS_BC/471BC64.txt"
filename_78 = "RESULTS_BC/473BC64.txt"
filename_79 = "RESULTS_BC/481BC64.txt"
filename_80 = "RESULTS_BC/482BC64.txt"
filename_81 = "RESULTS_BC/483BC64.txt"

# Content file extracter
with open(filename_55, 'r') as file:
    content_400BC64 = file.read()
with open(filename_56, 'r') as file:
    content_401BC64 = file.read()
with open(filename_57, 'r') as file:
    content_403BC64 = file.read()
with open(filename_58, 'r') as file:
    content_410BC64 = file.read()
with open(filename_59, 'r') as file:
    content_416BC64 = file.read()
with open(filename_60, 'r') as file:
    content_429BC64 = file.read()
with open(filename_61, 'r') as file:
    content_433BC64 = file.read()
with open(filename_62, 'r') as file:
    content_435BC64 = file.read()
with open(filename_63, 'r') as file:
    content_436BC64 = file.read()
with open(filename_64, 'r') as file:
    content_437BC64 = file.read()
with open(filename_65, 'r') as file:
    content_444BC64 = file.read()
with open(filename_66, 'r') as file:
    content_445BC64 = file.read()
with open(filename_67, 'r') as file:
    content_450BC64 = file.read()
with open(filename_68, 'r') as file:
    content_453BC64 = file.read()
with open(filename_69, 'r') as file:
    content_454BC64 = file.read()
with open(filename_70, 'r') as file:
    content_456BC64 = file.read()
with open(filename_71, 'r') as file:
    content_458BC64 = file.read()
with open(filename_72, 'r') as file:
    content_459BC64 = file.read()
with open(filename_73, 'r') as file:
    content_462BC64 = file.read()
with open(filename_74, 'r') as file:
    content_464BC64 = file.read()
with open(filename_75, 'r') as file:
    content_465BC64 = file.read()
with open(filename_76, 'r') as file:
    content_470BC64 = file.read()
with open(filename_77, 'r') as file:
    content_471BC64 = file.read()
with open(filename_78, 'r') as file:
    content_473BC64 = file.read()
with open(filename_79, 'r') as file:
    content_481BC64 = file.read()
with open(filename_80, 'r') as file:
    content_482BC64 = file.read()
with open(filename_81, 'r') as file:
    content_483BC64 = file.read()

# Variables según aplicación

# 400.pearlbench-41B
total_misses_400BC64 = re.search(
    r"Total_misses (\d+)", content_400BC64).group(1)
total_miss_rate_400BC64 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_400BC64).group(1)
total_read_misses_400BC64 = re.search(
    r"Total_read_misses (\d+)", content_400BC64).group(1)
total_read_miss_rate_400BC64 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_400BC64).group(1)
total_write_misses_400BC64 = re.search(
    r"Total_write_misses (\d+)", content_400BC64).group(1)
total_write_miss_rate_400BC64 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_400BC64).group(1)
print(">>>>>All BC64 400.pearlbench-41B variables where obtained successfully")

# 401.bzip2-226B
total_misses_401BC64 = re.search(
    r"Total_misses (\d+)", content_401BC64).group(1)
total_miss_rate_401BC64 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_401BC64).group(1)
total_read_misses_401BC64 = re.search(
    r"Total_read_misses (\d+)", content_401BC64).group(1)
total_read_miss_rate_401BC64 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_401BC64).group(1)
total_write_misses_401BC64 = re.search(
    r"Total_write_misses (\d+)", content_401BC64).group(1)
total_write_miss_rate_401BC64 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_401BC64).group(1)
print(">>>>>All BC64 401.bzip2-226B variables where obtained successfully")

# 403.gcc-16B
total_misses_403BC64 = re.search(
    r"Total_misses (\d+)", content_403BC64).group(1)
total_miss_rate_403BC64 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_403BC64).group(1)
total_read_misses_403BC64 = re.search(
    r"Total_read_misses (\d+)", content_403BC64).group(1)
total_read_miss_rate_403BC64 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_403BC64).group(1)
total_write_misses_403BC64 = re.search(
    r"Total_write_misses (\d+)", content_403BC64).group(1)
total_write_miss_rate_403BC64 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_403BC64).group(1)
print(">>>>>All BC64 403.gcc-16B variables where obtained successfully")

# 410.bwaves-1963B
total_misses_410BC64 = re.search(
    r"Total_misses (\d+)", content_410BC64).group(1)
total_miss_rate_410BC64 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_410BC64).group(1)
total_read_misses_410BC64 = re.search(
    r"Total_read_misses (\d+)", content_410BC64).group(1)
total_read_miss_rate_410BC64 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_410BC64).group(1)
total_write_misses_410BC64 = re.search(
    r"Total_write_misses (\d+)", content_410BC64).group(1)
total_write_miss_rate_410BC64 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_410BC64).group(1)
print(">>>>>All BC64 410.bwaves-1963B variables where obtained successfully")

# 416.gamess-875B
total_misses_416BC64 = re.search(
    r"Total_misses (\d+)", content_416BC64).group(1)
total_miss_rate_416BC64 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_416BC64).group(1)
total_read_misses_416BC64 = re.search(
    r"Total_read_misses (\d+)", content_416BC64).group(1)
total_read_miss_rate_416BC64 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_416BC64).group(1)
total_write_misses_416BC64 = re.search(
    r"Total_write_misses (\d+)", content_416BC64).group(1)
total_write_miss_rate_416BC64 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_416BC64).group(1)
print(">>>>>All BC64 416.gamess-875B variables where obtained successfully")

# 429.mcf-184B
total_misses_429BC64 = re.search(
    r"Total_misses (\d+)", content_429BC64).group(1)
total_miss_rate_429BC64 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_429BC64).group(1)
total_read_misses_429BC64 = re.search(
    r"Total_read_misses (\d+)", content_429BC64).group(1)
total_read_miss_rate_429BC64 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_429BC64).group(1)
total_write_misses_429BC64 = re.search(
    r"Total_write_misses (\d+)", content_429BC64).group(1)
total_write_miss_rate_429BC64 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_429BC64).group(1)
print(">>>>>All BC64 429.mcf-184B variables where obtained successfully")

# 433.milc-127B
total_misses_433BC64 = re.search(
    r"Total_misses (\d+)", content_433BC64).group(1)
total_miss_rate_433BC64 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_433BC64).group(1)
total_read_misses_433BC64 = re.search(
    r"Total_read_misses (\d+)", content_433BC64).group(1)
total_read_miss_rate_433BC64 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_433BC64).group(1)
total_write_misses_433BC64 = re.search(
    r"Total_write_misses (\d+)", content_433BC64).group(1)
total_write_miss_rate_433BC64 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_433BC64).group(1)
print(">>>>>All BC64 433.milc-127B variables where obtained successfully")

# 435.gromacs-111B
total_misses_435BC64 = re.search(
    r"Total_misses (\d+)", content_435BC64).group(1)
total_miss_rate_435BC64 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_435BC64).group(1)
total_read_misses_435BC64 = re.search(
    r"Total_read_misses (\d+)", content_435BC64).group(1)
total_read_miss_rate_435BC64 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_435BC64).group(1)
total_write_misses_435BC64 = re.search(
    r"Total_write_misses (\d+)", content_435BC64).group(1)
total_write_miss_rate_435BC64 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_435BC64).group(1)
print(">>>>>All BC64 435.gromacs-111B variables where obtained successfully")

# 436.cactusADM-1804B
total_misses_436BC64 = re.search(
    r"Total_misses (\d+)", content_436BC64).group(1)
total_miss_rate_436BC64 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_436BC64).group(1)
total_read_misses_436BC64 = re.search(
    r"Total_read_misses (\d+)", content_436BC64).group(1)
total_read_miss_rate_436BC64 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_436BC64).group(1)
total_write_misses_436BC64 = re.search(
    r"Total_write_misses (\d+)", content_436BC64).group(1)
total_write_miss_rate_436BC64 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_436BC64).group(1)
print(">>>>>All BC64 436.cactusADM-1804B variables where obtained successfully")

# 437.leslie3d-134B
total_misses_437BC64 = re.search(
    r"Total_misses (\d+)", content_437BC64).group(1)
total_miss_rate_437BC64 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_437BC64).group(1)
total_read_misses_437BC64 = re.search(
    r"Total_read_misses (\d+)", content_437BC64).group(1)
total_read_miss_rate_437BC64 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_437BC64).group(1)
total_write_misses_437BC64 = re.search(
    r"Total_write_misses (\d+)", content_437BC64).group(1)
total_write_miss_rate_437BC64 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_437BC64).group(1)
print(">>>>>All BC64 437.leslie3d-134B variables where obtained successfully")

# 444.namd-120B
total_misses_444BC64 = re.search(
    r"Total_misses (\d+)", content_444BC64).group(1)
total_miss_rate_444BC64 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_444BC64).group(1)
total_read_misses_444BC64 = re.search(
    r"Total_read_misses (\d+)", content_444BC64).group(1)
total_read_miss_rate_444BC64 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_444BC64).group(1)
total_write_misses_444BC64 = re.search(
    r"Total_write_misses (\d+)", content_444BC64).group(1)
total_write_miss_rate_444BC64 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_444BC64).group(1)
print(">>>>>All BC64 444.namd-120B variables where obtained successfully")

# 445.gobmk-17B
total_misses_445BC64 = re.search(
    r"Total_misses (\d+)", content_445BC64).group(1)
total_miss_rate_445BC64 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_445BC64).group(1)
total_read_misses_445BC64 = re.search(
    r"Total_read_misses (\d+)", content_445BC64).group(1)
total_read_miss_rate_445BC64 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_445BC64).group(1)
total_write_misses_445BC64 = re.search(
    r"Total_write_misses (\d+)", content_445BC64).group(1)
total_write_miss_rate_445BC64 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_445BC64).group(1)
print(">>>>>All BC64 445.gobmk-17B variables where obtained successfully")

# 450.soplex-247B
total_misses_450BC64 = re.search(
    r"Total_misses (\d+)", content_450BC64).group(1)
total_miss_rate_450BC64 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_450BC64).group(1)
total_read_misses_450BC64 = re.search(
    r"Total_read_misses (\d+)", content_450BC64).group(1)
total_read_miss_rate_450BC64 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_450BC64).group(1)
total_write_misses_450BC64 = re.search(
    r"Total_write_misses (\d+)", content_450BC64).group(1)
total_write_miss_rate_450BC64 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_450BC64).group(1)
print(">>>>>All BC64 450.soplex-247B variables where obtained successfully")

# 453.povray-887B
total_misses_453BC64 = re.search(
    r"Total_misses (\d+)", content_453BC64).group(1)
total_miss_rate_453BC64 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_453BC64).group(1)
total_read_misses_453BC64 = re.search(
    r"Total_read_misses (\d+)", content_453BC64).group(1)
total_read_miss_rate_453BC64 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_453BC64).group(1)
total_write_misses_453BC64 = re.search(
    r"Total_write_misses (\d+)", content_453BC64).group(1)
total_write_miss_rate_453BC64 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_453BC64).group(1)
print(">>>>>All BC64 453.povray-887B variables where obtained successfully")

# 454.calculix-104B
total_misses_454BC64 = re.search(
    r"Total_misses (\d+)", content_454BC64).group(1)
total_miss_rate_454BC64 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_454BC64).group(1)
total_read_misses_454BC64 = re.search(
    r"Total_read_misses (\d+)", content_454BC64).group(1)
total_read_miss_rate_454BC64 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_454BC64).group(1)
total_write_misses_454BC64 = re.search(
    r"Total_write_misses (\d+)", content_454BC64).group(1)
total_write_miss_rate_454BC64 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_454BC64).group(1)
print(">>>>>All BC64 454.calculix-104B variables where obtained successfully")

# 456.hmmer-191B
total_misses_456BC64 = re.search(
    r"Total_misses (\d+)", content_456BC64).group(1)
total_miss_rate_456BC64 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_456BC64).group(1)
total_read_misses_456BC64 = re.search(
    r"Total_read_misses (\d+)", content_456BC64).group(1)
total_read_miss_rate_456BC64 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_456BC64).group(1)
total_write_misses_456BC64 = re.search(
    r"Total_write_misses (\d+)", content_456BC64).group(1)
total_write_miss_rate_456BC64 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_456BC64).group(1)
print(">>>>>All BC64 456.hmmer-191B variables where obtained successfully")

# 458.sjeng-1088B
total_misses_458BC64 = re.search(
    r"Total_misses (\d+)", content_458BC64).group(1)
total_miss_rate_458BC64 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_458BC64).group(1)
total_read_misses_458BC64 = re.search(
    r"Total_read_misses (\d+)", content_458BC64).group(1)
total_read_miss_rate_458BC64 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_458BC64).group(1)
total_write_misses_458BC64 = re.search(
    r"Total_write_misses (\d+)", content_458BC64).group(1)
total_write_miss_rate_458BC64 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_458BC64).group(1)
print(">>>>>All BC64 458.sjeng-1088B variables where obtained successfully")

# 459.GemsFDTD-1169B
total_misses_459BC64 = re.search(
    r"Total_misses (\d+)", content_459BC64).group(1)
total_miss_rate_459BC64 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_459BC64).group(1)
total_read_misses_459BC64 = re.search(
    r"Total_read_misses (\d+)", content_459BC64).group(1)
total_read_miss_rate_459BC64 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_459BC64).group(1)
total_write_misses_459BC64 = re.search(
    r"Total_write_misses (\d+)", content_459BC64).group(1)
total_write_miss_rate_459BC64 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_459BC64).group(1)
print(">>>>>All BC64 459.GemsFDTD-1169B variables where obtained successfully")

# 462.libquantum-1343B
total_misses_462BC64 = re.search(
    r"Total_misses (\d+)", content_462BC64).group(1)
total_miss_rate_462BC64 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_462BC64).group(1)
total_read_misses_462BC64 = re.search(
    r"Total_read_misses (\d+)", content_462BC64).group(1)
total_read_miss_rate_462BC64 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_462BC64).group(1)
total_write_misses_462BC64 = re.search(
    r"Total_write_misses (\d+)", content_462BC64).group(1)
total_write_miss_rate_462BC64 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_462BC64).group(1)
print(">>>>>All BC64 462.libquantum-1343B variables where obtained successfully")

# 464.h264ref-30B
total_misses_464BC64 = re.search(
    r"Total_misses (\d+)", content_464BC64).group(1)
total_miss_rate_464BC64 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_464BC64).group(1)
total_read_misses_464BC64 = re.search(
    r"Total_read_misses (\d+)", content_464BC64).group(1)
total_read_miss_rate_464BC64 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_464BC64).group(1)
total_write_misses_464BC64 = re.search(
    r"Total_write_misses (\d+)", content_464BC64).group(1)
total_write_miss_rate_464BC64 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_464BC64).group(1)
print(">>>>>All BC64 464.h264ref-30B variables where obtained successfully")

# 465.tonto-1769B
total_misses_465BC64 = re.search(
    r"Total_misses (\d+)", content_465BC64).group(1)
total_miss_rate_465BC64 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_465BC64).group(1)
total_read_misses_465BC64 = re.search(
    r"Total_read_misses (\d+)", content_465BC64).group(1)
total_read_miss_rate_465BC64 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_465BC64).group(1)
total_write_misses_465BC64 = re.search(
    r"Total_write_misses (\d+)", content_465BC64).group(1)
total_write_miss_rate_465BC64 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_465BC64).group(1)
print(">>>>>All BC64 465.tonto-1769B variables where obtained successfully")

# 470.lbm-1274B
total_misses_470BC64 = re.search(
    r"Total_misses (\d+)", content_470BC64).group(1)
total_miss_rate_470BC64 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_470BC64).group(1)
total_read_misses_470BC64 = re.search(
    r"Total_read_misses (\d+)", content_470BC64).group(1)
total_read_miss_rate_470BC64 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_470BC64).group(1)
total_write_misses_470BC64 = re.search(
    r"Total_write_misses (\d+)", content_470BC64).group(1)
total_write_miss_rate_470BC64 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_470BC64).group(1)
print(">>>>>All BC64 470.lbm-1274B variables where obtained successfully")

# 471.omnetpp-188B
total_misses_471BC64 = re.search(
    r"Total_misses (\d+)", content_471BC64).group(1)
total_miss_rate_471BC64 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_471BC64).group(1)
total_read_misses_471BC64 = re.search(
    r"Total_read_misses (\d+)", content_471BC64).group(1)
total_read_miss_rate_471BC64 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_471BC64).group(1)
total_write_misses_471BC64 = re.search(
    r"Total_write_misses (\d+)", content_471BC64).group(1)
total_write_miss_rate_471BC64 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_471BC64).group(1)
print(">>>>>All BC64 471.omnetpp-188B variables where obtained successfully")

# 473.astar-153B
total_misses_473BC64 = re.search(
    r"Total_misses (\d+)", content_473BC64).group(1)
total_miss_rate_473BC64 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_473BC64).group(1)
total_read_misses_473BC64 = re.search(
    r"Total_read_misses (\d+)", content_473BC64).group(1)
total_read_miss_rate_473BC64 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_473BC64).group(1)
total_write_misses_473BC64 = re.search(
    r"Total_write_misses (\d+)", content_473BC64).group(1)
total_write_miss_rate_473BC64 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_473BC64).group(1)
print(">>>>>All BC64 473.astar-153B variables where obtained successfully")

# 481.wrf-1170B
total_misses_481BC64 = re.search(
    r"Total_misses (\d+)", content_481BC64).group(1)
total_miss_rate_481BC64 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_481BC64).group(1)
total_read_misses_481BC64 = re.search(
    r"Total_read_misses (\d+)", content_481BC64).group(1)
total_read_miss_rate_481BC64 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_481BC64).group(1)
total_write_misses_481BC64 = re.search(
    r"Total_write_misses (\d+)", content_481BC64).group(1)
total_write_miss_rate_481BC64 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_481BC64).group(1)
print(">>>>>All BC64 481.wrf-1170B variables where obtained successfully")

# 482.sphinx3-1100B
total_misses_482BC64 = re.search(
    r"Total_misses (\d+)", content_482BC64).group(1)
total_miss_rate_482BC64 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_482BC64).group(1)
total_read_misses_482BC64 = re.search(
    r"Total_read_misses (\d+)", content_482BC64).group(1)
total_read_miss_rate_482BC64 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_482BC64).group(1)
total_write_misses_482BC64 = re.search(
    r"Total_write_misses (\d+)", content_482BC64).group(1)
total_write_miss_rate_482BC64 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_482BC64).group(1)
print(">>>>>All BC64 482.sphinx3-1100B variables where obtained successfully")

# 483.xalancbmk-127B
total_misses_483BC64 = re.search(
    r"Total_misses (\d+)", content_483BC64).group(1)
total_miss_rate_483BC64 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_483BC64).group(1)
total_read_misses_483BC64 = re.search(
    r"Total_read_misses (\d+)", content_483BC64).group(1)
total_read_miss_rate_483BC64 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_483BC64).group(1)
total_write_misses_483BC64 = re.search(
    r"Total_write_misses (\d+)", content_483BC64).group(1)
total_write_miss_rate_483BC64 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_483BC64).group(1)
print(">>>>>All BC64 483.xalancbmk-127B variables where obtained successfully")

#############################
# Adjunta datos a dataframe #
#############################

# **400.perlbench-41B**

tabla_BC64.at['400.perlbench-41B', 'Total Misses'] = total_misses_400BC64

tabla_BC64.at['400.perlbench-41B',
              'Miss rate total [%]'] = total_miss_rate_400BC64

tabla_BC64.at['400.perlbench-41B',
              'Misses lectura'] = total_read_misses_400BC64

tabla_BC64.at['400.perlbench-41B',
              'Miss rate lectura [%]'] = total_read_miss_rate_400BC64

tabla_BC64.at['400.perlbench-41B',
              'Misses escritura'] = total_write_misses_400BC64

tabla_BC64.at['400.perlbench-41B',
              'Miss rate escritura [%]'] = total_write_miss_rate_400BC64

# **401.bzip2-226B**

tabla_BC64.at['401.bzip2-226B', 'Total Misses'] = total_misses_401BC64

tabla_BC64.at['401.bzip2-226B',
              'Miss rate total [%]'] = total_miss_rate_401BC64

tabla_BC64.at['401.bzip2-226B', 'Misses lectura'] = total_read_misses_401BC64

tabla_BC64.at['401.bzip2-226B',
              'Miss rate lectura [%]'] = total_read_miss_rate_401BC64

tabla_BC64.at['401.bzip2-226B',
              'Misses escritura'] = total_write_misses_401BC64

tabla_BC64.at['401.bzip2-226B',
              'Miss rate escritura [%]'] = total_write_miss_rate_401BC64

# **403.gcc-16B**

tabla_BC64.at['403.gcc-16B', 'Total Misses'] = total_misses_403BC64

tabla_BC64.at['403.gcc-16B', 'Miss rate total [%]'] = total_miss_rate_403BC64

tabla_BC64.at['403.gcc-16B', 'Misses lectura'] = total_read_misses_403BC64

tabla_BC64.at['403.gcc-16B',
              'Miss rate lectura [%]'] = total_read_miss_rate_403BC64

tabla_BC64.at['403.gcc-16B',
              'Misses escritura'] = total_write_misses_403BC64

tabla_BC64.at['403.gcc-16B',
              'Miss rate escritura [%]'] = total_write_miss_rate_403BC64

# **410.bwaves-1963B**

tabla_BC64.at['410.bwaves-1963B', 'Total Misses'] = total_misses_410BC64

tabla_BC64.at['410.bwaves-1963B',
              'Miss rate total [%]'] = total_miss_rate_410BC64

tabla_BC64.at['410.bwaves-1963B', 'Misses lectura'] = total_read_misses_410BC64

tabla_BC64.at['410.bwaves-1963B',
              'Miss rate lectura [%]'] = total_read_miss_rate_410BC64

tabla_BC64.at['410.bwaves-1963B',
              'Misses escritura'] = total_write_misses_410BC64

tabla_BC64.at['410.bwaves-1963B',
              'Miss rate escritura [%]'] = total_write_miss_rate_410BC64

# **416.gamess-875B**

tabla_BC64.at['416.gamess-875B', 'Total Misses'] = total_misses_416BC64

tabla_BC64.at['416.gamess-875B',
              'Miss rate total [%]'] = total_miss_rate_416BC64

tabla_BC64.at['416.gamess-875B', 'Misses lectura'] = total_read_misses_416BC64

tabla_BC64.at['416.gamess-875B',
              'Miss rate lectura [%]'] = total_read_miss_rate_416BC64

tabla_BC64.at['416.gamess-875B',
              'Misses escritura'] = total_write_misses_416BC64

tabla_BC64.at['416.gamess-875B',
              'Miss rate escritura [%]'] = total_write_miss_rate_416BC64

# **429.mcf-184B**

tabla_BC64.at['429.mcf-184B', 'Total Misses'] = total_misses_429BC64

tabla_BC64.at['429.mcf-184B', 'Miss rate total [%]'] = total_miss_rate_429BC64

tabla_BC64.at['429.mcf-184B', 'Misses lectura'] = total_read_misses_429BC64

tabla_BC64.at['429.mcf-184B',
              'Miss rate lectura [%]'] = total_read_miss_rate_429BC64

tabla_BC64.at['429.mcf-184B',
              'Misses escritura'] = total_write_misses_429BC64

tabla_BC64.at['429.mcf-184B',
              'Miss rate escritura [%]'] = total_write_miss_rate_429BC64

# **433.milc-127B**

tabla_BC64.at['433.milc-127B', 'Total Misses'] = total_misses_433BC64

tabla_BC64.at['433.milc-127B', 'Miss rate total [%]'] = total_miss_rate_433BC64

tabla_BC64.at['433.milc-127B', 'Misses lectura'] = total_read_misses_433BC64

tabla_BC64.at['433.milc-127B',
              'Miss rate lectura [%]'] = total_read_miss_rate_433BC64

tabla_BC64.at['433.milc-127B',
              'Misses escritura'] = total_write_misses_433BC64

tabla_BC64.at['433.milc-127B',
              'Miss rate escritura [%]'] = total_write_miss_rate_433BC64

# **435.gromacs-111B**

tabla_BC64.at['435.gromacs-111B', 'Total Misses'] = total_misses_435BC64

tabla_BC64.at['435.gromacs-111B',
              'Miss rate total [%]'] = total_miss_rate_435BC64

tabla_BC64.at['435.gromacs-111B', 'Misses lectura'] = total_read_misses_435BC64

tabla_BC64.at['435.gromacs-111B',
              'Miss rate lectura [%]'] = total_read_miss_rate_435BC64

tabla_BC64.at['435.gromacs-111B',
              'Misses escritura'] = total_write_misses_435BC64

tabla_BC64.at['435.gromacs-111B',
              'Miss rate escritura [%]'] = total_write_miss_rate_435BC64
# **436.cactusADM-1804B**

tabla_BC64.at['436.cactusADM-1804B', 'Total Misses'] = total_misses_436BC64

tabla_BC64.at['436.cactusADM-1804B',
              'Miss rate total [%]'] = total_miss_rate_436BC64

tabla_BC64.at['436.cactusADM-1804B',
              'Misses lectura'] = total_read_misses_436BC64

tabla_BC64.at['436.cactusADM-1804B',
              'Miss rate lectura [%]'] = total_read_miss_rate_436BC64

tabla_BC64.at['436.cactusADM-1804B',
              'Misses escritura'] = total_write_misses_436BC64

tabla_BC64.at['436.cactusADM-1804B',
              'Miss rate escritura [%]'] = total_write_miss_rate_436BC64

# **437.leslie3d-134B**

tabla_BC64.at['437.leslie3d-134B', 'Total Misses'] = total_misses_437BC64

tabla_BC64.at['437.leslie3d-134B',
              'Miss rate total [%]'] = total_miss_rate_437BC64

tabla_BC64.at['437.leslie3d-134B',
              'Misses lectura'] = total_read_misses_437BC64

tabla_BC64.at['437.leslie3d-134B',
              'Miss rate lectura [%]'] = total_read_miss_rate_437BC64

tabla_BC64.at['437.leslie3d-134B',
              'Misses escritura'] = total_write_misses_437BC64

tabla_BC64.at['437.leslie3d-134B',
              'Miss rate escritura [%]'] = total_write_miss_rate_437BC64

# **444.namd-120B**

tabla_BC64.at['444.namd-120B', 'Total Misses'] = total_misses_444BC64

tabla_BC64.at['444.namd-120B', 'Miss rate total [%]'] = total_miss_rate_444BC64

tabla_BC64.at['444.namd-120B', 'Misses lectura'] = total_read_misses_444BC64

tabla_BC64.at['444.namd-120B',
              'Miss rate lectura [%]'] = total_read_miss_rate_444BC64

tabla_BC64.at['444.namd-120B',
              'Misses escritura'] = total_write_misses_444BC64

tabla_BC64.at['444.namd-120B',
              'Miss rate escritura [%]'] = total_write_miss_rate_444BC64

# **445.gobmk-17B**

tabla_BC64.at['445.gobmk-17B', 'Total Misses'] = total_misses_445BC64

tabla_BC64.at['445.gobmk-17B', 'Miss rate total [%]'] = total_miss_rate_445BC64

tabla_BC64.at['445.gobmk-17B', 'Misses lectura'] = total_read_misses_445BC64

tabla_BC64.at['445.gobmk-17B',
              'Miss rate lectura [%]'] = total_read_miss_rate_445BC64

tabla_BC64.at['445.gobmk-17B',
              'Misses escritura'] = total_write_misses_445BC64

tabla_BC64.at['445.gobmk-17B',
              'Miss rate escritura [%]'] = total_write_miss_rate_445BC64

# **450.soplex-247B**

tabla_BC64.at['450.soplex-247B', 'Total Misses'] = total_misses_450BC64

tabla_BC64.at['450.soplex-247B',
              'Miss rate total [%]'] = total_miss_rate_450BC64

tabla_BC64.at['450.soplex-247B', 'Misses lectura'] = total_read_misses_450BC64

tabla_BC64.at['450.soplex-247B',
              'Miss rate lectura [%]'] = total_read_miss_rate_450BC64

tabla_BC64.at['450.soplex-247B',
              'Misses escritura'] = total_write_misses_450BC64

tabla_BC64.at['450.soplex-247B',
              'Miss rate escritura [%]'] = total_write_miss_rate_450BC64

# **453.povray-887B**

tabla_BC64.at['453.povray-887B', 'Total Misses'] = total_misses_453BC64

tabla_BC64.at['453.povray-887B',
              'Miss rate total [%]'] = total_miss_rate_453BC64

tabla_BC64.at['453.povray-887B', 'Misses lectura'] = total_read_misses_453BC64

tabla_BC64.at['453.povray-887B',
              'Miss rate lectura [%]'] = total_read_miss_rate_453BC64

tabla_BC64.at['453.povray-887B',
              'Misses escritura'] = total_write_misses_453BC64

tabla_BC64.at['453.povray-887B',
              'Miss rate escritura [%]'] = total_write_miss_rate_453BC64

# **454.calculix-104B**

tabla_BC64.at['454.calculix-104B', 'Total Misses'] = total_misses_454BC64

tabla_BC64.at['454.calculix-104B',
              'Miss rate total [%]'] = total_miss_rate_454BC64

tabla_BC64.at['454.calculix-104B',
              'Misses lectura'] = total_read_misses_454BC64

tabla_BC64.at['454.calculix-104B',
              'Miss rate lectura [%]'] = total_read_miss_rate_454BC64

tabla_BC64.at['454.calculix-104B',
              'Misses escritura'] = total_write_misses_454BC64

tabla_BC64.at['454.calculix-104B',
              'Miss rate escritura [%]'] = total_write_miss_rate_454BC64

# **456.hmmer-191B**

tabla_BC64.at['456.hmmer-191B', 'Total Misses'] = total_misses_456BC64

tabla_BC64.at['456.hmmer-191B',
              'Miss rate total [%]'] = total_miss_rate_456BC64

tabla_BC64.at['456.hmmer-191B', 'Misses lectura'] = total_read_misses_456BC64

tabla_BC64.at['456.hmmer-191B',
              'Miss rate lectura [%]'] = total_read_miss_rate_456BC64

tabla_BC64.at['456.hmmer-191B',
              'Misses escritura'] = total_write_misses_456BC64

tabla_BC64.at['456.hmmer-191B',
              'Miss rate escritura [%]'] = total_write_miss_rate_456BC64

# **458.sjeng-1088B**

tabla_BC64.at['458.sjeng-1088B', 'Total Misses'] = total_misses_458BC64

tabla_BC64.at['458.sjeng-1088B',
              'Miss rate total [%]'] = total_miss_rate_458BC64

tabla_BC64.at['458.sjeng-1088B', 'Misses lectura'] = total_read_misses_458BC64

tabla_BC64.at['458.sjeng-1088B',
              'Miss rate lectura [%]'] = total_read_miss_rate_458BC64

tabla_BC64.at['458.sjeng-1088B',
              'Misses escritura'] = total_write_misses_458BC64

tabla_BC64.at['458.sjeng-1088B',
              'Miss rate escritura [%]'] = total_write_miss_rate_458BC64

# **459.GemsFDTD-1169B**

tabla_BC64.at['459.GemsFDTD-1169B', 'Total Misses'] = total_misses_459BC64

tabla_BC64.at['459.GemsFDTD-1169B',
              'Miss rate total [%]'] = total_miss_rate_459BC64

tabla_BC64.at['459.GemsFDTD-1169B',
              'Misses lectura'] = total_read_misses_459BC64

tabla_BC64.at['459.GemsFDTD-1169B',
              'Miss rate lectura [%]'] = total_read_miss_rate_459BC64

tabla_BC64.at['459.GemsFDTD-1169B',
              'Misses escritura'] = total_write_misses_459BC64

tabla_BC64.at['459.GemsFDTD-1169B',
              'Miss rate escritura [%]'] = total_write_miss_rate_459BC64

# **462.libquantum-1343B**

tabla_BC64.at['462.libquantum-1343B', 'Total Misses'] = total_misses_462BC64

tabla_BC64.at['462.libquantum-1343B',
              'Miss rate total [%]'] = total_miss_rate_462BC64

tabla_BC64.at['462.libquantum-1343B',
              'Misses lectura'] = total_read_misses_462BC64

tabla_BC64.at['462.libquantum-1343B',
              'Miss rate lectura [%]'] = total_read_miss_rate_462BC64

tabla_BC64.at['462.libquantum-1343B',
              'Misses escritura'] = total_write_misses_462BC64

tabla_BC64.at['462.libquantum-1343B',
              'Miss rate escritura [%]'] = total_write_miss_rate_462BC64

# **464.h264ref-30B**

tabla_BC64.at['464.h264ref-30B', 'Total Misses'] = total_misses_464BC64

tabla_BC64.at['464.h264ref-30B',
              'Miss rate total [%]'] = total_miss_rate_464BC64

tabla_BC64.at['464.h264ref-30B', 'Misses lectura'] = total_read_misses_464BC64

tabla_BC64.at['464.h264ref-30B',
              'Miss rate lectura [%]'] = total_read_miss_rate_464BC64

tabla_BC64.at['464.h264ref-30B',
              'Misses escritura'] = total_write_misses_464BC64

tabla_BC64.at['464.h264ref-30B',
              'Miss rate escritura [%]'] = total_write_miss_rate_464BC64

# **465.tonto-1769B**

tabla_BC64.at['465.tonto-1769B', 'Total Misses'] = total_misses_465BC64

tabla_BC64.at['465.tonto-1769B',
              'Miss rate total [%]'] = total_miss_rate_465BC64

tabla_BC64.at['465.tonto-1769B', 'Misses lectura'] = total_read_misses_465BC64

tabla_BC64.at['465.tonto-1769B',
              'Miss rate lectura [%]'] = total_read_miss_rate_465BC64

tabla_BC64.at['465.tonto-1769B',
              'Misses escritura'] = total_write_misses_465BC64
tabla_BC64.at['465.tonto-1769B',
              'Miss rate escritura [%]'] = total_write_miss_rate_465BC64

# **470.lbm-1274B**

tabla_BC64.at['470.lbm-1274B', 'Total Misses'] = total_misses_470BC64

tabla_BC64.at['470.lbm-1274B', 'Miss rate total [%]'] = total_miss_rate_470BC64

tabla_BC64.at['470.lbm-1274B', 'Misses lectura'] = total_read_misses_470BC64

tabla_BC64.at['470.lbm-1274B',
              'Miss rate lectura [%]'] = total_read_miss_rate_470BC64

tabla_BC64.at['470.lbm-1274B',
              'Misses escritura'] = total_write_misses_470BC64

tabla_BC64.at['470.lbm-1274B',
              'Miss rate escritura [%]'] = total_write_miss_rate_470BC64

# **471.omnetpp-188B**

tabla_BC64.at['471.omnetpp-188B', 'Total Misses'] = total_misses_471BC64

tabla_BC64.at['471.omnetpp-188B',
              'Miss rate total [%]'] = total_miss_rate_471BC64

tabla_BC64.at['471.omnetpp-188B', 'Misses lectura'] = total_read_misses_471BC64

tabla_BC64.at['471.omnetpp-188B',
              'Miss rate lectura [%]'] = total_read_miss_rate_471BC64

tabla_BC64.at['471.omnetpp-188B',
              'Misses escritura'] = total_write_misses_471BC64

tabla_BC64.at['471.omnetpp-188B',
              'Miss rate escritura [%]'] = total_write_miss_rate_471BC64

# **473.astar-153B**

tabla_BC64.at['473.astar-153B', 'Total Misses'] = total_misses_473BC64

tabla_BC64.at['473.astar-153B',
              'Miss rate total [%]'] = total_miss_rate_473BC64

tabla_BC64.at['473.astar-153B', 'Misses lectura'] = total_read_misses_473BC64

tabla_BC64.at['473.astar-153B',
              'Miss rate lectura [%]'] = total_read_miss_rate_473BC64

tabla_BC64.at['473.astar-153B',
              'Misses escritura'] = total_write_misses_473BC64

tabla_BC64.at['473.astar-153B',
              'Miss rate escritura [%]'] = total_write_miss_rate_473BC64

# **481.wrf-1170B**

tabla_BC64.at['481.wrf-1170B', 'Total Misses'] = total_misses_481BC64

tabla_BC64.at['481.wrf-1170B', 'Miss rate total [%]'] = total_miss_rate_481BC64

tabla_BC64.at['481.wrf-1170B', 'Misses lectura'] = total_read_misses_481BC64

tabla_BC64.at['481.wrf-1170B',
              'Miss rate lectura [%]'] = total_read_miss_rate_481BC64

tabla_BC64.at['481.wrf-1170B',
              'Misses escritura'] = total_write_misses_481BC64

tabla_BC64.at['481.wrf-1170B',
              'Miss rate escritura [%]'] = total_write_miss_rate_481BC64

# **482.sphinx3-1100B**

tabla_BC64.at['482.sphinx3-1100B', 'Total Misses'] = total_misses_482BC64

tabla_BC64.at['482.sphinx3-1100B',
              'Miss rate total [%]'] = total_miss_rate_482BC64

tabla_BC64.at['482.sphinx3-1100B',
              'Misses lectura'] = total_read_misses_482BC64

tabla_BC64.at['482.sphinx3-1100B',
              'Miss rate lectura [%]'] = total_read_miss_rate_482BC64

tabla_BC64.at['482.sphinx3-1100B',
              'Misses escritura'] = total_write_misses_482BC64

tabla_BC64.at['482.sphinx3-1100B',
              'Miss rate escritura [%]'] = total_write_miss_rate_482BC64

# **483.xalancbmk-127B**

tabla_BC64.at['483.xalancbmk-127B', 'Total Misses'] = total_misses_483BC64

tabla_BC64.at['483.xalancbmk-127B',
              'Miss rate total [%]'] = total_miss_rate_483BC64

tabla_BC64.at['483.xalancbmk-127B',
              'Misses lectura'] = total_read_misses_483BC64

tabla_BC64.at['483.xalancbmk-127B',
              'Miss rate lectura [%]'] = total_read_miss_rate_483BC64

tabla_BC64.at['483.xalancbmk-127B',
              'Misses escritura'] = total_write_misses_483BC64

tabla_BC64.at['483.xalancbmk-127B',
              'Miss rate escritura [%]'] = total_write_miss_rate_483BC64

print(">>>>>All BC64 data has been uploaded successfully")

########################################################
# Extractor para experimento con tamaño de bloque 128kB#
########################################################

# Creación de tablas para adjuntar valores
# Una tabla por tamaño
tabla_BC128 = pd.DataFrame(index=[
    '400.perlbench-41B', '401.bzip2-226B', '403.gcc-16B', '410.bwaves-1963B', '416.gamess-875B', '429.mcf-184B', '433.milc-127B',
    '435.gromacs-111B', '436.cactusADM-1804B', '437.leslie3d-134B', '444.namd-120B', '445.gobmk-17B',
    '450.soplex-247B', '453.povray-887B', '454.calculix-104B', '456.hmmer-191B', '458.sjeng-1088B', '459.GemsFDTD-1169B',
    '462.libquantum-1343B', '464.h264ref-30B', '465.tonto-1769B', '470.lbm-1274B', '471.omnetpp-188B', '473.astar-153B', '481.wrf-1170B',
    '482.sphinx3-1100B', '483.xalancbmk-127B'], columns=[
    'App', 'Total Misses', 'Miss rate total [%]', 'Misses lectura', 'Miss rate lectura [%]', 'Misses escritura', 'Miss rate escritura [%]'])
tabla_BC128['App'] = tabla_BC128.index

# Files paths
filename_82 = "RESULTS_BC/400BC128.txt"
filename_83 = "RESULTS_BC/401BC128.txt"
filename_84 = "RESULTS_BC/403BC128.txt"
filename_85 = "RESULTS_BC/410BC128.txt"
filename_86 = "RESULTS_BC/416BC128.txt"
filename_87 = "RESULTS_BC/429BC128.txt"
filename_88 = "RESULTS_BC/433BC128.txt"
filename_89 = "RESULTS_BC/435BC128.txt"
filename_90 = "RESULTS_BC/436BC128.txt"
filename_91 = "RESULTS_BC/437BC128.txt"
filename_92 = "RESULTS_BC/444BC128.txt"
filename_93 = "RESULTS_BC/445BC128.txt"
filename_94 = "RESULTS_BC/450BC128.txt"
filename_95 = "RESULTS_BC/453BC128.txt"
filename_96 = "RESULTS_BC/454BC128.txt"
filename_97 = "RESULTS_BC/456BC128.txt"
filename_98 = "RESULTS_BC/458BC128.txt"
filename_99 = "RESULTS_BC/459BC128.txt"
filename_100 = "RESULTS_BC/462BC128.txt"
filename_101 = "RESULTS_BC/464BC128.txt"
filename_102 = "RESULTS_BC/465BC128.txt"
filename_103 = "RESULTS_BC/470BC128.txt"
filename_104 = "RESULTS_BC/471BC128.txt"
filename_105 = "RESULTS_BC/473BC128.txt"
filename_106 = "RESULTS_BC/481BC128.txt"
filename_107 = "RESULTS_BC/482BC128.txt"
filename_108 = "RESULTS_BC/483BC128.txt"

# Content file extracter
with open(filename_82, 'r') as file:
    content_400BC128 = file.read()
with open(filename_83, 'r') as file:
    content_401BC128 = file.read()
with open(filename_84, 'r') as file:
    content_403BC128 = file.read()
with open(filename_85, 'r') as file:
    content_410BC128 = file.read()
with open(filename_86, 'r') as file:
    content_416BC128 = file.read()
with open(filename_87, 'r') as file:
    content_429BC128 = file.read()
with open(filename_88, 'r') as file:
    content_433BC128 = file.read()
with open(filename_89, 'r') as file:
    content_435BC128 = file.read()
with open(filename_90, 'r') as file:
    content_436BC128 = file.read()
with open(filename_91, 'r') as file:
    content_437BC128 = file.read()
with open(filename_92, 'r') as file:
    content_444BC128 = file.read()
with open(filename_93, 'r') as file:
    content_445BC128 = file.read()
with open(filename_94, 'r') as file:
    content_450BC128 = file.read()
with open(filename_95, 'r') as file:
    content_453BC128 = file.read()
with open(filename_96, 'r') as file:
    content_454BC128 = file.read()
with open(filename_97, 'r') as file:
    content_456BC128 = file.read()
with open(filename_98, 'r') as file:
    content_458BC128 = file.read()
with open(filename_99, 'r') as file:
    content_459BC128 = file.read()
with open(filename_100, 'r') as file:
    content_462BC128 = file.read()
with open(filename_101, 'r') as file:
    content_464BC128 = file.read()
with open(filename_102, 'r') as file:
    content_465BC128 = file.read()
with open(filename_103, 'r') as file:
    content_470BC128 = file.read()
with open(filename_104, 'r') as file:
    content_471BC128 = file.read()
with open(filename_105, 'r') as file:
    content_473BC128 = file.read()
with open(filename_106, 'r') as file:
    content_481BC128 = file.read()
with open(filename_107, 'r') as file:
    content_482BC128 = file.read()
with open(filename_108, 'r') as file:
    content_483BC128 = file.read()

# Variables según aplicación

# 400.pearlbench-41B
total_misses_400BC128 = re.search(
    r"Total_misses (\d+)", content_400BC128).group(1)
total_miss_rate_400BC128 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_400BC128).group(1)
total_read_misses_400BC128 = re.search(
    r"Total_read_misses (\d+)", content_400BC128).group(1)
total_read_miss_rate_400BC128 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_400BC128).group(1)
total_write_misses_400BC128 = re.search(
    r"Total_write_misses (\d+)", content_400BC128).group(1)
total_write_miss_rate_400BC128 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_400BC128).group(1)
print(">>>>>All BC128 400.pearlbench-41B variables where obtained successfully")

# 401.bzip2-226B
total_misses_401BC128 = re.search(
    r"Total_misses (\d+)", content_401BC128).group(1)
total_miss_rate_401BC128 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_401BC128).group(1)
total_read_misses_401BC128 = re.search(
    r"Total_read_misses (\d+)", content_401BC128).group(1)
total_read_miss_rate_401BC128 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_401BC128).group(1)
total_write_misses_401BC128 = re.search(
    r"Total_write_misses (\d+)", content_401BC128).group(1)
total_write_miss_rate_401BC128 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_401BC128).group(1)
print(">>>>>All BC128 401.bzip2-226B variables where obtained successfully")

# 403.gcc-16B
total_misses_403BC128 = re.search(
    r"Total_misses (\d+)", content_403BC128).group(1)
total_miss_rate_403BC128 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_403BC128).group(1)
total_read_misses_403BC128 = re.search(
    r"Total_read_misses (\d+)", content_403BC128).group(1)
total_read_miss_rate_403BC128 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_403BC128).group(1)
total_write_misses_403BC128 = re.search(
    r"Total_write_misses (\d+)", content_403BC128).group(1)
total_write_miss_rate_403BC128 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_403BC128).group(1)
print(">>>>>All BC128 403.gcc-16B variables where obtained successfully")

# 410.bwaves-1963B
total_misses_410BC128 = re.search(
    r"Total_misses (\d+)", content_410BC128).group(1)
total_miss_rate_410BC128 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_410BC128).group(1)
total_read_misses_410BC128 = re.search(
    r"Total_read_misses (\d+)", content_410BC128).group(1)
total_read_miss_rate_410BC128 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_410BC128).group(1)
total_write_misses_410BC128 = re.search(
    r"Total_write_misses (\d+)", content_410BC128).group(1)
total_write_miss_rate_410BC128 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_410BC128).group(1)
print(">>>>>All BC128 410.bwaves-1963B variables where obtained successfully")

# 416.gamess-875B
total_misses_416BC128 = re.search(
    r"Total_misses (\d+)", content_416BC128).group(1)
total_miss_rate_416BC128 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_416BC128).group(1)
total_read_misses_416BC128 = re.search(
    r"Total_read_misses (\d+)", content_416BC128).group(1)
total_read_miss_rate_416BC128 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_416BC128).group(1)
total_write_misses_416BC128 = re.search(
    r"Total_write_misses (\d+)", content_416BC128).group(1)
total_write_miss_rate_416BC128 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_416BC128).group(1)
print(">>>>>All BC128 416.gamess-875B variables where obtained successfully")

# 429.mcf-184B
total_misses_429BC128 = re.search(
    r"Total_misses (\d+)", content_429BC128).group(1)
total_miss_rate_429BC128 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_429BC128).group(1)
total_read_misses_429BC128 = re.search(
    r"Total_read_misses (\d+)", content_429BC128).group(1)
total_read_miss_rate_429BC128 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_429BC128).group(1)
total_write_misses_429BC128 = re.search(
    r"Total_write_misses (\d+)", content_429BC128).group(1)
total_write_miss_rate_429BC128 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_429BC128).group(1)
print(">>>>>All BC128 429.mcf-184B variables where obtained successfully")

# 433.milc-127B
total_misses_433BC128 = re.search(
    r"Total_misses (\d+)", content_433BC128).group(1)
total_miss_rate_433BC128 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_433BC128).group(1)
total_read_misses_433BC128 = re.search(
    r"Total_read_misses (\d+)", content_433BC128).group(1)
total_read_miss_rate_433BC128 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_433BC128).group(1)
total_write_misses_433BC128 = re.search(
    r"Total_write_misses (\d+)", content_433BC128).group(1)
total_write_miss_rate_433BC128 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_433BC128).group(1)
print(">>>>>All BC128 433.milc-127B variables where obtained successfully")

# 435.gromacs-111B
total_misses_435BC128 = re.search(
    r"Total_misses (\d+)", content_435BC128).group(1)
total_miss_rate_435BC128 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_435BC128).group(1)
total_read_misses_435BC128 = re.search(
    r"Total_read_misses (\d+)", content_435BC128).group(1)
total_read_miss_rate_435BC128 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_435BC128).group(1)
total_write_misses_435BC128 = re.search(
    r"Total_write_misses (\d+)", content_435BC128).group(1)
total_write_miss_rate_435BC128 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_435BC128).group(1)
print(">>>>>All BC128 435.gromacs-111B variables where obtained successfully")

# 436.cactusADM-1804B
total_misses_436BC128 = re.search(
    r"Total_misses (\d+)", content_436BC128).group(1)
total_miss_rate_436BC128 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_436BC128).group(1)
total_read_misses_436BC128 = re.search(
    r"Total_read_misses (\d+)", content_436BC128).group(1)
total_read_miss_rate_436BC128 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_436BC128).group(1)
total_write_misses_436BC128 = re.search(
    r"Total_write_misses (\d+)", content_436BC128).group(1)
total_write_miss_rate_436BC128 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_436BC128).group(1)
print(">>>>>All BC128 436.cactusADM-1804B variables where obtained successfully")

# 437.leslie3d-134B
total_misses_437BC128 = re.search(
    r"Total_misses (\d+)", content_437BC128).group(1)
total_miss_rate_437BC128 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_437BC128).group(1)
total_read_misses_437BC128 = re.search(
    r"Total_read_misses (\d+)", content_437BC128).group(1)
total_read_miss_rate_437BC128 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_437BC128).group(1)
total_write_misses_437BC128 = re.search(
    r"Total_write_misses (\d+)", content_437BC128).group(1)
total_write_miss_rate_437BC128 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_437BC128).group(1)
print(">>>>>All BC128 437.leslie3d-134B variables where obtained successfully")

# 444.namd-120B
total_misses_444BC128 = re.search(
    r"Total_misses (\d+)", content_444BC128).group(1)
total_miss_rate_444BC128 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_444BC128).group(1)
total_read_misses_444BC128 = re.search(
    r"Total_read_misses (\d+)", content_444BC128).group(1)
total_read_miss_rate_444BC128 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_444BC128).group(1)
total_write_misses_444BC128 = re.search(
    r"Total_write_misses (\d+)", content_444BC128).group(1)
total_write_miss_rate_444BC128 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_444BC128).group(1)
print(">>>>>All BC128 444.namd-120B variables where obtained successfully")

# 445.gobmk-17B
total_misses_445BC128 = re.search(
    r"Total_misses (\d+)", content_445BC128).group(1)
total_miss_rate_445BC128 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_445BC128).group(1)
total_read_misses_445BC128 = re.search(
    r"Total_read_misses (\d+)", content_445BC128).group(1)
total_read_miss_rate_445BC128 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_445BC128).group(1)
total_write_misses_445BC128 = re.search(
    r"Total_write_misses (\d+)", content_445BC128).group(1)
total_write_miss_rate_445BC128 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_445BC128).group(1)
print(">>>>>All BC128 445.gobmk-17B variables where obtained successfully")

# 450.soplex-247B
total_misses_450BC128 = re.search(
    r"Total_misses (\d+)", content_450BC128).group(1)
total_miss_rate_450BC128 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_450BC128).group(1)
total_read_misses_450BC128 = re.search(
    r"Total_read_misses (\d+)", content_450BC128).group(1)
total_read_miss_rate_450BC128 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_450BC128).group(1)
total_write_misses_450BC128 = re.search(
    r"Total_write_misses (\d+)", content_450BC128).group(1)
total_write_miss_rate_450BC128 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_450BC128).group(1)
print(">>>>>All BC128 450.soplex-247B variables where obtained successfully")

# 453.povray-887B
total_misses_453BC128 = re.search(
    r"Total_misses (\d+)", content_453BC128).group(1)
total_miss_rate_453BC128 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_453BC128).group(1)
total_read_misses_453BC128 = re.search(
    r"Total_read_misses (\d+)", content_453BC128).group(1)
total_read_miss_rate_453BC128 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_453BC128).group(1)
total_write_misses_453BC128 = re.search(
    r"Total_write_misses (\d+)", content_453BC128).group(1)
total_write_miss_rate_453BC128 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_453BC128).group(1)
print(">>>>>All BC128 453.povray-887B variables where obtained successfully")

# 454.calculix-104B
total_misses_454BC128 = re.search(
    r"Total_misses (\d+)", content_454BC128).group(1)
total_miss_rate_454BC128 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_454BC128).group(1)
total_read_misses_454BC128 = re.search(
    r"Total_read_misses (\d+)", content_454BC128).group(1)
total_read_miss_rate_454BC128 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_454BC128).group(1)
total_write_misses_454BC128 = re.search(
    r"Total_write_misses (\d+)", content_454BC128).group(1)
total_write_miss_rate_454BC128 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_454BC128).group(1)
print(">>>>>All BC128 454.calculix-104B variables where obtained successfully")

# 456.hmmer-191B
total_misses_456BC128 = re.search(
    r"Total_misses (\d+)", content_456BC128).group(1)
total_miss_rate_456BC128 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_456BC128).group(1)
total_read_misses_456BC128 = re.search(
    r"Total_read_misses (\d+)", content_456BC128).group(1)
total_read_miss_rate_456BC128 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_456BC128).group(1)
total_write_misses_456BC128 = re.search(
    r"Total_write_misses (\d+)", content_456BC128).group(1)
total_write_miss_rate_456BC128 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_456BC128).group(1)
print(">>>>>All BC128 456.hmmer-191B variables where obtained successfully")

# 458.sjeng-1088B
total_misses_458BC128 = re.search(
    r"Total_misses (\d+)", content_458BC128).group(1)
total_miss_rate_458BC128 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_458BC128).group(1)
total_read_misses_458BC128 = re.search(
    r"Total_read_misses (\d+)", content_458BC128).group(1)
total_read_miss_rate_458BC128 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_458BC128).group(1)
total_write_misses_458BC128 = re.search(
    r"Total_write_misses (\d+)", content_458BC128).group(1)
total_write_miss_rate_458BC128 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_458BC128).group(1)
print(">>>>>All BC128 458.sjeng-1088B variables where obtained successfully")

# 459.GemsFDTD-1169B
total_misses_459BC128 = re.search(
    r"Total_misses (\d+)", content_459BC128).group(1)
total_miss_rate_459BC128 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_459BC128).group(1)
total_read_misses_459BC128 = re.search(
    r"Total_read_misses (\d+)", content_459BC128).group(1)
total_read_miss_rate_459BC128 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_459BC128).group(1)
total_write_misses_459BC128 = re.search(
    r"Total_write_misses (\d+)", content_459BC128).group(1)
total_write_miss_rate_459BC128 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_459BC128).group(1)
print(">>>>>All BC128 459.GemsFDTD-1169B variables where obtained successfully")

# 462.libquantum-1343B
total_misses_462BC128 = re.search(
    r"Total_misses (\d+)", content_462BC128).group(1)
total_miss_rate_462BC128 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_462BC128).group(1)
total_read_misses_462BC128 = re.search(
    r"Total_read_misses (\d+)", content_462BC128).group(1)
total_read_miss_rate_462BC128 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_462BC128).group(1)
total_write_misses_462BC128 = re.search(
    r"Total_write_misses (\d+)", content_462BC128).group(1)
total_write_miss_rate_462BC128 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_462BC128).group(1)
print(">>>>>All BC128 462.libquantum-1343B variables where obtained successfully")

# 464.h264ref-30B
total_misses_464BC128 = re.search(
    r"Total_misses (\d+)", content_464BC128).group(1)
total_miss_rate_464BC128 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_464BC128).group(1)
total_read_misses_464BC128 = re.search(
    r"Total_read_misses (\d+)", content_464BC128).group(1)
total_read_miss_rate_464BC128 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_464BC128).group(1)
total_write_misses_464BC128 = re.search(
    r"Total_write_misses (\d+)", content_464BC128).group(1)
total_write_miss_rate_464BC128 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_464BC128).group(1)
print(">>>>>All BC128 464.h264ref-30B variables where obtained successfully")

# 465.tonto-1769B
total_misses_465BC128 = re.search(
    r"Total_misses (\d+)", content_465BC128).group(1)
total_miss_rate_465BC128 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_465BC128).group(1)
total_read_misses_465BC128 = re.search(
    r"Total_read_misses (\d+)", content_465BC128).group(1)
total_read_miss_rate_465BC128 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_465BC128).group(1)
total_write_misses_465BC128 = re.search(
    r"Total_write_misses (\d+)", content_465BC128).group(1)
total_write_miss_rate_465BC128 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_465BC128).group(1)
print(">>>>>All BC128 465.tonto-1769B variables where obtained successfully")

# 470.lbm-1274B
total_misses_470BC128 = re.search(
    r"Total_misses (\d+)", content_470BC128).group(1)
total_miss_rate_470BC128 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_470BC128).group(1)
total_read_misses_470BC128 = re.search(
    r"Total_read_misses (\d+)", content_470BC128).group(1)
total_read_miss_rate_470BC128 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_470BC128).group(1)
total_write_misses_470BC128 = re.search(
    r"Total_write_misses (\d+)", content_470BC128).group(1)
total_write_miss_rate_470BC128 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_470BC128).group(1)
print(">>>>>All BC128 470.lbm-1274B variables where obtained successfully")

# 471.omnetpp-188B
total_misses_471BC128 = re.search(
    r"Total_misses (\d+)", content_471BC128).group(1)
total_miss_rate_471BC128 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_471BC128).group(1)
total_read_misses_471BC128 = re.search(
    r"Total_read_misses (\d+)", content_471BC128).group(1)
total_read_miss_rate_471BC128 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_471BC128).group(1)
total_write_misses_471BC128 = re.search(
    r"Total_write_misses (\d+)", content_471BC128).group(1)
total_write_miss_rate_471BC128 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_471BC128).group(1)
print(">>>>>All BC128 471.omnetpp-188B variables where obtained successfully")

# 473.astar-153B
total_misses_473BC128 = re.search(
    r"Total_misses (\d+)", content_473BC128).group(1)
total_miss_rate_473BC128 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_473BC128).group(1)
total_read_misses_473BC128 = re.search(
    r"Total_read_misses (\d+)", content_473BC128).group(1)
total_read_miss_rate_473BC128 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_473BC128).group(1)
total_write_misses_473BC128 = re.search(
    r"Total_write_misses (\d+)", content_473BC128).group(1)
total_write_miss_rate_473BC128 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_473BC128).group(1)
print(">>>>>All BC128 473.astar-153B variables where obtained successfully")

# 481.wrf-1170B
total_misses_481BC128 = re.search(
    r"Total_misses (\d+)", content_481BC128).group(1)
total_miss_rate_481BC128 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_481BC128).group(1)
total_read_misses_481BC128 = re.search(
    r"Total_read_misses (\d+)", content_481BC128).group(1)
total_read_miss_rate_481BC128 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_481BC128).group(1)
total_write_misses_481BC128 = re.search(
    r"Total_write_misses (\d+)", content_481BC128).group(1)
total_write_miss_rate_481BC128 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_481BC128).group(1)
print(">>>>>All BC128 481.wrf-1170B variables where obtained successfully")

# 482.sphinx3-1100B
total_misses_482BC128 = re.search(
    r"Total_misses (\d+)", content_482BC128).group(1)
total_miss_rate_482BC128 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_482BC128).group(1)
total_read_misses_482BC128 = re.search(
    r"Total_read_misses (\d+)", content_482BC128).group(1)
total_read_miss_rate_482BC128 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_482BC128).group(1)
total_write_misses_482BC128 = re.search(
    r"Total_write_misses (\d+)", content_482BC128).group(1)
total_write_miss_rate_482BC128 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_482BC128).group(1)
print(">>>>>All BC128 482.sphinx3-1100B variables where obtained successfully")

# 483.xalancbmk-127B
total_misses_483BC128 = re.search(
    r"Total_misses (\d+)", content_483BC128).group(1)
total_miss_rate_483BC128 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_483BC128).group(1)
total_read_misses_483BC128 = re.search(
    r"Total_read_misses (\d+)", content_483BC128).group(1)
total_read_miss_rate_483BC128 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_483BC128).group(1)
total_write_misses_483BC128 = re.search(
    r"Total_write_misses (\d+)", content_483BC128).group(1)
total_write_miss_rate_483BC128 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_483BC128).group(1)
print(">>>>>All BC128 483.xalancbmk-127B variables where obtained successfully")

#############################
# Adjunta datos a dataframe #
#############################

# **400.perlbench-41B**

tabla_BC128.at['400.perlbench-41B', 'Total Misses'] = total_misses_400BC128

tabla_BC128.at['400.perlbench-41B',
               'Miss rate total [%]'] = total_miss_rate_400BC128

tabla_BC128.at['400.perlbench-41B',
               'Misses lectura'] = total_read_misses_400BC128

tabla_BC128.at['400.perlbench-41B',
               'Miss rate lectura [%]'] = total_read_miss_rate_400BC128

tabla_BC128.at['400.perlbench-41B',
               'Misses escritura'] = total_write_misses_400BC128

tabla_BC128.at['400.perlbench-41B',
               'Miss rate escritura [%]'] = total_write_miss_rate_400BC128

# **401.bzip2-226B**

tabla_BC128.at['401.bzip2-226B', 'Total Misses'] = total_misses_401BC128

tabla_BC128.at['401.bzip2-226B',
               'Miss rate total [%]'] = total_miss_rate_401BC128

tabla_BC128.at['401.bzip2-226B', 'Misses lectura'] = total_read_misses_401BC128

tabla_BC128.at['401.bzip2-226B',
               'Miss rate lectura [%]'] = total_read_miss_rate_401BC128

tabla_BC128.at['401.bzip2-226B',
               'Misses escritura'] = total_write_misses_401BC128

tabla_BC128.at['401.bzip2-226B',
               'Miss rate escritura [%]'] = total_write_miss_rate_401BC128

# **403.gcc-16B**

tabla_BC128.at['403.gcc-16B', 'Total Misses'] = total_misses_403BC128

tabla_BC128.at['403.gcc-16B', 'Miss rate total [%]'] = total_miss_rate_403BC128

tabla_BC128.at['403.gcc-16B', 'Misses lectura'] = total_read_misses_403BC128

tabla_BC128.at['403.gcc-16B',
               'Miss rate lectura [%]'] = total_read_miss_rate_403BC128

tabla_BC128.at['403.gcc-16B',
               'Misses escritura'] = total_write_misses_403BC128

tabla_BC128.at['403.gcc-16B',
               'Miss rate escritura [%]'] = total_write_miss_rate_403BC128

# **410.bwaves-1963B**

tabla_BC128.at['410.bwaves-1963B', 'Total Misses'] = total_misses_410BC128

tabla_BC128.at['410.bwaves-1963B',
               'Miss rate total [%]'] = total_miss_rate_410BC128

tabla_BC128.at['410.bwaves-1963B',
               'Misses lectura'] = total_read_misses_410BC128

tabla_BC128.at['410.bwaves-1963B',
               'Miss rate lectura [%]'] = total_read_miss_rate_410BC128

tabla_BC128.at['410.bwaves-1963B',
               'Misses escritura'] = total_write_misses_410BC128

tabla_BC128.at['410.bwaves-1963B',
               'Miss rate escritura [%]'] = total_write_miss_rate_410BC128

# **416.gamess-875B**

tabla_BC128.at['416.gamess-875B', 'Total Misses'] = total_misses_416BC128

tabla_BC128.at['416.gamess-875B',
               'Miss rate total [%]'] = total_miss_rate_416BC128

tabla_BC128.at['416.gamess-875B',
               'Misses lectura'] = total_read_misses_416BC128

tabla_BC128.at['416.gamess-875B',
               'Miss rate lectura [%]'] = total_read_miss_rate_416BC128

tabla_BC128.at['416.gamess-875B',
               'Misses escritura'] = total_write_misses_416BC128

tabla_BC128.at['416.gamess-875B',
               'Miss rate escritura [%]'] = total_write_miss_rate_416BC128

# **429.mcf-184B**

tabla_BC128.at['429.mcf-184B', 'Total Misses'] = total_misses_429BC128

tabla_BC128.at['429.mcf-184B',
               'Miss rate total [%]'] = total_miss_rate_429BC128

tabla_BC128.at['429.mcf-184B', 'Misses lectura'] = total_read_misses_429BC128

tabla_BC128.at['429.mcf-184B',
               'Miss rate lectura [%]'] = total_read_miss_rate_429BC128

tabla_BC128.at['429.mcf-184B',
               'Misses escritura'] = total_write_misses_429BC128

tabla_BC128.at['429.mcf-184B',
               'Miss rate escritura [%]'] = total_write_miss_rate_429BC128

# **433.milc-127B**

tabla_BC128.at['433.milc-127B', 'Total Misses'] = total_misses_433BC128

tabla_BC128.at['433.milc-127B',
               'Miss rate total [%]'] = total_miss_rate_433BC128

tabla_BC128.at['433.milc-127B', 'Misses lectura'] = total_read_misses_433BC128

tabla_BC128.at['433.milc-127B',
               'Miss rate lectura [%]'] = total_read_miss_rate_433BC128

tabla_BC128.at['433.milc-127B',
               'Misses escritura'] = total_write_misses_433BC128

tabla_BC128.at['433.milc-127B',
               'Miss rate escritura [%]'] = total_write_miss_rate_433BC128

# **435.gromacs-111B**

tabla_BC128.at['435.gromacs-111B', 'Total Misses'] = total_misses_435BC128

tabla_BC128.at['435.gromacs-111B',
               'Miss rate total [%]'] = total_miss_rate_435BC128

tabla_BC128.at['435.gromacs-111B',
               'Misses lectura'] = total_read_misses_435BC128

tabla_BC128.at['435.gromacs-111B',
               'Miss rate lectura [%]'] = total_read_miss_rate_435BC128

tabla_BC128.at['435.gromacs-111B',
               'Misses escritura'] = total_write_misses_435BC128

tabla_BC128.at['435.gromacs-111B',
               'Miss rate escritura [%]'] = total_write_miss_rate_435BC128
# **436.cactusADM-1804B**

tabla_BC128.at['436.cactusADM-1804B', 'Total Misses'] = total_misses_436BC128

tabla_BC128.at['436.cactusADM-1804B',
               'Miss rate total [%]'] = total_miss_rate_436BC128

tabla_BC128.at['436.cactusADM-1804B',
               'Misses lectura'] = total_read_misses_436BC128

tabla_BC128.at['436.cactusADM-1804B',
               'Miss rate lectura [%]'] = total_read_miss_rate_436BC128

tabla_BC128.at['436.cactusADM-1804B',
               'Misses escritura'] = total_write_misses_436BC128

tabla_BC128.at['436.cactusADM-1804B',
               'Miss rate escritura [%]'] = total_write_miss_rate_436BC128

# **437.leslie3d-134B**

tabla_BC128.at['437.leslie3d-134B', 'Total Misses'] = total_misses_437BC128

tabla_BC128.at['437.leslie3d-134B',
               'Miss rate total [%]'] = total_miss_rate_437BC128

tabla_BC128.at['437.leslie3d-134B',
               'Misses lectura'] = total_read_misses_437BC128

tabla_BC128.at['437.leslie3d-134B',
               'Miss rate lectura [%]'] = total_read_miss_rate_437BC128

tabla_BC128.at['437.leslie3d-134B',
               'Misses escritura'] = total_write_misses_437BC128

tabla_BC128.at['437.leslie3d-134B',
               'Miss rate escritura [%]'] = total_write_miss_rate_437BC128

# **444.namd-120B**

tabla_BC128.at['444.namd-120B', 'Total Misses'] = total_misses_444BC128

tabla_BC128.at['444.namd-120B',
               'Miss rate total [%]'] = total_miss_rate_444BC128

tabla_BC128.at['444.namd-120B', 'Misses lectura'] = total_read_misses_444BC128

tabla_BC128.at['444.namd-120B',
               'Miss rate lectura [%]'] = total_read_miss_rate_444BC128

tabla_BC128.at['444.namd-120B',
               'Misses escritura'] = total_write_misses_444BC128

tabla_BC128.at['444.namd-120B',
               'Miss rate escritura [%]'] = total_write_miss_rate_444BC128

# **445.gobmk-17B**

tabla_BC128.at['445.gobmk-17B', 'Total Misses'] = total_misses_445BC128

tabla_BC128.at['445.gobmk-17B',
               'Miss rate total [%]'] = total_miss_rate_445BC128

tabla_BC128.at['445.gobmk-17B', 'Misses lectura'] = total_read_misses_445BC128

tabla_BC128.at['445.gobmk-17B',
               'Miss rate lectura [%]'] = total_read_miss_rate_445BC128

tabla_BC128.at['445.gobmk-17B',
               'Misses escritura'] = total_write_misses_445BC128

tabla_BC128.at['445.gobmk-17B',
               'Miss rate escritura [%]'] = total_write_miss_rate_445BC128

# **450.soplex-247B**

tabla_BC128.at['450.soplex-247B', 'Total Misses'] = total_misses_450BC128

tabla_BC128.at['450.soplex-247B',
               'Miss rate total [%]'] = total_miss_rate_450BC128

tabla_BC128.at['450.soplex-247B',
               'Misses lectura'] = total_read_misses_450BC128

tabla_BC128.at['450.soplex-247B',
               'Miss rate lectura [%]'] = total_read_miss_rate_450BC128

tabla_BC128.at['450.soplex-247B',
               'Misses escritura'] = total_write_misses_450BC128

tabla_BC128.at['450.soplex-247B',
               'Miss rate escritura [%]'] = total_write_miss_rate_450BC128

# **453.povray-887B**

tabla_BC128.at['453.povray-887B', 'Total Misses'] = total_misses_453BC128

tabla_BC128.at['453.povray-887B',
               'Miss rate total [%]'] = total_miss_rate_453BC128

tabla_BC128.at['453.povray-887B',
               'Misses lectura'] = total_read_misses_453BC128

tabla_BC128.at['453.povray-887B',
               'Miss rate lectura [%]'] = total_read_miss_rate_453BC128

tabla_BC128.at['453.povray-887B',
               'Misses escritura'] = total_write_misses_453BC128

tabla_BC128.at['453.povray-887B',
               'Miss rate escritura [%]'] = total_write_miss_rate_453BC128

# **454.calculix-104B**

tabla_BC128.at['454.calculix-104B', 'Total Misses'] = total_misses_454BC128

tabla_BC128.at['454.calculix-104B',
               'Miss rate total [%]'] = total_miss_rate_454BC128

tabla_BC128.at['454.calculix-104B',
               'Misses lectura'] = total_read_misses_454BC128

tabla_BC128.at['454.calculix-104B',
               'Miss rate lectura [%]'] = total_read_miss_rate_454BC128

tabla_BC128.at['454.calculix-104B',
               'Misses escritura'] = total_write_misses_454BC128

tabla_BC128.at['454.calculix-104B',
               'Miss rate escritura [%]'] = total_write_miss_rate_454BC128

# **456.hmmer-191B**

tabla_BC128.at['456.hmmer-191B', 'Total Misses'] = total_misses_456BC128

tabla_BC128.at['456.hmmer-191B',
               'Miss rate total [%]'] = total_miss_rate_456BC128

tabla_BC128.at['456.hmmer-191B', 'Misses lectura'] = total_read_misses_456BC128

tabla_BC128.at['456.hmmer-191B',
               'Miss rate lectura [%]'] = total_read_miss_rate_456BC128

tabla_BC128.at['456.hmmer-191B',
               'Misses escritura'] = total_write_misses_456BC128

tabla_BC128.at['456.hmmer-191B',
               'Miss rate escritura [%]'] = total_write_miss_rate_456BC128

# **458.sjeng-1088B**

tabla_BC128.at['458.sjeng-1088B', 'Total Misses'] = total_misses_458BC128

tabla_BC128.at['458.sjeng-1088B',
               'Miss rate total [%]'] = total_miss_rate_458BC128

tabla_BC128.at['458.sjeng-1088B',
               'Misses lectura'] = total_read_misses_458BC128

tabla_BC128.at['458.sjeng-1088B',
               'Miss rate lectura [%]'] = total_read_miss_rate_458BC128

tabla_BC128.at['458.sjeng-1088B',
               'Misses escritura'] = total_write_misses_458BC128

tabla_BC128.at['458.sjeng-1088B',
               'Miss rate escritura [%]'] = total_write_miss_rate_458BC128

# **459.GemsFDTD-1169B**

tabla_BC128.at['459.GemsFDTD-1169B', 'Total Misses'] = total_misses_459BC128

tabla_BC128.at['459.GemsFDTD-1169B',
               'Miss rate total [%]'] = total_miss_rate_459BC128

tabla_BC128.at['459.GemsFDTD-1169B',
               'Misses lectura'] = total_read_misses_459BC128

tabla_BC128.at['459.GemsFDTD-1169B',
               'Miss rate lectura [%]'] = total_read_miss_rate_459BC128

tabla_BC128.at['459.GemsFDTD-1169B',
               'Misses escritura'] = total_write_misses_459BC128

tabla_BC128.at['459.GemsFDTD-1169B',
               'Miss rate escritura [%]'] = total_write_miss_rate_459BC128

# **462.libquantum-1343B**

tabla_BC128.at['462.libquantum-1343B', 'Total Misses'] = total_misses_462BC128

tabla_BC128.at['462.libquantum-1343B',
               'Miss rate total [%]'] = total_miss_rate_462BC128

tabla_BC128.at['462.libquantum-1343B',
               'Misses lectura'] = total_read_misses_462BC128

tabla_BC128.at['462.libquantum-1343B',
               'Miss rate lectura [%]'] = total_read_miss_rate_462BC128

tabla_BC128.at['462.libquantum-1343B',
               'Misses escritura'] = total_write_misses_462BC128

tabla_BC128.at['462.libquantum-1343B',
               'Miss rate escritura [%]'] = total_write_miss_rate_462BC128

# **464.h264ref-30B**

tabla_BC128.at['464.h264ref-30B', 'Total Misses'] = total_misses_464BC128

tabla_BC128.at['464.h264ref-30B',
               'Miss rate total [%]'] = total_miss_rate_464BC128

tabla_BC128.at['464.h264ref-30B',
               'Misses lectura'] = total_read_misses_464BC128

tabla_BC128.at['464.h264ref-30B',
               'Miss rate lectura [%]'] = total_read_miss_rate_464BC128

tabla_BC128.at['464.h264ref-30B',
               'Misses escritura'] = total_write_misses_464BC128

tabla_BC128.at['464.h264ref-30B',
               'Miss rate escritura [%]'] = total_write_miss_rate_464BC128

# **465.tonto-1769B**

tabla_BC128.at['465.tonto-1769B', 'Total Misses'] = total_misses_465BC128

tabla_BC128.at['465.tonto-1769B',
               'Miss rate total [%]'] = total_miss_rate_465BC128

tabla_BC128.at['465.tonto-1769B',
               'Misses lectura'] = total_read_misses_465BC128

tabla_BC128.at['465.tonto-1769B',
               'Miss rate lectura [%]'] = total_read_miss_rate_465BC128

tabla_BC128.at['465.tonto-1769B',
               'Misses escritura'] = total_write_misses_465BC128
tabla_BC128.at['465.tonto-1769B',
               'Miss rate escritura [%]'] = total_write_miss_rate_465BC128

# **470.lbm-1274B**

tabla_BC128.at['470.lbm-1274B', 'Total Misses'] = total_misses_470BC128

tabla_BC128.at['470.lbm-1274B',
               'Miss rate total [%]'] = total_miss_rate_470BC128

tabla_BC128.at['470.lbm-1274B', 'Misses lectura'] = total_read_misses_470BC128

tabla_BC128.at['470.lbm-1274B',
               'Miss rate lectura [%]'] = total_read_miss_rate_470BC128

tabla_BC128.at['470.lbm-1274B',
               'Misses escritura'] = total_write_misses_470BC128

tabla_BC128.at['470.lbm-1274B',
               'Miss rate escritura [%]'] = total_write_miss_rate_470BC128

# **471.omnetpp-188B**

tabla_BC128.at['471.omnetpp-188B', 'Total Misses'] = total_misses_471BC128

tabla_BC128.at['471.omnetpp-188B',
               'Miss rate total [%]'] = total_miss_rate_471BC128

tabla_BC128.at['471.omnetpp-188B',
               'Misses lectura'] = total_read_misses_471BC128

tabla_BC128.at['471.omnetpp-188B',
               'Miss rate lectura [%]'] = total_read_miss_rate_471BC128

tabla_BC128.at['471.omnetpp-188B',
               'Misses escritura'] = total_write_misses_471BC128

tabla_BC128.at['471.omnetpp-188B',
               'Miss rate escritura [%]'] = total_write_miss_rate_471BC128

# **473.astar-153B**

tabla_BC128.at['473.astar-153B', 'Total Misses'] = total_misses_473BC128

tabla_BC128.at['473.astar-153B',
               'Miss rate total [%]'] = total_miss_rate_473BC128

tabla_BC128.at['473.astar-153B', 'Misses lectura'] = total_read_misses_473BC128

tabla_BC128.at['473.astar-153B',
               'Miss rate lectura [%]'] = total_read_miss_rate_473BC128

tabla_BC128.at['473.astar-153B',
               'Misses escritura'] = total_write_misses_473BC128

tabla_BC128.at['473.astar-153B',
               'Miss rate escritura [%]'] = total_write_miss_rate_473BC128

# **481.wrf-1170B**

tabla_BC128.at['481.wrf-1170B', 'Total Misses'] = total_misses_481BC128

tabla_BC128.at['481.wrf-1170B',
               'Miss rate total [%]'] = total_miss_rate_481BC128

tabla_BC128.at['481.wrf-1170B', 'Misses lectura'] = total_read_misses_481BC128

tabla_BC128.at['481.wrf-1170B',
               'Miss rate lectura [%]'] = total_read_miss_rate_481BC128

tabla_BC128.at['481.wrf-1170B',
               'Misses escritura'] = total_write_misses_481BC128

tabla_BC128.at['481.wrf-1170B',
               'Miss rate escritura [%]'] = total_write_miss_rate_481BC128

# **482.sphinx3-1100B**

tabla_BC128.at['482.sphinx3-1100B', 'Total Misses'] = total_misses_482BC128

tabla_BC128.at['482.sphinx3-1100B',
               'Miss rate total [%]'] = total_miss_rate_482BC128

tabla_BC128.at['482.sphinx3-1100B',
               'Misses lectura'] = total_read_misses_482BC128

tabla_BC128.at['482.sphinx3-1100B',
               'Miss rate lectura [%]'] = total_read_miss_rate_482BC128

tabla_BC128.at['482.sphinx3-1100B',
               'Misses escritura'] = total_write_misses_482BC128

tabla_BC128.at['482.sphinx3-1100B',
               'Miss rate escritura [%]'] = total_write_miss_rate_482BC128

# **483.xalancbmk-127B**

tabla_BC128.at['483.xalancbmk-127B', 'Total Misses'] = total_misses_483BC128

tabla_BC128.at['483.xalancbmk-127B',
               'Miss rate total [%]'] = total_miss_rate_483BC128

tabla_BC128.at['483.xalancbmk-127B',
               'Misses lectura'] = total_read_misses_483BC128

tabla_BC128.at['483.xalancbmk-127B',
               'Miss rate lectura [%]'] = total_read_miss_rate_483BC128

tabla_BC128.at['483.xalancbmk-127B',
               'Misses escritura'] = total_write_misses_483BC128

tabla_BC128.at['483.xalancbmk-127B',
               'Miss rate escritura [%]'] = total_write_miss_rate_483BC128

print(">>>>>All BC128 data has been uploaded successfully")

###########
# GEO MEAN#
###########

# GEO MEAN Miss rate total BC16
columna_BC16 = tabla_BC16['Miss rate total [%]']
columna_BC16_numpy = columna_BC16.to_numpy(dtype=np.float64)
GEOMEAN_Miss_rate_total_BC16 = gmean(columna_BC16_numpy)

# GEO MEAN Miss rate total BC32
columna_BC32 = tabla_BC32['Miss rate total [%]']
columna_BC32_numpy = columna_BC32.to_numpy(dtype=np.float64)
GEOMEAN_Miss_rate_total_BC32 = gmean(columna_BC32_numpy)

# GEO MEAN Miss rate total BC64
columna_BC64 = tabla_BC64['Miss rate total [%]']
columna_BC64_numpy = columna_BC64.to_numpy(dtype=np.float64)
GEOMEAN_Miss_rate_total_BC64 = gmean(columna_BC64_numpy)

# GEO MEAN Miss rate total BC128
columna_BC128 = tabla_BC128['Miss rate total [%]']
columna_BC128_numpy = columna_BC128.to_numpy(dtype=np.float64)
GEOMEAN_Miss_rate_total_BC128 = gmean(columna_BC128_numpy)

#############################################################################
# Dataframes de resultados: miss rate total, Miss rate total 401.bzip2-226B#
#############################################################################

# Creación de tablas para adjuntar valores

# Miss rate
tabla_miss_rate_total = pd.DataFrame(index=[
    'Miss rate total [%]'], columns=[
    'Parámetro', '16kB', '32kB', '64kB', '128kB'])
tabla_miss_rate_total['Parámetro'] = tabla_miss_rate_total.index


# Miss rate 465.tonto-1769B
tabla_miss_rate_total_401_bzip2_226B = pd.DataFrame(index=[
    'Miss rate total 401.bzip2-226B [%]'], columns=[
    'Parámetro', '16kB', '32kB', '64kB', '128kB'])
tabla_miss_rate_total_401_bzip2_226B['Parámetro'] = tabla_miss_rate_total_401_bzip2_226B.index

##############################
# Adjunta datos en dataframes#
##############################

# Miss rate total
tabla_miss_rate_total.at['Miss rate total [%]',
                         '16kB'] = GEOMEAN_Miss_rate_total_BC16
tabla_miss_rate_total.at['Miss rate total [%]',
                         '32kB'] = GEOMEAN_Miss_rate_total_BC32
tabla_miss_rate_total.at['Miss rate total [%]',
                         '64kB'] = GEOMEAN_Miss_rate_total_BC64
tabla_miss_rate_total.at['Miss rate total [%]',
                         '128kB'] = GEOMEAN_Miss_rate_total_BC128

# Miss rate total 465.tonto_1769B
tabla_miss_rate_total_401_bzip2_226B.at['Miss rate total 401.bzip2-226B [%]',
                                        '16kB'] = total_miss_rate_465BC16
tabla_miss_rate_total_401_bzip2_226B.at['Miss rate total 401.bzip2-226B [%]',
                                        '32kB'] = total_miss_rate_465BC32
tabla_miss_rate_total_401_bzip2_226B.at['Miss rate total 401.bzip2-226B [%]',
                                        '64kB'] = total_miss_rate_465BC64
tabla_miss_rate_total_401_bzip2_226B.at['Miss rate total 401.bzip2-226B [%]',
                                        '128kB'] = total_miss_rate_465BC128

############################################
# Archivo de salida para facilitar gráficos#
############################################

# Create an Excel writer using pandas
output = pd.ExcelWriter('Results_BC.xlsx')

# Write each dataframe to a different sheet in the Excel file
tabla_BC16.to_excel(output, sheet_name='BC16', index=False)
tabla_BC32.to_excel(output, sheet_name='BC32', index=False)
tabla_BC64.to_excel(output, sheet_name='BC64', index=False)
tabla_BC128.to_excel(output, sheet_name='BC128', index=False)
tabla_miss_rate_total.to_excel(
    output, sheet_name='Miss rate total promedio', index=False)
tabla_miss_rate_total_401_bzip2_226B.to_excel(
    output, sheet_name='Miss rate total promedio 401.bzip2-226B', index=False)

# Save the Excel file
output.save()

print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''' Tamaño bloque de caché 16''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
print(tabla_BC16.to_string(index=False))
print("##################################################################################")
print("El miss rate promedio [%] con un tamaño bloque de caché de 16kB es: ",
      GEOMEAN_Miss_rate_total_BC16, '#')
print("")
print("##################################################################################")
print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''' Tamaño bloque de caché 32''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
print(tabla_BC32.to_string(index=False))
print("##################################################################################")
print("El miss rate promedio [%] con un tamaño bloque de caché de 32kB es: ",
      GEOMEAN_Miss_rate_total_BC32, '#')
print("")
print("##################################################################################")
print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''' Tamaño bloque de caché 64''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
print(tabla_BC64.to_string(index=False))
print("##################################################################################")
print("El miss rate promedio [%] con un tamaño bloque de caché de 64kB es: ",
      GEOMEAN_Miss_rate_total_BC64, '#')
print("##################################################################################")
print("")
print("##################################################################################")
print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''' Tamaño bloque de caché 128''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
print(tabla_BC128.to_string(index=False))
print("##################################################################################")
print("El miss rate promedio [%] con un tamaño bloque de caché de 128kB es: ",
      GEOMEAN_Miss_rate_total_BC128, '#')
print("##################################################################################")
print("")
print("##################################################################################")
print("''''''''''''''''''''''''''' Miss rate total'''''''''''''''''''''''''''''")
print(tabla_miss_rate_total.to_string(index=False))
print("")
print("##################################################################################")
print("''''''''''''''''' Miss rate total 401.bzip2-226B'''''''''''''''''''''")
print(tabla_miss_rate_total_401_bzip2_226B.to_string(index=False))
