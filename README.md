# fourier-transform
## A Python Implementation of the Fast Fourier Transform (FFT) Algorithm

### Description
The Fast Fourier Transform (FFT) is an efficient algorithm for calculating the discrete Fourier transform (DFT) of a sequence. This project implements the Cooley-Tukey algorithm for the FFT, supporting both 1D and 2D transforms on complex-valued input signals.

### Features

* Implementation of the Cooley-Tukey algorithm for FFT
* Support for 1D and 2D FFT transforms
* Handling of complex-valued input signals

### Dependencies

* `numpy` for efficient numerical computations
* `scipy` for additional scientific computing functionality

### Installation

To install the project, run the following command:

```bash
pip install .
```

This will install the project and its dependencies. Alternatively, you can use a virtual environment to isolate the project dependencies.

### Usage

To use the FFT implementation, import the `fft` module and call the `fft` function with your input signal. For example:

```python
import numpy as np
from fourier_transform import fft

# Generate a sample input signal
signal = np.random.rand(1024)

# Perform the FFT
fft_signal = fft(signal)

# Print the resulting frequency spectrum
print(fft_signal)
```

### Building from Source

To build the project from source, run the following command:

```bash
python setup.py build
```

This will build the project and its dependencies. You can then install the built project using:

```bash
python setup.py install
```

### Project Structure

The project consists of the following files:

* `setup.py`: Build and installation script
* `pyproject.toml`: Project configuration
* `src/main.py`: Main entry point
* `src/utils.py`: Utility functions, including complex number arithmetic and array operations
* `src/fft.py`: Fast Fourier Transform implementation
* `tests/test_fft.py`: Unit tests for the FFT implementation
* `tests/test_utils.py`: Unit tests for utility functions
* `LICENSE`: Project license
* `.gitignore`: Git ignore file

### License

The project is licensed under the MIT License. See the `LICENSE` file for details.