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


######################################################################
# Extractor para experimento con asociatividad de caché mapeo directo#
######################################################################


# Creación de tablas para adjuntar valores
# Una tabla por tamaño
tabla_AC1 = pd.DataFrame(index=[
    '400.perlbench-41B', '401.bzip2-226B', '403.gcc-16B', '410.bwaves-1963B', '416.gamess-875B', '429.mcf-184B', '433.milc-127B',
    '435.gromacs-111B', '436.cactusADM-1804B', '437.leslie3d-134B', '444.namd-120B', '445.gobmk-17B',
    '450.soplex-247B', '453.povray-887B', '454.calculix-104B', '456.hmmer-191B', '458.sjeng-1088B', '459.GemsFDTD-1169B',
    '462.libquantum-1343B', '464.h264ref-30B', '465.tonto-1769B', '470.lbm-1274B', '471.omnetpp-188B', '473.astar-153B', '481.wrf-1170B',
    '482.sphinx3-1100B', '483.xalancbmk-127B'], columns=[
    'App', 'Total Misses', 'Miss rate total [%]', 'Misses lectura', 'Miss rate lectura [%]', 'Misses escritura', 'Miss rate escritura [%]'])
tabla_AC1['App'] = tabla_AC1.index

# Files paths
filename_1 = "RESULTS_AC/400AC1.txt"
filename_2 = "RESULTS_AC/401AC1.txt"
filename_3 = "RESULTS_AC/403AC1.txt"
filename_4 = "RESULTS_AC/410AC1.txt"
filename_5 = "RESULTS_AC/416AC1.txt"
filename_6 = "RESULTS_AC/429AC1.txt"
filename_7 = "RESULTS_AC/433AC1.txt"
filename_8 = "RESULTS_AC/435AC1.txt"
filename_9 = "RESULTS_AC/436AC1.txt"
filename_10 = "RESULTS_AC/437AC1.txt"
filename_11 = "RESULTS_AC/444AC1.txt"
filename_12 = "RESULTS_AC/445AC1.txt"
filename_13 = "RESULTS_AC/450AC1.txt"
filename_14 = "RESULTS_AC/453AC1.txt"
filename_15 = "RESULTS_AC/454AC1.txt"
filename_16 = "RESULTS_AC/456AC1.txt"
filename_17 = "RESULTS_AC/458AC1.txt"
filename_18 = "RESULTS_AC/459AC1.txt"
filename_19 = "RESULTS_AC/462AC1.txt"
filename_20 = "RESULTS_AC/464AC1.txt"
filename_21 = "RESULTS_AC/465AC1.txt"
filename_22 = "RESULTS_AC/470AC1.txt"
filename_23 = "RESULTS_AC/471AC1.txt"
filename_24 = "RESULTS_AC/473AC1.txt"
filename_25 = "RESULTS_AC/481AC1.txt"
filename_26 = "RESULTS_AC/482AC1.txt"
filename_27 = "RESULTS_AC/483AC1.txt"


# Content file extracter
with open(filename_1, 'r') as file:
    content_400AC1 = file.read()
with open(filename_2, 'r') as file:
    content_401AC1 = file.read()
with open(filename_3, 'r') as file:
    content_403AC1 = file.read()
with open(filename_4, 'r') as file:
    content_410AC1 = file.read()
with open(filename_5, 'r') as file:
    content_416AC1 = file.read()
with open(filename_6, 'r') as file:
    content_429AC1 = file.read()
with open(filename_7, 'r') as file:
    content_433AC1 = file.read()
with open(filename_8, 'r') as file:
    content_435AC1 = file.read()
with open(filename_9, 'r') as file:
    content_436AC1 = file.read()
with open(filename_10, 'r') as file:
    content_437AC1 = file.read()
with open(filename_11, 'r') as file:
    content_444AC1 = file.read()
with open(filename_12, 'r') as file:
    content_445AC1 = file.read()
with open(filename_13, 'r') as file:
    content_450AC1 = file.read()
with open(filename_14, 'r') as file:
    content_453AC1 = file.read()
with open(filename_15, 'r') as file:
    content_454AC1 = file.read()
with open(filename_16, 'r') as file:
    content_456AC1 = file.read()
with open(filename_17, 'r') as file:
    content_458AC1 = file.read()
with open(filename_18, 'r') as file:
    content_459AC1 = file.read()
with open(filename_19, 'r') as file:
    content_462AC1 = file.read()
with open(filename_20, 'r') as file:
    content_464AC1 = file.read()
with open(filename_21, 'r') as file:
    content_465AC1 = file.read()
with open(filename_22, 'r') as file:
    content_470AC1 = file.read()
with open(filename_23, 'r') as file:
    content_471AC1 = file.read()
with open(filename_24, 'r') as file:
    content_473AC1 = file.read()
with open(filename_25, 'r') as file:
    content_481AC1 = file.read()
with open(filename_26, 'r') as file:
    content_482AC1 = file.read()
with open(filename_27, 'r') as file:
    content_483AC1 = file.read()


# Variables según aplicación

# 400.pearlbench-41B
total_misses_400AC1 = re.search(r"Total_misses (\d+)", content_400AC1).group(1)
total_miss_rate_400AC1 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_400AC1).group(1)
total_read_misses_400AC1 = re.search(
    r"Total_read_misses (\d+)", content_400AC1).group(1)
total_read_miss_rate_400AC1 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_400AC1).group(1)
total_write_misses_400AC1 = re.search(
    r"Total_write_misses (\d+)", content_400AC1).group(1)
total_write_miss_rate_400AC1 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_400AC1).group(1)
print(">>>>>All AC1 400.pearlbench-41B variables where obtained successfully")

# 401.bzip2-226B
total_misses_401AC1 = re.search(r"Total_misses (\d+)", content_401AC1).group(1)
total_miss_rate_401AC1 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_401AC1).group(1)
total_read_misses_401AC1 = re.search(
    r"Total_read_misses (\d+)", content_401AC1).group(1)
total_read_miss_rate_401AC1 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_401AC1).group(1)
total_write_misses_401AC1 = re.search(
    r"Total_write_misses (\d+)", content_401AC1).group(1)
total_write_miss_rate_401AC1 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_401AC1).group(1)
print(">>>>>All AC1 401.bzip2-226B variables where obtained successfully")

# 403.gcc-16B
total_misses_403AC1 = re.search(r"Total_misses (\d+)", content_403AC1).group(1)
total_miss_rate_403AC1 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_403AC1).group(1)
total_read_misses_403AC1 = re.search(
    r"Total_read_misses (\d+)", content_403AC1).group(1)
total_read_miss_rate_403AC1 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_403AC1).group(1)
total_write_misses_403AC1 = re.search(
    r"Total_write_misses (\d+)", content_403AC1).group(1)
total_write_miss_rate_403AC1 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_403AC1).group(1)
print(">>>>>All AC1 403.gcc-16B variables where obtained successfully")

# 410.bwaves-1963B
total_misses_410AC1 = re.search(r"Total_misses (\d+)", content_410AC1).group(1)
total_miss_rate_410AC1 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_410AC1).group(1)
total_read_misses_410AC1 = re.search(
    r"Total_read_misses (\d+)", content_410AC1).group(1)
total_read_miss_rate_410AC1 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_410AC1).group(1)
total_write_misses_410AC1 = re.search(
    r"Total_write_misses (\d+)", content_410AC1).group(1)
total_write_miss_rate_410AC1 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_410AC1).group(1)
print(">>>>>All AC1 410.bwaves-1963B variables where obtained successfully")

# 416.gamess-875B
total_misses_416AC1 = re.search(r"Total_misses (\d+)", content_416AC1).group(1)
total_miss_rate_416AC1 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_416AC1).group(1)
total_read_misses_416AC1 = re.search(
    r"Total_read_misses (\d+)", content_416AC1).group(1)
total_read_miss_rate_416AC1 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_416AC1).group(1)
total_write_misses_416AC1 = re.search(
    r"Total_write_misses (\d+)", content_416AC1).group(1)
total_write_miss_rate_416AC1 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_416AC1).group(1)
print(">>>>>All AC1 416.gamess-875B variables where obtained successfully")

# 429.mcf-184B
total_misses_429AC1 = re.search(r"Total_misses (\d+)", content_429AC1).group(1)
total_miss_rate_429AC1 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_429AC1).group(1)
total_read_misses_429AC1 = re.search(
    r"Total_read_misses (\d+)", content_429AC1).group(1)
total_read_miss_rate_429AC1 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_429AC1).group(1)
total_write_misses_429AC1 = re.search(
    r"Total_write_misses (\d+)", content_429AC1).group(1)
total_write_miss_rate_429AC1 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_429AC1).group(1)
print(">>>>>All AC1 429.mcf-184B variables where obtained successfully")

# 433.milc-127B
total_misses_433AC1 = re.search(r"Total_misses (\d+)", content_433AC1).group(1)
total_miss_rate_433AC1 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_433AC1).group(1)
total_read_misses_433AC1 = re.search(
    r"Total_read_misses (\d+)", content_433AC1).group(1)
total_read_miss_rate_433AC1 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_433AC1).group(1)
total_write_misses_433AC1 = re.search(
    r"Total_write_misses (\d+)", content_433AC1).group(1)
total_write_miss_rate_433AC1 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_433AC1).group(1)
print(">>>>>All AC1 433.milc-127B variables where obtained successfully")

# 435.gromacs-111B
total_misses_435AC1 = re.search(r"Total_misses (\d+)", content_435AC1).group(1)
total_miss_rate_435AC1 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_435AC1).group(1)
total_read_misses_435AC1 = re.search(
    r"Total_read_misses (\d+)", content_435AC1).group(1)
total_read_miss_rate_435AC1 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_435AC1).group(1)
total_write_misses_435AC1 = re.search(
    r"Total_write_misses (\d+)", content_435AC1).group(1)
total_write_miss_rate_435AC1 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_435AC1).group(1)
print(">>>>>All AC1 435.gromacs-111B variables where obtained successfully")

# 436.cactusADM-1804B
total_misses_436AC1 = re.search(r"Total_misses (\d+)", content_436AC1).group(1)
total_miss_rate_436AC1 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_436AC1).group(1)
total_read_misses_436AC1 = re.search(
    r"Total_read_misses (\d+)", content_436AC1).group(1)
total_read_miss_rate_436AC1 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_436AC1).group(1)
total_write_misses_436AC1 = re.search(
    r"Total_write_misses (\d+)", content_436AC1).group(1)
total_write_miss_rate_436AC1 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_436AC1).group(1)
print(">>>>>All AC1 436.cactusADM-1804B variables where obtained successfully")

# 437.leslie3d-134B
total_misses_437AC1 = re.search(r"Total_misses (\d+)", content_437AC1).group(1)
total_miss_rate_437AC1 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_437AC1).group(1)
total_read_misses_437AC1 = re.search(
    r"Total_read_misses (\d+)", content_437AC1).group(1)
total_read_miss_rate_437AC1 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_437AC1).group(1)
total_write_misses_437AC1 = re.search(
    r"Total_write_misses (\d+)", content_437AC1).group(1)
total_write_miss_rate_437AC1 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_437AC1).group(1)
print(">>>>>All AC1 437.leslie3d-134B variables where obtained successfully")

# 444.namd-120B
total_misses_444AC1 = re.search(r"Total_misses (\d+)", content_444AC1).group(1)
total_miss_rate_444AC1 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_444AC1).group(1)
total_read_misses_444AC1 = re.search(
    r"Total_read_misses (\d+)", content_444AC1).group(1)
total_read_miss_rate_444AC1 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_444AC1).group(1)
total_write_misses_444AC1 = re.search(
    r"Total_write_misses (\d+)", content_444AC1).group(1)
total_write_miss_rate_444AC1 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_444AC1).group(1)
print(">>>>>All AC1 444.namd-120B variables where obtained successfully")

# 445.gobmk-17B
total_misses_445AC1 = re.search(r"Total_misses (\d+)", content_445AC1).group(1)
total_miss_rate_445AC1 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_445AC1).group(1)
total_read_misses_445AC1 = re.search(
    r"Total_read_misses (\d+)", content_445AC1).group(1)
total_read_miss_rate_445AC1 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_445AC1).group(1)
total_write_misses_445AC1 = re.search(
    r"Total_write_misses (\d+)", content_445AC1).group(1)
total_write_miss_rate_445AC1 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_445AC1).group(1)
print(">>>>>All AC1 445.gobmk-17B variables where obtained successfully")

# 450.soplex-247B
total_misses_450AC1 = re.search(r"Total_misses (\d+)", content_450AC1).group(1)
total_miss_rate_450AC1 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_450AC1).group(1)
total_read_misses_450AC1 = re.search(
    r"Total_read_misses (\d+)", content_450AC1).group(1)
total_read_miss_rate_450AC1 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_450AC1).group(1)
total_write_misses_450AC1 = re.search(
    r"Total_write_misses (\d+)", content_450AC1).group(1)
total_write_miss_rate_450AC1 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_450AC1).group(1)
print(">>>>>All AC1 450.soplex-247B variables where obtained successfully")

# 453.povray-887B
total_misses_453AC1 = re.search(r"Total_misses (\d+)", content_453AC1).group(1)
total_miss_rate_453AC1 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_453AC1).group(1)
total_read_misses_453AC1 = re.search(
    r"Total_read_misses (\d+)", content_453AC1).group(1)
total_read_miss_rate_453AC1 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_453AC1).group(1)
total_write_misses_453AC1 = re.search(
    r"Total_write_misses (\d+)", content_453AC1).group(1)
total_write_miss_rate_453AC1 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_453AC1).group(1)
print(">>>>>All AC1 453.povray-887B variables where obtained successfully")

# 454.calculix-104B
total_misses_454AC1 = re.search(r"Total_misses (\d+)", content_454AC1).group(1)
total_miss_rate_454AC1 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_454AC1).group(1)
total_read_misses_454AC1 = re.search(
    r"Total_read_misses (\d+)", content_454AC1).group(1)
total_read_miss_rate_454AC1 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_454AC1).group(1)
total_write_misses_454AC1 = re.search(
    r"Total_write_misses (\d+)", content_454AC1).group(1)
total_write_miss_rate_454AC1 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_454AC1).group(1)
print(">>>>>All AC1 454.calculix-104B variables where obtained successfully")

# 456.hmmer-191B
total_misses_456AC1 = re.search(r"Total_misses (\d+)", content_456AC1).group(1)
total_miss_rate_456AC1 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_456AC1).group(1)
total_read_misses_456AC1 = re.search(
    r"Total_read_misses (\d+)", content_456AC1).group(1)
total_read_miss_rate_456AC1 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_456AC1).group(1)
total_write_misses_456AC1 = re.search(
    r"Total_write_misses (\d+)", content_456AC1).group(1)
total_write_miss_rate_456AC1 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_456AC1).group(1)
print(">>>>>All AC1 456.hmmer-191B variables where obtained successfully")

# 458.sjeng-1088B
total_misses_458AC1 = re.search(r"Total_misses (\d+)", content_458AC1).group(1)
total_miss_rate_458AC1 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_458AC1).group(1)
total_read_misses_458AC1 = re.search(
    r"Total_read_misses (\d+)", content_458AC1).group(1)
total_read_miss_rate_458AC1 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_458AC1).group(1)
total_write_misses_458AC1 = re.search(
    r"Total_write_misses (\d+)", content_458AC1).group(1)
total_write_miss_rate_458AC1 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_458AC1).group(1)
print(">>>>>All AC1 458.sjeng-1088B variables where obtained successfully")

# 459.GemsFDTD-1169B
total_misses_459AC1 = re.search(r"Total_misses (\d+)", content_459AC1).group(1)
total_miss_rate_459AC1 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_459AC1).group(1)
total_read_misses_459AC1 = re.search(
    r"Total_read_misses (\d+)", content_459AC1).group(1)
total_read_miss_rate_459AC1 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_459AC1).group(1)
total_write_misses_459AC1 = re.search(
    r"Total_write_misses (\d+)", content_459AC1).group(1)
total_write_miss_rate_459AC1 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_459AC1).group(1)
print(">>>>>All AC1 459.GemsFDTD-1169B variables where obtained successfully")

# 462.libquantum-1343B
total_misses_462AC1 = re.search(r"Total_misses (\d+)", content_462AC1).group(1)
total_miss_rate_462AC1 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_462AC1).group(1)
total_read_misses_462AC1 = re.search(
    r"Total_read_misses (\d+)", content_462AC1).group(1)
total_read_miss_rate_462AC1 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_462AC1).group(1)
total_write_misses_462AC1 = re.search(
    r"Total_write_misses (\d+)", content_462AC1).group(1)
total_write_miss_rate_462AC1 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_462AC1).group(1)
print(">>>>>All AC1 462.libquantum-1343B variables where obtained successfully")

# 464.h264ref-30B
total_misses_464AC1 = re.search(r"Total_misses (\d+)", content_464AC1).group(1)
total_miss_rate_464AC1 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_464AC1).group(1)
total_read_misses_464AC1 = re.search(
    r"Total_read_misses (\d+)", content_464AC1).group(1)
total_read_miss_rate_464AC1 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_464AC1).group(1)
total_write_misses_464AC1 = re.search(
    r"Total_write_misses (\d+)", content_464AC1).group(1)
total_write_miss_rate_464AC1 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_464AC1).group(1)
print(">>>>>All AC1 464.h264ref-30B variables where obtained successfully")

# 465.tonto-1769B
total_misses_465AC1 = re.search(r"Total_misses (\d+)", content_465AC1).group(1)
total_miss_rate_465AC1 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_465AC1).group(1)
total_read_misses_465AC1 = re.search(
    r"Total_read_misses (\d+)", content_465AC1).group(1)
total_read_miss_rate_465AC1 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_465AC1).group(1)
total_write_misses_465AC1 = re.search(
    r"Total_write_misses (\d+)", content_465AC1).group(1)
total_write_miss_rate_465AC1 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_465AC1).group(1)
print(">>>>>All AC1 465.tonto-1769B variables where obtained successfully")

# 470.lbm-1274B
total_misses_470AC1 = re.search(r"Total_misses (\d+)", content_470AC1).group(1)
total_miss_rate_470AC1 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_470AC1).group(1)
total_read_misses_470AC1 = re.search(
    r"Total_read_misses (\d+)", content_470AC1).group(1)
total_read_miss_rate_470AC1 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_470AC1).group(1)
total_write_misses_470AC1 = re.search(
    r"Total_write_misses (\d+)", content_470AC1).group(1)
total_write_miss_rate_470AC1 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_470AC1).group(1)
print(">>>>>All AC1 470.lbm-1274B variables where obtained successfully")

# 471.omnetpp-188B
total_misses_471AC1 = re.search(r"Total_misses (\d+)", content_471AC1).group(1)
total_miss_rate_471AC1 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_471AC1).group(1)
total_read_misses_471AC1 = re.search(
    r"Total_read_misses (\d+)", content_471AC1).group(1)
total_read_miss_rate_471AC1 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_471AC1).group(1)
total_write_misses_471AC1 = re.search(
    r"Total_write_misses (\d+)", content_471AC1).group(1)
total_write_miss_rate_471AC1 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_471AC1).group(1)
print(">>>>>All AC1 471.omnetpp-188B variables where obtained successfully")

# 473.astar-153B
total_misses_473AC1 = re.search(r"Total_misses (\d+)", content_473AC1).group(1)
total_miss_rate_473AC1 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_473AC1).group(1)
total_read_misses_473AC1 = re.search(
    r"Total_read_misses (\d+)", content_473AC1).group(1)
total_read_miss_rate_473AC1 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_473AC1).group(1)
total_write_misses_473AC1 = re.search(
    r"Total_write_misses (\d+)", content_473AC1).group(1)
total_write_miss_rate_473AC1 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_473AC1).group(1)
print(">>>>>All AC1 473.astar-153B variables where obtained successfully")

# 481.wrf-1170B
total_misses_481AC1 = re.search(r"Total_misses (\d+)", content_481AC1).group(1)
total_miss_rate_481AC1 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_481AC1).group(1)
total_read_misses_481AC1 = re.search(
    r"Total_read_misses (\d+)", content_481AC1).group(1)
total_read_miss_rate_481AC1 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_481AC1).group(1)
total_write_misses_481AC1 = re.search(
    r"Total_write_misses (\d+)", content_481AC1).group(1)
total_write_miss_rate_481AC1 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_481AC1).group(1)
print(">>>>>All AC1 481.wrf-1170B variables where obtained successfully")

# 482.sphinx3-1100B
total_misses_482AC1 = re.search(r"Total_misses (\d+)", content_482AC1).group(1)
total_miss_rate_482AC1 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_482AC1).group(1)
total_read_misses_482AC1 = re.search(
    r"Total_read_misses (\d+)", content_482AC1).group(1)
total_read_miss_rate_482AC1 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_482AC1).group(1)
total_write_misses_482AC1 = re.search(
    r"Total_write_misses (\d+)", content_482AC1).group(1)
total_write_miss_rate_482AC1 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_482AC1).group(1)
print(">>>>>All AC1 482.sphinx3-1100B variables where obtained successfully")

# 483.xalancbmk-127B
total_misses_483AC1 = re.search(r"Total_misses (\d+)", content_483AC1).group(1)
total_miss_rate_483AC1 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_483AC1).group(1)
total_read_misses_483AC1 = re.search(
    r"Total_read_misses (\d+)", content_483AC1).group(1)
total_read_miss_rate_483AC1 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_483AC1).group(1)
total_write_misses_483AC1 = re.search(
    r"Total_write_misses (\d+)", content_483AC1).group(1)
total_write_miss_rate_483AC1 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_483AC1).group(1)
print(">>>>>All AC1 483.xalancbmk-127B variables where obtained successfully")


#############################
# Adjunta datos a dataframe #
#############################

# **400.perlbench-41B**

tabla_AC1.at['400.perlbench-41B', 'Total Misses'] = total_misses_400AC1

tabla_AC1.at['400.perlbench-41B',
             'Miss rate total [%]'] = total_miss_rate_400AC1

tabla_AC1.at['400.perlbench-41B', 'Misses lectura'] = total_read_misses_400AC1

tabla_AC1.at['400.perlbench-41B',
             'Miss rate lectura [%]'] = total_read_miss_rate_400AC1

tabla_AC1.at['400.perlbench-41B',
             'Misses escritura'] = total_write_misses_400AC1

tabla_AC1.at['400.perlbench-41B',
             'Miss rate escritura [%]'] = total_write_miss_rate_400AC1

# **401.bzip2-226B**

tabla_AC1.at['401.bzip2-226B', 'Total Misses'] = total_misses_401AC1

tabla_AC1.at['401.bzip2-226B', 'Miss rate total [%]'] = total_miss_rate_401AC1

tabla_AC1.at['401.bzip2-226B', 'Misses lectura'] = total_read_misses_401AC1

tabla_AC1.at['401.bzip2-226B',
             'Miss rate lectura [%]'] = total_read_miss_rate_401AC1

tabla_AC1.at['401.bzip2-226B',
             'Misses escritura'] = total_write_misses_401AC1

tabla_AC1.at['401.bzip2-226B',
             'Miss rate escritura [%]'] = total_write_miss_rate_401AC1

# **403.gcc-16B**

tabla_AC1.at['403.gcc-16B', 'Total Misses'] = total_misses_403AC1

tabla_AC1.at['403.gcc-16B', 'Miss rate total [%]'] = total_miss_rate_403AC1

tabla_AC1.at['403.gcc-16B', 'Misses lectura'] = total_read_misses_403AC1

tabla_AC1.at['403.gcc-16B',
             'Miss rate lectura [%]'] = total_read_miss_rate_403AC1

tabla_AC1.at['403.gcc-16B',
             'Misses escritura'] = total_write_misses_403AC1

tabla_AC1.at['403.gcc-16B',
             'Miss rate escritura [%]'] = total_write_miss_rate_403AC1

# **410.bwaves-1963B**

tabla_AC1.at['410.bwaves-1963B', 'Total Misses'] = total_misses_410AC1

tabla_AC1.at['410.bwaves-1963B',
             'Miss rate total [%]'] = total_miss_rate_410AC1

tabla_AC1.at['410.bwaves-1963B', 'Misses lectura'] = total_read_misses_410AC1

tabla_AC1.at['410.bwaves-1963B',
             'Miss rate lectura [%]'] = total_read_miss_rate_410AC1

tabla_AC1.at['410.bwaves-1963B',
             'Misses escritura'] = total_write_misses_410AC1

tabla_AC1.at['410.bwaves-1963B',
             'Miss rate escritura [%]'] = total_write_miss_rate_410AC1

# **416.gamess-875B**

tabla_AC1.at['416.gamess-875B', 'Total Misses'] = total_misses_416AC1

tabla_AC1.at['416.gamess-875B', 'Miss rate total [%]'] = total_miss_rate_416AC1

tabla_AC1.at['416.gamess-875B', 'Misses lectura'] = total_read_misses_416AC1

tabla_AC1.at['416.gamess-875B',
             'Miss rate lectura [%]'] = total_read_miss_rate_416AC1

tabla_AC1.at['416.gamess-875B',
             'Misses escritura'] = total_write_misses_416AC1

tabla_AC1.at['416.gamess-875B',
             'Miss rate escritura [%]'] = total_write_miss_rate_416AC1

# **429.mcf-184B**

tabla_AC1.at['429.mcf-184B', 'Total Misses'] = total_misses_429AC1

tabla_AC1.at['429.mcf-184B', 'Miss rate total [%]'] = total_miss_rate_429AC1

tabla_AC1.at['429.mcf-184B', 'Misses lectura'] = total_read_misses_429AC1

tabla_AC1.at['429.mcf-184B',
             'Miss rate lectura [%]'] = total_read_miss_rate_429AC1

tabla_AC1.at['429.mcf-184B',
             'Misses escritura'] = total_write_misses_429AC1

tabla_AC1.at['429.mcf-184B',
             'Miss rate escritura [%]'] = total_write_miss_rate_429AC1

# **433.milc-127B**

tabla_AC1.at['433.milc-127B', 'Total Misses'] = total_misses_433AC1

tabla_AC1.at['433.milc-127B', 'Miss rate total [%]'] = total_miss_rate_433AC1

tabla_AC1.at['433.milc-127B', 'Misses lectura'] = total_read_misses_433AC1

tabla_AC1.at['433.milc-127B',
             'Miss rate lectura [%]'] = total_read_miss_rate_433AC1

tabla_AC1.at['433.milc-127B',
             'Misses escritura'] = total_write_misses_433AC1

