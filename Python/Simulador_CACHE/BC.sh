#!/bin/bash

# Create an array to store the simulation process IDs
pids=()
echo "'''''''''''''''''''''''''''''''''''''''''''''''''''''''''"
echo "Experimento: variación del tamaño de bloque de Caché(BC) "
echo "'''''''''''''''''''''''''''''''''''''''''''''''''''''''''"

# Define the directory name where txt result will be stored
directory_name="RESULTS_BC"
# Create the directory
mkdir "$directory_name"

#################################
# Tamaño de bloque caché:  16 kB#
#################################
echo "'''''''''''''''''''''''''''''"
echo "' Tamaño de caché:  '''32kB''"
echo "' Asociatividad: 8-ways     '"
echo "' Tamaño de bloque: 16kB    '"    
echo "' Política de reemplazo: LRU'"
echo "'''''''''''''''''''''''''''''"

# Simulation 1: 400.perlbench bloque de caché: 16kB
echo "Running 400.perlbench-bloque de caché: 16kB"
python3 cache_sim.py -s 32 -a 8 -b 16 -r l -t traces/400.perlbench-41B.trace.txt.gz > "$directory_name/400BC16.txt" &
pid1=$!
pids+=($pid1)

# Simulation 2: 401.bzip2 bloque de caché: 16kB
echo "Running 401.bzip2-bloque de caché: 16kB"
python3 cache_sim.py -s 32 -a 8 -b 16 -r l -t traces/401.bzip2-226B.trace.txt.gz > "$directory_name/401BC16.txt" &
pid2=$!
pids+=($pid2)

# Simulation 3: 403.gcc bloque de caché: 16kB
echo "Running 403.gcc-bloque de caché: 16kB"
python3 cache_sim.py -s 32 -a 8 -b 16 -r l -t traces/403.gcc-16B.trace.txt.gz > "$directory_name/403BC16.txt" &
pid3=$!
pids+=($pid3)

# Simulation 4: 410.bwaves bloque de caché: 16kB
echo "Running 410.bwaves-bloque de caché: 16kB"
python3 cache_sim.py -s 32 -a 8 -b 16 -r l -t traces/410.bwaves-1963B.trace.txt.gz > "$directory_name/410BC16.txt" &
pid4=$!
pids+=($pid4)

# Simulation 5: 416.gamess bloque de caché: 16kB
echo "Running 416.gamess bloque de caché: 16kB"
python3 cache_sim.py -s 32 -a 8 -b 16 -r l -t traces/416.gamess-875B.trace.txt.gz > "$directory_name/416BC16.txt" &
pids+=($pid5)

# Simulation 6: 429.mcf bloque de caché: 16kB
echo "Running 429.mcf bloque de caché: 16kB"
python3 cache_sim.py -s 32 -a 8 -b 16 -r l -t traces/429.mcf-184B.trace.txt.gz > "$directory_name/429BC16.txt" &
pids+=($pid6)

# Simulation 7: 433.milc bloque de caché: 16kB
echo "Running 433.milc bloque de caché: 16kB"
python3 cache_sim.py -s 32 -a 8 -b 16 -r l -t traces/433.milc-127B.trace.txt.gz > "$directory_name/433BC16.txt" &
pids+=($pid7)

# Simulation 8: 435.gromacs bloque de caché: 16kB
echo "Running 435.gromacs bloque de caché: 16kB"
python3 cache_sim.py -s 32 -a 8 -b 16 -r l -t traces/435.gromacs-111B.trace.txt.gz > "$directory_name/435BC16.txt" &
pids+=($pid8)

# Simulation 9: 436.cactusADM bloque de caché: 16kB
echo "Running 436.cactusADM bloque de caché: 16kB"
python3 cache_sim.py -s 32 -a 8 -b 16 -r l -t traces/436.cactusADM-1804B.trace.txt.gz > "$directory_name/436BC16.txt" &
pids+=($pid9)

# Simulation 10: 437.leslie3d bloque de caché: 16kB
echo "Running 437.leslie3d bloque de caché: 16kB"
python3 cache_sim.py -s 32 -a 8 -b 16 -r l -t traces/437.leslie3d-134B.trace.txt.gz > "$directory_name/437BC16.txt" &
pids+=($pid10)

# Simulation 11: 444.namd bloque de caché: 16kB
echo "Running 444.namd bloque de caché: 16kB"
python3 cache_sim.py -s 32 -a 8 -b 16 -r l -t traces/444.namd-120B.trace.txt.gz > "$directory_name/444BC16.txt" &
pids+=($pid11)

# Simulation 12: 445.gobmk bloque de caché: 16kB
echo "Running 445.gobmk bloque de caché: 16kB"
python3 cache_sim.py -s 32 -a 8 -b 16 -r l -t traces/445.gobmk-17B.trace.txt.gz > "$directory_name/445BC16.txt" &
pids+=($pid12)

# Simulation 13: 450.soplex bloque de caché: 16kB
echo "Running 450.soplex bloque de caché: 16kB"
python3 cache_sim.py -s 32 -a 8 -b 16 -r l -t traces/450.soplex-247B.trace.txt.gz > "$directory_name/450BC16.txt" &
pids+=($pid13)

# Simulation 14: 453.povray bloque de caché: 16kB
echo "Running 453.povray bloque de caché: 16kB"
python3 cache_sim.py -s 32 -a 8 -b 16 -r l -t traces/453.povray-887B.trace.txt.gz > "$directory_name/453BC16.txt" &
pids+=($pid14)

# Simulation 15: 454.calculix bloque de caché: 16kB
echo "Running 454.calculix bloque de caché: 16kB"
python3 cache_sim.py -s 32 -a 8 -b 16 -r l -t traces/454.calculix-104B.trace.txt.gz > "$directory_name/454BC16.txt" &
pids+=($pid15)

# Simulation 16: 456.hmmer bloque de caché: 16kB
echo "Running 456.hmmer bloque de caché: 16kB"
python3 cache_sim.py -s 32 -a 8 -b 16 -r l -t traces/456.hmmer-191B.trace.txt.gz > "$directory_name/456BC16.txt" &
pids+=($pid16)

# Simulation 17: 458.sjeng bloque de caché: 16kB
echo "Running 458.sjeng bloque de caché: 16kB"
python3 cache_sim.py -s 32 -a 8 -b 16 -r l -t traces/458.sjeng-1088B.trace.txt.gz > "$directory_name/458BC16.txt" &
pids+=($pid17)

# Simulation 18: 459.GemsFDTD bloque de caché: 16kB
echo "Running 459.GemsFDTD bloque de caché: 16kB"
python3 cache_sim.py -s 32 -a 8 -b 16 -r l -t traces/459.GemsFDTD-1169B.trace.txt.gz > "$directory_name/459BC16.txt" &
pids+=($pid18)

