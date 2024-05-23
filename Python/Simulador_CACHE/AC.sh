#!/bin/bash

# Create an array to store the simulation process IDs
pids=()
echo "''''''''''''''''''''''''''''''''''''''''''''''''''"
echo "Experimento: variación asociatividad de Caché(AC) "
echo "''''''''''''''''''''''''''''''''''''''''''''''''''"

# Define the directory name where txt result will be stored
directory_name="RESULTS_AC"
# Create the directory
mkdir "$directory_name"

#########################################
# Asociatividad de caché:  mapeo directo#
#########################################
echo "'''''''''''''''''''''''''''''"
echo "' Tamaño de caché:   32kB    "
echo "' Asociatividad:mapeo directo"
echo "' Tamaño de bloque: 64kB    '"    
echo "' Política de reemplazo: LRU'"
echo "'''''''''''''''''''''''''''''"

# Simulation 1: 400.perlbench Asociatividad de caché: mapeo directo
echo "Running 400.perlbench-Asociatividad de caché: mapeo directo"
python3 cache_sim.py -s 32 -a 1 -b 64 -r l -t traces/400.perlbench-41B.trace.txt.gz > "$directory_name/400AC1.txt" &
pid1=$!
pids+=($pid1)

# Simulation 2: 401.bzip2 Asociatividad de caché: mapeo directo
echo "Running 401.bzip2-Asociatividad de caché: mapeo directo"
python3 cache_sim.py -s 32 -a 1 -b 64 -r l -t traces/401.bzip2-226B.trace.txt.gz > "$directory_name/401AC1.txt" &
pid2=$!
pids+=($pid2)

# Simulation 3: 403.gcc Asociatividad de caché: mapeo directo
echo "Running 403.gcc-Asociatividad de caché: mapeo directo"
python3 cache_sim.py -s 32 -a 1 -b 64 -r l -t traces/403.gcc-16B.trace.txt.gz > "$directory_name/403AC1.txt" &
pid3=$!
pids+=($pid3)

# Simulation 4: 410.bwaves Asociatividad de caché: mapeo directo
echo "Running 410.bwaves-Asociatividad de caché: mapeo directo"
python3 cache_sim.py -s 32 -a 1 -b 64 -r l -t traces/410.bwaves-1963B.trace.txt.gz > "$directory_name/410AC1.txt" &
pid4=$!
pids+=($pid4)

# Simulation 5: 416.gamess Asociatividad de caché: mapeo directo
echo "Running 416.gamess Asociatividad de caché: mapeo directo"
python3 cache_sim.py -s 32 -a 1 -b 64 -r l -t traces/416.gamess-875B.trace.txt.gz > "$directory_name/416AC1.txt" &
pids+=($pid5)

# Simulation 6: 429.mcf Asociatividad de caché: mapeo directo
echo "Running 429.mcf Asociatividad de caché: mapeo directo"
python3 cache_sim.py -s 32 -a 1 -b 64 -r l -t traces/429.mcf-184B.trace.txt.gz > "$directory_name/429AC1.txt" &
pids+=($pid6)

# Simulation 7: 433.milc Asociatividad de caché: mapeo directo
echo "Running 433.milc Asociatividad de caché: mapeo directo"
python3 cache_sim.py -s 32 -a 1 -b 64 -r l -t traces/433.milc-127B.trace.txt.gz > "$directory_name/433AC1.txt" &
pids+=($pid7)

# Simulation 8: 435.gromacs Asociatividad de caché: mapeo directo
echo "Running 435.gromacs Asociatividad de caché: mapeo directo"
python3 cache_sim.py -s 32 -a 1 -b 64 -r l -t traces/435.gromacs-111B.trace.txt.gz > "$directory_name/435AC1.txt" &
pids+=($pid8)

# Simulation 9: 436.cactusADM Asociatividad de caché: mapeo directo
echo "Running 436.cactusADM Asociatividad de caché: mapeo directo"
python3 cache_sim.py -s 32 -a 1 -b 64 -r l -t traces/436.cactusADM-1804B.trace.txt.gz > "$directory_name/436AC1.txt" &
pids+=($pid9)

# Simulation 10: 437.leslie3d Asociatividad de caché: mapeo directo
echo "Running 437.leslie3d Asociatividad de caché: mapeo directo"
python3 cache_sim.py -s 32 -a 1 -b 64 -r l -t traces/437.leslie3d-134B.trace.txt.gz > "$directory_name/437AC1.txt" &
pids+=($pid10)

# Simulation 11: 444.namd Asociatividad de caché: mapeo directo
echo "Running 444.namd Asociatividad de caché: mapeo directo"
python3 cache_sim.py -s 32 -a 1 -b 64 -r l -t traces/444.namd-120B.trace.txt.gz > "$directory_name/444AC1.txt" &
pids+=($pid11)

# Simulation 12: 445.gobmk Asociatividad de caché: mapeo directo
echo "Running 445.gobmk Asociatividad de caché: mapeo directo"
python3 cache_sim.py -s 32 -a 1 -b 64 -r l -t traces/445.gobmk-17B.trace.txt.gz > "$directory_name/445AC1.txt" &
pids+=($pid12)

# Simulation 13: 450.soplex Asociatividad de caché: mapeo directo
echo "Running 450.soplex Asociatividad de caché: mapeo directo"
python3 cache_sim.py -s 32 -a 1 -b 64 -r l -t traces/450.soplex-247B.trace.txt.gz > "$directory_name/450AC1.txt" &
pids+=($pid13)

# Simulation 14: 453.povray Asociatividad de caché: mapeo directo
echo "Running 453.povray Asociatividad de caché: mapeo directo"
python3 cache_sim.py -s 32 -a 1 -b 64 -r l -t traces/453.povray-887B.trace.txt.gz > "$directory_name/453AC1.txt" &
pids+=($pid14)

# Simulation 15: 454.calculix Asociatividad de caché: mapeo directo
echo "Running 454.calculix Asociatividad de caché: mapeo directo"
python3 cache_sim.py -s 32 -a 1 -b 64 -r l -t traces/454.calculix-104B.trace.txt.gz > "$directory_name/454AC1.txt" &
pids+=($pid15)

# Simulation 16: 456.hmmer Asociatividad de caché: mapeo directo
echo "Running 456.hmmer Asociatividad de caché: mapeo directo"
python3 cache_sim.py -s 32 -a 1 -b 64 -r l -t traces/456.hmmer-191B.trace.txt.gz > "$directory_name/456AC1.txt" &
pids+=($pid16)

# Simulation 17: 458.sjeng Asociatividad de caché: mapeo directo
echo "Running 458.sjeng Asociatividad de caché: mapeo directo"
python3 cache_sim.py -s 32 -a 1 -b 64 -r l -t traces/458.sjeng-1088B.trace.txt.gz > "$directory_name/458AC1.txt" &
pids+=($pid17)

# Simulation 18: 459.GemsFDTD Asociatividad de caché: mapeo directo
echo "Running 459.GemsFDTD Asociatividad de caché: mapeo directo"
python3 cache_sim.py -s 32 -a 1 -b 64 -r l -t traces/459.GemsFDTD-1169B.trace.txt.gz > "$directory_name/459AC1.txt" &
pids+=($pid18)

# Simulation 19: 462.libquantum Asociatividad de caché: mapeo directo
echo "Running 462.libquantum Asociatividad de caché: mapeo directo"
python3 cache_sim.py -s 32 -a 1 -b 64 -r l -t traces/462.libquantum-1343B.trace.txt.gz > "$directory_name/462AC1.txt" &
pids+=($pid19)

# Simulation 20: 464.h264 Asociatividad de caché: mapeo directo
echo "Running 464.h264ref Asociatividad de caché: mapeo directo"
python3 cache_sim.py -s 32 -a 1 -b 64 -r l -t traces/464.h264ref-30B.trace.txt.gz > "$directory_name/464AC1.txt" &
pids+=($pid20)

# Simulation 21: 465.tonto Asociatividad de caché: mapeo directo
echo "Running 465.tonto Asociatividad de caché: mapeo directo"
python3 cache_sim.py -s 32 -a 1 -b 64 -r l -t traces/465.tonto-1769B.trace.txt.gz > "$directory_name/465AC1.txt" &
pids+=($pid21)