tabla_AC1.at['433.milc-127B',
             'Miss rate escritura [%]'] = total_write_miss_rate_433AC1

# **435.gromacs-111B**

tabla_AC1.at['435.gromacs-111B', 'Total Misses'] = total_misses_435AC1

tabla_AC1.at['435.gromacs-111B',
             'Miss rate total [%]'] = total_miss_rate_435AC1

tabla_AC1.at['435.gromacs-111B', 'Misses lectura'] = total_read_misses_435AC1

tabla_AC1.at['435.gromacs-111B',
             'Miss rate lectura [%]'] = total_read_miss_rate_435AC1

tabla_AC1.at['435.gromacs-111B',
             'Misses escritura'] = total_write_misses_435AC1

tabla_AC1.at['435.gromacs-111B',
             'Miss rate escritura [%]'] = total_write_miss_rate_435AC1

# **436.cactusADM-1804B**

tabla_AC1.at['436.cactusADM-1804B', 'Total Misses'] = total_misses_436AC1

tabla_AC1.at['436.cactusADM-1804B',
             'Miss rate total [%]'] = total_miss_rate_436AC1

tabla_AC1.at['436.cactusADM-1804B',
             'Misses lectura'] = total_read_misses_436AC1

tabla_AC1.at['436.cactusADM-1804B',
             'Miss rate lectura [%]'] = total_read_miss_rate_436AC1

tabla_AC1.at['436.cactusADM-1804B',
             'Misses escritura'] = total_write_misses_436AC1

tabla_AC1.at['436.cactusADM-1804B',
             'Miss rate escritura [%]'] = total_write_miss_rate_436AC1

# **437.leslie3d-134B**

tabla_AC1.at['437.leslie3d-134B', 'Total Misses'] = total_misses_437AC1

tabla_AC1.at['437.leslie3d-134B',
             'Miss rate total [%]'] = total_miss_rate_437AC1

tabla_AC1.at['437.leslie3d-134B', 'Misses lectura'] = total_read_misses_437AC1

tabla_AC1.at['437.leslie3d-134B',
             'Miss rate lectura [%]'] = total_read_miss_rate_437AC1

tabla_AC1.at['437.leslie3d-134B',
             'Misses escritura'] = total_write_misses_437AC1

tabla_AC1.at['437.leslie3d-134B',
             'Miss rate escritura [%]'] = total_write_miss_rate_437AC1

# **444.namd-120B**

tabla_AC1.at['444.namd-120B', 'Total Misses'] = total_misses_444AC1

tabla_AC1.at['444.namd-120B', 'Miss rate total [%]'] = total_miss_rate_444AC1

tabla_AC1.at['444.namd-120B', 'Misses lectura'] = total_read_misses_444AC1

tabla_AC1.at['444.namd-120B',
             'Miss rate lectura [%]'] = total_read_miss_rate_444AC1

tabla_AC1.at['444.namd-120B',
             'Misses escritura'] = total_write_misses_444AC1

tabla_AC1.at['444.namd-120B',
             'Miss rate escritura [%]'] = total_write_miss_rate_444AC1

# **445.gobmk-17B**

tabla_AC1.at['445.gobmk-17B', 'Total Misses'] = total_misses_445AC1

tabla_AC1.at['445.gobmk-17B', 'Miss rate total [%]'] = total_miss_rate_445AC1

tabla_AC1.at['445.gobmk-17B', 'Misses lectura'] = total_read_misses_445AC1

tabla_AC1.at['445.gobmk-17B',
             'Miss rate lectura [%]'] = total_read_miss_rate_445AC1

tabla_AC1.at['445.gobmk-17B',
             'Misses escritura'] = total_write_misses_445AC1

tabla_AC1.at['445.gobmk-17B',
             'Miss rate escritura [%]'] = total_write_miss_rate_445AC1

# **450.soplex-247B**

tabla_AC1.at['450.soplex-247B', 'Total Misses'] = total_misses_450AC1

tabla_AC1.at['450.soplex-247B', 'Miss rate total [%]'] = total_miss_rate_450AC1

tabla_AC1.at['450.soplex-247B', 'Misses lectura'] = total_read_misses_450AC1

tabla_AC1.at['450.soplex-247B',
             'Miss rate lectura [%]'] = total_read_miss_rate_450AC1

tabla_AC1.at['450.soplex-247B',
             'Misses escritura'] = total_write_misses_450AC1

tabla_AC1.at['450.soplex-247B',
             'Miss rate escritura [%]'] = total_write_miss_rate_450AC1

# **453.povray-887B**

tabla_AC1.at['453.povray-887B', 'Total Misses'] = total_misses_453AC1

tabla_AC1.at['453.povray-887B', 'Miss rate total [%]'] = total_miss_rate_453AC1

tabla_AC1.at['453.povray-887B', 'Misses lectura'] = total_read_misses_453AC1

tabla_AC1.at['453.povray-887B',
             'Miss rate lectura [%]'] = total_read_miss_rate_453AC1

tabla_AC1.at['453.povray-887B',
             'Misses escritura'] = total_write_misses_453AC1

tabla_AC1.at['453.povray-887B',
             'Miss rate escritura [%]'] = total_write_miss_rate_453AC1

# **454.calculix-104B**

tabla_AC1.at['454.calculix-104B', 'Total Misses'] = total_misses_454AC1

tabla_AC1.at['454.calculix-104B',
             'Miss rate total [%]'] = total_miss_rate_454AC1

tabla_AC1.at['454.calculix-104B', 'Misses lectura'] = total_read_misses_454AC1

tabla_AC1.at['454.calculix-104B',
             'Miss rate lectura [%]'] = total_read_miss_rate_454AC1

tabla_AC1.at['454.calculix-104B',
             'Misses escritura'] = total_write_misses_454AC1

tabla_AC1.at['454.calculix-104B',
             'Miss rate escritura [%]'] = total_write_miss_rate_454AC1

# **456.hmmer-191B**

tabla_AC1.at['456.hmmer-191B', 'Total Misses'] = total_misses_456AC1

tabla_AC1.at['456.hmmer-191B', 'Miss rate total [%]'] = total_miss_rate_456AC1

tabla_AC1.at['456.hmmer-191B', 'Misses lectura'] = total_read_misses_456AC1

tabla_AC1.at['456.hmmer-191B',
             'Miss rate lectura [%]'] = total_read_miss_rate_456AC1

tabla_AC1.at['456.hmmer-191B',
             'Misses escritura'] = total_write_misses_456AC1

tabla_AC1.at['456.hmmer-191B',
             'Miss rate escritura [%]'] = total_write_miss_rate_456AC1

# **458.sjeng-1088B**

tabla_AC1.at['458.sjeng-1088B', 'Total Misses'] = total_misses_458AC1

tabla_AC1.at['458.sjeng-1088B', 'Miss rate total [%]'] = total_miss_rate_458AC1

tabla_AC1.at['458.sjeng-1088B', 'Misses lectura'] = total_read_misses_458AC1

tabla_AC1.at['458.sjeng-1088B',
             'Miss rate lectura [%]'] = total_read_miss_rate_458AC1

tabla_AC1.at['458.sjeng-1088B',
             'Misses escritura'] = total_write_misses_458AC1

tabla_AC1.at['458.sjeng-1088B',
             'Miss rate escritura [%]'] = total_write_miss_rate_458AC1

# **459.GemsFDTD-1169B**

tabla_AC1.at['459.GemsFDTD-1169B', 'Total Misses'] = total_misses_459AC1

tabla_AC1.at['459.GemsFDTD-1169B',
             'Miss rate total [%]'] = total_miss_rate_459AC1

tabla_AC1.at['459.GemsFDTD-1169B', 'Misses lectura'] = total_read_misses_459AC1

tabla_AC1.at['459.GemsFDTD-1169B',
             'Miss rate lectura [%]'] = total_read_miss_rate_459AC1

tabla_AC1.at['459.GemsFDTD-1169B',
             'Misses escritura'] = total_write_misses_459AC1

tabla_AC1.at['459.GemsFDTD-1169B',
             'Miss rate escritura [%]'] = total_write_miss_rate_459AC1

# **462.libquantum-1343B**

tabla_AC1.at['462.libquantum-1343B', 'Total Misses'] = total_misses_462AC1

tabla_AC1.at['462.libquantum-1343B',
             'Miss rate total [%]'] = total_miss_rate_462AC1

tabla_AC1.at['462.libquantum-1343B',
             'Misses lectura'] = total_read_misses_462AC1

tabla_AC1.at['462.libquantum-1343B',
             'Miss rate lectura [%]'] = total_read_miss_rate_462AC1

tabla_AC1.at['462.libquantum-1343B',
             'Misses escritura'] = total_write_misses_462AC1

tabla_AC1.at['462.libquantum-1343B',
             'Miss rate escritura [%]'] = total_write_miss_rate_462AC1

# **464.h264ref-30B**

tabla_AC1.at['464.h264ref-30B', 'Total Misses'] = total_misses_464AC1

tabla_AC1.at['464.h264ref-30B', 'Miss rate total [%]'] = total_miss_rate_464AC1

tabla_AC1.at['464.h264ref-30B', 'Misses lectura'] = total_read_misses_464AC1

tabla_AC1.at['464.h264ref-30B',
             'Miss rate lectura [%]'] = total_read_miss_rate_464AC1

tabla_AC1.at['464.h264ref-30B',
             'Misses escritura'] = total_write_misses_464AC1

tabla_AC1.at['464.h264ref-30B',
             'Miss rate escritura [%]'] = total_write_miss_rate_464AC1

# **465.tonto-1769B**

tabla_AC1.at['465.tonto-1769B', 'Total Misses'] = total_misses_465AC1

tabla_AC1.at['465.tonto-1769B', 'Miss rate total [%]'] = total_miss_rate_465AC1

tabla_AC1.at['465.tonto-1769B', 'Misses lectura'] = total_read_misses_465AC1

tabla_AC1.at['465.tonto-1769B',
             'Miss rate lectura [%]'] = total_read_miss_rate_465AC1

tabla_AC1.at['465.tonto-1769B',
             'Misses escritura'] = total_write_misses_465AC1

tabla_AC1.at['465.tonto-1769B',
             'Miss rate escritura [%]'] = total_write_miss_rate_465AC1

# **470.lbm-1274B**

tabla_AC1.at['470.lbm-1274B', 'Total Misses'] = total_misses_470AC1

tabla_AC1.at['470.lbm-1274B', 'Miss rate total [%]'] = total_miss_rate_470AC1

tabla_AC1.at['470.lbm-1274B', 'Misses lectura'] = total_read_misses_470AC1

tabla_AC1.at['470.lbm-1274B',
             'Miss rate lectura [%]'] = total_read_miss_rate_470AC1

tabla_AC1.at['470.lbm-1274B',
             'Misses escritura'] = total_write_misses_470AC1

tabla_AC1.at['470.lbm-1274B',
             'Miss rate escritura [%]'] = total_write_miss_rate_470AC1

# **471.omnetpp-188B**

tabla_AC1.at['471.omnetpp-188B', 'Total Misses'] = total_misses_471AC1

tabla_AC1.at['471.omnetpp-188B',
             'Miss rate total [%]'] = total_miss_rate_471AC1

tabla_AC1.at['471.omnetpp-188B', 'Misses lectura'] = total_read_misses_471AC1

tabla_AC1.at['471.omnetpp-188B',
             'Miss rate lectura [%]'] = total_read_miss_rate_471AC1

tabla_AC1.at['471.omnetpp-188B',
             'Misses escritura'] = total_write_misses_471AC1

tabla_AC1.at['471.omnetpp-188B',
             'Miss rate escritura [%]'] = total_write_miss_rate_471AC1

# **473.astar-153B**

tabla_AC1.at['473.astar-153B', 'Total Misses'] = total_misses_473AC1

tabla_AC1.at['473.astar-153B', 'Miss rate total [%]'] = total_miss_rate_473AC1

tabla_AC1.at['473.astar-153B', 'Misses lectura'] = total_read_misses_473AC1

tabla_AC1.at['473.astar-153B',
             'Miss rate lectura [%]'] = total_read_miss_rate_473AC1

tabla_AC1.at['473.astar-153B',
             'Misses escritura'] = total_write_misses_473AC1

tabla_AC1.at['473.astar-153B',
             'Miss rate escritura [%]'] = total_write_miss_rate_473AC1

# **481.wrf-1170B**

tabla_AC1.at['481.wrf-1170B', 'Total Misses'] = total_misses_481AC1

tabla_AC1.at['481.wrf-1170B', 'Miss rate total [%]'] = total_miss_rate_481AC1

tabla_AC1.at['481.wrf-1170B', 'Misses lectura'] = total_read_misses_481AC1

tabla_AC1.at['481.wrf-1170B',
             'Miss rate lectura [%]'] = total_read_miss_rate_481AC1

tabla_AC1.at['481.wrf-1170B',
             'Misses escritura'] = total_write_misses_481AC1

tabla_AC1.at['481.wrf-1170B',
             'Miss rate escritura [%]'] = total_write_miss_rate_481AC1

# **482.sphinx3-1100B**

tabla_AC1.at['482.sphinx3-1100B', 'Total Misses'] = total_misses_482AC1

tabla_AC1.at['482.sphinx3-1100B',
             'Miss rate total [%]'] = total_miss_rate_482AC1

tabla_AC1.at['482.sphinx3-1100B', 'Misses lectura'] = total_read_misses_482AC1

tabla_AC1.at['482.sphinx3-1100B',
             'Miss rate lectura [%]'] = total_read_miss_rate_482AC1

tabla_AC1.at['482.sphinx3-1100B',
             'Misses escritura'] = total_write_misses_482AC1

tabla_AC1.at['482.sphinx3-1100B',
             'Miss rate escritura [%]'] = total_write_miss_rate_482AC1

# **483.xalancbmk-127B**

tabla_AC1.at['483.xalancbmk-127B', 'Total Misses'] = total_misses_483AC1

tabla_AC1.at['483.xalancbmk-127B',
             'Miss rate total [%]'] = total_miss_rate_483AC1

tabla_AC1.at['483.xalancbmk-127B', 'Misses lectura'] = total_read_misses_483AC1

tabla_AC1.at['483.xalancbmk-127B',
             'Miss rate lectura [%]'] = total_read_miss_rate_483AC1

tabla_AC1.at['483.xalancbmk-127B',
             'Misses escritura'] = total_write_misses_483AC1

tabla_AC1.at['483.xalancbmk-127B',
             'Miss rate escritura [%]'] = total_write_miss_rate_483AC1

print(">>>>>All AC1 data has been uploaded successfully")

##############################################################
# Extractor para experimento con asociatividad de caché 2-way#
##############################################################


# Creación de tablas para adjuntar valores
# Una tabla por tamaño
tabla_AC2 = pd.DataFrame(index=[
    '400.perlbench-41B', '401.bzip2-226B', '403.gcc-16B', '410.bwaves-1963B', '416.gamess-875B', '429.mcf-184B', '433.milc-127B',
    '435.gromacs-111B', '436.cactusADM-1804B', '437.leslie3d-134B', '444.namd-120B', '445.gobmk-17B',
    '450.soplex-247B', '453.povray-887B', '454.calculix-104B', '456.hmmer-191B', '458.sjeng-1088B', '459.GemsFDTD-1169B',
    '462.libquantum-1343B', '464.h264ref-30B', '465.tonto-1769B', '470.lbm-1274B', '471.omnetpp-188B', '473.astar-153B', '481.wrf-1170B',
    '482.sphinx3-1100B', '483.xalancbmk-127B'], columns=[
    'App', 'Total Misses', 'Miss rate total [%]', 'Misses lectura', 'Miss rate lectura [%]', 'Misses escritura', 'Miss rate escritura [%]'])
tabla_AC2['App'] = tabla_AC2.index

# Files paths
filename_28 = "RESULTS_AC/400AC2.txt"
filename_29 = "RESULTS_AC/401AC2.txt"
filename_30 = "RESULTS_AC/403AC2.txt"
filename_31 = "RESULTS_AC/410AC2.txt"
filename_32 = "RESULTS_AC/416AC2.txt"
filename_33 = "RESULTS_AC/429AC2.txt"
filename_34 = "RESULTS_AC/433AC2.txt"
filename_35 = "RESULTS_AC/435AC2.txt"
filename_36 = "RESULTS_AC/436AC2.txt"
filename_37 = "RESULTS_AC/437AC2.txt"
filename_38 = "RESULTS_AC/444AC2.txt"
filename_39 = "RESULTS_AC/445AC2.txt"
filename_40 = "RESULTS_AC/450AC2.txt"
filename_41 = "RESULTS_AC/453AC2.txt"
filename_42 = "RESULTS_AC/454AC2.txt"
filename_43 = "RESULTS_AC/456AC2.txt"
filename_44 = "RESULTS_AC/458AC2.txt"
filename_45 = "RESULTS_AC/459AC2.txt"
filename_46 = "RESULTS_AC/462AC2.txt"
filename_47 = "RESULTS_AC/464AC2.txt"
filename_48 = "RESULTS_AC/465AC2.txt"
filename_49 = "RESULTS_AC/470AC2.txt"
filename_50 = "RESULTS_AC/471AC2.txt"
filename_51 = "RESULTS_AC/473AC2.txt"
filename_52 = "RESULTS_AC/481AC2.txt"
filename_53 = "RESULTS_AC/482AC2.txt"
filename_54 = "RESULTS_AC/483AC2.txt"


# Content file extracter
with open(filename_28, 'r') as file:
    content_400AC2 = file.read()
with open(filename_29, 'r') as file:
    content_401AC2 = file.read()
with open(filename_30, 'r') as file:
    content_403AC2 = file.read()
with open(filename_31, 'r') as file:
    content_410AC2 = file.read()
with open(filename_32, 'r') as file:
    content_416AC2 = file.read()
with open(filename_33, 'r') as file:
    content_429AC2 = file.read()
with open(filename_34, 'r') as file:
    content_433AC2 = file.read()
with open(filename_35, 'r') as file:
    content_435AC2 = file.read()
with open(filename_36, 'r') as file:
    content_436AC2 = file.read()
with open(filename_37, 'r') as file:
    content_437AC2 = file.read()
with open(filename_38, 'r') as file:
    content_444AC2 = file.read()
with open(filename_39, 'r') as file:
    content_445AC2 = file.read()
with open(filename_40, 'r') as file:
    content_450AC2 = file.read()
with open(filename_41, 'r') as file:
    content_453AC2 = file.read()
with open(filename_42, 'r') as file:
    content_454AC2 = file.read()
with open(filename_43, 'r') as file:
    content_456AC2 = file.read()
with open(filename_44, 'r') as file:
    content_458AC2 = file.read()
with open(filename_45, 'r') as file:
    content_459AC2 = file.read()
with open(filename_46, 'r') as file:
    content_462AC2 = file.read()
with open(filename_47, 'r') as file:
    content_464AC2 = file.read()
with open(filename_48, 'r') as file:
    content_465AC2 = file.read()
with open(filename_49, 'r') as file:
    content_470AC2 = file.read()
with open(filename_50, 'r') as file:
    content_471AC2 = file.read()
with open(filename_51, 'r') as file:
    content_473AC2 = file.read()
with open(filename_52, 'r') as file:
    content_481AC2 = file.read()
with open(filename_53, 'r') as file:
    content_482AC2 = file.read()
with open(filename_54, 'r') as file:
    content_483AC2 = file.read()


# Variables según aplicación

# 400.pearlbench-41B
total_misses_400AC2 = re.search(
    r"Total_misses (\d+)", content_400AC2).group(1)
total_miss_rate_400AC2 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_400AC2).group(1)
total_read_misses_400AC2 = re.search(
    r"Total_read_misses (\d+)", content_400AC2).group(1)
total_read_miss_rate_400AC2 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_400AC2).group(1)
total_write_misses_400AC2 = re.search(
    r"Total_write_misses (\d+)", content_400AC2).group(1)
total_write_miss_rate_400AC2 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_400AC2).group(1)
print(">>>>>All AC2 400.pearlbench-41B variables where obtained successfully")

# 401.bzip2-226B
total_misses_401AC2 = re.search(
    r"Total_misses (\d+)", content_401AC2).group(1)
total_miss_rate_401AC2 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_401AC2).group(1)
total_read_misses_401AC2 = re.search(
    r"Total_read_misses (\d+)", content_401AC2).group(1)
total_read_miss_rate_401AC2 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_401AC2).group(1)
total_write_misses_401AC2 = re.search(
    r"Total_write_misses (\d+)", content_401AC2).group(1)
total_write_miss_rate_401AC2 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_401AC2).group(1)
print(">>>>>All AC2 401.bzip2-226B variables where obtained successfully")

# 403.gcc-16B
total_misses_403AC2 = re.search(
    r"Total_misses (\d+)", content_403AC2).group(1)
total_miss_rate_403AC2 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_403AC2).group(1)
total_read_misses_403AC2 = re.search(
    r"Total_read_misses (\d+)", content_403AC2).group(1)
total_read_miss_rate_403AC2 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_403AC2).group(1)
total_write_misses_403AC2 = re.search(
    r"Total_write_misses (\d+)", content_403AC2).group(1)
total_write_miss_rate_403AC2 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_403AC2).group(1)
print(">>>>>All AC2 403.gcc-16B variables where obtained successfully")

# 410.bwaves-1963B
total_misses_410AC2 = re.search(
    r"Total_misses (\d+)", content_410AC2).group(1)
total_miss_rate_410AC2 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_410AC2).group(1)
total_read_misses_410AC2 = re.search(
    r"Total_read_misses (\d+)", content_410AC2).group(1)
total_read_miss_rate_410AC2 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_410AC2).group(1)
total_write_misses_410AC2 = re.search(
    r"Total_write_misses (\d+)", content_410AC2).group(1)
total_write_miss_rate_410AC2 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_410AC2).group(1)
print(">>>>>All AC2 410.bwaves-1963B variables where obtained successfully")

# 416.gamess-875B
total_misses_416AC2 = re.search(
    r"Total_misses (\d+)", content_416AC2).group(1)
total_miss_rate_416AC2 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_416AC2).group(1)
total_read_misses_416AC2 = re.search(
    r"Total_read_misses (\d+)", content_416AC2).group(1)
total_read_miss_rate_416AC2 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_416AC2).group(1)
total_write_misses_416AC2 = re.search(
    r"Total_write_misses (\d+)", content_416AC2).group(1)
total_write_miss_rate_416AC2 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_416AC2).group(1)
print(">>>>>All AC2 416.gamess-875B variables where obtained successfully")

# 429.mcf-184B
total_misses_429AC2 = re.search(
    r"Total_misses (\d+)", content_429AC2).group(1)
total_miss_rate_429AC2 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_429AC2).group(1)
total_read_misses_429AC2 = re.search(
    r"Total_read_misses (\d+)", content_429AC2).group(1)
total_read_miss_rate_429AC2 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_429AC2).group(1)
total_write_misses_429AC2 = re.search(
    r"Total_write_misses (\d+)", content_429AC2).group(1)
total_write_miss_rate_429AC2 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_429AC2).group(1)
print(">>>>>All AC2 429.mcf-184B variables where obtained successfully")

# 433.milc-127B
total_misses_433AC2 = re.search(
    r"Total_misses (\d+)", content_433AC2).group(1)
total_miss_rate_433AC2 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_433AC2).group(1)
total_read_misses_433AC2 = re.search(
    r"Total_read_misses (\d+)", content_433AC2).group(1)
total_read_miss_rate_433AC2 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_433AC2).group(1)
total_write_misses_433AC2 = re.search(
    r"Total_write_misses (\d+)", content_433AC2).group(1)
total_write_miss_rate_433AC2 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_433AC2).group(1)
print(">>>>>All AC2 433.milc-127B variables where obtained successfully")

# 435.gromacs-111B
total_misses_435AC2 = re.search(
    r"Total_misses (\d+)", content_435AC2).group(1)
total_miss_rate_435AC2 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_435AC2).group(1)
total_read_misses_435AC2 = re.search(
    r"Total_read_misses (\d+)", content_435AC2).group(1)
total_read_miss_rate_435AC2 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_435AC2).group(1)
total_write_misses_435AC2 = re.search(
    r"Total_write_misses (\d+)", content_435AC2).group(1)
total_write_miss_rate_435AC2 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_435AC2).group(1)
print(">>>>>All AC2 435.gromacs-111B variables where obtained successfully")

# 436.cactusADM-1804B
total_misses_436AC2 = re.search(
    r"Total_misses (\d+)", content_436AC2).group(1)
total_miss_rate_436AC2 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_436AC2).group(1)
total_read_misses_436AC2 = re.search(
    r"Total_read_misses (\d+)", content_436AC2).group(1)
total_read_miss_rate_436AC2 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_436AC2).group(1)
total_write_misses_436AC2 = re.search(
    r"Total_write_misses (\d+)", content_436AC2).group(1)
total_write_miss_rate_436AC2 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_436AC2).group(1)
print(">>>>>All AC2 436.cactusADM-1804B variables where obtained successfully")

# 437.leslie3d-134B
total_misses_437AC2 = re.search(
    r"Total_misses (\d+)", content_437AC2).group(1)
total_miss_rate_437AC2 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_437AC2).group(1)
total_read_misses_437AC2 = re.search(
    r"Total_read_misses (\d+)", content_437AC2).group(1)
total_read_miss_rate_437AC2 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_437AC2).group(1)
total_write_misses_437AC2 = re.search(
    r"Total_write_misses (\d+)", content_437AC2).group(1)
total_write_miss_rate_437AC2 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_437AC2).group(1)
print(">>>>>All AC2 437.leslie3d-134B variables where obtained successfully")

# 444.namd-120B
total_misses_444AC2 = re.search(
    r"Total_misses (\d+)", content_444AC2).group(1)
total_miss_rate_444AC2 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_444AC2).group(1)
total_read_misses_444AC2 = re.search(
    r"Total_read_misses (\d+)", content_444AC2).group(1)
total_read_miss_rate_444AC2 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_444AC2).group(1)
total_write_misses_444AC2 = re.search(
    r"Total_write_misses (\d+)", content_444AC2).group(1)
total_write_miss_rate_444AC2 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_444AC2).group(1)
print(">>>>>All AC2 444.namd-120B variables where obtained successfully")

# 445.gobmk-17B
total_misses_445AC2 = re.search(
    r"Total_misses (\d+)", content_445AC2).group(1)
total_miss_rate_445AC2 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_445AC2).group(1)
total_read_misses_445AC2 = re.search(
    r"Total_read_misses (\d+)", content_445AC2).group(1)
