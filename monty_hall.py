import random
from __future__ import division
import matplotlib.pyplot as plt


def monty_hall(switch = True):
    doors = [1, 2, 3]
    guess = random.choice(doors)
    car = random.choice(doors)
    doors.remove(car)
    goat1, goat2 = doors[0], doors[-1]

    # revealing the door not the car or not the guess
    if guess == car: # won't matter which to reveal first
        reveal = random.choice(doors)
    else:
        doors.remove(guess)
        reveal = doors[0]

    # figuring out if they won the car
    if switch == False:
        if car == guess:
            win = 'car'
        else:
            win = 'goat'
    else: # switch == True
        doors = [1, 2, 3]
        doors.remove(guess)
        doors.remove(reveal)
        if doors[0] == car:
            win = 'car'
        else:
            win = 'goat'
    return win

# Running the simulation
def monty_simulation(iterations, switch = True):
    cars, goats = 0, 0
    for i in range(iterations):
        prize = monty_hall(switch = switch)
        if prize == 'car':
            cars += 1
        else:
            goats += 1
    return cars/iterations, goats/iterations

def plot_monty(iterations):
    # Plots the proportion of success for each iteration
    outcomes_with_switch = [0]
    outcomes_no_switch = [0]
    cars = 0
    # Plotting outcome with switch
    for i in range(1, iterations+1):
        if monty_hall() == 'car':
            cars += 1
            outcomes_with_switch.append(cars/i)
        else:
            # Need to add something to make the proportion go down
            # when you don't get a car
            outcomes_with_switch.append(outcomes_with_switch[i-1]*(i-1)/i)

    cars = 0
    # Plotting outcomes without switch
    for i in range(1, iterations+1):
        if monty_hall(switch = False) == 'car':
            cars += 1
            outcomes_no_switch.append(cars/i)
        else:
            outcomes_no_switch.append(outcomes_no_switch[i-1]*(i-1)/i)

    plt.plot(outcomes_with_switch, color = 'c')
    plt.plot(outcomes_no_switch, color = 'm')
    plt.legend(['When You Switch', "When You Don't"])
    plt.show()
