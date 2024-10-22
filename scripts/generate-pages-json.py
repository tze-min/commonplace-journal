import os
import json
from bs4 import BeautifulSoup
import hashlib
# import PyRSS2Gen
import xml.etree.ElementTree as ET
from datetime import datetime

HTML_DIRECTORY = './pages'
PAGES_JSON = 'pages.json'
RSS_XML = 'feed.xml'

def get_html_pages(filepath):
    '''
    Visit a html file given its filepath, parse the contents, and return a dict of the title, filepath and data-tags
    '''
    with open(filepath, 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')
        published_time = soup.find('meta', property='article:published_time')['content']
        modified_time = soup.find('meta', property='article:modified_time')['content']
        title = soup.title.string.strip()
        tags = soup.body.get('data-tags').split(';')
        tags = [tag.strip() for tag in tags]
        content = soup.body
        
        result = {
            'title': title, 
            'url': filepath,
            'published': published_time,
            'modified': modified_time,
            'tags': tags,
            'content': content
        }
        return result

def create_rss_item(filepath):
    with open(filepath, 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')
        published_time = soup.find('meta', property='article:published_time')['content']
        modified_time = soup.find('meta', property='article:modified_time')['content']
        title = soup.title.string.strip()
        # tags = soup.body.get('data-tags').split(';')
        # tags = [tag.strip() for tag in tags]
        content = soup.body

        guid = hashlib.md5(filepath.encode()).hexdigest()

        item = ET.Element('item')
        ET.SubElement(item, 'title').text = title
        ET.SubElement(item, 'link').text = 'https://commonplace-journal.pages.dev' + filepath[1:]
        ET.SubElement(item, 'guid').text = guid
        ET.SubElement(item, 'description').text = '<![CDATA[' + str(content) + ']]>'
        ET.SubElement(item, 'pubDate').text = datetime.strftime(datetime.strptime(published_time, '%Y-%m-%d'), "%a, %d %b %Y %H:%M:%S +0000")
        ET.SubElement(item, 'lastBuildDate').text = datetime.strftime(datetime.strptime(modified_time, '%Y-%m-%d'), "%a, %d %b %Y %H:%M:%S +0000")

        return item

def sort_html_pages(pages, reverse=True, by='published'):
    '''
    Given a list of dictionaries, sort them by the given key word
    '''
    return sorted(pages, key=lambda page: page[by], reverse=reverse)

def get_html_pages_from_directory(directory):
    '''
    Given a directory of html files, iterate through each file and apply get_html_tags to return a list of dict
    '''
    pages = []
    for filename in os.listdir(directory):
        filepath = directory + '/' + filename
        full_dict = get_html_pages(filepath)
        dict_for_pages_json = {key: full_dict[key] for key in full_dict if key not in ['content']}
        pages.append(dict_for_pages_json)
    return sort_html_pages(pages)

def get_rss_items_from_directory(directory):
    items = []
    for filename in os.listdir(directory):
        filepath = directory + '/' + filename
        item = create_rss_item(filepath)
        items.append(item)
        print('Generating guid...', filename, item)
    return items

def generate_pages_json(directory):
    '''
    Replace PAGES_JSON file with html tags yoinked from HTML_DIRECTORY
    '''
    pages = get_html_pages_from_directory(directory)
    with open(PAGES_JSON, 'w', encoding='utf-8') as outfile:
        json.dump(pages, outfile, indent=2)

def generate_rss_feed(directory):
    feed = ET.Element('rss', version='2.0')
    channel = ET.SubElement(feed, 'channel')
    ET.SubElement(channel, 'title').text = "Tze Min's commonplace journal"
    ET.SubElement(channel, 'link').text = "https://commonplace-journal.pages.dev"
    ET.SubElement(channel, 'description').text = "Here, I write about my everyday learnings, including my notes, thoughts and references."
    ET.SubElement(channel, 'lastBuildDate').text = datetime.now().strftime("%a, %d %b %Y %H:%M:%S +0000")
    
    items = get_rss_items_from_directory(directory)
    for item in items:
        channel.append(item)
    
    print('feed...', feed)
    tree = ET.ElementTree(feed)
    print('tree...', tree)
    tree.write(RSS_XML, encoding='utf-8', xml_declaration=True)
    # print(type(ET.tostring(feed, encoding="unicode")))
    # tree = ET.ElementTree(ET.tostring(feed, encoding="utf-8"))
    # tree.write(RSS_XML, encoding="utf-8", xml_declaration=True)

if __name__ == "__main__":
    generate_rss_feed(HTML_DIRECTORY)
    # generate_pages_json(HTML_DIRECTORY)