total_read_miss_rate_445AC2 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_445AC2).group(1)
total_write_misses_445AC2 = re.search(
    r"Total_write_misses (\d+)", content_445AC2).group(1)
total_write_miss_rate_445AC2 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_445AC2).group(1)
print(">>>>>All AC2 445.gobmk-17B variables where obtained successfully")

# 450.soplex-247B
total_misses_450AC2 = re.search(
    r"Total_misses (\d+)", content_450AC2).group(1)
total_miss_rate_450AC2 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_450AC2).group(1)
total_read_misses_450AC2 = re.search(
    r"Total_read_misses (\d+)", content_450AC2).group(1)
total_read_miss_rate_450AC2 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_450AC2).group(1)
total_write_misses_450AC2 = re.search(
    r"Total_write_misses (\d+)", content_450AC2).group(1)
total_write_miss_rate_450AC2 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_450AC2).group(1)
print(">>>>>All AC2 450.soplex-247B variables where obtained successfully")

# 453.povray-887B
total_misses_453AC2 = re.search(
    r"Total_misses (\d+)", content_453AC2).group(1)
total_miss_rate_453AC2 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_453AC2).group(1)
total_read_misses_453AC2 = re.search(
    r"Total_read_misses (\d+)", content_453AC2).group(1)
total_read_miss_rate_453AC2 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_453AC2).group(1)
total_write_misses_453AC2 = re.search(
    r"Total_write_misses (\d+)", content_453AC2).group(1)
total_write_miss_rate_453AC2 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_453AC2).group(1)
print(">>>>>All AC2 453.povray-887B variables where obtained successfully")

# 454.calculix-104B
total_misses_454AC2 = re.search(
    r"Total_misses (\d+)", content_454AC2).group(1)
total_miss_rate_454AC2 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_454AC2).group(1)
total_read_misses_454AC2 = re.search(
    r"Total_read_misses (\d+)", content_454AC2).group(1)
total_read_miss_rate_454AC2 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_454AC2).group(1)
total_write_misses_454AC2 = re.search(
    r"Total_write_misses (\d+)", content_454AC2).group(1)
total_write_miss_rate_454AC2 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_454AC2).group(1)
print(">>>>>All AC2 454.calculix-104B variables where obtained successfully")

# 456.hmmer-191B
total_misses_456AC2 = re.search(
    r"Total_misses (\d+)", content_456AC2).group(1)
total_miss_rate_456AC2 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_456AC2).group(1)
total_read_misses_456AC2 = re.search(
    r"Total_read_misses (\d+)", content_456AC2).group(1)
total_read_miss_rate_456AC2 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_456AC2).group(1)
total_write_misses_456AC2 = re.search(
    r"Total_write_misses (\d+)", content_456AC2).group(1)
total_write_miss_rate_456AC2 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_456AC2).group(1)
print(">>>>>All AC2 456.hmmer-191B variables where obtained successfully")

# 458.sjeng-1088B
total_misses_458AC2 = re.search(
    r"Total_misses (\d+)", content_458AC2).group(1)
total_miss_rate_458AC2 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_458AC2).group(1)
total_read_misses_458AC2 = re.search(
    r"Total_read_misses (\d+)", content_458AC2).group(1)
total_read_miss_rate_458AC2 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_458AC2).group(1)
total_write_misses_458AC2 = re.search(
    r"Total_write_misses (\d+)", content_458AC2).group(1)
total_write_miss_rate_458AC2 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_458AC2).group(1)
print(">>>>>All AC2 458.sjeng-1088B variables where obtained successfully")

# 459.GemsFDTD-1169B
total_misses_459AC2 = re.search(
    r"Total_misses (\d+)", content_459AC2).group(1)
total_miss_rate_459AC2 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_459AC2).group(1)
total_read_misses_459AC2 = re.search(
    r"Total_read_misses (\d+)", content_459AC2).group(1)
total_read_miss_rate_459AC2 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_459AC2).group(1)
total_write_misses_459AC2 = re.search(
    r"Total_write_misses (\d+)", content_459AC2).group(1)
total_write_miss_rate_459AC2 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_459AC2).group(1)
print(">>>>>All AC2 459.GemsFDTD-1169B variables where obtained successfully")

# 462.libquantum-1343B
total_misses_462AC2 = re.search(
    r"Total_misses (\d+)", content_462AC2).group(1)
total_miss_rate_462AC2 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_462AC2).group(1)
total_read_misses_462AC2 = re.search(
    r"Total_read_misses (\d+)", content_462AC2).group(1)
total_read_miss_rate_462AC2 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_462AC2).group(1)
total_write_misses_462AC2 = re.search(
    r"Total_write_misses (\d+)", content_462AC2).group(1)
total_write_miss_rate_462AC2 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_462AC2).group(1)
print(">>>>>All AC2 462.libquantum-1343B variables where obtained successfully")

# 464.h264ref-30B
total_misses_464AC2 = re.search(
    r"Total_misses (\d+)", content_464AC2).group(1)
total_miss_rate_464AC2 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_464AC2).group(1)
total_read_misses_464AC2 = re.search(
    r"Total_read_misses (\d+)", content_464AC2).group(1)
total_read_miss_rate_464AC2 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_464AC2).group(1)
total_write_misses_464AC2 = re.search(
    r"Total_write_misses (\d+)", content_464AC2).group(1)
total_write_miss_rate_464AC2 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_464AC2).group(1)
print(">>>>>All AC2 464.h264ref-30B variables where obtained successfully")

# 465.tonto-1769B
total_misses_465AC2 = re.search(
    r"Total_misses (\d+)", content_465AC2).group(1)
total_miss_rate_465AC2 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_465AC2).group(1)
total_read_misses_465AC2 = re.search(
    r"Total_read_misses (\d+)", content_465AC2).group(1)
total_read_miss_rate_465AC2 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_465AC2).group(1)
total_write_misses_465AC2 = re.search(
    r"Total_write_misses (\d+)", content_465AC2).group(1)
total_write_miss_rate_465AC2 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_465AC2).group(1)
print(">>>>>All AC2 465.tonto-1769B variables where obtained successfully")

# 470.lbm-1274B
total_misses_470AC2 = re.search(
    r"Total_misses (\d+)", content_470AC2).group(1)
total_miss_rate_470AC2 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_470AC2).group(1)
total_read_misses_470AC2 = re.search(
    r"Total_read_misses (\d+)", content_470AC2).group(1)
total_read_miss_rate_470AC2 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_470AC2).group(1)
total_write_misses_470AC2 = re.search(
    r"Total_write_misses (\d+)", content_470AC2).group(1)
total_write_miss_rate_470AC2 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_470AC2).group(1)
print(">>>>>All AC2 470.lbm-1274B variables where obtained successfully")

# 471.omnetpp-188B
total_misses_471AC2 = re.search(
    r"Total_misses (\d+)", content_471AC2).group(1)
total_miss_rate_471AC2 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_471AC2).group(1)
total_read_misses_471AC2 = re.search(
    r"Total_read_misses (\d+)", content_471AC2).group(1)
total_read_miss_rate_471AC2 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_471AC2).group(1)
total_write_misses_471AC2 = re.search(
    r"Total_write_misses (\d+)", content_471AC2).group(1)
total_write_miss_rate_471AC2 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_471AC2).group(1)
print(">>>>>All AC2 471.omnetpp-188B variables where obtained successfully")

# 473.astar-153B
total_misses_473AC2 = re.search(
    r"Total_misses (\d+)", content_473AC2).group(1)
total_miss_rate_473AC2 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_473AC2).group(1)
total_read_misses_473AC2 = re.search(
    r"Total_read_misses (\d+)", content_473AC2).group(1)
total_read_miss_rate_473AC2 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_473AC2).group(1)
total_write_misses_473AC2 = re.search(
    r"Total_write_misses (\d+)", content_473AC2).group(1)
total_write_miss_rate_473AC2 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_473AC2).group(1)
print(">>>>>All AC2 473.astar-153B variables where obtained successfully")

# 481.wrf-1170B
total_misses_481AC2 = re.search(
    r"Total_misses (\d+)", content_481AC2).group(1)
total_miss_rate_481AC2 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_481AC2).group(1)
total_read_misses_481AC2 = re.search(
    r"Total_read_misses (\d+)", content_481AC2).group(1)
total_read_miss_rate_481AC2 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_481AC2).group(1)
total_write_misses_481AC2 = re.search(
    r"Total_write_misses (\d+)", content_481AC2).group(1)
total_write_miss_rate_481AC2 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_481AC2).group(1)
print(">>>>>All AC2 481.wrf-1170B variables where obtained successfully")

# 482.sphinx3-1100B
total_misses_482AC2 = re.search(
    r"Total_misses (\d+)", content_482AC2).group(1)
total_miss_rate_482AC2 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_482AC2).group(1)
total_read_misses_482AC2 = re.search(
    r"Total_read_misses (\d+)", content_482AC2).group(1)
total_read_miss_rate_482AC2 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_482AC2).group(1)
total_write_misses_482AC2 = re.search(
    r"Total_write_misses (\d+)", content_482AC2).group(1)
total_write_miss_rate_482AC2 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_482AC2).group(1)
print(">>>>>All AC2 482.sphinx3-1100B variables where obtained successfully")

# 483.xalancbmk-127B
total_misses_483AC2 = re.search(
    r"Total_misses (\d+)", content_483AC2).group(1)
total_miss_rate_483AC2 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_483AC2).group(1)
total_read_misses_483AC2 = re.search(
    r"Total_read_misses (\d+)", content_483AC2).group(1)
total_read_miss_rate_483AC2 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_483AC2).group(1)
total_write_misses_483AC2 = re.search(
    r"Total_write_misses (\d+)", content_483AC2).group(1)
total_write_miss_rate_483AC2 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_483AC2).group(1)
print(">>>>>All AC2 483.xalancbmk-127B variables where obtained successfully")

#############################
# Adjunta datos a dataframe #
#############################

# **400.perlbench-41B**

tabla_AC2.at['400.perlbench-41B', 'Total Misses'] = total_misses_400AC2

tabla_AC2.at['400.perlbench-41B',
             'Miss rate total [%]'] = total_miss_rate_400AC2

tabla_AC2.at['400.perlbench-41B',
             'Misses lectura'] = total_read_misses_400AC2

tabla_AC2.at['400.perlbench-41B',
             'Miss rate lectura [%]'] = total_read_miss_rate_400AC2

tabla_AC2.at['400.perlbench-41B',
             'Misses escritura'] = total_write_misses_400AC2

tabla_AC2.at['400.perlbench-41B',
             'Miss rate escritura [%]'] = total_write_miss_rate_400AC2

# **401.bzip2-226B**

tabla_AC2.at['401.bzip2-226B', 'Total Misses'] = total_misses_401AC2

tabla_AC2.at['401.bzip2-226B',
             'Miss rate total [%]'] = total_miss_rate_401AC2

tabla_AC2.at['401.bzip2-226B', 'Misses lectura'] = total_read_misses_401AC2

tabla_AC2.at['401.bzip2-226B',
             'Miss rate lectura [%]'] = total_read_miss_rate_401AC2

tabla_AC2.at['401.bzip2-226B',
             'Misses escritura'] = total_write_misses_401AC2

tabla_AC2.at['401.bzip2-226B',
             'Miss rate escritura [%]'] = total_write_miss_rate_401AC2

# **403.gcc-16B**

tabla_AC2.at['403.gcc-16B', 'Total Misses'] = total_misses_403AC2

tabla_AC2.at['403.gcc-16B', 'Miss rate total [%]'] = total_miss_rate_403AC2

tabla_AC2.at['403.gcc-16B', 'Misses lectura'] = total_read_misses_403AC2

tabla_AC2.at['403.gcc-16B',
             'Miss rate lectura [%]'] = total_read_miss_rate_403AC2

tabla_AC2.at['403.gcc-16B',
             'Misses escritura'] = total_write_misses_403AC2

tabla_AC2.at['403.gcc-16B',
             'Miss rate escritura [%]'] = total_write_miss_rate_403AC2

# **410.bwaves-1963B**

tabla_AC2.at['410.bwaves-1963B', 'Total Misses'] = total_misses_410AC2

tabla_AC2.at['410.bwaves-1963B',
             'Miss rate total [%]'] = total_miss_rate_410AC2

tabla_AC2.at['410.bwaves-1963B', 'Misses lectura'] = total_read_misses_410AC2

tabla_AC2.at['410.bwaves-1963B',
             'Miss rate lectura [%]'] = total_read_miss_rate_410AC2

tabla_AC2.at['410.bwaves-1963B',
             'Misses escritura'] = total_write_misses_410AC2

tabla_AC2.at['410.bwaves-1963B',
             'Miss rate escritura [%]'] = total_write_miss_rate_410AC2

# **416.gamess-875B**

tabla_AC2.at['416.gamess-875B', 'Total Misses'] = total_misses_416AC2

tabla_AC2.at['416.gamess-875B',
             'Miss rate total [%]'] = total_miss_rate_416AC2

tabla_AC2.at['416.gamess-875B', 'Misses lectura'] = total_read_misses_416AC2

tabla_AC2.at['416.gamess-875B',
             'Miss rate lectura [%]'] = total_read_miss_rate_416AC2

tabla_AC2.at['416.gamess-875B',
             'Misses escritura'] = total_write_misses_416AC2

tabla_AC2.at['416.gamess-875B',
             'Miss rate escritura [%]'] = total_write_miss_rate_416AC2

# **429.mcf-184B**

tabla_AC2.at['429.mcf-184B', 'Total Misses'] = total_misses_429AC2

tabla_AC2.at['429.mcf-184B', 'Miss rate total [%]'] = total_miss_rate_429AC2

tabla_AC2.at['429.mcf-184B', 'Misses lectura'] = total_read_misses_429AC2

tabla_AC2.at['429.mcf-184B',
             'Miss rate lectura [%]'] = total_read_miss_rate_429AC2

tabla_AC2.at['429.mcf-184B',
             'Misses escritura'] = total_write_misses_429AC2

tabla_AC2.at['429.mcf-184B',
             'Miss rate escritura [%]'] = total_write_miss_rate_429AC2

# **433.milc-127B**

tabla_AC2.at['433.milc-127B', 'Total Misses'] = total_misses_433AC2

tabla_AC2.at['433.milc-127B', 'Miss rate total [%]'] = total_miss_rate_433AC2

tabla_AC2.at['433.milc-127B', 'Misses lectura'] = total_read_misses_433AC2

tabla_AC2.at['433.milc-127B',
             'Miss rate lectura [%]'] = total_read_miss_rate_433AC2

tabla_AC2.at['433.milc-127B',
             'Misses escritura'] = total_write_misses_433AC2

tabla_AC2.at['433.milc-127B',
             'Miss rate escritura [%]'] = total_write_miss_rate_433AC2

# **435.gromacs-111B**

tabla_AC2.at['435.gromacs-111B', 'Total Misses'] = total_misses_435AC2

tabla_AC2.at['435.gromacs-111B',
             'Miss rate total [%]'] = total_miss_rate_435AC2

tabla_AC2.at['435.gromacs-111B', 'Misses lectura'] = total_read_misses_435AC2

tabla_AC2.at['435.gromacs-111B',
             'Miss rate lectura [%]'] = total_read_miss_rate_435AC2

tabla_AC2.at['435.gromacs-111B',
             'Misses escritura'] = total_write_misses_435AC2

tabla_AC2.at['435.gromacs-111B',
             'Miss rate escritura [%]'] = total_write_miss_rate_435AC2
# **436.cactusADM-1804B**

tabla_AC2.at['436.cactusADM-1804B', 'Total Misses'] = total_misses_436AC2

tabla_AC2.at['436.cactusADM-1804B',
             'Miss rate total [%]'] = total_miss_rate_436AC2

tabla_AC2.at['436.cactusADM-1804B',
             'Misses lectura'] = total_read_misses_436AC2

tabla_AC2.at['436.cactusADM-1804B',
             'Miss rate lectura [%]'] = total_read_miss_rate_436AC2

tabla_AC2.at['436.cactusADM-1804B',
             'Misses escritura'] = total_write_misses_436AC2

tabla_AC2.at['436.cactusADM-1804B',
             'Miss rate escritura [%]'] = total_write_miss_rate_436AC2

# **437.leslie3d-134B**

tabla_AC2.at['437.leslie3d-134B', 'Total Misses'] = total_misses_437AC2

tabla_AC2.at['437.leslie3d-134B',
             'Miss rate total [%]'] = total_miss_rate_437AC2

tabla_AC2.at['437.leslie3d-134B',
             'Misses lectura'] = total_read_misses_437AC2

tabla_AC2.at['437.leslie3d-134B',
             'Miss rate lectura [%]'] = total_read_miss_rate_437AC2

tabla_AC2.at['437.leslie3d-134B',
             'Misses escritura'] = total_write_misses_437AC2

tabla_AC2.at['437.leslie3d-134B',
             'Miss rate escritura [%]'] = total_write_miss_rate_437AC2

# **444.namd-120B**

tabla_AC2.at['444.namd-120B', 'Total Misses'] = total_misses_444AC2

tabla_AC2.at['444.namd-120B', 'Miss rate total [%]'] = total_miss_rate_444AC2

tabla_AC2.at['444.namd-120B', 'Misses lectura'] = total_read_misses_444AC2

tabla_AC2.at['444.namd-120B',
             'Miss rate lectura [%]'] = total_read_miss_rate_444AC2

tabla_AC2.at['444.namd-120B',
             'Misses escritura'] = total_write_misses_444AC2

tabla_AC2.at['444.namd-120B',
             'Miss rate escritura [%]'] = total_write_miss_rate_444AC2

# **445.gobmk-17B**

tabla_AC2.at['445.gobmk-17B', 'Total Misses'] = total_misses_445AC2

tabla_AC2.at['445.gobmk-17B', 'Miss rate total [%]'] = total_miss_rate_445AC2

tabla_AC2.at['445.gobmk-17B', 'Misses lectura'] = total_read_misses_445AC2

tabla_AC2.at['445.gobmk-17B',
             'Miss rate lectura [%]'] = total_read_miss_rate_445AC2

tabla_AC2.at['445.gobmk-17B',
             'Misses escritura'] = total_write_misses_445AC2

tabla_AC2.at['445.gobmk-17B',
             'Miss rate escritura [%]'] = total_write_miss_rate_445AC2

# **450.soplex-247B**

tabla_AC2.at['450.soplex-247B', 'Total Misses'] = total_misses_450AC2

tabla_AC2.at['450.soplex-247B',
             'Miss rate total [%]'] = total_miss_rate_450AC2

tabla_AC2.at['450.soplex-247B', 'Misses lectura'] = total_read_misses_450AC2

tabla_AC2.at['450.soplex-247B',
             'Miss rate lectura [%]'] = total_read_miss_rate_450AC2

tabla_AC2.at['450.soplex-247B',
             'Misses escritura'] = total_write_misses_450AC2

tabla_AC2.at['450.soplex-247B',
             'Miss rate escritura [%]'] = total_write_miss_rate_450AC2

# **453.povray-887B**

tabla_AC2.at['453.povray-887B', 'Total Misses'] = total_misses_453AC2

tabla_AC2.at['453.povray-887B',
             'Miss rate total [%]'] = total_miss_rate_453AC2

tabla_AC2.at['453.povray-887B', 'Misses lectura'] = total_read_misses_453AC2

tabla_AC2.at['453.povray-887B',
             'Miss rate lectura [%]'] = total_read_miss_rate_453AC2

tabla_AC2.at['453.povray-887B',
             'Misses escritura'] = total_write_misses_453AC2

tabla_AC2.at['453.povray-887B',
             'Miss rate escritura [%]'] = total_write_miss_rate_453AC2

# **454.calculix-104B**

tabla_AC2.at['454.calculix-104B', 'Total Misses'] = total_misses_454AC2

tabla_AC2.at['454.calculix-104B',
             'Miss rate total [%]'] = total_miss_rate_454AC2

tabla_AC2.at['454.calculix-104B',
             'Misses lectura'] = total_read_misses_454AC2

tabla_AC2.at['454.calculix-104B',
             'Miss rate lectura [%]'] = total_read_miss_rate_454AC2

tabla_AC2.at['454.calculix-104B',
             'Misses escritura'] = total_write_misses_454AC2

tabla_AC2.at['454.calculix-104B',
             'Miss rate escritura [%]'] = total_write_miss_rate_454AC2

# **456.hmmer-191B**

tabla_AC2.at['456.hmmer-191B', 'Total Misses'] = total_misses_456AC2

tabla_AC2.at['456.hmmer-191B',
             'Miss rate total [%]'] = total_miss_rate_456AC2

tabla_AC2.at['456.hmmer-191B', 'Misses lectura'] = total_read_misses_456AC2

tabla_AC2.at['456.hmmer-191B',
             'Miss rate lectura [%]'] = total_read_miss_rate_456AC2

tabla_AC2.at['456.hmmer-191B',
             'Misses escritura'] = total_write_misses_456AC2

tabla_AC2.at['456.hmmer-191B',
             'Miss rate escritura [%]'] = total_write_miss_rate_456AC2

# **458.sjeng-1088B**

tabla_AC2.at['458.sjeng-1088B', 'Total Misses'] = total_misses_458AC2

tabla_AC2.at['458.sjeng-1088B',
             'Miss rate total [%]'] = total_miss_rate_458AC2

tabla_AC2.at['458.sjeng-1088B', 'Misses lectura'] = total_read_misses_458AC2

tabla_AC2.at['458.sjeng-1088B',
             'Miss rate lectura [%]'] = total_read_miss_rate_458AC2

tabla_AC2.at['458.sjeng-1088B',
             'Misses escritura'] = total_write_misses_458AC2

tabla_AC2.at['458.sjeng-1088B',
             'Miss rate escritura [%]'] = total_write_miss_rate_458AC2

# **459.GemsFDTD-1169B**

tabla_AC2.at['459.GemsFDTD-1169B', 'Total Misses'] = total_misses_459AC2

tabla_AC2.at['459.GemsFDTD-1169B',
             'Miss rate total [%]'] = total_miss_rate_459AC2

tabla_AC2.at['459.GemsFDTD-1169B',
             'Misses lectura'] = total_read_misses_459AC2

tabla_AC2.at['459.GemsFDTD-1169B',
             'Miss rate lectura [%]'] = total_read_miss_rate_459AC2

tabla_AC2.at['459.GemsFDTD-1169B',
             'Misses escritura'] = total_write_misses_459AC2

tabla_AC2.at['459.GemsFDTD-1169B',
             'Miss rate escritura [%]'] = total_write_miss_rate_459AC2

# **462.libquantum-1343B**

tabla_AC2.at['462.libquantum-1343B', 'Total Misses'] = total_misses_462AC2

tabla_AC2.at['462.libquantum-1343B',
             'Miss rate total [%]'] = total_miss_rate_462AC2

tabla_AC2.at['462.libquantum-1343B',
             'Misses lectura'] = total_read_misses_462AC2

tabla_AC2.at['462.libquantum-1343B',
             'Miss rate lectura [%]'] = total_read_miss_rate_462AC2

tabla_AC2.at['462.libquantum-1343B',
             'Misses escritura'] = total_write_misses_462AC2

tabla_AC2.at['462.libquantum-1343B',
             'Miss rate escritura [%]'] = total_write_miss_rate_462AC2

# **464.h264ref-30B**

tabla_AC2.at['464.h264ref-30B', 'Total Misses'] = total_misses_464AC2

tabla_AC2.at['464.h264ref-30B',
             'Miss rate total [%]'] = total_miss_rate_464AC2

tabla_AC2.at['464.h264ref-30B', 'Misses lectura'] = total_read_misses_464AC2

tabla_AC2.at['464.h264ref-30B',
             'Miss rate lectura [%]'] = total_read_miss_rate_464AC2

tabla_AC2.at['464.h264ref-30B',
             'Misses escritura'] = total_write_misses_464AC2

tabla_AC2.at['464.h264ref-30B',
             'Miss rate escritura [%]'] = total_write_miss_rate_464AC2

# **465.tonto-1769B**

tabla_AC2.at['465.tonto-1769B', 'Total Misses'] = total_misses_465AC2

tabla_AC2.at['465.tonto-1769B',
             'Miss rate total [%]'] = total_miss_rate_465AC2

tabla_AC2.at['465.tonto-1769B', 'Misses lectura'] = total_read_misses_465AC2

tabla_AC2.at['465.tonto-1769B',
             'Miss rate lectura [%]'] = total_read_miss_rate_465AC2

tabla_AC2.at['465.tonto-1769B',
             'Misses escritura'] = total_write_misses_465AC2
tabla_AC2.at['465.tonto-1769B',
             'Miss rate escritura [%]'] = total_write_miss_rate_465AC2

# **470.lbm-1274B**

tabla_AC2.at['470.lbm-1274B', 'Total Misses'] = total_misses_470AC2

tabla_AC2.at['470.lbm-1274B', 'Miss rate total [%]'] = total_miss_rate_470AC2

tabla_AC2.at['470.lbm-1274B', 'Misses lectura'] = total_read_misses_470AC2

tabla_AC2.at['470.lbm-1274B',
             'Miss rate lectura [%]'] = total_read_miss_rate_470AC2

tabla_AC2.at['470.lbm-1274B',
             'Misses escritura'] = total_write_misses_470AC2

tabla_AC2.at['470.lbm-1274B',
             'Miss rate escritura [%]'] = total_write_miss_rate_470AC2

# **471.omnetpp-188B**

tabla_AC2.at['471.omnetpp-188B', 'Total Misses'] = total_misses_471AC2

tabla_AC2.at['471.omnetpp-188B',
             'Miss rate total [%]'] = total_miss_rate_471AC2

tabla_AC2.at['471.omnetpp-188B', 'Misses lectura'] = total_read_misses_471AC2

tabla_AC2.at['471.omnetpp-188B',
             'Miss rate lectura [%]'] = total_read_miss_rate_471AC2

tabla_AC2.at['471.omnetpp-188B',
             'Misses escritura'] = total_write_misses_471AC2

tabla_AC2.at['471.omnetpp-188B',
             'Miss rate escritura [%]'] = total_write_miss_rate_471AC2

# **473.astar-153B**

tabla_AC2.at['473.astar-153B', 'Total Misses'] = total_misses_473AC2

tabla_AC2.at['473.astar-153B',
             'Miss rate total [%]'] = total_miss_rate_473AC2

tabla_AC2.at['473.astar-153B', 'Misses lectura'] = total_read_misses_473AC2

tabla_AC2.at['473.astar-153B',
             'Miss rate lectura [%]'] = total_read_miss_rate_473AC2

