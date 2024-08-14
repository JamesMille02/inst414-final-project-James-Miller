import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def read_csv(file_path):
    """
    Reads the CSV file and returns a pandas DataFrame.
    
    Args:
        file_path (str): The path to the CSV file.
    
    Returns:
        DataFrame: The DataFrame containing the data from the CSV file.
    """
    return pd.read_csv(file_path)

def genre_split_by_year(df):
    """
    Finds the split of the genres for each year.
    
    Args:
        df (DataFrame): The DataFrame containing the media data.
    
    Returns:
        DataFrame: A DataFrame with genre counts split by year.
    """
    df['year'] = df['dateAdded'].str.extract(r'(\d{4})')
    genre_counts_by_year = {}
    
    for year in df['year'].unique():
        df_year = df[df['year'] == year]
        genres_split = df_year['genres'].str.split(',', expand=True).stack().reset_index(level=1, drop=True)
        genres_split = genres_split[~genres_split.str.contains(r'\d|\\N')]
        genre_counts = genres_split.value_counts().reset_index()
        genre_counts.columns = ['genre', 'count']
        genre_counts['year'] = year
        genre_counts_by_year[year] = genre_counts
    
    all_genres_counts = pd.concat(genre_counts_by_year.values(), ignore_index=True)
    return all_genres_counts


def plot_genre_split_pie_chart(df):
    """
    Plots a pie chart of the genre split for all years combined.
    
    Args:
        df (DataFrame): The DataFrame containing the genre splits by year.
    """
    genre_counts = df.groupby('genre')['count'].sum().reset_index()
    total_counts = genre_counts['count'].sum()
    
    # Calculate percentage and filter genres less than 3%
    genre_counts['percentage'] = 100 * genre_counts['count'] / total_counts
    other_genres = genre_counts[genre_counts['percentage'] < 3]['count'].sum()
    genre_counts = genre_counts[genre_counts['percentage'] >= 3]
    
    plt.figure(figsize=(10, 10))
    plt.pie(genre_counts['count'], labels=genre_counts['genre'], autopct='%1.1f%%', startangle=140, colors=sns.color_palette('viridis', len(genre_counts)))
    plt.title('Genre Split for All Years Combined')
    plt.axis('equal')
    plt.savefig('./vis/genre_split.png')

def count_added_movies_by_year(file_path):
    """
    Counts the total number of re-added movies for each year and calculates the average of duplicates.
    
    Args:
        file_path (str): The path to the CSV file containing media data.
    
    Returns:
        pd.DataFrame: A DataFrame with counts of re-added movies per year.
        float: The average number of re-added movies per year.
    """
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Extract the year from the 'dateAdded' column
    df['year'] = df['dateAdded'].str.extract(r'(\d{4})')
    
    # Count occurrences of each movie for each year
    df['count'] = df.groupby(['year', 'media'])['media'].transform('count')
    
    # Filter to get only re-added movies (appear more than once)
    df_readded = df[df['count'] > 1]
    
    # Count re-added movies by year
    readded_by_year = df_readded.groupby('year')['count'].sum().reset_index()
    
    # Calculate the average number of re-added movies per year
    average_readded = readded_by_year['count'].mean()
    
    return readded_by_year, average_readded

def plot_added_movies_by_year(readded_by_year, average_readded):
    """
    Plots the re-added movies by year and includes a horizontal line for the average number of re-added movies.
    
    Args:
        readded_by_year (pd.DataFrame): DataFrame containing re-added movie counts by year.
        average_readded (float): The average number of re-added movies per year.
    """
    plt.figure(figsize=(14, 7))
    plt.plot(readded_by_year['year'], readded_by_year['count'], marker='o', label='Added Movies')
    plt.axhline(y=average_readded, color='r', linestyle='--', label=f'Average: {average_readded:.2f}')
    
    plt.title('Added Movies by Year')
    plt.xlabel('Year')
    plt.ylabel('Count of Added Movies')
    plt.legend()
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig('./vis/movies_added_year.png')