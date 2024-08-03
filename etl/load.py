import pandas as pd

def load_datasets():
    """
    Load the IMDb dataset with awards and the final Netflix dataset from CSV files.
    
    Returns:
    - imdb_df: DataFrame containing the IMDb dataset with awards.
    - netflix_df: DataFrame containing the final Netflix dataset.
    """
    # File paths
    imdb_path = 'data/processed/imdb_dataset_with_awards.csv'
    netflix_path = 'data/output/final_netflix_dataset.csv'
    
    # Load the CSV files into DataFrames
    imdb_df = pd.read_csv(imdb_path)
    netflix_df = pd.read_csv(netflix_path)
    
    return imdb_df, netflix_df