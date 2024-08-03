import pandas as pd

def clean_film_names(df, column_name):
    """Cleans film names for consistent formatting."""
    df[column_name] = df[column_name].str.strip().str.lower()
    return df

def add_awards_to_media_ratings():
    """Adds columns for nominations and wins to the media ratings and IMDb datasets based on Golden Globes awards data."""
    
    # File paths
    media_ratings_csv = 'data/processed/merged_media_ratings.csv'
    imdb_csv = 'data/processed/combined_imdb.csv'
    awards_csv = 'data/extracted/golden_globe_awards.csv'
    media_output_csv = 'data/processed/merged_media_ratings_with_awards.csv'
    imdb_output_csv = 'data/processed/imdb_dataset_with_awards.csv'
    
    # Read the CSV files
    media_ratings_df = pd.read_csv(media_ratings_csv)
    imdb_df = pd.read_csv(imdb_csv)
    awards_df = pd.read_csv(awards_csv)
    
    # Remove leading and trailing spaces from column names
    media_ratings_df.columns = media_ratings_df.columns.str.strip()
    imdb_df.columns = imdb_df.columns.str.strip()
    awards_df.columns = awards_df.columns.str.strip()
    
    # Clean film names for exact matching
    media_ratings_df = clean_film_names(media_ratings_df, 'media')
    imdb_df = clean_film_names(imdb_df, 'primaryTitle')
    awards_df = clean_film_names(awards_df, 'film')
    
    # Calculate nominations and wins for each film
    nominations_wins = awards_df.groupby('film').agg({'win': 'sum', 'ceremony': 'count'}).reset_index()
    nominations_wins.rename(columns={'ceremony': 'nominations', 'win': 'wins'}, inplace=True)
    
    # Merge the awards data with media ratings data
    media_merged_df = pd.merge(media_ratings_df, nominations_wins, left_on='media', right_on='film', how='left')
    media_merged_df.drop(columns=['film'], inplace=True, errors='ignore')
    media_merged_df['nominations'] = media_merged_df['nominations'].fillna(0)
    media_merged_df['wins'] = media_merged_df['wins'].fillna(0)
    media_merged_df.rename(columns={'wins': 'golden_globe_wins', 'nominations': 'golden_globe_nominations'}, inplace=True)
    media_merged_df.to_csv(media_output_csv, index=False)
    
    # Merge the awards data with IMDb dataset
    imdb_merged_df = pd.merge(imdb_df, nominations_wins, left_on='primaryTitle', right_on='film', how='left')
    imdb_merged_df.drop(columns=['film'], inplace=True, errors='ignore')
    imdb_merged_df['nominations'] = imdb_merged_df['nominations'].fillna(0)
    imdb_merged_df['wins'] = imdb_merged_df['wins'].fillna(0)
    imdb_merged_df.rename(columns={'wins': 'golden_globe_wins', 'nominations': 'golden_globe_nominations'}, inplace=True)
    imdb_merged_df.to_csv(imdb_output_csv, index=False)

    print(f"Media ratings with awards saved to '{media_output_csv}'")
    print(f"IMDb dataset with awards saved to '{imdb_output_csv}'")

# Call the function to execute the process
add_awards_to_media_ratings()