tabla_AC2.at['473.astar-153B',
             'Misses escritura'] = total_write_misses_473AC2

tabla_AC2.at['473.astar-153B',
             'Miss rate escritura [%]'] = total_write_miss_rate_473AC2

# **481.wrf-1170B**

tabla_AC2.at['481.wrf-1170B', 'Total Misses'] = total_misses_481AC2

tabla_AC2.at['481.wrf-1170B', 'Miss rate total [%]'] = total_miss_rate_481AC2

tabla_AC2.at['481.wrf-1170B', 'Misses lectura'] = total_read_misses_481AC2

tabla_AC2.at['481.wrf-1170B',
             'Miss rate lectura [%]'] = total_read_miss_rate_481AC2

tabla_AC2.at['481.wrf-1170B',
             'Misses escritura'] = total_write_misses_481AC2

tabla_AC2.at['481.wrf-1170B',
             'Miss rate escritura [%]'] = total_write_miss_rate_481AC2

# **482.sphinx3-1100B**

tabla_AC2.at['482.sphinx3-1100B', 'Total Misses'] = total_misses_482AC2

tabla_AC2.at['482.sphinx3-1100B',
             'Miss rate total [%]'] = total_miss_rate_482AC2

tabla_AC2.at['482.sphinx3-1100B',
             'Misses lectura'] = total_read_misses_482AC2

tabla_AC2.at['482.sphinx3-1100B',
             'Miss rate lectura [%]'] = total_read_miss_rate_482AC2

tabla_AC2.at['482.sphinx3-1100B',
             'Misses escritura'] = total_write_misses_482AC2

tabla_AC2.at['482.sphinx3-1100B',
             'Miss rate escritura [%]'] = total_write_miss_rate_482AC2

# **483.xalancbmk-127B**

tabla_AC2.at['483.xalancbmk-127B', 'Total Misses'] = total_misses_483AC2

tabla_AC2.at['483.xalancbmk-127B',
             'Miss rate total [%]'] = total_miss_rate_483AC2

tabla_AC2.at['483.xalancbmk-127B',
             'Misses lectura'] = total_read_misses_483AC2

tabla_AC2.at['483.xalancbmk-127B',
             'Miss rate lectura [%]'] = total_read_miss_rate_483AC2

tabla_AC2.at['483.xalancbmk-127B',
             'Misses escritura'] = total_write_misses_483AC2

tabla_AC2.at['483.xalancbmk-127B',
             'Miss rate escritura [%]'] = total_write_miss_rate_483AC2

print(">>>>>All AC2 data has been uploaded successfully")

###########################################
# Extractor para experimento con asociatividad de caché: 4-way#
###########################################

# Creación de tablas para adjuntar valores
# Una tabla por tamaño
tabla_AC4 = pd.DataFrame(index=[
    '400.perlbench-41B', '401.bzip2-226B', '403.gcc-16B', '410.bwaves-1963B', '416.gamess-875B', '429.mcf-184B', '433.milc-127B',
    '435.gromacs-111B', '436.cactusADM-1804B', '437.leslie3d-134B', '444.namd-120B', '445.gobmk-17B',
    '450.soplex-247B', '453.povray-887B', '454.calculix-104B', '456.hmmer-191B', '458.sjeng-1088B', '459.GemsFDTD-1169B',
    '462.libquantum-1343B', '464.h264ref-30B', '465.tonto-1769B', '470.lbm-1274B', '471.omnetpp-188B', '473.astar-153B', '481.wrf-1170B',
    '482.sphinx3-1100B', '483.xalancbmk-127B'], columns=[
    'App', 'Total Misses', 'Miss rate total [%]', 'Misses lectura', 'Miss rate lectura [%]', 'Misses escritura', 'Miss rate escritura [%]'])
tabla_AC4['App'] = tabla_AC4.index

# Files paths
filename_55 = "RESULTS_AC/400AC4.txt"
filename_56 = "RESULTS_AC/401AC4.txt"
filename_57 = "RESULTS_AC/403AC4.txt"
filename_58 = "RESULTS_AC/410AC4.txt"
filename_59 = "RESULTS_AC/416AC4.txt"
filename_60 = "RESULTS_AC/429AC4.txt"
filename_61 = "RESULTS_AC/433AC4.txt"
filename_62 = "RESULTS_AC/435AC4.txt"
filename_63 = "RESULTS_AC/436AC4.txt"
filename_64 = "RESULTS_AC/437AC4.txt"
filename_65 = "RESULTS_AC/444AC4.txt"
filename_66 = "RESULTS_AC/445AC4.txt"
filename_67 = "RESULTS_AC/450AC4.txt"
filename_68 = "RESULTS_AC/453AC4.txt"
filename_69 = "RESULTS_AC/454AC4.txt"
filename_70 = "RESULTS_AC/456AC4.txt"
filename_71 = "RESULTS_AC/458AC4.txt"
filename_72 = "RESULTS_AC/459AC4.txt"
filename_73 = "RESULTS_AC/462AC4.txt"
filename_74 = "RESULTS_AC/464AC4.txt"
filename_75 = "RESULTS_AC/465AC4.txt"
filename_76 = "RESULTS_AC/470AC4.txt"
filename_77 = "RESULTS_AC/471AC4.txt"
filename_78 = "RESULTS_AC/473AC4.txt"
filename_79 = "RESULTS_AC/481AC4.txt"
filename_80 = "RESULTS_AC/482AC4.txt"
filename_81 = "RESULTS_AC/483AC4.txt"

# Content file extracter
with open(filename_55, 'r') as file:
    content_400AC4 = file.read()
with open(filename_56, 'r') as file:
    content_401AC4 = file.read()
with open(filename_57, 'r') as file:
    content_403AC4 = file.read()
with open(filename_58, 'r') as file:
    content_410AC4 = file.read()
with open(filename_59, 'r') as file:
    content_416AC4 = file.read()
with open(filename_60, 'r') as file:
    content_429AC4 = file.read()
with open(filename_61, 'r') as file:
    content_433AC4 = file.read()
with open(filename_62, 'r') as file:
    content_435AC4 = file.read()
with open(filename_63, 'r') as file:
    content_436AC4 = file.read()
with open(filename_64, 'r') as file:
    content_437AC4 = file.read()
with open(filename_65, 'r') as file:
    content_444AC4 = file.read()
with open(filename_66, 'r') as file:
    content_445AC4 = file.read()
with open(filename_67, 'r') as file:
    content_450AC4 = file.read()
with open(filename_68, 'r') as file:
    content_453AC4 = file.read()
with open(filename_69, 'r') as file:
    content_454AC4 = file.read()
with open(filename_70, 'r') as file:
    content_456AC4 = file.read()
with open(filename_71, 'r') as file:
    content_458AC4 = file.read()
with open(filename_72, 'r') as file:
    content_459AC4 = file.read()
with open(filename_73, 'r') as file:
    content_462AC4 = file.read()
with open(filename_74, 'r') as file:
    content_464AC4 = file.read()
with open(filename_75, 'r') as file:
    content_465AC4 = file.read()
with open(filename_76, 'r') as file:
    content_470AC4 = file.read()
with open(filename_77, 'r') as file:
    content_471AC4 = file.read()
with open(filename_78, 'r') as file:
    content_473AC4 = file.read()
with open(filename_79, 'r') as file:
    content_481AC4 = file.read()
with open(filename_80, 'r') as file:
    content_482AC4 = file.read()
with open(filename_81, 'r') as file:
    content_483AC4 = file.read()

# Variables según aplicación

# 400.pearlbench-41B
total_misses_400AC4 = re.search(
    r"Total_misses (\d+)", content_400AC4).group(1)
total_miss_rate_400AC4 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_400AC4).group(1)
total_read_misses_400AC4 = re.search(
    r"Total_read_misses (\d+)", content_400AC4).group(1)
total_read_miss_rate_400AC4 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_400AC4).group(1)
total_write_misses_400AC4 = re.search(
    r"Total_write_misses (\d+)", content_400AC4).group(1)
total_write_miss_rate_400AC4 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_400AC4).group(1)
print(">>>>>All AC4 400.pearlbench-41B variables where obtained successfully")

# 401.bzip2-226B
total_misses_401AC4 = re.search(
    r"Total_misses (\d+)", content_401AC4).group(1)
total_miss_rate_401AC4 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_401AC4).group(1)
total_read_misses_401AC4 = re.search(
    r"Total_read_misses (\d+)", content_401AC4).group(1)
total_read_miss_rate_401AC4 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_401AC4).group(1)
total_write_misses_401AC4 = re.search(
    r"Total_write_misses (\d+)", content_401AC4).group(1)
total_write_miss_rate_401AC4 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_401AC4).group(1)
print(">>>>>All AC4 401.bzip2-226B variables where obtained successfully")

# 403.gcc-16B
total_misses_403AC4 = re.search(
    r"Total_misses (\d+)", content_403AC4).group(1)
total_miss_rate_403AC4 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_403AC4).group(1)
total_read_misses_403AC4 = re.search(
    r"Total_read_misses (\d+)", content_403AC4).group(1)
total_read_miss_rate_403AC4 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_403AC4).group(1)
total_write_misses_403AC4 = re.search(
    r"Total_write_misses (\d+)", content_403AC4).group(1)
total_write_miss_rate_403AC4 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_403AC4).group(1)
print(">>>>>All AC4 403.gcc-16B variables where obtained successfully")

# 410.bwaves-1963B
total_misses_410AC4 = re.search(
    r"Total_misses (\d+)", content_410AC4).group(1)
total_miss_rate_410AC4 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_410AC4).group(1)
total_read_misses_410AC4 = re.search(
    r"Total_read_misses (\d+)", content_410AC4).group(1)
total_read_miss_rate_410AC4 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_410AC4).group(1)
total_write_misses_410AC4 = re.search(
    r"Total_write_misses (\d+)", content_410AC4).group(1)
total_write_miss_rate_410AC4 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_410AC4).group(1)
print(">>>>>All AC4 410.bwaves-1963B variables where obtained successfully")

# 416.gamess-875B
total_misses_416AC4 = re.search(
    r"Total_misses (\d+)", content_416AC4).group(1)
total_miss_rate_416AC4 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_416AC4).group(1)
total_read_misses_416AC4 = re.search(
    r"Total_read_misses (\d+)", content_416AC4).group(1)
total_read_miss_rate_416AC4 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_416AC4).group(1)
total_write_misses_416AC4 = re.search(
    r"Total_write_misses (\d+)", content_416AC4).group(1)
total_write_miss_rate_416AC4 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_416AC4).group(1)
print(">>>>>All AC4 416.gamess-875B variables where obtained successfully")

# 429.mcf-184B
total_misses_429AC4 = re.search(
    r"Total_misses (\d+)", content_429AC4).group(1)
total_miss_rate_429AC4 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_429AC4).group(1)
total_read_misses_429AC4 = re.search(
    r"Total_read_misses (\d+)", content_429AC4).group(1)
total_read_miss_rate_429AC4 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_429AC4).group(1)
total_write_misses_429AC4 = re.search(
    r"Total_write_misses (\d+)", content_429AC4).group(1)
total_write_miss_rate_429AC4 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_429AC4).group(1)
print(">>>>>All AC4 429.mcf-184B variables where obtained successfully")

# 433.milc-127B
total_misses_433AC4 = re.search(
    r"Total_misses (\d+)", content_433AC4).group(1)
total_miss_rate_433AC4 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_433AC4).group(1)
total_read_misses_433AC4 = re.search(
    r"Total_read_misses (\d+)", content_433AC4).group(1)
total_read_miss_rate_433AC4 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_433AC4).group(1)
total_write_misses_433AC4 = re.search(
    r"Total_write_misses (\d+)", content_433AC4).group(1)
total_write_miss_rate_433AC4 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_433AC4).group(1)
print(">>>>>All AC4 433.milc-127B variables where obtained successfully")

# 435.gromacs-111B
total_misses_435AC4 = re.search(
    r"Total_misses (\d+)", content_435AC4).group(1)
total_miss_rate_435AC4 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_435AC4).group(1)
total_read_misses_435AC4 = re.search(
    r"Total_read_misses (\d+)", content_435AC4).group(1)
total_read_miss_rate_435AC4 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_435AC4).group(1)
total_write_misses_435AC4 = re.search(
    r"Total_write_misses (\d+)", content_435AC4).group(1)
total_write_miss_rate_435AC4 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_435AC4).group(1)
print(">>>>>All AC4 435.gromacs-111B variables where obtained successfully")

# 436.cactusADM-1804B
total_misses_436AC4 = re.search(
    r"Total_misses (\d+)", content_436AC4).group(1)
total_miss_rate_436AC4 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_436AC4).group(1)
total_read_misses_436AC4 = re.search(
    r"Total_read_misses (\d+)", content_436AC4).group(1)
total_read_miss_rate_436AC4 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_436AC4).group(1)
total_write_misses_436AC4 = re.search(
    r"Total_write_misses (\d+)", content_436AC4).group(1)
total_write_miss_rate_436AC4 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_436AC4).group(1)
print(">>>>>All AC4 436.cactusADM-1804B variables where obtained successfully")

# 437.leslie3d-134B
total_misses_437AC4 = re.search(
    r"Total_misses (\d+)", content_437AC4).group(1)
total_miss_rate_437AC4 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_437AC4).group(1)
total_read_misses_437AC4 = re.search(
    r"Total_read_misses (\d+)", content_437AC4).group(1)
total_read_miss_rate_437AC4 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_437AC4).group(1)
total_write_misses_437AC4 = re.search(
    r"Total_write_misses (\d+)", content_437AC4).group(1)
total_write_miss_rate_437AC4 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_437AC4).group(1)
print(">>>>>All AC4 437.leslie3d-134B variables where obtained successfully")

# 444.namd-120B
total_misses_444AC4 = re.search(
    r"Total_misses (\d+)", content_444AC4).group(1)
total_miss_rate_444AC4 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_444AC4).group(1)
total_read_misses_444AC4 = re.search(
    r"Total_read_misses (\d+)", content_444AC4).group(1)
total_read_miss_rate_444AC4 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_444AC4).group(1)
total_write_misses_444AC4 = re.search(
    r"Total_write_misses (\d+)", content_444AC4).group(1)
total_write_miss_rate_444AC4 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_444AC4).group(1)
print(">>>>>All AC4 444.namd-120B variables where obtained successfully")

# 445.gobmk-17B
total_misses_445AC4 = re.search(
    r"Total_misses (\d+)", content_445AC4).group(1)
total_miss_rate_445AC4 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_445AC4).group(1)
total_read_misses_445AC4 = re.search(
    r"Total_read_misses (\d+)", content_445AC4).group(1)
total_read_miss_rate_445AC4 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_445AC4).group(1)
total_write_misses_445AC4 = re.search(
    r"Total_write_misses (\d+)", content_445AC4).group(1)
total_write_miss_rate_445AC4 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_445AC4).group(1)
print(">>>>>All AC4 445.gobmk-17B variables where obtained successfully")

# 450.soplex-247B
total_misses_450AC4 = re.search(
    r"Total_misses (\d+)", content_450AC4).group(1)
total_miss_rate_450AC4 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_450AC4).group(1)
total_read_misses_450AC4 = re.search(
    r"Total_read_misses (\d+)", content_450AC4).group(1)
total_read_miss_rate_450AC4 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_450AC4).group(1)
total_write_misses_450AC4 = re.search(
    r"Total_write_misses (\d+)", content_450AC4).group(1)
total_write_miss_rate_450AC4 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_450AC4).group(1)
print(">>>>>All AC4 450.soplex-247B variables where obtained successfully")

# 453.povray-887B
total_misses_453AC4 = re.search(
    r"Total_misses (\d+)", content_453AC4).group(1)
total_miss_rate_453AC4 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_453AC4).group(1)
total_read_misses_453AC4 = re.search(
    r"Total_read_misses (\d+)", content_453AC4).group(1)
total_read_miss_rate_453AC4 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_453AC4).group(1)
total_write_misses_453AC4 = re.search(
    r"Total_write_misses (\d+)", content_453AC4).group(1)
total_write_miss_rate_453AC4 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_453AC4).group(1)
print(">>>>>All AC4 453.povray-887B variables where obtained successfully")

# 454.calculix-104B
total_misses_454AC4 = re.search(
    r"Total_misses (\d+)", content_454AC4).group(1)
total_miss_rate_454AC4 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_454AC4).group(1)
total_read_misses_454AC4 = re.search(
    r"Total_read_misses (\d+)", content_454AC4).group(1)
total_read_miss_rate_454AC4 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_454AC4).group(1)
total_write_misses_454AC4 = re.search(
    r"Total_write_misses (\d+)", content_454AC4).group(1)
total_write_miss_rate_454AC4 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_454AC4).group(1)
print(">>>>>All AC4 454.calculix-104B variables where obtained successfully")

# 456.hmmer-191B
total_misses_456AC4 = re.search(
    r"Total_misses (\d+)", content_456AC4).group(1)
total_miss_rate_456AC4 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_456AC4).group(1)
total_read_misses_456AC4 = re.search(
    r"Total_read_misses (\d+)", content_456AC4).group(1)
total_read_miss_rate_456AC4 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_456AC4).group(1)
total_write_misses_456AC4 = re.search(
    r"Total_write_misses (\d+)", content_456AC4).group(1)
total_write_miss_rate_456AC4 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_456AC4).group(1)
print(">>>>>All AC4 456.hmmer-191B variables where obtained successfully")

# 458.sjeng-1088B
total_misses_458AC4 = re.search(
    r"Total_misses (\d+)", content_458AC4).group(1)
total_miss_rate_458AC4 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_458AC4).group(1)
total_read_misses_458AC4 = re.search(
    r"Total_read_misses (\d+)", content_458AC4).group(1)
total_read_miss_rate_458AC4 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_458AC4).group(1)
total_write_misses_458AC4 = re.search(
    r"Total_write_misses (\d+)", content_458AC4).group(1)
total_write_miss_rate_458AC4 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_458AC4).group(1)
print(">>>>>All AC4 458.sjeng-1088B variables where obtained successfully")

# 459.GemsFDTD-1169B
total_misses_459AC4 = re.search(
    r"Total_misses (\d+)", content_459AC4).group(1)
total_miss_rate_459AC4 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_459AC4).group(1)
total_read_misses_459AC4 = re.search(
    r"Total_read_misses (\d+)", content_459AC4).group(1)
total_read_miss_rate_459AC4 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_459AC4).group(1)
total_write_misses_459AC4 = re.search(
    r"Total_write_misses (\d+)", content_459AC4).group(1)
total_write_miss_rate_459AC4 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_459AC4).group(1)
print(">>>>>All AC4 459.GemsFDTD-1169B variables where obtained successfully")

# 462.libquantum-1343B
total_misses_462AC4 = re.search(
    r"Total_misses (\d+)", content_462AC4).group(1)
total_miss_rate_462AC4 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_462AC4).group(1)
total_read_misses_462AC4 = re.search(
    r"Total_read_misses (\d+)", content_462AC4).group(1)
total_read_miss_rate_462AC4 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_462AC4).group(1)
total_write_misses_462AC4 = re.search(
    r"Total_write_misses (\d+)", content_462AC4).group(1)
total_write_miss_rate_462AC4 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_462AC4).group(1)
print(">>>>>All AC4 462.libquantum-1343B variables where obtained successfully")

# 464.h264ref-30B
total_misses_464AC4 = re.search(
    r"Total_misses (\d+)", content_464AC4).group(1)
total_miss_rate_464AC4 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_464AC4).group(1)
total_read_misses_464AC4 = re.search(
    r"Total_read_misses (\d+)", content_464AC4).group(1)
total_read_miss_rate_464AC4 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_464AC4).group(1)
total_write_misses_464AC4 = re.search(
    r"Total_write_misses (\d+)", content_464AC4).group(1)
total_write_miss_rate_464AC4 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_464AC4).group(1)
print(">>>>>All AC4 464.h264ref-30B variables where obtained successfully")

# 465.tonto-1769B
total_misses_465AC4 = re.search(
    r"Total_misses (\d+)", content_465AC4).group(1)
total_miss_rate_465AC4 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_465AC4).group(1)
total_read_misses_465AC4 = re.search(
    r"Total_read_misses (\d+)", content_465AC4).group(1)
total_read_miss_rate_465AC4 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_465AC4).group(1)
total_write_misses_465AC4 = re.search(
    r"Total_write_misses (\d+)", content_465AC4).group(1)
total_write_miss_rate_465AC4 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_465AC4).group(1)
print(">>>>>All AC4 465.tonto-1769B variables where obtained successfully")

# 470.lbm-1274B
total_misses_470AC4 = re.search(
    r"Total_misses (\d+)", content_470AC4).group(1)
total_miss_rate_470AC4 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_470AC4).group(1)
total_read_misses_470AC4 = re.search(
    r"Total_read_misses (\d+)", content_470AC4).group(1)
total_read_miss_rate_470AC4 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_470AC4).group(1)
total_write_misses_470AC4 = re.search(
    r"Total_write_misses (\d+)", content_470AC4).group(1)
total_write_miss_rate_470AC4 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_470AC4).group(1)
print(">>>>>All AC4 470.lbm-1274B variables where obtained successfully")

# 471.omnetpp-188B
total_misses_471AC4 = re.search(
    r"Total_misses (\d+)", content_471AC4).group(1)
total_miss_rate_471AC4 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_471AC4).group(1)
total_read_misses_471AC4 = re.search(
    r"Total_read_misses (\d+)", content_471AC4).group(1)
total_read_miss_rate_471AC4 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_471AC4).group(1)
total_write_misses_471AC4 = re.search(
    r"Total_write_misses (\d+)", content_471AC4).group(1)
total_write_miss_rate_471AC4 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_471AC4).group(1)
print(">>>>>All AC4 471.omnetpp-188B variables where obtained successfully")

# 473.astar-153B
total_misses_473AC4 = re.search(
    r"Total_misses (\d+)", content_473AC4).group(1)
total_miss_rate_473AC4 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_473AC4).group(1)
total_read_misses_473AC4 = re.search(
    r"Total_read_misses (\d+)", content_473AC4).group(1)
total_read_miss_rate_473AC4 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_473AC4).group(1)
total_write_misses_473AC4 = re.search(
    r"Total_write_misses (\d+)", content_473AC4).group(1)
total_write_miss_rate_473AC4 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_473AC4).group(1)
print(">>>>>All AC4 473.astar-153B variables where obtained successfully")

# 481.wrf-1170B
total_misses_481AC4 = re.search(
    r"Total_misses (\d+)", content_481AC4).group(1)
total_miss_rate_481AC4 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_481AC4).group(1)
total_read_misses_481AC4 = re.search(
    r"Total_read_misses (\d+)", content_481AC4).group(1)
total_read_miss_rate_481AC4 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_481AC4).group(1)
total_write_misses_481AC4 = re.search(
    r"Total_write_misses (\d+)", content_481AC4).group(1)
total_write_miss_rate_481AC4 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_481AC4).group(1)
print(">>>>>All AC4 481.wrf-1170B variables where obtained successfully")

# 482.sphinx3-1100B
total_misses_482AC4 = re.search(
    r"Total_misses (\d+)", content_482AC4).group(1)
total_miss_rate_482AC4 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_482AC4).group(1)
total_read_misses_482AC4 = re.search(
    r"Total_read_misses (\d+)", content_482AC4).group(1)
total_read_miss_rate_482AC4 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_482AC4).group(1)
total_write_misses_482AC4 = re.search(
    r"Total_write_misses (\d+)", content_482AC4).group(1)
total_write_miss_rate_482AC4 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_482AC4).group(1)
print(">>>>>All AC4 482.sphinx3-1100B variables where obtained successfully")

# 483.xalancbmk-127B
total_misses_483AC4 = re.search(
    r"Total_misses (\d+)", content_483AC4).group(1)
total_miss_rate_483AC4 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_483AC4).group(1)
total_read_misses_483AC4 = re.search(
    r"Total_read_misses (\d+)", content_483AC4).group(1)
total_read_miss_rate_483AC4 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_483AC4).group(1)
total_write_misses_483AC4 = re.search(
    r"Total_write_misses (\d+)", content_483AC4).group(1)
total_write_miss_rate_483AC4 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_483AC4).group(1)
print(">>>>>All AC4 483.xalancbmk-127B variables where obtained successfully")

#############################
# Adjunta datos a dataframe #
#############################

# **400.perlbench-41B**

tabla_AC4.at['400.perlbench-41B', 'Total Misses'] = total_misses_400AC4

tabla_AC4.at['400.perlbench-41B',
             'Miss rate total [%]'] = total_miss_rate_400AC4

tabla_AC4.at['400.perlbench-41B',
             'Misses lectura'] = total_read_misses_400AC4

tabla_AC4.at['400.perlbench-41B',
             'Miss rate lectura [%]'] = total_read_miss_rate_400AC4

tabla_AC4.at['400.perlbench-41B',
             'Misses escritura'] = total_write_misses_400AC4

tabla_AC4.at['400.perlbench-41B',
             'Miss rate escritura [%]'] = total_write_miss_rate_400AC4

# **401.bzip2-226B**

tabla_AC4.at['401.bzip2-226B', 'Total Misses'] = total_misses_401AC4

tabla_AC4.at['401.bzip2-226B',
             'Miss rate total [%]'] = total_miss_rate_401AC4

tabla_AC4.at['401.bzip2-226B', 'Misses lectura'] = total_read_misses_401AC4

tabla_AC4.at['401.bzip2-226B',
             'Miss rate lectura [%]'] = total_read_miss_rate_401AC4

tabla_AC4.at['401.bzip2-226B',
             'Misses escritura'] = total_write_misses_401AC4

tabla_AC4.at['401.bzip2-226B',
             'Miss rate escritura [%]'] = total_write_miss_rate_401AC4

# **403.gcc-16B**

tabla_AC4.at['403.gcc-16B', 'Total Misses'] = total_misses_403AC4

tabla_AC4.at['403.gcc-16B', 'Miss rate total [%]'] = total_miss_rate_403AC4

tabla_AC4.at['403.gcc-16B', 'Misses lectura'] = total_read_misses_403AC4

tabla_AC4.at['403.gcc-16B',
             'Miss rate lectura [%]'] = total_read_miss_rate_403AC4

tabla_AC4.at['403.gcc-16B',
             'Misses escritura'] = total_write_misses_403AC4

tabla_AC4.at['403.gcc-16B',
             'Miss rate escritura [%]'] = total_write_miss_rate_403AC4

# **410.bwaves-1963B**

tabla_AC4.at['410.bwaves-1963B', 'Total Misses'] = total_misses_410AC4

