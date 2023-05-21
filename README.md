## Quantitative Analysis of Paleomagnetic Sampling Strategies

This repository contains all the requirement notebooks and code to reproduce the analysis for the different sampling procedures in order
to estimate the precision of different strategies at the moment of estimating paleomagnetic poles and secular variation of the magnetic field 
based on site observations. 

You can open a cloud JupyterHub version of all the code in this repository and execute it using the following Binder link:
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/PolarWandering/PaleoSampling/HEAD)
Lear more about the Binder project in this [link](https://mybinder.readthedocs.io/en/latest/).

### Organization

This repository includes a series of tools and code organized in different folders. 
- `notebooks`: It includes Jupyter Notebooks with examples of different sampling procedures and the code to parallelize the simulations using Dask (`Parallel.ipynb`).
- `figures`: It includes all the Jupyter Notebooks to generate the figures in the paper. 
- `outputs`: It inclides the simulated data from all the simulations used in the figures in `csv` format.
- `smpsite`: Python package to run simulations and estimate poles and dispersion (see Installation for more information). 

We also provide with an `environment.yml` and `Makefile` for setup of the computational environment used for this project. 

### Installation

All the notebooks inside this notebook can be executed after properly setting the environmnet. The `environment.yml` file can be used to 
install all the requiered dependencies. Beside some standard Python dependencies, the `environment.yml` file include the installation of 
`Pmagpy` using pip and the extra installation of the module `smpsite` (included in this repository). The package `smpsite` includes all the code used to make the simulations and compute the 
estimated poles. 

In order to install the environment, you can use conda or mamba (see [Managing Environments](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) for more information) with `conda env create -f environment.yml`. Alternativelly, we included a `Makefile` that allow to create the conda environment and install the associated iPython kernel so this environment can be accessible though Jupyter notebooks all at once. In order to do this, you just need to open a terminal where the repository is located and enter
```
make env
```

Alternativelly, if you just want to install the `smpsite` modeule, you can simply clone this repository and do 
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
- `make env`: Creates the conda environment associated to the `environment.yml` file and then creates the respective iPython kernel such that the 
environment can be accessed via Jupyter notebooks. 
- `make help`: Prints a short description of all available commands and their explanation. 