# Simulation 22: 470.lbm Asociatividad de caché: mapeo directo
echo "Running 470.lbm Asociatividad de caché: mapeo directo"
python3 cache_sim.py -s 32 -a 1 -b 64 -r l -t traces/470.lbm-1274B.trace.txt.gz > "$directory_name/470AC1.txt" &
pids+=($pid22)

# Simulation 23: 471.omnetpp Asociatividad de caché: mapeo directo
echo "Running 471.omnetpp Asociatividad de caché: mapeo directo"
python3 cache_sim.py -s 32 -a 1 -b 64 -r l -t traces/471.omnetpp-188B.trace.txt.gz > "$directory_name/471AC1.txt" &
pids+=($pid23)

# Simulation 24: 473.astar Asociatividad de caché: mapeo directo
echo "Running 473.astar Asociatividad de caché: mapeo directo"
python3 cache_sim.py -s 32 -a 1 -b 64 -r l -t traces/473.astar-153B.trace.txt.gz > "$directory_name/473AC1.txt" &
pids+=($pid24)

# Simulation 25: 481.wrf Asociatividad de caché: mapeo directo
echo "Running 481.wrf Asociatividad de caché: mapeo directo"
python3 cache_sim.py -s 32 -a 1 -b 64 -r l -t traces/481.wrf-1170B.trace.txt.gz > "$directory_name/481AC1.txt" &
pids+=($pid25)

# Simulation 26: 482.sphinx3 Asociatividad de caché: mapeo directo
echo "Running 482.sphinx3 Asociatividad de caché: mapeo directo"
python3 cache_sim.py -s 32 -a 1 -b 64 -r l -t traces/482.sphinx3-1100B.trace.txt.gz > "$directory_name/482AC1.txt" &
pids+=($pid26)

# Simulation 27: 483.xalancbmk Asociatividad de caché: mapeo directo
echo "Running 483.xalancbmk Asociatividad de caché: mapeo directo"
python3 cache_sim.py -s 32 -a 1 -b 64 -r l -t traces/483.xalancbmk-127B.trace.txt.gz > "$directory_name/483AC1.txt" &
pids+=($pid27)

# Wait for simulation process to finish
wait $pid1
echo ">>>>>Simulation 1:  400.perlbench Asociatividad de caché: mapeo directo"

# Wait for simulation process to finish
wait $pid2
echo ">>>>>Simulation 2:  401.bzip2 Asociatividad de caché: mapeo directo"

# Wait for simulation process to finish
wait $pid3
echo ">>>>>Simulation 3:  403.gcc Asociatividad de caché: mapeo directo"

# Wait for simulation process to finish
wait $pid4
echo ">>>>>Simulation 4:  410.bwaves Asociatividad de caché: mapeo directo"

# Wait for simulation process to finish
wait $pid5
echo ">>>>>Simulation 5:  416.gamess Asociatividad de caché: mapeo directo"

# Wait for simulation process to finish
wait $pid6
echo ">>>>>Simulation 6:  429.mcf Asociatividad de caché: mapeo directo"

# Wait for simulation process to finish
wait $pid7
echo ">>>>>Simulation 7:  433.milc Asociatividad de caché: mapeo directo"

# Wait for simulation process to finish
wait $pid8
echo ">>>>>Simulation 8:  435.gromacs Asociatividad de caché: mapeo directo"

# Wait for simulation process to finish
wait $pid9
echo ">>>>>Simulation 9:  436.cactusADM Asociatividad de caché: mapeo directo"

# Wait for simulation process to finish
wait $pid10
echo ">>>>>Simulation 10:  437.leslie3d Asociatividad de caché: mapeo directo"

# Wait for simulation process to finish
wait $pid11
echo ">>>>>Simulation 11:  444.namd Asociatividad de caché: mapeo directo"

# Wait for simulation process to finish
wait $pid12
echo ">>>>>Simulation 12:  445.gobmk Asociatividad de caché: mapeo directo"

# Wait for simulation process to finish
wait $pid13
echo ">>>>>Simulation 13:  450.soplex  Asociatividad de caché: mapeo directo"

# Wait for simulation process to finish
wait $pid14
echo ">>>>>Simulation 14:  453.povray Asociatividad de caché: mapeo directo"

# Wait for simulation process to finish
wait $pid15
echo ">>>>>Simulation 15:  454.calculix Asociatividad de caché: mapeo directo"

# Wait for simulation process to finish
wait $pid16
echo ">>>>>Simulation 16:  456.hmmer Asociatividad de caché: mapeo directo"

# Wait for simulation process to finish
wait $pid17
echo ">>>>>Simulation 17:  458.sjeng Asociatividad de caché: mapeo directo"

# Wait for simulation process to finish
wait $pid18
echo ">>>>>Simulation 18:  459.GemsFDTD Asociatividad de caché: mapeo directo"

# Wait for simulation process to finish
wait $pid19
echo ">>>>>Simulation 19:  462.libquantum Asociatividad de caché: mapeo directo"

# Wait for simulation process to finish
wait $pid20
echo ">>>>>Simulation 20:  464.h264ref Asociatividad de caché: mapeo directo"

# Wait for simulation process to finish
wait $pid21
echo ">>>>>Simulation 21:  465.tonto Asociatividad de caché: mapeo directo"

# Wait for simulation process to finish
wait $pid22
echo ">>>>>Simulation 22:  470.lbm Asociatividad de caché: mapeo directo"

# Wait for simulation process to finish
wait $pid23
echo ">>>>>Simulation 23:  471.omnetpp Asociatividad de caché: mapeo directo"

# Wait for simulation process to finish
wait $pid24
echo ">>>>>Simulation 24:  473.astar Asociatividad de caché: mapeo directo"

# Wait for simulation process to finish
wait $pid25
echo ">>>>>Simulation 25:  481.wrf Asociatividad de caché: mapeo directo"

# Wait for simulation process to finish
wait $pid26
echo ">>>>>Simulation 26:  482.sphinx3 Asociatividad de caché: mapeo directo"

# Wait for simulation process to finish
wait $pid27
echo ">>>>>Simulation 27:  483.xalancbmk Asociatividad de caché: mapeo directo"

echo ""
echo "Simulaciones con Asociatividad de caché: mapeo directo"
echo ""
echo "Revisar txt en directorio '$directory_name1'"
echo ""
echo ""
echo ""


#########################################
# Asociatividad de caché:  2-way        #
#########################################
echo "'''''''''''''''''''''''''''''"
echo "' Tamaño de caché:   32kB    "
echo "' Asociatividad:       2-way "
echo "' Tamaño de bloque: 64kB    '"    
echo "' Política de reemplazo: LRU'"
echo "'''''''''''''''''''''''''''''"

# Simulation 28: 400.perlbench Asociatividad de caché: 2-way
echo "Running 400.perlbench-Asociatividad de caché: 2-way"
python3 cache_sim.py -s 32 -a 2 -b 64 -r l -t traces/400.perlbench-41B.trace.txt.gz > "$directory_name/400AC2.txt" &
pid28=$!
pids+=($pid28)

# Simulation 29: 401.bzip2 Asociatividad de caché: 2-way
echo "Running 401.bzip2-Tamaño de caché:16kB"
python3 cache_sim.py -s 32 -a 2 -b 64 -r l -t traces/401.bzip2-226B.trace.txt.gz > "$directory_name/401AC2.txt" &
pid29=$!
pids+=($pid29)

# Simulation 30: 403.gcc Asociatividad de caché: 2-way
echo "Running 403.gcc-Asociatividad de caché: 2-way"
python3 cache_sim.py -s 32 -a 2 -b 64 -r l -t traces/403.gcc-16B.trace.txt.gz > "$directory_name/403AC2.txt" &
pid30=$!
pids+=($pid30)

# Simulation 31: 410.bwaves Asociatividad de caché: 2-way
echo "Running 410.bwaves-Asociatividad de caché: 2-way"
python3 cache_sim.py -s 32 -a 2 -b 64 -r l -t traces/410.bwaves-1963B.trace.txt.gz > "$directory_name/410AC2.txt" &
pid31=$!
pids+=($pid31)

# Simulation 32: 416.gamess Asociatividad de caché: 2-way
echo "Running 416.gamess Asociatividad de caché: 2-way"
python3 cache_sim.py -s 32 -a 2 -b 64 -r l -t traces/416.gamess-875B.trace.txt.gz > "$directory_name/416AC2.txt" &
pids+=($pid32)

