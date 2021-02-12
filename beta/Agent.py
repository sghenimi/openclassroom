import json
import math

class Zone:
    MIN_LONGITUDE = -180
    MAX_LONGITUDE = 180
    WIDTH_DEGREES = 1
    def __init__(self, corner_left, corner_right):
        self.corner_left = corner_left
        self.corner_right = corner_right
        self.inhabitants = 0
    def init_zones(self):
        for longitude in range(self.MIN_LONGITUDE, self.MAX_LONGITUDE)

class Position:
    def __init__(self, longit, latit):
        self.longitude_deg = longit
        self.latitude_deg = latit
    @property
    def longitude(self):
        return self.longitude_deg * math.pi/180
    @property
    def latitude(self):
        return self.latitude_deg * math.pi/180

class Agent:
    def __init__(self, position, **attributes):
        self.position = position
        for attr_name, attr_value in attributes.items():
            setattr(self, attr_name, attr_value)


agent_attributes = {"neuroticism": -0.0739192627121713, "language": "Shona", "latitude": -19.922097800281783, "country_tld": "zw", "age": 12, "income": 333, "longitude": 29.798455535838603, "sex": "Male", "religion": "syncretic", "extraversion": 1.051833688742943, "date_of_birth": "2005-01-10", "agreeableness": 0.1441229877537559, "id_str": "LB3-3Cl", "conscientiousness": 0.2419104411765549, "internet": False, "country_name": "Zimbabwe", "openness": -0.024607605122172617, "id": 6636726630}

def go_main():
    for myattributes in json.load(open("files/agents-100k.json")):

        longitude = myattributes.pop("longitude")
        latitude = myattributes.pop("latitude")

        my_position = Position(longitude, latitude)
        my_agent = Agent(my_position, **myattributes)

        #print(my_agent.position.latitude,"  ,  ", my_agent.position.longitude)
        #mzone = Zone()
        print(Zone.MIN_LONGITUDE)


go_main()