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


####################################################
# Extractor para experimento con replace policy LRU#
####################################################


# Creación de tablas para adjuntar valores
# Una tabla por tamaño
tabla_RCl = pd.DataFrame(index=[
    '400.perlbench-41B', '401.bzip2-226B', '403.gcc-16B', '410.bwaves-1963B', '416.gamess-875B', '429.mcf-184B', '433.milc-127B',
    '435.gromacs-111B', '436.cactusADM-1804B', '437.leslie3d-134B', '444.namd-120B', '445.gobmk-17B',
    '450.soplex-247B', '453.povray-887B', '454.calculix-104B', '456.hmmer-191B', '458.sjeng-1088B', '459.GemsFDTD-1169B',
    '462.libquantum-1343B', '464.h264ref-30B', '465.tonto-1769B', '470.lbm-1274B', '471.omnetpp-188B', '473.astar-153B', '481.wrf-1170B',
    '482.sphinx3-1100B', '483.xalancbmk-127B'], columns=[
    'App', 'Total Misses', 'Miss rate total [%]', 'Misses lectura', 'Miss rate lectura [%]', 'Misses escritura', 'Miss rate escritura [%]'])
tabla_RCl['App'] = tabla_RCl.index

# Files paths
filename_1 = "RESULTS_RC/400RCl.txt"
filename_2 = "RESULTS_RC/401RCl.txt"
filename_3 = "RESULTS_RC/403RCl.txt"
filename_4 = "RESULTS_RC/410RCl.txt"
filename_5 = "RESULTS_RC/416RCl.txt"
filename_6 = "RESULTS_RC/429RCl.txt"
filename_7 = "RESULTS_RC/433RCl.txt"
filename_8 = "RESULTS_RC/435RCl.txt"
filename_9 = "RESULTS_RC/436RCl.txt"
filename_10 = "RESULTS_RC/437RCl.txt"
filename_11 = "RESULTS_RC/444RCl.txt"
filename_12 = "RESULTS_RC/445RCl.txt"
filename_13 = "RESULTS_RC/450RCl.txt"
filename_14 = "RESULTS_RC/453RCl.txt"
filename_15 = "RESULTS_RC/454RCl.txt"
filename_16 = "RESULTS_RC/456RCl.txt"
filename_17 = "RESULTS_RC/458RCl.txt"
filename_18 = "RESULTS_RC/459RCl.txt"
filename_19 = "RESULTS_RC/462RCl.txt"
filename_20 = "RESULTS_RC/464RCl.txt"
filename_21 = "RESULTS_RC/465RCl.txt"
filename_22 = "RESULTS_RC/470RCl.txt"
filename_23 = "RESULTS_RC/471RCl.txt"
filename_24 = "RESULTS_RC/473RCl.txt"
filename_25 = "RESULTS_RC/481RCl.txt"
filename_26 = "RESULTS_RC/482RCl.txt"
filename_27 = "RESULTS_RC/483RCl.txt"


# Content file extracter
with open(filename_1, 'r') as file:
    content_400RCl = file.read()
with open(filename_2, 'r') as file:
    content_401RCl = file.read()
with open(filename_3, 'r') as file:
    content_403RCl = file.read()
with open(filename_4, 'r') as file:
    content_410RCl = file.read()
with open(filename_5, 'r') as file:
    content_416RCl = file.read()
with open(filename_6, 'r') as file:
    content_429RCl = file.read()
with open(filename_7, 'r') as file:
    content_433RCl = file.read()
with open(filename_8, 'r') as file:
    content_435RCl = file.read()
with open(filename_9, 'r') as file:
    content_436RCl = file.read()
with open(filename_10, 'r') as file:
    content_437RCl = file.read()
with open(filename_11, 'r') as file:
    content_444RCl = file.read()
with open(filename_12, 'r') as file:
    content_445RCl = file.read()
with open(filename_13, 'r') as file:
    content_450RCl = file.read()
with open(filename_14, 'r') as file:
    content_453RCl = file.read()
with open(filename_15, 'r') as file:
    content_454RCl = file.read()
with open(filename_16, 'r') as file:
    content_456RCl = file.read()
with open(filename_17, 'r') as file:
    content_458RCl = file.read()
with open(filename_18, 'r') as file:
    content_459RCl = file.read()
with open(filename_19, 'r') as file:
    content_462RCl = file.read()
with open(filename_20, 'r') as file:
    content_464RCl = file.read()
with open(filename_21, 'r') as file:
    content_465RCl = file.read()
with open(filename_22, 'r') as file:
    content_470RCl = file.read()
with open(filename_23, 'r') as file:
    content_471RCl = file.read()
with open(filename_24, 'r') as file:
    content_473RCl = file.read()
with open(filename_25, 'r') as file:
    content_481RCl = file.read()
with open(filename_26, 'r') as file:
    content_482RCl = file.read()
with open(filename_27, 'r') as file:
    content_483RCl = file.read()


# Variables según aplicación

# 400.pearlbench-41B
total_misses_400RCl = re.search(r"Total_misses (\d+)", content_400RCl).group(1)
total_miss_rate_400RCl = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_400RCl).group(1)
total_read_misses_400RCl = re.search(
    r"Total_read_misses (\d+)", content_400RCl).group(1)
total_read_miss_rate_400RCl = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_400RCl).group(1)
total_write_misses_400RCl = re.search(
    r"Total_write_misses (\d+)", content_400RCl).group(1)
total_write_miss_rate_400RCl = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_400RCl).group(1)
print(">>>>>All RCl 400.pearlbench-41B variables where obtained successfully")

# 401.bzip2-226B
total_misses_401RCl = re.search(r"Total_misses (\d+)", content_401RCl).group(1)
total_miss_rate_401RCl = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_401RCl).group(1)
total_read_misses_401RCl = re.search(
    r"Total_read_misses (\d+)", content_401RCl).group(1)
total_read_miss_rate_401RCl = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_401RCl).group(1)
total_write_misses_401RCl = re.search(
    r"Total_write_misses (\d+)", content_401RCl).group(1)
total_write_miss_rate_401RCl = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_401RCl).group(1)
print(">>>>>All RCl 401.bzip2-226B variables where obtained successfully")

# 403.gcc-16B
total_misses_403RCl = re.search(r"Total_misses (\d+)", content_403RCl).group(1)
total_miss_rate_403RCl = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_403RCl).group(1)
total_read_misses_403RCl = re.search(
    r"Total_read_misses (\d+)", content_403RCl).group(1)
total_read_miss_rate_403RCl = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_403RCl).group(1)
total_write_misses_403RCl = re.search(
    r"Total_write_misses (\d+)", content_403RCl).group(1)
total_write_miss_rate_403RCl = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_403RCl).group(1)
print(">>>>>All RCl 403.gcc-16B variables where obtained successfully")

# 410.bwaves-1963B
total_misses_410RCl = re.search(r"Total_misses (\d+)", content_410RCl).group(1)
total_miss_rate_410RCl = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_410RCl).group(1)
total_read_misses_410RCl = re.search(
    r"Total_read_misses (\d+)", content_410RCl).group(1)
total_read_miss_rate_410RCl = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_410RCl).group(1)
total_write_misses_410RCl = re.search(
    r"Total_write_misses (\d+)", content_410RCl).group(1)
total_write_miss_rate_410RCl = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_410RCl).group(1)
print(">>>>>All RCl 410.bwaves-1963B variables where obtained successfully")

# 416.gamess-875B
total_misses_416RCl = re.search(r"Total_misses (\d+)", content_416RCl).group(1)
total_miss_rate_416RCl = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_416RCl).group(1)
total_read_misses_416RCl = re.search(
    r"Total_read_misses (\d+)", content_416RCl).group(1)
total_read_miss_rate_416RCl = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_416RCl).group(1)
total_write_misses_416RCl = re.search(
    r"Total_write_misses (\d+)", content_416RCl).group(1)
total_write_miss_rate_416RCl = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_416RCl).group(1)
print(">>>>>All RCl 416.gamess-875B variables where obtained successfully")

# 429.mcf-184B
total_misses_429RCl = re.search(r"Total_misses (\d+)", content_429RCl).group(1)
total_miss_rate_429RCl = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_429RCl).group(1)
total_read_misses_429RCl = re.search(
    r"Total_read_misses (\d+)", content_429RCl).group(1)
total_read_miss_rate_429RCl = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_429RCl).group(1)
total_write_misses_429RCl = re.search(
    r"Total_write_misses (\d+)", content_429RCl).group(1)
total_write_miss_rate_429RCl = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_429RCl).group(1)
print(">>>>>All RCl 429.mcf-184B variables where obtained successfully")

# 433.milc-127B
total_misses_433RCl = re.search(r"Total_misses (\d+)", content_433RCl).group(1)
total_miss_rate_433RCl = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_433RCl).group(1)
total_read_misses_433RCl = re.search(
    r"Total_read_misses (\d+)", content_433RCl).group(1)
total_read_miss_rate_433RCl = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_433RCl).group(1)
total_write_misses_433RCl = re.search(
    r"Total_write_misses (\d+)", content_433RCl).group(1)
total_write_miss_rate_433RCl = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_433RCl).group(1)
print(">>>>>All RCl 433.milc-127B variables where obtained successfully")

# 435.gromacs-111B
total_misses_435RCl = re.search(r"Total_misses (\d+)", content_435RCl).group(1)
total_miss_rate_435RCl = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_435RCl).group(1)
total_read_misses_435RCl = re.search(
    r"Total_read_misses (\d+)", content_435RCl).group(1)
total_read_miss_rate_435RCl = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_435RCl).group(1)
total_write_misses_435RCl = re.search(
    r"Total_write_misses (\d+)", content_435RCl).group(1)
total_write_miss_rate_435RCl = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_435RCl).group(1)
print(">>>>>All RCl 435.gromacs-111B variables where obtained successfully")

# 436.cactusADM-1804B
total_misses_436RCl = re.search(r"Total_misses (\d+)", content_436RCl).group(1)
total_miss_rate_436RCl = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_436RCl).group(1)
total_read_misses_436RCl = re.search(
    r"Total_read_misses (\d+)", content_436RCl).group(1)
total_read_miss_rate_436RCl = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_436RCl).group(1)
total_write_misses_436RCl = re.search(
    r"Total_write_misses (\d+)", content_436RCl).group(1)
total_write_miss_rate_436RCl = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_436RCl).group(1)
print(">>>>>All RCl 436.cactusADM-1804B variables where obtained successfully")

# 437.leslie3d-134B
total_misses_437RCl = re.search(r"Total_misses (\d+)", content_437RCl).group(1)
total_miss_rate_437RCl = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_437RCl).group(1)
total_read_misses_437RCl = re.search(
    r"Total_read_misses (\d+)", content_437RCl).group(1)
