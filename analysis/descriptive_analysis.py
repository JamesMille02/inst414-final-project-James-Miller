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
    Counts the total number of movies added for each year from 2016 to 2023 and calculates the average number of movies added per year.
    
    Args:
        file_path (str): The path to the CSV file containing media data.
    
    Returns:
        pd.DataFrame: A DataFrame with counts of movies added per year between 2016 and 2023.
        float: The average number of movies added per year.
        float: The average number of movies added per year from 2020 to 2023.
    """
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Extract the year from the 'dateAdded' column
    df['year'] = df['dateAdded'].str.extract(r'(\d{4})')
    
    # Ensure 'year' column is numeric
    df['year'] = pd.to_numeric(df['year'], errors='coerce')
    
    # Filter rows to include only the years between 2016 and 2023
    df = df[df['year'].between(2016, 2023)]
    
    # Count the number of movies added each year
    movies_added_by_year = df.groupby('year').size().reset_index(name='count')
    
    # Calculate the average number of movies added per year
    average_added = movies_added_by_year['count'].mean()
    
    # Calculate the average number of movies added per year from 2020 to 2023
    recent_avg_added = movies_added_by_year[movies_added_by_year['year'].between(2020, 2023)]['count'].mean()
    
    return movies_added_by_year, average_added, recent_avg_added

def plot_added_movies_by_year(readded_by_year, average_readded, recent_avg_added):
    """
    Plots the added movies by year and includes a horizontal line for the average number of added movies, 
    as well as the average from 2020 to 2023 in the legend.
    
    Args:
        readded_by_year (pd.DataFrame): DataFrame containing added movie counts by year.
        average_readded (float): The average number of added movies per year.
        recent_avg_added (float): The average number of added movies per year from 2020 to 2023.
    """
    plt.figure(figsize=(14, 7))
    plt.plot(readded_by_year['year'], readded_by_year['count'], marker='o', label='Added Movies')
    
    # Plot the average line for the entire period (2016-2023)
    plt.axhline(average_readded, color='r', linestyle='--', label=f'Average 2016-2023: {average_readded:.2f}')
    
    # Plot the average line for the period 2020-2023
    plt.axhline(recent_avg_added, color='g', linestyle=':', label=f'Average 2020-2023: {recent_avg_added:.2f}')
    
    plt.title('Added Movies by Year')
    plt.xlabel('Year')
    plt.ylabel('Count of Added Movies')
    plt.legend()
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig('./vis/movies_added_year.png')



def genre_split(df):
    """
    Finds the split of the genres across the entire dataset.
    
    Args:
        df (DataFrame): The DataFrame containing the media data.
    
    Returns:
        DataFrame: A DataFrame with genre counts.
    """
    # Split genres into rows and remove invalid entries
    genres_split = df['genre'].str.split(',', expand=True).stack().reset_index(level=1, drop=True)
    genres_split = genres_split[~genres_split.str.contains(r'\d|\\N', na=False)]

    # Count genres
    genre_counts = genres_split.value_counts().reset_index()
    genre_counts.columns = ['genre', 'count']
    
    return genre_counts

def rec_plot_genre_split_pie_chart(df):
    """
    Plots a pie chart of the top 10 genre splits for the entire dataset.
    
    Args:
        df (DataFrame): The DataFrame containing the genre counts.
    """

    # Filter to include only the top 10 genres with the largest counts
    top_8_genres = df.nlargest(8, 'count')

    # Plot the pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(
        top_8_genres['count'],
        labels=top_8_genres['genre'],
        autopct='%1.1f%%',  
        startangle=140,
        colors=sns.color_palette('viridis', len(top_8_genres))
    )
    plt.title('Top 8 Genre Split for Entire Dataset')
    plt.axis('equal')  
    plt.savefig('./vis/rec_genre_split_top_8.png')
