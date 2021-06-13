from termcolor import colored
import time
import activities as a
import constants.UI as UIConstants
import random as rand
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def draw_day_description():
    return rand.choice(list(UIConstants.UI)).value


def draw_food_activity():
    return rand.choice(a.food_list)


def draw_hunt_activity():
    return rand.choice(a.hunting_list)


def draw_rest_activity():
    return rand.choice(a.rest_list)


def get_activities():
    activities = []

    food_activity = draw_food_activity()
    print(colored("1. Zbieranie zapasów", "blue"))
    food_activity.print_activity()
    time.sleep(0.5)

    hunt_activity = draw_hunt_activity()
    print(colored("2. Czas na polowanie", "blue"))
    hunt_activity.print_activity()
    time.sleep(0.5)

    rest_activity = draw_rest_activity()
    print(colored("3. Dziś dzień na odpoczynek", "blue"))
    rest_activity.print_activity()
    time.sleep(0.5)

    activities.append(food_activity)
    activities.append(hunt_activity)
    activities.append(rest_activity)
    return activities

def one_night():
    activity = a.Activity(
        description="night",
        success_rate=1,
        success_gain_energy=20,
        success_gain_health=5,
        success_gain_food=-10)
    activity.apply()

    print(colored("Zapadła noc...\n","grey"))
    time.sleep(0.8)
    print(colored("Health +5","red"))
    time.sleep(0.3)
    print(colored("Energy +20","red"))
    time.sleep(0.3)
    print(colored("Food -10\n","red"))
    time.sleep(2)


def one_day(day):
    time.sleep(0.3)
    print(colored("DAY ", "green"), colored(day, "green"))
    time.sleep(0.5)
    a.print_stats()
    time.sleep(0.5)
    day_description = draw_day_description()
    print(day_description)
    time.sleep(2.1)

    activities1 = get_activities()

    choice = 0
    while choice < 1 or choice > 3:
        choice = int(input(colored("Co zrobisz?\n","blue")))

    chosen_activity = activities1[choice - 1]
    returned = chosen_activity.apply()
    if returned:
        print(colored("ODNIOSŁEŚ SUKCES", "green"))
    else:
        print(colored("PONIOSŁEŚ PORAŻKĘ", "red"))

    a.print_stats()



def start_game(n):
    for day in range(n):
        one_day(day + 1)
        time.sleep(1.7)
        cls()
        one_night()
        cls()
        if a.stats_health == 0:
            print(colored("Umarłeś. Życzymy powodzenia następnym razem","red"))
            break

if __name__ == "__main__":
    print("...")
    start_game(30)
