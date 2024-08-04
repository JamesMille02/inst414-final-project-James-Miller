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
    



