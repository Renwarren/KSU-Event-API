from event_count import Total
import requests
from event_class import Event
from date_time import today

value = Total
BASE_URL = "https://owllife.kennesaw.edu/api/discovery/event/search"
parameters = {
    "endsAfter": today,
    "orderByField": "endsOn",
    "orderByDirection": "ascending",
    "status": "Approved",
    "take": value,
    "query": "",
}
base_url = 'https://owllife.kennesaw.edu/api/discovery/event/search?endsAfter={' '}' \
           '&orderByField=endsOn&orderByDirection=ascending&status=Approved&take={' \
           '}'.format(
    today,
    value)

response = requests.get(base_url).json()
#print(response)


def get_json_events(r):
    e = []
    for item in r['value']:
        id = item['id']
        organizationName = item['organizationName']
        organizationNames = item['organizationNames']
        name = item['name']
        description = item['description']
        location = item['location']
        startsOn = item['startsOn']
        endsOn = item['endsOn']
        theme = item['theme']
        categoryNames = item['categoryNames']
        benefitNames = item['benefitNames']
        institutionId = item['institutionId']
        organizationId = item['organizationId']
        organizationIds = item['organizationIds']
        organizationProfilePicture = item['organizationProfilePicture']
        branchId = item['branchId']
        imagePath = item['imagePath']
        visibility = item['visibility']
        status = item['status']
        searchScore = item['@search.score']

        ev = Event(id, organizationName, organizationNames, name,
                   description, location, startsOn, endsOn, theme,
                   categoryNames,
                   benefitNames, institutionId, branchId, organizationIds, organizationProfilePicture,
                   organizationId, status,
                   imagePath, visibility, searchScore)
        e.append(ev)

    return e


events = get_json_events(response)
