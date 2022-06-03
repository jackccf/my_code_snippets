# assignment q3a
# purpose: a python program that
# written by Cheung Chun Fai (s1285547)
# On 3/29/2021
# For Assignment_02 q3a (comp-s258, 2021Autumn)


# import the random module
import random
# import the time module
import time
# import the math module
import math


# probability information about the business
noOfPassenger = (1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500)
probabilitiesTuple = (0.01, 0.02, 0.08, 0.13, 0.18,
                      0.21, 0.21, 0.10, 0.04, 0.02)

# create variables for given data
busCapacity = 19
costOfFuelATrip = 27
wageOfDriver = 620
costOfDpct = 264
costOfMaintenance = 35
hourOfOper = 8
hourOfSingleTrip = 0.5
fare = 7.5
tripsAMinibusAday = 16  # calculate totoal trips a minibus is able to make
costAMinibusADay = wageOfDriver + costOfDpct + \
    costOfMaintenance  # calculate fixed daily cost

# randPassenger() returns a number of passengers based on given number and weigh


def randPassenger():
    randPassenger = random.choices(noOfPassenger, probabilitiesTuple)
    return randPassenger[0]

# simulateOneDay() returns calculated profit/loss with given number of minibus


def simulateOneDay(numOfMinibus):
    availablePassengers = randPassenger()   # get available number of passengers

    # calculate actual number of passengers with given number of minibus
    actualPassengers = tripsAMinibusAday * numOfMinibus * 19

    if actualPassengers > availablePassengers:  # check and decide the real number of passengers
        actualPassengers = availablePassengers

    # calculate the real total trips
    tripsAday = math.ceil(actualPassengers / busCapacity)

    incomeADay = actualPassengers * fare    # calcuate the total income
    costAday = costAMinibusADay * numOfMinibus + \
        costOfFuelATrip * tripsAday    # calculate the total cost

    # calculate the net value, if positive, it is a profit, if negative, it is a loss
    return incomeADay - costAday

# findMaxProfit() analyze given data and print out the result


def findMaxProfit():
    average = [0] * 30  # create list to store result of 1 to 30 minibuses
    for i in range(1, 31):
        sum = 0
        for j in range(100000):
            sum += simulateOneDay(i)
        average[i-1] = sum / 100000
        print(f"Average profit for {i} minibus is: ${average[i-1]:.2f} ")

    # find the max value(highest profit) of average list
    maxProfit = max(average)
    # spot the index (number of minibus) of max value
    numOfMinibusForMaxProfit = average.index(maxProfit) + 1
    # print the result
    print(f"{numOfMinibusForMaxProfit} minibuses would have the highest profit")


# Set a fixed random seed
random.seed(0)

# Call function to find results
findMaxProfit()

# help to display result after executing the program
input()
