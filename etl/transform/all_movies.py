import pandas as pd
import re

def clean_film_names(df, column_name):
    """
    Cleans film names in the specified column of a DataFrame by removing 
    leading/trailing whitespace, converting to lowercase, and removing special characters.
    
    Args:
        df(dataFrame): The DataFrame containing the film names.
        column_name (str): The name of the column to clean.

    Returns:
        df(DataFrame): The DataFrame with cleaned film names 
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
    
    # Save to CSV
    final_df.to_csv(output_path, index=False)
    
    print(f"Final combined CSV saved to '{output_path}'")