# Simulation 19: 462.libquantum bloque de caché: 16kB
echo "Running 462.libquantum bloque de caché: 16kB"
python3 cache_sim.py -s 32 -a 8 -b 16 -r l -t traces/462.libquantum-1343B.trace.txt.gz > "$directory_name/462BC16.txt" &
pids+=($pid19)

# Simulation 20: 464.h264 bloque de caché: 16kB
echo "Running 464.h264ref bloque de caché: 16kB"
python3 cache_sim.py -s 32 -a 8 -b 16 -r l -t traces/464.h264ref-30B.trace.txt.gz > "$directory_name/464BC16.txt" &
pids+=($pid20)

# Simulation 21: 465.tonto bloque de caché: 16kB
echo "Running 465.tonto bloque de caché: 16kB"
python3 cache_sim.py -s 32 -a 8 -b 16 -r l -t traces/465.tonto-1769B.trace.txt.gz > "$directory_name/465BC16.txt" &
pids+=($pid21)

# Simulation 22: 470.lbm bloque de caché: 16kB
echo "Running 470.lbm bloque de caché: 16kB"
python3 cache_sim.py -s 32 -a 8 -b 16 -r l -t traces/470.lbm-1274B.trace.txt.gz > "$directory_name/470BC16.txt" &
pids+=($pid22)

# Simulation 23: 471.omnetpp bloque de caché: 16kB
echo "Running 471.omnetpp bloque de caché: 16kB"
python3 cache_sim.py -s 32 -a 8 -b 16 -r l -t traces/471.omnetpp-188B.trace.txt.gz > "$directory_name/471BC16.txt" &
pids+=($pid23)

# Simulation 24: 473.astar bloque de caché: 16kB
echo "Running 473.astar bloque de caché: 16kB"
python3 cache_sim.py -s 32 -a 8 -b 16 -r l -t traces/473.astar-153B.trace.txt.gz > "$directory_name/473BC16.txt" &
pids+=($pid24)

# Simulation 25: 481.wrf bloque de caché: 16kB
echo "Running 481.wrf bloque de caché: 16kB"
python3 cache_sim.py -s 32 -a 8 -b 16 -r l -t traces/481.wrf-1170B.trace.txt.gz > "$directory_name/481BC16.txt" &
pids+=($pid25)

# Simulation 26: 482.sphinx3 bloque de caché: 16kB
echo "Running 482.sphinx3 bloque de caché: 16kB"
python3 cache_sim.py -s 32 -a 8 -b 16 -r l -t traces/482.sphinx3-1100B.trace.txt.gz > "$directory_name/482BC16.txt" &
pids+=($pid26)

# Simulation 27: 483.xalancbmk bloque de caché: 16kB
echo "Running 483.xalancbmk bloque de caché: 16kB"
python3 cache_sim.py -s 32 -a 8 -b 16 -r l -t traces/483.xalancbmk-127B.trace.txt.gz > "$directory_name/483BC16.txt" &
pids+=($pid27)


# Wait for simulation process to finish
wait $pid1
echo ">>>>>Simulation 1:  400.perlbench bloque de caché: 16kB"

# Wait for simulation process to finish
wait $pid2
echo ">>>>>Simulation 2:  401.bzip2 bloque de caché: 16kB"

# Wait for simulation process to finish
wait $pid3
echo ">>>>>Simulation 3:  403.gcc bloque de caché: 16kB"

# Wait for simulation process to finish
wait $pid4
echo ">>>>>Simulation 4:  410.bwaves bloque de caché: 16kB"

# Wait for simulation process to finish
wait $pid5
echo ">>>>>Simulation 5:  416.gamess bloque de caché: 16kB"

# Wait for simulation process to finish
wait $pid6
echo ">>>>>Simulation 6:  429.mcf bloque de caché: 16kB"

# Wait for simulation process to finish
wait $pid7
echo ">>>>>Simulation 7:  433.milc bloque de caché: 16kB"

# Wait for simulation process to finish
wait $pid8
echo ">>>>>Simulation 8:  435.gromacs bloque de caché: 16kB"

# Wait for simulation process to finish
wait $pid9
echo ">>>>>Simulation 9:  436.cactusADM bloque de caché: 16kB"

# Wait for simulation process to finish
wait $pid10
echo ">>>>>Simulation 10:  437.leslie3d bloque de caché: 16kB"

# Wait for simulation process to finish
wait $pid11
echo ">>>>>Simulation 11:  444.namd bloque de caché: 16kB"

# Wait for simulation process to finish
wait $pid12
echo ">>>>>Simulation 12:  445.gobmk bloque de caché: 16kB"

# Wait for simulation process to finish
wait $pid13
echo ">>>>>Simulation 13:  450.soplex  bloque de caché: 16kB"

# Wait for simulation process to finish
wait $pid14
echo ">>>>>Simulation 14:  453.povray bloque de caché: 16kB"

# Wait for simulation process to finish
wait $pid15
echo ">>>>>Simulation 15:  454.calculix bloque de caché: 16kB"

# Wait for simulation process to finish
wait $pid16
echo ">>>>>Simulation 16:  456.hmmer bloque de caché: 16kB"

# Wait for simulation process to finish
wait $pid17
echo ">>>>>Simulation 17:  458.sjeng bloque de caché: 16kB"

# Wait for simulation process to finish
wait $pid18
echo ">>>>>Simulation 18:  459.GemsFDTD bloque de caché: 16kB"

# Wait for simulation process to finish
wait $pid19
echo ">>>>>Simulation 19:  462.libquantum bloque de caché: 16kB"

# Wait for simulation process to finish
wait $pid20
echo ">>>>>Simulation 20:  464.h264ref bloque de caché: 16kB"

# Wait for simulation process to finish
wait $pid21
echo ">>>>>Simulation 21:  465.tonto bloque de caché: 16kB"

# Wait for simulation process to finish
wait $pid22
echo ">>>>>Simulation 22:  470.lbm bloque de caché: 16kB"

# Wait for simulation process to finish
wait $pid23
echo ">>>>>Simulation 23:  471.omnetpp bloque de caché: 16kB"

# Wait for simulation process to finish
wait $pid24
echo ">>>>>Simulation 24:  473.astar bloque de caché: 16kB"

# Wait for simulation process to finish
wait $pid25
echo ">>>>>Simulation 25:  481.wrf bloque de caché: 16kB"

# Wait for simulation process to finish
wait $pid26
echo ">>>>>Simulation 26:  482.sphinx3 bloque de caché: 16kB"