tabla_AC4.at['410.bwaves-1963B',
             'Miss rate total [%]'] = total_miss_rate_410AC4

tabla_AC4.at['410.bwaves-1963B', 'Misses lectura'] = total_read_misses_410AC4

tabla_AC4.at['410.bwaves-1963B',
             'Miss rate lectura [%]'] = total_read_miss_rate_410AC4

tabla_AC4.at['410.bwaves-1963B',
             'Misses escritura'] = total_write_misses_410AC4

tabla_AC4.at['410.bwaves-1963B',
             'Miss rate escritura [%]'] = total_write_miss_rate_410AC4

# **416.gamess-875B**

tabla_AC4.at['416.gamess-875B', 'Total Misses'] = total_misses_416AC4

tabla_AC4.at['416.gamess-875B',
             'Miss rate total [%]'] = total_miss_rate_416AC4

tabla_AC4.at['416.gamess-875B', 'Misses lectura'] = total_read_misses_416AC4

tabla_AC4.at['416.gamess-875B',
             'Miss rate lectura [%]'] = total_read_miss_rate_416AC4

tabla_AC4.at['416.gamess-875B',
             'Misses escritura'] = total_write_misses_416AC4

tabla_AC4.at['416.gamess-875B',
             'Miss rate escritura [%]'] = total_write_miss_rate_416AC4

# **429.mcf-184B**

tabla_AC4.at['429.mcf-184B', 'Total Misses'] = total_misses_429AC4

tabla_AC4.at['429.mcf-184B', 'Miss rate total [%]'] = total_miss_rate_429AC4

tabla_AC4.at['429.mcf-184B', 'Misses lectura'] = total_read_misses_429AC4

tabla_AC4.at['429.mcf-184B',
             'Miss rate lectura [%]'] = total_read_miss_rate_429AC4

tabla_AC4.at['429.mcf-184B',
             'Misses escritura'] = total_write_misses_429AC4

tabla_AC4.at['429.mcf-184B',
             'Miss rate escritura [%]'] = total_write_miss_rate_429AC4

# **433.milc-127B**

tabla_AC4.at['433.milc-127B', 'Total Misses'] = total_misses_433AC4

tabla_AC4.at['433.milc-127B', 'Miss rate total [%]'] = total_miss_rate_433AC4

tabla_AC4.at['433.milc-127B', 'Misses lectura'] = total_read_misses_433AC4

tabla_AC4.at['433.milc-127B',
             'Miss rate lectura [%]'] = total_read_miss_rate_433AC4

tabla_AC4.at['433.milc-127B',
             'Misses escritura'] = total_write_misses_433AC4

tabla_AC4.at['433.milc-127B',
             'Miss rate escritura [%]'] = total_write_miss_rate_433AC4

# **435.gromacs-111B**

tabla_AC4.at['435.gromacs-111B', 'Total Misses'] = total_misses_435AC4

tabla_AC4.at['435.gromacs-111B',
             'Miss rate total [%]'] = total_miss_rate_435AC4

tabla_AC4.at['435.gromacs-111B', 'Misses lectura'] = total_read_misses_435AC4

tabla_AC4.at['435.gromacs-111B',
             'Miss rate lectura [%]'] = total_read_miss_rate_435AC4

tabla_AC4.at['435.gromacs-111B',
             'Misses escritura'] = total_write_misses_435AC4

tabla_AC4.at['435.gromacs-111B',
             'Miss rate escritura [%]'] = total_write_miss_rate_435AC4
# **436.cactusADM-1804B**

tabla_AC4.at['436.cactusADM-1804B', 'Total Misses'] = total_misses_436AC4

tabla_AC4.at['436.cactusADM-1804B',
             'Miss rate total [%]'] = total_miss_rate_436AC4

tabla_AC4.at['436.cactusADM-1804B',
             'Misses lectura'] = total_read_misses_436AC4

tabla_AC4.at['436.cactusADM-1804B',
             'Miss rate lectura [%]'] = total_read_miss_rate_436AC4

tabla_AC4.at['436.cactusADM-1804B',
             'Misses escritura'] = total_write_misses_436AC4

tabla_AC4.at['436.cactusADM-1804B',
             'Miss rate escritura [%]'] = total_write_miss_rate_436AC4

# **437.leslie3d-134B**

tabla_AC4.at['437.leslie3d-134B', 'Total Misses'] = total_misses_437AC4

tabla_AC4.at['437.leslie3d-134B',
             'Miss rate total [%]'] = total_miss_rate_437AC4

tabla_AC4.at['437.leslie3d-134B',
             'Misses lectura'] = total_read_misses_437AC4

tabla_AC4.at['437.leslie3d-134B',
             'Miss rate lectura [%]'] = total_read_miss_rate_437AC4

tabla_AC4.at['437.leslie3d-134B',
             'Misses escritura'] = total_write_misses_437AC4

tabla_AC4.at['437.leslie3d-134B',
             'Miss rate escritura [%]'] = total_write_miss_rate_437AC4

# **444.namd-120B**

tabla_AC4.at['444.namd-120B', 'Total Misses'] = total_misses_444AC4

tabla_AC4.at['444.namd-120B', 'Miss rate total [%]'] = total_miss_rate_444AC4

tabla_AC4.at['444.namd-120B', 'Misses lectura'] = total_read_misses_444AC4

tabla_AC4.at['444.namd-120B',
             'Miss rate lectura [%]'] = total_read_miss_rate_444AC4

tabla_AC4.at['444.namd-120B',
             'Misses escritura'] = total_write_misses_444AC4

tabla_AC4.at['444.namd-120B',
             'Miss rate escritura [%]'] = total_write_miss_rate_444AC4

# **445.gobmk-17B**

tabla_AC4.at['445.gobmk-17B', 'Total Misses'] = total_misses_445AC4

tabla_AC4.at['445.gobmk-17B', 'Miss rate total [%]'] = total_miss_rate_445AC4

tabla_AC4.at['445.gobmk-17B', 'Misses lectura'] = total_read_misses_445AC4

tabla_AC4.at['445.gobmk-17B',
             'Miss rate lectura [%]'] = total_read_miss_rate_445AC4

tabla_AC4.at['445.gobmk-17B',
             'Misses escritura'] = total_write_misses_445AC4

tabla_AC4.at['445.gobmk-17B',
             'Miss rate escritura [%]'] = total_write_miss_rate_445AC4

# **450.soplex-247B**

tabla_AC4.at['450.soplex-247B', 'Total Misses'] = total_misses_450AC4

tabla_AC4.at['450.soplex-247B',
             'Miss rate total [%]'] = total_miss_rate_450AC4

tabla_AC4.at['450.soplex-247B', 'Misses lectura'] = total_read_misses_450AC4

tabla_AC4.at['450.soplex-247B',
             'Miss rate lectura [%]'] = total_read_miss_rate_450AC4

tabla_AC4.at['450.soplex-247B',
             'Misses escritura'] = total_write_misses_450AC4

tabla_AC4.at['450.soplex-247B',
             'Miss rate escritura [%]'] = total_write_miss_rate_450AC4

# **453.povray-887B**

tabla_AC4.at['453.povray-887B', 'Total Misses'] = total_misses_453AC4

tabla_AC4.at['453.povray-887B',
             'Miss rate total [%]'] = total_miss_rate_453AC4

tabla_AC4.at['453.povray-887B', 'Misses lectura'] = total_read_misses_453AC4

tabla_AC4.at['453.povray-887B',
             'Miss rate lectura [%]'] = total_read_miss_rate_453AC4

tabla_AC4.at['453.povray-887B',
             'Misses escritura'] = total_write_misses_453AC4

tabla_AC4.at['453.povray-887B',
             'Miss rate escritura [%]'] = total_write_miss_rate_453AC4

# **454.calculix-104B**

tabla_AC4.at['454.calculix-104B', 'Total Misses'] = total_misses_454AC4

tabla_AC4.at['454.calculix-104B',
             'Miss rate total [%]'] = total_miss_rate_454AC4

tabla_AC4.at['454.calculix-104B',
             'Misses lectura'] = total_read_misses_454AC4

tabla_AC4.at['454.calculix-104B',
             'Miss rate lectura [%]'] = total_read_miss_rate_454AC4

tabla_AC4.at['454.calculix-104B',
             'Misses escritura'] = total_write_misses_454AC4

tabla_AC4.at['454.calculix-104B',
             'Miss rate escritura [%]'] = total_write_miss_rate_454AC4

# **456.hmmer-191B**

tabla_AC4.at['456.hmmer-191B', 'Total Misses'] = total_misses_456AC4

tabla_AC4.at['456.hmmer-191B',
             'Miss rate total [%]'] = total_miss_rate_456AC4

tabla_AC4.at['456.hmmer-191B', 'Misses lectura'] = total_read_misses_456AC4

tabla_AC4.at['456.hmmer-191B',
             'Miss rate lectura [%]'] = total_read_miss_rate_456AC4

tabla_AC4.at['456.hmmer-191B',
             'Misses escritura'] = total_write_misses_456AC4

tabla_AC4.at['456.hmmer-191B',
             'Miss rate escritura [%]'] = total_write_miss_rate_456AC4

# **458.sjeng-1088B**

tabla_AC4.at['458.sjeng-1088B', 'Total Misses'] = total_misses_458AC4

tabla_AC4.at['458.sjeng-1088B',
             'Miss rate total [%]'] = total_miss_rate_458AC4

tabla_AC4.at['458.sjeng-1088B', 'Misses lectura'] = total_read_misses_458AC4

tabla_AC4.at['458.sjeng-1088B',
             'Miss rate lectura [%]'] = total_read_miss_rate_458AC4

tabla_AC4.at['458.sjeng-1088B',
             'Misses escritura'] = total_write_misses_458AC4

tabla_AC4.at['458.sjeng-1088B',
             'Miss rate escritura [%]'] = total_write_miss_rate_458AC4

# **459.GemsFDTD-1169B**

tabla_AC4.at['459.GemsFDTD-1169B', 'Total Misses'] = total_misses_459AC4

tabla_AC4.at['459.GemsFDTD-1169B',
             'Miss rate total [%]'] = total_miss_rate_459AC4

tabla_AC4.at['459.GemsFDTD-1169B',
             'Misses lectura'] = total_read_misses_459AC4

tabla_AC4.at['459.GemsFDTD-1169B',
             'Miss rate lectura [%]'] = total_read_miss_rate_459AC4

tabla_AC4.at['459.GemsFDTD-1169B',
             'Misses escritura'] = total_write_misses_459AC4

tabla_AC4.at['459.GemsFDTD-1169B',
             'Miss rate escritura [%]'] = total_write_miss_rate_459AC4

# **462.libquantum-1343B**

tabla_AC4.at['462.libquantum-1343B', 'Total Misses'] = total_misses_462AC4

tabla_AC4.at['462.libquantum-1343B',
             'Miss rate total [%]'] = total_miss_rate_462AC4

tabla_AC4.at['462.libquantum-1343B',
             'Misses lectura'] = total_read_misses_462AC4

tabla_AC4.at['462.libquantum-1343B',
             'Miss rate lectura [%]'] = total_read_miss_rate_462AC4

tabla_AC4.at['462.libquantum-1343B',
             'Misses escritura'] = total_write_misses_462AC4

tabla_AC4.at['462.libquantum-1343B',
             'Miss rate escritura [%]'] = total_write_miss_rate_462AC4

# **464.h264ref-30B**

tabla_AC4.at['464.h264ref-30B', 'Total Misses'] = total_misses_464AC4

tabla_AC4.at['464.h264ref-30B',
             'Miss rate total [%]'] = total_miss_rate_464AC4

tabla_AC4.at['464.h264ref-30B', 'Misses lectura'] = total_read_misses_464AC4

tabla_AC4.at['464.h264ref-30B',
             'Miss rate lectura [%]'] = total_read_miss_rate_464AC4

tabla_AC4.at['464.h264ref-30B',
             'Misses escritura'] = total_write_misses_464AC4

tabla_AC4.at['464.h264ref-30B',
             'Miss rate escritura [%]'] = total_write_miss_rate_464AC4

# **465.tonto-1769B**

tabla_AC4.at['465.tonto-1769B', 'Total Misses'] = total_misses_465AC4

tabla_AC4.at['465.tonto-1769B',
             'Miss rate total [%]'] = total_miss_rate_465AC4

tabla_AC4.at['465.tonto-1769B', 'Misses lectura'] = total_read_misses_465AC4

tabla_AC4.at['465.tonto-1769B',
             'Miss rate lectura [%]'] = total_read_miss_rate_465AC4

tabla_AC4.at['465.tonto-1769B',
             'Misses escritura'] = total_write_misses_465AC4
tabla_AC4.at['465.tonto-1769B',
             'Miss rate escritura [%]'] = total_write_miss_rate_465AC4

# **470.lbm-1274B**

tabla_AC4.at['470.lbm-1274B', 'Total Misses'] = total_misses_470AC4

tabla_AC4.at['470.lbm-1274B', 'Miss rate total [%]'] = total_miss_rate_470AC4

tabla_AC4.at['470.lbm-1274B', 'Misses lectura'] = total_read_misses_470AC4

tabla_AC4.at['470.lbm-1274B',
             'Miss rate lectura [%]'] = total_read_miss_rate_470AC4

tabla_AC4.at['470.lbm-1274B',
             'Misses escritura'] = total_write_misses_470AC4

tabla_AC4.at['470.lbm-1274B',
             'Miss rate escritura [%]'] = total_write_miss_rate_470AC4

# **471.omnetpp-188B**

tabla_AC4.at['471.omnetpp-188B', 'Total Misses'] = total_misses_471AC4

tabla_AC4.at['471.omnetpp-188B',
             'Miss rate total [%]'] = total_miss_rate_471AC4

tabla_AC4.at['471.omnetpp-188B', 'Misses lectura'] = total_read_misses_471AC4

tabla_AC4.at['471.omnetpp-188B',
             'Miss rate lectura [%]'] = total_read_miss_rate_471AC4

tabla_AC4.at['471.omnetpp-188B',
             'Misses escritura'] = total_write_misses_471AC4

tabla_AC4.at['471.omnetpp-188B',
             'Miss rate escritura [%]'] = total_write_miss_rate_471AC4

# **473.astar-153B**

tabla_AC4.at['473.astar-153B', 'Total Misses'] = total_misses_473AC4

tabla_AC4.at['473.astar-153B',
             'Miss rate total [%]'] = total_miss_rate_473AC4

tabla_AC4.at['473.astar-153B', 'Misses lectura'] = total_read_misses_473AC4

tabla_AC4.at['473.astar-153B',
             'Miss rate lectura [%]'] = total_read_miss_rate_473AC4

tabla_AC4.at['473.astar-153B',
             'Misses escritura'] = total_write_misses_473AC4

tabla_AC4.at['473.astar-153B',
             'Miss rate escritura [%]'] = total_write_miss_rate_473AC4

# **481.wrf-1170B**

tabla_AC4.at['481.wrf-1170B', 'Total Misses'] = total_misses_481AC4

tabla_AC4.at['481.wrf-1170B', 'Miss rate total [%]'] = total_miss_rate_481AC4

tabla_AC4.at['481.wrf-1170B', 'Misses lectura'] = total_read_misses_481AC4

tabla_AC4.at['481.wrf-1170B',
             'Miss rate lectura [%]'] = total_read_miss_rate_481AC4

tabla_AC4.at['481.wrf-1170B',
             'Misses escritura'] = total_write_misses_481AC4

tabla_AC4.at['481.wrf-1170B',
             'Miss rate escritura [%]'] = total_write_miss_rate_481AC4

# **482.sphinx3-1100B**

tabla_AC4.at['482.sphinx3-1100B', 'Total Misses'] = total_misses_482AC4

tabla_AC4.at['482.sphinx3-1100B',
             'Miss rate total [%]'] = total_miss_rate_482AC4

tabla_AC4.at['482.sphinx3-1100B',
             'Misses lectura'] = total_read_misses_482AC4

tabla_AC4.at['482.sphinx3-1100B',
             'Miss rate lectura [%]'] = total_read_miss_rate_482AC4

tabla_AC4.at['482.sphinx3-1100B',
             'Misses escritura'] = total_write_misses_482AC4

tabla_AC4.at['482.sphinx3-1100B',
             'Miss rate escritura [%]'] = total_write_miss_rate_482AC4

# **483.xalancbmk-127B**

tabla_AC4.at['483.xalancbmk-127B', 'Total Misses'] = total_misses_483AC4

tabla_AC4.at['483.xalancbmk-127B',
             'Miss rate total [%]'] = total_miss_rate_483AC4

tabla_AC4.at['483.xalancbmk-127B',
             'Misses lectura'] = total_read_misses_483AC4

tabla_AC4.at['483.xalancbmk-127B',
             'Miss rate lectura [%]'] = total_read_miss_rate_483AC4

tabla_AC4.at['483.xalancbmk-127B',
             'Misses escritura'] = total_write_misses_483AC4

tabla_AC4.at['483.xalancbmk-127B',
             'Miss rate escritura [%]'] = total_write_miss_rate_483AC4

print(">>>>>All AC4 data has been uploaded successfully")

###########################################
# Extractor para experimento con tamaño 64#
###########################################

# Creación de tablas para adjuntar valores
# Una tabla por tamaño
tabla_AC8 = pd.DataFrame(index=[
    '400.perlbench-41B', '401.bzip2-226B', '403.gcc-16B', '410.bwaves-1963B', '416.gamess-875B', '429.mcf-184B', '433.milc-127B',
    '435.gromacs-111B', '436.cactusADM-1804B', '437.leslie3d-134B', '444.namd-120B', '445.gobmk-17B',
    '450.soplex-247B', '453.povray-887B', '454.calculix-104B', '456.hmmer-191B', '458.sjeng-1088B', '459.GemsFDTD-1169B',
    '462.libquantum-1343B', '464.h264ref-30B', '465.tonto-1769B', '470.lbm-1274B', '471.omnetpp-188B', '473.astar-153B', '481.wrf-1170B',
    '482.sphinx3-1100B', '483.xalancbmk-127B'], columns=[
    'App', 'Total Misses', 'Miss rate total [%]', 'Misses lectura', 'Miss rate lectura [%]', 'Misses escritura', 'Miss rate escritura [%]'])
tabla_AC8['App'] = tabla_AC8.index

# Files paths
filename_82 = "RESULTS_AC/400AC8.txt"
filename_83 = "RESULTS_AC/401AC8.txt"
filename_84 = "RESULTS_AC/403AC8.txt"
filename_85 = "RESULTS_AC/410AC8.txt"
filename_86 = "RESULTS_AC/416AC8.txt"
filename_87 = "RESULTS_AC/429AC8.txt"
filename_88 = "RESULTS_AC/433AC8.txt"
filename_89 = "RESULTS_AC/435AC8.txt"
filename_90 = "RESULTS_AC/436AC8.txt"
filename_91 = "RESULTS_AC/437AC8.txt"
filename_92 = "RESULTS_AC/444AC8.txt"
filename_93 = "RESULTS_AC/445AC8.txt"
filename_94 = "RESULTS_AC/450AC8.txt"
filename_95 = "RESULTS_AC/453AC8.txt"
filename_96 = "RESULTS_AC/454AC8.txt"
filename_97 = "RESULTS_AC/456AC8.txt"
filename_98 = "RESULTS_AC/458AC8.txt"
filename_99 = "RESULTS_AC/459AC8.txt"
filename_100 = "RESULTS_AC/462AC8.txt"
filename_101 = "RESULTS_AC/464AC8.txt"
filename_102 = "RESULTS_AC/465AC8.txt"
filename_103 = "RESULTS_AC/470AC8.txt"
filename_104 = "RESULTS_AC/471AC8.txt"
filename_105 = "RESULTS_AC/473AC8.txt"
filename_106 = "RESULTS_AC/481AC8.txt"
filename_107 = "RESULTS_AC/482AC8.txt"
filename_108 = "RESULTS_AC/483AC8.txt"

# Content file extracter
with open(filename_82, 'r') as file:
    content_400AC8 = file.read()
with open(filename_83, 'r') as file:
    content_401AC8 = file.read()
with open(filename_84, 'r') as file:
    content_403AC8 = file.read()
with open(filename_85, 'r') as file:
    content_410AC8 = file.read()
with open(filename_86, 'r') as file:
    content_416AC8 = file.read()
with open(filename_87, 'r') as file:
    content_429AC8 = file.read()
with open(filename_88, 'r') as file:
    content_433AC8 = file.read()
with open(filename_89, 'r') as file:
    content_435AC8 = file.read()
with open(filename_90, 'r') as file:
    content_436AC8 = file.read()
with open(filename_91, 'r') as file:
    content_437AC8 = file.read()
with open(filename_92, 'r') as file:
    content_444AC8 = file.read()
with open(filename_93, 'r') as file:
    content_445AC8 = file.read()
with open(filename_94, 'r') as file:
    content_450AC8 = file.read()
with open(filename_95, 'r') as file:
    content_453AC8 = file.read()
with open(filename_96, 'r') as file:
    content_454AC8 = file.read()
with open(filename_97, 'r') as file:
    content_456AC8 = file.read()
with open(filename_98, 'r') as file:
    content_458AC8 = file.read()
with open(filename_99, 'r') as file:
    content_459AC8 = file.read()
with open(filename_100, 'r') as file:
    content_462AC8 = file.read()
with open(filename_101, 'r') as file:
    content_464AC8 = file.read()
with open(filename_102, 'r') as file:
    content_465AC8 = file.read()
with open(filename_103, 'r') as file:
    content_470AC8 = file.read()
with open(filename_104, 'r') as file:
    content_471AC8 = file.read()
with open(filename_105, 'r') as file:
    content_473AC8 = file.read()
with open(filename_106, 'r') as file:
    content_481AC8 = file.read()
with open(filename_107, 'r') as file:
    content_482AC8 = file.read()
with open(filename_108, 'r') as file:
    content_483AC8 = file.read()

# Variables según aplicación

# 400.pearlbench-41B
total_misses_400AC8 = re.search(
    r"Total_misses (\d+)", content_400AC8).group(1)
total_miss_rate_400AC8 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_400AC8).group(1)
total_read_misses_400AC8 = re.search(
    r"Total_read_misses (\d+)", content_400AC8).group(1)
total_read_miss_rate_400AC8 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_400AC8).group(1)
total_write_misses_400AC8 = re.search(
    r"Total_write_misses (\d+)", content_400AC8).group(1)
total_write_miss_rate_400AC8 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_400AC8).group(1)
print(">>>>>All AC8 400.pearlbench-41B variables where obtained successfully")

# 401.bzip2-226B
total_misses_401AC8 = re.search(
    r"Total_misses (\d+)", content_401AC8).group(1)
total_miss_rate_401AC8 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_401AC8).group(1)
total_read_misses_401AC8 = re.search(
    r"Total_read_misses (\d+)", content_401AC8).group(1)
total_read_miss_rate_401AC8 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_401AC8).group(1)
total_write_misses_401AC8 = re.search(
    r"Total_write_misses (\d+)", content_401AC8).group(1)
total_write_miss_rate_401AC8 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_401AC8).group(1)
print(">>>>>All AC8 401.bzip2-226B variables where obtained successfully")

# 403.gcc-16B
total_misses_403AC8 = re.search(
    r"Total_misses (\d+)", content_403AC8).group(1)
total_miss_rate_403AC8 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_403AC8).group(1)
total_read_misses_403AC8 = re.search(
    r"Total_read_misses (\d+)", content_403AC8).group(1)
total_read_miss_rate_403AC8 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_403AC8).group(1)
total_write_misses_403AC8 = re.search(
    r"Total_write_misses (\d+)", content_403AC8).group(1)
total_write_miss_rate_403AC8 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_403AC8).group(1)
print(">>>>>All AC8 403.gcc-16B variables where obtained successfully")

# 410.bwaves-1963B
total_misses_410AC8 = re.search(
    r"Total_misses (\d+)", content_410AC8).group(1)
total_miss_rate_410AC8 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_410AC8).group(1)
total_read_misses_410AC8 = re.search(
    r"Total_read_misses (\d+)", content_410AC8).group(1)
total_read_miss_rate_410AC8 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_410AC8).group(1)
total_write_misses_410AC8 = re.search(
    r"Total_write_misses (\d+)", content_410AC8).group(1)
total_write_miss_rate_410AC8 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_410AC8).group(1)
print(">>>>>All AC8 410.bwaves-1963B variables where obtained successfully")

# 416.gamess-875B
total_misses_416AC8 = re.search(
    r"Total_misses (\d+)", content_416AC8).group(1)
total_miss_rate_416AC8 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_416AC8).group(1)
total_read_misses_416AC8 = re.search(
    r"Total_read_misses (\d+)", content_416AC8).group(1)
total_read_miss_rate_416AC8 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_416AC8).group(1)
total_write_misses_416AC8 = re.search(
    r"Total_write_misses (\d+)", content_416AC8).group(1)
total_write_miss_rate_416AC8 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_416AC8).group(1)
print(">>>>>All AC8 416.gamess-875B variables where obtained successfully")

# 429.mcf-184B
total_misses_429AC8 = re.search(
    r"Total_misses (\d+)", content_429AC8).group(1)
total_miss_rate_429AC8 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_429AC8).group(1)
total_read_misses_429AC8 = re.search(
    r"Total_read_misses (\d+)", content_429AC8).group(1)
total_read_miss_rate_429AC8 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_429AC8).group(1)
total_write_misses_429AC8 = re.search(
    r"Total_write_misses (\d+)", content_429AC8).group(1)
total_write_miss_rate_429AC8 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_429AC8).group(1)
print(">>>>>All AC8 429.mcf-184B variables where obtained successfully")

# 433.milc-127B
total_misses_433AC8 = re.search(
    r"Total_misses (\d+)", content_433AC8).group(1)
total_miss_rate_433AC8 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_433AC8).group(1)
total_read_misses_433AC8 = re.search(
    r"Total_read_misses (\d+)", content_433AC8).group(1)
total_read_miss_rate_433AC8 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_433AC8).group(1)
total_write_misses_433AC8 = re.search(
    r"Total_write_misses (\d+)", content_433AC8).group(1)
total_write_miss_rate_433AC8 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_433AC8).group(1)
print(">>>>>All AC8 433.milc-127B variables where obtained successfully")

# 435.gromacs-111B
total_misses_435AC8 = re.search(
    r"Total_misses (\d+)", content_435AC8).group(1)
total_miss_rate_435AC8 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_435AC8).group(1)
total_read_misses_435AC8 = re.search(
    r"Total_read_misses (\d+)", content_435AC8).group(1)
