#!/bin/bash

# Create an array to store the simulation process IDs
pids=()
echo "''''''''''''''''''''''''''''''''''''''''''''''''"
echo "Experimento: variación replace policy cache(RC) "
echo "''''''''''''''''''''''''''''''''''''''''''''''''"

# Define the directory name where txt result will be stored
directory_name="RESULTS_RC"
# Create the directory
mkdir "$directory_name"

##########################
# Replace policy:    LRU #
##########################
echo "'''''''''''''''''''''''''''''"
echo "' Tamaño de caché:  '''32kB'''"
echo "' Asociatividad: 8-ways     '"
echo "' Tamaño de bloque: 64kB    '"    
echo "' Política de reemplazo: LRU'"
echo "'''''''''''''''''''''''''''''"

# Simulation 1: 400.perlbench Replace policy: LRU
echo "Running 400.perlbench-Replace policy: LRU"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/400.perlbench-41B.trace.txt.gz > "$directory_name/400RCl.txt" &
pid1=$!
pids+=($pid1)

# Simulation 2: 401.bzip2 Replace policy: LRU
echo "Running 401.bzip2-Replace policy: LRU"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/401.bzip2-226B.trace.txt.gz > "$directory_name/401RCl.txt" &
pid2=$!
pids+=($pid2)

# Simulation 3: 403.gcc Replace policy: LRU
echo "Running 403.gcc-Replace policy: LRU"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/403.gcc-16B.trace.txt.gz > "$directory_name/403RCl.txt" &
pid3=$!
pids+=($pid3)

# Simulation 4: 410.bwaves Replace policy: LRU
echo "Running 410.bwaves-Replace policy: LRU"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/410.bwaves-1963B.trace.txt.gz > "$directory_name/410RCl.txt" &
pid4=$!
pids+=($pid4)

# Simulation 5: 416.gamess Replace policy: LRU
echo "Running 416.gamess Replace policy: LRU"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/416.gamess-875B.trace.txt.gz > "$directory_name/416RCl.txt" &
pids+=($pid5)

# Simulation 6: 429.mcf Replace policy: LRU
echo "Running 429.mcf Replace policy: LRU"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/429.mcf-184B.trace.txt.gz > "$directory_name/429RCl.txt" &
pids+=($pid6)

# Simulation 7: 433.milc Replace policy: LRU
echo "Running 433.milc Replace policy: LRU"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/433.milc-127B.trace.txt.gz > "$directory_name/433RCl.txt" &
pids+=($pid7)

# Simulation 8: 435.gromacs Replace policy: LRU
echo "Running 435.gromacs Replace policy: LRU"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/435.gromacs-111B.trace.txt.gz > "$directory_name/435RCl.txt" &
pids+=($pid8)

# Simulation 9: 436.cactusADM Replace policy: LRU
echo "Running 436.cactusADM Replace policy: LRU"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/436.cactusADM-1804B.trace.txt.gz > "$directory_name/436RCl.txt" &
pids+=($pid9)

# Simulation 10: 437.leslie3d Replace policy: LRU
echo "Running 437.leslie3d Replace policy: LRU"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/437.leslie3d-134B.trace.txt.gz > "$directory_name/437RCl.txt" &
pids+=($pid10)

# Simulation 11: 444.namd Replace policy: LRU
echo "Running 444.namd Replace policy: LRU"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/444.namd-120B.trace.txt.gz > "$directory_name/444RCl.txt" &
pids+=($pid11)

# Simulation 12: 445.gobmk Replace policy: LRU
echo "Running 445.gobmk Replace policy: LRU"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/445.gobmk-17B.trace.txt.gz > "$directory_name/445RCl.txt" &
pids+=($pid12)

# Simulation 13: 450.soplex Replace policy: LRU
echo "Running 450.soplex Replace policy: LRU"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/450.soplex-247B.trace.txt.gz > "$directory_name/450RCl.txt" &
pids+=($pid13)

# Simulation 14: 453.povray Replace policy: LRU
echo "Running 453.povray Replace policy: LRU"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/453.povray-887B.trace.txt.gz > "$directory_name/453RCl.txt" &
pids+=($pid14)