# Simulation 33: 429.mcf Asociatividad de caché: 2-way
echo "Running 429.mcf Asociatividad de caché: 2-way"
python3 cache_sim.py -s 32 -a 2 -b 64 -r l -t traces/429.mcf-184B.trace.txt.gz > "$directory_name/429AC2.txt" &
pids+=($pid33)

# Simulation 34: 433.milc Asociatividad de caché: 2-way
echo "Running 433.milc Asociatividad de caché: 2-way"
python3 cache_sim.py -s 32 -a 2 -b 64 -r l -t traces/433.milc-127B.trace.txt.gz > "$directory_name/433AC2.txt" &
pids+=($pid34)

# Simulation 35: 435.gromacs Asociatividad de caché: 2-way
echo "Running 435.gromacs Asociatividad de caché: 2-way"
python3 cache_sim.py -s 32 -a 2 -b 64 -r l -t traces/435.gromacs-111B.trace.txt.gz > "$directory_name/435AC2.txt" &
pids+=($pid35)

# Simulation 36: 436.cactusADM Asociatividad de caché: 2-way
echo "Running 436.cactusADM Asociatividad de caché: 2-way"
python3 cache_sim.py -s 32 -a 2 -b 64 -r l -t traces/436.cactusADM-1804B.trace.txt.gz > "$directory_name/436AC2.txt" &
pids+=($pid36)

# Simulation 37: 437.leslie3d Asociatividad de caché: 2-way
echo "Running 437.leslie3d Asociatividad de caché: 2-way"
python3 cache_sim.py -s 32 -a 2 -b 64 -r l -t traces/437.leslie3d-134B.trace.txt.gz > "$directory_name/437AC2.txt" &
pids+=($pid37)

# Simulation 38: 444.namd Asociatividad de caché: 2-way
echo "Running 444.namd Asociatividad de caché: 2-way"
python3 cache_sim.py -s 32 -a 2 -b 64 -r l -t traces/444.namd-120B.trace.txt.gz > "$directory_name/444AC2.txt" &
pids+=($pid38)

# Simulation 39: 445.gobmk Asociatividad de caché: 2-way
echo "Running 445.gobmk Asociatividad de caché: 2-way"
python3 cache_sim.py -s 32 -a 2 -b 64 -r l -t traces/445.gobmk-17B.trace.txt.gz > "$directory_name/445AC2.txt" &
pids+=($pid39)

# Simulation 40: 450.soplex Asociatividad de caché: 2-way
echo "Running 450.soplex Asociatividad de caché: 2-way"
python3 cache_sim.py -s 32 -a 2 -b 64 -r l -t traces/450.soplex-247B.trace.txt.gz > "$directory_name/450AC2.txt" &
pids+=($pid40)

# Simulation 41: 453.povray Asociatividad de caché: 2-way
echo "Running 453.povray Asociatividad de caché: 2-way"
python3 cache_sim.py -s 32 -a 2 -b 64 -r l -t traces/453.povray-887B.trace.txt.gz > "$directory_name/453AC2.txt" &
pids+=($pid41)

# Simulation 42: 454.calculix Asociatividad de caché: 2-way
echo "Running 454.calculix Asociatividad de caché: 2-way"
python3 cache_sim.py -s 32 -a 2 -b 64 -r l -t traces/454.calculix-104B.trace.txt.gz > "$directory_name/454AC2.txt" &
pids+=($pid42)

# Simulation 43: 456.hmmer Asociatividad de caché: 2-way
echo "Running 456.hmmer Asociatividad de caché: 2-way"
python3 cache_sim.py -s 32 -a 2 -b 64 -r l -t traces/456.hmmer-191B.trace.txt.gz > "$directory_name/456AC2.txt" &
pids+=($pid43)

# Simulation 44: 458.sjeng Asociatividad de caché: 2-way
echo "Running 458.sjeng Asociatividad de caché: 2-way"
python3 cache_sim.py -s 32 -a 2 -b 64 -r l -t traces/458.sjeng-1088B.trace.txt.gz > "$directory_name/458AC2.txt" &
pids+=($pid44)

# Simulation 45: 459.GemsFDTD Asociatividad de caché: 2-way
echo "Running 459.GemsFDTD Asociatividad de caché: 2-way"
python3 cache_sim.py -s 32 -a 2 -b 64 -r l -t traces/459.GemsFDTD-1169B.trace.txt.gz > "$directory_name/459AC2.txt" &
pids+=($pid45)

# Simulation 46: 462.libquantum Asociatividad de caché: 2-way
echo "Running 462.libquantum Asociatividad de caché: 2-way"
python3 cache_sim.py -s 32 -a 2 -b 64 -r l -t traces/462.libquantum-1343B.trace.txt.gz > "$directory_name/462AC2.txt" &
pids+=($pid46)

# Simulation 47: 464.h264 Asociatividad de caché: 2-way
echo "Running 464.h264ref Asociatividad de caché: 2-way"
python3 cache_sim.py -s 32 -a 2 -b 64 -r l -t traces/464.h264ref-30B.trace.txt.gz > "$directory_name/464AC2.txt" &
pids+=($pid47)

# Simulation 48: 465.tonto Asociatividad de caché: 2-way
echo "Running 465.tonto Asociatividad de caché: 2-way"
python3 cache_sim.py -s 32 -a 2 -b 64 -r l -t traces/465.tonto-1769B.trace.txt.gz > "$directory_name/465AC2.txt" &
pids+=($pid48)

# Simulation 49: 470.lbm Asociatividad de caché: 2-way
echo "Running 470.lbm Asociatividad de caché: 2-way"
python3 cache_sim.py -s 32 -a 2 -b 64 -r l -t traces/470.lbm-1274B.trace.txt.gz > "$directory_name/470AC2.txt" &
pids+=($pid49)

# Simulation 50: 471.omnetpp Asociatividad de caché: 2-way
echo "Running 471.omnetpp Asociatividad de caché: 2-way"
python3 cache_sim.py -s 32 -a 2 -b 64 -r l -t traces/471.omnetpp-188B.trace.txt.gz > "$directory_name/471AC2.txt" &
pids+=($pid50)

# Simulation 51: 473.astar Asociatividad de caché: 2-way
echo "Running 473.astar Asociatividad de caché: 2-way"
python3 cache_sim.py -s 32 -a 2 -b 64 -r l -t traces/473.astar-153B.trace.txt.gz > "$directory_name/473AC2.txt" &
pids+=($pid51)

# Simulation 52: 481.wrf Asociatividad de caché: 2-way
echo "Running 481.wrf Asociatividad de caché: 2-way"
python3 cache_sim.py -s 32 -a 2 -b 64 -r l -t traces/481.wrf-1170B.trace.txt.gz > "$directory_name/481AC2.txt" &
pids+=($pid52)

# Simulation 53: 482.sphinx3 Asociatividad de caché: 2-way
echo "Running 482.sphinx3 Asociatividad de caché: 2-way"
python3 cache_sim.py -s 32 -a 2 -b 64 -r l -t traces/482.sphinx3-1100B.trace.txt.gz > "$directory_name/482AC2.txt" &
pids+=($pid53)

# Simulation 54: 483.xalancbmk Asociatividad de caché: 2-way
echo "Running 483.xalancbmk Asociatividad de caché: 2-way"
python3 cache_sim.py -s 32 -a 2 -b 64 -r l -t traces/483.xalancbmk-127B.trace.txt.gz > "$directory_name/483AC2.txt" &
pids+=($pid54)


# Wait for simulation process to finish
wait $pid28
echo ">>>>>Simulation 28:  400.perlbench Asociatividad de caché: 2-way"

# Wait for simulation process to finish
wait $pid29
echo ">>>>>Simulation 29:  401.bzip2 Asociatividad de caché: 2-way"

# Wait for simulation process to finish
wait $pid30
echo ">>>>>Simulation 30:  403.gcc Asociatividad de caché: 2-way"

# Wait for simulation process to finish
wait $pid31
echo ">>>>>Simulation 31:  410.bwaves Asociatividad de caché: 2-way"

# Wait for simulation process to finish
wait $pid32
echo ">>>>>Simulation 32:  416.gamess Asociatividad de caché: 2-way"

# Wait for simulation process to finish
wait $pid33
echo ">>>>>Simulation 33:  429.mcf Asociatividad de caché: 2-way"

# Wait for simulation process to finish
wait $pid34
echo ">>>>>Simulation 34:  433.milc Asociatividad de caché: 2-way"

