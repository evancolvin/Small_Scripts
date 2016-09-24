import random
from __future__ import division


def monty_hall(switch = True, iterations = 100000):
    cars = 0
    goats = 0
    for i in range(iterations):
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
                cars += 1
            else:
                goats += 1
        else: # switch == True
            doors = [1, 2, 3]
            doors.remove(guess)
            doors.remove(reveal)
            if doors[0] == car:
                cars += 1
            else:
                goats += 1
    return cars/iterations, goats/iterations