# Simulation 15: 454.calculix Replace policy: LRU
echo "Running 454.calculix Replace policy: LRU"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/454.calculix-104B.trace.txt.gz > "$directory_name/454RCl.txt" &
pids+=($pid15)

# Simulation 16: 456.hmmer Replace policy: LRU
echo "Running 456.hmmer Replace policy: LRU"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/456.hmmer-191B.trace.txt.gz > "$directory_name/456RCl.txt" &
pids+=($pid16)

# Simulation 17: 458.sjeng Replace policy: LRU
echo "Running 458.sjeng Replace policy: LRU"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/458.sjeng-1088B.trace.txt.gz > "$directory_name/458RCl.txt" &
pids+=($pid17)

# Simulation 18: 459.GemsFDTD Replace policy: LRU
echo "Running 459.GemsFDTD Replace policy: LRU"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/459.GemsFDTD-1169B.trace.txt.gz > "$directory_name/459RCl.txt" &
pids+=($pid18)

# Simulation 19: 462.libquantum Replace policy: LRU
echo "Running 462.libquantum Replace policy: LRU"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/462.libquantum-1343B.trace.txt.gz > "$directory_name/462RCl.txt" &
pids+=($pid19)

# Simulation 20: 464.h264 Replace policy: LRU
echo "Running 464.h264ref Replace policy: LRU"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/464.h264ref-30B.trace.txt.gz > "$directory_name/464RCl.txt" &
pids+=($pid20)

# Simulation 21: 465.tonto Replace policy: LRU
echo "Running 465.tonto Replace policy: LRU"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/465.tonto-1769B.trace.txt.gz > "$directory_name/465RCl.txt" &
pids+=($pid21)

# Simulation 22: 470.lbm Replace policy: LRU
echo "Running 470.lbm Replace policy: LRU"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/470.lbm-1274B.trace.txt.gz > "$directory_name/470RCl.txt" &
pids+=($pid22)

# Simulation 23: 471.omnetpp Replace policy: LRU
echo "Running 471.omnetpp Replace policy: LRU"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/471.omnetpp-188B.trace.txt.gz > "$directory_name/471RCl.txt" &
pids+=($pid23)

# Simulation 24: 473.astar Replace policy: LRU
echo "Running 473.astar Replace policy: LRU"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/473.astar-153B.trace.txt.gz > "$directory_name/473RCl.txt" &
pids+=($pid24)

# Simulation 25: 481.wrf Replace policy: LRU
echo "Running 481.wrf Replace policy: LRU"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/481.wrf-1170B.trace.txt.gz > "$directory_name/481RCl.txt" &
pids+=($pid25)

# Simulation 26: 482.sphinx3 Replace policy: LRU
echo "Running 482.sphinx3 Replace policy: LRU"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/482.sphinx3-1100B.trace.txt.gz > "$directory_name/482RCl.txt" &
pids+=($pid26)

# Simulation 27: 483.xalancbmk Replace policy: LRU
echo "Running 483.xalancbmk Replace policy: LRU"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/483.xalancbmk-127B.trace.txt.gz > "$directory_name/483RCl.txt" &
pids+=($pid27)


# Wait for simulation process to finish
wait $pid1
echo ">>>>>Simulation 1:  400.perlbench Replace policy: LRU"

# Wait for simulation process to finish
wait $pid2
echo ">>>>>Simulation 2:  401.bzip2 Replace policy: LRU"

# Wait for simulation process to finish
wait $pid3
echo ">>>>>Simulation 3:  403.gcc Replace policy: LRU"

# Wait for simulation process to finish
wait $pid4
echo ">>>>>Simulation 4:  410.bwaves Replace policy: LRU"

# Wait for simulation process to finish
wait $pid5
echo ">>>>>Simulation 5:  416.gamess Replace policy: LRU"

# Wait for simulation process to finish
wait $pid6
echo ">>>>>Simulation 6:  429.mcf Replace policy: LRU"

# Wait for simulation process to finish
wait $pid7
echo ">>>>>Simulation 7:  433.milc Replace policy: LRU"

