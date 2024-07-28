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
                writer.writerow([media, f'{month_year} 2019'])

def jan_2019_add():
    """Extracts movie titles from the January 2018 page."""
    url = 'https://www.whats-on-netflix.com/coming-soon/january-2019-new-netflix-releases/'
    get_titles_from_url(url, 'January')

def feb_2019_add():
    """Extracts movie titles from the February 2018 page."""
    url = 'https://www.whats-on-netflix.com/coming-soon/february-2019-new-netflix-releases/'
    get_titles_from_url(url, 'February')

def mar_2019_add():
    """Extracts movie titles from the March 2018 page."""
    url = 'https://www.whats-on-netflix.com/coming-soon/march-2019-new-netflix-releases/'
    get_titles_from_url(url, 'March')

def apr_2019_add():
    """Extracts movie titles from the April 2018 page."""
    url = 'https://www.whats-on-netflix.com/coming-soon/april-2019-new-netflix-releases/'
    get_titles_from_url(url, 'April')

def may_2019_add():
    """Extracts movie titles from the May 2018 page."""
    url = 'https://www.whats-on-netflix.com/coming-soon/may-2019-new-netflix-releases/'
    get_titles_from_url(url, 'May')

def jun_2019_add():
    """Extracts movie titles from the June 2018 page."""
    url = 'https://www.whats-on-netflix.com/coming-soon/june-2019-new-netflix-releases/'
    get_titles_from_url(url, 'June')

def jul_2019_add():
    """Extracts movie titles from the July 2018 page."""
    url = 'https://www.whats-on-netflix.com/coming-soon/july-2019-new-netflix-releases/'
    get_titles_from_url(url, 'July')

def aug_2019_add():
    """Extracts movie titles from the August 2018 page."""
    url = 'https://www.whats-on-netflix.com/coming-soon/whats-coming-to-netflix-in-august-2019-08-24/'
    get_titles_from_url(url, 'August')

def sept_2019_add():
    """Extracts movie titles from the September 2018 page."""
    url = 'https://www.whats-on-netflix.com/coming-soon/whats-coming-to-netflix-in-september-2019-25-09/'
    get_titles_from_url(url, 'September')

def oct_2019_add():
    """Extracts movie titles from the October 2018 page."""
    url = 'https://www.whats-on-netflix.com/coming-soon/whats-coming-to-netflix-in-october-2019-11-22/'
    get_titles_from_url(url, 'October')

def nov_2019_add():
    """Extracts movie titles from the November 2018 page."""
    url = 'https://www.whats-on-netflix.com/coming-soon/whats-coming-to-netflix-in-november-2019-11-22/'
    get_titles_from_url(url, 'November')

def dec_2019_add():
    """Extracts movie titles from the December 2018 page."""
    url = 'https://www.whats-on-netflix.com/coming-soon/whats-coming-to-netflix-in-december-2019-12-22/'
    get_titles_from_url(url, 'December')