total_read_miss_rate_435AC8 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_435AC8).group(1)
total_write_misses_435AC8 = re.search(
    r"Total_write_misses (\d+)", content_435AC8).group(1)
total_write_miss_rate_435AC8 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_435AC8).group(1)
print(">>>>>All AC8 435.gromacs-111B variables where obtained successfully")

# 436.cactusADM-1804B
total_misses_436AC8 = re.search(
    r"Total_misses (\d+)", content_436AC8).group(1)
total_miss_rate_436AC8 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_436AC8).group(1)
total_read_misses_436AC8 = re.search(
    r"Total_read_misses (\d+)", content_436AC8).group(1)
total_read_miss_rate_436AC8 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_436AC8).group(1)
total_write_misses_436AC8 = re.search(
    r"Total_write_misses (\d+)", content_436AC8).group(1)
total_write_miss_rate_436AC8 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_436AC8).group(1)
print(">>>>>All AC8 436.cactusADM-1804B variables where obtained successfully")

# 437.leslie3d-134B
total_misses_437AC8 = re.search(
    r"Total_misses (\d+)", content_437AC8).group(1)
total_miss_rate_437AC8 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_437AC8).group(1)
total_read_misses_437AC8 = re.search(
    r"Total_read_misses (\d+)", content_437AC8).group(1)
total_read_miss_rate_437AC8 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_437AC8).group(1)
total_write_misses_437AC8 = re.search(
    r"Total_write_misses (\d+)", content_437AC8).group(1)
total_write_miss_rate_437AC8 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_437AC8).group(1)
print(">>>>>All AC8 437.leslie3d-134B variables where obtained successfully")

# 444.namd-120B
total_misses_444AC8 = re.search(
    r"Total_misses (\d+)", content_444AC8).group(1)
total_miss_rate_444AC8 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_444AC8).group(1)
total_read_misses_444AC8 = re.search(
    r"Total_read_misses (\d+)", content_444AC8).group(1)
total_read_miss_rate_444AC8 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_444AC8).group(1)
total_write_misses_444AC8 = re.search(
    r"Total_write_misses (\d+)", content_444AC8).group(1)
total_write_miss_rate_444AC8 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_444AC8).group(1)
print(">>>>>All AC8 444.namd-120B variables where obtained successfully")

# 445.gobmk-17B
total_misses_445AC8 = re.search(
    r"Total_misses (\d+)", content_445AC8).group(1)
total_miss_rate_445AC8 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_445AC8).group(1)
total_read_misses_445AC8 = re.search(
    r"Total_read_misses (\d+)", content_445AC8).group(1)
total_read_miss_rate_445AC8 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_445AC8).group(1)
total_write_misses_445AC8 = re.search(
    r"Total_write_misses (\d+)", content_445AC8).group(1)
total_write_miss_rate_445AC8 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_445AC8).group(1)
print(">>>>>All AC8 445.gobmk-17B variables where obtained successfully")

# 450.soplex-247B
total_misses_450AC8 = re.search(
    r"Total_misses (\d+)", content_450AC8).group(1)
total_miss_rate_450AC8 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_450AC8).group(1)
total_read_misses_450AC8 = re.search(
    r"Total_read_misses (\d+)", content_450AC8).group(1)
total_read_miss_rate_450AC8 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_450AC8).group(1)
total_write_misses_450AC8 = re.search(
    r"Total_write_misses (\d+)", content_450AC8).group(1)
total_write_miss_rate_450AC8 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_450AC8).group(1)
print(">>>>>All AC8 450.soplex-247B variables where obtained successfully")

# 453.povray-887B
total_misses_453AC8 = re.search(
    r"Total_misses (\d+)", content_453AC8).group(1)
total_miss_rate_453AC8 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_453AC8).group(1)
total_read_misses_453AC8 = re.search(
    r"Total_read_misses (\d+)", content_453AC8).group(1)
total_read_miss_rate_453AC8 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_453AC8).group(1)
total_write_misses_453AC8 = re.search(
    r"Total_write_misses (\d+)", content_453AC8).group(1)
total_write_miss_rate_453AC8 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_453AC8).group(1)
print(">>>>>All AC8 453.povray-887B variables where obtained successfully")

# 454.calculix-104B
total_misses_454AC8 = re.search(
    r"Total_misses (\d+)", content_454AC8).group(1)
total_miss_rate_454AC8 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_454AC8).group(1)
total_read_misses_454AC8 = re.search(
    r"Total_read_misses (\d+)", content_454AC8).group(1)
total_read_miss_rate_454AC8 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_454AC8).group(1)
total_write_misses_454AC8 = re.search(
    r"Total_write_misses (\d+)", content_454AC8).group(1)
total_write_miss_rate_454AC8 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_454AC8).group(1)
print(">>>>>All AC8 454.calculix-104B variables where obtained successfully")

# 456.hmmer-191B
total_misses_456AC8 = re.search(
    r"Total_misses (\d+)", content_456AC8).group(1)
total_miss_rate_456AC8 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_456AC8).group(1)
total_read_misses_456AC8 = re.search(
    r"Total_read_misses (\d+)", content_456AC8).group(1)
total_read_miss_rate_456AC8 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_456AC8).group(1)
total_write_misses_456AC8 = re.search(
    r"Total_write_misses (\d+)", content_456AC8).group(1)
total_write_miss_rate_456AC8 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_456AC8).group(1)
print(">>>>>All AC8 456.hmmer-191B variables where obtained successfully")

# 458.sjeng-1088B
total_misses_458AC8 = re.search(
    r"Total_misses (\d+)", content_458AC8).group(1)
total_miss_rate_458AC8 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_458AC8).group(1)
total_read_misses_458AC8 = re.search(
    r"Total_read_misses (\d+)", content_458AC8).group(1)
total_read_miss_rate_458AC8 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_458AC8).group(1)
total_write_misses_458AC8 = re.search(
    r"Total_write_misses (\d+)", content_458AC8).group(1)
total_write_miss_rate_458AC8 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_458AC8).group(1)
print(">>>>>All AC8 458.sjeng-1088B variables where obtained successfully")

# 459.GemsFDTD-1169B
total_misses_459AC8 = re.search(
    r"Total_misses (\d+)", content_459AC8).group(1)
total_miss_rate_459AC8 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_459AC8).group(1)
total_read_misses_459AC8 = re.search(
    r"Total_read_misses (\d+)", content_459AC8).group(1)
total_read_miss_rate_459AC8 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_459AC8).group(1)
total_write_misses_459AC8 = re.search(
    r"Total_write_misses (\d+)", content_459AC8).group(1)
total_write_miss_rate_459AC8 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_459AC8).group(1)
print(">>>>>All AC8 459.GemsFDTD-1169B variables where obtained successfully")

# 462.libquantum-1343B
total_misses_462AC8 = re.search(
    r"Total_misses (\d+)", content_462AC8).group(1)
total_miss_rate_462AC8 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_462AC8).group(1)
total_read_misses_462AC8 = re.search(
    r"Total_read_misses (\d+)", content_462AC8).group(1)
total_read_miss_rate_462AC8 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_462AC8).group(1)
total_write_misses_462AC8 = re.search(
    r"Total_write_misses (\d+)", content_462AC8).group(1)
total_write_miss_rate_462AC8 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_462AC8).group(1)
print(">>>>>All AC8 462.libquantum-1343B variables where obtained successfully")

# 464.h264ref-30B
total_misses_464AC8 = re.search(
    r"Total_misses (\d+)", content_464AC8).group(1)
total_miss_rate_464AC8 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_464AC8).group(1)
total_read_misses_464AC8 = re.search(
    r"Total_read_misses (\d+)", content_464AC8).group(1)
total_read_miss_rate_464AC8 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_464AC8).group(1)
total_write_misses_464AC8 = re.search(
    r"Total_write_misses (\d+)", content_464AC8).group(1)
total_write_miss_rate_464AC8 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_464AC8).group(1)
print(">>>>>All AC8 464.h264ref-30B variables where obtained successfully")

# 465.tonto-1769B
total_misses_465AC8 = re.search(
    r"Total_misses (\d+)", content_465AC8).group(1)
total_miss_rate_465AC8 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_465AC8).group(1)
total_read_misses_465AC8 = re.search(
    r"Total_read_misses (\d+)", content_465AC8).group(1)
total_read_miss_rate_465AC8 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_465AC8).group(1)
total_write_misses_465AC8 = re.search(
    r"Total_write_misses (\d+)", content_465AC8).group(1)
total_write_miss_rate_465AC8 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_465AC8).group(1)
print(">>>>>All AC8 465.tonto-1769B variables where obtained successfully")

# 470.lbm-1274B
total_misses_470AC8 = re.search(
    r"Total_misses (\d+)", content_470AC8).group(1)
total_miss_rate_470AC8 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_470AC8).group(1)
total_read_misses_470AC8 = re.search(
    r"Total_read_misses (\d+)", content_470AC8).group(1)
total_read_miss_rate_470AC8 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_470AC8).group(1)
total_write_misses_470AC8 = re.search(
    r"Total_write_misses (\d+)", content_470AC8).group(1)
total_write_miss_rate_470AC8 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_470AC8).group(1)
print(">>>>>All AC8 470.lbm-1274B variables where obtained successfully")

# 471.omnetpp-188B
total_misses_471AC8 = re.search(
    r"Total_misses (\d+)", content_471AC8).group(1)
total_miss_rate_471AC8 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_471AC8).group(1)
total_read_misses_471AC8 = re.search(
    r"Total_read_misses (\d+)", content_471AC8).group(1)
total_read_miss_rate_471AC8 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_471AC8).group(1)
total_write_misses_471AC8 = re.search(
    r"Total_write_misses (\d+)", content_471AC8).group(1)
total_write_miss_rate_471AC8 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_471AC8).group(1)
print(">>>>>All AC8 471.omnetpp-188B variables where obtained successfully")

# 473.astar-153B
total_misses_473AC8 = re.search(
    r"Total_misses (\d+)", content_473AC8).group(1)
total_miss_rate_473AC8 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_473AC8).group(1)
total_read_misses_473AC8 = re.search(
    r"Total_read_misses (\d+)", content_473AC8).group(1)
total_read_miss_rate_473AC8 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_473AC8).group(1)
total_write_misses_473AC8 = re.search(
    r"Total_write_misses (\d+)", content_473AC8).group(1)
total_write_miss_rate_473AC8 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_473AC8).group(1)
print(">>>>>All AC8 473.astar-153B variables where obtained successfully")

# 481.wrf-1170B
total_misses_481AC8 = re.search(
    r"Total_misses (\d+)", content_481AC8).group(1)
total_miss_rate_481AC8 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_481AC8).group(1)
total_read_misses_481AC8 = re.search(
    r"Total_read_misses (\d+)", content_481AC8).group(1)
total_read_miss_rate_481AC8 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_481AC8).group(1)
total_write_misses_481AC8 = re.search(
    r"Total_write_misses (\d+)", content_481AC8).group(1)
total_write_miss_rate_481AC8 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_481AC8).group(1)
print(">>>>>All AC8 481.wrf-1170B variables where obtained successfully")

# 482.sphinx3-1100B
total_misses_482AC8 = re.search(
    r"Total_misses (\d+)", content_482AC8).group(1)
total_miss_rate_482AC8 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_482AC8).group(1)
total_read_misses_482AC8 = re.search(
    r"Total_read_misses (\d+)", content_482AC8).group(1)
total_read_miss_rate_482AC8 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_482AC8).group(1)
total_write_misses_482AC8 = re.search(
    r"Total_write_misses (\d+)", content_482AC8).group(1)
total_write_miss_rate_482AC8 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_482AC8).group(1)
print(">>>>>All AC8 482.sphinx3-1100B variables where obtained successfully")

# 483.xalancbmk-127B
total_misses_483AC8 = re.search(
    r"Total_misses (\d+)", content_483AC8).group(1)
total_miss_rate_483AC8 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_483AC8).group(1)
total_read_misses_483AC8 = re.search(
    r"Total_read_misses (\d+)", content_483AC8).group(1)
total_read_miss_rate_483AC8 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_483AC8).group(1)
total_write_misses_483AC8 = re.search(
    r"Total_write_misses (\d+)", content_483AC8).group(1)
total_write_miss_rate_483AC8 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_483AC8).group(1)
print(">>>>>All AC8 483.xalancbmk-127B variables where obtained successfully")

#############################
# Adjunta datos a dataframe #
#############################

# **400.perlbench-41B**

tabla_AC8.at['400.perlbench-41B', 'Total Misses'] = total_misses_400AC8

tabla_AC8.at['400.perlbench-41B',
             'Miss rate total [%]'] = total_miss_rate_400AC8

tabla_AC8.at['400.perlbench-41B',
             'Misses lectura'] = total_read_misses_400AC8

tabla_AC8.at['400.perlbench-41B',
             'Miss rate lectura [%]'] = total_read_miss_rate_400AC8

tabla_AC8.at['400.perlbench-41B',
             'Misses escritura'] = total_write_misses_400AC8

tabla_AC8.at['400.perlbench-41B',
             'Miss rate escritura [%]'] = total_write_miss_rate_400AC8

# **401.bzip2-226B**

tabla_AC8.at['401.bzip2-226B', 'Total Misses'] = total_misses_401AC8

tabla_AC8.at['401.bzip2-226B',
             'Miss rate total [%]'] = total_miss_rate_401AC8

tabla_AC8.at['401.bzip2-226B', 'Misses lectura'] = total_read_misses_401AC8

tabla_AC8.at['401.bzip2-226B',
             'Miss rate lectura [%]'] = total_read_miss_rate_401AC8

tabla_AC8.at['401.bzip2-226B',
             'Misses escritura'] = total_write_misses_401AC8

tabla_AC8.at['401.bzip2-226B',
             'Miss rate escritura [%]'] = total_write_miss_rate_401AC8

# **403.gcc-16B**

tabla_AC8.at['403.gcc-16B', 'Total Misses'] = total_misses_403AC8

tabla_AC8.at['403.gcc-16B', 'Miss rate total [%]'] = total_miss_rate_403AC8

tabla_AC8.at['403.gcc-16B', 'Misses lectura'] = total_read_misses_403AC8

tabla_AC8.at['403.gcc-16B',
             'Miss rate lectura [%]'] = total_read_miss_rate_403AC8

tabla_AC8.at['403.gcc-16B',
             'Misses escritura'] = total_write_misses_403AC8

tabla_AC8.at['403.gcc-16B',
             'Miss rate escritura [%]'] = total_write_miss_rate_403AC8

# **410.bwaves-1963B**

tabla_AC8.at['410.bwaves-1963B', 'Total Misses'] = total_misses_410AC8

tabla_AC8.at['410.bwaves-1963B',
             'Miss rate total [%]'] = total_miss_rate_410AC8

tabla_AC8.at['410.bwaves-1963B', 'Misses lectura'] = total_read_misses_410AC8

tabla_AC8.at['410.bwaves-1963B',
             'Miss rate lectura [%]'] = total_read_miss_rate_410AC8

tabla_AC8.at['410.bwaves-1963B',
             'Misses escritura'] = total_write_misses_410AC8

tabla_AC8.at['410.bwaves-1963B',
             'Miss rate escritura [%]'] = total_write_miss_rate_410AC8

# **416.gamess-875B**

tabla_AC8.at['416.gamess-875B', 'Total Misses'] = total_misses_416AC8

tabla_AC8.at['416.gamess-875B',
             'Miss rate total [%]'] = total_miss_rate_416AC8

tabla_AC8.at['416.gamess-875B', 'Misses lectura'] = total_read_misses_416AC8

tabla_AC8.at['416.gamess-875B',
             'Miss rate lectura [%]'] = total_read_miss_rate_416AC8

tabla_AC8.at['416.gamess-875B',
             'Misses escritura'] = total_write_misses_416AC8

tabla_AC8.at['416.gamess-875B',
             'Miss rate escritura [%]'] = total_write_miss_rate_416AC8

# **429.mcf-184B**

tabla_AC8.at['429.mcf-184B', 'Total Misses'] = total_misses_429AC8

tabla_AC8.at['429.mcf-184B', 'Miss rate total [%]'] = total_miss_rate_429AC8

tabla_AC8.at['429.mcf-184B', 'Misses lectura'] = total_read_misses_429AC8

tabla_AC8.at['429.mcf-184B',
             'Miss rate lectura [%]'] = total_read_miss_rate_429AC8

tabla_AC8.at['429.mcf-184B',
             'Misses escritura'] = total_write_misses_429AC8

tabla_AC8.at['429.mcf-184B',
             'Miss rate escritura [%]'] = total_write_miss_rate_429AC8

# **433.milc-127B**

tabla_AC8.at['433.milc-127B', 'Total Misses'] = total_misses_433AC8

tabla_AC8.at['433.milc-127B', 'Miss rate total [%]'] = total_miss_rate_433AC8

tabla_AC8.at['433.milc-127B', 'Misses lectura'] = total_read_misses_433AC8

tabla_AC8.at['433.milc-127B',
             'Miss rate lectura [%]'] = total_read_miss_rate_433AC8

tabla_AC8.at['433.milc-127B',
             'Misses escritura'] = total_write_misses_433AC8

tabla_AC8.at['433.milc-127B',
             'Miss rate escritura [%]'] = total_write_miss_rate_433AC8

# **435.gromacs-111B**

tabla_AC8.at['435.gromacs-111B', 'Total Misses'] = total_misses_435AC8

tabla_AC8.at['435.gromacs-111B',
             'Miss rate total [%]'] = total_miss_rate_435AC8

tabla_AC8.at['435.gromacs-111B', 'Misses lectura'] = total_read_misses_435AC8

tabla_AC8.at['435.gromacs-111B',
             'Miss rate lectura [%]'] = total_read_miss_rate_435AC8

tabla_AC8.at['435.gromacs-111B',
             'Misses escritura'] = total_write_misses_435AC8

tabla_AC8.at['435.gromacs-111B',
             'Miss rate escritura [%]'] = total_write_miss_rate_435AC8
# **436.cactusADM-1804B**

tabla_AC8.at['436.cactusADM-1804B', 'Total Misses'] = total_misses_436AC8

tabla_AC8.at['436.cactusADM-1804B',
             'Miss rate total [%]'] = total_miss_rate_436AC8

tabla_AC8.at['436.cactusADM-1804B',
             'Misses lectura'] = total_read_misses_436AC8

tabla_AC8.at['436.cactusADM-1804B',
             'Miss rate lectura [%]'] = total_read_miss_rate_436AC8

tabla_AC8.at['436.cactusADM-1804B',
             'Misses escritura'] = total_write_misses_436AC8

tabla_AC8.at['436.cactusADM-1804B',
             'Miss rate escritura [%]'] = total_write_miss_rate_436AC8

# **437.leslie3d-134B**

tabla_AC8.at['437.leslie3d-134B', 'Total Misses'] = total_misses_437AC8

tabla_AC8.at['437.leslie3d-134B',
             'Miss rate total [%]'] = total_miss_rate_437AC8

tabla_AC8.at['437.leslie3d-134B',
             'Misses lectura'] = total_read_misses_437AC8

tabla_AC8.at['437.leslie3d-134B',
             'Miss rate lectura [%]'] = total_read_miss_rate_437AC8

tabla_AC8.at['437.leslie3d-134B',
             'Misses escritura'] = total_write_misses_437AC8

tabla_AC8.at['437.leslie3d-134B',
             'Miss rate escritura [%]'] = total_write_miss_rate_437AC8

# **444.namd-120B**

tabla_AC8.at['444.namd-120B', 'Total Misses'] = total_misses_444AC8

tabla_AC8.at['444.namd-120B', 'Miss rate total [%]'] = total_miss_rate_444AC8

tabla_AC8.at['444.namd-120B', 'Misses lectura'] = total_read_misses_444AC8

tabla_AC8.at['444.namd-120B',
             'Miss rate lectura [%]'] = total_read_miss_rate_444AC8

tabla_AC8.at['444.namd-120B',
             'Misses escritura'] = total_write_misses_444AC8

tabla_AC8.at['444.namd-120B',
             'Miss rate escritura [%]'] = total_write_miss_rate_444AC8

# **445.gobmk-17B**

tabla_AC8.at['445.gobmk-17B', 'Total Misses'] = total_misses_445AC8

tabla_AC8.at['445.gobmk-17B', 'Miss rate total [%]'] = total_miss_rate_445AC8

tabla_AC8.at['445.gobmk-17B', 'Misses lectura'] = total_read_misses_445AC8

tabla_AC8.at['445.gobmk-17B',
             'Miss rate lectura [%]'] = total_read_miss_rate_445AC8

tabla_AC8.at['445.gobmk-17B',
             'Misses escritura'] = total_write_misses_445AC8

tabla_AC8.at['445.gobmk-17B',
             'Miss rate escritura [%]'] = total_write_miss_rate_445AC8

# **450.soplex-247B**

tabla_AC8.at['450.soplex-247B', 'Total Misses'] = total_misses_450AC8

tabla_AC8.at['450.soplex-247B',
             'Miss rate total [%]'] = total_miss_rate_450AC8

tabla_AC8.at['450.soplex-247B', 'Misses lectura'] = total_read_misses_450AC8

tabla_AC8.at['450.soplex-247B',
             'Miss rate lectura [%]'] = total_read_miss_rate_450AC8

tabla_AC8.at['450.soplex-247B',
             'Misses escritura'] = total_write_misses_450AC8

tabla_AC8.at['450.soplex-247B',
             'Miss rate escritura [%]'] = total_write_miss_rate_450AC8

# **453.povray-887B**

tabla_AC8.at['453.povray-887B', 'Total Misses'] = total_misses_453AC8

tabla_AC8.at['453.povray-887B',
             'Miss rate total [%]'] = total_miss_rate_453AC8

tabla_AC8.at['453.povray-887B', 'Misses lectura'] = total_read_misses_453AC8

tabla_AC8.at['453.povray-887B',
             'Miss rate lectura [%]'] = total_read_miss_rate_453AC8

tabla_AC8.at['453.povray-887B',
             'Misses escritura'] = total_write_misses_453AC8

tabla_AC8.at['453.povray-887B',
             'Miss rate escritura [%]'] = total_write_miss_rate_453AC8

# **454.calculix-104B**

tabla_AC8.at['454.calculix-104B', 'Total Misses'] = total_misses_454AC8

tabla_AC8.at['454.calculix-104B',
             'Miss rate total [%]'] = total_miss_rate_454AC8

tabla_AC8.at['454.calculix-104B',
             'Misses lectura'] = total_read_misses_454AC8

tabla_AC8.at['454.calculix-104B',
             'Miss rate lectura [%]'] = total_read_miss_rate_454AC8

tabla_AC8.at['454.calculix-104B',
             'Misses escritura'] = total_write_misses_454AC8

tabla_AC8.at['454.calculix-104B',
             'Miss rate escritura [%]'] = total_write_miss_rate_454AC8

# **456.hmmer-191B**

tabla_AC8.at['456.hmmer-191B', 'Total Misses'] = total_misses_456AC8

tabla_AC8.at['456.hmmer-191B',
             'Miss rate total [%]'] = total_miss_rate_456AC8

tabla_AC8.at['456.hmmer-191B', 'Misses lectura'] = total_read_misses_456AC8

tabla_AC8.at['456.hmmer-191B',
             'Miss rate lectura [%]'] = total_read_miss_rate_456AC8

tabla_AC8.at['456.hmmer-191B',
             'Misses escritura'] = total_write_misses_456AC8

tabla_AC8.at['456.hmmer-191B',
             'Miss rate escritura [%]'] = total_write_miss_rate_456AC8

# **458.sjeng-1088B**

tabla_AC8.at['458.sjeng-1088B', 'Total Misses'] = total_misses_458AC8

tabla_AC8.at['458.sjeng-1088B',
             'Miss rate total [%]'] = total_miss_rate_458AC8

tabla_AC8.at['458.sjeng-1088B', 'Misses lectura'] = total_read_misses_458AC8

tabla_AC8.at['458.sjeng-1088B',
             'Miss rate lectura [%]'] = total_read_miss_rate_458AC8

tabla_AC8.at['458.sjeng-1088B',
             'Misses escritura'] = total_write_misses_458AC8

tabla_AC8.at['458.sjeng-1088B',
             'Miss rate escritura [%]'] = total_write_miss_rate_458AC8

# **459.GemsFDTD-1169B**

tabla_AC8.at['459.GemsFDTD-1169B', 'Total Misses'] = total_misses_459AC8

tabla_AC8.at['459.GemsFDTD-1169B',
             'Miss rate total [%]'] = total_miss_rate_459AC8

tabla_AC8.at['459.GemsFDTD-1169B',
             'Misses lectura'] = total_read_misses_459AC8

tabla_AC8.at['459.GemsFDTD-1169B',
             'Miss rate lectura [%]'] = total_read_miss_rate_459AC8

tabla_AC8.at['459.GemsFDTD-1169B',
             'Misses escritura'] = total_write_misses_459AC8

tabla_AC8.at['459.GemsFDTD-1169B',
             'Miss rate escritura [%]'] = total_write_miss_rate_459AC8

# **462.libquantum-1343B**

tabla_AC8.at['462.libquantum-1343B', 'Total Misses'] = total_misses_462AC8

tabla_AC8.at['462.libquantum-1343B',
             'Miss rate total [%]'] = total_miss_rate_462AC8

tabla_AC8.at['462.libquantum-1343B',
             'Misses lectura'] = total_read_misses_462AC8

tabla_AC8.at['462.libquantum-1343B',
             'Miss rate lectura [%]'] = total_read_miss_rate_462AC8

tabla_AC8.at['462.libquantum-1343B',
             'Misses escritura'] = total_write_misses_462AC8

tabla_AC8.at['462.libquantum-1343B',
             'Miss rate escritura [%]'] = total_write_miss_rate_462AC8

# **464.h264ref-30B**

tabla_AC8.at['464.h264ref-30B', 'Total Misses'] = total_misses_464AC8

tabla_AC8.at['464.h264ref-30B',
             'Miss rate total [%]'] = total_miss_rate_464AC8

tabla_AC8.at['464.h264ref-30B', 'Misses lectura'] = total_read_misses_464AC8

tabla_AC8.at['464.h264ref-30B',
             'Miss rate lectura [%]'] = total_read_miss_rate_464AC8

tabla_AC8.at['464.h264ref-30B',
             'Misses escritura'] = total_write_misses_464AC8

tabla_AC8.at['464.h264ref-30B',
             'Miss rate escritura [%]'] = total_write_miss_rate_464AC8

# **465.tonto-1769B**

