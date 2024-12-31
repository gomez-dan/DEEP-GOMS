import pandas as pd

def preprocess_bulk_rnaseq(input_filepath, output_filepath):
    # Load raw bulk RNA-seq data
    raw_data = pd.read_csv(input_filepath)
    
    # Preprocess the data (normalization, scaling, etc.)
    # This is a placeholder; actual preprocessing steps may vary
    preprocessed_data = raw_data.apply(lambda x: (x - x.mean()) / x.std())

    # Save preprocessed data
    preprocessed_data.to_csv(output_filepath, index=False)

if __name__ == "__main__":
    preprocess_bulk_rnaseq("data/raw/bulk_rnaseq/raw_rnaseq_data.csv", 
                           "data/processed/preprocessed_rnaseq_data.csv")
