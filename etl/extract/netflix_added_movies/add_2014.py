import requests
from bs4 import BeautifulSoup
import re
import csv
import pandas as pd
import os

def jan_2014_add():
    url = 'https://www.vulture.com/2014/01/whats-new-on-netflix-streaming-january-2014.html'
    filename = 'data/extracted/media.csv'

    def get_vulture_movies():
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract movie names from <strong> tags
        strong_tags = soup.find_all('strong')
        strong_movie_names = [tag.get_text() for tag in strong_tags]

        # Extract movie names from <p> tags
        p_tag = soup.find('p', {
            'class': 'clay-paragraph', 
            'data-editable': 'text', 
            'data-uri': 'www.vulture.com/_components/clay-paragraph/instances/ambrose-33d0a96ffc1783812d66cde95e73bfc6-13-0-0@published', 
            'data-word-count': '129'
        })

        movie_names = []
        if p_tag:
            i_tags = p_tag.find_all('i')
            for tag in i_tags:
                movies = tag.decode_contents().split('<br/>')
                for movie in movies:
                    movie_text = BeautifulSoup(movie, 'html.parser').get_text().strip()
                    if movie_text and not re.match(r'^[Aa]', movie_text):
                        movie_names.append(movie_text)

        movie_names = strong_movie_names + movie_names
        return movie_names

    # Extract movie titles
    movies = get_vulture_movies()

    # Create or update CSV with headers and data
    def create_or_update_csv(filename, movies, month_year):
        # Check if the file exists
        file_exists = os.path.isfile(filename)
        
        # Prepare the data for the DataFrame
        data = {'media': movies, 'date added': [month_year] * len(movies)}
        
        # Create a DataFrame
        df = pd.DataFrame(data)

        # If the file doesn't exist, create it with headers
        if not file_exists:
            df.to_csv(filename, index=False, header=True)
        else:
            df.to_csv(filename, mode='a', index=False, header=False)

    # Call the function to create or update the CSV file
    create_or_update_csv(filename, movies, 'January 2014')

# Example usage
jan_2014_add()


def feb_2014_add():
    url = 'https://screencrush.com/new-netflix-instant-releases-february-2014/'

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    strong_tags = soup.find_all('strong')
    titles = set()  

    for strong in strong_tags:
        title = strong.get_text(strip=True)
        title = title.split('(')[0].strip()
        title = title.replace('\'', '')  
        if  'Complete Series' not in title and 'Feb' not in title:
            titles.add(title)  
    
    filename = 'data/extracted/media.csv'
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for media in titles:
            writer.writerow([media, 'February 2014'])

def mar_2014_add():
    url = 'https://screencrush.com/new-netflix-instant-releases-march-2014/'

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    strong_tags = soup.find_all('strong')
    titles = set()  

    for strong in strong_tags:
        title = strong.get_text(strip=True)
        title = title.split('(')[0].strip()
        title = title.replace('\'', '')  
        if 'Complete Series' not in title and 'Mar' not in title:
            titles.add(title)

    filename = 'data/extracted/media.csv'
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for media in titles:
            writer.writerow([media, 'March 2014'])

def april_2014_add():
    url = 'https://screencrush.com/new-on-netflix-in-april-2024/'

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    strong_tags = soup.find_all('strong')
    titles = set() 

    unwanted_patterns = re.compile(r'--.*|NETFLIX FILM', re.IGNORECASE)
    
    for strong in strong_tags:
        title = strong.get_text(strip=True)
        title = title.split('(')[0].strip()
        title = title.replace('\'', '')
        title = unwanted_patterns.sub('', title).strip()
        if 'Complete Series' not in title and 'Avail' not in title:
            titles.add(title)

    filename = 'data/extracted/media.csv'
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for media in titles:
            writer.writerow([media, 'April 2014'])

def may_2014_add():
    url = 'https://screencrush.com/new-netflix-instant-releases-may-2014/'

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    strong_tags = soup.find_all('strong')
    titles = set()  

    unwanted_patterns = re.compile(r'--.*|NETFLIX FILM', re.IGNORECASE)
    
    for strong in strong_tags:
        title = strong.get_text(strip=True)
        title = title.split('(')[0].strip()
        title = title.replace('\'', '')
        title = unwanted_patterns.sub('', title).strip()
        if 'Complete Series' not in title and 'May' not in title:
            titles.add(title)

    filename = 'data/extracted/media.csv'
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for media in titles:
            writer.writerow([media, 'May 2014'])

