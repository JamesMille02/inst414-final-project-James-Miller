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
    merged_df = merged_df[['media', 'date added', 'averageRating', 'numVotes', 'genres']]
    
    # Write the result to a new CSV file
    merged_df.to_csv(output_csv, index=False)


