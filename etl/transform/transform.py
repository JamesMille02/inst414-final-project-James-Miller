import pandas as pd
import re
import numpy as np

def clean_film_names(df, column_name):
    """
    Cleans film names in the specified column of a DataFrame by removing 
    leading/trailing whitespace, converting to lowercase, and removing special characters.
    
    Args:
        df (DataFrame): The DataFrame containing the film names.
        column_name (str): The name of the column to clean.

    Returns:
        df (DataFrame): The DataFrame with cleaned film names.
    """
    df[column_name] = df[column_name].fillna('')
    df[column_name] = df[column_name].astype(str).str.strip().str.lower()
    df[column_name] = df[column_name].apply(lambda x: re.sub(r'[^\w\s]', '', x))
    return df

def combine_and_filter_csv():
    """
    Combine and filter CSV files to create a final dataset with specified columns,
    including language region filtering, and add 'been_on_netflix' column.
    """
    # File paths
    ratings_path = 'data/extracted/ratings.csv'
    titles_path = 'data/processed/cleaned_imdb_title.csv'
    language_path = 'data/extracted/language.csv'
    netflix_path = 'data/extracted/media.csv'
    output_path = 'data/processed/combined_imdb.csv'
    
    # Load the CSV files
    ratings_df = pd.read_csv(ratings_path)
    titles_df = pd.read_csv(titles_path)
    netflix_df = pd.read_csv(netflix_path)
    
    # Load only the 'titleID' and 'region' columns from the language file
    language_df = pd.read_csv(language_path, usecols=['titleId', 'region'], on_bad_lines='skip')
    
    # Filter titles to include only movies and tvSeries
    filtered_titles_df = titles_df[titles_df['titleType'].isin(['movie', 'tvSeries'])]
    
    # Filter language data to include only US region
    filtered_language_df = language_df[language_df['region'] == 'US']
    
    # Merge the filtered titles with ratings based on 'tconst'
    merged_df = pd.merge(filtered_titles_df, ratings_df, left_on='tconst', right_on='tconst')
    
    # Further filter merged data based on the filtered language data
    merged_df = pd.merge(merged_df, filtered_language_df, left_on='tconst', right_on='titleId')
    
    # Clean film names for exact matching
    merged_df = clean_film_names(merged_df, 'primaryTitle')
    netflix_df = clean_film_names(netflix_df, 'media')
    
    # Create the final DataFrame with specified columns
    final_df = merged_df[['primaryTitle', 'startYear', 'genres', 'runtimeMinutes', 'averageRating', 'numVotes']]
    
    # Add the 'movie' and 'tvseries' columns using .loc
    final_df.loc[:, 'movie'] = (merged_df['titleType'] == 'movie').astype(int)
    final_df.loc[:, 'tvseries'] = (merged_df['titleType'] == 'tvSeries').astype(int)
    
    # Add 'been_on_netflix' column
    final_df['been_on_netflix'] = final_df['primaryTitle'].isin(netflix_df['media']).astype(int)
    
    # Drop duplicates
    final_df = final_df.drop_duplicates()
    
    # Save to CSV
    final_df.to_csv(output_path, index=False)

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

import pandas as pd

def clean_film_names(df, column_name):
    """
    Cleans film names in the specified column of a DataFrame by removing 
    leading/trailing whitespace and converting to lowercase.

    Args:
        df (DataFrame): The DataFrame containing the film names.
        column_name (str): The name of the column to clean.

    Returns:
        DataFrame: The DataFrame with cleaned film names in the specified column.
    """
    df[column_name] = df[column_name].str.strip().str.lower()
    return df

