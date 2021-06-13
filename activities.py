import constants.Food as food
from constants.Health import *
from constants.Energy import *

class Activity:
    def __init__(self, description, success_rate=0.0, success_gain_health=0, success_gain_food=0, success_gain_energy=0):
        self.description = description
        self.success_rate = success_rate
        self.success_gain_health = success_gain_health
        self.success_gain_food = success_gain_food
        self.success_gain_energy = success_gain_energy

    def apply(self):
        


food_list = list()
health_list = list()
having_a_rest_list = list()
hunting_list = list()



food_list.append(Activity(description=food.FOOD_FISH))
food_list.append(Activity(description=food))