# Wait for simulation process to finish
wait $pid27
echo ">>>>>Simulation 27:  483.xalancbmk bloque de caché: 16kB"

echo ""
echo "Simulaciones con bloque de caché: 16kB"
echo ""
echo "Revisar txt en directorio '$directory_name1'"

#################################
# Tamaño de bloque caché:  32 kB#
#################################
echo "'''''''''''''''''''''''''''''''''"
echo "' Tamaño de caché (s): '''32kB'''"
echo "' Asociatividad (a):      8-ways'"
echo "' Tamaño de bloque (-b):    32kB'"    
echo "' Política de reemplazo:     LRU'"
echo "'''''''''''''''''''''''''''''''''"

# Simulation 28: 400.perlbench bloque de caché: 32kB
echo "Running 400.perlbench-bloque de caché: 32kB"
python3 cache_sim.py -s 32 -a 8 -b 32 -r l -t traces/400.perlbench-41B.trace.txt.gz > "$directory_name/400BC32.txt" &
pid28=$!
pids+=($pid28)

# Simulation 29: 401.bzip2 bloque de caché: 32kB
echo "Running 401.bzip2-Tamaño de caché:16kB"
python3 cache_sim.py -s 32 -a 8 -b 32 -r l -t traces/401.bzip2-226B.trace.txt.gz > "$directory_name/401BC32.txt" &
pid29=$!
pids+=($pid29)

# Simulation 30: 403.gcc bloque de caché: 32kB
echo "Running 403.gcc-bloque de caché: 32kB"
python3 cache_sim.py -s 32 -a 8 -b 32 -r l -t traces/403.gcc-16B.trace.txt.gz > "$directory_name/403BC32.txt" &
pid30=$!
pids+=($pid30)

# Simulation 31: 410.bwaves bloque de caché: 32kB
echo "Running 410.bwaves-bloque de caché: 32kB"
python3 cache_sim.py -s 32 -a 8 -b 32 -r l -t traces/410.bwaves-1963B.trace.txt.gz > "$directory_name/410BC32.txt" &
pid31=$!
pids+=($pid31)

# Simulation 32: 416.gamess bloque de caché: 32kB
echo "Running 416.gamess bloque de caché: 32kB"
python3 cache_sim.py -s 32 -a 8 -b 32 -r l -t traces/416.gamess-875B.trace.txt.gz > "$directory_name/416BC32.txt" &
pids+=($pid32)

# Simulation 33: 429.mcf bloque de caché: 32kB
echo "Running 429.mcf bloque de caché: 32kB"
python3 cache_sim.py -s 32 -a 8 -b 32 -r l -t traces/429.mcf-184B.trace.txt.gz > "$directory_name/429BC32.txt" &
pids+=($pid33)

# Simulation 34: 433.milc bloque de caché: 32kB
echo "Running 433.milc bloque de caché: 32kB"
python3 cache_sim.py -s 32 -a 8 -b 32 -r l -t traces/433.milc-127B.trace.txt.gz > "$directory_name/433BC32.txt" &
pids+=($pid34)

# Simulation 35: 435.gromacs bloque de caché: 32kB
echo "Running 435.gromacs bloque de caché: 32kB"
python3 cache_sim.py -s 32 -a 8 -b 32 -r l -t traces/435.gromacs-111B.trace.txt.gz > "$directory_name/435BC32.txt" &
pids+=($pid35)

# Simulation 36: 436.cactusADM bloque de caché: 32kB
echo "Running 436.cactusADM bloque de caché: 32kB"
python3 cache_sim.py -s 32 -a 8 -b 32 -r l -t traces/436.cactusADM-1804B.trace.txt.gz > "$directory_name/436BC32.txt" &
pids+=($pid36)

# Simulation 37: 437.leslie3d bloque de caché: 32kB
echo "Running 437.leslie3d bloque de caché: 32kB"
python3 cache_sim.py -s 32 -a 8 -b 32 -r l -t traces/437.leslie3d-134B.trace.txt.gz > "$directory_name/437BC32.txt" &
pids+=($pid37)

# Simulation 38: 444.namd bloque de caché: 32kB
echo "Running 444.namd bloque de caché: 32kB"
python3 cache_sim.py -s 32 -a 8 -b 32 -r l -t traces/444.namd-120B.trace.txt.gz > "$directory_name/444BC32.txt" &
pids+=($pid38)

# Simulation 39: 445.gobmk bloque de caché: 32kB
echo "Running 445.gobmk bloque de caché: 32kB"
python3 cache_sim.py -s 32 -a 8 -b 32 -r l -t traces/445.gobmk-17B.trace.txt.gz > "$directory_name/445BC32.txt" &
pids+=($pid39)

# Simulation 40: 450.soplex bloque de caché: 32kB
echo "Running 450.soplex bloque de caché: 32kB"
python3 cache_sim.py -s 32 -a 8 -b 32 -r l -t traces/450.soplex-247B.trace.txt.gz > "$directory_name/450BC32.txt" &
pids+=($pid40)

# Simulation 41: 453.povray bloque de caché: 32kB
echo "Running 453.povray bloque de caché: 32kB"
python3 cache_sim.py -s 32 -a 8 -b 32 -r l -t traces/453.povray-887B.trace.txt.gz > "$directory_name/453BC32.txt" &
pids+=($pid41)

# Simulation 42: 454.calculix bloque de caché: 32kB
echo "Running 454.calculix bloque de caché: 32kB"
python3 cache_sim.py -s 32 -a 8 -b 32 -r l -t traces/454.calculix-104B.trace.txt.gz > "$directory_name/454BC32.txt" &
pids+=($pid42)

# Simulation 43: 456.hmmer bloque de caché: 32kB
echo "Running 456.hmmer bloque de caché: 32kB"
python3 cache_sim.py -s 32 -a 8 -b 32 -r l -t traces/456.hmmer-191B.trace.txt.gz > "$directory_name/456BC32.txt" &
pids+=($pid43)

# Simulation 44: 458.sjeng bloque de caché: 32kB
echo "Running 458.sjeng bloque de caché: 32kB"
python3 cache_sim.py -s 32 -a 8 -b 32 -r l -t traces/458.sjeng-1088B.trace.txt.gz > "$directory_name/458BC32.txt" &
pids+=($pid44)

# Simulation 45: 459.GemsFDTD bloque de caché: 32kB
echo "Running 459.GemsFDTD bloque de caché: 32kB"
python3 cache_sim.py -s 32 -a 8 -b 32 -r l -t traces/459.GemsFDTD-1169B.trace.txt.gz > "$directory_name/459BC32.txt" &
pids+=($pid45)