total_read_miss_rate_437RCl = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_437RCl).group(1)
total_write_misses_437RCl = re.search(
    r"Total_write_misses (\d+)", content_437RCl).group(1)
total_write_miss_rate_437RCl = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_437RCl).group(1)
print(">>>>>All RCl 437.leslie3d-134B variables where obtained successfully")

# 444.namd-120B
total_misses_444RCl = re.search(r"Total_misses (\d+)", content_444RCl).group(1)
total_miss_rate_444RCl = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_444RCl).group(1)
total_read_misses_444RCl = re.search(
    r"Total_read_misses (\d+)", content_444RCl).group(1)
total_read_miss_rate_444RCl = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_444RCl).group(1)
total_write_misses_444RCl = re.search(
    r"Total_write_misses (\d+)", content_444RCl).group(1)
total_write_miss_rate_444RCl = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_444RCl).group(1)
print(">>>>>All RCl 444.namd-120B variables where obtained successfully")

# 445.gobmk-17B
total_misses_445RCl = re.search(r"Total_misses (\d+)", content_445RCl).group(1)
total_miss_rate_445RCl = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_445RCl).group(1)
total_read_misses_445RCl = re.search(
    r"Total_read_misses (\d+)", content_445RCl).group(1)
total_read_miss_rate_445RCl = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_445RCl).group(1)
total_write_misses_445RCl = re.search(
    r"Total_write_misses (\d+)", content_445RCl).group(1)
total_write_miss_rate_445RCl = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_445RCl).group(1)
print(">>>>>All RCl 445.gobmk-17B variables where obtained successfully")

# 450.soplex-247B
total_misses_450RCl = re.search(r"Total_misses (\d+)", content_450RCl).group(1)
total_miss_rate_450RCl = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_450RCl).group(1)
total_read_misses_450RCl = re.search(
    r"Total_read_misses (\d+)", content_450RCl).group(1)
total_read_miss_rate_450RCl = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_450RCl).group(1)
total_write_misses_450RCl = re.search(
    r"Total_write_misses (\d+)", content_450RCl).group(1)
total_write_miss_rate_450RCl = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_450RCl).group(1)
print(">>>>>All RCl 450.soplex-247B variables where obtained successfully")

# 453.povray-887B
total_misses_453RCl = re.search(r"Total_misses (\d+)", content_453RCl).group(1)
total_miss_rate_453RCl = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_453RCl).group(1)
total_read_misses_453RCl = re.search(
    r"Total_read_misses (\d+)", content_453RCl).group(1)
total_read_miss_rate_453RCl = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_453RCl).group(1)
total_write_misses_453RCl = re.search(
    r"Total_write_misses (\d+)", content_453RCl).group(1)
total_write_miss_rate_453RCl = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_453RCl).group(1)
print(">>>>>All RCl 453.povray-887B variables where obtained successfully")

# 454.calculix-104B
total_misses_454RCl = re.search(r"Total_misses (\d+)", content_454RCl).group(1)
total_miss_rate_454RCl = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_454RCl).group(1)
total_read_misses_454RCl = re.search(
    r"Total_read_misses (\d+)", content_454RCl).group(1)
total_read_miss_rate_454RCl = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_454RCl).group(1)
total_write_misses_454RCl = re.search(
    r"Total_write_misses (\d+)", content_454RCl).group(1)
total_write_miss_rate_454RCl = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_454RCl).group(1)
print(">>>>>All RCl 454.calculix-104B variables where obtained successfully")

# 456.hmmer-191B
total_misses_456RCl = re.search(r"Total_misses (\d+)", content_456RCl).group(1)
total_miss_rate_456RCl = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_456RCl).group(1)
total_read_misses_456RCl = re.search(
    r"Total_read_misses (\d+)", content_456RCl).group(1)
total_read_miss_rate_456RCl = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_456RCl).group(1)
total_write_misses_456RCl = re.search(
    r"Total_write_misses (\d+)", content_456RCl).group(1)
total_write_miss_rate_456RCl = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_456RCl).group(1)
print(">>>>>All RCl 456.hmmer-191B variables where obtained successfully")

# 458.sjeng-1088B
total_misses_458RCl = re.search(r"Total_misses (\d+)", content_458RCl).group(1)
total_miss_rate_458RCl = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_458RCl).group(1)
total_read_misses_458RCl = re.search(
    r"Total_read_misses (\d+)", content_458RCl).group(1)
total_read_miss_rate_458RCl = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_458RCl).group(1)
total_write_misses_458RCl = re.search(
    r"Total_write_misses (\d+)", content_458RCl).group(1)
total_write_miss_rate_458RCl = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_458RCl).group(1)
print(">>>>>All RCl 458.sjeng-1088B variables where obtained successfully")

# 459.GemsFDTD-1169B
total_misses_459RCl = re.search(r"Total_misses (\d+)", content_459RCl).group(1)
total_miss_rate_459RCl = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_459RCl).group(1)
total_read_misses_459RCl = re.search(
    r"Total_read_misses (\d+)", content_459RCl).group(1)
total_read_miss_rate_459RCl = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_459RCl).group(1)
total_write_misses_459RCl = re.search(
    r"Total_write_misses (\d+)", content_459RCl).group(1)
total_write_miss_rate_459RCl = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_459RCl).group(1)
print(">>>>>All RCl 459.GemsFDTD-1169B variables where obtained successfully")

# 462.libquantum-1343B
total_misses_462RCl = re.search(r"Total_misses (\d+)", content_462RCl).group(1)
total_miss_rate_462RCl = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_462RCl).group(1)
total_read_misses_462RCl = re.search(
    r"Total_read_misses (\d+)", content_462RCl).group(1)
total_read_miss_rate_462RCl = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_462RCl).group(1)
total_write_misses_462RCl = re.search(
    r"Total_write_misses (\d+)", content_462RCl).group(1)
total_write_miss_rate_462RCl = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_462RCl).group(1)
print(">>>>>All RCl 462.libquantum-1343B variables where obtained successfully")

# 464.h264ref-30B
total_misses_464RCl = re.search(r"Total_misses (\d+)", content_464RCl).group(1)
total_miss_rate_464RCl = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_464RCl).group(1)
total_read_misses_464RCl = re.search(
    r"Total_read_misses (\d+)", content_464RCl).group(1)
total_read_miss_rate_464RCl = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_464RCl).group(1)
total_write_misses_464RCl = re.search(
    r"Total_write_misses (\d+)", content_464RCl).group(1)
total_write_miss_rate_464RCl = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_464RCl).group(1)
print(">>>>>All RCl 464.h264ref-30B variables where obtained successfully")

# 465.tonto-1769B
total_misses_465RCl = re.search(r"Total_misses (\d+)", content_465RCl).group(1)
total_miss_rate_465RCl = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_465RCl).group(1)
total_read_misses_465RCl = re.search(
    r"Total_read_misses (\d+)", content_465RCl).group(1)
total_read_miss_rate_465RCl = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_465RCl).group(1)
total_write_misses_465RCl = re.search(
    r"Total_write_misses (\d+)", content_465RCl).group(1)
total_write_miss_rate_465RCl = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_465RCl).group(1)
print(">>>>>All RCl 465.tonto-1769B variables where obtained successfully")

# 470.lbm-1274B
total_misses_470RCl = re.search(r"Total_misses (\d+)", content_470RCl).group(1)
total_miss_rate_470RCl = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_470RCl).group(1)
total_read_misses_470RCl = re.search(
    r"Total_read_misses (\d+)", content_470RCl).group(1)
total_read_miss_rate_470RCl = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_470RCl).group(1)
total_write_misses_470RCl = re.search(
    r"Total_write_misses (\d+)", content_470RCl).group(1)
total_write_miss_rate_470RCl = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_470RCl).group(1)
print(">>>>>All RCl 470.lbm-1274B variables where obtained successfully")

# 471.omnetpp-188B
total_misses_471RCl = re.search(r"Total_misses (\d+)", content_471RCl).group(1)
total_miss_rate_471RCl = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_471RCl).group(1)
total_read_misses_471RCl = re.search(
    r"Total_read_misses (\d+)", content_471RCl).group(1)
total_read_miss_rate_471RCl = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_471RCl).group(1)
total_write_misses_471RCl = re.search(
    r"Total_write_misses (\d+)", content_471RCl).group(1)
total_write_miss_rate_471RCl = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_471RCl).group(1)
print(">>>>>All RCl 471.omnetpp-188B variables where obtained successfully")

# 473.astar-153B
total_misses_473RCl = re.search(r"Total_misses (\d+)", content_473RCl).group(1)
total_miss_rate_473RCl = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_473RCl).group(1)
total_read_misses_473RCl = re.search(
    r"Total_read_misses (\d+)", content_473RCl).group(1)
total_read_miss_rate_473RCl = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_473RCl).group(1)
total_write_misses_473RCl = re.search(
    r"Total_write_misses (\d+)", content_473RCl).group(1)
total_write_miss_rate_473RCl = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_473RCl).group(1)
print(">>>>>All RCl 473.astar-153B variables where obtained successfully")

# 481.wrf-1170B
total_misses_481RCl = re.search(r"Total_misses (\d+)", content_481RCl).group(1)
total_miss_rate_481RCl = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_481RCl).group(1)
total_read_misses_481RCl = re.search(
    r"Total_read_misses (\d+)", content_481RCl).group(1)
total_read_miss_rate_481RCl = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_481RCl).group(1)
total_write_misses_481RCl = re.search(
    r"Total_write_misses (\d+)", content_481RCl).group(1)
total_write_miss_rate_481RCl = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_481RCl).group(1)
print(">>>>>All RCl 481.wrf-1170B variables where obtained successfully")

# 482.sphinx3-1100B
total_misses_482RCl = re.search(r"Total_misses (\d+)", content_482RCl).group(1)
total_miss_rate_482RCl = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_482RCl).group(1)
total_read_misses_482RCl = re.search(
    r"Total_read_misses (\d+)", content_482RCl).group(1)
total_read_miss_rate_482RCl = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_482RCl).group(1)
total_write_misses_482RCl = re.search(
    r"Total_write_misses (\d+)", content_482RCl).group(1)
total_write_miss_rate_482RCl = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_482RCl).group(1)
print(">>>>>All RCl 482.sphinx3-1100B variables where obtained successfully")

# 483.xalancbmk-127B
total_misses_483RCl = re.search(r"Total_misses (\d+)", content_483RCl).group(1)
total_miss_rate_483RCl = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_483RCl).group(1)
total_read_misses_483RCl = re.search(
    r"Total_read_misses (\d+)", content_483RCl).group(1)
