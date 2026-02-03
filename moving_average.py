import numpy as np

def moving_average(signal, window_size):
    signal = np.array(signal, dtype=float)
    n = len(signal)
    k = (window_size - 1) // 2

    result = np.zeros(n, dtype=float)

    for i in range(n):
        start = max(0, i - k)
        end = min(n - 1, i + k)
        result[i] = np.mean(signal[start:end + 1])

    return result


