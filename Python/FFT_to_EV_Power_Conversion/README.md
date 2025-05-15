# Power Signal FFT Analyzer

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)  
![NumPy](https://img.shields.io/badge/Library-NumPy-orange)  
![Signal Processing](https://img.shields.io/badge/Type-FFT_Analysis-green)

## Description  
A simple Python script that implements the **Fast Fourier Transform (FFT)** to analyze power signals. It extracts the magnitude and frequency of signal components in the positive frequency spectrum—commonly used for inspecting harmonics in power systems, electrical signals, or educational demonstrations.

---

### Core Function: `FFT(signal, sampling_rate)`

Performs frequency analysis on a given signal using FFT.

#### Parameters:
- `signal` *(array-like)*: The time-domain signal to analyze.
- `sampling_rate` *(int)*: Sampling rate in Hz (e.g., 4000 for 4 kHz).

#### Returns:
- `posiv_freq` *(ndarray)*: Array of positive frequency bins (in Hz).
- `magnitude` *(ndarray)*: Corresponding magnitude values for each frequency.

#### Processing Steps:
- Computes FFT using `np.fft.fft`
- Extracts corresponding frequency bins using `np.fft.fftfreq`
- Selects the positive half of the spectrum (`[:n//2]`)
- Normalizes the magnitude

---

### Example Usage

```python
sampling_rate = 4000  # 4 kHz sampling
t = np.linspace(0, 1, sampling_rate, endpoint=False)  # 1 second duration
signal = 0.7 * np.sin(2 * np.pi * 50 * t) + 0.5 * np.sin(2 * np.pi * 120 * t)

freq, mag = FFT(signal, sampling_rate)