total_read_miss_rate_483RCl = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_483RCl).group(1)
total_write_misses_483RCl = re.search(
    r"Total_write_misses (\d+)", content_483RCl).group(1)
total_write_miss_rate_483RCl = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_483RCl).group(1)
print(">>>>>All RCl 483.xalancbmk-127B variables where obtained successfully")


#############################
# Adjunta datos a dataframe #
#############################

# **400.perlbench-41B**

tabla_RCl.at['400.perlbench-41B', 'Total Misses'] = total_misses_400RCl

tabla_RCl.at['400.perlbench-41B',
             'Miss rate total [%]'] = total_miss_rate_400RCl

tabla_RCl.at['400.perlbench-41B', 'Misses lectura'] = total_read_misses_400RCl

tabla_RCl.at['400.perlbench-41B',
             'Miss rate lectura [%]'] = total_read_miss_rate_400RCl

tabla_RCl.at['400.perlbench-41B',
             'Misses escritura'] = total_write_misses_400RCl

tabla_RCl.at['400.perlbench-41B',
             'Miss rate escritura [%]'] = total_write_miss_rate_400RCl

# **401.bzip2-226B**

tabla_RCl.at['401.bzip2-226B', 'Total Misses'] = total_misses_401RCl

tabla_RCl.at['401.bzip2-226B', 'Miss rate total [%]'] = total_miss_rate_401RCl

tabla_RCl.at['401.bzip2-226B', 'Misses lectura'] = total_read_misses_401RCl

tabla_RCl.at['401.bzip2-226B',
             'Miss rate lectura [%]'] = total_read_miss_rate_401RCl

tabla_RCl.at['401.bzip2-226B',
             'Misses escritura'] = total_write_misses_401RCl

tabla_RCl.at['401.bzip2-226B',
             'Miss rate escritura [%]'] = total_write_miss_rate_401RCl

# **403.gcc-16B**

tabla_RCl.at['403.gcc-16B', 'Total Misses'] = total_misses_403RCl

tabla_RCl.at['403.gcc-16B', 'Miss rate total [%]'] = total_miss_rate_403RCl

tabla_RCl.at['403.gcc-16B', 'Misses lectura'] = total_read_misses_403RCl

tabla_RCl.at['403.gcc-16B',
             'Miss rate lectura [%]'] = total_read_miss_rate_403RCl

tabla_RCl.at['403.gcc-16B',
             'Misses escritura'] = total_write_misses_403RCl

tabla_RCl.at['403.gcc-16B',
             'Miss rate escritura [%]'] = total_write_miss_rate_403RCl

# **410.bwaves-1963B**

tabla_RCl.at['410.bwaves-1963B', 'Total Misses'] = total_misses_410RCl

tabla_RCl.at['410.bwaves-1963B',
             'Miss rate total [%]'] = total_miss_rate_410RCl

tabla_RCl.at['410.bwaves-1963B', 'Misses lectura'] = total_read_misses_410RCl

tabla_RCl.at['410.bwaves-1963B',
             'Miss rate lectura [%]'] = total_read_miss_rate_410RCl

tabla_RCl.at['410.bwaves-1963B',
             'Misses escritura'] = total_write_misses_410RCl

tabla_RCl.at['410.bwaves-1963B',
             'Miss rate escritura [%]'] = total_write_miss_rate_410RCl

# **416.gamess-875B**

tabla_RCl.at['416.gamess-875B', 'Total Misses'] = total_misses_416RCl

tabla_RCl.at['416.gamess-875B', 'Miss rate total [%]'] = total_miss_rate_416RCl

tabla_RCl.at['416.gamess-875B', 'Misses lectura'] = total_read_misses_416RCl

tabla_RCl.at['416.gamess-875B',
             'Miss rate lectura [%]'] = total_read_miss_rate_416RCl

tabla_RCl.at['416.gamess-875B',
             'Misses escritura'] = total_write_misses_416RCl

tabla_RCl.at['416.gamess-875B',
             'Miss rate escritura [%]'] = total_write_miss_rate_416RCl

# **429.mcf-184B**

tabla_RCl.at['429.mcf-184B', 'Total Misses'] = total_misses_429RCl

tabla_RCl.at['429.mcf-184B', 'Miss rate total [%]'] = total_miss_rate_429RCl

tabla_RCl.at['429.mcf-184B', 'Misses lectura'] = total_read_misses_429RCl

tabla_RCl.at['429.mcf-184B',
             'Miss rate lectura [%]'] = total_read_miss_rate_429RCl

tabla_RCl.at['429.mcf-184B',
             'Misses escritura'] = total_write_misses_429RCl

tabla_RCl.at['429.mcf-184B',
             'Miss rate escritura [%]'] = total_write_miss_rate_429RCl

# **433.milc-127B**

tabla_RCl.at['433.milc-127B', 'Total Misses'] = total_misses_433RCl

tabla_RCl.at['433.milc-127B', 'Miss rate total [%]'] = total_miss_rate_433RCl

tabla_RCl.at['433.milc-127B', 'Misses lectura'] = total_read_misses_433RCl

tabla_RCl.at['433.milc-127B',
             'Miss rate lectura [%]'] = total_read_miss_rate_433RCl

tabla_RCl.at['433.milc-127B',
             'Misses escritura'] = total_write_misses_433RCl

tabla_RCl.at['433.milc-127B',
             'Miss rate escritura [%]'] = total_write_miss_rate_433RCl

# **435.gromacs-111B**

tabla_RCl.at['435.gromacs-111B', 'Total Misses'] = total_misses_435RCl

tabla_RCl.at['435.gromacs-111B',
             'Miss rate total [%]'] = total_miss_rate_435RCl

tabla_RCl.at['435.gromacs-111B', 'Misses lectura'] = total_read_misses_435RCl

tabla_RCl.at['435.gromacs-111B',
             'Miss rate lectura [%]'] = total_read_miss_rate_435RCl

tabla_RCl.at['435.gromacs-111B',
             'Misses escritura'] = total_write_misses_435RCl

tabla_RCl.at['435.gromacs-111B',
             'Miss rate escritura [%]'] = total_write_miss_rate_435RCl

# **436.cactusADM-1804B**

tabla_RCl.at['436.cactusADM-1804B', 'Total Misses'] = total_misses_436RCl

tabla_RCl.at['436.cactusADM-1804B',
             'Miss rate total [%]'] = total_miss_rate_436RCl

tabla_RCl.at['436.cactusADM-1804B',
             'Misses lectura'] = total_read_misses_436RCl

tabla_RCl.at['436.cactusADM-1804B',
             'Miss rate lectura [%]'] = total_read_miss_rate_436RCl

tabla_RCl.at['436.cactusADM-1804B',
             'Misses escritura'] = total_write_misses_436RCl

tabla_RCl.at['436.cactusADM-1804B',
             'Miss rate escritura [%]'] = total_write_miss_rate_436RCl

# **437.leslie3d-134B**

tabla_RCl.at['437.leslie3d-134B', 'Total Misses'] = total_misses_437RCl

tabla_RCl.at['437.leslie3d-134B',
             'Miss rate total [%]'] = total_miss_rate_437RCl

tabla_RCl.at['437.leslie3d-134B', 'Misses lectura'] = total_read_misses_437RCl

tabla_RCl.at['437.leslie3d-134B',
             'Miss rate lectura [%]'] = total_read_miss_rate_437RCl

tabla_RCl.at['437.leslie3d-134B',
             'Misses escritura'] = total_write_misses_437RCl

tabla_RCl.at['437.leslie3d-134B',
             'Miss rate escritura [%]'] = total_write_miss_rate_437RCl

# **444.namd-120B**

tabla_RCl.at['444.namd-120B', 'Total Misses'] = total_misses_444RCl

tabla_RCl.at['444.namd-120B', 'Miss rate total [%]'] = total_miss_rate_444RCl

tabla_RCl.at['444.namd-120B', 'Misses lectura'] = total_read_misses_444RCl

tabla_RCl.at['444.namd-120B',
             'Miss rate lectura [%]'] = total_read_miss_rate_444RCl

tabla_RCl.at['444.namd-120B',
             'Misses escritura'] = total_write_misses_444RCl

tabla_RCl.at['444.namd-120B',
             'Miss rate escritura [%]'] = total_write_miss_rate_444RCl

# **445.gobmk-17B**

tabla_RCl.at['445.gobmk-17B', 'Total Misses'] = total_misses_445RCl

tabla_RCl.at['445.gobmk-17B', 'Miss rate total [%]'] = total_miss_rate_445RCl

tabla_RCl.at['445.gobmk-17B', 'Misses lectura'] = total_read_misses_445RCl

tabla_RCl.at['445.gobmk-17B',
             'Miss rate lectura [%]'] = total_read_miss_rate_445RCl

tabla_RCl.at['445.gobmk-17B',
             'Misses escritura'] = total_write_misses_445RCl

tabla_RCl.at['445.gobmk-17B',
             'Miss rate escritura [%]'] = total_write_miss_rate_445RCl

# **450.soplex-247B**

tabla_RCl.at['450.soplex-247B', 'Total Misses'] = total_misses_450RCl

tabla_RCl.at['450.soplex-247B', 'Miss rate total [%]'] = total_miss_rate_450RCl

tabla_RCl.at['450.soplex-247B', 'Misses lectura'] = total_read_misses_450RCl

tabla_RCl.at['450.soplex-247B',
             'Miss rate lectura [%]'] = total_read_miss_rate_450RCl

tabla_RCl.at['450.soplex-247B',
             'Misses escritura'] = total_write_misses_450RCl

tabla_RCl.at['450.soplex-247B',
             'Miss rate escritura [%]'] = total_write_miss_rate_450RCl

# **453.povray-887B**

tabla_RCl.at['453.povray-887B', 'Total Misses'] = total_misses_453RCl

tabla_RCl.at['453.povray-887B', 'Miss rate total [%]'] = total_miss_rate_453RCl

tabla_RCl.at['453.povray-887B', 'Misses lectura'] = total_read_misses_453RCl

tabla_RCl.at['453.povray-887B',
             'Miss rate lectura [%]'] = total_read_miss_rate_453RCl

tabla_RCl.at['453.povray-887B',
             'Misses escritura'] = total_write_misses_453RCl

tabla_RCl.at['453.povray-887B',
             'Miss rate escritura [%]'] = total_write_miss_rate_453RCl

# **454.calculix-104B**

tabla_RCl.at['454.calculix-104B', 'Total Misses'] = total_misses_454RCl

tabla_RCl.at['454.calculix-104B',
             'Miss rate total [%]'] = total_miss_rate_454RCl

tabla_RCl.at['454.calculix-104B', 'Misses lectura'] = total_read_misses_454RCl

tabla_RCl.at['454.calculix-104B',
             'Miss rate lectura [%]'] = total_read_miss_rate_454RCl

