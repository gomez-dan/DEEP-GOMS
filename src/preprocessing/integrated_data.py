import pandas as pd

def integrate_data(spatial_meta_filepath, metagenomic_filepath, metabolomic_filepath, rnaseq_filepath, dna_filepath, methylation_filepath, proteome_filepath, codex_filepath, visium_filepath, output_filepath):
    # Load data
    spatial_meta_data = pd.read_csv(spatial_meta_filepath)
    metagenomic_data = pd.read_csv(metagenomic_filepath)
    metabolomic_data = pd.read_csv(metabolomic_filepath)
    rnaseq_data = pd.read_csv(rnaseq_filepath)
    dna_data = pd.read_csv(dna_filepath)
    methylation_data = pd.read_csv(methylation_filepath)
    proteome_data = pd.read_csv(proteome_filepath)
    codex_data = pd.read_csv(codex_filepath)
    visium_data = pd.read_csv(visium_filepath)
    
    # Merge datasets on the sample identifier
    integrated_data = spatial_meta_data.merge(metagenomic_data, on='SampleID') \
                                      .merge(metabolomic_data, on='SampleID') \
                                      .merge(rnaseq_data, on='SampleID') \
                                      .merge(dna_data, on='SampleID') \
                                      .merge(methylation_data, on='SampleID') \
                                      .merge(proteome_data, on='SampleID') \
                                      .merge(codex_data, on='SampleID') \
                                      .merge(visium_data, on='SampleID')
    
    # Save integrated data
    integrated_data.to_csv(output_filepath, index=False)

if __name__ == "__main__":
    integrate_data("data/raw/spatial_metatranscriptomic/data.csv", 
                   "data/raw/metagenomic/data.csv", 
                   "data/raw/metabolomic/data.csv",
                   "data/processed/preprocessed_rnaseq_data.csv", 
                   "data/processed/preprocessed_dna_data.csv", 
                   "data/processed/preprocessed_methylation_data.csv", 
                   "data/processed/preprocessed_proteome_data.csv", 
                   "data/processed/preprocessed_codex_data.csv",
                   "data/processed/preprocessed_visium_data.csv",
                   "data/processed/integrated_data.csv")