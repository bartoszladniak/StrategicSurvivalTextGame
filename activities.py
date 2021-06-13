from constants.Hunt import *
from constants.Rest import *
from constants.Food import *
import random
from termcolor import colored

stats_health = 50
stats_energy = 50
stats_food = 50


def print_stats():
    print(colored("HEALTH:","green"), colored(stats_health,"yellow"),
          colored("ENERGY:","green"), colored(stats_energy,"yellow"),
          colored("FOOD:","green"), colored(stats_food,"yellow"))


class Activity:
    def __init__(self, description, success_rate=0.0, success_gain_health=0,
                 success_gain_food=0, success_gain_energy=0, failure_gain_health = 0,
                 failure_gain_energy = 0, failure_gain_food=0):
        self.description = description
        self.success_rate = success_rate
        self.success_gain_health = success_gain_health
        self.success_gain_food = success_gain_food
        self.success_gain_energy = success_gain_energy
        self.failure_gain_health = failure_gain_health
        self.failure_gain_food = failure_gain_food
        self.failure_gain_energy = failure_gain_energy

    def print_activity(self):
        print(self.description)
        print("    [ ", colored(self.success_rate * 100, "magenta"), "% ]",
              "[ Health: ", self.success_gain_health, " Energy: ", self.success_gain_energy, " Food: ", self.success_gain_food, " ]")
        print("    [ ", colored(100 - self.success_rate * 100,"magenta"), "% ]",
              "[ Health: ", self.failure_gain_health, " Energy: ", self.failure_gain_energy, " Food: ", self.failure_gain_food, " ]")

    def apply(self):
        global stats_food, stats_energy, stats_health
        success = False
        if random.random() <= self.success_rate:
            success = True

        health_gain = self.success_gain_health
        energy_gain = self.success_gain_energy
        food_gain = self.success_gain_food
        if not success:
            health_gain = self.failure_gain_health
            energy_gain = self.failure_gain_energy
            food_gain = self.failure_gain_food

        stats_health += health_gain
        stats_energy += energy_gain
        stats_food += food_gain

        if stats_health > 100:
            stats_health = 100
        if stats_energy > 100:
            stats_energy = 100
        if stats_food > 100:
            stats_food = 100

        if stats_food < 0:
            stats_health += stats_food
            stats_food = 0
        if stats_energy < 0:
            stats_health += stats_energy
            stats_energy = 0


        return success


#Food
food_list = list()

food_list.append(Activity(description = Food.FOOD_FISH.value, success_rate=0.6, success_gain_energy=-30,
                          success_gain_food=15, failure_gain_energy=-30))
food_list.append(Activity(description = Food.FOOD_BERRIES.value, success_rate=0.5, success_gain_energy=-30,
                          success_gain_food=20, failure_gain_energy=-30))
food_list.append(Activity(description = Food.FOOD_COCONUT.value, success_rate=0.7, success_gain_energy=-30,
                          success_gain_food=30, failure_gain_energy=-30, failure_gain_health=-50))
food_list.append(Activity(description = Food.FOOD_ALOE.value, success_rate=0.5, success_gain_health=10,
                          success_gain_energy=-10, failure_gain_health=-10, failure_gain_energy=-10))
food_list.append(Activity(description = Food.FOOD_NONE.value, success_rate=1))

#Rest
rest_list = list()
rest_list.append(Activity(description = Rest.REST.value, success_rate=0.9, success_gain_energy=20,
                          success_gain_health=5, failure_gain_energy=15))
#Hunting
hunting_list = list()
hunting_list.append(
    Activity(
        description=Hunt.FOOD_TURTLE.value,
        success_rate=0.95,
        success_gain_energy=-30,
        success_gain_health=-5,
        success_gain_food=10,
        failure_gain_energy=-30,
        failure_gain_health=-20,
        failure_gain_food=0
    )
)
hunting_list.append(
    Activity(
        description=Hunt.FOOD_RABBIT.value,
        success_rate=0.3,
        success_gain_energy=-50,
        success_gain_health=-5,
        success_gain_food=30,
        failure_gain_energy=-50,
        failure_gain_health=-30,
        failure_gain_food=0
    )
)

hunting_list.append(
    Activity(
        description=Hunt.FOOD_BOAR.value,
        success_rate=0.3,
        success_gain_energy=-50,
        success_gain_health=-40,
        success_gain_food=40,
        failure_gain_energy=-50,
        failure_gain_health=-50,
        failure_gain_food=0
    )
)

hunting_list.append(
    Activity(
        description=Hunt.FOOD_BEAR.value,
        success_rate=0.2,
        success_gain_energy=-50,
        success_gain_health=-50,
        success_gain_food=70,
        failure_gain_energy=-50,
        failure_gain_health=-80,
        failure_gain_food=0
    )
)
hunting_list.append(
    Activity(
        description=Hunt.FOOD_NONE.value,
        success_rate=1
    )
)