# Wait for simulation process to finish
wait $pid35
echo ">>>>>Simulation 35:  435.gromacs Asociatividad de caché: 2-way"

# Wait for simulation process to finish
wait $pid36
echo ">>>>>Simulation 36:  436.cactusADM Asociatividad de caché: 2-way"

# Wait for simulation process to finish
wait $pid37
echo ">>>>>Simulation 37:  437.leslie3d Asociatividad de caché: 2-way"

# Wait for simulation process to finish
wait $pid38
echo ">>>>>Simulation 38:  444.namd Asociatividad de caché: 2-way"

# Wait for simulation process to finish
wait $pid39
echo ">>>>>Simulation 39:  445.gobmk Asociatividad de caché: 2-way"

# Wait for simulation process to finish
wait $pid40
echo ">>>>>Simulation 40:  450.soplex  Asociatividad de caché: 2-way"

# Wait for simulation process to finish
wait $pid41
echo ">>>>>Simulation 41:  453.povray Asociatividad de caché: 2-way"

# Wait for simulation process to finish
wait $pid42
echo ">>>>>Simulation 42:  454.calculix Asociatividad de caché: 2-way"

# Wait for simulation process to finish
wait $pid43
echo ">>>>>Simulation 43:  456.hmmer Asociatividad de caché: 2-way"

# Wait for simulation process to finish
wait $pid44
echo ">>>>>Simulation 44:  458.sjeng Asociatividad de caché: 2-way"

# Wait for simulation process to finish
wait $pid45
echo ">>>>>Simulation 45:  459.GemsFDTD Asociatividad de caché: 2-way"

# Wait for simulation process to finish
wait $pid46
echo ">>>>>Simulation 46:  462.libquantum Asociatividad de caché: 2-way"

# Wait for simulation process to finish
wait $pid47
echo ">>>>>Simulation 47:  464.h264ref Asociatividad de caché: 2-way"

# Wait for simulation process to finish
wait $pid48
echo ">>>>>Simulation 48:  465.tonto Asociatividad de caché: 2-way"

# Wait for simulation process to finish
wait $pid49
echo ">>>>>Simulation 49:  470.lbm Asociatividad de caché: 2-way"

# Wait for simulation process to finish
wait $pid50
echo ">>>>>Simulation 50:  471.omnetpp Asociatividad de caché: 2-way"

# Wait for simulation process to finish
wait $pid51
echo ">>>>>Simulation 51:  473.astar Asociatividad de caché: 2-way"

# Wait for simulation process to finish
wait $pid52
echo ">>>>>Simulation 52:  481.wrf Asociatividad de caché: 2-way"

# Wait for simulation process to finish
wait $pid53
echo ">>>>>Simulation 53:  482.sphinx3 Asociatividad de caché: 2-way"

# Wait for simulation process to finish
wait $pid54
echo ">>>>>Simulation 54:  483.xalancbmk Asociatividad de caché: 2-way"
echo ""
echo "Simulaciones con Asociatividad de caché: 2-way"
echo ""
echo "Revisar txt en directorio '$directory_name'"
echo ""
echo ""
echo ""
echo ""

#########################################
# Asociatividad de caché:  4-way        #
#########################################
echo "'''''''''''''''''''''''''''''"
echo "' Tamaño de caché:   32kB    "
echo "' Asociatividad:       4-way "
echo "' Tamaño de bloque: 64kB    '"    
echo "' Política de reemplazo: LRU'"
echo "'''''''''''''''''''''''''''''"

# Simulation 55: 400.perlbench Asociatividad de caché: 4-way
echo "Running 400.perlbench-Asociatividad de caché: 4-way"
python3 cache_sim.py -s 32 -a 4 -b 64 -r l -t traces/400.perlbench-41B.trace.txt.gz > "$directory_name/400AC4.txt" &
pid55=$!
pids+=($pid55)

# Simulation 56: 401.bzip2 Asociatividad de caché: 4-way
echo "Running 401.bzip2-Asociatividad de caché: 4-way"
python3 cache_sim.py -s 32 -a 4 -b 64 -r l -t traces/401.bzip2-226B.trace.txt.gz > "$directory_name/401AC4.txt" &
pid56=$!
pids+=($pid56)

# Simulation 57: 403.gcc Asociatividad de caché: 4-way
echo "Running 403.gcc-Asociatividad de caché: 4-way"
python3 cache_sim.py -s 32 -a 4 -b 64 -r l -t traces/403.gcc-16B.trace.txt.gz > "$directory_name/403AC4.txt" &
pid57=$!
pids+=($pid57)

# Simulation 58: 410.bwaves Asociatividad de caché: 4-way
echo "Running 410.bwaves-Asociatividad de caché: 4-way"
python3 cache_sim.py -s 32 -a 4 -b 64 -r l -t traces/410.bwaves-1963B.trace.txt.gz > "$directory_name/410AC4.txt" &
pid58=$!
pids+=($pid58)

# Simulation 59: 416.gamess Asociatividad de caché: 4-way
echo "Running 416.gamess Asociatividad de caché: 4-way"
python3 cache_sim.py -s 32 -a 4 -b 64 -r l -t traces/416.gamess-875B.trace.txt.gz > "$directory_name/416AC4.txt" &
pids+=($pid59)

# Simulation 60: 429.mcf Asociatividad de caché: 4-way
echo "Running 429.mcf Asociatividad de caché: 4-way"
python3 cache_sim.py -s 32 -a 4 -b 64 -r l -t traces/429.mcf-184B.trace.txt.gz > "$directory_name/429AC4.txt" &
pids+=($pid60)

# Simulation 61: 433.milc Asociatividad de caché: 4-way
echo "Running 433.milc Asociatividad de caché: 4-way"
python3 cache_sim.py -s 32 -a 4 -b 64 -r l -t traces/433.milc-127B.trace.txt.gz > "$directory_name/433AC4.txt" &
pids+=($pid61)

# Simulation 62: 435.gromacs Asociatividad de caché: 4-way
echo "Running 435.gromacs Asociatividad de caché: 4-way"
python3 cache_sim.py -s 32 -a 4 -b 64 -r l -t traces/435.gromacs-111B.trace.txt.gz > "$directory_name/435AC4.txt" &
pids+=($pid62)

# Simulation 63: 436.cactusADM Asociatividad de caché: 4-way
echo "Running 436.cactusADM Asociatividad de caché: 4-way"
python3 cache_sim.py -s 32 -a 4 -b 64 -r l -t traces/436.cactusADM-1804B.trace.txt.gz > "$directory_name/436AC4.txt" &
pids+=($pid63)

# Simulation 64: 437.leslie3d Asociatividad de caché: 4-way
echo "Running 437.leslie3d Asociatividad de caché: 4-way"
python3 cache_sim.py -s 32 -a 4 -b 64 -r l -t traces/437.leslie3d-134B.trace.txt.gz > "$directory_name/437AC4.txt" &
pids+=($pid64)

# Simulation 65: 444.namd Asociatividad de caché: 4-way
echo "Running 444.namd Asociatividad de caché: 4-way"
python3 cache_sim.py -s 32 -a 4 -b 64 -r l -t traces/444.namd-120B.trace.txt.gz > "$directory_name/444AC4.txt" &
pids+=($pid65)

# Simulation 66: 445.gobmk Asociatividad de caché: 4-way
echo "Running 445.gobmk Asociatividad de caché: 4-way"
python3 cache_sim.py -s 32 -a 4 -b 64 -r l -t traces/445.gobmk-17B.trace.txt.gz > "$directory_name/445AC4.txt" &
pids+=($pid66)

# Simulation 67: 450.soplex Asociatividad de caché: 4-way
echo "Running 450.soplex Asociatividad de caché: 4-way"
python3 cache_sim.py -s 32 -a 4 -b 64 -r l -t traces/450.soplex-247B.trace.txt.gz > "$directory_name/450AC4.txt" &
pids+=($pid67)

# Simulation 68: 453.povray Asociatividad de caché: 4-way
echo "Running 453.povray Asociatividad de caché: 4-way"
python3 cache_sim.py -s 32 -a 4 -b 64 -r l -t traces/453.povray-887B.trace.txt.gz > "$directory_name/453AC4.txt" &
pids+=($pid68)

# Simulation 69: 454.calculix Asociatividad de caché: 4-way
echo "Running 454.calculix Asociatividad de caché: 4-way"
python3 cache_sim.py -s 32 -a 4 -b 64 -r l -t traces/454.calculix-104B.trace.txt.gz > "$directory_name/454AC4.txt" &
pids+=($pid69)

