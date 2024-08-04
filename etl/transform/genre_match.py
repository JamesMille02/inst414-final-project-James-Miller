import pandas as pd
import numpy as np

def process_genres(imdb_path, netflix_path, updated_imdb_path, updated_netflix_path):
    # Load the datasets
    imdb_df = pd.read_csv(imdb_path)
    netflix_df = pd.read_csv(netflix_path)

    # Extract unique genres from the IMDb dataset, filtering out numeric values
    imdb_genres = imdb_df['genres'].dropna().str.split(',').explode().unique()
    imdb_genres = [genre for genre in imdb_genres if not genre.isdigit()]

    # Create a mapping of genres to numeric identifiers
    genre_to_id = {genre: idx for idx, genre in enumerate(imdb_genres)}

    # Function to map genres to numeric identifiers
    def map_genres_to_ids(genres):
        if pd.isna(genres):
            return np.nan
        genre_ids = [genre_to_id[genre] for genre in genres.split(',') if genre in genre_to_id]
        return ','.join(map(str, genre_ids))
    
    # Apply the mapping to both datasets
    imdb_df['genres'] = imdb_df['genres'].apply(map_genres_to_ids)
    netflix_df['genres'] = netflix_df['genres'].apply(map_genres_to_ids)
    
    # Drop rows with NaN genres
    imdb_df = imdb_df.dropna(subset=['genres'])
    netflix_df = netflix_df.dropna(subset=['genres'])

    # Save the updated datasets
    imdb_df.to_csv(updated_imdb_path, index=False)
    netflix_df.to_csv(updated_netflix_path, index=False)

    return genre_to_id