tabla_RCl.at['454.calculix-104B',
             'Misses escritura'] = total_write_misses_454RCl

tabla_RCl.at['454.calculix-104B',
             'Miss rate escritura [%]'] = total_write_miss_rate_454RCl

# **456.hmmer-191B**

tabla_RCl.at['456.hmmer-191B', 'Total Misses'] = total_misses_456RCl

tabla_RCl.at['456.hmmer-191B', 'Miss rate total [%]'] = total_miss_rate_456RCl

tabla_RCl.at['456.hmmer-191B', 'Misses lectura'] = total_read_misses_456RCl

tabla_RCl.at['456.hmmer-191B',
             'Miss rate lectura [%]'] = total_read_miss_rate_456RCl

tabla_RCl.at['456.hmmer-191B',
             'Misses escritura'] = total_write_misses_456RCl

tabla_RCl.at['456.hmmer-191B',
             'Miss rate escritura [%]'] = total_write_miss_rate_456RCl

# **458.sjeng-1088B**

tabla_RCl.at['458.sjeng-1088B', 'Total Misses'] = total_misses_458RCl

tabla_RCl.at['458.sjeng-1088B', 'Miss rate total [%]'] = total_miss_rate_458RCl

tabla_RCl.at['458.sjeng-1088B', 'Misses lectura'] = total_read_misses_458RCl

tabla_RCl.at['458.sjeng-1088B',
             'Miss rate lectura [%]'] = total_read_miss_rate_458RCl

tabla_RCl.at['458.sjeng-1088B',
             'Misses escritura'] = total_write_misses_458RCl

tabla_RCl.at['458.sjeng-1088B',
             'Miss rate escritura [%]'] = total_write_miss_rate_458RCl

# **459.GemsFDTD-1169B**

tabla_RCl.at['459.GemsFDTD-1169B', 'Total Misses'] = total_misses_459RCl

tabla_RCl.at['459.GemsFDTD-1169B',
             'Miss rate total [%]'] = total_miss_rate_459RCl

tabla_RCl.at['459.GemsFDTD-1169B', 'Misses lectura'] = total_read_misses_459RCl

tabla_RCl.at['459.GemsFDTD-1169B',
             'Miss rate lectura [%]'] = total_read_miss_rate_459RCl

tabla_RCl.at['459.GemsFDTD-1169B',
             'Misses escritura'] = total_write_misses_459RCl

tabla_RCl.at['459.GemsFDTD-1169B',
             'Miss rate escritura [%]'] = total_write_miss_rate_459RCl

# **462.libquantum-1343B**

tabla_RCl.at['462.libquantum-1343B', 'Total Misses'] = total_misses_462RCl

tabla_RCl.at['462.libquantum-1343B',
             'Miss rate total [%]'] = total_miss_rate_462RCl

tabla_RCl.at['462.libquantum-1343B',
             'Misses lectura'] = total_read_misses_462RCl

tabla_RCl.at['462.libquantum-1343B',
             'Miss rate lectura [%]'] = total_read_miss_rate_462RCl

tabla_RCl.at['462.libquantum-1343B',
             'Misses escritura'] = total_write_misses_462RCl

tabla_RCl.at['462.libquantum-1343B',
             'Miss rate escritura [%]'] = total_write_miss_rate_462RCl

# **464.h264ref-30B**

tabla_RCl.at['464.h264ref-30B', 'Total Misses'] = total_misses_464RCl

tabla_RCl.at['464.h264ref-30B', 'Miss rate total [%]'] = total_miss_rate_464RCl

tabla_RCl.at['464.h264ref-30B', 'Misses lectura'] = total_read_misses_464RCl

tabla_RCl.at['464.h264ref-30B',
             'Miss rate lectura [%]'] = total_read_miss_rate_464RCl

tabla_RCl.at['464.h264ref-30B',
             'Misses escritura'] = total_write_misses_464RCl

tabla_RCl.at['464.h264ref-30B',
             'Miss rate escritura [%]'] = total_write_miss_rate_464RCl

# **465.tonto-1769B**

tabla_RCl.at['465.tonto-1769B', 'Total Misses'] = total_misses_465RCl

tabla_RCl.at['465.tonto-1769B', 'Miss rate total [%]'] = total_miss_rate_465RCl

tabla_RCl.at['465.tonto-1769B', 'Misses lectura'] = total_read_misses_465RCl

tabla_RCl.at['465.tonto-1769B',
             'Miss rate lectura [%]'] = total_read_miss_rate_465RCl

tabla_RCl.at['465.tonto-1769B',
             'Misses escritura'] = total_write_misses_465RCl

tabla_RCl.at['465.tonto-1769B',
             'Miss rate escritura [%]'] = total_write_miss_rate_465RCl

# **470.lbm-1274B**

tabla_RCl.at['470.lbm-1274B', 'Total Misses'] = total_misses_470RCl

tabla_RCl.at['470.lbm-1274B', 'Miss rate total [%]'] = total_miss_rate_470RCl

tabla_RCl.at['470.lbm-1274B', 'Misses lectura'] = total_read_misses_470RCl

tabla_RCl.at['470.lbm-1274B',
             'Miss rate lectura [%]'] = total_read_miss_rate_470RCl

tabla_RCl.at['470.lbm-1274B',
             'Misses escritura'] = total_write_misses_470RCl

tabla_RCl.at['470.lbm-1274B',
             'Miss rate escritura [%]'] = total_write_miss_rate_470RCl

# **471.omnetpp-188B**

tabla_RCl.at['471.omnetpp-188B', 'Total Misses'] = total_misses_471RCl

tabla_RCl.at['471.omnetpp-188B',
             'Miss rate total [%]'] = total_miss_rate_471RCl

tabla_RCl.at['471.omnetpp-188B', 'Misses lectura'] = total_read_misses_471RCl

tabla_RCl.at['471.omnetpp-188B',
             'Miss rate lectura [%]'] = total_read_miss_rate_471RCl

tabla_RCl.at['471.omnetpp-188B',
             'Misses escritura'] = total_write_misses_471RCl

tabla_RCl.at['471.omnetpp-188B',
             'Miss rate escritura [%]'] = total_write_miss_rate_471RCl

# **473.astar-153B**

tabla_RCl.at['473.astar-153B', 'Total Misses'] = total_misses_473RCl

tabla_RCl.at['473.astar-153B', 'Miss rate total [%]'] = total_miss_rate_473RCl

tabla_RCl.at['473.astar-153B', 'Misses lectura'] = total_read_misses_473RCl

tabla_RCl.at['473.astar-153B',
             'Miss rate lectura [%]'] = total_read_miss_rate_473RCl

tabla_RCl.at['473.astar-153B',
             'Misses escritura'] = total_write_misses_473RCl

tabla_RCl.at['473.astar-153B',
             'Miss rate escritura [%]'] = total_write_miss_rate_473RCl

# **481.wrf-1170B**

tabla_RCl.at['481.wrf-1170B', 'Total Misses'] = total_misses_481RCl

tabla_RCl.at['481.wrf-1170B', 'Miss rate total [%]'] = total_miss_rate_481RCl

tabla_RCl.at['481.wrf-1170B', 'Misses lectura'] = total_read_misses_481RCl

tabla_RCl.at['481.wrf-1170B',
             'Miss rate lectura [%]'] = total_read_miss_rate_481RCl

tabla_RCl.at['481.wrf-1170B',
             'Misses escritura'] = total_write_misses_481RCl

tabla_RCl.at['481.wrf-1170B',
             'Miss rate escritura [%]'] = total_write_miss_rate_481RCl

# **482.sphinx3-1100B**

tabla_RCl.at['482.sphinx3-1100B', 'Total Misses'] = total_misses_482RCl

tabla_RCl.at['482.sphinx3-1100B',
             'Miss rate total [%]'] = total_miss_rate_482RCl

tabla_RCl.at['482.sphinx3-1100B', 'Misses lectura'] = total_read_misses_482RCl

tabla_RCl.at['482.sphinx3-1100B',
             'Miss rate lectura [%]'] = total_read_miss_rate_482RCl

tabla_RCl.at['482.sphinx3-1100B',
             'Misses escritura'] = total_write_misses_482RCl

tabla_RCl.at['482.sphinx3-1100B',
             'Miss rate escritura [%]'] = total_write_miss_rate_482RCl

# **483.xalancbmk-127B**

tabla_RCl.at['483.xalancbmk-127B', 'Total Misses'] = total_misses_483RCl

tabla_RCl.at['483.xalancbmk-127B',
             'Miss rate total [%]'] = total_miss_rate_483RCl

tabla_RCl.at['483.xalancbmk-127B', 'Misses lectura'] = total_read_misses_483RCl

tabla_RCl.at['483.xalancbmk-127B',
             'Miss rate lectura [%]'] = total_read_miss_rate_483RCl

tabla_RCl.at['483.xalancbmk-127B',
             'Misses escritura'] = total_write_misses_483RCl

tabla_RCl.at['483.xalancbmk-127B',
             'Miss rate escritura [%]'] = total_write_miss_rate_483RCl

print(">>>>>All RCl data has been uploaded successfully")

##########################################################
# Extractor para experimento con replace policy aleatorio#
##########################################################

# Creación de tablas para adjuntar valores
# Una tabla por tamaño
tabla_RCa = pd.DataFrame(index=[
    '400.perlbench-41B', '401.bzip2-226B', '403.gcc-16B', '410.bwaves-1963B', '416.gamess-875B', '429.mcf-184B', '433.milc-127B',
    '435.gromacs-111B', '436.cactusADM-1804B', '437.leslie3d-134B', '444.namd-120B', '445.gobmk-17B',
    '450.soplex-247B', '453.povray-887B', '454.calculix-104B', '456.hmmer-191B', '458.sjeng-1088B', '459.GemsFDTD-1169B',
    '462.libquantum-1343B', '464.h264ref-30B', '465.tonto-1769B', '470.lbm-1274B', '471.omnetpp-188B', '473.astar-153B', '481.wrf-1170B',
    '482.sphinx3-1100B', '483.xalancbmk-127B'], columns=[
    'App', 'Total Misses', 'Miss rate total [%]', 'Misses lectura', 'Miss rate lectura [%]', 'Misses escritura', 'Miss rate escritura [%]'])
tabla_RCa['App'] = tabla_RCa.index

