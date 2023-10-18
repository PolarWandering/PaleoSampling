.ONESHELL:
SHELL = /bin/bash

## env :              Creates conda environment and iPython kernel based on environment.yml file
env :
#	source /srv/conda/etc/profile.d/conda.sh
	conda env create -f environment.yml 
	conda activate paleosampling
	conda install ipykernel
	python -m ipykernel install --user --name paleosampling --display-name "IPython - PaleoSampling"
    
    
.PHONY : help
help : Makefile
	@sed -n 's/^##//p' $<