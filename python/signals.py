import numpy as np


def rms(a):
    return np.sqrt(np.mean(np.square(a)))

def repeat_waveform(time_base, voltage_base, period, num_repeats):
    """
    Repeat a base signal over multiple periods.

    Parameters:
    - time_base: np.ndarray, relative time points (e.g., [0, 1e-6, 2e-6])
    - voltage_base: np.ndarray, corresponding voltages
    - period: float, the time period between repeats (in seconds)
    - num_repeats: int, how many times to repeat the wfm

    Returns:
    - time: np.ndarray, full time vector
    - voltage: np.ndarray, full voltage vector
    """
    time = []
    voltage = []

    for i in range(num_repeats):
        t_offset = i * period
        time.extend(time_base + t_offset)
        voltage.extend(voltage_base)
        
    return np.array(time), np.array(voltage)


def estimate_frequency(signal, sampling_rate):
    """
    Estimates the dominant frequency of a periodic signal using FFT.
    
    Parameters:
        signal (np.ndarray): 1D array containing the signal values.
        sampling_rate (float): Sampling rate in Hz.
    
    Returns:
        float: Estimated frequency in Hz.
    """
    n = len(signal)
    freqs = np.fft.fftfreq(n, d=1/sampling_rate)
    fft_values = np.fft.fft(signal)
    
    # Only consider the positive frequencies
    pos_mask = freqs > 0
    freqs = freqs[pos_mask]
    magnitudes = np.abs(fft_values[pos_mask])

    # Get frequency with highest magnitude
    dominant_freq = freqs[np.argmax(magnitudes)]
    return dominant_freq
