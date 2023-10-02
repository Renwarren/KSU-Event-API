# feed.py

import requests
from requests_html import HTMLSession
import re
from event import Event


def get_source(url):
    """Get HTML source code"""
    try:
        session = HTMLSession()
        response = session.get(url)
        return response
    except requests.exceptions.RequestException as e:
        print(e)


def extract_image_url(input_string):
    pattern = r'(.*\.*png)'
    match = re.search(pattern, input_string)
    if match:
        return match.group()
    else:
        return None

def get_feed(url):
    response = get_source(url)
    events = []
    with response as r:
        items = r.html.find("item", first=False)

        for item in items:
            # Extract attributes in XML
            enclosure = item.find('enclosure', first=True)
            if enclosure is not None:
                full_url = enclosure.attrs.get('url')
                image_url = extract_image_url(full_url)

            category = item.find('category', first=True).text
            host = item.find('host', first=True).text if item.find('host') else 'N/A'
            author = item.find('author', first=True).text if item.find('author') else 'N/A'
            status = item.find('status', first=True).text if item.find('status') else 'N/A'

            title = item.find('title', first=True).text
            pubDate = item.find('pubDate', first=True).text
            guid = item.find('guid', first=True).text
            description = item.find('description', first=True).text
            description = re.sub(r'\]\]\>', '', description).rstrip()
            location = item.find('location', first=True).text

            event = Event(title, pubDate, guid, description, category, location, host, image_url, author, status)
            events.append(event)

    return events



# code to extract feed items and create Event objects
