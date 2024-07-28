"""
from etl.extract.netflix_added_movies.combine_web import *
web_scrapper_combined()

from etl.extract.ratings_extraction import *
title_type_change()
ratings_type_change()




from etl.transform.ratings_combine import *
clean_imdb_title_csv()
merge_media_with_ratings()
from etl.transform.golden_globe_trans import *
add_awards_to_media_ratings()
from etl.transform.oscars_combine import *
merge_oscar_awards()
clean_csv_columns()
"""
from analysis.evaluate import *
df = read_csv()
"""genre_splits = genre_split_by_year(df)
save_to_csv(genre_splits)"""

media_counts = media_count_by_year(df)
save_to_csv(media_counts, 'data/output/media_count_by_year.csv')










