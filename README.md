<<<<<<< HEAD
<<<<<<< HEAD
# inst414-final-project-James-Miller
Project Overview
    Business Problem: The media that is added to Netflix can increase or decrease subscribers. With the cost of liscensing a movie being so high, determining the best media to is important for any streaming platform. The goal for this project is to answer the question of what is the best media to add and it will do this by determining the media to add based on past data and growth.
    
    Data Sets Used:
    
        Web scrapping of websites that report on media added to Netflix each month. 
              Example: https://www.whats-on-netflix.com/coming-soon/whats-coming-to-netflix-in-august-2023-08-20/
              
        https://www.kaggle.com/datasets/unanimad/golden-globe-awards
        
        https://www.kaggle.com/datasets/unanimad/the-oscar-award
        
        https://datasets.imdbws.com/
        
            Used https://datasets.imdbws.com/title.ratings.tsv.gz and https://datasets.imdbws.com/title.basics.tsv.gz
            
    Techniques used:
    
        Web scarping, combining CSVs, joining tables, removing rows and columns, adding information in blank columns through other datasets.
        
    Expected Outputs:
    
        CSV files for title and date added, title, date_added and ratings, titles, ratings, date_added and golden globes, titles, ratings, date_added, oscars, and golden globes. Also, category genre splits for a year and all years combined, subscriber loss and gain per a year, media added each year.
        
Setup instructions:

    Clone the repository: click green code button, go to vscode, click github button on the side bar and paste the link into the top bar.
    
    Activate Venv: activate venv by typing .venv/Scripts/activate in the terminal.

    Kaggle API:
    
        https://www.kaggle.com/docs/api
    
    Install dependencies:
    
        pip install -r requirements.txt
        
Running the Project:
    To run code go to main file and run, the data sets in the /data files need to be deleted before running or it will add on the bottom of documents and change the expected csv files. If you need to run certain functions, surrond the chunks over unused functions in triple quotes, """functions""".

Structure:
├── data/

│   ├── extracted/

│   ├── processed/

│   ├── outputs/

│   ├── reference-tables/

├── etl/

│   ├── extract

│   │   ├── netflix_added

│   │   │  ├── added_2014.py

│   │   │  ├── added_2015.py

│   │   │  ├── added_2016.py

│   │   │  ├── added_2017.py

│   │   │  ├── added_2018.py

│   │   │  ├── added_2019.py

│   │   │  ├── added_2020.py

│   │   │  ├── added_2021.py

│   │   │  ├── added_2022.py

│   │   │  ├── added_2023.py

│   │   │  ├── added_2024.py

│   │   │  ├── combine.py

│   │   ├── ratings_extraction.py

│   ├── transform

│   │   ├── golden_globe_trans.py

│   │   ├── oscars_combine.py

│   │   ├── ratings_combine.py

│   │   ├── genre_combine.py

│   ├── load.py

├── analysis/

│   ├── model.py

│   ├── evaluate.py

├── vis/

│   ├── visualizations.py

├── main.py

├── README.md

├── requirements.txt
    
        

            
=======

>>>>>>> main
=======
# inst414-final-project-James-Miller
>>>>>>> main
