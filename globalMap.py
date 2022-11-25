class GlobalMap:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(GlobalMap, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.places = {}

    def addPlace(self, place, neiborhood: list):
        if not place in self.places:
            self.places[place] = neiborhood

    def getPlaces(self):
        return self.places



class MapGraph:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(GlobalMap, cls).__new__(cls)
        return cls.instance

        
