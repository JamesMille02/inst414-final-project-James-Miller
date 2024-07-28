from etl.extract.netflix_added_movies.add_2014 import *
from etl.extract.netflix_added_movies.add_2015 import *
from etl.extract.netflix_added_movies.add_2016 import *
from etl.extract.netflix_added_movies.add_2017 import *
from etl.extract.netflix_added_movies.add_2018 import *
from etl.extract.netflix_added_movies.add_2019 import *
from etl.extract.netflix_added_movies.add_2020 import *
from etl.extract.netflix_added_movies.add_2021 import *
from etl.extract.netflix_added_movies.add_2022 import *
from etl.extract.netflix_added_movies.add_2023 import *
from etl.extract.netflix_added_movies.add_2024 import *
import os
import csv

def web_scrapper_combined():
    def add_headers_if_not_exists(filename):
        """Adds column headers to the CSV file if it does not already exist."""
        if not os.path.exists(filename):
            with open(filename, 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=['media', 'date_added'])
                writer.writeheader()

    filename = 'data/extracted/media.csv'

    add_headers_if_not_exists(filename)

    jan_2014_add()
    feb_2014_add()
    mar_2014_add()
    april_2014_add()
    may_2014_add()
    june_2014_add()
    july_2014_add()
    aug_2014_add()
    sept_2014_add()
    oct_2014_add()
    nov_2014_add()
    dec_2014_add()

    jan_2015_add()
    feb_2015_add()
    mar_2015_add()
    april_2015_add()
    may_2015_add()
    june_2015_add()
    july_2015_add()
    aug_2015_add()
    sep_2015_add()
    oct_2015_add()
    nov_2015_add()
    dec_2015_add()

    jan_2016_add()
    feb_2016_add()
    mar_2016_add()
    apr_2016_add()
    may_2016_add()
    jun_2016_add()
    jul_2016_add()
    aug_2016_add()
    sep_2016_add()
    oct_2016_add()
    nov_2016_add()
    dec_2016_add()

    jan_2017_add()
    feb_2017_add()
    mar_2017_add()
    apr_2017_add()
    may_2017_add()
    jun_2017_add()
    jul_2017_add()
    aug_2017_add()
    sept_2017_add()
    oct_2017_add()
    nov_2017_add()
    dec_2017_add()

    jan_2018_add()
    feb_2018_add()
    mar_2018_add()
    apr_2018_add()
    may_2018_add()
    jun_2018_add()
    jul_2018_add()
    aug_2018_add()
    sept_2018_add()
    oct_2018_add()
    nov_2018_add()
    dec_2018_add()

    jan_2019_add()
    feb_2019_add()
    mar_2019_add()
    apr_2019_add()
    may_2019_add()
    jun_2019_add()
    jul_2019_add()
    aug_2019_add()
    sept_2019_add()
    oct_2019_add()
    nov_2019_add()
    dec_2019_add()

    jan_2020_add()
    feb_2020_add()
    mar_2020_add()
    apr_2020_add()
    may_2020_add()
    jun_2020_add()
    jul_2020_add()
    aug_2020_add()
    sept_2020_add()
    oct_2020_add()
    nov_2020_add()
    dec_2020_add()

    jan_2021_add()
    feb_2021_add()
    mar_2021_add()
    apr_2021_add()
    may_2021_add()
    jun_2021_add()
    jul_2021_add()
    aug_2021_add()
    sept_2021_add()
    oct_2021_add()
    nov_2021_add()
    dec_2021_add()

    jan_2022_add()
    feb_2022_add()
    mar_2022_add()
    apr_2022_add()
    may_2022_add()
    jun_2022_add()
    jul_2022_add()
    aug_2022_add()
    sept_2022_add()
    oct_2022_add()
    nov_2022_add()
    dec_2022_add()

    jan_2023_add()
    feb_2023_add()
    mar_2023_add()
    apr_2023_add()
    may_2023_add()
    jun_2023_add()
    jul_2023_add()
    aug_2023_add()
    sept_2023_add()
    oct_2023_add()
    nov_2023_add()
    dec_2023_add()

    jan_2024_add()
    feb_2024_add()
    mar_2024_add()
    apr_2024_add()
    may_2024_add()
    jun_2024_add()
    jul_2024_add()
