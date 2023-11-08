import requests
from date_time import today

url = 'https://owllife.kennesaw.edu/api/discovery/event/search?endsAfter={' '}&orderByField=endsOn&orderByDirection=ascending&status=Approved'.format(today)


py_wpage = requests.get(url)
data1 = py_wpage.json()
Total = str(data1['@odata.count'])
#print(Total)
#print(today)
