import pandas as pd

def clean_film_names(df, column_name):
    """
    Cleans film names in the specified column of a DataFrame by removing 
    leading/trailing whitespace and converting to lowercase.

    Args:
        df (pd.DataFrame): The DataFrame containing the film names.
        column_name (str): The name of the column to clean.

    Returns:
        pd.DataFrame: The DataFrame with cleaned film names in the specified column.
    """
    df[column_name] = df[column_name].str.strip().str.lower()
    return df

def merge_oscar_awards(input_csv, output_csv):
    """
    Merges Oscar awards data into a media dataset and updates the dataset with 
    Oscar nominations and awards, filling in missing data with zeros.

    Args:
        input_csv (str): Path to the input media dataset CSV file.
        output_csv (str): Path to the output CSV file where the merged data will be saved.
    """
    
    # File path for the Oscar awards data
    oscar_award_csv = 'data/extracted/the_oscar_award.csv'
    
    # Read the CSV files
    media_df = pd.read_csv(input_csv)
    oscar_award_df = pd.read_csv(oscar_award_csv)
    
    # Remove leading and trailing spaces from column names
    media_df.columns = media_df.columns.str.strip()
    oscar_award_df.columns = oscar_award_df.columns.str.strip()
    
    # Clean film names for exact matching
    media_df = clean_film_names(media_df, 'primaryTitle' if 'primaryTitle' in media_df.columns else 'media')
    oscar_award_df = clean_film_names(oscar_award_df, 'film')
    
    # Create columns for Oscar nominations and awards if they do not exist
    if 'oscar_nominations' not in media_df.columns:
        media_df['oscar_nominations'] = 0
    if 'oscar_awards' not in media_df.columns:
        media_df['oscar_awards'] = 0
    
    # Calculate nominations and awards for each film from Oscars
    oscar_award_stats = oscar_award_df.groupby('film').agg({
        'winner': 'sum',                # Sum of True values gives the number of awards (wins)
        'ceremony': 'count'            # Count of all entries gives the number of nominations
    }).reset_index()
    
    oscar_award_stats.rename(columns={
        'ceremony': 'oscar_nominations',
        'winner': 'oscar_awards'
    }, inplace=True)
    
    # Merge the Oscar awards data with the media data
    final_merged_df = pd.merge(media_df, oscar_award_stats, left_on='primaryTitle' if 'primaryTitle' in media_df.columns else 'media', right_on='film', how='left')
    
    # Ensure 'oscar_nominations' and 'oscar_awards' columns exist and fill missing values with 0
    if 'oscar_nominations' not in final_merged_df.columns:
        final_merged_df['oscar_nominations'] = 0
    if 'oscar_awards' not in final_merged_df.columns:
        final_merged_df['oscar_awards'] = 0
    
    final_merged_df['oscar_nominations'] = final_merged_df['oscar_nominations'].fillna(0).astype(int)
    final_merged_df['oscar_awards'] = final_merged_df['oscar_awards'].fillna(0).astype(int)
    
    # Fill missing values for Golden Globe columns with 0
    for col in ['golden_globe_wins', 'golden_globe_nominations']:
        if col not in final_merged_df.columns:
            final_merged_df[col] = 0
        final_merged_df[col] = final_merged_df[col].fillna(0).astype(float)
    
    # Ensure no extra columns are left after merging
    if 'film' in final_merged_df.columns:
        final_merged_df.drop(columns=['film'], inplace=True, errors='ignore')
    
    # Write the updated DataFrame to a new CSV file
    final_merged_df.to_csv(output_csv, index=False)
    
    print(f"Final merged CSV saved to '{output_csv}'")
