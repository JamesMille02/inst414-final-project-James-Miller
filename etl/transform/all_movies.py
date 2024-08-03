import pandas as pd

def combine_and_filter_csv():
    """
    Combine and filter CSV files to create a final dataset with specified columns,
    including language region filtering.
    """
    # File paths
    ratings_path = 'data/extracted/ratings.csv'
    titles_path = 'data/processed/cleaned_imdb_title.csv'
    language_path = 'data/extracted/language.csv'
    output_path = 'data/processed/combined_imdb.csv'
    
    # Load the CSV files
    ratings_df = pd.read_csv(ratings_path)
    titles_df = pd.read_csv(titles_path)
    
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
    
    # Create the final DataFrame with specified columns
    final_df = merged_df[['primaryTitle', 'startYear', 'genres', 'runtimeMinutes', 'averageRating', 'numVotes']]
    
    # Add the 'movie' and 'tvseries' columns using .loc
    final_df.loc[:, 'movie'] = (merged_df['titleType'] == 'movie').astype(int)
    final_df.loc[:, 'tvseries'] = (merged_df['titleType'] == 'tvSeries').astype(int)
    
    # Save to CSV
    final_df.to_csv(output_path, index=False)
    
    print(f"Final combined CSV saved to '{output_path}'")


