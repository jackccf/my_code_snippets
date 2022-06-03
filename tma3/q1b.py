# assignment q1b
# purpose: a python program that breaks down an amount of money and prints out the result
# written by Cheung Chun Fai (s1285547)
# On 3/31/2021
# For Assignment_03 q1b (comp-s258, 2021Autumn)


ans = 'y'  # default value to start the loop
while ans == 'y':
    # create a dictionary to store all face value in key and numbers in value,
    # and initialize all values to 0
    moneyBreakdown = {500: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}

    # Input Valdiation Loop
    while True:
        amount = input("Enter the amount you wish to break down: ")
        try:
            val = int(amount)
            if val < 5:
                print("Amount cannot be less than $5.")
                val = None  # None stand for error
                break
            else:
                break
        except:
            print("Please enter a valid dollar amount (whole numbers only).")
            val = None  # None stand for error
            break

    # perform the breakdown and store the result to moneyBreakdown dictionary
    if val is not None:
        moneyBreakdown[500] = int(val/500)
        val %= 500

        moneyBreakdown[100] = int(val/100)
        val %= 100

        moneyBreakdown[50] = int(val/50)
        val %= 50
        moneyBreakdown[20] = int(val/20)
        val %= 20

        moneyBreakdown[10] = int(val/10)
        val %= 10

        moneyBreakdown[5] = int(val/5)
        val %= 5

        moneyBreakdown[2] = int(val/2)
        val %= 2

        moneyBreakdown[1] = val

        # print out the result
        for key, value in moneyBreakdown.items():
            if value == 0:  # skip all denomination with 0 number
                pass
            else:
                print(f"$ {key} : {moneyBreakdown[key]}")

    while True:
        ans = input('Want to enter another amount (y/n): ')
        # ADD REMAINING CODER TO HANDLE THE INPUT AND INVALID CASES
        if ans == 'n' or ans == 'y':
            break
        else:
            pass    # ask for valid choice if input is not y/n
