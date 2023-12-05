---
title: PaleoSampling
---

# Quantitative Analysis of Paleomagnetic Sampling Strategies

This JupyterBook contains notebooks to analyze different sampling procedures in order to estimate the precision of different strategies for estimating paleomagnetic poles and paleosecular variation of the magnetic field based on site magnetizations. It also contains the notebooks that generate all the figures of [Sapienza et al. 2023](https://doi.org/10.1029/2023JB027211).

::::{grid} 1 1 2 2
:class-container: text-center
:gutter: 3

:::{grid-item-card}
:link: ../notebooks/DIY-Figure1
:link-type: doc
:class-header: bg-light

DIY Figure 1 📈
^^^

```{image} ../figures/logo.png
:width: 200
```

This notebook enables a researcher to compute the mean error associated with paleopole estimation given different sampling strategies. It generates a "do-it-yourself" version of Figure 1 of Sapienza et al. 2023 using the theoretical approximation.

:::

:::{grid-item-card}
:link: ../notebooks/Sampling_comparison
:link-type: doc
:class-header: bg-light

Sampling strategy comparison ✏️
^^^

```{image} ../figures/figure3_histogram/Figure3a.png
:width: 250
```

Compare the distribution of paleopole estimation errors for two sampling strategies through simulation. The user can vary parameters (e.g. # of samples per site, outlier rate, and within-site precision) to make their own version of Sapienza et al. 2023 Figure 3.
:::

::::

## Running the notebooks yourself

The notebooks within this JupyterBook book are a static rendition of the code. Running the code yourself enables you to change the parameters to best fit your study by either creating a Python environment to run the code locally or by opening the PaleoSampling repository on Binder.

### Run the code locally 💻

For instructions for how to set up your environment to run the notebooks on your computer, see the [installation instructions](installation.md).

### Run on Binder ☁️

To open a cloud JupyterHub version of the notebooks in this repository and run them on Binder used the following Binder link. Note that the repository will take a long time to load as the environment is being created: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/PolarWandering/PaleoSampling/HEAD)

## How to cite 📖

If you want to cite this work, the citation is:

Sapienza, F., Gallo, L. C., Zhang, Y., Vaes, B., Domeier, M., & Swanson-Hysell, N. L. (2023). Quantitative Analysis of Paleomagnetic Sampling Strategies. Journal of Geophysical Research: Solid Earth, 128, e2023JB027211. https://doi.org/10.1029/2023JB027211

You can use this BibTex citation:
```
@article{Sapienza2023_Quantitative,
author = {Sapienza, F. and Gallo, L. C. and Zhang, Y. and Vaes, B. and Domeier, M. and Swanson-Hysell, N. L.},
title = {Quantitative Analysis of Paleomagnetic Sampling Strategies},
journal = {Journal of Geophysical Research: Solid Earth},
pages = {e2023JB027211},
keywords = {Paleomagnetism, Paleopole estimation, Secular variation, Error quantification},
doi = {https://doi.org/10.1029/2023JB027211},
}
```
If you want to cite the software in this repository, you can instead use the following DOI in Zenodo:

[![DOI](https://zenodo.org/badge/595793364.svg)](https://zenodo.org/badge/latestdoi/595793364)

or use this bibtex entry: 
```
@software{Sapienza_PaleoSampling,
  author = {Sapienza, Facundo and Gallo, Leandro Cesar and Zhang, Yiming and Vaes, Bram and Domeier, Mathew and Swanson-Hysell, Nick},
  title = {PaleoSampling},
  month = sep,
  year = 2023,
  note = {{Quantitative Analysis of Paleomagnetic Sampling Strategies}},
  publisher = {Zenodo},
  version = {v1.0.0},
  doi = {10.5281/zenodo.8347149},
  url = {https://doi.org/10.5281/zenodo.8347149}
}
```

## Contributors

<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="http://facusapienza.com"><img src="https://avatars.githubusercontent.com/u/39526081?v=4?s=100" width="100px;" alt="Facundo Sapienza"/><br /><sub><b>Facundo Sapienza</b></sub></a><br /><a href="#doc-facusapienza21" title="Documentation">📖</a> <a href="#code-facusapienza21" title="Code">💻</a> <a href="#infra-facusapienza21" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a> <a href="#design-facusapienza21" title="Design">🎨</a> <a href="#maintenance-facusapienza21" title="Maintenance">🚧</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/LenGallo"><img src="https://avatars.githubusercontent.com/u/29756069?v=4?s=100" width="100px;" alt="Leandro Gallo"/><br /><sub><b>Leandro Gallo</b></sub></a><br /><a href="#code-LenGallo" title="Code">💻</a> <a href="#bug-LenGallo" title="Bug reports">🐛</a> <a href="#mentoring-LenGallo" title="Mentoring">🧑‍🏫</a> <a href="#design-LenGallo" title="Design">🎨</a> <a href="#question-LenGallo" title="Answering Questions">💬</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://www.swanson-hysell.org"><img src="https://avatars.githubusercontent.com/u/4332322?v=4?s=100" width="100px;" alt="Nick Swanson-Hysell"/><br /><sub><b>Nick Swanson-Hysell</b></sub></a><br /><a href="#review-Swanson-Hysell" title="Reviewed Pull Requests">👀</a> <a href="#doc-Swanson-Hysell" title="Documentation">📖</a> <a href="#design-Swanson-Hysell" title="Design">🎨</a> <a href="#mentoring-Swanson-Hysell" title="Mentoring">🧑‍🏫</a> <a href="#code-Swanson-Hysell" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/matdomeier"><img src="https://avatars.githubusercontent.com/u/40273197?v=4?s=100" width="100px;" alt="matdomeier"/><br /><sub><b>matdomeier</b></sub></a><br /><a href="#ideas-matdomeier" title="Ideas, Planning, & Feedback">🤔</a> <a href="#design-matdomeier" title="Design">🎨</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://www.uu.nl/medewerkers/BVaes"><img src="https://avatars.githubusercontent.com/u/94557078?v=4?s=100" width="100px;" alt="Bram Vaes"/><br /><sub><b>Bram Vaes</b></sub></a><br /><a href="#design-bramvaes" title="Design">🎨</a> <a href="#ideas-bramvaes" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://duserzym.github.io/"><img src="https://avatars.githubusercontent.com/u/39976081?v=4?s=100" width="100px;" alt="Yiming Zhang"/><br /><sub><b>Yiming Zhang</b></sub></a><br /><a href="#ideas-duserzym" title="Ideas, Planning, & Feedback">🤔</a></td>
    </tr>
  </tbody>
</table>