# Simulation 70: 456.hmmer Asociatividad de caché: 4-way
echo "Running 456.hmmer Asociatividad de caché: 4-way"
python3 cache_sim.py -s 32 -a 4 -b 64 -r l -t traces/456.hmmer-191B.trace.txt.gz > "$directory_name/456AC4.txt" &
pids+=($pid70)

# Simulation 71: 458.sjeng Asociatividad de caché: 4-way
echo "Running 458.sjeng Asociatividad de caché: 4-way"
python3 cache_sim.py -s 32 -a 4 -b 64 -r l -t traces/458.sjeng-1088B.trace.txt.gz > "$directory_name/458AC4.txt" &
pids+=($pid71)

# Simulation 72: 459.GemsFDTD Asociatividad de caché: 4-way
echo "Running 459.GemsFDTD Asociatividad de caché: 4-way"
python3 cache_sim.py -s 32 -a 4 -b 64 -r l -t traces/459.GemsFDTD-1169B.trace.txt.gz > "$directory_name/459AC4.txt" &
pids+=($pid72)

# Simulation 73: 462.libquantum Asociatividad de caché: 4-way
echo "Running 462.libquantum Asociatividad de caché: 4-way"
python3 cache_sim.py -s 32 -a 4 -b 64 -r l -t traces/462.libquantum-1343B.trace.txt.gz > "$directory_name/462AC4.txt" &
pids+=($pid73)

# Simulation 74: 464.h264 Asociatividad de caché: 4-way
echo "Running 464.h264ref Asociatividad de caché: 4-way"
python3 cache_sim.py -s 32 -a 4 -b 64 -r l -t traces/464.h264ref-30B.trace.txt.gz > "$directory_name/464AC4.txt" &
pids+=($pid74)

# Simulation 75: 465.tonto Asociatividad de caché: 4-way
echo "Running 465.tonto Asociatividad de caché: 4-way"
python3 cache_sim.py -s 32 -a 4 -b 64 -r l -t traces/465.tonto-1769B.trace.txt.gz > "$directory_name/465AC4.txt" &
pids+=($pid75)

# Simulation 76: 470.lbm Asociatividad de caché: 4-way
echo "Running 470.lbm Asociatividad de caché: 4-way"
python3 cache_sim.py -s 32 -a 4 -b 64 -r l -t traces/470.lbm-1274B.trace.txt.gz > "$directory_name/470AC4.txt" &
pids+=($pid76)

# Simulation 77: 471.omnetpp Asociatividad de caché: 4-way
echo "Running 471.omnetpp Asociatividad de caché: 4-way"
python3 cache_sim.py -s 32 -a 4 -b 64 -r l -t traces/471.omnetpp-188B.trace.txt.gz > "$directory_name/471AC4.txt" &
pids+=($pid77)

# Simulation 78: 473.astar Asociatividad de caché: 4-way
echo "Running 473.astar Asociatividad de caché: 4-way"
python3 cache_sim.py -s 32 -a 4 -b 64 -r l -t traces/473.astar-153B.trace.txt.gz > "$directory_name/473AC4.txt" &
pids+=($pid78)

# Simulation 79: 481.wrf Asociatividad de caché: 4-way
echo "Running 481.wrf Asociatividad de caché: 4-way"
python3 cache_sim.py -s 32 -a 4 -b 64 -r l -t traces/481.wrf-1170B.trace.txt.gz > "$directory_name/481AC4.txt" &
pids+=($pid79)

# Simulation 80: 482.sphinx3 Asociatividad de caché: 4-way
echo "Running 482.sphinx3 Asociatividad de caché: 4-way"
python3 cache_sim.py -s 32 -a 4 -b 64 -r l -t traces/482.sphinx3-1100B.trace.txt.gz > "$directory_name/482AC4.txt" &
pids+=($pid80)

# Simulation 81: 483.xalancbmk Asociatividad de caché: 4-way
echo "Running 483.xalancbmk Asociatividad de caché: 4-way"
python3 cache_sim.py -s 32 -a 4 -b 64 -r l -t traces/483.xalancbmk-127B.trace.txt.gz > "$directory_name/483AC4.txt" &
pids+=($pid81)


# Wait for simulation process to finish
wait $pid55
echo ">>>>>Simulation 55:  400.perlbench Asociatividad de caché: 4-way"

# Wait for simulation process to finish
wait $pid56
echo ">>>>>Simulation 56:  401.bzip2 Asociatividad de caché: 4-way"

# Wait for simulation process to finish
wait $pid57
echo ">>>>>Simulation 57:  403.gcc Asociatividad de caché: 4-way"

# Wait for simulation process to finish
wait $pid58
echo ">>>>>Simulation 58:  410.bwaves Asociatividad de caché: 4-way"

# Wait for simulation process to finish
wait $pid59
echo ">>>>>Simulation 59:  416.gamess Asociatividad de caché: 4-way"

# Wait for simulation process to finish
wait $pid60
echo ">>>>>Simulation 60:  429.mcf Asociatividad de caché: 4-way"

# Wait for simulation process to finish
wait $pid61
echo ">>>>>Simulation 61:  433.milc Asociatividad de caché: 4-way"

# Wait for simulation process to finish
wait $pid62
echo ">>>>>Simulation 62:  435.gromacs Asociatividad de caché: 4-way"

# Wait for simulation process to finish
wait $pid63
echo ">>>>>Simulation 63:  436.cactusADM Asociatividad de caché: 4-way"

# Wait for simulation process to finish
wait $pid64
echo ">>>>>Simulation 64:  437.leslie3d Asociatividad de caché: 4-way"

# Wait for simulation process to finish
wait $pid65
echo ">>>>>Simulation 65:  444.namd Asociatividad de caché: 4-way"

# Wait for simulation process to finish
wait $pid66
echo ">>>>>Simulation 66:  445.gobmk Asociatividad de caché: 4-way"

# Wait for simulation process to finish
wait $pid67
echo ">>>>>Simulation 67:  450.soplex  Asociatividad de caché: 4-way"

# Wait for simulation process to finish
wait $pid68
echo ">>>>>Simulation 68:  453.povray Asociatividad de caché: 4-way"

# Wait for simulation process to finish
wait $pid69
echo ">>>>>Simulation 69:  454.calculix Asociatividad de caché: 4-way"

# Wait for simulation process to finish
wait $pid70
echo ">>>>>Simulation 70:  456.hmmer Asociatividad de caché: 4-way"

# Wait for simulation process to finish
wait $pid71
echo ">>>>>Simulation 71:  458.sjeng Asociatividad de caché: 4-way"

# Wait for simulation process to finish
wait $pid72
echo ">>>>>Simulation 72:  459.GemsFDTD Asociatividad de caché: 4-way"

# Wait for simulation process to finish
wait $pid73
echo ">>>>>Simulation 73:  462.libquantum Asociatividad de caché: 4-way"

# Wait for simulation process to finish
wait $pid74
echo ">>>>>Simulation 74:  464.h264ref Asociatividad de caché: 4-way"

# Wait for simulation process to finish
wait $pid75
echo ">>>>>Simulation 75:  465.tonto Asociatividad de caché: 4-way"

# Wait for simulation process to finish
wait $pid76
echo ">>>>>Simulation 76:  470.lbm Asociatividad de caché: 4-way"

# Wait for simulation process to finish
wait $pid77
echo ">>>>>Simulation 77:  471.omnetpp Asociatividad de caché: 4-way"

# Wait for simulation process to finish
wait $pid78
echo ">>>>>Simulation 78:  473.astar Asociatividad de caché: 4-way"

# Wait for simulation process to finish
wait $pid79
echo ">>>>>Simulation 79:  481.wrf Asociatividad de caché: 4-way"

# Wait for simulation process to finish
wait $pid80
echo ">>>>>Simulation 80:  482.sphinx3 Asociatividad de caché: 4-way"

# Wait for simulation process to finish
wait $pid81
echo ">>>>>Simulation 81:  483.xalancbmk Asociatividad de caché: 4-way"
echo ""
echo "Simulaciones con Asociatividad de caché: 4-way"
echo ""
echo "Revisar txt en directorio '$directory_name'"
echo ""
echo ""
echo ""