# Wait for simulation process to finish
wait $pid8
echo ">>>>>Simulation 8:  435.gromacs Replace policy: LRU"

# Wait for simulation process to finish
wait $pid9
echo ">>>>>Simulation 9:  436.cactusADM Replace policy: LRU"

# Wait for simulation process to finish
wait $pid10
echo ">>>>>Simulation 10:  437.leslie3d Replace policy: LRU"

# Wait for simulation process to finish
wait $pid11
echo ">>>>>Simulation 11:  444.namd Replace policy: LRU"

# Wait for simulation process to finish
wait $pid12
echo ">>>>>Simulation 12:  445.gobmk Replace policy: LRU"

# Wait for simulation process to finish
wait $pid13
echo ">>>>>Simulation 13:  450.soplex  Replace policy: LRU"

# Wait for simulation process to finish
wait $pid14
echo ">>>>>Simulation 14:  453.povray Replace policy: LRU"

# Wait for simulation process to finish
wait $pid15
echo ">>>>>Simulation 15:  454.calculix Replace policy: LRU"

# Wait for simulation process to finish
wait $pid16
echo ">>>>>Simulation 16:  456.hmmer Replace policy: LRU"

# Wait for simulation process to finish
wait $pid17
echo ">>>>>Simulation 17:  458.sjeng Replace policy: LRU"

# Wait for simulation process to finish
wait $pid18
echo ">>>>>Simulation 18:  459.GemsFDTD Replace policy: LRU"

# Wait for simulation process to finish
wait $pid19
echo ">>>>>Simulation 19:  462.libquantum Replace policy: LRU"

# Wait for simulation process to finish
wait $pid20
echo ">>>>>Simulation 20:  464.h264ref Replace policy: LRU"

# Wait for simulation process to finish
wait $pid21
echo ">>>>>Simulation 21:  465.tonto Replace policy: LRU"

# Wait for simulation process to finish
wait $pid22
echo ">>>>>Simulation 22:  470.lbm Replace policy: LRU"

# Wait for simulation process to finish
wait $pid23
echo ">>>>>Simulation 23:  471.omnetpp Replace policy: LRU"

# Wait for simulation process to finish
wait $pid24
echo ">>>>>Simulation 24:  473.astar Replace policy: LRU"

# Wait for simulation process to finish
wait $pid25
echo ">>>>>Simulation 25:  481.wrf Replace policy: LRU"

# Wait for simulation process to finish
wait $pid26
echo ">>>>>Simulation 26:  482.sphinx3 Replace policy: LRU"

# Wait for simulation process to finish
wait $pid27
echo ">>>>>Simulation 27:  483.xalancbmk Replace policy: LRU"

echo ""
echo "Simulaciones con Replace policy: LRU"
echo ""
echo "Revisar txt en directorio '$directory_name1'"
echo ""
echo ""
echo ""

################################
# Replace policy:    aleatorio #
################################
echo "'''''''''''''''''''''''''''''''''''"
echo "' Tamaño de caché:       '''32kB'''"
echo "' Asociatividad:       8-ways     '"
echo "' Tamaño de bloque:       64kB    '"    
echo "' Política de reemplazo: aleatorio'"
echo "'''''''''''''''''''''''''''''''''''"

# Simulation 28: 400.perlbench Replace policy: aleatoria
echo "Running 400.perlbench-Replace policy: aleatoria"
python3 cache_sim.py -s 32 -a 8 -b 64 -r r -t traces/400.perlbench-41B.trace.txt.gz > "$directory_name/400RCa.txt" &
pid28=$!
pids+=($pid28)

# Simulation 29: 401.bzip2 Replace policy: aleatoria
echo "Running 401.bzip2-Tamaño de caché:16kB"
python3 cache_sim.py -s 32 -a 8 -b 64 -r r -t traces/401.bzip2-226B.trace.txt.gz > "$directory_name/401RCa.txt" &
pid29=$!
pids+=($pid29)

