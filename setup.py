from setuptools import setup

def get_version():
    """Get the version from the __init__ file in the src directory."""
    import os
    init_path = os.path.join('src', '__init__.py')
    with open(init_path, 'r') as f:
        for line in f:
            if line.startswith('VERSION'):
                return line.split('=')[1].strip().strip('"')
    raise ValueError('Could not find VERSION in src/__init__.py')

setup(
    name='fourier-transform',
    version=get_version(),
    description='A Python implementation of the Fast Fourier Transform (FFT) algorithm for signal processing',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    author='Samy Alderson',
    author_email='samyalder@gmail.com',
    url='https://github.com/samyalder/fourier-transform',
    license='MIT',
    packages=['fourier_transform'],
    install_requires=['numpy', 'scipy'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False
)