# Files paths
filename_28 = "RESULTS_RC/400RCa.txt"
filename_29 = "RESULTS_RC/401RCa.txt"
filename_30 = "RESULTS_RC/403RCa.txt"
filename_31 = "RESULTS_RC/410RCa.txt"
filename_32 = "RESULTS_RC/416RCa.txt"
filename_33 = "RESULTS_RC/429RCa.txt"
filename_34 = "RESULTS_RC/433RCa.txt"
filename_35 = "RESULTS_RC/435RCa.txt"
filename_36 = "RESULTS_RC/436RCa.txt"
filename_37 = "RESULTS_RC/437RCa.txt"
filename_38 = "RESULTS_RC/444RCa.txt"
filename_39 = "RESULTS_RC/445RCa.txt"
filename_40 = "RESULTS_RC/450RCa.txt"
filename_41 = "RESULTS_RC/453RCa.txt"
filename_42 = "RESULTS_RC/454RCa.txt"
filename_43 = "RESULTS_RC/456RCa.txt"
filename_44 = "RESULTS_RC/458RCa.txt"
filename_45 = "RESULTS_RC/459RCa.txt"
filename_46 = "RESULTS_RC/462RCa.txt"
filename_47 = "RESULTS_RC/464RCa.txt"
filename_48 = "RESULTS_RC/465RCa.txt"
filename_49 = "RESULTS_RC/470RCa.txt"
filename_50 = "RESULTS_RC/471RCa.txt"
filename_51 = "RESULTS_RC/473RCa.txt"
filename_52 = "RESULTS_RC/481RCa.txt"
filename_53 = "RESULTS_RC/482RCa.txt"
filename_54 = "RESULTS_RC/483RCa.txt"


# Content file extracter
with open(filename_28, 'r') as file:
    content_400RCa = file.read()
with open(filename_29, 'r') as file:
    content_401RCa = file.read()
with open(filename_30, 'r') as file:
    content_403RCa = file.read()
with open(filename_31, 'r') as file:
    content_410RCa = file.read()
with open(filename_32, 'r') as file:
    content_416RCa = file.read()
with open(filename_33, 'r') as file:
    content_429RCa = file.read()
with open(filename_34, 'r') as file:
    content_433RCa = file.read()
with open(filename_35, 'r') as file:
    content_435RCa = file.read()
with open(filename_36, 'r') as file:
    content_436RCa = file.read()
with open(filename_37, 'r') as file:
    content_437RCa = file.read()
with open(filename_38, 'r') as file:
    content_444RCa = file.read()
with open(filename_39, 'r') as file:
    content_445RCa = file.read()
with open(filename_40, 'r') as file:
    content_450RCa = file.read()
with open(filename_41, 'r') as file:
    content_453RCa = file.read()
with open(filename_42, 'r') as file:
    content_454RCa = file.read()
with open(filename_43, 'r') as file:
    content_456RCa = file.read()
with open(filename_44, 'r') as file:
    content_458RCa = file.read()
with open(filename_45, 'r') as file:
    content_459RCa = file.read()
with open(filename_46, 'r') as file:
    content_462RCa = file.read()
with open(filename_47, 'r') as file:
    content_464RCa = file.read()
with open(filename_48, 'r') as file:
    content_465RCa = file.read()
with open(filename_49, 'r') as file:
    content_470RCa = file.read()
with open(filename_50, 'r') as file:
    content_471RCa = file.read()
with open(filename_51, 'r') as file:
    content_473RCa = file.read()
with open(filename_52, 'r') as file:
    content_481RCa = file.read()
with open(filename_53, 'r') as file:
    content_482RCa = file.read()
with open(filename_54, 'r') as file:
    content_483RCa = file.read()


# Variables según aplicación

# 400.pearlbench-41B
total_misses_400RCa = re.search(
    r"Total_misses (\d+)", content_400RCa).group(1)
total_miss_rate_400RCa = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_400RCa).group(1)
total_read_misses_400RCa = re.search(
    r"Total_read_misses (\d+)", content_400RCa).group(1)
total_read_miss_rate_400RCa = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_400RCa).group(1)
total_write_misses_400RCa = re.search(
    r"Total_write_misses (\d+)", content_400RCa).group(1)
total_write_miss_rate_400RCa = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_400RCa).group(1)
print(">>>>>All RCa 400.pearlbench-41B variables where obtained successfully")

# 401.bzip2-226B
total_misses_401RCa = re.search(
    r"Total_misses (\d+)", content_401RCa).group(1)
total_miss_rate_401RCa = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_401RCa).group(1)
total_read_misses_401RCa = re.search(
    r"Total_read_misses (\d+)", content_401RCa).group(1)
total_read_miss_rate_401RCa = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_401RCa).group(1)
total_write_misses_401RCa = re.search(
    r"Total_write_misses (\d+)", content_401RCa).group(1)
total_write_miss_rate_401RCa = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_401RCa).group(1)
print(">>>>>All RCa 401.bzip2-226B variables where obtained successfully")

# 403.gcc-16B
total_misses_403RCa = re.search(
    r"Total_misses (\d+)", content_403RCa).group(1)
total_miss_rate_403RCa = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_403RCa).group(1)
total_read_misses_403RCa = re.search(
    r"Total_read_misses (\d+)", content_403RCa).group(1)
total_read_miss_rate_403RCa = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_403RCa).group(1)
total_write_misses_403RCa = re.search(
    r"Total_write_misses (\d+)", content_403RCa).group(1)
total_write_miss_rate_403RCa = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_403RCa).group(1)
print(">>>>>All RCa 403.gcc-16B variables where obtained successfully")

# 410.bwaves-1963B
total_misses_410RCa = re.search(
    r"Total_misses (\d+)", content_410RCa).group(1)
total_miss_rate_410RCa = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_410RCa).group(1)
total_read_misses_410RCa = re.search(
    r"Total_read_misses (\d+)", content_410RCa).group(1)
total_read_miss_rate_410RCa = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_410RCa).group(1)
total_write_misses_410RCa = re.search(
    r"Total_write_misses (\d+)", content_410RCa).group(1)
total_write_miss_rate_410RCa = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_410RCa).group(1)
print(">>>>>All RCa 410.bwaves-1963B variables where obtained successfully")

# 416.gamess-875B
total_misses_416RCa = re.search(
    r"Total_misses (\d+)", content_416RCa).group(1)
total_miss_rate_416RCa = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_416RCa).group(1)
total_read_misses_416RCa = re.search(
    r"Total_read_misses (\d+)", content_416RCa).group(1)
total_read_miss_rate_416RCa = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_416RCa).group(1)
total_write_misses_416RCa = re.search(
    r"Total_write_misses (\d+)", content_416RCa).group(1)
total_write_miss_rate_416RCa = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_416RCa).group(1)
print(">>>>>All RCa 416.gamess-875B variables where obtained successfully")

# 429.mcf-184B
total_misses_429RCa = re.search(
    r"Total_misses (\d+)", content_429RCa).group(1)
total_miss_rate_429RCa = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_429RCa).group(1)
total_read_misses_429RCa = re.search(
    r"Total_read_misses (\d+)", content_429RCa).group(1)
total_read_miss_rate_429RCa = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_429RCa).group(1)
total_write_misses_429RCa = re.search(
    r"Total_write_misses (\d+)", content_429RCa).group(1)
total_write_miss_rate_429RCa = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_429RCa).group(1)
print(">>>>>All RCa 429.mcf-184B variables where obtained successfully")

# 433.milc-127B
total_misses_433RCa = re.search(
    r"Total_misses (\d+)", content_433RCa).group(1)
total_miss_rate_433RCa = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_433RCa).group(1)
total_read_misses_433RCa = re.search(
    r"Total_read_misses (\d+)", content_433RCa).group(1)
total_read_miss_rate_433RCa = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_433RCa).group(1)
total_write_misses_433RCa = re.search(
    r"Total_write_misses (\d+)", content_433RCa).group(1)
total_write_miss_rate_433RCa = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_433RCa).group(1)
print(">>>>>All RCa 433.milc-127B variables where obtained successfully")

# 435.gromacs-111B
total_misses_435RCa = re.search(
    r"Total_misses (\d+)", content_435RCa).group(1)
total_miss_rate_435RCa = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_435RCa).group(1)
total_read_misses_435RCa = re.search(
    r"Total_read_misses (\d+)", content_435RCa).group(1)
total_read_miss_rate_435RCa = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_435RCa).group(1)
total_write_misses_435RCa = re.search(
    r"Total_write_misses (\d+)", content_435RCa).group(1)
total_write_miss_rate_435RCa = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_435RCa).group(1)
print(">>>>>All RCa 435.gromacs-111B variables where obtained successfully")

# 436.cactusADM-1804B
total_misses_436RCa = re.search(
    r"Total_misses (\d+)", content_436RCa).group(1)
total_miss_rate_436RCa = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_436RCa).group(1)
total_read_misses_436RCa = re.search(
    r"Total_read_misses (\d+)", content_436RCa).group(1)
total_read_miss_rate_436RCa = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_436RCa).group(1)
total_write_misses_436RCa = re.search(
    r"Total_write_misses (\d+)", content_436RCa).group(1)
total_write_miss_rate_436RCa = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_436RCa).group(1)
print(">>>>>All RCa 436.cactusADM-1804B variables where obtained successfully")

# 437.leslie3d-134B
total_misses_437RCa = re.search(
    r"Total_misses (\d+)", content_437RCa).group(1)
total_miss_rate_437RCa = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_437RCa).group(1)
total_read_misses_437RCa = re.search(
    r"Total_read_misses (\d+)", content_437RCa).group(1)
total_read_miss_rate_437RCa = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_437RCa).group(1)
total_write_misses_437RCa = re.search(
    r"Total_write_misses (\d+)", content_437RCa).group(1)
total_write_miss_rate_437RCa = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_437RCa).group(1)
print(">>>>>All RCa 437.leslie3d-134B variables where obtained successfully")

# 444.namd-120B
total_misses_444RCa = re.search(
    r"Total_misses (\d+)", content_444RCa).group(1)
total_miss_rate_444RCa = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_444RCa).group(1)
total_read_misses_444RCa = re.search(
    r"Total_read_misses (\d+)", content_444RCa).group(1)
total_read_miss_rate_444RCa = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_444RCa).group(1)
total_write_misses_444RCa = re.search(
    r"Total_write_misses (\d+)", content_444RCa).group(1)
total_write_miss_rate_444RCa = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_444RCa).group(1)
print(">>>>>All RCa 444.namd-120B variables where obtained successfully")

# 445.gobmk-17B
total_misses_445RCa = re.search(
    r"Total_misses (\d+)", content_445RCa).group(1)
total_miss_rate_445RCa = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_445RCa).group(1)
total_read_misses_445RCa = re.search(
    r"Total_read_misses (\d+)", content_445RCa).group(1)
total_read_miss_rate_445RCa = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_445RCa).group(1)
total_write_misses_445RCa = re.search(
    r"Total_write_misses (\d+)", content_445RCa).group(1)
