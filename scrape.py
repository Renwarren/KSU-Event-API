import requests
import pandas as pd
from requests_html import HTMLSession
import re


# Events class
class Events:

    def __init__(self):
        self.df = None

    def set_events(self, df):
        self.df = df

    def get_events(self):
        return self.df



def get_source(url):
    """Get HTML source code"""

    try:
        session = HTMLSession()
        response = session.get(url)
        return response

    except requests.exceptions.RequestException as e:
        print(e)


def extract_image_url(input_string):
    pattern = r'(.*\.png)'
    match = re.search(pattern, input_string)
    if match:
        return match.group()
    else:
        return None


def get_feed(url):
    response = get_source(url)

    df = pd.DataFrame(
        columns=['title', 'pubDate', 'guid', 'description', 'category', 'location', 'host', 'url','author','status'])

    with response as r:
        items = r.html.find("item", first=False)

        for item in items:

            # Extract attributes in XML
            enclosure = item.find('enclosure', first=True)
            if enclosure is not None:
                full_url = enclosure.attrs.get('url')
                url = extract_image_url(full_url)



            category = item.find('category', first=True).text
            host = item.find('host', first=True).text if item.find('host') else 'N/A'
            author = item.find('author', first=True).text if item.find('author') else 'N/A'
            status = item.find('status', first=True).text if item.find('status') else 'N/A'

            title = item.find('title', first=True).text
            pubDate = item.find('pubDate', first=True).text
            guid = item.find('guid', first=True).text
            description = item.find('description', first=True).text
            location = item.find('location', first=True).text

            # Build row dict
            row = {'title': title, 'pubDate': pubDate, 'guid': guid, 'description': description, 'category': category,
                   'location': location, 'host': host, 'author': author, 'url': url, 'status': status}

            # Create DataFrame from row
            row_df = pd.DataFrame(row, index=[0])

            # Append to main DataFrame
            df = pd.concat([df, row_df], ignore_index=True)

    return df


url = "https://owllife.kennesaw.edu/events.rss"
df = get_feed(url)

# Create Events object
events = Events()

# Set df
events.set_events(df)

# Access df and print object to stdout
#print(events.get_events())


# Set print options
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
print(df)#Prints to stdout

df.to_csv('data49.csv', index=False)#saves to file in current directory use it to see the entirety of the dataframe