# Simulation 30: 403.gcc Replace policy: aleatoria
echo "Running 403.gcc-Replace policy: aleatoria"
python3 cache_sim.py -s 32 -a 8 -b 64 -r r -t traces/403.gcc-16B.trace.txt.gz > "$directory_name/403RCa.txt" &
pid30=$!
pids+=($pid30)

# Simulation 31: 410.bwaves Replace policy: aleatoria
echo "Running 410.bwaves-Replace policy: aleatoria"
python3 cache_sim.py -s 32 -a 8 -b 64 -r r -t traces/410.bwaves-1963B.trace.txt.gz > "$directory_name/410RCa.txt" &
pid31=$!
pids+=($pid31)

# Simulation 32: 416.gamess Replace policy: aleatoria
echo "Running 416.gamess Replace policy: aleatoria"
python3 cache_sim.py -s 32 -a 8 -b 64 -r r -t traces/416.gamess-875B.trace.txt.gz > "$directory_name/416RCa.txt" &
pids+=($pid32)

# Simulation 33: 429.mcf Replace policy: aleatoria
echo "Running 429.mcf Replace policy: aleatoria"
python3 cache_sim.py -s 32 -a 8 -b 64 -r r -t traces/429.mcf-184B.trace.txt.gz > "$directory_name/429RCa.txt" &
pids+=($pid33)

# Simulation 34: 433.milc Replace policy: aleatoria
echo "Running 433.milc Replace policy: aleatoria"
python3 cache_sim.py -s 32 -a 8 -b 64 -r r -t traces/433.milc-127B.trace.txt.gz > "$directory_name/433RCa.txt" &
pids+=($pid34)

# Simulation 35: 435.gromacs Replace policy: aleatoria
echo "Running 435.gromacs Replace policy: aleatoria"
python3 cache_sim.py -s 32 -a 8 -b 64 -r r -t traces/435.gromacs-111B.trace.txt.gz > "$directory_name/435RCa.txt" &
pids+=($pid35)

# Simulation 36: 436.cactusADM Replace policy: aleatoria
echo "Running 436.cactusADM Replace policy: aleatoria"
python3 cache_sim.py -s 32 -a 8 -b 64 -r r -t traces/436.cactusADM-1804B.trace.txt.gz > "$directory_name/436RCa.txt" &
pids+=($pid36)

# Simulation 37: 437.leslie3d Replace policy: aleatoria
echo "Running 437.leslie3d Replace policy: aleatoria"
python3 cache_sim.py -s 32 -a 8 -b 64 -r r -t traces/437.leslie3d-134B.trace.txt.gz > "$directory_name/437RCa.txt" &
pids+=($pid37)

# Simulation 38: 444.namd Replace policy: aleatoria
echo "Running 444.namd Replace policy: aleatoria"
python3 cache_sim.py -s 32 -a 8 -b 64 -r r -t traces/444.namd-120B.trace.txt.gz > "$directory_name/444RCa.txt" &
pids+=($pid38)

# Simulation 39: 445.gobmk Replace policy: aleatoria
echo "Running 445.gobmk Replace policy: aleatoria"
python3 cache_sim.py -s 32 -a 8 -b 64 -r r -t traces/445.gobmk-17B.trace.txt.gz > "$directory_name/445RCa.txt" &
pids+=($pid39)

# Simulation 40: 450.soplex Replace policy: aleatoria
echo "Running 450.soplex Replace policy: aleatoria"
python3 cache_sim.py -s 32 -a 8 -b 64 -r r -t traces/450.soplex-247B.trace.txt.gz > "$directory_name/450RCa.txt" &
pids+=($pid40)

# Simulation 41: 453.povray Replace policy: aleatoria
echo "Running 453.povray Replace policy: aleatoria"
python3 cache_sim.py -s 32 -a 8 -b 64 -r r -t traces/453.povray-887B.trace.txt.gz > "$directory_name/453RCa.txt" &
pids+=($pid41)

# Simulation 42: 454.calculix Replace policy: aleatoria
echo "Running 454.calculix Replace policy: aleatoria"
python3 cache_sim.py -s 32 -a 8 -b 64 -r r -t traces/454.calculix-104B.trace.txt.gz > "$directory_name/454RCa.txt" &
pids+=($pid42)

