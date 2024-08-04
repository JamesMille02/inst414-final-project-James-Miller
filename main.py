"""
from etl.extract.downloadCSVs import *

download_imdb_datasets()

download_kaggle_datasets()

from etl.extract.netflix_added_movies.combine_web import *
web_scrapper_combined()

from etl.extract.ratings_extraction import *
title_type_change()
ratings_type_change()
language_type_change()


from etl.transform.ratings_combine import *
clean_imdb_title_csv()
merge_media_with_ratings()

from  etl.transform.all_movies  import *
combine_and_filter_csv()

from etl.transform.golden_globe_trans import *
add_awards_to_media_ratings()

from etl.transform.oscars_combine import *
merge_imdb_oscar_awards()
clean_imdb_csv_columns()
merge_oscar_awards()
clean_csv_columns()

from etl.transform.genre_match import *
genre_mapping = process_genres(
    imdb_path='data/output/final_imdb_dataset',
    netflix_path='data/output/final_netflix_dataset.csv',
    updated_imdb_path='data/output/final_imdb_data.csv',
    updated_netflix_path='data/output/final_netflix_data.csv'
)

print("Genre mapping:", genre_mapping)
"""
from etl.load import *
imdb_df, netflix_df = load_datasets()
"""
from analysis.descriptive_analysis import *

# Perform analysis on Netflix dataset
genre_splits = genre_split_by_year(netflix_df)
plot_genre_split_pie_chart(genre_splits)
readded_by_year, average_readded = count_added_movies_by_year('data/extracted/media.csv')
plot_added_movies_by_year(readded_by_year, average_readded)
"""
from analysis.model import  *

imdb_df, netflix_df, genre_to_id = preprocess_data(imdb_df, netflix_df)
avg_characteristics = calculate_average_characteristics(netflix_df)
recommendations_df = predict_movies_to_license(imdb_df, avg_characteristics)

from analysis.evaluate import *
evaluate_characteristics(recommendations_df, netflix_df)