total_write_miss_rate_445RCa = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_445RCa).group(1)
print(">>>>>All RCa 445.gobmk-17B variables where obtained successfully")

# 450.soplex-247B
total_misses_450RCa = re.search(
    r"Total_misses (\d+)", content_450RCa).group(1)
total_miss_rate_450RCa = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_450RCa).group(1)
total_read_misses_450RCa = re.search(
    r"Total_read_misses (\d+)", content_450RCa).group(1)
total_read_miss_rate_450RCa = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_450RCa).group(1)
total_write_misses_450RCa = re.search(
    r"Total_write_misses (\d+)", content_450RCa).group(1)
total_write_miss_rate_450RCa = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_450RCa).group(1)
print(">>>>>All RCa 450.soplex-247B variables where obtained successfully")

# 453.povray-887B
total_misses_453RCa = re.search(
    r"Total_misses (\d+)", content_453RCa).group(1)
total_miss_rate_453RCa = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_453RCa).group(1)
total_read_misses_453RCa = re.search(
    r"Total_read_misses (\d+)", content_453RCa).group(1)
total_read_miss_rate_453RCa = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_453RCa).group(1)
total_write_misses_453RCa = re.search(
    r"Total_write_misses (\d+)", content_453RCa).group(1)
total_write_miss_rate_453RCa = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_453RCa).group(1)
print(">>>>>All RCa 453.povray-887B variables where obtained successfully")

# 454.calculix-104B
total_misses_454RCa = re.search(
    r"Total_misses (\d+)", content_454RCa).group(1)
total_miss_rate_454RCa = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_454RCa).group(1)
total_read_misses_454RCa = re.search(
    r"Total_read_misses (\d+)", content_454RCa).group(1)
total_read_miss_rate_454RCa = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_454RCa).group(1)
total_write_misses_454RCa = re.search(
    r"Total_write_misses (\d+)", content_454RCa).group(1)
total_write_miss_rate_454RCa = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_454RCa).group(1)
print(">>>>>All RCa 454.calculix-104B variables where obtained successfully")

# 456.hmmer-191B
total_misses_456RCa = re.search(
    r"Total_misses (\d+)", content_456RCa).group(1)
total_miss_rate_456RCa = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_456RCa).group(1)
total_read_misses_456RCa = re.search(
    r"Total_read_misses (\d+)", content_456RCa).group(1)
total_read_miss_rate_456RCa = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_456RCa).group(1)
total_write_misses_456RCa = re.search(
    r"Total_write_misses (\d+)", content_456RCa).group(1)
total_write_miss_rate_456RCa = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_456RCa).group(1)
print(">>>>>All RCa 456.hmmer-191B variables where obtained successfully")

# 458.sjeng-1088B
total_misses_458RCa = re.search(
    r"Total_misses (\d+)", content_458RCa).group(1)
total_miss_rate_458RCa = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_458RCa).group(1)
total_read_misses_458RCa = re.search(
    r"Total_read_misses (\d+)", content_458RCa).group(1)
total_read_miss_rate_458RCa = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_458RCa).group(1)
total_write_misses_458RCa = re.search(
    r"Total_write_misses (\d+)", content_458RCa).group(1)
total_write_miss_rate_458RCa = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_458RCa).group(1)
print(">>>>>All RCa 458.sjeng-1088B variables where obtained successfully")

# 459.GemsFDTD-1169B
total_misses_459RCa = re.search(
    r"Total_misses (\d+)", content_459RCa).group(1)
total_miss_rate_459RCa = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_459RCa).group(1)
total_read_misses_459RCa = re.search(
    r"Total_read_misses (\d+)", content_459RCa).group(1)
total_read_miss_rate_459RCa = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_459RCa).group(1)
total_write_misses_459RCa = re.search(
    r"Total_write_misses (\d+)", content_459RCa).group(1)
total_write_miss_rate_459RCa = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_459RCa).group(1)
print(">>>>>All RCa 459.GemsFDTD-1169B variables where obtained successfully")

# 462.libquantum-1343B
total_misses_462RCa = re.search(
    r"Total_misses (\d+)", content_462RCa).group(1)
total_miss_rate_462RCa = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_462RCa).group(1)
total_read_misses_462RCa = re.search(
    r"Total_read_misses (\d+)", content_462RCa).group(1)
total_read_miss_rate_462RCa = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_462RCa).group(1)
total_write_misses_462RCa = re.search(
    r"Total_write_misses (\d+)", content_462RCa).group(1)
total_write_miss_rate_462RCa = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_462RCa).group(1)
print(">>>>>All RCa 462.libquantum-1343B variables where obtained successfully")

# 464.h264ref-30B
total_misses_464RCa = re.search(
    r"Total_misses (\d+)", content_464RCa).group(1)
total_miss_rate_464RCa = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_464RCa).group(1)
total_read_misses_464RCa = re.search(
    r"Total_read_misses (\d+)", content_464RCa).group(1)
total_read_miss_rate_464RCa = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_464RCa).group(1)
total_write_misses_464RCa = re.search(
    r"Total_write_misses (\d+)", content_464RCa).group(1)
total_write_miss_rate_464RCa = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_464RCa).group(1)
print(">>>>>All RCa 464.h264ref-30B variables where obtained successfully")

# 465.tonto-1769B
total_misses_465RCa = re.search(
    r"Total_misses (\d+)", content_465RCa).group(1)
total_miss_rate_465RCa = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_465RCa).group(1)
total_read_misses_465RCa = re.search(
    r"Total_read_misses (\d+)", content_465RCa).group(1)
total_read_miss_rate_465RCa = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_465RCa).group(1)
total_write_misses_465RCa = re.search(
    r"Total_write_misses (\d+)", content_465RCa).group(1)
total_write_miss_rate_465RCa = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_465RCa).group(1)
print(">>>>>All RCa 465.tonto-1769B variables where obtained successfully")

# 470.lbm-1274B
total_misses_470RCa = re.search(
    r"Total_misses (\d+)", content_470RCa).group(1)
total_miss_rate_470RCa = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_470RCa).group(1)
total_read_misses_470RCa = re.search(
    r"Total_read_misses (\d+)", content_470RCa).group(1)
total_read_miss_rate_470RCa = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_470RCa).group(1)
total_write_misses_470RCa = re.search(
    r"Total_write_misses (\d+)", content_470RCa).group(1)
total_write_miss_rate_470RCa = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_470RCa).group(1)
print(">>>>>All RCa 470.lbm-1274B variables where obtained successfully")

# 471.omnetpp-188B
total_misses_471RCa = re.search(
    r"Total_misses (\d+)", content_471RCa).group(1)
total_miss_rate_471RCa = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_471RCa).group(1)
total_read_misses_471RCa = re.search(
    r"Total_read_misses (\d+)", content_471RCa).group(1)
total_read_miss_rate_471RCa = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_471RCa).group(1)
total_write_misses_471RCa = re.search(
    r"Total_write_misses (\d+)", content_471RCa).group(1)
total_write_miss_rate_471RCa = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_471RCa).group(1)
print(">>>>>All RCa 471.omnetpp-188B variables where obtained successfully")

# 473.astar-153B
total_misses_473RCa = re.search(
    r"Total_misses (\d+)", content_473RCa).group(1)
total_miss_rate_473RCa = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_473RCa).group(1)
total_read_misses_473RCa = re.search(
    r"Total_read_misses (\d+)", content_473RCa).group(1)
total_read_miss_rate_473RCa = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_473RCa).group(1)
total_write_misses_473RCa = re.search(
    r"Total_write_misses (\d+)", content_473RCa).group(1)
total_write_miss_rate_473RCa = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_473RCa).group(1)
print(">>>>>All RCa 473.astar-153B variables where obtained successfully")

# 481.wrf-1170B
total_misses_481RCa = re.search(
    r"Total_misses (\d+)", content_481RCa).group(1)
total_miss_rate_481RCa = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_481RCa).group(1)
total_read_misses_481RCa = re.search(
    r"Total_read_misses (\d+)", content_481RCa).group(1)
total_read_miss_rate_481RCa = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_481RCa).group(1)
total_write_misses_481RCa = re.search(
    r"Total_write_misses (\d+)", content_481RCa).group(1)
total_write_miss_rate_481RCa = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_481RCa).group(1)
print(">>>>>All RCa 481.wrf-1170B variables where obtained successfully")

# 482.sphinx3-1100B
total_misses_482RCa = re.search(
    r"Total_misses (\d+)", content_482RCa).group(1)
total_miss_rate_482RCa = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_482RCa).group(1)
total_read_misses_482RCa = re.search(
    r"Total_read_misses (\d+)", content_482RCa).group(1)
total_read_miss_rate_482RCa = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_482RCa).group(1)
total_write_misses_482RCa = re.search(
    r"Total_write_misses (\d+)", content_482RCa).group(1)
total_write_miss_rate_482RCa = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_482RCa).group(1)
print(">>>>>All RCa 482.sphinx3-1100B variables where obtained successfully")

# 483.xalancbmk-127B
total_misses_483RCa = re.search(
    r"Total_misses (\d+)", content_483RCa).group(1)
total_miss_rate_483RCa = re.search(
    r"Total_miss_rate (\d+\.\d+)", content_483RCa).group(1)
total_read_misses_483RCa = re.search(
    r"Total_read_misses (\d+)", content_483RCa).group(1)
total_read_miss_rate_483RCa = re.search(
    r"Total_read_miss_rate (\d+\.\d+)", content_483RCa).group(1)
total_write_misses_483RCa = re.search(
    r"Total_write_misses (\d+)", content_483RCa).group(1)
total_write_miss_rate_483RCa = re.search(
    r"Total_write_miss_rate (\d+\.\d+)", content_483RCa).group(1)
print(">>>>>All RCa 483.xalancbmk-127B variables where obtained successfully")

#############################
# Adjunta datos a dataframe #
#############################

# **400.perlbench-41B**

tabla_RCa.at['400.perlbench-41B', 'Total Misses'] = total_misses_400RCa

tabla_RCa.at['400.perlbench-41B',
             'Miss rate total [%]'] = total_miss_rate_400RCa

tabla_RCa.at['400.perlbench-41B',
             'Misses lectura'] = total_read_misses_400RCa

tabla_RCa.at['400.perlbench-41B',
             'Miss rate lectura [%]'] = total_read_miss_rate_400RCa

tabla_RCa.at['400.perlbench-41B',
             'Misses escritura'] = total_write_misses_400RCa

tabla_RCa.at['400.perlbench-41B',
             'Miss rate escritura [%]'] = total_write_miss_rate_400RCa

# **401.bzip2-226B**

tabla_RCa.at['401.bzip2-226B', 'Total Misses'] = total_misses_401RCa