# Simulation 43: 456.hmmer Replace policy: aleatoria
echo "Running 456.hmmer Replace policy: aleatoria"
python3 cache_sim.py -s 32 -a 8 -b 64 -r r -t traces/456.hmmer-191B.trace.txt.gz > "$directory_name/456RCa.txt" &
pids+=($pid43)

# Simulation 44: 458.sjeng Replace policy: aleatoria
echo "Running 458.sjeng Replace policy: aleatoria"
python3 cache_sim.py -s 32 -a 8 -b 64 -r r -t traces/458.sjeng-1088B.trace.txt.gz > "$directory_name/458RCa.txt" &
pids+=($pid44)

# Simulation 45: 459.GemsFDTD Replace policy: aleatoria
echo "Running 459.GemsFDTD Replace policy: aleatoria"
python3 cache_sim.py -s 32 -a 8 -b 64 -r r -t traces/459.GemsFDTD-1169B.trace.txt.gz > "$directory_name/459RCa.txt" &
pids+=($pid45)

# Simulation 46: 462.libquantum Replace policy: aleatoria
echo "Running 462.libquantum Replace policy: aleatoria"
python3 cache_sim.py -s 32 -a 8 -b 64 -r r -t traces/462.libquantum-1343B.trace.txt.gz > "$directory_name/462RCa.txt" &
pids+=($pid46)

# Simulation 47: 464.h264 Replace policy: aleatoria
echo "Running 464.h264ref Replace policy: aleatoria"
python3 cache_sim.py -s 32 -a 8 -b 64 -r r -t traces/464.h264ref-30B.trace.txt.gz > "$directory_name/464RCa.txt" &
pids+=($pid47)

# Simulation 48: 465.tonto Replace policy: aleatoria
echo "Running 465.tonto Replace policy: aleatoria"
python3 cache_sim.py -s 32 -a 8 -b 64 -r r -t traces/465.tonto-1769B.trace.txt.gz > "$directory_name/465RCa.txt" &
pids+=($pid48)

# Simulation 49: 470.lbm Replace policy: aleatoria
echo "Running 470.lbm Replace policy: aleatoria"
python3 cache_sim.py -s 32 -a 8 -b 64 -r r -t traces/470.lbm-1274B.trace.txt.gz > "$directory_name/470RCa.txt" &
pids+=($pid49)

# Simulation 50: 471.omnetpp Replace policy: aleatoria
echo "Running 471.omnetpp Replace policy: aleatoria"
python3 cache_sim.py -s 32 -a 8 -b 64 -r r -t traces/471.omnetpp-188B.trace.txt.gz > "$directory_name/471RCa.txt" &
pids+=($pid50)

# Simulation 51: 473.astar Replace policy: aleatoria
echo "Running 473.astar Replace policy: aleatoria"
python3 cache_sim.py -s 32 -a 8 -b 64 -r r -t traces/473.astar-153B.trace.txt.gz > "$directory_name/473RCa.txt" &
pids+=($pid51)

# Simulation 52: 481.wrf Replace policy: aleatoria
echo "Running 481.wrf Replace policy: aleatoria"
python3 cache_sim.py -s 32 -a 8 -b 64 -r r -t traces/481.wrf-1170B.trace.txt.gz > "$directory_name/481RCa.txt" &
pids+=($pid52)

# Simulation 53: 482.sphinx3 Replace policy: aleatoria
echo "Running 482.sphinx3 Replace policy: aleatoria"
python3 cache_sim.py -s 32 -a 8 -b 64 -r r -t traces/482.sphinx3-1100B.trace.txt.gz > "$directory_name/482RCa.txt" &
pids+=($pid53)

# Simulation 54: 483.xalancbmk Replace policy: aleatoria
echo "Running 483.xalancbmk Replace policy: aleatoria"
python3 cache_sim.py -s 32 -a 8 -b 64 -r r -t traces/483.xalancbmk-127B.trace.txt.gz > "$directory_name/483RCa.txt" &
pids+=($pid54)


