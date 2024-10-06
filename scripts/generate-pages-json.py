import os
import json
from bs4 import BeautifulSoup

HTML_DIRECTORY = './pages'
PAGES_JSON = 'pages.json'

def get_html_pages(filepath):
    '''
    Visit a html file given its filepath, parse the contents, and return a dict of the title, filepath and data-tags
    '''
    with open(filepath, 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')
        title = soup.title.string.strip()
        tags = soup.body.get('data-tags').split(';')
        tags = [tag.strip() for tag in tags]
        
        result = {
            'title': title, 
            'url': filepath,
            'tags': tags
        }
        return result

def get_html_pages_from_directory(directory):
    '''
    Given a directory of html files, iterate through each file and apply get_html_tags to return a list of dict
    '''
    pages = []
    for filename in os.listdir(directory):
        filepath = directory + '/' + filename
        pages.append(get_html_pages(filepath))
    return pages

def generate_pages_json(directory):
    '''
    Replace PAGES_JSON file with html tags yoinked from HTML_DIRECTORY
    '''
    pages = get_html_pages_from_directory(directory)
    with open(PAGES_JSON, 'w', encoding='utf-8') as outfile:
        json.dump(pages, outfile, indent=2)

if __name__ == "__main__":
    generate_pages_json(HTML_DIRECTORY)