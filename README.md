## Quantitative Analysis of Paleomagnetic Sampling Strategies

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/PolarWandering/PaleoSampling/HEAD)

### Installation

All the notebooks inside this notebook can be executed after properly setting the environmnet. The `environment.yml` file can be used to 
install all the requiered dependencies. 

This repository also includes a small python package called `smpsite` that include all the code used to make the simulations and compute the 
estimated poles. In order to install this module, you can simply do 
```
pip install smpsite
```
or 
```
pip install -e smpsite
```
if you are working in developer mode. 


### Makefile

The current repository counts with a `Makefile` that allows the user to run different routines on the code. You can move in a terminal to the 
path to this repository and use the following commnands to trigger their respective actions. 
- `make envs`: Creates the conda environment associated to the `environment.yml` file and then creates the respective iPython kernel such that the 
environment can be accessed via Jupyter notebooks. 
- `make help`: Prints a short description of all available commands and their explanation. 