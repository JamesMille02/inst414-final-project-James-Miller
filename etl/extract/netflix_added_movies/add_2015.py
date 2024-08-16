import requests
from bs4 import BeautifulSoup
import re
import csv

def jan_2015_add():
    """Adds the movies that were added for January 2015."""
    url = 'https://screencrush.com/netflix-instant-january-2015/'
    
    # Send a request to the website
    response = requests.get(url)

    # Parse the content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all <strong> tags within <div> tags
    strong_tags = soup.find_all('strong')
    titles = set()

    # Avoid duplicates
    for strong in strong_tags:
        title = strong.get_text(strip=True)
        # Remove trailing white spaces, characters after (, and any single quotes
        title = title.split('(')[0].strip()
        title = title.replace('\'', '')  
        title = title.replace('‘', '')  
        title = title.replace('’', '') 
        # Remove entries containing ':'
        if 'Avail' not in title and 'Season' not in title and 'Complete Series' not in title and title and 'Jan' not in title:
            titles.add(title)  
    
    filename = 'data/extracted/media.csv'
    # Write to CSV file
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write media data with the date added
        for media in titles:
            writer.writerow([media, 'January 2015'])

def feb_2015_add():
    """Adds the movies that were added for February 2015."""
    url = 'https://screencrush.com/new-netflix-instant-releases-february-2015/'
    
    # Send a request to the website
    response = requests.get(url)

    # Parse the content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all <strong> tags within <div> tags
    strong_tags = soup.find_all('strong')
    titles = set()

    # Regular expression to identify unwanted descriptors
    unwanted_patterns = re.compile(r'--.*|NETFLIX FILM', re.IGNORECASE)
    
    for strong in strong_tags:
        title = strong.get_text(strip=True)
        # Remove trailing characters after '(' and unwanted descriptors
        title = title.split('(')[0].strip()
        title = title.replace('\'', '')  
        title = title.replace('‘', '')  
        title = title.replace('’', '') 
        # Remove unwanted descriptors
        title = unwanted_patterns.sub('', title).strip()
        title = re.sub(r'^[\'"]+|[\'"]+$', '', title)
        title = re.sub(r'^[“‘]+|[”’]+$', '', title) 
        if 'Avail' not in title and 'Season' not in title and 'Complete Series' not in title and title and 'Feb' not in title:
            if title:  
                titles.add(title)
        
    filename = 'data/extracted/media.csv'
    # Write to CSV file
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write media data with the date added
        for media in titles:
            writer.writerow([media, 'February 2015'])

def mar_2015_add():
    """Adds the movies that were added for March 2015."""
    url = 'https://screencrush.com/new-netflix-instant-march-2015/'  
    
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
            if'Avail' not in title and 'Season' not in title and 'Complete Series' not in title and 'Mar' not in title:
                titles.add(title)

    filename = 'data/extracted/media.csv'
    # Write to CSV file
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write media data with the date added
        for media in titles:
            writer.writerow([media, 'March 2015'])

def april_2015_add():
    """Adds the movies that were added for April 2015."""
    url = 'https://screencrush.com/new-netflix-instant-releases-april-2015/'  
    
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
            if 'director' not in title and 'Avail' not in title and 'Season' not in title and 'Complete Series' not in title and 'April' not in title:
                titles.add(title)

    filename = 'data/extracted/media.csv'
    # Write to CSV file
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write media data with the date added
        for media in titles:
            writer.writerow([media, 'April 2015'])

def may_2015_add():
    """Adds the movies that were added for May 2015."""
    url = 'https://screencrush.com/new-netflix-instant-releases-may-2015/'  
    
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
            writer.writerow([media, 'May 2015'])

def june_2015_add():
    """Adds the movies that were added for June 2015."""
    url = 'https://screencrush.com/new-netflix-instant-releases-june-2015/'  
    
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
            writer.writerow([media, 'June 2015'])

def july_2015_add():
    """Adds the movies that were added for July 2015."""
    url = 'https://screencrush.com/new-netflix-instant-releases-july-2015/'  
    
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
            writer.writerow([media, 'July 2015'])

def aug_2015_add():
    """Adds the movies that were added for August 2015."""
    url = 'https://screencrush.com/new-netflix-instant-releases-august-2015/'  
    
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
            writer.writerow([media, 'August 2015'])

def sep_2015_add():
    """Adds the movies that were added for September 2015."""
    url = 'https://screencrush.com/new-netflix-instant-releases-september-2015/'  
    
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
            writer.writerow([media, 'September 2015'])

def oct_2015_add():
    """Adds the movies that were added for October 2015."""
    url = 'https://screencrush.com/new-netflix-instant-releases-october-2015/'  
    
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
            if 'Avail' not in title and 'Season' not in title and 'Complete Series' not in title and 'October' not in title:
                titles.add(title)

    filename = 'data/extracted/media.csv'
    # Write to CSV file
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write media data with the date added
        for media in titles:
            writer.writerow([media, 'October 2015'])

def nov_2015_add():
    """Adds the movies that were added for November 2015."""
    url = 'https://screencrush.com/new-netflix-instant-releases-november-2015/'  
    
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
            writer.writerow([media, 'November 2015'])

def dec_2015_add():
    """Adds the movies that were added for December 2015."""
    url = 'https://screencrush.com/new-netflix-instant-releases-december-2015/'  
    
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
            writer.writerow([media, 'December 2015'])