# Simulation 46: 462.libquantum bloque de caché: 32kB
echo "Running 462.libquantum bloque de caché: 32kB"
python3 cache_sim.py -s 32 -a 8 -b 32 -r l -t traces/462.libquantum-1343B.trace.txt.gz > "$directory_name/462BC32.txt" &
pids+=($pid46)

# Simulation 47: 464.h264 bloque de caché: 32kB
echo "Running 464.h264ref bloque de caché: 32kB"
python3 cache_sim.py -s 32 -a 8 -b 32 -r l -t traces/464.h264ref-30B.trace.txt.gz > "$directory_name/464BC32.txt" &
pids+=($pid47)

# Simulation 48: 465.tonto bloque de caché: 32kB
echo "Running 465.tonto bloque de caché: 32kB"
python3 cache_sim.py -s 32 -a 8 -b 32 -r l -t traces/465.tonto-1769B.trace.txt.gz > "$directory_name/465BC32.txt" &
pids+=($pid48)

# Simulation 49: 470.lbm bloque de caché: 32kB
echo "Running 470.lbm bloque de caché: 32kB"
python3 cache_sim.py -s 32 -a 8 -b 32 -r l -t traces/470.lbm-1274B.trace.txt.gz > "$directory_name/470BC32.txt" &
pids+=($pid49)

# Simulation 50: 471.omnetpp bloque de caché: 32kB
echo "Running 471.omnetpp bloque de caché: 32kB"
python3 cache_sim.py -s 32 -a 8 -b 32 -r l -t traces/471.omnetpp-188B.trace.txt.gz > "$directory_name/471BC32.txt" &
pids+=($pid50)

# Simulation 51: 473.astar bloque de caché: 32kB
echo "Running 473.astar bloque de caché: 32kB"
python3 cache_sim.py -s 32 -a 8 -b 32 -r l -t traces/473.astar-153B.trace.txt.gz > "$directory_name/473BC32.txt" &
pids+=($pid51)

# Simulation 52: 481.wrf bloque de caché: 32kB
echo "Running 481.wrf bloque de caché: 32kB"
python3 cache_sim.py -s 32 -a 8 -b 32 -r l -t traces/481.wrf-1170B.trace.txt.gz > "$directory_name/481BC32.txt" &
pids+=($pid52)

# Simulation 53: 482.sphinx3 bloque de caché: 32kB
echo "Running 482.sphinx3 bloque de caché: 32kB"
python3 cache_sim.py -s 32 -a 8 -b 32 -r l -t traces/482.sphinx3-1100B.trace.txt.gz > "$directory_name/482BC32.txt" &
pids+=($pid53)

# Simulation 54: 483.xalancbmk bloque de caché: 32kB
echo "Running 483.xalancbmk bloque de caché: 32kB"
python3 cache_sim.py -s 32 -a 8 -b 32 -r l -t traces/483.xalancbmk-127B.trace.txt.gz > "$directory_name/483BC32.txt" &
pids+=($pid54)


# Wait for simulation process to finish
wait $pid28
echo ">>>>>Simulation 28:  400.perlbench bloque de caché: 32kB"

# Wait for simulation process to finish
wait $pid29
echo ">>>>>Simulation 29:  401.bzip2 bloque de caché: 32kB"

# Wait for simulation process to finish
wait $pid30
echo ">>>>>Simulation 30:  403.gcc bloque de caché: 32kB"

# Wait for simulation process to finish
wait $pid31
echo ">>>>>Simulation 31:  410.bwaves bloque de caché: 32kB"

# Wait for simulation process to finish
wait $pid32
echo ">>>>>Simulation 32:  416.gamess bloque de caché: 32kB"

# Wait for simulation process to finish
wait $pid33
echo ">>>>>Simulation 33:  429.mcf bloque de caché: 32kB"

# Wait for simulation process to finish
wait $pid34
echo ">>>>>Simulation 34:  433.milc bloque de caché: 32kB"

# Wait for simulation process to finish
wait $pid35
echo ">>>>>Simulation 35:  435.gromacs bloque de caché: 32kB"

# Wait for simulation process to finish
wait $pid36
echo ">>>>>Simulation 36:  436.cactusADM bloque de caché: 32kB"

# Wait for simulation process to finish
wait $pid37
echo ">>>>>Simulation 37:  437.leslie3d bloque de caché: 32kB"

# Wait for simulation process to finish
wait $pid38
echo ">>>>>Simulation 38:  444.namd bloque de caché: 32kB"

# Wait for simulation process to finish
wait $pid39
echo ">>>>>Simulation 39:  445.gobmk bloque de caché: 32kB"

# Wait for simulation process to finish
wait $pid40
echo ">>>>>Simulation 40:  450.soplex  bloque de caché: 32kB"

# Wait for simulation process to finish
wait $pid41
echo ">>>>>Simulation 41:  453.povray bloque de caché: 32kB"

# Wait for simulation process to finish
wait $pid42
echo ">>>>>Simulation 42:  454.calculix bloque de caché: 32kB"

# Wait for simulation process to finish
wait $pid43
echo ">>>>>Simulation 43:  456.hmmer bloque de caché: 32kB"

# Wait for simulation process to finish
wait $pid44
echo ">>>>>Simulation 44:  458.sjeng bloque de caché: 32kB"

# Wait for simulation process to finish
wait $pid45
echo ">>>>>Simulation 45:  459.GemsFDTD bloque de caché: 32kB"

# Wait for simulation process to finish
wait $pid46
echo ">>>>>Simulation 46:  462.libquantum bloque de caché: 32kB"

# Wait for simulation process to finish
wait $pid47
echo ">>>>>Simulation 47:  464.h264ref bloque de caché: 32kB"

# Wait for simulation process to finish
wait $pid48
echo ">>>>>Simulation 48:  465.tonto bloque de caché: 32kB"

# Wait for simulation process to finish
wait $pid49
echo ">>>>>Simulation 49:  470.lbm bloque de caché: 32kB"

# Wait for simulation process to finish
wait $pid50
echo ">>>>>Simulation 50:  471.omnetpp bloque de caché: 32kB"

# Wait for simulation process to finish
wait $pid51
echo ">>>>>Simulation 51:  473.astar bloque de caché: 32kB"

# Wait for simulation process to finish
wait $pid52
echo ">>>>>Simulation 52:  481.wrf bloque de caché: 32kB"

# Wait for simulation process to finish
wait $pid53
echo ">>>>>Simulation 53:  482.sphinx3 bloque de caché: 32kB"

