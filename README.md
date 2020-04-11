# GarminDataAnalyser

This repository contains Python code to analyse data recorded with Garmin devices.

## Requirements

- Conda 4.8.3 or newer
- Python 3.8

## Setup instructions

- Clone the repository

- Create the conda environment: 
`conda env create -f environment.yml`

- Activate the environment: 
`conda activate fitanalyser`

- Install the local package in edit mode:
`pip install -e .`

## Conda commands

- Create new blank environment: 
```
conda create --name fitanalyser python=3.8
```

- Create new environment from file:
```
conda env create -f environment.yml
```

- Activate environment:
```
conda activate fitanalyser
```

- Update and prune envionment (from within):
```
conda env update --file environment.in.yml --prune
```

- Save the environment to yml (from within):
```
conda env export > environment.yml
```
