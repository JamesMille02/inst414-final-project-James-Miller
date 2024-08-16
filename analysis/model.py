import pandas as pd
import numpy as np

def preprocess_data(imdb_df, netflix_df):
    """
    Preprocess the IMDb and Netflix DataFrames by converting genres to numeric identifiers 
    and filtering out non-movie entries in the IMDb DataFrame.
    
    Args:
        imdb_df (DataFrame): The DataFrame containing IMDb movie data.
        netflix_df (DataFrame): The DataFrame containing Netflix movie data.
    
    Returns:
        imdb_df (DataFrame): IMDb DataFrame, 
        netflix_df (DataFrame): the processed Netflix DataFrame, 
        genre_to_id (dict): a dictionary mapping genre names to numeric IDs.
    """
    imdb_df['genres'] = imdb_df['genres'].astype(str)
    netflix_df['genres'] = netflix_df['genres'].astype(str)
    imdb_df = imdb_df[imdb_df['movie'] == 1].copy()
    
    all_genres = pd.concat([imdb_df['genres'], netflix_df['genres']]).dropna().str.split(',').explode().unique()
    all_genres = [genre for genre in all_genres if not genre.isdigit()]
    genre_to_id = {genre: idx for idx, genre in enumerate(all_genres)}

    def map_genres_to_ids(genres):
        if pd.isna(genres):
            return np.nan
        genre_ids = [genre_to_id[genre] for genre in genres.split(',') if genre in genre_to_id]
        return ','.join(map(str, genre_ids))
    
    imdb_df.loc[:, 'genres'] = imdb_df['genres'].apply(map_genres_to_ids)
    netflix_df.loc[:, 'genres'] = netflix_df['genres'].apply(map_genres_to_ids)
    imdb_df = imdb_df.dropna(subset=['genres'])
    netflix_df = netflix_df.dropna(subset=['genres'])
    
    return imdb_df, netflix_df, genre_to_id

def calculate_average_characteristics(netflix_df):
    """
    Calculate the average characteristics for movies in the Netflix DataFrame.
    
    Args:
        netflix_df (DataFrame): The DataFrame containing Netflix movie data.
    
    Returns:
        avg_characteristics (Series): A Series containing the average values for numeric characteristics.
    """
    numeric_columns = ['averageRating', 'numVotes', 'golden_globe_wins', 'golden_globe_nominations', 'oscar_awards', 'oscar_nominations']
    avg_characteristics = netflix_df[numeric_columns].mean()
    return avg_characteristics

def calculate_distance_matrix(df, avg_characteristics):
    """
    Calculate the Euclidean distance between each movie's characteristics and the average characteristics.
    
    Args:
        df (pd.DataFrame): The DataFrame containing movie data.
        avg_characteristics (pd.Series): A Series containing average characteristics for comparison.
    
    Returns:
        np.ndarray: An array of distances between each movie's characteristics and the average characteristics.
    """
    df_numeric = df[['averageRating', 'numVotes', 'golden_globe_wins', 'golden_globe_nominations', 'oscar_awards', 'oscar_nominations']].values
    avg_values = np.array([avg_characteristics[col] for col in ['averageRating', 'numVotes', 'golden_globe_wins', 'golden_globe_nominations', 'oscar_awards', 'oscar_nominations']])
    distances = np.sqrt(np.sum((df_numeric - avg_values) ** 2, axis=1))
    return distances

def predict_movies_to_license(imdb_df, avg_characteristics, top_n=1962):
    """
    Predict movies to license by calculating their distance from the average characteristics 
    and selecting the top N movies closest to the average.
    
    Args:
        imdb_df (pd.DataFrame): The DataFrame containing IMDb movie data.
        avg_characteristics (pd.Series): A Series containing average characteristics for comparison.
        top_n (int): The number of top movies to select based on distance.
    
    Returns:
        pd.DataFrame: The top N recommended movies based on their distance from the average characteristics.
    """
    imdb_df['distance_from_avg'] = calculate_distance_matrix(imdb_df, avg_characteristics)
    
    recommendations = imdb_df.sort_values('distance_from_avg').head(top_n)
    
    print(f"Number of recommendations: {len(recommendations)}")
    
    return recommendations

def evaluate_characteristics(recommendations_df, netflix_df):
    """
    Evaluate the average characteristics of the recommended movies and compare them with 
    the characteristics of movies in the Netflix DataFrame.
    
    Args:
        recommendations_df (DataFrame): The DataFrame containing recommended movies.
        netflix_df (DataFrame): The DataFrame containing Netflix movie data.
    """
    if recommendations_df is not None and not recommendations_df.empty:
        numeric_columns = ['averageRating', 'numVotes', 'golden_globe_wins', 'golden_globe_nominations', 'oscar_awards', 'oscar_nominations']
        avg_recommendations = recommendations_df[numeric_columns].mean()
        print("Average characteristics of recommended movies:")
        print(avg_recommendations)
    else:
        print("Recommendations DataFrame is None or empty. Cannot evaluate characteristics.")

    net_numeric_columns = ['averageRating', 'numVotes', 'golden_globe_wins', 'golden_globe_nominations', 'oscar_awards', 'oscar_nominations']
    net_avg_recommendations = netflix_df[net_numeric_columns].mean()

    print('Netflix averages:')
    print(net_avg_recommendations)


def revert_genre_ids(recommendations, genre_to_id, save_path='data/output/model_recommendations.csv'):
    """
    Convert genre IDs back to their original string format and save the DataFrame to a CSV file.
    
    Args:
        recommendations (df): data frame of recommendations
        genre_to_id (dict): A dictionary mapping genre names to numeric IDs.
        save_path (str): The path to save the CSV file with the model recommendations.
    
    Returns:
        recommendations (DataFrame): recommendations DataFrame with genres as strings.
    """
    id_to_genre = {idx: genre for genre, idx in genre_to_id.items()}

    def map_ids_to_genres(genre_ids):
        if pd.isna(genre_ids) or genre_ids == '':
            return np.nan
        genres = [id_to_genre[int(genre_id)] for genre_id in genre_ids.split(',') if genre_id.isdigit()]
        return ','.join(genres)
    
    recommendations['genre'] = recommendations['genres'].apply(map_ids_to_genres)

    recommendations.to_csv(save_path, index=False)
    print(f"Recommendations saved to {save_path}")
    
    return recommendations