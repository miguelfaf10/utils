import os

def write_pwl_file(time_array, voltage_array, filename):
    """
    Write a PWL file for LTspice from time and voltage numpy arrays.

    Parameters:
    - time_array: np.ndarray of time values (in seconds or with units like 'u' handled outside)
    - voltage_array: np.ndarray of corresponding voltage values
    - filename: str, output file path (e.g., 'wfm.txt')
    """
    if len(time_array) != len(voltage_array):
        raise ValueError("Time and voltage arrays must be the same length.")
    
    with open(filename, 'w') as f:
        for t, v in zip(time_array, voltage_array):
            f.write(f"{t:.9g}\t{v:.9g}\n")

    os.utime(filename, None)