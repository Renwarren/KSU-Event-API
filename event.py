# event.py

class Event:

    def __init__(self, title, pubDate, guid, description, category, location, host, image_url, author, status):
        self.title = title
        self.pubDate = pubDate
        self.guid = guid
        self.description = description
        self.category = category
        self.location = location
        self.host = host
        self.image_url = image_url
        self.author = author
        self.status = status