tabla_RCa.at['401.bzip2-226B',
             'Miss rate total [%]'] = total_miss_rate_401RCa

tabla_RCa.at['401.bzip2-226B', 'Misses lectura'] = total_read_misses_401RCa

tabla_RCa.at['401.bzip2-226B',
             'Miss rate lectura [%]'] = total_read_miss_rate_401RCa

tabla_RCa.at['401.bzip2-226B',
             'Misses escritura'] = total_write_misses_401RCa

tabla_RCa.at['401.bzip2-226B',
             'Miss rate escritura [%]'] = total_write_miss_rate_401RCa

# **403.gcc-16B**

tabla_RCa.at['403.gcc-16B', 'Total Misses'] = total_misses_403RCa

tabla_RCa.at['403.gcc-16B', 'Miss rate total [%]'] = total_miss_rate_403RCa

tabla_RCa.at['403.gcc-16B', 'Misses lectura'] = total_read_misses_403RCa

tabla_RCa.at['403.gcc-16B',
             'Miss rate lectura [%]'] = total_read_miss_rate_403RCa

tabla_RCa.at['403.gcc-16B',
             'Misses escritura'] = total_write_misses_403RCa

tabla_RCa.at['403.gcc-16B',
             'Miss rate escritura [%]'] = total_write_miss_rate_403RCa

# **410.bwaves-1963B**

tabla_RCa.at['410.bwaves-1963B', 'Total Misses'] = total_misses_410RCa

tabla_RCa.at['410.bwaves-1963B',
             'Miss rate total [%]'] = total_miss_rate_410RCa

tabla_RCa.at['410.bwaves-1963B', 'Misses lectura'] = total_read_misses_410RCa

tabla_RCa.at['410.bwaves-1963B',
             'Miss rate lectura [%]'] = total_read_miss_rate_410RCa

tabla_RCa.at['410.bwaves-1963B',
             'Misses escritura'] = total_write_misses_410RCa

tabla_RCa.at['410.bwaves-1963B',
             'Miss rate escritura [%]'] = total_write_miss_rate_410RCa

# **416.gamess-875B**

tabla_RCa.at['416.gamess-875B', 'Total Misses'] = total_misses_416RCa

tabla_RCa.at['416.gamess-875B',
             'Miss rate total [%]'] = total_miss_rate_416RCa

tabla_RCa.at['416.gamess-875B', 'Misses lectura'] = total_read_misses_416RCa

tabla_RCa.at['416.gamess-875B',
             'Miss rate lectura [%]'] = total_read_miss_rate_416RCa

tabla_RCa.at['416.gamess-875B',
             'Misses escritura'] = total_write_misses_416RCa

tabla_RCa.at['416.gamess-875B',
             'Miss rate escritura [%]'] = total_write_miss_rate_416RCa

# **429.mcf-184B**

tabla_RCa.at['429.mcf-184B', 'Total Misses'] = total_misses_429RCa

tabla_RCa.at['429.mcf-184B', 'Miss rate total [%]'] = total_miss_rate_429RCa

tabla_RCa.at['429.mcf-184B', 'Misses lectura'] = total_read_misses_429RCa

tabla_RCa.at['429.mcf-184B',
             'Miss rate lectura [%]'] = total_read_miss_rate_429RCa

tabla_RCa.at['429.mcf-184B',
             'Misses escritura'] = total_write_misses_429RCa

tabla_RCa.at['429.mcf-184B',
             'Miss rate escritura [%]'] = total_write_miss_rate_429RCa

# **433.milc-127B**

tabla_RCa.at['433.milc-127B', 'Total Misses'] = total_misses_433RCa

tabla_RCa.at['433.milc-127B', 'Miss rate total [%]'] = total_miss_rate_433RCa

tabla_RCa.at['433.milc-127B', 'Misses lectura'] = total_read_misses_433RCa

tabla_RCa.at['433.milc-127B',
             'Miss rate lectura [%]'] = total_read_miss_rate_433RCa

tabla_RCa.at['433.milc-127B',
             'Misses escritura'] = total_write_misses_433RCa

tabla_RCa.at['433.milc-127B',
             'Miss rate escritura [%]'] = total_write_miss_rate_433RCa

# **435.gromacs-111B**

tabla_RCa.at['435.gromacs-111B', 'Total Misses'] = total_misses_435RCa

tabla_RCa.at['435.gromacs-111B',
             'Miss rate total [%]'] = total_miss_rate_435RCa

tabla_RCa.at['435.gromacs-111B', 'Misses lectura'] = total_read_misses_435RCa

tabla_RCa.at['435.gromacs-111B',
             'Miss rate lectura [%]'] = total_read_miss_rate_435RCa

tabla_RCa.at['435.gromacs-111B',
             'Misses escritura'] = total_write_misses_435RCa

tabla_RCa.at['435.gromacs-111B',
             'Miss rate escritura [%]'] = total_write_miss_rate_435RCa
# **436.cactusADM-1804B**

tabla_RCa.at['436.cactusADM-1804B', 'Total Misses'] = total_misses_436RCa

tabla_RCa.at['436.cactusADM-1804B',
             'Miss rate total [%]'] = total_miss_rate_436RCa

tabla_RCa.at['436.cactusADM-1804B',
             'Misses lectura'] = total_read_misses_436RCa

tabla_RCa.at['436.cactusADM-1804B',
             'Miss rate lectura [%]'] = total_read_miss_rate_436RCa

tabla_RCa.at['436.cactusADM-1804B',
             'Misses escritura'] = total_write_misses_436RCa

tabla_RCa.at['436.cactusADM-1804B',
             'Miss rate escritura [%]'] = total_write_miss_rate_436RCa

# **437.leslie3d-134B**

tabla_RCa.at['437.leslie3d-134B', 'Total Misses'] = total_misses_437RCa

tabla_RCa.at['437.leslie3d-134B',
             'Miss rate total [%]'] = total_miss_rate_437RCa

tabla_RCa.at['437.leslie3d-134B',
             'Misses lectura'] = total_read_misses_437RCa

tabla_RCa.at['437.leslie3d-134B',
             'Miss rate lectura [%]'] = total_read_miss_rate_437RCa

tabla_RCa.at['437.leslie3d-134B',
             'Misses escritura'] = total_write_misses_437RCa

tabla_RCa.at['437.leslie3d-134B',
             'Miss rate escritura [%]'] = total_write_miss_rate_437RCa

# **444.namd-120B**

tabla_RCa.at['444.namd-120B', 'Total Misses'] = total_misses_444RCa

tabla_RCa.at['444.namd-120B', 'Miss rate total [%]'] = total_miss_rate_444RCa

tabla_RCa.at['444.namd-120B', 'Misses lectura'] = total_read_misses_444RCa

tabla_RCa.at['444.namd-120B',
             'Miss rate lectura [%]'] = total_read_miss_rate_444RCa

tabla_RCa.at['444.namd-120B',
             'Misses escritura'] = total_write_misses_444RCa

tabla_RCa.at['444.namd-120B',
             'Miss rate escritura [%]'] = total_write_miss_rate_444RCa

# **445.gobmk-17B**

tabla_RCa.at['445.gobmk-17B', 'Total Misses'] = total_misses_445RCa

tabla_RCa.at['445.gobmk-17B', 'Miss rate total [%]'] = total_miss_rate_445RCa

tabla_RCa.at['445.gobmk-17B', 'Misses lectura'] = total_read_misses_445RCa

tabla_RCa.at['445.gobmk-17B',
             'Miss rate lectura [%]'] = total_read_miss_rate_445RCa

tabla_RCa.at['445.gobmk-17B',
             'Misses escritura'] = total_write_misses_445RCa

tabla_RCa.at['445.gobmk-17B',
             'Miss rate escritura [%]'] = total_write_miss_rate_445RCa

# **450.soplex-247B**

tabla_RCa.at['450.soplex-247B', 'Total Misses'] = total_misses_450RCa

tabla_RCa.at['450.soplex-247B',
             'Miss rate total [%]'] = total_miss_rate_450RCa

tabla_RCa.at['450.soplex-247B', 'Misses lectura'] = total_read_misses_450RCa

tabla_RCa.at['450.soplex-247B',
             'Miss rate lectura [%]'] = total_read_miss_rate_450RCa

tabla_RCa.at['450.soplex-247B',
             'Misses escritura'] = total_write_misses_450RCa

tabla_RCa.at['450.soplex-247B',
             'Miss rate escritura [%]'] = total_write_miss_rate_450RCa

# **453.povray-887B**

tabla_RCa.at['453.povray-887B', 'Total Misses'] = total_misses_453RCa

tabla_RCa.at['453.povray-887B',
             'Miss rate total [%]'] = total_miss_rate_453RCa

tabla_RCa.at['453.povray-887B', 'Misses lectura'] = total_read_misses_453RCa

tabla_RCa.at['453.povray-887B',
             'Miss rate lectura [%]'] = total_read_miss_rate_453RCa

tabla_RCa.at['453.povray-887B',
             'Misses escritura'] = total_write_misses_453RCa

tabla_RCa.at['453.povray-887B',
             'Miss rate escritura [%]'] = total_write_miss_rate_453RCa

# **454.calculix-104B**

tabla_RCa.at['454.calculix-104B', 'Total Misses'] = total_misses_454RCa

tabla_RCa.at['454.calculix-104B',
             'Miss rate total [%]'] = total_miss_rate_454RCa

tabla_RCa.at['454.calculix-104B',
             'Misses lectura'] = total_read_misses_454RCa

tabla_RCa.at['454.calculix-104B',
             'Miss rate lectura [%]'] = total_read_miss_rate_454RCa

tabla_RCa.at['454.calculix-104B',
             'Misses escritura'] = total_write_misses_454RCa

tabla_RCa.at['454.calculix-104B',
             'Miss rate escritura [%]'] = total_write_miss_rate_454RCa

# **456.hmmer-191B**

tabla_RCa.at['456.hmmer-191B', 'Total Misses'] = total_misses_456RCa

tabla_RCa.at['456.hmmer-191B',
             'Miss rate total [%]'] = total_miss_rate_456RCa

tabla_RCa.at['456.hmmer-191B', 'Misses lectura'] = total_read_misses_456RCa

tabla_RCa.at['456.hmmer-191B',
             'Miss rate lectura [%]'] = total_read_miss_rate_456RCa

tabla_RCa.at['456.hmmer-191B',
             'Misses escritura'] = total_write_misses_456RCa

tabla_RCa.at['456.hmmer-191B',
             'Miss rate escritura [%]'] = total_write_miss_rate_456RCa

# **458.sjeng-1088B**

tabla_RCa.at['458.sjeng-1088B', 'Total Misses'] = total_misses_458RCa

tabla_RCa.at['458.sjeng-1088B',
             'Miss rate total [%]'] = total_miss_rate_458RCa