tabla_AC8.at['465.tonto-1769B', 'Total Misses'] = total_misses_465AC8

tabla_AC8.at['465.tonto-1769B',
             'Miss rate total [%]'] = total_miss_rate_465AC8

tabla_AC8.at['465.tonto-1769B', 'Misses lectura'] = total_read_misses_465AC8

tabla_AC8.at['465.tonto-1769B',
             'Miss rate lectura [%]'] = total_read_miss_rate_465AC8

tabla_AC8.at['465.tonto-1769B',
             'Misses escritura'] = total_write_misses_465AC8
tabla_AC8.at['465.tonto-1769B',
             'Miss rate escritura [%]'] = total_write_miss_rate_465AC8

# **470.lbm-1274B**

tabla_AC8.at['470.lbm-1274B', 'Total Misses'] = total_misses_470AC8

tabla_AC8.at['470.lbm-1274B', 'Miss rate total [%]'] = total_miss_rate_470AC8

tabla_AC8.at['470.lbm-1274B', 'Misses lectura'] = total_read_misses_470AC8

tabla_AC8.at['470.lbm-1274B',
             'Miss rate lectura [%]'] = total_read_miss_rate_470AC8

tabla_AC8.at['470.lbm-1274B',
             'Misses escritura'] = total_write_misses_470AC8

tabla_AC8.at['470.lbm-1274B',
             'Miss rate escritura [%]'] = total_write_miss_rate_470AC8

# **471.omnetpp-188B**

tabla_AC8.at['471.omnetpp-188B', 'Total Misses'] = total_misses_471AC8

tabla_AC8.at['471.omnetpp-188B',
             'Miss rate total [%]'] = total_miss_rate_471AC8

tabla_AC8.at['471.omnetpp-188B', 'Misses lectura'] = total_read_misses_471AC8

tabla_AC8.at['471.omnetpp-188B',
             'Miss rate lectura [%]'] = total_read_miss_rate_471AC8

tabla_AC8.at['471.omnetpp-188B',
             'Misses escritura'] = total_write_misses_471AC8

tabla_AC8.at['471.omnetpp-188B',
             'Miss rate escritura [%]'] = total_write_miss_rate_471AC8

# **473.astar-153B**

tabla_AC8.at['473.astar-153B', 'Total Misses'] = total_misses_473AC8

tabla_AC8.at['473.astar-153B',
             'Miss rate total [%]'] = total_miss_rate_473AC8

tabla_AC8.at['473.astar-153B', 'Misses lectura'] = total_read_misses_473AC8

tabla_AC8.at['473.astar-153B',
             'Miss rate lectura [%]'] = total_read_miss_rate_473AC8

tabla_AC8.at['473.astar-153B',
             'Misses escritura'] = total_write_misses_473AC8

tabla_AC8.at['473.astar-153B',
             'Miss rate escritura [%]'] = total_write_miss_rate_473AC8

# **481.wrf-1170B**

tabla_AC8.at['481.wrf-1170B', 'Total Misses'] = total_misses_481AC8

tabla_AC8.at['481.wrf-1170B', 'Miss rate total [%]'] = total_miss_rate_481AC8

tabla_AC8.at['481.wrf-1170B', 'Misses lectura'] = total_read_misses_481AC8

tabla_AC8.at['481.wrf-1170B',
             'Miss rate lectura [%]'] = total_read_miss_rate_481AC8

tabla_AC8.at['481.wrf-1170B',
             'Misses escritura'] = total_write_misses_481AC8

tabla_AC8.at['481.wrf-1170B',
             'Miss rate escritura [%]'] = total_write_miss_rate_481AC8

# **482.sphinx3-1100B**

tabla_AC8.at['482.sphinx3-1100B', 'Total Misses'] = total_misses_482AC8

tabla_AC8.at['482.sphinx3-1100B',
             'Miss rate total [%]'] = total_miss_rate_482AC8

tabla_AC8.at['482.sphinx3-1100B',
             'Misses lectura'] = total_read_misses_482AC8

tabla_AC8.at['482.sphinx3-1100B',
             'Miss rate lectura [%]'] = total_read_miss_rate_482AC8

tabla_AC8.at['482.sphinx3-1100B',
             'Misses escritura'] = total_write_misses_482AC8

tabla_AC8.at['482.sphinx3-1100B',
             'Miss rate escritura [%]'] = total_write_miss_rate_482AC8

# **483.xalancbmk-127B**

tabla_AC8.at['483.xalancbmk-127B', 'Total Misses'] = total_misses_483AC8

tabla_AC8.at['483.xalancbmk-127B',
             'Miss rate total [%]'] = total_miss_rate_483AC8

tabla_AC8.at['483.xalancbmk-127B',
             'Misses lectura'] = total_read_misses_483AC8

tabla_AC8.at['483.xalancbmk-127B',
             'Miss rate lectura [%]'] = total_read_miss_rate_483AC8

tabla_AC8.at['483.xalancbmk-127B',
             'Misses escritura'] = total_write_misses_483AC8

tabla_AC8.at['483.xalancbmk-127B',
             'Miss rate escritura [%]'] = total_write_miss_rate_483AC8

print(">>>>>All AC8 data has been uploaded successfully")

################################################################
# Extractor para experimento con asociatividad de caché: 16-way#
################################################################

# Creación de tablas para adjuntar valores
# Una tabla por tamaño
tabla_AC16 = pd.DataFrame(index=[
    '400.perlbench-41B', '401.bzip2-226B', '403.gcc-16B', '410.bwaves-1963B', '416.gamess-875B', '429.mcf-184B', '433.milc-127B',
    '435.gromacs-111B', '436.cactusADM-1804B', '437.leslie3d-134B', '444.namd-120B', '445.gobmk-17B',
    '450.soplex-247B', '453.povray-887B', '454.calculix-104B', '456.hmmer-191B', '458.sjeng-1088B', '459.GemsFDTD-1169B',
    '462.libquantum-1343B', '464.h264ref-30B', '465.tonto-1769B', '470.lbm-1274B', '471.omnetpp-188B', '473.astar-153B', '481.wrf-1170B',
    '482.sphinx3-1100B', '483.xalancbmk-127B'], columns=[
    'App', 'Total Misses', 'Miss rate total [%]', 'Misses lectura', 'Miss rate lectura [%]', 'Misses escritura', 'Miss rate escritura [%]'])
tabla_AC16['App'] = tabla_AC16.index

# Files paths
filename_109 = "RESULTS_AC/400AC16.txt"
filename_110 = "RESULTS_AC/401AC16.txt"
filename_111 = "RESULTS_AC/403AC16.txt"
filename_112 = "RESULTS_AC/410AC16.txt"
filename_113 = "RESULTS_AC/416AC16.txt"
filename_114 = "RESULTS_AC/429AC16.txt"
filename_115 = "RESULTS_AC/433AC16.txt"
filename_116 = "RESULTS_AC/435AC16.txt"
filename_117 = "RESULTS_AC/436AC16.txt"
filename_118 = "RESULTS_AC/437AC16.txt"
filename_119 = "RESULTS_AC/444AC16.txt"
filename_120 = "RESULTS_AC/445AC16.txt"
filename_121 = "RESULTS_AC/450AC16.txt"
filename_122 = "RESULTS_AC/453AC16.txt"
filename_123 = "RESULTS_AC/454AC16.txt"
filename_124 = "RESULTS_AC/456AC16.txt"
filename_125 = "RESULTS_AC/458AC16.txt"
filename_126 = "RESULTS_AC/459AC16.txt"
filename_127 = "RESULTS_AC/462AC16.txt"
filename_128 = "RESULTS_AC/464AC16.txt"
filename_129 = "RESULTS_AC/465AC16.txt"
filename_130 = "RESULTS_AC/470AC16.txt"
filename_131 = "RESULTS_AC/471AC16.txt"
filename_132 = "RESULTS_AC/473AC16.txt"
filename_133 = "RESULTS_AC/481AC16.txt"
filename_134 = "RESULTS_AC/482AC16.txt"
filename_135 = "RESULTS_AC/483AC16.txt"

# Content file extracter
with open(filename_109, 'r') as file:
    content_400AC16 = file.read()
with open(filename_110, 'r') as file:
    content_401AC16 = file.read()
with open(filename_111, 'r') as file:
    content_403AC16 = file.read()
with open(filename_112, 'r') as file:
    content_410AC16 = file.read()
with open(filename_113, 'r') as file:
    content_416AC16 = file.read()
with open(filename_114, 'r') as file:
    content_429AC16 = file.read()
with open(filename_115, 'r') as file:
    content_433AC16 = file.read()
with open(filename_116, 'r') as file:
    content_435AC16 = file.read()
with open(filename_117, 'r') as file:
    content_436AC16 = file.read()
with open(filename_118, 'r') as file:
    content_437AC16 = file.read()
with open(filename_119, 'r') as file:
    content_444AC16 = file.read()
with open(filename_120, 'r') as file:
    content_445AC16 = file.read()
with open(filename_121, 'r') as file:
    content_450AC16 = file.read()
with open(filename_122, 'r') as file:
    content_453AC16 = file.read()
with open(filename_123, 'r') as file:
    content_454AC16 = file.read()
with open(filename_124, 'r') as file:
    content_456AC16 = file.read()
with open(filename_125, 'r') as file:
    content_458AC16 = file.read()
with open(filename_126, 'r') as file:
    content_459AC16 = file.read()
with open(filename_127, 'r') as file:
    content_462AC16 = file.read()
with open(filename_128, 'r') as file:
    content_464AC16 = file.read()
with open(filename_129, 'r') as file:
    content_465AC16 = file.read()
with open(filename_130, 'r') as file:
    content_470AC16 = file.read()
with open(filename_131, 'r') as file:
    content_471AC16 = file.read()
with open(filename_132, 'r') as file:
    content_473AC16 = file.read()
with open(filename_133, 'r') as file:
    content_481AC16 = file.read()
with open(filename_134, 'r') as file:
    content_482AC16 = file.read()
with open(filename_135, 'r') as file:
    content_483AC16 = file.read()

# Variables según aplicación

# 400.pearlbench-41B
total_misses_400AC16 = re.search(
    r"Total_misses (\d+)", content_400AC16).group(1)
total_miss_rate_400AC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_400AC16).group(1)
total_read_misses_400AC16 = re.search(
    r"Total_read_misses (\d+)", content_400AC16).group(1)
total_read_miss_rate_400AC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_400AC16).group(1)
total_write_misses_400AC16 = re.search(
    r"Total_write_misses (\d+)", content_400AC16).group(1)
total_write_miss_rate_400AC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_400AC16).group(1)
print(">>>>>All AC16 400.pearlbench-41B variables where obtained successfully")

# 401.bzip2-226B
total_misses_401AC16 = re.search(
    r"Total_misses (\d+)", content_401AC16).group(1)
total_miss_rate_401AC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_401AC16).group(1)
total_read_misses_401AC16 = re.search(
    r"Total_read_misses (\d+)", content_401AC16).group(1)
total_read_miss_rate_401AC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_401AC16).group(1)
total_write_misses_401AC16 = re.search(
    r"Total_write_misses (\d+)", content_401AC16).group(1)
total_write_miss_rate_401AC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_401AC16).group(1)
print(">>>>>All AC16 401.bzip2-226B variables where obtained successfully")

# 403.gcc-16B
total_misses_403AC16 = re.search(
    r"Total_misses (\d+)", content_403AC16).group(1)
total_miss_rate_403AC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_403AC16).group(1)
total_read_misses_403AC16 = re.search(
    r"Total_read_misses (\d+)", content_403AC16).group(1)
total_read_miss_rate_403AC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_403AC16).group(1)
total_write_misses_403AC16 = re.search(
    r"Total_write_misses (\d+)", content_403AC16).group(1)
total_write_miss_rate_403AC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_403AC16).group(1)
print(">>>>>All AC16 403.gcc-16B variables where obtained successfully")

# 410.bwaves-1963B
total_misses_410AC16 = re.search(
    r"Total_misses (\d+)", content_410AC16).group(1)
total_miss_rate_410AC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_410AC16).group(1)
total_read_misses_410AC16 = re.search(
    r"Total_read_misses (\d+)", content_410AC16).group(1)
total_read_miss_rate_410AC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_410AC16).group(1)
total_write_misses_410AC16 = re.search(
    r"Total_write_misses (\d+)", content_410AC16).group(1)
total_write_miss_rate_410AC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_410AC16).group(1)
print(">>>>>All AC16 410.bwaves-1963B variables where obtained successfully")

# 416.gamess-875B
total_misses_416AC16 = re.search(
    r"Total_misses (\d+)", content_416AC16).group(1)
total_miss_rate_416AC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_416AC16).group(1)
total_read_misses_416AC16 = re.search(
    r"Total_read_misses (\d+)", content_416AC16).group(1)
total_read_miss_rate_416AC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_416AC16).group(1)
total_write_misses_416AC16 = re.search(
    r"Total_write_misses (\d+)", content_416AC16).group(1)
total_write_miss_rate_416AC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_416AC16).group(1)
print(">>>>>All AC16 416.gamess-875B variables where obtained successfully")

# 429.mcf-184B
total_misses_429AC16 = re.search(
    r"Total_misses (\d+)", content_429AC16).group(1)
total_miss_rate_429AC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_429AC16).group(1)
total_read_misses_429AC16 = re.search(
    r"Total_read_misses (\d+)", content_429AC16).group(1)
total_read_miss_rate_429AC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_429AC16).group(1)
total_write_misses_429AC16 = re.search(
    r"Total_write_misses (\d+)", content_429AC16).group(1)
total_write_miss_rate_429AC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_429AC16).group(1)
print(">>>>>All AC16 429.mcf-184B variables where obtained successfully")

# 433.milc-127B
total_misses_433AC16 = re.search(
    r"Total_misses (\d+)", content_433AC16).group(1)
total_miss_rate_433AC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_433AC16).group(1)
total_read_misses_433AC16 = re.search(
    r"Total_read_misses (\d+)", content_433AC16).group(1)
total_read_miss_rate_433AC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_433AC16).group(1)
total_write_misses_433AC16 = re.search(
    r"Total_write_misses (\d+)", content_433AC16).group(1)
total_write_miss_rate_433AC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_433AC16).group(1)
print(">>>>>All AC16 433.milc-127B variables where obtained successfully")

# 435.gromacs-111B
total_misses_435AC16 = re.search(
    r"Total_misses (\d+)", content_435AC16).group(1)
total_miss_rate_435AC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_435AC16).group(1)
total_read_misses_435AC16 = re.search(
    r"Total_read_misses (\d+)", content_435AC16).group(1)
total_read_miss_rate_435AC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_435AC16).group(1)
total_write_misses_435AC16 = re.search(
    r"Total_write_misses (\d+)", content_435AC16).group(1)
total_write_miss_rate_435AC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_435AC16).group(1)
print(">>>>>All AC16 435.gromacs-111B variables where obtained successfully")

# 436.cactusADM-1804B
total_misses_436AC16 = re.search(
    r"Total_misses (\d+)", content_436AC16).group(1)
total_miss_rate_436AC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_436AC16).group(1)
total_read_misses_436AC16 = re.search(
    r"Total_read_misses (\d+)", content_436AC16).group(1)
total_read_miss_rate_436AC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_436AC16).group(1)
total_write_misses_436AC16 = re.search(
    r"Total_write_misses (\d+)", content_436AC16).group(1)
total_write_miss_rate_436AC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_436AC16).group(1)
print(">>>>>All AC16 436.cactusADM-1804B variables where obtained successfully")

# 437.leslie3d-134B
total_misses_437AC16 = re.search(
    r"Total_misses (\d+)", content_437AC16).group(1)
total_miss_rate_437AC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_437AC16).group(1)
total_read_misses_437AC16 = re.search(
    r"Total_read_misses (\d+)", content_437AC16).group(1)
total_read_miss_rate_437AC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_437AC16).group(1)
total_write_misses_437AC16 = re.search(
    r"Total_write_misses (\d+)", content_437AC16).group(1)
total_write_miss_rate_437AC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_437AC16).group(1)
print(">>>>>All AC16 437.leslie3d-134B variables where obtained successfully")

# 444.namd-120B
total_misses_444AC16 = re.search(
    r"Total_misses (\d+)", content_444AC16).group(1)
total_miss_rate_444AC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_444AC16).group(1)
total_read_misses_444AC16 = re.search(
    r"Total_read_misses (\d+)", content_444AC16).group(1)
total_read_miss_rate_444AC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_444AC16).group(1)
total_write_misses_444AC16 = re.search(
    r"Total_write_misses (\d+)", content_444AC16).group(1)
total_write_miss_rate_444AC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_444AC16).group(1)
print(">>>>>All AC16 444.namd-120B variables where obtained successfully")

# 445.gobmk-17B
total_misses_445AC16 = re.search(
    r"Total_misses (\d+)", content_445AC16).group(1)
total_miss_rate_445AC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_445AC16).group(1)
total_read_misses_445AC16 = re.search(
    r"Total_read_misses (\d+)", content_445AC16).group(1)
total_read_miss_rate_445AC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_445AC16).group(1)
total_write_misses_445AC16 = re.search(
    r"Total_write_misses (\d+)", content_445AC16).group(1)
total_write_miss_rate_445AC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_445AC16).group(1)
print(">>>>>All AC16 445.gobmk-17B variables where obtained successfully")

# 450.soplex-247B
total_misses_450AC16 = re.search(
    r"Total_misses (\d+)", content_450AC16).group(1)
total_miss_rate_450AC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_450AC16).group(1)
total_read_misses_450AC16 = re.search(
    r"Total_read_misses (\d+)", content_450AC16).group(1)
total_read_miss_rate_450AC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_450AC16).group(1)
total_write_misses_450AC16 = re.search(
    r"Total_write_misses (\d+)", content_450AC16).group(1)
total_write_miss_rate_450AC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_450AC16).group(1)
print(">>>>>All AC16 450.soplex-247B variables where obtained successfully")

# 453.povray-887B
total_misses_453AC16 = re.search(
    r"Total_misses (\d+)", content_453AC16).group(1)
total_miss_rate_453AC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_453AC16).group(1)
total_read_misses_453AC16 = re.search(
    r"Total_read_misses (\d+)", content_453AC16).group(1)
total_read_miss_rate_453AC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_453AC16).group(1)
total_write_misses_453AC16 = re.search(
    r"Total_write_misses (\d+)", content_453AC16).group(1)
total_write_miss_rate_453AC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_453AC16).group(1)
print(">>>>>All AC16 453.povray-887B variables where obtained successfully")

# 454.calculix-104B
total_misses_454AC16 = re.search(
    r"Total_misses (\d+)", content_454AC16).group(1)
total_miss_rate_454AC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_454AC16).group(1)
total_read_misses_454AC16 = re.search(
    r"Total_read_misses (\d+)", content_454AC16).group(1)
total_read_miss_rate_454AC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_454AC16).group(1)
total_write_misses_454AC16 = re.search(
    r"Total_write_misses (\d+)", content_454AC16).group(1)
total_write_miss_rate_454AC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_454AC16).group(1)
print(">>>>>All AC16 454.calculix-104B variables where obtained successfully")

# 456.hmmer-191B
total_misses_456AC16 = re.search(
    r"Total_misses (\d+)", content_456AC16).group(1)
total_miss_rate_456AC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_456AC16).group(1)
total_read_misses_456AC16 = re.search(
    r"Total_read_misses (\d+)", content_456AC16).group(1)
total_read_miss_rate_456AC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_456AC16).group(1)
total_write_misses_456AC16 = re.search(
    r"Total_write_misses (\d+)", content_456AC16).group(1)
total_write_miss_rate_456AC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_456AC16).group(1)
print(">>>>>All AC16 456.hmmer-191B variables where obtained successfully")

# 458.sjeng-1088B
total_misses_458AC16 = re.search(
    r"Total_misses (\d+)", content_458AC16).group(1)
total_miss_rate_458AC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_458AC16).group(1)
total_read_misses_458AC16 = re.search(
    r"Total_read_misses (\d+)", content_458AC16).group(1)
total_read_miss_rate_458AC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_458AC16).group(1)
total_write_misses_458AC16 = re.search(
    r"Total_write_misses (\d+)", content_458AC16).group(1)
total_write_miss_rate_458AC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_458AC16).group(1)
print(">>>>>All AC16 458.sjeng-1088B variables where obtained successfully")

# 459.GemsFDTD-1169B
total_misses_459AC16 = re.search(
    r"Total_misses (\d+)", content_459AC16).group(1)
total_miss_rate_459AC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_459AC16).group(1)
total_read_misses_459AC16 = re.search(
    r"Total_read_misses (\d+)", content_459AC16).group(1)
total_read_miss_rate_459AC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_459AC16).group(1)
total_write_misses_459AC16 = re.search(
    r"Total_write_misses (\d+)", content_459AC16).group(1)
total_write_miss_rate_459AC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_459AC16).group(1)
print(">>>>>All AC16 459.GemsFDTD-1169B variables where obtained successfully")

# 462.libquantum-1343B
total_misses_462AC16 = re.search(
    r"Total_misses (\d+)", content_462AC16).group(1)
total_miss_rate_462AC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_462AC16).group(1)
total_read_misses_462AC16 = re.search(
    r"Total_read_misses (\d+)", content_462AC16).group(1)
total_read_miss_rate_462AC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_462AC16).group(1)
total_write_misses_462AC16 = re.search(
    r"Total_write_misses (\d+)", content_462AC16).group(1)
total_write_miss_rate_462AC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_462AC16).group(1)
print(">>>>>All AC16 462.libquantum-1343B variables where obtained successfully")

# 464.h264ref-30B
total_misses_464AC16 = re.search(
    r"Total_misses (\d+)", content_464AC16).group(1)
total_miss_rate_464AC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_464AC16).group(1)
total_read_misses_464AC16 = re.search(
    r"Total_read_misses (\d+)", content_464AC16).group(1)
total_read_miss_rate_464AC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_464AC16).group(1)
total_write_misses_464AC16 = re.search(
    r"Total_write_misses (\d+)", content_464AC16).group(1)
total_write_miss_rate_464AC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_464AC16).group(1)
print(">>>>>All AC16 464.h264ref-30B variables where obtained successfully")

# 465.tonto-1769B
total_misses_465AC16 = re.search(
    r"Total_misses (\d+)", content_465AC16).group(1)
total_miss_rate_465AC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_465AC16).group(1)
total_read_misses_465AC16 = re.search(
    r"Total_read_misses (\d+)", content_465AC16).group(1)
total_read_miss_rate_465AC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_465AC16).group(1)
total_write_misses_465AC16 = re.search(
    r"Total_write_misses (\d+)", content_465AC16).group(1)
total_write_miss_rate_465AC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_465AC16).group(1)
print(">>>>>All AC16 465.tonto-1769B variables where obtained successfully")

# 470.lbm-1274B
total_misses_470AC16 = re.search(
    r"Total_misses (\d+)", content_470AC16).group(1)
total_miss_rate_470AC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_470AC16).group(1)
total_read_misses_470AC16 = re.search(
    r"Total_read_misses (\d+)", content_470AC16).group(1)
total_read_miss_rate_470AC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_470AC16).group(1)
total_write_misses_470AC16 = re.search(
    r"Total_write_misses (\d+)", content_470AC16).group(1)
total_write_miss_rate_470AC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_470AC16).group(1)
print(">>>>>All AC16 470.lbm-1274B variables where obtained successfully")

# 471.omnetpp-188B
total_misses_471AC16 = re.search(
    r"Total_misses (\d+)", content_471AC16).group(1)
total_miss_rate_471AC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_471AC16).group(1)
total_read_misses_471AC16 = re.search(
    r"Total_read_misses (\d+)", content_471AC16).group(1)
total_read_miss_rate_471AC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_471AC16).group(1)
total_write_misses_471AC16 = re.search(
    r"Total_write_misses (\d+)", content_471AC16).group(1)
total_write_miss_rate_471AC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_471AC16).group(1)
print(">>>>>All AC16 471.omnetpp-188B variables where obtained successfully")

# 473.astar-153B
total_misses_473AC16 = re.search(
    r"Total_misses (\d+)", content_473AC16).group(1)
total_miss_rate_473AC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_473AC16).group(1)
total_read_misses_473AC16 = re.search(
    r"Total_read_misses (\d+)", content_473AC16).group(1)
total_read_miss_rate_473AC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_473AC16).group(1)
total_write_misses_473AC16 = re.search(
    r"Total_write_misses (\d+)", content_473AC16).group(1)
total_write_miss_rate_473AC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_473AC16).group(1)
print(">>>>>All AC16 473.astar-153B variables where obtained successfully")

# 481.wrf-1170B
total_misses_481AC16 = re.search(
    r"Total_misses (\d+)", content_481AC16).group(1)
total_miss_rate_481AC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_481AC16).group(1)
total_read_misses_481AC16 = re.search(
    r"Total_read_misses (\d+)", content_481AC16).group(1)
total_read_miss_rate_481AC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_481AC16).group(1)
total_write_misses_481AC16 = re.search(
    r"Total_write_misses (\d+)", content_481AC16).group(1)
total_write_miss_rate_481AC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_481AC16).group(1)
print(">>>>>All AC16 481.wrf-1170B variables where obtained successfully")

# 482.sphinx3-1100B
total_misses_482AC16 = re.search(
    r"Total_misses (\d+)", content_482AC16).group(1)
total_miss_rate_482AC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_482AC16).group(1)
total_read_misses_482AC16 = re.search(
    r"Total_read_misses (\d+)", content_482AC16).group(1)
total_read_miss_rate_482AC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_482AC16).group(1)
total_write_misses_482AC16 = re.search(
    r"Total_write_misses (\d+)", content_482AC16).group(1)
total_write_miss_rate_482AC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_482AC16).group(1)
print(">>>>>All AC16 482.sphinx3-1100B variables where obtained successfully")

# 483.xalancbmk-127B
total_misses_483AC16 = re.search(
    r"Total_misses (\d+)", content_483AC16).group(1)
total_miss_rate_483AC16 = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_483AC16).group(1)
total_read_misses_483AC16 = re.search(
    r"Total_read_misses (\d+)", content_483AC16).group(1)
total_read_miss_rate_483AC16 = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_483AC16).group(1)
total_write_misses_483AC16 = re.search(
    r"Total_write_misses (\d+)", content_483AC16).group(1)
total_write_miss_rate_483AC16 = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_483AC16).group(1)
print(">>>>>All AC16 483.xalancbmk-127B variables where obtained successfully")

#############################
# Adjunta datos a dataframe #
#############################

# **400.perlbench-41B**

