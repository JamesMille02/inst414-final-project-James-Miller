import requests
from bs4 import BeautifulSoup
import re
import csv

def get_titles_from_url(url, month_year):
    """Extracts movie titles from the given URL and writes them to a CSV file."""
    # Send a request to the website
    response = requests.get(url)
    
    # Parse the content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all <div> tags
    div_tags = soup.find_all('div')
    titles = set()

    # Regular expression to identify unwanted descriptors
    unwanted_patterns = re.compile(r'-.*|NETFLIX FILM', re.IGNORECASE)
    
    for div in div_tags:
        # Find all <p> and <em> tags within <div> tags
        for tag in div.find_all(['p', 'em']):
            title = tag.get_text(strip=True)
            # Remove trailing characters after '(' and unwanted descriptors
            title = title.split('(')[0].strip()
            title = title.replace('\'', '')  
            title = title.replace('‘', '')  
            title = title.replace('’', '')  
            # Remove unwanted descriptors
            title = unwanted_patterns.sub('', title).strip()
            title = unwanted_patterns.sub(',', title).strip()
            # Remove any remaining quotes or unwanted characters
            title = re.sub(r'^[\'"]+|[\'"]+$', '', title)
            title = re.sub(r'^[“‘]+|[”’]+$', '', title) 
            if  'Avail' not in title and 'Season' not in title and 'Complete Series' not in title and month_year not in title:
                titles.add(title)

    filename = 'data/extracted/media.csv'
    # Write to CSV file
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write media data with the date added
        for media in titles:
            if media: 
                writer.writerow([media, f'{month_year} 2017'])

def jan_2017_add():
    """Extracts movie titles from the January 2016 page."""
    url = 'https://screencrush.com/new-netflix-instant-releases-january-2017/'
    get_titles_from_url(url, 'January')

def feb_2017_add():
    """Extracts movie titles from the February 2016 page."""
    url = 'https://screencrush.com/new-netflix-instant-releases-february-2017/'
    get_titles_from_url(url, 'February')

def mar_2017_add():
    """Extracts movie titles from the March 2016 page."""
    url = 'https://screencrush.com/new-netflix-instant-releases-march-2017/'
    get_titles_from_url(url, 'March')

def apr_2017_add():
    """Extracts movie titles from the April 2016 page."""
    url = 'https://screencrush.com/new-netflix-instant-releases-april-2017/'
    get_titles_from_url(url, 'April')

def may_2017_add():
    """Extracts movie titles from the May 2016 page."""
    url = 'https://screencrush.com/new-netflix-instant-releases-may-2017/'
    get_titles_from_url(url, 'May')

def jun_2017_add():
    """Extracts movie titles from the June 2016 page."""
    url = 'https://screencrush.com/new-netflix-instant-releases-june-2017/'
    get_titles_from_url(url, 'June')

def jul_2017_add():
    """Extracts movie titles from the July 2016 page."""
    url = 'https://screencrush.com/new-netflix-instant-releases-july-2017/'
    get_titles_from_url(url, 'July')

def aug_2017_add():
    """Extracts movie titles from the August 2016 page."""
    url = 'https://screencrush.com/netflix-instant-releases-august-2017/'
    get_titles_from_url(url, 'August')

def oct_2017_add():
    """Extracts movie titles from the October 2016 page."""
    url = 'https://screencrush.com/new-netflix-instant-releases-october-2017/'
    get_titles_from_url(url, 'October')

def nov_2017_add():
    """Extracts movie titles from the November 2016 page."""
    url = 'https://screencrush.com/new-netflix-instant-releases-november-2017/'
    get_titles_from_url(url, 'November')

def dec_2017_add():
    """Extracts movie titles from the December 2016 page."""
    url = 'https://screencrush.com/new-netflix-instant-releases-december-2017/'
    get_titles_from_url(url, 'December')

def get_titles_from_colliderurl(url, month_year):
    """Extracts movie titles from the given URL and writes them to a CSV file."""
    # Send a request to the website
    response = requests.get(url)
    
    # Parse the content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract titles based on <p> tags in this layout
    titles = set()

    # Find all <p> tags
    p_tags = soup.find_all('p')

    # Regular expression to identify unwanted descriptors
    unwanted_patterns = re.compile(r'-.*|NETFLIX FILM', re.IGNORECASE)
    
    for p in p_tags:
        title = p.get_text(strip=True)
        # Clean title and remove unwanted descriptors
        title = title.split('(')[0].strip()
        title = title.replace('\'', '')  
        title = title.replace('‘', '')  
        title = title.replace('’', '')  
        # Remove unwanted descriptors
        title = unwanted_patterns.sub('', title).strip()
        title = unwanted_patterns.sub(',', title).strip()
        # Remove any remaining quotes or unwanted characters
        title = re.sub(r'^[\'"]+|[\'"]+$', '', title)
        title = re.sub(r'^[“‘]+|[”’]+$', '', title) 
        if 'Avail' not in title and 'Season' not in title and 'Complete Series' not in title and month_year not in title:
            titles.add(title)

    filename = 'data/extracted/media.csv'
    # Write to CSV file
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write media data with the date added
        for media in titles:
            if media:  
                writer.writerow([media, f'{month_year} 2017'])

def sept_2017_add():
    """Extracts movie titles from the September 2017 page."""
    url = 'https://collider.com/new-to-netflix-september-2017/'
    get_titles_from_url(url, 'September')