def merge_oscar_awards():
    """Merges the Oscar awards data into the media ratings with Golden Globes data."""
    
    # File paths
    existing_data_csv = 'data/processed/merged_media_ratings_with_awards.csv'
    oscar_award_csv = 'data/extracted/the_oscar_award.csv'
    output_csv = 'data/processed/merged_media_ratings_with_awards_and_oscar.csv'
    
    # Read the CSV files
    existing_df = pd.read_csv(existing_data_csv)
    oscar_award_df = pd.read_csv(oscar_award_csv)
    
    # Remove leading and trailing spaces from column names
    existing_df.columns = existing_df.columns.str.strip()
    oscar_award_df.columns = oscar_award_df.columns.str.strip()
    
    # Clean film names for exact matching
    existing_df = clean_film_names(existing_df, 'media')
    oscar_award_df = clean_film_names(oscar_award_df, 'film')
    
    # Create columns for Oscar nominations and awards
    existing_df['oscar_nominations'] = 0
    existing_df['oscar_awards'] = 0
    
    # Convert 'winner' to boolean type
    oscar_award_df['winner'] = oscar_award_df['winner'].astype(bool)
    
    # Calculate nominations and awards for each film from Oscars
    oscar_award_stats = oscar_award_df.groupby('film').agg({
        'winner': 'sum',                
        'ceremony': 'count'            
    }).reset_index()
    
    oscar_award_stats.rename(columns={
        'ceremony': 'oscar_nominations',
        'winner': 'oscar_awards'
    }, inplace=True)
    
    # Merge the Oscar awards data with the existing data
    final_merged_df = pd.merge(existing_df, oscar_award_stats, left_on='media', right_on='film', how='left')
    
    # Drop the '_x' columns
    cols_to_drop = [col for col in final_merged_df if col.endswith('_x')]
    final_merged_df.drop(columns=cols_to_drop, inplace=True, errors='ignore')
    
    # Fill NaN values in the '_y' columns with 0
    cols_to_fill = [col for col in final_merged_df if col.endswith('_y')]
    for col in cols_to_fill:
        final_merged_df[col] = final_merged_df[col].fillna(0)
    
    # Rename '_y' columns to remove '_y'
    cols_to_rename = {col: col.replace('_y', '') for col in cols_to_fill}
    final_merged_df.rename(columns=cols_to_rename, inplace=True)
    
    # Drop the extra 'film' column after merging
    final_merged_df.drop(columns=['film'], inplace=True, errors='ignore')
    
    # Write the updated DataFrame to a new CSV file
    final_merged_df.to_csv(output_csv, index=False)

def clean_csv_columns():
    """Reads the combined CSV, drops columns with only zeros, and saves the cleaned DataFrame back to CSV."""
    
    input_csv = 'data/processed/merged_media_ratings_with_awards_and_oscar.csv'
    output_csv = 'data/output/final_netflix_dataset.csv'
    
    # Read the CSV file
    df = pd.read_csv(input_csv)
    
    # Drop columns where all values are zero
    df_cleaned = df.loc[:, (df != 0).any(axis=0)]
    
    # Write the cleaned DataFrame to a new CSV file
    df_cleaned.to_csv(output_csv, index=False)



def merge_imdb_oscar_awards():
    """
    Merges Oscar awards data into a media dataset and updates the dataset with 
    Oscar nominations and awards.
    """
    existing_data_csv = 'data/processed/imdb_dataset_with_awards.csv'
    oscar_award_csv = 'data/extracted/the_oscar_award.csv'
    output_csv = 'data/processed/mergedimdb_media_ratings_with_awards_and_oscar.csv'
    
    # Read the CSV files
    existing_df = pd.read_csv(existing_data_csv)
    oscar_award_df = pd.read_csv(oscar_award_csv)
    
    # Remove leading and trailing spaces from column names
    existing_df.columns = existing_df.columns.str.strip()
    oscar_award_df.columns = oscar_award_df.columns.str.strip()
    
    # Clean film names for exact matching
    existing_df = clean_film_names(existing_df, 'primaryTitle')
    oscar_award_df = clean_film_names(oscar_award_df, 'film')
    
    # Create columns for Oscar nominations and awards
    existing_df['oscar_nominations'] = 0
    existing_df['oscar_awards'] = 0
    
    # Convert 'winner' to boolean type
    oscar_award_df['winner'] = oscar_award_df['winner'].astype(bool)
    
    # Calculate nominations and awards for each film from Oscars
    oscar_award_stats = oscar_award_df.groupby('film').agg({
        'winner': 'sum',                
        'ceremony': 'count'            
    }).reset_index()
    
    oscar_award_stats.rename(columns={
        'ceremony': 'oscar_nominations',
        'winner': 'oscar_awards'
    }, inplace=True)
    
    # Merge the Oscar awards data with the existing data
    final_merged_df = pd.merge(existing_df, oscar_award_stats, left_on='primaryTitle', right_on='film', how='left')
    
    # Drop the '_x' columns
    cols_to_drop = [col for col in final_merged_df if col.endswith('_x')]
    final_merged_df.drop(columns=cols_to_drop, inplace=True, errors='ignore')
    
    # Fill NaN values in the '_y' columns with 0
    cols_to_fill = [col for col in final_merged_df if col.endswith('_y')]
    for col in cols_to_fill:
        final_merged_df[col] = final_merged_df[col].fillna(0)
    
    # Rename '_y' columns to remove '_y'
    cols_to_rename = {col: col.replace('_y', '') for col in cols_to_fill}
    final_merged_df.rename(columns=cols_to_rename, inplace=True)
    
    # Drop the extra 'film' column after merging
    final_merged_df.drop(columns=['film'], inplace=True, errors='ignore')
    
    # Write the updated DataFrame to a new CSV file
    final_merged_df.to_csv(output_csv, index=False)