tabla_AC16.at['400.perlbench-41B', 'Total Misses'] = total_misses_400AC16

tabla_AC16.at['400.perlbench-41B',
              'Miss rate total [%]'] = total_miss_rate_400AC16

tabla_AC16.at['400.perlbench-41B',
              'Misses lectura'] = total_read_misses_400AC16

tabla_AC16.at['400.perlbench-41B',
              'Miss rate lectura [%]'] = total_read_miss_rate_400AC16

tabla_AC16.at['400.perlbench-41B',
              'Misses escritura'] = total_write_misses_400AC16

tabla_AC16.at['400.perlbench-41B',
              'Miss rate escritura [%]'] = total_write_miss_rate_400AC16

# **401.bzip2-226B**

tabla_AC16.at['401.bzip2-226B', 'Total Misses'] = total_misses_401AC16

tabla_AC16.at['401.bzip2-226B',
              'Miss rate total [%]'] = total_miss_rate_401AC16

tabla_AC16.at['401.bzip2-226B', 'Misses lectura'] = total_read_misses_401AC16

tabla_AC16.at['401.bzip2-226B',
              'Miss rate lectura [%]'] = total_read_miss_rate_401AC16

tabla_AC16.at['401.bzip2-226B',
              'Misses escritura'] = total_write_misses_401AC16

tabla_AC16.at['401.bzip2-226B',
              'Miss rate escritura [%]'] = total_write_miss_rate_401AC16

# **403.gcc-16B**

tabla_AC16.at['403.gcc-16B', 'Total Misses'] = total_misses_403AC16

tabla_AC16.at['403.gcc-16B', 'Miss rate total [%]'] = total_miss_rate_403AC16

tabla_AC16.at['403.gcc-16B', 'Misses lectura'] = total_read_misses_403AC16

tabla_AC16.at['403.gcc-16B',
              'Miss rate lectura [%]'] = total_read_miss_rate_403AC16

tabla_AC16.at['403.gcc-16B',
              'Misses escritura'] = total_write_misses_403AC16

tabla_AC16.at['403.gcc-16B',
              'Miss rate escritura [%]'] = total_write_miss_rate_403AC16

# **410.bwaves-1963B**

tabla_AC16.at['410.bwaves-1963B', 'Total Misses'] = total_misses_410AC16

tabla_AC16.at['410.bwaves-1963B',
              'Miss rate total [%]'] = total_miss_rate_410AC16

tabla_AC16.at['410.bwaves-1963B',
              'Misses lectura'] = total_read_misses_410AC16

tabla_AC16.at['410.bwaves-1963B',
              'Miss rate lectura [%]'] = total_read_miss_rate_410AC16

tabla_AC16.at['410.bwaves-1963B',
              'Misses escritura'] = total_write_misses_410AC16

tabla_AC16.at['410.bwaves-1963B',
              'Miss rate escritura [%]'] = total_write_miss_rate_410AC16

# **416.gamess-875B**

tabla_AC16.at['416.gamess-875B', 'Total Misses'] = total_misses_416AC16

tabla_AC16.at['416.gamess-875B',
              'Miss rate total [%]'] = total_miss_rate_416AC16

tabla_AC16.at['416.gamess-875B',
              'Misses lectura'] = total_read_misses_416AC16

tabla_AC16.at['416.gamess-875B',
              'Miss rate lectura [%]'] = total_read_miss_rate_416AC16

tabla_AC16.at['416.gamess-875B',
              'Misses escritura'] = total_write_misses_416AC16

tabla_AC16.at['416.gamess-875B',
              'Miss rate escritura [%]'] = total_write_miss_rate_416AC16

# **429.mcf-184B**

tabla_AC16.at['429.mcf-184B', 'Total Misses'] = total_misses_429AC16

tabla_AC16.at['429.mcf-184B',
              'Miss rate total [%]'] = total_miss_rate_429AC16

tabla_AC16.at['429.mcf-184B', 'Misses lectura'] = total_read_misses_429AC16

tabla_AC16.at['429.mcf-184B',
              'Miss rate lectura [%]'] = total_read_miss_rate_429AC16

tabla_AC16.at['429.mcf-184B',
              'Misses escritura'] = total_write_misses_429AC16

tabla_AC16.at['429.mcf-184B',
              'Miss rate escritura [%]'] = total_write_miss_rate_429AC16

# **433.milc-127B**

tabla_AC16.at['433.milc-127B', 'Total Misses'] = total_misses_433AC16

tabla_AC16.at['433.milc-127B',
              'Miss rate total [%]'] = total_miss_rate_433AC16

tabla_AC16.at['433.milc-127B', 'Misses lectura'] = total_read_misses_433AC16

tabla_AC16.at['433.milc-127B',
              'Miss rate lectura [%]'] = total_read_miss_rate_433AC16

tabla_AC16.at['433.milc-127B',
              'Misses escritura'] = total_write_misses_433AC16

tabla_AC16.at['433.milc-127B',
              'Miss rate escritura [%]'] = total_write_miss_rate_433AC16

# **435.gromacs-111B**

tabla_AC16.at['435.gromacs-111B', 'Total Misses'] = total_misses_435AC16

tabla_AC16.at['435.gromacs-111B',
              'Miss rate total [%]'] = total_miss_rate_435AC16

tabla_AC16.at['435.gromacs-111B',
              'Misses lectura'] = total_read_misses_435AC16

tabla_AC16.at['435.gromacs-111B',
              'Miss rate lectura [%]'] = total_read_miss_rate_435AC16

tabla_AC16.at['435.gromacs-111B',
              'Misses escritura'] = total_write_misses_435AC16

tabla_AC16.at['435.gromacs-111B',
              'Miss rate escritura [%]'] = total_write_miss_rate_435AC16
# **436.cactusADM-1804B**

tabla_AC16.at['436.cactusADM-1804B', 'Total Misses'] = total_misses_436AC16

tabla_AC16.at['436.cactusADM-1804B',
              'Miss rate total [%]'] = total_miss_rate_436AC16

tabla_AC16.at['436.cactusADM-1804B',
              'Misses lectura'] = total_read_misses_436AC16

tabla_AC16.at['436.cactusADM-1804B',
              'Miss rate lectura [%]'] = total_read_miss_rate_436AC16

tabla_AC16.at['436.cactusADM-1804B',
              'Misses escritura'] = total_write_misses_436AC16

tabla_AC16.at['436.cactusADM-1804B',
              'Miss rate escritura [%]'] = total_write_miss_rate_436AC16

# **437.leslie3d-134B**

tabla_AC16.at['437.leslie3d-134B', 'Total Misses'] = total_misses_437AC16

tabla_AC16.at['437.leslie3d-134B',
              'Miss rate total [%]'] = total_miss_rate_437AC16

tabla_AC16.at['437.leslie3d-134B',
              'Misses lectura'] = total_read_misses_437AC16

tabla_AC16.at['437.leslie3d-134B',
              'Miss rate lectura [%]'] = total_read_miss_rate_437AC16

tabla_AC16.at['437.leslie3d-134B',
              'Misses escritura'] = total_write_misses_437AC16

tabla_AC16.at['437.leslie3d-134B',
              'Miss rate escritura [%]'] = total_write_miss_rate_437AC16

# **444.namd-120B**

tabla_AC16.at['444.namd-120B', 'Total Misses'] = total_misses_444AC16

tabla_AC16.at['444.namd-120B',
              'Miss rate total [%]'] = total_miss_rate_444AC16

tabla_AC16.at['444.namd-120B', 'Misses lectura'] = total_read_misses_444AC16

tabla_AC16.at['444.namd-120B',
              'Miss rate lectura [%]'] = total_read_miss_rate_444AC16

tabla_AC16.at['444.namd-120B',
              'Misses escritura'] = total_write_misses_444AC16

tabla_AC16.at['444.namd-120B',
              'Miss rate escritura [%]'] = total_write_miss_rate_444AC16

# **445.gobmk-17B**

tabla_AC16.at['445.gobmk-17B', 'Total Misses'] = total_misses_445AC16

tabla_AC16.at['445.gobmk-17B',
              'Miss rate total [%]'] = total_miss_rate_445AC16

tabla_AC16.at['445.gobmk-17B', 'Misses lectura'] = total_read_misses_445AC16

tabla_AC16.at['445.gobmk-17B',
              'Miss rate lectura [%]'] = total_read_miss_rate_445AC16

tabla_AC16.at['445.gobmk-17B',
              'Misses escritura'] = total_write_misses_445AC16

tabla_AC16.at['445.gobmk-17B',
              'Miss rate escritura [%]'] = total_write_miss_rate_445AC16

# **450.soplex-247B**

tabla_AC16.at['450.soplex-247B', 'Total Misses'] = total_misses_450AC16

tabla_AC16.at['450.soplex-247B',
              'Miss rate total [%]'] = total_miss_rate_450AC16

tabla_AC16.at['450.soplex-247B',
              'Misses lectura'] = total_read_misses_450AC16

tabla_AC16.at['450.soplex-247B',
              'Miss rate lectura [%]'] = total_read_miss_rate_450AC16

tabla_AC16.at['450.soplex-247B',
              'Misses escritura'] = total_write_misses_450AC16

tabla_AC16.at['450.soplex-247B',
              'Miss rate escritura [%]'] = total_write_miss_rate_450AC16

# **453.povray-887B**

tabla_AC16.at['453.povray-887B', 'Total Misses'] = total_misses_453AC16

tabla_AC16.at['453.povray-887B',
              'Miss rate total [%]'] = total_miss_rate_453AC16

tabla_AC16.at['453.povray-887B',
              'Misses lectura'] = total_read_misses_453AC16

tabla_AC16.at['453.povray-887B',
              'Miss rate lectura [%]'] = total_read_miss_rate_453AC16

tabla_AC16.at['453.povray-887B',
              'Misses escritura'] = total_write_misses_453AC16

tabla_AC16.at['453.povray-887B',
              'Miss rate escritura [%]'] = total_write_miss_rate_453AC16

# **454.calculix-104B**

tabla_AC16.at['454.calculix-104B', 'Total Misses'] = total_misses_454AC16

tabla_AC16.at['454.calculix-104B',
              'Miss rate total [%]'] = total_miss_rate_454AC16

tabla_AC16.at['454.calculix-104B',
              'Misses lectura'] = total_read_misses_454AC16

tabla_AC16.at['454.calculix-104B',
              'Miss rate lectura [%]'] = total_read_miss_rate_454AC16

tabla_AC16.at['454.calculix-104B',
              'Misses escritura'] = total_write_misses_454AC16

tabla_AC16.at['454.calculix-104B',
              'Miss rate escritura [%]'] = total_write_miss_rate_454AC16

# **456.hmmer-191B**

tabla_AC16.at['456.hmmer-191B', 'Total Misses'] = total_misses_456AC16

tabla_AC16.at['456.hmmer-191B',
              'Miss rate total [%]'] = total_miss_rate_456AC16

tabla_AC16.at['456.hmmer-191B', 'Misses lectura'] = total_read_misses_456AC16

tabla_AC16.at['456.hmmer-191B',
              'Miss rate lectura [%]'] = total_read_miss_rate_456AC16

tabla_AC16.at['456.hmmer-191B',
              'Misses escritura'] = total_write_misses_456AC16

tabla_AC16.at['456.hmmer-191B',
              'Miss rate escritura [%]'] = total_write_miss_rate_456AC16

# **458.sjeng-1088B**

tabla_AC16.at['458.sjeng-1088B', 'Total Misses'] = total_misses_458AC16

tabla_AC16.at['458.sjeng-1088B',
              'Miss rate total [%]'] = total_miss_rate_458AC16

tabla_AC16.at['458.sjeng-1088B',
              'Misses lectura'] = total_read_misses_458AC16

tabla_AC16.at['458.sjeng-1088B',
              'Miss rate lectura [%]'] = total_read_miss_rate_458AC16

tabla_AC16.at['458.sjeng-1088B',
              'Misses escritura'] = total_write_misses_458AC16

tabla_AC16.at['458.sjeng-1088B',
              'Miss rate escritura [%]'] = total_write_miss_rate_458AC16

# **459.GemsFDTD-1169B**

tabla_AC16.at['459.GemsFDTD-1169B', 'Total Misses'] = total_misses_459AC16

tabla_AC16.at['459.GemsFDTD-1169B',
              'Miss rate total [%]'] = total_miss_rate_459AC16

tabla_AC16.at['459.GemsFDTD-1169B',
              'Misses lectura'] = total_read_misses_459AC16

tabla_AC16.at['459.GemsFDTD-1169B',
              'Miss rate lectura [%]'] = total_read_miss_rate_459AC16

tabla_AC16.at['459.GemsFDTD-1169B',
              'Misses escritura'] = total_write_misses_459AC16

tabla_AC16.at['459.GemsFDTD-1169B',
              'Miss rate escritura [%]'] = total_write_miss_rate_459AC16

# **462.libquantum-1343B**

tabla_AC16.at['462.libquantum-1343B', 'Total Misses'] = total_misses_462AC16

tabla_AC16.at['462.libquantum-1343B',
              'Miss rate total [%]'] = total_miss_rate_462AC16

tabla_AC16.at['462.libquantum-1343B',
              'Misses lectura'] = total_read_misses_462AC16

tabla_AC16.at['462.libquantum-1343B',
              'Miss rate lectura [%]'] = total_read_miss_rate_462AC16

tabla_AC16.at['462.libquantum-1343B',
              'Misses escritura'] = total_write_misses_462AC16

tabla_AC16.at['462.libquantum-1343B',
              'Miss rate escritura [%]'] = total_write_miss_rate_462AC16

# **464.h264ref-30B**

tabla_AC16.at['464.h264ref-30B', 'Total Misses'] = total_misses_464AC16

tabla_AC16.at['464.h264ref-30B',
              'Miss rate total [%]'] = total_miss_rate_464AC16

tabla_AC16.at['464.h264ref-30B',
              'Misses lectura'] = total_read_misses_464AC16

tabla_AC16.at['464.h264ref-30B',
              'Miss rate lectura [%]'] = total_read_miss_rate_464AC16

tabla_AC16.at['464.h264ref-30B',
              'Misses escritura'] = total_write_misses_464AC16

tabla_AC16.at['464.h264ref-30B',
              'Miss rate escritura [%]'] = total_write_miss_rate_464AC16

# **465.tonto-1769B**

tabla_AC16.at['465.tonto-1769B', 'Total Misses'] = total_misses_465AC16

tabla_AC16.at['465.tonto-1769B',
              'Miss rate total [%]'] = total_miss_rate_465AC16

tabla_AC16.at['465.tonto-1769B',
              'Misses lectura'] = total_read_misses_465AC16

tabla_AC16.at['465.tonto-1769B',
              'Miss rate lectura [%]'] = total_read_miss_rate_465AC16

tabla_AC16.at['465.tonto-1769B',
              'Misses escritura'] = total_write_misses_465AC16
tabla_AC16.at['465.tonto-1769B',
              'Miss rate escritura [%]'] = total_write_miss_rate_465AC16

# **470.lbm-1274B**

tabla_AC16.at['470.lbm-1274B', 'Total Misses'] = total_misses_470AC16

tabla_AC16.at['470.lbm-1274B',
              'Miss rate total [%]'] = total_miss_rate_470AC16

tabla_AC16.at['470.lbm-1274B', 'Misses lectura'] = total_read_misses_470AC16

tabla_AC16.at['470.lbm-1274B',
              'Miss rate lectura [%]'] = total_read_miss_rate_470AC16

tabla_AC16.at['470.lbm-1274B',
              'Misses escritura'] = total_write_misses_470AC16

tabla_AC16.at['470.lbm-1274B',
              'Miss rate escritura [%]'] = total_write_miss_rate_470AC16

# **471.omnetpp-188B**

tabla_AC16.at['471.omnetpp-188B', 'Total Misses'] = total_misses_471AC16

tabla_AC16.at['471.omnetpp-188B',
              'Miss rate total [%]'] = total_miss_rate_471AC16

tabla_AC16.at['471.omnetpp-188B',
              'Misses lectura'] = total_read_misses_471AC16

tabla_AC16.at['471.omnetpp-188B',
              'Miss rate lectura [%]'] = total_read_miss_rate_471AC16

tabla_AC16.at['471.omnetpp-188B',
              'Misses escritura'] = total_write_misses_471AC16

tabla_AC16.at['471.omnetpp-188B',
              'Miss rate escritura [%]'] = total_write_miss_rate_471AC16

# **473.astar-153B**

tabla_AC16.at['473.astar-153B', 'Total Misses'] = total_misses_473AC16

tabla_AC16.at['473.astar-153B',
              'Miss rate total [%]'] = total_miss_rate_473AC16

tabla_AC16.at['473.astar-153B', 'Misses lectura'] = total_read_misses_473AC16

tabla_AC16.at['473.astar-153B',
              'Miss rate lectura [%]'] = total_read_miss_rate_473AC16

tabla_AC16.at['473.astar-153B',
              'Misses escritura'] = total_write_misses_473AC16

tabla_AC16.at['473.astar-153B',
              'Miss rate escritura [%]'] = total_write_miss_rate_473AC16

# **481.wrf-1170B**

tabla_AC16.at['481.wrf-1170B', 'Total Misses'] = total_misses_481AC16

tabla_AC16.at['481.wrf-1170B',
              'Miss rate total [%]'] = total_miss_rate_481AC16

tabla_AC16.at['481.wrf-1170B', 'Misses lectura'] = total_read_misses_481AC16

tabla_AC16.at['481.wrf-1170B',
              'Miss rate lectura [%]'] = total_read_miss_rate_481AC16

tabla_AC16.at['481.wrf-1170B',
              'Misses escritura'] = total_write_misses_481AC16

tabla_AC16.at['481.wrf-1170B',
              'Miss rate escritura [%]'] = total_write_miss_rate_481AC16

# **482.sphinx3-1100B**

tabla_AC16.at['482.sphinx3-1100B', 'Total Misses'] = total_misses_482AC16

tabla_AC16.at['482.sphinx3-1100B',
              'Miss rate total [%]'] = total_miss_rate_482AC16

tabla_AC16.at['482.sphinx3-1100B',
              'Misses lectura'] = total_read_misses_482AC16

tabla_AC16.at['482.sphinx3-1100B',
              'Miss rate lectura [%]'] = total_read_miss_rate_482AC16

tabla_AC16.at['482.sphinx3-1100B',
              'Misses escritura'] = total_write_misses_482AC16

tabla_AC16.at['482.sphinx3-1100B',
              'Miss rate escritura [%]'] = total_write_miss_rate_482AC16

# **483.xalancbmk-127B**

tabla_AC16.at['483.xalancbmk-127B', 'Total Misses'] = total_misses_483AC16

tabla_AC16.at['483.xalancbmk-127B',
              'Miss rate total [%]'] = total_miss_rate_483AC16

tabla_AC16.at['483.xalancbmk-127B',
              'Misses lectura'] = total_read_misses_483AC16

tabla_AC16.at['483.xalancbmk-127B',
              'Miss rate lectura [%]'] = total_read_miss_rate_483AC16

tabla_AC16.at['483.xalancbmk-127B',
              'Misses escritura'] = total_write_misses_483AC16

tabla_AC16.at['483.xalancbmk-127B',
              'Miss rate escritura [%]'] = total_write_miss_rate_483AC16

print(">>>>>All AC16 data has been uploaded successfully")


###########
# GEO MEAN#
###########

# GEO MEAN Miss rate total AC1
columna_AC1 = tabla_AC1['Miss rate total [%]']
columna_AC1_numpy = columna_AC1.to_numpy(dtype=np.float64)
GEOMEAN_Miss_rate_total_AC1 = gmean(columna_AC1_numpy)

# GEO MEAN Miss rate total AC2
columna_AC2 = tabla_AC2['Miss rate total [%]']
columna_AC2_numpy = columna_AC2.to_numpy(dtype=np.float64)
GEOMEAN_Miss_rate_total_AC2 = gmean(columna_AC2_numpy)

# GEO MEAN Miss rate total AC4
columna_AC4 = tabla_AC4['Miss rate total [%]']
columna_AC4_numpy = columna_AC4.to_numpy(dtype=np.float64)
GEOMEAN_Miss_rate_total_AC4 = gmean(columna_AC4_numpy)

# GEO MEAN Miss rate total AC8
columna_AC8 = tabla_AC8['Miss rate total [%]']
columna_AC8_numpy = columna_AC8.to_numpy(dtype=np.float64)
GEOMEAN_Miss_rate_total_AC8 = gmean(columna_AC8_numpy)

# GEO MEAN Miss rate total AC16
columna_AC16 = tabla_AC16['Miss rate total [%]']
columna_AC16_numpy = columna_AC16.to_numpy(dtype=np.float64)
GEOMEAN_Miss_rate_total_AC16 = gmean(columna_AC16_numpy)


#############################################################################
# Dataframes de resultados: miss rate total, miss rate total 465.tonto-1769B#
#############################################################################

# Creación de tablas para adjuntar valores

# Miss rate
tabla_miss_rate_total = pd.DataFrame(index=[
    'Miss rate total [%]'], columns=[
    'Parámetro', 'Mapeo directo', '2-way', '4-way', '8-way', '16-way'])
tabla_miss_rate_total['Parámetro'] = tabla_miss_rate_total.index


# Miss rate 470_LBM_1274B
tabla_miss_rate_total_470_lbm_1274B = pd.DataFrame(index=[
    'Miss rate total 470_lbm_1274B [%]'], columns=[
    'Parámetro', 'Mapeo directo', '2-way', '4-way', '8-way', '16-way'])
tabla_miss_rate_total_470_lbm_1274B['Parámetro'] = tabla_miss_rate_total_470_lbm_1274B.index

##############################
# Adjunta datos en dataframes#
##############################

# Miss rate total
tabla_miss_rate_total.at['Miss rate total [%]',
                         'Mapeo directo'] = GEOMEAN_Miss_rate_total_AC1
tabla_miss_rate_total.at['Miss rate total [%]',
                         '2-way'] = GEOMEAN_Miss_rate_total_AC2
tabla_miss_rate_total.at['Miss rate total [%]',
                         '4-way'] = GEOMEAN_Miss_rate_total_AC4
tabla_miss_rate_total.at['Miss rate total [%]',
                         '8-way'] = GEOMEAN_Miss_rate_total_AC8
tabla_miss_rate_total.at['Miss rate total [%]',
                         '16-way'] = GEOMEAN_Miss_rate_total_AC16

# Miss rate total 465.tonto_1769B
tabla_miss_rate_total_470_lbm_1274B.at['Miss rate total 470_lbm_1274B [%]',
                                       'Mapeo directo'] = total_miss_rate_470AC1
tabla_miss_rate_total_470_lbm_1274B.at['Miss rate total 470_lbm_1274B [%]',
                                       '2-way'] = total_miss_rate_470AC2
tabla_miss_rate_total_470_lbm_1274B.at['Miss rate total 470_lbm_1274B [%]',
                                       '4-way'] = total_miss_rate_470AC4
tabla_miss_rate_total_470_lbm_1274B.at['Miss rate total 470_lbm_1274B [%]',
                                       '8-way'] = total_miss_rate_470AC8
tabla_miss_rate_total_470_lbm_1274B.at['Miss rate total 470_lbm_1274B [%]',
                                       '16-way'] = total_miss_rate_470AC16

############################################
# Archivo de salida para facilitar gráficos#
############################################

# Create an Excel writer using pandas
output = pd.ExcelWriter('Results_AC.xlsx')

# Write each dataframe to a different sheet in the Excel file
tabla_AC1.to_excel(output, sheet_name='AC1', index=False)
tabla_AC2.to_excel(output, sheet_name='AC2', index=False)
tabla_AC4.to_excel(output, sheet_name='AC4', index=False)
tabla_AC8.to_excel(output, sheet_name='AC8', index=False)
tabla_AC16.to_excel(output, sheet_name='AC16', index=False)
tabla_miss_rate_total.to_excel(
    output, sheet_name='Miss rate total promedio', index=False)
tabla_miss_rate_total_470_lbm_1274B.to_excel(
    output, sheet_name='Miss rate total promedio 470_lbm_1274B', index=False)

# Save the Excel file
output.save()

print("'''''''''''''''''''''''''''''''''''''''''' Asociatividad de caché mapeo directo''''''''''''''''''''''''''''''''''''''''''''''''")
print(tabla_AC1.to_string(index=False))
print("################################################################################################")
print("El miss rate promedio [%] con una asociatividad de caché mapeo directo es: ",
      GEOMEAN_Miss_rate_total_AC1, ' #')
print("################################################################################################")
print("")
print("'''''''''''''''''''''''''''''''''''''''''''' Asociatividad de caché 2-way''''''''''''''''''''''''''''''''''''''''''''''''''''")
print(tabla_AC2.to_string(index=False))
print("###########################################################################################")
print("El miss rate promedio [%] con una asociatividad de caché de 2-way es: ",
      GEOMEAN_Miss_rate_total_AC2, ' #')
print("###########################################################################################")
print("")
print("'''''''''''''''''''''''''''''''''''''''''''''' Asociatividad de caché 4-way''''''''''''''''''''''''''''''''''''''''''''''''''''")
print(tabla_AC4.to_string(index=False))
print("###########################################################################################")
print("El miss rate promedio [%] con una asociatividad de caché de 4-way es: ",
      GEOMEAN_Miss_rate_total_AC4, ' #')
print("###########################################################################################")
print("")
print("''''''''''''''''''''''''''''''''''''''''''''' Asociatividad de caché 8-way''''''''''''''''''''''''''''''''''''''''''''''''''''")
print(tabla_AC8.to_string(index=False))
print("############################################################################################")
print("El miss rate promedio [%] con una asociatividad de caché de 8-way es: ",
      GEOMEAN_Miss_rate_total_AC8, ' #')
print("############################################################################################")
print("")
print("'''''''''''''''''''''''''''''''''''''''''''' Asociatividad de caché 16-way''''''''''''''''''''''''''''''''''''''''''''''''")
print(tabla_AC16.to_string(index=False))
print("#############################################################################################")
print("El miss rate promedio [%] con una asociatividad de caché de 16-way es: ",
      GEOMEAN_Miss_rate_total_AC16, ' #')
print("#############################################################################################")
print("")
print("##################################################################################")
print("''''''''''''''''''''''''''' Miss rate total'''''''''''''''''''''''''''''")
print(tabla_miss_rate_total.to_string(index=False))
print("")
print("##################################################################################")
print("''''''''''''''''' Miss rate total 470.lbm-1274B'''''''''''''''''''''")
print(tabla_miss_rate_total_470_lbm_1274B.to_string(index=False))
