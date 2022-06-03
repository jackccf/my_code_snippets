# Consider executing the following program that is a simple question on arithmetic.
# The program prints “Wrong!” if the input is “0.6666”, “0.66666”, or even “0.666666” which are supposed to be correct. Suggest the reasons.

answer = input("enter the result of 2 divided by 3: ")
if (answer == 2 / 3):
    print("correct!")
else:
    print("wrong!")


# There are 2 problems in the given program.
# First, the variable answer references to a string input by the user. The comparison of a string with a floating point value 2 / 3 is always different.
# Second, even though if we change the input statement to
# answer = float(input ("Enter the result of 2 divided by 3 :"))
# to convert the string input by a user to a floating point value, the result output by the program is also “Wrong!”
# Since 2 / 3 gives a floating-point value. Floating-point values cannot be represented exactly in computer memory.
# So the comparison of 2 floating-point values by means of == operator are always different. A reasonable way to compare 2 floating point values 
# is to use comparison <= and >= to test within an acceptable range such as 0.66 to 0.67.