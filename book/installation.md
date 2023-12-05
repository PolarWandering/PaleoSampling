## Installation

All the notebooks inside this JupyterBook can be executed after properly setting the environment. The `environment.yml` file in the [GitHub repository](https://github.com/PolarWandering/PaleoSampling) can be used to
install all the required dependencies. Beside some standard Python dependencies, the `environment.yml` file include the installation of
`Pmagpy` using pip and the extra installation of the module `smpsite` (included in this repository). The package `smpsite` includes all the code used to make the simulations and compute the
estimated poles.

In order to install the environment, you can use conda or mamba (see [Managing Environments](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) for more information) with `conda env create -f environment.yml`. Once the environment is created, you can create the associated iPython kernel with 
```
python -m ipykernel install --user --name paleostats --display-name "IPython - PaleoStats"
```
This will allow you to execute this environment directly from Jupyter notebooks. 

Alternatively, we included a `Makefile` in the [GitHub repository](https://github.com/PolarWandering/PaleoSampling) that creates the conda environment and installs the associated iPython kernel so this environment can be accessible though Jupyter notebooks all at once. In order to use the Makefile, you need to open a terminal where the repository is located and enter
```
make env
```

Alternatively, if you just want to install the `smpsite` module, you can clone this repository and do
```
pip install smpsite
```
or
```
pip install -e smpsite
```
if you are working in developer mode. 

### Makefile

The current [repository](https://github.com/PolarWandering/PaleoSampling) contains a `Makefile` that allows the user to run different routines on the code. You can move in a terminal to the
path to this repository and use the following commands to trigger their respective actions. 
- `make env`: Creates the conda environment associated with the `environment.yml` file and then creates the respective iPython kernel such that the 
environment can be accessed via Jupyter notebooks. 
- `make help`: Prints a short description of all available commands and their explanation. 