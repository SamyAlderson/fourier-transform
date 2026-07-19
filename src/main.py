import numpy as np
from scipy import fftpack

def complex_abs(z):
    """Calculate the absolute value (magnitude) of a complex number."""
    return np.sqrt(z.real**2 + z.imag**2)

def fft_1d(x, n=None):
    """Perform a 1D Fast Fourier Transform on a real-valued input signal."""
    if n is None:
        n = len(x)
    X = fftpack.fft(x, n=n)
    return X[:n//2 + 1]  # Return only the positive frequency components

def fft_2d(x):
    """Perform a 2D Fast Fourier Transform on a real-valued input signal."""
    X = np.fft.fft2(x)
    return np.fft.fftshift(X)

def cooley_tukey(x, n=None):
    """Implement the Cooley-Tukey algorithm for the Fast Fourier Transform."""
    if n is None:
        n = len(x)
    if n == 1:
        return x
    even = cooley_tukey(x[::2])
    odd = cooley_tukey(x[1::2])
    combined = np.zeros(n, dtype=np.complex128)
    for k in range(n // 2):
        combined[k] = even[k] + np.exp(-2j * np.pi * k / n) * odd[k]
        combined[k + n // 2] = even[k] - np.exp(-2j * np.pi * k / n) * odd[k]
    return combined

def fft(x, n=None, mode='1d'):
    """Perform a Fast Fourier Transform on a real-valued input signal."""
    if mode == '1d':
        return fft_1d(x, n=n)
    elif mode == '2d':
        return fft_2d(x)
    else:
        raise ValueError("Invalid mode. Choose '1d' or '2d'.")

def main():
    """Main entry point for the Fourier Transform program."""
    import argparse
    parser = argparse.ArgumentParser(description='Perform a Fast Fourier Transform on a signal.')
    parser.add_argument('input', type=str, help='Path to the input signal file.')
    parser.add_argument('--mode', type=str, default='1d', help='Choose the transform mode (1d or 2d).')
    parser.add_argument('--n', type=int, default=None, help='Specify the transform length (for 1D FFT).')
    args = parser.parse_args()
    
    try:
        x = np.loadtxt(args.input)
        if len(x.shape) == 2:  # 2D signal
            X = fft(x, mode='2d')
        else:  # 1D signal
            X = fft(x, n=args.n, mode='1d')
        print("Transformed signal:")
        print(X)
    except FileNotFoundError:
        print("Error: Input file not found.")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()