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

    # Find all <ul> tags
    ul_tags = soup.find_all('ul')
    titles = set()

    unwanted_patterns = re.compile(r'(Netflix Film|NETFLIX FILM)', re.IGNORECASE)

    for ul in ul_tags:
        # Find all <li> tags within <ul> tags
        for li in ul.find_all('li'):
            title = li.get_text(strip=True)
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
            # Only add non-empty titles
            if 'Avail' not in title and 'Season' not in title and 'Complete Series' not in title and month_year not in title:
                titles.add(title)

    filename = 'data/extracted/media.csv'
    # Write to CSV file
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write media data with the date added
        for media in titles:
            if media:  
                writer.writerow([media, f'{month_year} 2024'])

def jan_2024_add():
    """Extracts movie titles from the January 2024 page."""
    url = 'https://www.whats-on-netflix.com/coming-soon/whats-coming-to-netflix-in-january-2024-01-11/'
    get_titles_from_url(url, 'January')

def feb_2024_add():
    """Extracts movie titles from the February 2024 page."""
    url = 'https://www.whats-on-netflix.com/coming-soon/whats-coming-to-netflix-in-february-2024/'
    get_titles_from_url(url, 'February')

def mar_2024_add():
    """Extracts movie titles from the March 2024 page."""
    url = 'https://www.whats-on-netflix.com/coming-soon/whats-coming-to-netflix-in-march-2024/'
    get_titles_from_url(url, 'March')

def apr_2024_add():
    """Extracts movie titles from the April 2024 page."""
    url = 'https://www.whats-on-netflix.com/coming-soon/whats-coming-to-netflix-in-april-2024/'
    get_titles_from_url(url, 'April')

def may_2024_add():
    """Extracts movie titles from the May 2024 page."""
    url = 'https://www.whats-on-netflix.com/coming-soon/whats-coming-to-netflix-in-may-2024/'
    get_titles_from_url(url, 'May')

def jun_2024_add():
    """Extracts movie titles from the June 2024 page."""
    url = 'https://www.whats-on-netflix.com/coming-soon/whats-coming-to-netflix-in-june-2024/'
    get_titles_from_url(url, 'June')

def jul_2024_add():
    """Extracts movie titles from the July 2024 page."""
    url = 'https://www.whats-on-netflix.com/coming-soon/whats-coming-to-netflix-in-july-2024/'
    get_titles_from_url(url, 'July')