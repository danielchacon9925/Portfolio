# Implement a FFT to analize power signals.

#____Libraries____
import numpy as np

#____FFT processing function____
def FFT(signal, sampling_rate):
    # Signal size
    n = len(signal)
    # FFT from np
    FFT_t = np.fft.fft(signal)
    # Freq extraction
    freqs = np.fft.fftfreq(n,1/sampling_rate)

    #### Positive freq ####
    # Selects the array from the beginning up to the integrer division n//2
    posiv_freq = freqs[:n//2]
    magnitude = np.abs(FFT_t[:n//2] * 2/n)

    #### Prints #####
    print("Parámetros de señal por transformar:")
    print("\tLa señal recibida es:\t\t"+str(signal)+"\ty tiene un tamaño de\t"+str(n))
    print("Parámetros de transformada:")
    print("\tLa señal recibida transformada es:\t\t"+str(FFT_t)+"\ty tiene una frecuencia de\t"+str(freqs))
    print("\tSu valor de frecuencia es:\t"+str(posiv_freq)+"\ty tiene una magnitud de\t"+str(magnitude))
   



    return posiv_freq, magnitude





#____Test_code_____
sampling_rate = 4000 #4kHz
#____Testing_time_vector_____
# Represents time instants at which the signal is sampled
t = np.linspace(0, 1, sampling_rate, endpoint = False)
#____Signals____
signal = 0.7*np.sin(2*np.pi*50*t) + 0.5*np.sin(2*np.pi*120*t)
# Freq and magnitude of signal
freq, mag = FFT(signal,sampling_rate)