# Wait for simulation process to finish
wait $pid54
echo ">>>>>Simulation 54:  483.xalancbmk bloque de caché: 32kB"
echo ""
echo "Simulaciones con bloque de caché: 32kB"
echo ""
echo "Revisar txt en directorio '$directory_name'"
echo ""
echo ""
echo ""
echo ""

#################################
# Tamaño de bloque caché:  64 kB#
#################################
echo "'''''''''''''''''''''''''''''''''"
echo "' Tamaño de caché (s): '''32kB'''"
echo "' Asociatividad (a):      8-ways'"
echo "' Tamaño de bloque (-b):    64kB'"    
echo "' Política de reemplazo:     LRU'"
echo "'''''''''''''''''''''''''''''''''"

# Simulation 55: 400.perlbench Tamaño bloque de caché: 64kB
echo "Running 400.perlbench-Tamaño bloque de caché: 64kB"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/400.perlbench-41B.trace.txt.gz > "$directory_name/400BC64.txt" &
pid55=$!
pids+=($pid55)

# Simulation 56: 401.bzip2 Tamaño bloque de caché: 64kB
echo "Running 401.bzip2-Tamaño de caché:32kB"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/401.bzip2-226B.trace.txt.gz > "$directory_name/401BC64.txt" &
pid56=$!
pids+=($pid56)

# Simulation 57: 403.gcc Tamaño bloque de caché: 64kB
echo "Running 403.gcc-Tamaño bloque de caché: 64kB"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/403.gcc-16B.trace.txt.gz > "$directory_name/403BC64.txt" &
pid57=$!
pids+=($pid57)

# Simulation 58: 410.bwaves Tamaño bloque de caché: 64kB
echo "Running 410.bwaves-Tamaño bloque de caché: 64kB"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/410.bwaves-1963B.trace.txt.gz > "$directory_name/410BC64.txt" &
pid58=$!
pids+=($pid58)

# Simulation 59: 416.gamess Tamaño bloque de caché: 64kB
echo "Running 416.gamess Tamaño bloque de caché: 64kB"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/416.gamess-875B.trace.txt.gz > "$directory_name/416BC64.txt" &
pids+=($pid59)

# Simulation 60: 429.mcf Tamaño bloque de caché: 64kB
echo "Running 429.mcf Tamaño bloque de caché: 64kB"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/429.mcf-184B.trace.txt.gz > "$directory_name/429BC64.txt" &
pids+=($pid60)

# Simulation 61: 433.milc Tamaño bloque de caché: 64kB
echo "Running 433.milc Tamaño bloque de caché: 64kB"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/433.milc-127B.trace.txt.gz > "$directory_name/433BC64.txt" &
pids+=($pid61)

# Simulation 62: 435.gromacs Tamaño bloque de caché: 64kB
echo "Running 435.gromacs Tamaño bloque de caché: 64kB"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/435.gromacs-111B.trace.txt.gz > "$directory_name/435BC64.txt" &
pids+=($pid62)

# Simulation 63: 436.cactusADM Tamaño bloque de caché: 64kB
echo "Running 436.cactusADM Tamaño bloque de caché: 64kB"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/436.cactusADM-1804B.trace.txt.gz > "$directory_name/436BC64.txt" &
pids+=($pid63)

# Simulation 64: 437.leslie3d Tamaño bloque de caché: 64kB
echo "Running 437.leslie3d Tamaño bloque de caché: 64kB"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/437.leslie3d-134B.trace.txt.gz > "$directory_name/437BC64.txt" &
pids+=($pid64)

# Simulation 65: 444.namd Tamaño bloque de caché: 64kB
echo "Running 444.namd Tamaño bloque de caché: 64kB"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/444.namd-120B.trace.txt.gz > "$directory_name/444BC64.txt" &
pids+=($pid65)

# Simulation 66: 445.gobmk Tamaño bloque de caché: 64kB
echo "Running 445.gobmk Tamaño bloque de caché: 64kB"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/445.gobmk-17B.trace.txt.gz > "$directory_name/445BC64.txt" &
pids+=($pid66)

# Simulation 67: 450.soplex Tamaño bloque de caché: 64kB
echo "Running 450.soplex Tamaño bloque de caché: 64kB"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/450.soplex-247B.trace.txt.gz > "$directory_name/450BC64.txt" &
pids+=($pid67)

# Simulation 68: 453.povray Tamaño bloque de caché: 64kB
echo "Running 453.povray Tamaño bloque de caché: 64kB"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/453.povray-887B.trace.txt.gz > "$directory_name/453BC64.txt" &
pids+=($pid68)

# Simulation 69: 454.calculix Tamaño bloque de caché: 64kB
echo "Running 454.calculix Tamaño bloque de caché: 64kB"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/454.calculix-104B.trace.txt.gz > "$directory_name/454BC64.txt" &
pids+=($pid69)

# Simulation 70: 456.hmmer Tamaño bloque de caché: 64kB
echo "Running 456.hmmer Tamaño bloque de caché: 64kB"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/456.hmmer-191B.trace.txt.gz > "$directory_name/456BC64.txt" &
pids+=($pid70)

# Simulation 71: 458.sjeng Tamaño bloque de caché: 64kB
echo "Running 458.sjeng Tamaño bloque de caché: 64kB"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/458.sjeng-1088B.trace.txt.gz > "$directory_name/458BC64.txt" &
pids+=($pid71)

# Simulation 72: 459.GemsFDTD Tamaño bloque de caché: 64kB
echo "Running 459.GemsFDTD Tamaño bloque de caché: 64kB"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/459.GemsFDTD-1169B.trace.txt.gz > "$directory_name/459BC64.txt" &
pids+=($pid72)

# Simulation 73: 462.libquantum Tamaño bloque de caché: 64kB
echo "Running 462.libquantum Tamaño bloque de caché: 64kB"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/462.libquantum-1343B.trace.txt.gz > "$directory_name/462BC64.txt" &
pids+=($pid73)

# Simulation 74: 464.h264 Tamaño bloque de caché: 64kB
echo "Running 464.h264ref Tamaño bloque de caché: 64kB"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/464.h264ref-30B.trace.txt.gz > "$directory_name/464BC64.txt" &
pids+=($pid74)

# Simulation 75: 465.tonto Tamaño bloque de caché: 64kB
echo "Running 465.tonto Tamaño bloque de caché: 64kB"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/465.tonto-1769B.trace.txt.gz > "$directory_name/465BC64.txt" &
pids+=($pid75)

# Simulation 76: 470.lbm Tamaño bloque de caché: 64kB
echo "Running 470.lbm Tamaño bloque de caché: 64kB"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/470.lbm-1274B.trace.txt.gz > "$directory_name/470BC64.txt" &
pids+=($pid76)

