# Write a complete program that reads in a month as a number (e.g. 1 for January; 2 for February, etc.) 
# and prints out the number of days in that month. Assume that the year is not a leap year (so February has 28 days). 
# Print an error message if the input month is out of the valid range.

days_in_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

try:
    month_in = int(input("month: "))
    assert (month_in >= 1 and month_in <= 12)
    print(f"month of {month_in} has {days_in_month[month_in-1]} days")

except: 
    print("invalid input.")

    