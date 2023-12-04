from datetime import datetime


now = datetime.now()

date_string = now.strftime("%Y-%m-%dT%H:%M:%S")
timezone_string = now.strftime("%z")

# URL encode : and -
date_string = date_string.replace(":", "%3A")
timezone_string = timezone_string.replace("-", "%2D")

today = "" + date_string + timezone_string

