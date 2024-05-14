# OpenLane Parameter Exploration

## Table of Contents
- [Introduction](#introduction)
- [Configuration](#configuration)
- [Experiment Data](#experiment-data)
- [Results](#results)
- [Data generation from random configurations](#data-generation-from-random-configurations)
- [The clock period at which the flow successfully completes](#the-clock-period-at-which-the-flow-successfully-completes)
- [The core usage percentage at which the flow successfully completes](#the-core-usage-percentage-at-which-the-flow-successfully-completes)
- [Reports and values](#reports-and-values)


## Introduction
The principal aim of this project is to meticulously analyze the performance repercussions arising from variances in the configurations stipulated within the config.json file. By engaging in methodical experimentation encompassing a wide array of settings and parameters, our aim is to procure comprehensive insights into the significant impact these configurations wield over the comprehensive functionality and operational efficacy of the system.

The secondary objective entails conducting experiments on OpenLane design exemplars to ascertain the initial clock period value and core utilization that facilitate the successful completion of the OpenLane flux while adhering to the default configuration for each design. 

## Configuration
To initiate the analysis, follow these steps:

1. **Configuration Changes**: Start by modifying the configurations within the `config.json` file to suit your experimental requirements.

2. **Running the OpenLane Flow**: Execute the complete OpenLane flow with the updated configurations.

3. **Data Extraction**: Utilize the "EXTRACTER.py" script to extract timing data. This script also appends the obtained data to two separate data tables:
   - The general data table, "tabla_data.csv," which aggregates data from all experiments.
   - The Floorplaning data table, "Floorplaning_data.csv."
4. **Random Optimizations**: Execute the Python code "Randomizer.py" and specify the design intended for testing. The configurations previously discovered are stored in a dictionary with random attributes.
5. **Starting clk period and core utility values**: To streamline the multiple testing process, the code "PERIOD_UTIL_Randomizer.py" manages the selection of the design and prompts the user to specify the number of experiments. Considering that each test builds upon the preceding one, it is advisable to conduct more than 50 experiments per design.

In the event of inadvertent data table overwriting, as has occurred previously, the 'RECOVER.py' script can be employed to append all experimental data to the existing data table.


## Experiment Data

The initial 24 experiments are dedicated to capturing synthesis data. Subsequently, additional data tables will be introduced to accommodate information stemming from subsequent stages of the analysis.

## Results

### Synthesis
#### Configurations Influencing Performance

In this section, we describe the implemented configurations that have a notable impact on circuit performance.

##### SYNTH_STRATEGY
Selects the priority in synthesis strategy and mapping technology.

Available options:
- **DELAY**: Indicates a priority on delay optimization. Available values are **0-4**.
- **AREA**: Indicates a priority on area optimization. Available values are **0-3**.

When implementing these configurations on the "picorv32a" circuit, selecting **DELAY: 4** results in the **lowest timing values**.

##### SYNTH_ADDER_TYPE
Selects the type of adder implemented during synthesis. Its significance lies in the fact that the type of adder implements logical functions that can have more or fewer logic cells depending on the case.

Available options:
- **FA**: Full Adder structure. Adds two inputs, considering the carry-in.
- **YOSYS**: Uses YOSYS's internal definition of an adder.
- **RCA**: Uses the ripple carry structure, passing the output carry as the input carry for the final summation stage.
- **CSA**: The carry select adder implements two full adders. One assumes no input carry, and the other does. Subsequently, a multiplexer selects the output sum.

Among the configurations mentioned above, the adder that allows for the **lowest timing values** is **FA**.

##### SYNTH_BUFFERING
Configuration that enables or disables the insertion of buffer stages for signal paths.

##### SYNTH_BUFFER_DIRECT_WIRES
Enables or disables the insertion of buffer cells on connected wires.

### Floorplaning

##### FP_CORE_UTIL

Indicates the percentage of core area utilized by the implementation.

##### FP_ASPECT_RATIO 
Selects the aspect ratio of the width to the design size. This setting is deprecated when implementing "absolute," which indicates that there will be no specific ratio, and it will be indicated by the DIE AREA.

##### FP_SIZING
Indicates whether the circuit area will be relative or absolute, which will be provided by the DIE AREA.

##### DIE_AREA
Specifies the circuit area through coordinates (x1 x2 y1 y2).

The picorv32a circuit has the following original dimensions:

- **Height**: 476.03
- **Width**: 465.31009

Modifying the width and height of the circuit allows for placing larger cells and accommodating more cells within the circuit, respectively. This is because expanding the width allows for the use of cells with more inputs, and increasing the height enables the arrangement of more cells on top of each other.

### Placement

##### PL_TARGET_DENSITY 
Indicates the desired density in cell placement. Its parameters "closely dense" and "widely spread" indicate the selection criteria.

##### PL_TIME_DRIVEN
The placement is done considering the path that consumes the least time.

##### PL_ROUTABILITY_DRIVEN
Indicates whether the placement should be routability-driven.

### Routing

#### GLB_RESIZER_TIMING_OPTIMIZATIONS
The resizer is a tool used in integrated circuit design to automatically adjust the sizes of logic gates to meet timing requirements and improve circuit performance.

#### GLB_RESIZER_DESIGN_OPTIMIZATIONS
Automatically adjusts the sizes of logic gates to meet timing requirements and improve circuit performance.

#### GLB_RESIZER_MAX_WIRE_LENGTH
Maximum allowed length of interconnections or wires within the circuit design used by the resizer for buffer insertion.

 <!-- #### GLB_RESIZER_MAX_SLEW_MARGIN-->
<!--  Maximum allowable margin for variation in signal transition speed within the circuit.-->

 <!--  #### GLB_RESIZER_MAX_CAP_MARGIN
Maximum allowable margin for capacitance in the circuit design.-->

<!-- #### GLB_RESIZER_HOLD_SLACK_MARGIN
Maximum slack margin allowed for hold times in the circuit when hold violations are resolved.

#### GLB_RESIZER_SETUP_SLACK_MARGIN
 Maximum slack margin allowed for setup times in the circuit when setup violations are resolved.-->
<!--
#### GLB_RESIZER_HOLD_MAX_BUFFER_PERCENT
Maximum percentage of buffers allowed to resolve setup violations.

#### GLB_RESIZER_SETUP_MAX_BUFFER_PERCENT
Maximum percentage of buffers allowed to resolve setup violations.

#### GLB_RESIZER_ALLOW_SETUP_VIOS
Enable or disable setup timing violation in the circuit design.-->


## Data generation from random configurations

In order to get the most random results posible, a random test generator was created. Randomizer.py select the design specified by the user to insert N random configurations from the dictonary. 

Each design entails a distinct set of specific configurations crucial for the successful completion of the workflow. While conducting random test experiments, an issue surfaced when none of the previously identified configurations proved sufficient to facilitate the completion of the workflow.

To explore various optimizations for OpenLane designs, the focus was shifted to a new paradigm. Random clock periods were applied to ascertain the period that enables the successful completion of the workflow.

## The clock period at which the flow successfully completes

To determine the clock period at which the flow successfully completes, the initial step involves checking whether "CLOCK_PERIOD" is specified in the config.json file. If no "CLOCK_PERIOD" is defined, a new one with a value of 0.5 ns will be added.

Subsequently, a random percentage (ranging from 0.05 to 0.08) of the "CLOCK_PERIOD" will be employed to execute the initial flow, which is anticipated to fail. The variable COUNT represents the desired number of experiments for the particular design. For each unsuccessful run, an additional 1 ns will be added to the "CLOCK_PERIOD" until the flow achieves successful completion.

For each selected design, a text file with a TAG corresponding to the run will be generated. This file will contain information pertaining to the original clock period (either initially added or specified), the percentage of the original clock period used in the first run, and the subsequent clock periods applied until the flow achieves success. 

## The core usage percentage at which the flow successfully completes

To determine the core usage percentage at which the flow successfully completes, the initial step involves checking whether "FP_CORE_UTIL" is specified in the config.json file. If no, a new one with a value of 0.20% will be added.

Subsequently, a random percentage (ranging from 0.05 to 0.10) of the "FP_CORE_UTIL" will be employed to execute the initial flow, which is anticipated to fail. For each unsuccessful run, an additional 5% will be added.

For each selected design, a text file with a TAG corresponding to the run will be generated. This file will contain information pertaining to the original core usage percentage (either initially added or specified) and the subsequent percentages applied until the flow achieves success.

## Reports and values

| Design             | Report                                                   | Value (ns) | Min value (%) | Max value (%) |
| ------------------ | -------------------------------------------------------- | ---------- | ------------- | ------------- |
| s44                | s44_8_30.txt, s44_COREUTIL_50_4.txt and s44_COREUTIL_50_5_TOGND.txt | 3.785 | 5  | 45  |
| spm                | spm_8_10.txt, spm_COREUTIL_50_0.2.txt and spm_COREUTIL_80_5_TOGND.txt                | 0.719      | 5             | 80   |
| PPU                | PPU_8_0.5.txt, PPU_COREUTIL_80_20.txt and PPU_COREUTIL_80_7_TOGND.txt                 | 6.040      | 7             | 30   |
| pipeline_8b_adder  | pipeline_8b_adder_50_3.18.txt, pipeline_8b_adder_COREUTIL_50_0.5.txt and pipeline_8b_adder_COREUTIL_80_45_TOGND.txt | 3.213 | 45  | 90   |
| mem_1r1w           | mem_1r1w_50_10.0.txt, mem_1r1w_COREUTIL_55_0.2.txt and mem_1r1w_COREUTIL_80_40_TOGND.txt  | 2.629      | 40            | 65   |
| usb                | usb_50_0.5.txt, usb_COREUTIL_80_40.txt and usb_COREUTIL_80_34_TOGND.txt                 | 3.033      | 34            | 70   |
| wbqspiflash        | wbqspiflash_50_0.5.txt, wbqspiflash_COREUTIL_80_0.2.txt and wbqspiflash_COREUTIL_80_5_TOGND.txt | 5.028    | 5             | 40   |
| zipdiv             | zipdiv_50_0.5.txt, zipdiv_COREUTIL_50_0.2.txt and zipdiv_COREUTIL_80_5_TOGND.txt        | 4.031      | 5             | 85   |
| picorv32a          | picorv32a_50_10.txt, picorv32a_COREUTIL_50_35.txt and picorv32a_COREUTIL_80_12_TOGND.txt    | 0          | 12            | 35   |


## Author

- **Daniel Chacón Mora**
- Student ID: B72018