#########################################
# Asociatividad de caché:  8-way        #
#########################################
echo "'''''''''''''''''''''''''''''"
echo "' Tamaño de caché:   32kB   '"
echo "' Asociatividad:       8-way'"
echo "' Tamaño de bloque: 64kB    '"    
echo "' Política de reemplazo: LRU'"
echo "'''''''''''''''''''''''''''''"

# Simulation 82: 400.perlbench Asociatividad de caché: 8-way
echo "Running 400.perlbench-Asociatividad de caché: 8-way"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/400.perlbench-41B.trace.txt.gz > "$directory_name/400AC8.txt" &
pid82=$!
pids+=($pid82)

# Simulation 83: 401.bzip2 Asociatividad de caché: 8-way
echo "Running 401.bzip2-Asociatividad de caché: 8-way"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/401.bzip2-226B.trace.txt.gz > "$directory_name/401AC8.txt" &
pid83=$!
pids+=($pid83)

# Simulation 84: 403.gcc Asociatividad de caché: 8-way
echo "Running 403.gcc-Asociatividad de caché: 8-way"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/403.gcc-16B.trace.txt.gz > "$directory_name/403AC8.txt" &
pid84=$!
pids+=($pid84)

# Simulation 85: 410.bwaves Asociatividad de caché: 8-way
echo "Running 410.bwaves-Asociatividad de caché: 8-way"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/410.bwaves-1963B.trace.txt.gz > "$directory_name/410AC8.txt" &
pid85=$!
pids+=($pid85)

# Simulation 86: 416.gamess Asociatividad de caché: 8-way
echo "Running 416.gamess Asociatividad de caché: 8-way"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/416.gamess-875B.trace.txt.gz > "$directory_name/416AC8.txt" &
pids+=($pid86)

# Simulation 87: 429.mcf Asociatividad de caché: 8-way
echo "Running 429.mcf Asociatividad de caché: 8-way"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/429.mcf-184B.trace.txt.gz > "$directory_name/429AC8.txt" &
pids+=($pid87)

# Simulation 88: 433.milc Asociatividad de caché: 8-way
echo "Running 433.milc Asociatividad de caché: 8-way"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/433.milc-127B.trace.txt.gz > "$directory_name/433AC8.txt" &
pids+=($pid88)

# Simulation 89: 435.gromacs Asociatividad de caché: 8-way
echo "Running 435.gromacs Asociatividad de caché: 8-way"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/435.gromacs-111B.trace.txt.gz > "$directory_name/435AC8.txt" &
pids+=($pid89)

# Simulation 90: 436.cactusADM Asociatividad de caché: 8-way
echo "Running 436.cactusADM Asociatividad de caché: 8-way"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/436.cactusADM-1804B.trace.txt.gz > "$directory_name/436AC8.txt" &
pids+=($pid90)

# Simulation 91: 437.leslie3d Asociatividad de caché: 8-way
echo "Running 437.leslie3d Asociatividad de caché: 8-way"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/437.leslie3d-134B.trace.txt.gz > "$directory_name/437AC8.txt" &
pids+=($pid91)

# Simulation 92: 444.namd Asociatividad de caché: 8-way
echo "Running 444.namd Asociatividad de caché: 8-way"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/444.namd-120B.trace.txt.gz > "$directory_name/444AC8.txt" &
pids+=($pid92)

# Simulation 93: 445.gobmk Asociatividad de caché: 8-way
echo "Running 445.gobmk Asociatividad de caché: 8-way"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/445.gobmk-17B.trace.txt.gz > "$directory_name/445AC8.txt" &
pids+=($pid93)

# Simulation 94: 450.soplex Asociatividad de caché: 8-way
echo "Running 450.soplex Asociatividad de caché: 8-way"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/450.soplex-247B.trace.txt.gz > "$directory_name/450AC8.txt" &
pids+=($pid94)

# Simulation 95: 453.povray Asociatividad de caché: 8-way
echo "Running 453.povray Asociatividad de caché: 8-way"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/453.povray-887B.trace.txt.gz > "$directory_name/453AC8.txt" &
pids+=($pid95)

# Simulation 96: 454.calculix Asociatividad de caché: 8-way
echo "Running 454.calculix Asociatividad de caché: 8-way"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/454.calculix-104B.trace.txt.gz > "$directory_name/454AC8.txt" &
pids+=($pid96)

# Simulation 97: 456.hmmer Asociatividad de caché: 8-way
echo "Running 456.hmmer Asociatividad de caché: 8-way"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/456.hmmer-191B.trace.txt.gz > "$directory_name/456AC8.txt" &
pids+=($pid97)

# Simulation 98: 458.sjeng Asociatividad de caché: 8-way
echo "Running 458.sjeng Asociatividad de caché: 8-way"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/458.sjeng-1088B.trace.txt.gz > "$directory_name/458AC8.txt" &
pids+=($pid98)

# Simulation 99: 459.GemsFDTD Asociatividad de caché: 8-way
echo "Running 459.GemsFDTD Asociatividad de caché: 8-way"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/459.GemsFDTD-1169B.trace.txt.gz > "$directory_name/459AC8.txt" &
pids+=($pid99)

# Simulation 100: 462.libquantum Asociatividad de caché: 8-way
echo "Running 462.libquantum Asociatividad de caché: 8-way"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/462.libquantum-1343B.trace.txt.gz > "$directory_name/462AC8.txt" &
pids+=($pid100)

# Simulation 101: 464.h264 Asociatividad de caché: 8-way
echo "Running 464.h264ref Asociatividad de caché: 8-way"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/464.h264ref-30B.trace.txt.gz > "$directory_name/464AC8.txt" &
pids+=($pid101)

# Simulation 102: 465.tonto Asociatividad de caché: 8-way
echo "Running 465.tonto Asociatividad de caché: 8-way"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/465.tonto-1769B.trace.txt.gz > "$directory_name/465AC8.txt" &
pids+=($pid102)

# Simulation 103: 470.lbm Asociatividad de caché: 8-way
echo "Running 470.lbm Asociatividad de caché: 8-way"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/470.lbm-1274B.trace.txt.gz > "$directory_name/470AC8.txt" &
pids+=($pid103)

# Simulation 104: 471.omnetpp Asociatividad de caché: 8-way
echo "Running 471.omnetpp Asociatividad de caché: 8-way"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/471.omnetpp-188B.trace.txt.gz > "$directory_name/471AC8.txt" &
pids+=($pid104)

# Simulation 105: 473.astar Asociatividad de caché: 8-way
echo "Running 473.astar Asociatividad de caché: 8-way"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/473.astar-153B.trace.txt.gz > "$directory_name/473AC8.txt" &
pids+=($pid105)

# Simulation 106: 481.wrf Asociatividad de caché: 8-way
echo "Running 481.wrf Asociatividad de caché: 8-way"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/481.wrf-1170B.trace.txt.gz > "$directory_name/481AC8.txt" &
pids+=($pid106)

# Simulation 107: 482.sphinx3 Asociatividad de caché: 8-way
echo "Running 482.sphinx3 Asociatividad de caché: 8-way"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/482.sphinx3-1100B.trace.txt.gz > "$directory_name/482AC8.txt" &
pids+=($pid107)

# Simulation 108: 483.xalancbmk Asociatividad de caché: 8-way
echo "Running 483.xalancbmk Asociatividad de caché: 8-way"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/483.xalancbmk-127B.trace.txt.gz > "$directory_name/483AC8.txt" &
pids+=($pid108)

# Wait for simulation process to finish
wait $pid82
echo ">>>>>Simulation 82:  400.perlbench Asociatividad de caché: 8-way"

# Wait for simulation process to finish
wait $pid83
echo ">>>>>Simulation 83:  401.bzip2 Asociatividad de caché: 8-way"

# Wait for simulation process to finish
wait $pid84
echo ">>>>>Simulation 84:  403.gcc Asociatividad de caché: 8-way"

# Wait for simulation process to finish
wait $pid85
echo ">>>>>Simulation 85:  410.bwaves Asociatividad de caché: 8-way"

# Wait for simulation process to finish
wait $pid86
echo ">>>>>Simulation 86:  416.gamess Asociatividad de caché: 8-way"

# Wait for simulation process to finish
wait $pid87
echo ">>>>>Simulation 87:  429.mcf Asociatividad de caché: 8-way"

# Wait for simulation process to finish
wait $pid88
echo ">>>>>Simulation 88:  433.milc Asociatividad de caché: 8-way"

