# assignment q1c
# purpose: a python program that reads in GPA value and prints the burger price accordingly
# written by Cheung Chun Fai (s1285547)
# On 3/29/2021
# For Assignment_02 q1c (comp-s258, 2021Autumn)


# initialize a dictionary with data of given correspondence of between GPA and burger price
burgerPrice = {'A': '$50', 'B': '$45', 'C': '$40', 'D': '$35', }

# Input Validation Loop
while True:
    gpaStr = input('Enter GPA: ')

    # check if input is empty
    if gpaStr == '':
        print('The input is empty')
        continue

    # validate other input errors
    else:
        try:
            gpa = float(gpaStr)

        except Exception as err:
            print('The input is not a number')
            continue

        if gpa < 0:
            print('The GPA should be positive')
            continue

        elif (gpa >= 0 and gpa < 2.0) or gpa > 4.0:
            print('The GPA should be >= 2.0 and <=4.0')
            continue

        # map the inputted GPA to price based on the given information
        else:
            if gpa >= 3.5:
                grade = 'A'
            elif gpa >= 3.0 and gpa < 3.5:
                grade = 'B'
            elif gpa >= 2.5 and gpa < 3.0:
                grade = 'C'
            else:
                grade = 'D'

        print('The price is ', burgerPrice[grade], end='')
        break

# help to display result after executing the program
input()