# Wait for simulation process to finish
wait $pid28
echo ">>>>>Simulation 28:  400.perlbench Replace policy: aleatoria"

# Wait for simulation process to finish
wait $pid29
echo ">>>>>Simulation 29:  401.bzip2 Replace policy: aleatoria"

# Wait for simulation process to finish
wait $pid30
echo ">>>>>Simulation 30:  403.gcc Replace policy: aleatoria"

# Wait for simulation process to finish
wait $pid31
echo ">>>>>Simulation 31:  410.bwaves Replace policy: aleatoria"

# Wait for simulation process to finish
wait $pid32
echo ">>>>>Simulation 32:  416.gamess Replace policy: aleatoria"

# Wait for simulation process to finish
wait $pid33
echo ">>>>>Simulation 33:  429.mcf Replace policy: aleatoria"

# Wait for simulation process to finish
wait $pid34
echo ">>>>>Simulation 34:  433.milc Replace policy: aleatoria"

# Wait for simulation process to finish
wait $pid35
echo ">>>>>Simulation 35:  435.gromacs Replace policy: aleatoria"

# Wait for simulation process to finish
wait $pid36
echo ">>>>>Simulation 36:  436.cactusADM Replace policy: aleatoria"

# Wait for simulation process to finish
wait $pid37
echo ">>>>>Simulation 37:  437.leslie3d Replace policy: aleatoria"

# Wait for simulation process to finish
wait $pid38
echo ">>>>>Simulation 38:  444.namd Replace policy: aleatoria"

# Wait for simulation process to finish
wait $pid39
echo ">>>>>Simulation 39:  445.gobmk Replace policy: aleatoria"

# Wait for simulation process to finish
wait $pid40
echo ">>>>>Simulation 40:  450.soplex  Replace policy: aleatoria"

# Wait for simulation process to finish
wait $pid41
echo ">>>>>Simulation 41:  453.povray Replace policy: aleatoria"

# Wait for simulation process to finish
wait $pid42
echo ">>>>>Simulation 42:  454.calculix Replace policy: aleatoria"

# Wait for simulation process to finish
wait $pid43
echo ">>>>>Simulation 43:  456.hmmer Replace policy: aleatoria"

# Wait for simulation process to finish
wait $pid44
echo ">>>>>Simulation 44:  458.sjeng Replace policy: aleatoria"

# Wait for simulation process to finish
wait $pid45
echo ">>>>>Simulation 45:  459.GemsFDTD Replace policy: aleatoria"

# Wait for simulation process to finish
wait $pid46
echo ">>>>>Simulation 46:  462.libquantum Replace policy: aleatoria"

# Wait for simulation process to finish
wait $pid47
echo ">>>>>Simulation 47:  464.h264ref Replace policy: aleatoria"

# Wait for simulation process to finish
wait $pid48
echo ">>>>>Simulation 48:  465.tonto Replace policy: aleatoria"

# Wait for simulation process to finish
wait $pid49
echo ">>>>>Simulation 49:  470.lbm Replace policy: aleatoria"

# Wait for simulation process to finish
wait $pid50
echo ">>>>>Simulation 50:  471.omnetpp Replace policy: aleatoria"

# Wait for simulation process to finish
wait $pid51
echo ">>>>>Simulation 51:  473.astar Replace policy: aleatoria"

# Wait for simulation process to finish
wait $pid52
echo ">>>>>Simulation 52:  481.wrf Replace policy: aleatoria"

# Wait for simulation process to finish
wait $pid53
echo ">>>>>Simulation 53:  482.sphinx3 Replace policy: aleatoria"

# Wait for simulation process to finish
wait $pid54
echo ">>>>>Simulation 54:  483.xalancbmk Replace policy: aleatoria"
echo ""
echo "Simulaciones con Replace policy: aleatoria"
echo ""
echo "Revisar txt en directorio '$directory_name'"
echo ""
echo ""
echo ""
echo ""

echo "Extractor corriendo"
python3 EXTRACTER_RC.py

echo "Mostrando resultados en excel: "
open Results_RC.xlsx
