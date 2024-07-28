import requests
from bs4 import BeautifulSoup
import re
import csv

def jan_2016_add():
    """Adds the movies that were added for March 2015."""
    url = 'https://screencrush.com/new-netflix-instant-releases-january-2016/'  
    
    # Send a request to the website
    response = requests.get(url)

    # Parse the content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all <div> tags
    div_tags = soup.find_all('div')
    titles = set()

    # Regular expression to identify unwanted descriptors
    unwanted_patterns = re.compile(r'--.*|NETFLIX FILM', re.IGNORECASE)
    
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
            title = re.sub(r'^[\'"]+|[\'"]+$', '', title)
            title = re.sub(r'^[“‘]+|[”’]+$', '', title) 
            if 'Avail' not in title and 'Season' not in title and 'Complete Series' not in title and 'Jan' not in title:
                titles.add(title)

    filename = 'data/extracted/media.csv'
    # Write to CSV file
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write media data with the date added
        for media in titles:
            writer.writerow([media, 'January 2016'])

def feb_2016_add():
    """Adds the movies that were added for March 2015."""
    url = 'https://screencrush.com/new-netflix-instant-releases-january-2016/'  
    
    # Send a request to the website
    response = requests.get(url)

    # Parse the content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all <div> tags
    div_tags = soup.find_all('div')
    titles = set()

    # Regular expression to identify unwanted descriptors
    unwanted_patterns = re.compile(r'--.*|NETFLIX FILM', re.IGNORECASE)
    
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
            title = re.sub(r'^[\'"]+|[\'"]+$', '', title)
            title = re.sub(r'^[“‘]+|[”’]+$', '', title) 
            if 'Avail' not in title and 'Season' not in title and 'Complete Series' not in title and 'Feb' not in title:
                titles.add(title)

    filename = 'data/extracted/media.csv'
    # Write to CSV file
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write media data with the date added
        for media in titles:
            writer.writerow([media, 'February 2016'])

def mar_2016_add():
    """Adds the movies that were added for March 2015."""
    url = 'https://screencrush.com/new-netflix-instant-releases-january-2016/'  
    
    # Send a request to the website
    response = requests.get(url)

    # Parse the content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all <div> tags
    div_tags = soup.find_all('div')
    titles = set()

    # Regular expression to identify unwanted descriptors
    unwanted_patterns = re.compile(r'--.*|NETFLIX FILM', re.IGNORECASE)
    
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
            title = re.sub(r'^[\'"]+|[\'"]+$', '', title)
            title = re.sub(r'^[“‘]+|[”’]+$', '', title) 
            if 'Avail' not in title and 'Season' not in title and 'Complete Series' not in title and 'March' not in title:
                titles.add(title)

    filename = 'data/extracted/media.csv'
    # Write to CSV file
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write media data with the date added
        for media in titles:
            writer.writerow([media, 'March 2016'])

def apr_2016_add():
    """Adds the movies that were added for April 2016."""
    url = 'https://screencrush.com/new-netflix-instant-releases-april-2016/'  
    
    # Send a request to the website
    response = requests.get(url)

    # Parse the content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all <div> tags
    div_tags = soup.find_all('div')
    titles = set()

    # Regular expression to identify unwanted descriptors
    unwanted_patterns = re.compile(r'--.*|NETFLIX FILM', re.IGNORECASE)
    
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
            if 'Avail' not in title and 'Season' not in title and 'Complete Series' not in title and 'April' not in title:
                titles.add(title)

    filename = 'data/extracted/media.csv'
    # Write to CSV file
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write media data with the date added
        for media in titles:
            writer.writerow([media, 'April 2016'])

def may_2016_add():
    """Adds the movies that were added for May 2016."""
    url = 'https://screencrush.com/new-netflix-instant-releases-may-2016/'  
    
    # Send a request to the website
    response = requests.get(url)

    # Parse the content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all <div> tags
    div_tags = soup.find_all('div')
    titles = set()

    # Regular expression to identify unwanted descriptors
    unwanted_patterns = re.compile(r'--.*|NETFLIX FILM', re.IGNORECASE)
    
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
            if 'Avail' not in title and 'Season' not in title and 'Complete Series' not in title and 'May' not in title:
                titles.add(title)

    filename = 'data/extracted/media.csv'
    # Write to CSV file
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write media data with the date added
        for media in titles:
            writer.writerow([media, 'May 2016'])

def jun_2016_add():
    """Adds the movies that were added for June 2016."""
    url = 'https://screencrush.com/new-netflix-instant-releases-june-2016/'  
    
    # Send a request to the website
    response = requests.get(url)

    # Parse the content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all <div> tags
    div_tags = soup.find_all('div')
    titles = set()

    # Regular expression to identify unwanted descriptors
    unwanted_patterns = re.compile(r'--.*|NETFLIX FILM', re.IGNORECASE)
    
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
            if 'Avail' not in title and 'Season' not in title and 'Complete Series' not in title and 'June' not in title:
                titles.add(title)

    filename = 'data/extracted/media.csv'
    # Write to CSV file
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write media data with the date added
        for media in titles:
            writer.writerow([media, 'June 2016'])