# Simulation 77: 471.omnetpp Tamaño bloque de caché: 64kB
echo "Running 471.omnetpp Tamaño bloque de caché: 64kB"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/471.omnetpp-188B.trace.txt.gz > "$directory_name/471BC64.txt" &
pids+=($pid77)

# Simulation 78: 473.astar Tamaño bloque de caché: 64kB
echo "Running 473.astar Tamaño bloque de caché: 64kB"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/473.astar-153B.trace.txt.gz > "$directory_name/473BC64.txt" &
pids+=($pid78)

# Simulation 79: 481.wrf Tamaño bloque de caché: 64kB
echo "Running 481.wrf Tamaño bloque de caché: 64kB"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/481.wrf-1170B.trace.txt.gz > "$directory_name/481BC64.txt" &
pids+=($pid79)

# Simulation 80: 482.sphinx3 Tamaño bloque de caché: 64kB
echo "Running 482.sphinx3 Tamaño bloque de caché: 64kB"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/482.sphinx3-1100B.trace.txt.gz > "$directory_name/482BC64.txt" &
pids+=($pid80)

# Simulation 81: 483.xalancbmk Tamaño bloque de caché: 64kB
echo "Running 483.xalancbmk Tamaño bloque de caché: 64kB"
python3 cache_sim.py -s 32 -a 8 -b 64 -r l -t traces/483.xalancbmk-127B.trace.txt.gz > "$directory_name/483BC64.txt" &
pids+=($pid81)


# Wait for simulation process to finish
wait $pid55
echo ">>>>>Simulation 55:  400.perlbench Tamaño bloque de caché: 64kB"

# Wait for simulation process to finish
wait $pid56
echo ">>>>>Simulation 56:  401.bzip2 Tamaño bloque de caché: 64kB"

# Wait for simulation process to finish
wait $pid57
echo ">>>>>Simulation 57:  403.gcc Tamaño bloque de caché: 64kB"

# Wait for simulation process to finish
wait $pid58
echo ">>>>>Simulation 58:  410.bwaves Tamaño bloque de caché: 64kB"

# Wait for simulation process to finish
wait $pid59
echo ">>>>>Simulation 59:  416.gamess Tamaño bloque de caché: 64kB"

# Wait for simulation process to finish
wait $pid60
echo ">>>>>Simulation 60:  429.mcf Tamaño bloque de caché: 64kB"

# Wait for simulation process to finish
wait $pid61
echo ">>>>>Simulation 61:  433.milc Tamaño bloque de caché: 64kB"

# Wait for simulation process to finish
wait $pid62
echo ">>>>>Simulation 62:  435.gromacs Tamaño bloque de caché: 64kB"

# Wait for simulation process to finish
wait $pid63
echo ">>>>>Simulation 63:  436.cactusADM Tamaño bloque de caché: 64kB"

# Wait for simulation process to finish
wait $pid64
echo ">>>>>Simulation 64:  437.leslie3d Tamaño bloque de caché: 64kB"

# Wait for simulation process to finish
wait $pid65
echo ">>>>>Simulation 65:  444.namd Tamaño bloque de caché: 64kB"

# Wait for simulation process to finish
wait $pid66
echo ">>>>>Simulation 66:  445.gobmk Tamaño bloque de caché: 64kB"

# Wait for simulation process to finish
wait $pid67
echo ">>>>>Simulation 67:  450.soplex  Tamaño bloque de caché: 64kB"

# Wait for simulation process to finish
wait $pid68
echo ">>>>>Simulation 68:  453.povray Tamaño bloque de caché: 64kB"

# Wait for simulation process to finish
wait $pid69
echo ">>>>>Simulation 69:  454.calculix Tamaño bloque de caché: 64kB"

# Wait for simulation process to finish
wait $pid70
echo ">>>>>Simulation 70:  456.hmmer Tamaño bloque de caché: 64kB"

# Wait for simulation process to finish
wait $pid71
echo ">>>>>Simulation 71:  458.sjeng Tamaño bloque de caché: 64kB"

# Wait for simulation process to finish
wait $pid72
echo ">>>>>Simulation 72:  459.GemsFDTD Tamaño bloque de caché: 64kB"

# Wait for simulation process to finish
wait $pid73
echo ">>>>>Simulation 73:  462.libquantum Tamaño bloque de caché: 64kB"

# Wait for simulation process to finish
wait $pid74
echo ">>>>>Simulation 74:  464.h264ref Tamaño bloque de caché: 64kB"

# Wait for simulation process to finish
wait $pid75
echo ">>>>>Simulation 75:  465.tonto Tamaño bloque de caché: 64kB"

# Wait for simulation process to finish
wait $pid76
echo ">>>>>Simulation 76:  470.lbm Tamaño bloque de caché: 64kB"

# Wait for simulation process to finish
wait $pid77
echo ">>>>>Simulation 77:  471.omnetpp Tamaño bloque de caché: 64kB"

# Wait for simulation process to finish
wait $pid78
echo ">>>>>Simulation 78:  473.astar Tamaño bloque de caché: 64kB"

# Wait for simulation process to finish
wait $pid79
echo ">>>>>Simulation 79:  481.wrf Tamaño bloque de caché: 64kB"

# Wait for simulation process to finish
wait $pid80
echo ">>>>>Simulation 80:  482.sphinx3 Tamaño bloque de caché: 64kB"

# Wait for simulation process to finish
wait $pid81
echo ">>>>>Simulation 81:  483.xalancbmk Tamaño bloque de caché: 64kB"
echo ""
echo "Simulaciones con Tamaño bloque de caché: 64kB"
echo ""
echo "Revisar txt en directorio '$directory_name'"
echo ""
echo ""
echo ""

##################################
# Tamaño de bloque caché:  128 kB#
##################################
echo "'''''''''''''''''''''''''''''''''"
echo "' Tamaño de caché (s): '''32kB'''"
echo "' Asociatividad (a):      8-ways'"
echo "' Tamaño de bloque (-b):   128kB'"    
echo "' Política de reemplazo:     LRU'"
echo "'''''''''''''''''''''''''''''''''"

# Simulation 82: 400.perlbench Tamaño bloque de caché: 128kB
echo "Running 400.perlbench-Tamaño bloque de caché: 128kB"
python3 cache_sim.py -s 32 -a 8 -b 128 -r l -t traces/400.perlbench-41B.trace.txt.gz > "$directory_name/400BC128.txt" &
pid82=$!
pids+=($pid82)

# Simulation 83: 401.bzip2 Tamaño bloque de caché: 128kB
echo "Running 401.bzip2-Tamaño de caché:64kB"
python3 cache_sim.py -s 32 -a 8 -b 128 -r l -t traces/401.bzip2-226B.trace.txt.gz > "$directory_name/401BC128.txt" &
pid83=$!
pids+=($pid83)

