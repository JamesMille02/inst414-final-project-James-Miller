import pandas as pd

def read_csv(file_path):
    """Reads the CSV file and returns a pandas DataFrame."""
    df = pd.read_csv(file_path)
    return df

def genre_split_by_year(df):
    """Finds the split of the genres for each year."""
    # Extract the year from the 'date added' column
    df['year'] = df['date added'].str.extract(r'(\d{4})')
    
    # Initialize a dictionary to store the genre counts for each year
    genre_counts_by_year = {}
    
    # Iterate over each unique year in the DataFrame
    for year in df['year'].unique():
        # Filter the DataFrame for the current year
        df_year = df[df['year'] == year]
        
        # Split the genres column into multiple rows
        genres_split = df_year['genres'].str.split(',', expand=True).stack().reset_index(level=1, drop=True)
        
        # Remove genres containing numbers or \N
        genres_split = genres_split[~genres_split.str.contains(r'\d|\\N')]
        
        # Count the occurrences of each genre
        genre_counts = genres_split.value_counts().reset_index()
        genre_counts.columns = ['genre', 'count']
        genre_counts['year'] = year
        
        # Add the genre counts for the current year to the dictionary
        genre_counts_by_year[year] = genre_counts
    
    # Concatenate the genre counts for all years into a single DataFrame
    all_genres_counts = pd.concat(genre_counts_by_year.values(), ignore_index=True)
    
    return all_genres_counts

def save_to_csv(df): 
    """Saves the result to a CSV file."""
    output_path = 'data/output/genre_split.csv'
    # Save the DataFrame to a CSV file
    df.to_csv(output_path, index=False)

def read_csv(file_path):
    df = pd.read_csv(file_path)
    return df

def genre_split_by_year(df):
    """Finds the split of the genres for each year."""
    # Extract the year from the 'date added' column
    df['year'] = df['dateAdded'].str.extract(r'(\d{4})')
    
    # Initialize a dictionary to store the genre counts for each year
    genre_counts_by_year = {}
    
    # Iterate over each unique year in the DataFrame
    for year in df['year'].unique():
        # Filter the DataFrame for the current year
        df_year = df[df['year'] == year]
        
        # Split the genres column into multiple rows
        genres_split = df_year['genres'].str.split(',', expand=True).stack().reset_index(level=1, drop=True)
        
        # Remove genres containing numbers or \N
        genres_split = genres_split[~genres_split.str.contains(r'\d|\\N')]
        
        # Count the occurrences of each genre
        genre_counts = genres_split.value_counts().reset_index()
        genre_counts.columns = ['genre', 'count']
        genre_counts['year'] = year
        
        # Add the genre counts for the current year to the dictionary
        genre_counts_by_year[year] = genre_counts
    
    # Concatenate the genre counts for all years into a single DataFrame
    all_genres_counts = pd.concat(genre_counts_by_year.values(), ignore_index=True)
    
    return all_genres_counts

def media_count_by_year(df):
    """counts the number of media added each year and returns a DataFrame."""
    #extract the year from the 'date added' column
    df['year'] = df['dateAdded'].str.extract(r'(\d{4})')
    
    # Count the occurrences of each year
    media_counts = df['year'].value_counts().reset_index()
    media_counts.columns = ['year', 'count']
    media_counts = media_counts.sort_values(by='year', ascending=True)
    
    return media_counts

def save_to_csv(df, output_path):
    """Saves the result to a CSV file."""
    df.to_csv(output_path, index=False)




