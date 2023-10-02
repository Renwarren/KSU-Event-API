# main.py
import sys
from event import Event
from feed import get_feed

url = "https://owllife.kennesaw.edu/events.rss"

events = get_feed(url)

for event in events:
    print(f"Title: {event.title}")
    print(f"Date: {event.pubDate}")
    print(f"GUID: {event.guid}")
    print(f"Description: {event.description}")
    print(f"Category: {event.category}")
    print(f"Location: {event.location}")
    print(f"Host: {event.host}")
    print(f"URL: {event.image_url}")
    print(f"Author: {event.author}")
    print(f"Status: {event.status}")

    print("--")  # separator

print(sys.getsizeof(Event), "bytes") #size of an event object