# Simulation 84: 403.gcc Tamaño bloque de caché: 128kB
echo "Running 403.gcc-Tamaño bloque de caché: 128kB"
python3 cache_sim.py -s 32 -a 8 -b 128 -r l -t traces/403.gcc-16B.trace.txt.gz > "$directory_name/403BC128.txt" &
pid84=$!
pids+=($pid84)

# Simulation 85: 410.bwaves Tamaño bloque de caché: 128kB
echo "Running 410.bwaves-Tamaño bloque de caché: 128kB"
python3 cache_sim.py -s 32 -a 8 -b 128 -r l -t traces/410.bwaves-1963B.trace.txt.gz > "$directory_name/410BC128.txt" &
pid85=$!
pids+=($pid85)

# Simulation 86: 416.gamess Tamaño bloque de caché: 128kB
echo "Running 416.gamess Tamaño bloque de caché: 128kB"
python3 cache_sim.py -s 32 -a 8 -b 128 -r l -t traces/416.gamess-875B.trace.txt.gz > "$directory_name/416BC128.txt" &
pids+=($pid86)

# Simulation 87: 429.mcf Tamaño bloque de caché: 128kB
echo "Running 429.mcf Tamaño bloque de caché: 128kB"
python3 cache_sim.py -s 32 -a 8 -b 128 -r l -t traces/429.mcf-184B.trace.txt.gz > "$directory_name/429BC128.txt" &
pids+=($pid87)

# Simulation 88: 433.milc Tamaño bloque de caché: 128kB
echo "Running 433.milc Tamaño bloque de caché: 128kB"
python3 cache_sim.py -s 32 -a 8 -b 128 -r l -t traces/433.milc-127B.trace.txt.gz > "$directory_name/433BC128.txt" &
pids+=($pid88)

# Simulation 89: 435.gromacs Tamaño bloque de caché: 128kB
echo "Running 435.gromacs Tamaño bloque de caché: 128kB"
python3 cache_sim.py -s 32 -a 8 -b 128 -r l -t traces/435.gromacs-111B.trace.txt.gz > "$directory_name/435BC128.txt" &
pids+=($pid89)

# Simulation 90: 436.cactusADM Tamaño bloque de caché: 128kB
echo "Running 436.cactusADM Tamaño bloque de caché: 128kB"
python3 cache_sim.py -s 32 -a 8 -b 128 -r l -t traces/436.cactusADM-1804B.trace.txt.gz > "$directory_name/436BC128.txt" &
pids+=($pid90)

# Simulation 91: 437.leslie3d Tamaño bloque de caché: 128kB
echo "Running 437.leslie3d Tamaño bloque de caché: 128kB"
python3 cache_sim.py -s 32 -a 8 -b 128 -r l -t traces/437.leslie3d-134B.trace.txt.gz > "$directory_name/437BC128.txt" &
pids+=($pid91)

# Simulation 92: 444.namd Tamaño bloque de caché: 128kB
echo "Running 444.namd Tamaño bloque de caché: 128kB"
python3 cache_sim.py -s 32 -a 8 -b 128 -r l -t traces/444.namd-120B.trace.txt.gz > "$directory_name/444BC128.txt" &
pids+=($pid92)

# Simulation 93: 445.gobmk Tamaño bloque de caché: 128kB
echo "Running 445.gobmk Tamaño bloque de caché: 128kB"
python3 cache_sim.py -s 32 -a 8 -b 128 -r l -t traces/445.gobmk-17B.trace.txt.gz > "$directory_name/445BC128.txt" &
pids+=($pid93)

# Simulation 94: 450.soplex Tamaño bloque de caché: 128kB
echo "Running 450.soplex Tamaño bloque de caché: 128kB"
python3 cache_sim.py -s 32 -a 8 -b 128 -r l -t traces/450.soplex-247B.trace.txt.gz > "$directory_name/450BC128.txt" &
pids+=($pid94)

# Simulation 95: 453.povray Tamaño bloque de caché: 128kB
echo "Running 453.povray Tamaño bloque de caché: 128kB"
python3 cache_sim.py -s 32 -a 8 -b 128 -r l -t traces/453.povray-887B.trace.txt.gz > "$directory_name/453BC128.txt" &
pids+=($pid95)

# Simulation 96: 454.calculix Tamaño bloque de caché: 128kB
echo "Running 454.calculix Tamaño bloque de caché: 128kB"
python3 cache_sim.py -s 32 -a 8 -b 128 -r l -t traces/454.calculix-104B.trace.txt.gz > "$directory_name/454BC128.txt" &
pids+=($pid96)

# Simulation 97: 456.hmmer Tamaño bloque de caché: 128kB
echo "Running 456.hmmer Tamaño bloque de caché: 128kB"
python3 cache_sim.py -s 32 -a 8 -b 128 -r l -t traces/456.hmmer-191B.trace.txt.gz > "$directory_name/456BC128.txt" &
pids+=($pid97)

# Simulation 98: 458.sjeng Tamaño bloque de caché: 128kB
echo "Running 458.sjeng Tamaño bloque de caché: 128kB"
python3 cache_sim.py -s 32 -a 8 -b 128 -r l -t traces/458.sjeng-1088B.trace.txt.gz > "$directory_name/458BC128.txt" &
pids+=($pid98)

# Simulation 99: 459.GemsFDTD Tamaño bloque de caché: 128kB
echo "Running 459.GemsFDTD Tamaño bloque de caché: 128kB"
python3 cache_sim.py -s 32 -a 8 -b 128 -r l -t traces/459.GemsFDTD-1169B.trace.txt.gz > "$directory_name/459BC128.txt" &
pids+=($pid99)

# Simulation 100: 462.libquantum Tamaño bloque de caché: 128kB
echo "Running 462.libquantum Tamaño bloque de caché: 128kB"
python3 cache_sim.py -s 32 -a 8 -b 128 -r l -t traces/462.libquantum-1343B.trace.txt.gz > "$directory_name/462BC128.txt" &
pids+=($pid100)

# Simulation 101: 464.h264 Tamaño bloque de caché: 128kB
echo "Running 464.h264ref Tamaño bloque de caché: 128kB"
python3 cache_sim.py -s 32 -a 8 -b 128 -r l -t traces/464.h264ref-30B.trace.txt.gz > "$directory_name/464BC128.txt" &
pids+=($pid101)

# Simulation 102: 465.tonto Tamaño bloque de caché: 128kB
echo "Running 465.tonto Tamaño bloque de caché: 128kB"
python3 cache_sim.py -s 32 -a 8 -b 128 -r l -t traces/465.tonto-1769B.trace.txt.gz > "$directory_name/465BC128.txt" &
pids+=($pid102)

