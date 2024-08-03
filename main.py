
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

from etl.load import *
imdb_df, netflix_df = load_datasets()

from analysis.descriptive_analysis import *
df = read_csv('data/output/final_netflix_dataset.csv')
genre_splits = genre_split_by_year(df)

media_counts = media_count_by_year(df)