# Wait for simulation process to finish
wait $pid89
echo ">>>>>Simulation 89:  435.gromacs Asociatividad de caché: 8-way"

# Wait for simulation process to finish
wait $pid90
echo ">>>>>Simulation 90:  436.cactusADM Asociatividad de caché: 8-way"

# Wait for simulation process to finish
wait $pid91
echo ">>>>>Simulation 91:  437.leslie3d Asociatividad de caché: 8-way"

# Wait for simulation process to finish
wait $pid92
echo ">>>>>Simulation 92:  444.namd Asociatividad de caché: 8-way"

# Wait for simulation process to finish
wait $pid93
echo ">>>>>Simulation 93:  445.gobmk Asociatividad de caché: 8-way"

# Wait for simulation process to finish
wait $pid94
echo ">>>>>Simulation 94:  450.soplex  Asociatividad de caché: 8-way"

# Wait for simulation process to finish
wait $pid95
echo ">>>>>Simulation 95:  453.povray Asociatividad de caché: 8-way"

# Wait for simulation process to finish
wait $pid96
echo ">>>>>Simulation 96:  454.calculix Asociatividad de caché: 8-way"

# Wait for simulation process to finish
wait $pid97
echo ">>>>>Simulation 97:  456.hmmer Asociatividad de caché: 8-way"

# Wait for simulation process to finish
wait $pid98
echo ">>>>>Simulation 98:  458.sjeng Asociatividad de caché: 8-way"

# Wait for simulation process to finish
wait $pid99
echo ">>>>>Simulation 99:  459.GemsFDTD Asociatividad de caché: 8-way"

# Wait for simulation process to finish
wait $pid100
echo ">>>>>Simulation 100:  462.libquantum Asociatividad de caché: 8-way"

# Wait for simulation process to finish
wait $pid101
echo ">>>>>Simulation 101:  464.h264ref Asociatividad de caché: 8-way"

# Wait for simulation process to finish
wait $pid102
echo ">>>>>Simulation 102:  465.tonto Asociatividad de caché: 8-way"

# Wait for simulation process to finish
wait $pid103
echo ">>>>>Simulation 103:  470.lbm Asociatividad de caché: 8-way"

# Wait for simulation process to finish
wait $pid104
echo ">>>>>Simulation 104:  471.omnetpp Asociatividad de caché: 8-way"

# Wait for simulation process to finish
wait $pid105
echo ">>>>>Simulation 105:  473.astar Asociatividad de caché: 8-way"

# Wait for simulation process to finish
wait $pid106
echo ">>>>>Simulation 106:  481.wrf Asociatividad de caché: 8-way"

# Wait for simulation process to finish
wait $pid107
echo ">>>>>Simulation 107:  482.sphinx3 Asociatividad de caché: 8-way"

# Wait for simulation process to finish
wait $pid108
echo ">>>>>Simulation 108:  483.xalancbmk Asociatividad de caché: 8-way"
echo ""
echo "Simulaciones con Asociatividad de caché: 8-way: "
echo ""
echo "Revisar txt en directorio '$directory_name'"
echo ""
echo ""
echo ""

#########################################
# Asociatividad de caché:  16-way        #
#########################################
echo "'''''''''''''''''''''''''''''"
echo "' Tamaño de caché:   32kB   '"
echo "' Asociatividad:      16-way'"
echo "' Tamaño de bloque: 64kB    '"    
echo "' Política de reemplazo: LRU'"
echo "'''''''''''''''''''''''''''''"

# Simulation 109: 400.perlbench Asociatividad de caché: 16-way
echo "Running 400.perlbench-Asociatividad de caché: 16-way"
python3 cache_sim.py -s 32 -a 16 -b 64 -r l -t traces/400.perlbench-41B.trace.txt.gz > "$directory_name/400AC16.txt" &
pid109=$!
pids+=($pid109)

# Simulation 110: 401.bzip2 Asociatividad de caché: 16-way
echo "Running 401.bzip2-Asociatividad de caché: 16-way"
python3 cache_sim.py -s 32 -a 16 -b 64 -r l -t traces/401.bzip2-226B.trace.txt.gz > "$directory_name/401AC16.txt" &
pid110=$!
pids+=($pid110)

# Simulation 111: 403.gcc Asociatividad de caché: 16-way
echo "Running 403.gcc-Asociatividad de caché: 16-way"
python3 cache_sim.py -s 32 -a 16 -b 64 -r l -t traces/403.gcc-16B.trace.txt.gz > "$directory_name/403AC16.txt" &
pid111=$!
pids+=($pid111)

# Simulation 112: 410.bwaves Asociatividad de caché: 16-way
echo "Running 410.bwaves-Asociatividad de caché: 16-way"
python3 cache_sim.py -s 32 -a 16 -b 64 -r l -t traces/410.bwaves-1963B.trace.txt.gz > "$directory_name/410AC16.txt" &
pid112=$!
pids+=($pid112)

# Simulation 113: 416.gamess Asociatividad de caché: 16-way
echo "Running 416.gamess Asociatividad de caché: 16-way"
python3 cache_sim.py -s 32 -a 16 -b 64 -r l -t traces/416.gamess-875B.trace.txt.gz > "$directory_name/416AC16.txt" &
pids+=($pid113)

# Simulation 114: 429.mcf Asociatividad de caché: 16-way
echo "Running 429.mcf Asociatividad de caché: 16-way"
python3 cache_sim.py -s 32 -a 16 -b 64 -r l -t traces/429.mcf-184B.trace.txt.gz > "$directory_name/429AC16.txt" &
pids+=($pid114)

# Simulation 115: 433.milc Asociatividad de caché: 16-way
echo "Running 433.milc Asociatividad de caché: 16-way"
python3 cache_sim.py -s 32 -a 16 -b 64 -r l -t traces/433.milc-127B.trace.txt.gz > "$directory_name/433AC16.txt" &
pids+=($pid115)

# Simulation 116: 435.gromacs Asociatividad de caché: 16-way
echo "Running 435.gromacs Asociatividad de caché: 16-way"
python3 cache_sim.py -s 32 -a 16 -b 64 -r l -t traces/435.gromacs-111B.trace.txt.gz > "$directory_name/435AC16.txt" &
pids+=($pid116)

# Simulation 117: 436.cactusADM Asociatividad de caché: 16-way
echo "Running 436.cactusADM Asociatividad de caché: 16-way"
python3 cache_sim.py -s 32 -a 16 -b 64 -r l -t traces/436.cactusADM-1804B.trace.txt.gz > "$directory_name/436AC16.txt" &
pids+=($pid117)

# Simulation 118: 437.leslie3d Asociatividad de caché: 16-way
echo "Running 437.leslie3d Asociatividad de caché: 16-way"
python3 cache_sim.py -s 32 -a 16 -b 64 -r l -t traces/437.leslie3d-134B.trace.txt.gz > "$directory_name/437AC16.txt" &
pids+=($pid118)

# Simulation 119: 444.namd Asociatividad de caché: 16-way
echo "Running 444.namd Asociatividad de caché: 16-way"
python3 cache_sim.py -s 32 -a 16 -b 64 -r l -t traces/444.namd-120B.trace.txt.gz > "$directory_name/444AC16.txt" &
pids+=($pid119)

# Simulation 120: 445.gobmk Asociatividad de caché: 16-way
echo "Running 445.gobmk Asociatividad de caché: 16-way"
python3 cache_sim.py -s 32 -a 16 -b 64 -r l -t traces/445.gobmk-17B.trace.txt.gz > "$directory_name/445AC16.txt" &
pids+=($pid120)

# Simulation 121: 450.soplex Asociatividad de caché: 16-way
echo "Running 450.soplex Asociatividad de caché: 16-way"
python3 cache_sim.py -s 32 -a 16 -b 64 -r l -t traces/450.soplex-247B.trace.txt.gz > "$directory_name/450AC16.txt" &
pids+=($pid121)

# Simulation 122: 453.povray Asociatividad de caché: 16-way
echo "Running 453.povray Asociatividad de caché: 16-way"
python3 cache_sim.py -s 32 -a 16 -b 64 -r l -t traces/453.povray-887B.trace.txt.gz > "$directory_name/453AC16.txt" &
pids+=($pid122)

# Simulation 123: 454.calculix Asociatividad de caché: 16-way
echo "Running 454.calculix Asociatividad de caché: 16-way"
python3 cache_sim.py -s 32 -a 16 -b 64 -r l -t traces/454.calculix-104B.trace.txt.gz > "$directory_name/454AC16.txt" &
pids+=($pid123)