def jul_2016_add():
    """Adds the movies that were added for July 2016."""
    url = 'https://screencrush.com/new-on-netflix-july-2016/'  
    
    # Send a request to the website
    response = requests.get(url)

    # Parse the content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all <div> tags
    div_tags = soup.find_all('div')
    titles = set()

    # Regular expression to identify unwanted descriptors
    unwanted_patterns = re.compile(r'--.*|NETFLIX FILM', re.IGNORECASE)
    
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
            if 'Avail' not in title and 'Season' not in title and 'Complete Series' not in title and 'July' not in title:
                titles.add(title)

    filename = 'data/extracted/media.csv'
    # Write to CSV file
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write media data with the date added
        for media in titles:
            writer.writerow([media, 'July 2016'])

def aug_2016_add():
    """Adds the movies that were added for August 2016."""
    url = 'https://screencrush.com/new-netflix-instant-releases-august-2016/'  
    
    # Send a request to the website
    response = requests.get(url)

    # Parse the content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all <div> tags
    div_tags = soup.find_all('div')
    titles = set()

    # Regular expression to identify unwanted descriptors
    unwanted_patterns = re.compile(r'--.*|NETFLIX FILM', re.IGNORECASE)
    
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
            if 'Avail' not in title and 'Season' not in title and 'Complete Series' not in title and 'August' not in title:
                titles.add(title)

    filename = 'data/extracted/media.csv'
    # Write to CSV file
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write media data with the date added
        for media in titles:
            writer.writerow([media, 'August 2016'])

def sep_2016_add():
    """Adds the movies that were added for September 2016."""
    url = 'https://screencrush.com/new-netflix-instant-releases-september-2016/'  
    
    # Send a request to the website
    response = requests.get(url)

    # Parse the content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all <div> tags
    div_tags = soup.find_all('div')
    titles = set()

    # Regular expression to identify unwanted descriptors
    unwanted_patterns = re.compile(r'--.*|NETFLIX FILM', re.IGNORECASE)
    
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
            if 'Avail' not in title and 'Season' not in title and 'Complete Series' not in title and 'September' not in title:
                titles.add(title)

    filename = 'data/extracted/media.csv'
    # Write to CSV file
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write media data with the date added
        for media in titles:
            writer.writerow([media, 'September 2016'])

def oct_2016_add():
    """Adds the movies that were added for October 2016."""
    url = 'https://screencrush.com/new-netflix-instant-releases-october-2016/'  
    
    # Send a request to the website
    response = requests.get(url)

    # Parse the content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all <div> tags
    div_tags = soup.find_all('div')
    titles = set()

    # Regular expression to identify unwanted descriptors
    unwanted_patterns = re.compile(r'--.*|NETFLIX FILM', re.IGNORECASE)
    
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
            if  'Avail' not in title and 'Season' not in title and 'Complete Series' not in title and 'October' not in title:
                titles.add(title)

    filename = 'data/extracted/media.csv'
    # Write to CSV file
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write media data with the date added
        for media in titles:
            writer.writerow([media, 'October 2016'])

def nov_2016_add():
    """Adds the movies that were added for November 2016."""
    url = 'https://screencrush.com/new-on-netflix-november-2016/'  
    
    # Send a request to the website
    response = requests.get(url)

    # Parse the content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all <div> tags
    div_tags = soup.find_all('div')
    titles = set()

    # Regular expression to identify unwanted descriptors
    unwanted_patterns = re.compile(r'--.*|NETFLIX FILM', re.IGNORECASE)
    
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
            if 'Avail' not in title and 'Season' not in title and 'Complete Series' not in title and 'November' not in title:
                titles.add(title)

    filename = 'data/extracted/media.csv'
    # Write to CSV file
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write media data with the date added
        for media in titles:
            writer.writerow([media, 'November 2016'])

def dec_2016_add():
    """Adds the movies that were added for December 2016."""
    url = 'https://screencrush.com/new-netflix-instant-releases-december-2016/'  
    
    # Send a request to the website
    response = requests.get(url)

    # Parse the content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all <div> tags
    div_tags = soup.find_all('div')
    titles = set()

    # Regular expression to identify unwanted descriptors
    unwanted_patterns = re.compile(r'--.*|NETFLIX FILM', re.IGNORECASE)
    
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
            if 'Avail' not in title and 'Season' not in title and 'Complete Series' not in title and 'December' not in title:
                titles.add(title)

    filename = 'data/extracted/media.csv'
    # Write to CSV file
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write media data with the date added
        for media in titles:
            writer.writerow([media, 'December 2016'])
