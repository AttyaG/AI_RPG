class MainCharacter:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(MainCharacter, cls).__new__(cls)
        return cls.instance
    def __init__(self, name=None, currentLocation=None):
        self.name = None
        self.currentLocation = None
        self.level = 0
        self.role = None
        self.health_limit = None
        self.remaining_health = None
        self.power = None
        self.energy = None
        self.mana = None
        self.armor = None

    def setName(self, newName):
        self.name = newName

    def getName(self):
        return self.name

    def setCurrentLocation(self, place):
        self.currentLocation = place

    def getCL(self):
        return self.currentLocation


'''

    def go(self, place):
        self.setCurrentLocation(place)


'''