def june_2014_add():
    url = 'https://screencrush.com/new-netflix-instant-releases-june-2014/'

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    strong_tags = soup.find_all('strong')
    titles = set()  

    unwanted_patterns = re.compile(r'--.*|NETFLIX FILM', re.IGNORECASE)
    
    for strong in strong_tags:
        title = strong.get_text(strip=True)
        title = title.split('(')[0].strip()
        title = title.replace('\'', '')
        title = unwanted_patterns.sub('', title).strip()
        if 'Complete Series' not in title and 'June' not in title:
            titles.add(title)
    
    filename = 'data/extracted/media.csv'
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for media in titles:
            writer.writerow([media, 'June 2014'])

def july_2014_add():
    url = 'https://screencrush.com/new-netflix-instant-releases-july-2014/'

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    strong_tags = soup.find_all('strong')
    titles = set()  

    unwanted_patterns = re.compile(r'--.*|NETFLIX FILM', re.IGNORECASE)
    
    for strong in strong_tags:
        title = strong.get_text(strip=True)
        title = title.split('(')[0].strip()
        title = title.replace('\'', '')
        title = unwanted_patterns.sub('', title).strip()
        if ':' not in title and title and 'Complete Series' not in title and 'July' not in title:
            titles.add(title)

    filename = 'data/extracted/media.csv'
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for media in titles:
            writer.writerow([media, 'July 2014'])

def aug_2014_add():
    url = 'https://screencrush.com/new-netflix-instant-releases-august-2014/'

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    strong_tags = soup.find_all('strong')
    titles = set()  

    for strong in strong_tags:
        title = strong.get_text(strip=True)
        title = title.split('(')[0].strip()
        title = title.replace('\'', '')
        if 'Season' not in title and 'Complete Series' not in title and title and 'August' not in title:
            titles.add(title)

    filename = 'data/extracted/media.csv'
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for media in titles:
            writer.writerow([media, 'August 2014'])

def sept_2014_add():
    url = 'https://screencrush.com/new-netflix-instant-releases-september-2014/'

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    strong_tags = soup.find_all('strong')
    titles = set()  

    for strong in strong_tags:
        title = strong.get_text(strip=True)
        title = title.split('(')[0].strip()
        title = title.replace('\'', '')
        if 'Season' not in title and 'Complete Series' not in title and title and 'Sept' not in title:
            titles.add(title)

    filename = 'data/extracted/media.csv'
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for media in titles:
            writer.writerow([media, 'September 2014'])

def oct_2014_add():
    url = 'https://screencrush.com/new-netflix-instant-releases-october-2014/'

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    strong_tags = soup.find_all('strong')
    titles = set()  

    for strong in strong_tags:
        title = strong.get_text(strip=True)
        title = title.split('(')[0].strip()
        title = title.replace('\'', '')
        if  'Season' not in title and 'Complete Series' not in title and title and 'October' not in title:
            titles.add(title)

    filename = 'data/extracted/media.csv'
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for media in titles:
            writer.writerow([media, 'October 2014'])

def nov_2014_add():
    url = 'https://screencrush.com/new-netflix-instant-releases-november-2014/'

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    strong_tags = soup.find_all('strong')
    titles = set()  

    unwanted_patterns = re.compile(r'--.*|NETFLIX FILM', re.IGNORECASE)
    
    for strong in strong_tags:
        title = strong.get_text(strip=True)
        title = title.split('(')[0].strip()
        title = title.replace('\'', '')
        title = unwanted_patterns.sub('', title).strip()
        if 'Complete Series' not in title and 'Nov' not in title:
            titles.add(title)

    filename = 'data/extracted/media.csv'
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for media in titles:
            writer.writerow([media, 'November 2014'])

def dec_2014_add():
    url = 'https://screencrush.com/new-netflix-instant-releases-december-2014/'

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    strong_tags = soup.find_all('strong')
    titles = set()  

    for strong in strong_tags:
        title = strong.get_text(strip=True)
        title = title.split('(')[0].strip()
        title = title.replace('\'', '')
        if 'Season' not in title and 'Complete Series' not in title and title and 'Dec' not in title:
            titles.add(title)

    filename = 'data/extracted/media.csv'
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for media in titles:
            writer.writerow([media, 'December 2014'])