# Simulation 103: 470.lbm Tamaño bloque de caché: 128kB
echo "Running 470.lbm Tamaño bloque de caché: 128kB"
python3 cache_sim.py -s 32 -a 8 -b 128 -r l -t traces/470.lbm-1274B.trace.txt.gz > "$directory_name/470BC128.txt" &
pids+=($pid103)

# Simulation 104: 471.omnetpp Tamaño bloque de caché: 128kB
echo "Running 471.omnetpp Tamaño bloque de caché: 128kB"
python3 cache_sim.py -s 32 -a 8 -b 128 -r l -t traces/471.omnetpp-188B.trace.txt.gz > "$directory_name/471BC128.txt" &
pids+=($pid104)

# Simulation 105: 473.astar Tamaño bloque de caché: 128kB
echo "Running 473.astar Tamaño bloque de caché: 128kB"
python3 cache_sim.py -s 32 -a 8 -b 128 -r l -t traces/473.astar-153B.trace.txt.gz > "$directory_name/473BC128.txt" &
pids+=($pid105)

# Simulation 106: 481.wrf Tamaño bloque de caché: 128kB
echo "Running 481.wrf Tamaño bloque de caché: 128kB"
python3 cache_sim.py -s 32 -a 8 -b 128 -r l -t traces/481.wrf-1170B.trace.txt.gz > "$directory_name/481BC128.txt" &
pids+=($pid106)

# Simulation 107: 482.sphinx3 Tamaño bloque de caché: 128kB
echo "Running 482.sphinx3 Tamaño bloque de caché: 128kB"
python3 cache_sim.py -s 32 -a 8 -b 128 -r l -t traces/482.sphinx3-1100B.trace.txt.gz > "$directory_name/482BC128.txt" &
pids+=($pid107)

# Simulation 108: 483.xalancbmk Tamaño bloque de caché: 128kB
echo "Running 483.xalancbmk Tamaño bloque de caché: 128kB"
python3 cache_sim.py -s 32 -a 8 -b 128 -r l -t traces/483.xalancbmk-127B.trace.txt.gz > "$directory_name/483BC128.txt" &
pids+=($pid108)

# Wait for simulation process to finish
wait $pid82
echo ">>>>>Simulation 82:  400.perlbench Tamaño bloque de caché: 128kB"

# Wait for simulation process to finish
wait $pid83
echo ">>>>>Simulation 83:  401.bzip2 Tamaño bloque de caché: 128kB"

# Wait for simulation process to finish
wait $pid84
echo ">>>>>Simulation 84:  403.gcc Tamaño bloque de caché: 128kB"

# Wait for simulation process to finish
wait $pid85
echo ">>>>>Simulation 85:  410.bwaves Tamaño bloque de caché: 128kB"

# Wait for simulation process to finish
wait $pid86
echo ">>>>>Simulation 86:  416.gamess Tamaño bloque de caché: 128kB"

# Wait for simulation process to finish
wait $pid87
echo ">>>>>Simulation 87:  429.mcf Tamaño bloque de caché: 128kB"

# Wait for simulation process to finish
wait $pid88
echo ">>>>>Simulation 88:  433.milc Tamaño bloque de caché: 128kB"

# Wait for simulation process to finish
wait $pid89
echo ">>>>>Simulation 89:  435.gromacs Tamaño bloque de caché: 128kB"

# Wait for simulation process to finish
wait $pid90
echo ">>>>>Simulation 90:  436.cactusADM Tamaño bloque de caché: 128kB"

# Wait for simulation process to finish
wait $pid91
echo ">>>>>Simulation 91:  437.leslie3d Tamaño bloque de caché: 128kB"

# Wait for simulation process to finish
wait $pid92
echo ">>>>>Simulation 92:  444.namd Tamaño bloque de caché: 128kB"

# Wait for simulation process to finish
wait $pid93
echo ">>>>>Simulation 93:  445.gobmk Tamaño bloque de caché: 128kB"

# Wait for simulation process to finish
wait $pid94
echo ">>>>>Simulation 94:  450.soplex  Tamaño bloque de caché: 128kB"

# Wait for simulation process to finish
wait $pid95
echo ">>>>>Simulation 95:  453.povray Tamaño bloque de caché: 128kB"

# Wait for simulation process to finish
wait $pid96
echo ">>>>>Simulation 96:  454.calculix Tamaño bloque de caché: 128kB"

# Wait for simulation process to finish
wait $pid97
echo ">>>>>Simulation 97:  456.hmmer Tamaño bloque de caché: 128kB"

# Wait for simulation process to finish
wait $pid98
echo ">>>>>Simulation 98:  458.sjeng Tamaño bloque de caché: 128kB"

# Wait for simulation process to finish
wait $pid99
echo ">>>>>Simulation 99:  459.GemsFDTD Tamaño bloque de caché: 128kB"

# Wait for simulation process to finish
wait $pid100
echo ">>>>>Simulation 100:  462.libquantum Tamaño bloque de caché: 128kB"

# Wait for simulation process to finish
wait $pid101
echo ">>>>>Simulation 101:  464.h264ref Tamaño bloque de caché: 128kB"

# Wait for simulation process to finish
wait $pid102
echo ">>>>>Simulation 102:  465.tonto Tamaño bloque de caché: 128kB"

# Wait for simulation process to finish
wait $pid103
echo ">>>>>Simulation 103:  470.lbm Tamaño bloque de caché: 128kB"

# Wait for simulation process to finish
wait $pid104
echo ">>>>>Simulation 104:  471.omnetpp Tamaño bloque de caché: 128kB"

# Wait for simulation process to finish
wait $pid105
echo ">>>>>Simulation 105:  473.astar Tamaño bloque de caché: 128kB"

# Wait for simulation process to finish
wait $pid106
echo ">>>>>Simulation 106:  481.wrf Tamaño bloque de caché: 128kB"

# Wait for simulation process to finish
wait $pid107
echo ">>>>>Simulation 107:  482.sphinx3 Tamaño bloque de caché: 128kB"

# Wait for simulation process to finish
wait $pid108
echo ">>>>>Simulation 108:  483.xalancbmk Tamaño bloque de caché: 128kB"
echo ""
echo "Simulaciones con Tamaño bloque de caché: 128kB"
echo ""
echo "Revisar txt en directorio '$directory_name'"
echo ""
echo ""
echo ""

echo "Extractor corriendo"
python3 EXTRACTER_BC.py

echo "Mostrando resultados en excel: "
open Results_BC.xlsx