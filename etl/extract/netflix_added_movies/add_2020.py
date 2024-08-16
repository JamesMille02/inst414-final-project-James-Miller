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

    unwanted_patterns = re.compile(r'(Netflix)', re.IGNORECASE)

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
                writer.writerow([media, f'{month_year} 2020'])

def jan_2020_add():
    """Extracts movie titles from the January page."""
    url = 'https://www.whats-on-netflix.com/coming-soon/whats-coming-to-netflix-in-january-2020-01-24/'
    get_titles_from_url(url, 'January')

def feb_2020_add():
    """Extracts movie titles from the February page."""
    url = 'https://www.whats-on-netflix.com/coming-soon/whats-coming-to-netflix-in-february-2020-02-20/'
    get_titles_from_url(url, 'February')

def mar_2020_add():
    """Extracts movie titles from the March page."""
    url = 'https://www.whats-on-netflix.com/coming-soon/whats-coming-to-netflix-in-march-2020-03-25/'
    get_titles_from_url(url, 'March')

def apr_2020_add():
    """Extracts movie titles from the April page."""
    url = 'https://www.whats-on-netflix.com/coming-soon/whats-coming-to-netflix-in-april-2020-04-23/'
    get_titles_from_url(url, 'April')

def may_2020_add():
    """Extracts movie titles from the May page."""
    url = 'https://www.whats-on-netflix.com/coming-soon/whats-coming-to-netflix-in-may-2020-05-21/'
    get_titles_from_url(url, 'May')

def jun_2020_add():
    """Extracts movie titles from the June 2020 page."""
    url = 'https://www.whats-on-netflix.com/coming-soon/whats-coming-to-netflix-in-june-2020-06-25/'
    get_titles_from_url(url, 'June')

def jul_2020_add():
    """Extracts movie titles from the July 2020 page."""
    url = 'https://www.whats-on-netflix.com/coming-soon/whats-coming-to-netflix-in-july-2020-07-23/'
    get_titles_from_url(url, 'July')

def aug_2020_add():
    """Extracts movie titles from the August page."""
    url = 'https://www.whats-on-netflix.com/coming-soon/whats-coming-to-netflix-in-august-2020-08-21/'
    get_titles_from_url(url, 'August')

def sept_2020_add():
    """Extracts movie titles from the September page."""
    url = 'https://www.whats-on-netflix.com/coming-soon/whats-coming-to-netflix-in-september-2020-09-26/'
    get_titles_from_url(url, 'September')

def oct_2020_add():
    """Extracts movie titles from the October page."""
    url = 'https://www.whats-on-netflix.com/coming-soon/whats-coming-to-netflix-in-october-2020-10-16/'
    get_titles_from_url(url, 'October')

def nov_2020_add():
    """Extracts movie titles from the November page."""
    url = 'https://www.whats-on-netflix.com/coming-soon/whats-coming-to-netflix-in-november-2020-11-17/'
    get_titles_from_url(url, 'November')

def dec_2020_add():
    """Extracts movie titles from the December page."""
    url = 'https://www.whats-on-netflix.com/coming-soon/whats-coming-to-netflix-in-december-2020-12-26/'
    get_titles_from_url(url, 'December')