# Simulation 124: 456.hmmer Asociatividad de caché: 16-way
echo "Running 456.hmmer Asociatividad de caché: 16-way"
python3 cache_sim.py -s 32 -a 16 -b 64 -r l -t traces/456.hmmer-191B.trace.txt.gz > "$directory_name/456AC16.txt" &
pids+=($pid124)

# Simulation 125: 458.sjeng Asociatividad de caché: 16-way
echo "Running 458.sjeng Asociatividad de caché: 16-way"
python3 cache_sim.py -s 32 -a 16 -b 64 -r l -t traces/458.sjeng-1088B.trace.txt.gz > "$directory_name/458AC16.txt" &
pids+=($pid125)

# Simulation 126: 459.GemsFDTD Asociatividad de caché: 16-way
echo "Running 459.GemsFDTD Asociatividad de caché: 16-way"
python3 cache_sim.py -s 32 -a 16 -b 64 -r l -t traces/459.GemsFDTD-1169B.trace.txt.gz > "$directory_name/459AC16.txt" &
pids+=($pid126)

# Simulation 127: 462.libquantum Asociatividad de caché: 16-way
echo "Running 462.libquantum Asociatividad de caché: 16-way"
python3 cache_sim.py -s 32 -a 16 -b 64 -r l -t traces/462.libquantum-1343B.trace.txt.gz > "$directory_name/462AC16.txt" &
pids+=($pid127)

# Simulation 128: 464.h264 Asociatividad de caché: 16-way
echo "Running 464.h264ref Asociatividad de caché: 16-way"
python3 cache_sim.py -s 32 -a 16 -b 64 -r l -t traces/464.h264ref-30B.trace.txt.gz > "$directory_name/464AC16.txt" &
pids+=($pid128)

# Simulation 129: 465.tonto Asociatividad de caché: 16-way
echo "Running 465.tonto Asociatividad de caché: 16-way"
python3 cache_sim.py -s 32 -a 16 -b 64 -r l -t traces/465.tonto-1769B.trace.txt.gz > "$directory_name/465AC16.txt" &
pids+=($pid129)

# Simulation 130: 470.lbm Asociatividad de caché: 16-way
echo "Running 470.lbm Asociatividad de caché: 16-way"
python3 cache_sim.py -s 32 -a 16 -b 64 -r l -t traces/470.lbm-1274B.trace.txt.gz > "$directory_name/470AC16.txt" &
pids+=($pid130)

# Simulation 131: 471.omnetpp Asociatividad de caché: 16-way
echo "Running 471.omnetpp Asociatividad de caché: 16-way"
python3 cache_sim.py -s 32 -a 16 -b 64 -r l -t traces/471.omnetpp-188B.trace.txt.gz > "$directory_name/471AC16.txt" &
pids+=($pid131)

# Simulation 132: 473.astar Asociatividad de caché: 16-way
echo "Running 473.astar Asociatividad de caché: 16-way"
python3 cache_sim.py -s 32 -a 16 -b 64 -r l -t traces/473.astar-153B.trace.txt.gz > "$directory_name/473AC16.txt" &
pids+=($pid132)

# Simulation 133: 481.wrf Asociatividad de caché: 16-way
echo "Running 481.wrf Asociatividad de caché: 16-way"
python3 cache_sim.py -s 32 -a 16 -b 64 -r l -t traces/481.wrf-1170B.trace.txt.gz > "$directory_name/481AC16.txt" &
pids+=($pid133)

# Simulation 134: 482.sphinx3 Asociatividad de caché: 16-way
echo "Running 482.sphinx3 Asociatividad de caché: 16-way"
python3 cache_sim.py -s 32 -a 16 -b 64 -r l -t traces/482.sphinx3-1100B.trace.txt.gz > "$directory_name/482AC16.txt" &
pids+=($pid134)

# Simulation 135: 483.xalancbmk Asociatividad de caché: 16-way
echo "Running 483.xalancbmk Asociatividad de caché: 16-way"
python3 cache_sim.py -s 32 -a 16 -b 64 -r l -t traces/483.xalancbmk-127B.trace.txt.gz > "$directory_name/483AC16.txt" &
pids+=($pid135)

# Wait for simulation process to finish
wait $pid109
echo ">>>>>Simulation 109:  400.perlbench Asociatividad de caché: 16-way"

# Wait for simulation process to finish
wait $pid110
echo ">>>>>Simulation 110:  401.bzip2 Asociatividad de caché: 16-way"

# Wait for simulation process to finish
wait $pid111
echo ">>>>>Simulation 111:  403.gcc Asociatividad de caché: 16-way"

# Wait for simulation process to finish
wait $pid112
echo ">>>>>Simulation 112:  410.bwaves Asociatividad de caché: 16-way"

# Wait for simulation process to finish
wait $pid113
echo ">>>>>Simulation 113:  416.gamess Asociatividad de caché: 16-way"

# Wait for simulation process to finish
wait $pid114
echo ">>>>>Simulation 114:  429.mcf Asociatividad de caché: 16-way"

# Wait for simulation process to finish
wait $pid115
echo ">>>>>Simulation 115:  433.milc Asociatividad de caché: 16-way"

# Wait for simulation process to finish
wait $pid116
echo ">>>>>Simulation 116:  435.gromacs Asociatividad de caché: 16-way"

# Wait for simulation process to finish
wait $pid117
echo ">>>>>Simulation 117:  436.cactusADM Asociatividad de caché: 16-way"

# Wait for simulation process to finish
wait $pid118
echo ">>>>>Simulation 118:  437.leslie3d Asociatividad de caché: 16-way"

# Wait for simulation process to finish
wait $pid119
echo ">>>>>Simulation 119:  444.namd Asociatividad de caché: 16-way"

# Wait for simulation process to finish
wait $pid120
echo ">>>>>Simulation 120:  445.gobmk Asociatividad de caché: 16-way"

# Wait for simulation process to finish
wait $pid121
echo ">>>>>Simulation 121:  450.soplex  Asociatividad de caché: 16-way"

# Wait for simulation process to finish
wait $pid122
echo ">>>>>Simulation 122:  453.povray Asociatividad de caché: 16-way"

# Wait for simulation process to finish
wait $pid123
echo ">>>>>Simulation 123:  454.calculix Asociatividad de caché: 16-way"

# Wait for simulation process to finish
wait $pid124
echo ">>>>>Simulation 124:  456.hmmer Asociatividad de caché: 16-way"

# Wait for simulation process to finish
wait $pid125
echo ">>>>>Simulation 125:  458.sjeng Asociatividad de caché: 16-way"

# Wait for simulation process to finish
wait $pid126
echo ">>>>>Simulation 126:  459.GemsFDTD Asociatividad de caché: 16-way"

# Wait for simulation process to finish
wait $pid127
echo ">>>>>Simulation 127:  462.libquantum Asociatividad de caché: 16-way"

# Wait for simulation process to finish
wait $pid128
echo ">>>>>Simulation 128:  464.h264ref Asociatividad de caché: 16-way"

# Wait for simulation process to finish
wait $pid129
echo ">>>>>Simulation 129:  465.tonto Asociatividad de caché: 16-way"

# Wait for simulation process to finish
wait $pid130
echo ">>>>>Simulation 130:  470.lbm Asociatividad de caché: 16-way"

# Wait for simulation process to finish
wait $pid131
echo ">>>>>Simulation 131:  471.omnetpp Asociatividad de caché: 16-way"

# Wait for simulation process to finish
wait $pid132
echo ">>>>>Simulation 132:  473.astar Asociatividad de caché: 16-way"

# Wait for simulation process to finish
wait $pid133
echo ">>>>>Simulation 133:  481.wrf Asociatividad de caché: 16-way"

# Wait for simulation process to finish
wait $pid134
echo ">>>>>Simulation 134:  482.sphinx3 Asociatividad de caché: 16-way"

# Wait for simulation process to finish
wait $pid135
echo ">>>>>Simulation 135:  483.xalancbmk Asociatividad de caché: 16-way"
echo ""
echo "Simulaciones con Tamaño de caché: ."
echo ""
echo "Revisar txt en directorio '$directory_name'"
echo ""
echo ""
echo ""

echo "Extractor corriendo"
python3 EXTRACTER_AC.py

echo "Mostrando resultados en excel: "
open Results_AC.xlsx