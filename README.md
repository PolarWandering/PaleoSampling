### ⚠️ New preprint available! ⚠️

For a detailed description of the project, take a look at [our preprint of a manuscript that is in revision at JGR](https://www.authorea.com/doi/full/10.22541/essoar.168881772.25833701).

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/PolarWandering/PaleoSampling/HEAD) 
[![DOI](https://zenodo.org/badge/595793364.svg)](https://zenodo.org/badge/latestdoi/595793364) 
[![Jupyter Book Badge](https://jupyterbook.org/badge.svg)](https://polarwandering.github.io/PaleoSampling/) 
[![Build Status](https://github.com/PolarWandering/PaleoSampling/actions/workflows/book.yml/badge.svg?branch=main)](https://github.com/PolarWandering/PaleoSampling/actions/workflows/book.yml?query=branch%3Amain)
[![All Contributors](https://img.shields.io/github/all-contributors/PolarWandering/PaleoSampling?color=ee8449&style=flat-square)](#contributors)


## Quantitative Analysis of Paleomagnetic Sampling Strategies

This repository contains all the notebooks and code to reproduce the analysis for the different sampling procedures in order
to estimate the precision of different strategies for estimating paleomagnetic poles and paleosecular variation of the magnetic field
based on site magnetizations.

You can open a cloud JupyterHub version of all the code in this repository and execute it using the following Binder link:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/PolarWandering/PaleoSampling/HEAD)

Learn more about the Binder project in this [link](https://mybinder.readthedocs.io/en/latest/). Note that it will take a very long time to load.

The notebooks in this repository can be directly been access though the following JupyterBook. This link opens a website
where all the notebooks can be visualized.

[![Jupyter Book Badge](https://jupyterbook.org/badge.svg)](https://polarwandering.github.io/PaleoSampling/)

### Organization

This repository includes a series of tools and code organized in different folders:
- `notebooks`: It includes Jupyter Notebooks with examples of different sampling procedures and the code to parallelize the simulations using Dask (`Parallel.ipynb`).
- `figures`: It includes all the Jupyter Notebooks to generate the figures in the paper.
- `outputs`: It includes the simulated data from all the simulations used in the figures in `csv` format.
- `smpsite`: Python package to run simulations and estimate poles and dispersion (see Installation for more information).

We also provide an `environment.yml` and `Makefile` for setup of the computational environment used for this project.

### Installation

All the notebooks inside this notebook can be executed after properly setting the environment. The `environment.yml` file can be used to
install all the required dependencies. Beside some standard Python dependencies, the `environment.yml` file include the installation of
`Pmagpy` using pip and the extra installation of the module `smpsite` (included in this repository). The package `smpsite` includes all the code used to make the simulations and compute the
estimated poles.

In order to install the environment, you can use conda or mamba (see [Managing Environments](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) for more information) with `conda env create -f environment.yml`. Alternatively, we included a `Makefile` that creates the conda environment and installs the associated iPython kernel so this environment can be accessible though Jupyter notebooks all at once. In order to use the Makefile, you need to open a terminal where the repository is located and enter
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

The current repository contains a `Makefile` that allows the user to run different routines on the code. You can move in a terminal to the
path to this repository and use the following commands to trigger their respective actions. 
- `make env`: Creates the conda environment associated with the `environment.yml` file and then creates the respective iPython kernel such that the 
environment can be accessed via Jupyter notebooks. 
- `make help`: Prints a short description of all available commands and their explanation. 

### How to cite 📖

If you want to cite this work, please use this BibTex citation from [our latest preprint](https://www.authorea.com/doi/full/10.22541/essoar.168881772.25833701):
```
@article{sapienza2023quantitative,
  title={Quantitative Analysis of Paleomagnetic Sampling Strategies},
  author={Sapienza, Facundo and Gallo, Leandro Cesar and Zhang, Yiming and Vaes, Bram and Domeier, Mathew and Swanson-Hysell, Nicholas L},
  journal={Authorea Preprints},
  year={2023},
  publisher={Authorea}
}
```
If you want to cite the software in this repository, you can instead use the following DOI in Zenodo:

[![DOI](https://zenodo.org/badge/595793364.svg)](https://zenodo.org/badge/latestdoi/595793364)


## Contributors

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="http://facusapienza.com"><img src="https://avatars.githubusercontent.com/u/39526081?v=4?s=100" width="100px;" alt="Facundo Sapienza"/><br /><sub><b>Facundo Sapienza</b></sub></a><br /><a href="#doc-facusapienza21" title="Documentation">📖</a> <a href="#code-facusapienza21" title="Code">💻</a> <a href="#infra-facusapienza21" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/LenGallo"><img src="https://avatars.githubusercontent.com/u/29756069?v=4?s=100" width="100px;" alt="Leandro Gallo"/><br /><sub><b>Leandro Gallo</b></sub></a><br /><a href="#code-LenGallo" title="Code">💻</a> <a href="#bug-LenGallo" title="Bug reports">🐛</a> <a href="#mentoring-LenGallo" title="Mentoring">🧑‍🏫</a> <a href="#design-LenGallo" title="Design">🎨</a> <a href="#question-LenGallo" title="Answering Questions">💬</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/LenGallo"><img src="https://avatars.githubusercontent.com/u/29756069?v=4?s=100" width="100px;" alt="Leandro Gallo"/><br /><sub><b>Leandro Gallo</b></sub></a><br /><a href="#code-LenGallo" title="Code">💻</a> <a href="#bug-LenGallo" title="Bug reports">🐛</a> <a href="#mentoring-LenGallo" title="Mentoring">🧑‍🏫</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://www.swanson-hysell.org"><img src="https://avatars.githubusercontent.com/u/4332322?v=4?s=100" width="100px;" alt="Nick Swanson-Hysell"/><br /><sub><b>Nick Swanson-Hysell</b></sub></a><br /><a href="#review-Swanson-Hysell" title="Reviewed Pull Requests">👀</a> <a href="#doc-Swanson-Hysell" title="Documentation">📖</a> <a href="#ideas-Swanson-Hysell" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/matdomeier"><img src="https://avatars.githubusercontent.com/u/40273197?v=4?s=100" width="100px;" alt="matdomeier"/><br /><sub><b>matdomeier</b></sub></a><br /><a href="#ideas-matdomeier" title="Ideas, Planning, & Feedback">🤔</a> <a href="#design-matdomeier" title="Design">🎨</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->
