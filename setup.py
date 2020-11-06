from setuptools import setup, find_packages

setup(
    name='shrbk',
    version='0.0.1',
    url='https://github.com/CosmoStat/Shear-and-PSF-Reading-Group/',
    author='ShearBook Authors',
    description='Shear book ccompanying code',
    packages=find_packages(),    
    install_requires=['numpy', 'scipy', 'matplotlib'],
)