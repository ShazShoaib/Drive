from settings import *

class speedMan:

    def __init__(self):
        pass

    def add(self,value):
        global ROAD_SPEED
        if ROAD_SPEED*SPEEDOMETER_ACCELERATION + value < MAX_SPEED:
            ROAD_SPEED = ROAD_SPEED + value

    def mul(self,value):
        global ROAD_SPEED
        if ROAD_SPEED*SPEEDOMETER_ACCELERATION * value < MAX_SPEED:
            ROAD_SPEED = ROAD_SPEED * value

    def getSpeed(self):
        global ROAD_SPEED
        return ROAD_SPEED
