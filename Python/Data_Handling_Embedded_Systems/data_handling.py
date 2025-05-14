# Function to process data from sensors simulating an ADAS sistem.
#   1. Recieve a list of tuples(timestamp,value)
#   2. Filter anomalous data(+- 3 off standard deviation)
#   3. Calculate mobile average


#____Libraries____
import numpy as np

#____Function____
def process_sensor_data(data, window_size=5):
    #################
    # Error handling#
    #################
    if not data:
        print("Empty data")
        return []
    ###################
    # Value extraction#
    ###################
    values = np.array([value for (timestamp,value) in data])
    # The value of the timestamp in the tuple is stored on a numpy array
    #####################
    # Outliers filtering#
    #####################
    mean = np.mean(values)
    std = np.std(values)
    filtered_data = []
    for (t,v) in data:
        # For every key:value in tupla
        if mean - 3*std <= v <= mean + 3*std:
            # Filter values +- std deviation 
            filtered_data.append((t,v))
            # key:value added to list
    # Also can be done: filtered_data = [(t,v) for (t,v) in data if mean - 3*std <= v mean + 3*std]
    #################
    # Moving average#
    #################
    mvg_avg = []
    # Window calculation: avoid overboarding data. Every window has window_size elemnts
    for i in range(len(filtered_data) - window_size +1):
        # Sublist from i to i+window size. i = 0, window = filtered[0:5]
        window = filtered_data[i:i+window_size]
        # Average of window
        avg = sum(v for (t,v) in window)/window_size
        # Store result. Access to the (i+window size-1) tuple to the first elemnt[0] timestamp
        #   Append the avg to that timestamp 
        mvg_avg.append((filtered_data[i+window_size-1][0],avg))
        # Moving average
    return mvg_avg

#____Test case____

sensor_data = [(i, i+np.random.normal(0,1)) for i in range(100)]
print(sensor_data)
print(process_sensor_data(sensor_data))