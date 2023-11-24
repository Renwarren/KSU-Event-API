class Event:

    def __init__(self, id, organizationName, organizationNames, name, description, location, startsOn, endsOn, theme,
                 category_names, benefit_names, institutionId, branchId, organizationIds, organizationProfilePicture,
                 organizationId, status,
                 imagePath, visibility, searchScore):
        self.id = id
        self.organizationName = organizationName
        self.organizationNames = organizationNames
        self.name = name
        self.description = description
        self.location = location
        self.startsOn = startsOn
        self.endsOn = endsOn
        self.theme = theme
        self.category_names = category_names
        self.benefit_names = benefit_names
        self.searchScore = searchScore
        self.status = status
        self.visibility = visibility
        self.imagePath = imagePath
        self.organizationProfilePicture = organizationProfilePicture
        self.branchId = branchId
        self.organizationIds = organizationIds
        self.organizationId = organizationId
        self.institutionId = institutionId


#print(sys.getsizeof(Event), "bytes")  # size of an event object