tabla_RCa.at['458.sjeng-1088B', 'Misses lectura'] = total_read_misses_458RCa

tabla_RCa.at['458.sjeng-1088B',
             'Miss rate lectura [%]'] = total_read_miss_rate_458RCa

tabla_RCa.at['458.sjeng-1088B',
             'Misses escritura'] = total_write_misses_458RCa

tabla_RCa.at['458.sjeng-1088B',
             'Miss rate escritura [%]'] = total_write_miss_rate_458RCa

# **459.GemsFDTD-1169B**

tabla_RCa.at['459.GemsFDTD-1169B', 'Total Misses'] = total_misses_459RCa

tabla_RCa.at['459.GemsFDTD-1169B',
             'Miss rate total [%]'] = total_miss_rate_459RCa

tabla_RCa.at['459.GemsFDTD-1169B',
             'Misses lectura'] = total_read_misses_459RCa

tabla_RCa.at['459.GemsFDTD-1169B',
             'Miss rate lectura [%]'] = total_read_miss_rate_459RCa

tabla_RCa.at['459.GemsFDTD-1169B',
             'Misses escritura'] = total_write_misses_459RCa

tabla_RCa.at['459.GemsFDTD-1169B',
             'Miss rate escritura [%]'] = total_write_miss_rate_459RCa

# **462.libquantum-1343B**

tabla_RCa.at['462.libquantum-1343B', 'Total Misses'] = total_misses_462RCa

tabla_RCa.at['462.libquantum-1343B',
             'Miss rate total [%]'] = total_miss_rate_462RCa

tabla_RCa.at['462.libquantum-1343B',
             'Misses lectura'] = total_read_misses_462RCa

tabla_RCa.at['462.libquantum-1343B',
             'Miss rate lectura [%]'] = total_read_miss_rate_462RCa

tabla_RCa.at['462.libquantum-1343B',
             'Misses escritura'] = total_write_misses_462RCa

tabla_RCa.at['462.libquantum-1343B',
             'Miss rate escritura [%]'] = total_write_miss_rate_462RCa

# **464.h264ref-30B**

tabla_RCa.at['464.h264ref-30B', 'Total Misses'] = total_misses_464RCa

tabla_RCa.at['464.h264ref-30B',
             'Miss rate total [%]'] = total_miss_rate_464RCa

tabla_RCa.at['464.h264ref-30B', 'Misses lectura'] = total_read_misses_464RCa

tabla_RCa.at['464.h264ref-30B',
             'Miss rate lectura [%]'] = total_read_miss_rate_464RCa

tabla_RCa.at['464.h264ref-30B',
             'Misses escritura'] = total_write_misses_464RCa

tabla_RCa.at['464.h264ref-30B',
             'Miss rate escritura [%]'] = total_write_miss_rate_464RCa

# **465.tonto-1769B**

tabla_RCa.at['465.tonto-1769B', 'Total Misses'] = total_misses_465RCa

tabla_RCa.at['465.tonto-1769B',
             'Miss rate total [%]'] = total_miss_rate_465RCa

tabla_RCa.at['465.tonto-1769B', 'Misses lectura'] = total_read_misses_465RCa

tabla_RCa.at['465.tonto-1769B',
             'Miss rate lectura [%]'] = total_read_miss_rate_465RCa

tabla_RCa.at['465.tonto-1769B',
             'Misses escritura'] = total_write_misses_465RCa
tabla_RCa.at['465.tonto-1769B',
             'Miss rate escritura [%]'] = total_write_miss_rate_465RCa

# **470.lbm-1274B**

tabla_RCa.at['470.lbm-1274B', 'Total Misses'] = total_misses_470RCa

tabla_RCa.at['470.lbm-1274B', 'Miss rate total [%]'] = total_miss_rate_470RCa

tabla_RCa.at['470.lbm-1274B', 'Misses lectura'] = total_read_misses_470RCa

tabla_RCa.at['470.lbm-1274B',
             'Miss rate lectura [%]'] = total_read_miss_rate_470RCa

tabla_RCa.at['470.lbm-1274B',
             'Misses escritura'] = total_write_misses_470RCa

tabla_RCa.at['470.lbm-1274B',
             'Miss rate escritura [%]'] = total_write_miss_rate_470RCa

# **471.omnetpp-188B**

tabla_RCa.at['471.omnetpp-188B', 'Total Misses'] = total_misses_471RCa

tabla_RCa.at['471.omnetpp-188B',
             'Miss rate total [%]'] = total_miss_rate_471RCa

tabla_RCa.at['471.omnetpp-188B', 'Misses lectura'] = total_read_misses_471RCa

tabla_RCa.at['471.omnetpp-188B',
             'Miss rate lectura [%]'] = total_read_miss_rate_471RCa

tabla_RCa.at['471.omnetpp-188B',
             'Misses escritura'] = total_write_misses_471RCa

tabla_RCa.at['471.omnetpp-188B',
             'Miss rate escritura [%]'] = total_write_miss_rate_471RCa

# **473.astar-153B**

tabla_RCa.at['473.astar-153B', 'Total Misses'] = total_misses_473RCa

tabla_RCa.at['473.astar-153B',
             'Miss rate total [%]'] = total_miss_rate_473RCa

tabla_RCa.at['473.astar-153B', 'Misses lectura'] = total_read_misses_473RCa

tabla_RCa.at['473.astar-153B',
             'Miss rate lectura [%]'] = total_read_miss_rate_473RCa

tabla_RCa.at['473.astar-153B',
             'Misses escritura'] = total_write_misses_473RCa

tabla_RCa.at['473.astar-153B',
             'Miss rate escritura [%]'] = total_write_miss_rate_473RCa

# **481.wrf-1170B**

tabla_RCa.at['481.wrf-1170B', 'Total Misses'] = total_misses_481RCa

tabla_RCa.at['481.wrf-1170B', 'Miss rate total [%]'] = total_miss_rate_481RCa

tabla_RCa.at['481.wrf-1170B', 'Misses lectura'] = total_read_misses_481RCa

tabla_RCa.at['481.wrf-1170B',
             'Miss rate lectura [%]'] = total_read_miss_rate_481RCa

tabla_RCa.at['481.wrf-1170B',
             'Misses escritura'] = total_write_misses_481RCa

tabla_RCa.at['481.wrf-1170B',
             'Miss rate escritura [%]'] = total_write_miss_rate_481RCa

# **482.sphinx3-1100B**

tabla_RCa.at['482.sphinx3-1100B', 'Total Misses'] = total_misses_482RCa

tabla_RCa.at['482.sphinx3-1100B',
             'Miss rate total [%]'] = total_miss_rate_482RCa

tabla_RCa.at['482.sphinx3-1100B',
             'Misses lectura'] = total_read_misses_482RCa

tabla_RCa.at['482.sphinx3-1100B',
             'Miss rate lectura [%]'] = total_read_miss_rate_482RCa

tabla_RCa.at['482.sphinx3-1100B',
             'Misses escritura'] = total_write_misses_482RCa

tabla_RCa.at['482.sphinx3-1100B',
             'Miss rate escritura [%]'] = total_write_miss_rate_482RCa

# **483.xalancbmk-127B**

tabla_RCa.at['483.xalancbmk-127B', 'Total Misses'] = total_misses_483RCa

tabla_RCa.at['483.xalancbmk-127B',
             'Miss rate total [%]'] = total_miss_rate_483RCa

tabla_RCa.at['483.xalancbmk-127B',
             'Misses lectura'] = total_read_misses_483RCa

tabla_RCa.at['483.xalancbmk-127B',
             'Miss rate lectura [%]'] = total_read_miss_rate_483RCa

tabla_RCa.at['483.xalancbmk-127B',
             'Misses escritura'] = total_write_misses_483RCa

tabla_RCa.at['483.xalancbmk-127B',
             'Miss rate escritura [%]'] = total_write_miss_rate_483RCa

print(">>>>>All RCa data has been uploaded successfully")

###########
# GEO MEAN#
###########

# GEO MEAN Miss rate total RCl
columna_RCl = tabla_RCl['Miss rate total [%]']
columna_RCl_numpy = columna_RCl.to_numpy(dtype=np.float64)
GEOMEAN_Miss_rate_total_RCl = gmean(columna_RCl_numpy)

# GEO MEAN Miss rate total RCa
columna_RCa = tabla_RCa['Miss rate total [%]']
columna_RCa_numpy = columna_RCa.to_numpy(dtype=np.float64)
GEOMEAN_Miss_rate_total_RCa = gmean(columna_RCa_numpy)

############################################
# Dataframes de resultados: miss rate total#
############################################

# Creación de tablas para adjuntar valores

# Miss rate
tabla_miss_rate_total = pd.DataFrame(index=[
    'Miss rate total [%]'], columns=[
    'Parámetro', 'LRU', 'aleatorio'])
tabla_miss_rate_total['Parámetro'] = tabla_miss_rate_total.index

##############################
# Adjunta datos en dataframes#
##############################

# Miss rate total
tabla_miss_rate_total.at['Miss rate total [%]',
                         'LRU'] = GEOMEAN_Miss_rate_total_RCl
tabla_miss_rate_total.at['Miss rate total [%]',
                         'aleatorio'] = GEOMEAN_Miss_rate_total_RCa

############################################
# Archivo de salida para facilitar gráficos#
############################################

# Create an Excel writer using pandas
output = pd.ExcelWriter('Results_RC.xlsx')

# Write each dataframe to a different sheet in the Excel file
tabla_RCl.to_excel(output, sheet_name='RCl', index=False)
tabla_RCa.to_excel(output, sheet_name='RCa', index=False)
tabla_miss_rate_total.to_excel(
    output, sheet_name='Miss rate total promedio', index=False)

# Save the Excel file
output.save()

print("''''''''''''''''''''''''''''''''''''''''''''''''''''''' Replace policy: LRU''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
print(tabla_RCl.to_string(index=False))
print("#################################################################################")
print("El miss rate promedio [%] con replace policy: LRU es: ",
      GEOMEAN_Miss_rate_total_RCl, ' #')
print("#################################################################################")
print("")
print("'''''''''''''''''''''''''''''''''''''''''''''''''''' Replace policy: aleatorio'''''''''''''''''''''''''''''''''''''''''''''''''''''")
print(tabla_RCa.to_string(index=False))
print("##################################################################################")
print("El miss rate promedio [%] con un tamaño de caché de 16kB es: ",
      GEOMEAN_Miss_rate_total_RCa, '#')
print("")
print("##################################################################################")
print("''''''''''''''''''''''''''' Miss rate total'''''''''''''''''''''''''''''")
print(tabla_miss_rate_total.to_string(index=False))
print("")