def clean_imdb_csv_columns():
    """Reads the combined CSV, drops columns with only zeros, and saves the cleaned DataFrame back to CSV."""
    
    input_csv = 'data/processed/mergedimdb_media_ratings_with_awards_and_oscar.csv'
    output_csv = 'data/output/final_imdb_dataset.csv'
    
    # Read the CSV file
    df = pd.read_csv(input_csv)
    
    # Drop columns where all values are zero
    df_cleaned = df.loc[:, (df != 0).any(axis=0)]
    
    # Write the cleaned DataFrame to a new CSV file
    df_cleaned.to_csv(output_csv, index=False)

import pandas as pd

def clean_imdb_title_csv():
    """
    Cleans the IMDb titles CSV file by retaining only the necessary columns up to 'genres'.
    """
    input_csv = 'data/extracted/imdb_title.csv'
    output_csv = 'data/processed/cleaned_imdb_title.csv'
    # Define the columns to keep
    columns_to_keep = ['tconst', 'titleType', 'primaryTitle', 'originalTitle', 'isAdult', 'startYear', 'endYear', 'runtimeMinutes', 'genres']
    
    # Read the CSV file
    try:
        df = pd.read_csv(input_csv, usecols=columns_to_keep)
    except pd.errors.ParserError as e:
        print(f"Error reading {input_csv}: {e}")
        return
    
    # Write the cleaned data to a new CSV file
    df.to_csv(output_csv, index=False)


def merge_media_with_ratings():
    """Merges media CSV with IMDb titles and ratings CSV to include ratings and selected genres."""
    
    media_csv = 'data/extracted/media.csv'
    imdb_title_csv = 'data/processed/cleaned_imdb_title.csv' 
    ratings_csv = 'data/extracted/ratings.csv'
    output_csv = 'data/processed/merged_media_ratings.csv'

    # Read the media CSV file
    media_df = pd.read_csv(media_csv)
    
    # Define the correct column names for the IMDb titles CSV file
    imdb_columns = ['tconst', 'titleType', 'primaryTitle', 'originalTitle', 'isAdult', 'startYear', 'endYear', 'runtimeMinutes', 'genres']
    
    # Read the IMDb titles CSV file with specified columns
    imdb_title_df = pd.read_csv(imdb_title_csv, usecols=['tconst', 'primaryTitle', 'genres'], names=imdb_columns, header=0)
    
    # Read the ratings CSV file
    ratings_df = pd.read_csv(ratings_csv)
    
    
    # Remove duplicates
    media_df = media_df.drop_duplicates()
    imdb_title_df = imdb_title_df.drop_duplicates(subset=['primaryTitle'])
    
    # Trim whitespace and convert to lowercase for matching
    media_df['media'] = media_df['media'].str.strip().str.lower()
    imdb_title_df['primaryTitle'] = imdb_title_df['primaryTitle'].str.strip().str.lower()
    
    # Merge media data with IMDb titles using the 'media' column from media_df and 'primaryTitle' from imdb_title_df
    media_with_titles_df = pd.merge(media_df, imdb_title_df, left_on='media', right_on='primaryTitle', how='left')
    
    # Merge the result with ratings data using the 'tconst' column
    merged_df = pd.merge(media_with_titles_df, ratings_df, on='tconst', how='left')
    
    # Drop rows where ratings are not available
    merged_df = merged_df.dropna(subset=['averageRating', 'numVotes'])
    
    # Drop duplicate rows based on the 'media' column
    merged_df = merged_df.drop_duplicates(subset=['media'])
    
    # Select and rename necessary columns
    merged_df = merged_df[['media', 'dateAdded', 'averageRating', 'numVotes', 'genres']]
    
    # Write the result to a new CSV file
    merged_df.to_csv(output_csv, index=False)



    




