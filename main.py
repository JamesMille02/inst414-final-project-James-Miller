import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,  # Adjust the level as needed (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),  # Log to console
        logging.FileHandler('etl_and_analysis.log')  # Log to file
    ]
)

# Create a logger
logger = logging.getLogger(__name__)

from etl.extract.downloadCSVs import *

logger.info('Starting to download datasets...')
download_imdb_datasets()
logger.info('IMDB datasets downloaded.')

download_kaggle_datasets()
logger.info('Kaggle datasets downloaded.')

from etl.extract.netflix_added_movies.combine_web import *
logger.info('Starting web scraping for combined Netflix movies...')
web_scrapper_combined()
logger.info('Web scraping completed.')

from etl.extract.ratings_extraction import *
logger.info('Starting ratings extraction...')
title_type_change()
ratings_type_change()
language_type_change()
logger.info('Ratings extraction completed.')

from etl.transform.ratings_combine import *
logger.info('Starting ratings transformation...')
clean_imdb_title_csv()
merge_media_with_ratings()
logger.info('Ratings transformation completed.')

from etl.transform.all_movies import *
logger.info('Starting all movies transformation...')
combine_and_filter_csv()
logger.info('All movies transformation completed.')

from etl.transform.golden_globe_trans import *
logger.info('Starting to add Golden Globe awards...')
add_awards_to_media_ratings()
logger.info('Golden Globe awards added.')

from etl.transform.oscars_combine import *
logger.info('Starting to merge IMDb Oscar awards...')
merge_imdb_oscar_awards()
clean_imdb_csv_columns()
merge_oscar_awards()
clean_csv_columns()
logger.info('Oscar awards merged.')

from etl.transform.genre_match import *
logger.info('Starting genre mapping...')
genre_mapping = process_genres(
    imdb_path='data/output/final_imdb_dataset',
    netflix_path='data/output/final_netflix_dataset.csv',
    updated_imdb_path='data/output/final_imdb_data.csv',
    updated_netflix_path='data/output/final_netflix_data.csv'
)
logger.info(f'Genre mapping completed: {genre_mapping}')

from etl.load import *
logger.info('Loading datasets...')
imdb_df, netflix_df = load_datasets()
logger.info('Datasets loaded.')

from analysis.descriptive_analysis import *

logger.info('Performing descriptive analysis...')
# Perform analysis on Netflix dataset
genre_splits = genre_split_by_year(netflix_df)
plot_genre_split_pie_chart(genre_splits)
readded_by_year, average_readded = count_added_movies_by_year('data/extracted/media.csv')
plot_added_movies_by_year(readded_by_year, average_readded)
logger.info('Descriptive analysis completed.')

from analysis.model import  *

logger.info('Preprocessing data for model...')
imdb_df, netflix_df, genre_to_id = preprocess_data(imdb_df, netflix_df)
avg_characteristics = calculate_average_characteristics(netflix_df)
recommendations_df = predict_movies_to_license(imdb_df, avg_characteristics)
logger.info('Model predictions completed.')

from analysis.evaluate import *
logger.info('Evaluating model recommendations...')
evaluate_characteristics(recommendations_df, netflix_df)
logger.info('Model evaluation completed.')
