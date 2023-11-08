import pymysql
from bs4 import BeautifulSoup
from get_event_data import events

db = pymysql.connect(host='eventtracker.ctgvnaaozzpy.us-east-2.rds.amazonaws.com',
                     user='admin',
                     password='Mnas1506$',
                     db='eventtracker',
                     port=3306)


def list_to_string(stringify):
    if len(stringify) == 0:
        return "NULL"
    else:
        return ", ".join(stringify)


cursor = db.cursor()
cursor.execute("DELETE FROM `eventtracker`.`eventB`")

for item in [event.__dict__ for event in events]:
    id = item['id']
    organizationName = item['organizationName']
    organizationNames = list_to_string(item['organizationNames'])
    name = item['name']
    desc = item['description']
    # if desc is None:
    #     desc = ""
    description = BeautifulSoup(desc, 'html.parser').getText().rstrip().replace('\xA0', '').replace('\r\n', '').replace(
        '\s+', '')
    location = item['location']
    startsOn = item['startsOn']
    endsOn = item['endsOn']
    theme = item['theme']
    categoryNames = list_to_string(item['category_names'])
    benefitNames = list_to_string(item['benefit_names'])
    institutionId = item['institutionId']
    organizationId = item['organizationId']
    organizationIds = list_to_string(item['organizationIds'])
    organizationProfilePicture = item['organizationProfilePicture']
    branchId = item['branchId']
    imagePath = item['imagePath']
    visibility = item['visibility']
    status = item['status']
    searchScore = item['searchScore']

    query = "INSERT INTO `eventtracker`.`eventB` (`id`,`organizationName`,`organizationNames`,`name`,`description`," \
            "`location`,`startsOn`,`endsOn`,`theme`,`categoryNames`,`benefitNames`,`institutionId`,`organizationId`," \
            "`organizationIds`,`organizationProfilePicture`,`branchId`,`imagePath`,`visibility`,`status`," \
            "`searchScore`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "

    cursor.execute(query, (
        id, organizationName, organizationNames, name, description, location, startsOn, endsOn, theme, categoryNames,
        benefitNames, organizationId, institutionId, organizationIds, organizationProfilePicture, branchId, imagePath,
        visibility, status, searchScore))
    #print("committed")
    db.commit()

db.close()


