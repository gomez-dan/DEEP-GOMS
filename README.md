# DEEP-GOMS: Deep Evolutionary Ensemble Predictor for Gut OncoMicrobiome Signatures

### Overview
The DEEP-GOMS project aims to develop a reproducible next-generation biomarker prediction model for combinatorial immune checkpoint blockade (CICB) response in early-stage I-II cancers. This innovative approach integrates multi-omics data, including metagenomic, spatial meta-transcriptomic, and metabolomic analyses, to identify reproducible gut microbiome signatures (GOMS) associated with CICB response. The model incorporates advanced machine learning techniques and considers emerging cancer immunotherapy modalities beyond traditional immune checkpoint inhibitors.

## Key Features
Integrates multi-omics data including shotgun metagenomic sequencing, spatial meta-transcriptomics, and metabolomics to provide a comprehensive view of the gut microbiome.
Utilizes advanced feature selection techniques like LASSO, Ridge Regression, and tree-based model feature importance.
Employs deep learning architectures such as Convolutional Neural Networks for complex data integration and prediction tasks.
Considers emerging immunotherapy approaches including CAR T-cell therapy, TCR-engineered T cells, neoantigen vaccines with dendritic cells, and exercise immunotherapy.
Incorporates automated pipeline using Snakemake and Nextflow for reproducibility and scalability.

## Project Structure
The project is organized into the following directories:

data/: Contains raw, processed, and external datasets.
notebooks/: Jupyter notebooks for interactive data analysis and development.
src/: Source code for data preprocessing, feature selection, model training, and evaluation.
models/: Stores trained models and related artifacts.
results/: Contains figures, tables, and reports generated during analysis.
tests/: Unit tests for ensuring code quality and correctness.
scripts/: Standalone scripts for running different parts of the pipeline.
workflows/: Configuration files for pipeline automation using Snakemake and Nextflow.
requirements.txt: Lists the dependencies required for the project.
README.md: Provides an overview and instructions for setting up and running the project.
.gitignore: Specifies files and directories to be ignored by Git.

Getting Started
1. Clone the Repository:
```
git clone <repository_url>
cd DEEP-GOMS
```
2. Install Dependencies:
```
pip install -r requirements.txt
```
3. Run the Pipeline:
* Using Snakemake:
```
snakemake --cores <number_of_cores>
```
* Using Nextflow:
```
nextflow run workflows/nextflow.config
```


Explore Notebooks: Open and run the Jupyter notebooks in the ```notebooks/``` directory to interactively explore data preprocessing, feature selection, model training, and evaluation.

This project provides a robust framework for developing and validating a predictive model for CICB response, leveraging state-of-the-art techniques in multi-omics data integration and machine learning.
