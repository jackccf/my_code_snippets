# Improve the input validation to your solution for Question 2(c) above. If the month input is invalid, 
# in addition to printing the error message, the user is asked to re-enter.

days_in_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

while True:
    try:
        month_in = int(input("month: "))
        assert (month_in >= 1 and month_in <= 12)
        print(f"month of {month_in} has {days_in_month[month_in-1]} days")
        break

    except: 
        print("invalid input.")
