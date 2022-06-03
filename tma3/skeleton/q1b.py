
ans = 'y'  # default value to start the loop
while ans == 'y':

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

    if val is not None:
        pass
        # ENTER YOUR CODE HERE

    while True:
        ans = input('Want to enter another amount (y/n): ')
        # ADD REMAINING CODER TO HANDLE THE INPUT AND INVALID CASES
        if ans == 'n' or ans == 'y':
            break
