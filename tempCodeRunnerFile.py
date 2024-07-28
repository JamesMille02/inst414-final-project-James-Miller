"""
from etl.extract.netflix_added_movies.combine_web import *
web_scrapper_combined()

from etl.extract.ratings_extraction import *
title_type_change()
ratings_type_change()
"""


from etl.transform.ratings_combine import *
merge_media_with_ratings()

from etl.transform.golden_globe_trans import *
add_awards_to_media_ratings()
from etl.transform.oscars_combine import *
merge_oscar_awards()
clean_csv_columns()












