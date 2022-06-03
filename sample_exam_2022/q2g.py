# An old carpenter makes furniture using British length measurements in yards, feet and inches. He would like to have 
# a function that accepts a length measurement in meters and centimeters then converts and returns the equivalent length 
# in yards, feet, and inches so that he can understand the requirements from the young customers using Standard International (SI) 
# length measurements in meters and centimeters.

# The function has input parameters meters that should be an integer and centimeters that should be a float. 
# The 3 return values from the function are yards (integer) and feet (integer) and inches (float).

# The conversion rate is given in the following.
# • 1 meter = 100 centimeters
# • 1 inch = 2.54 centimeters
# • 1 foot = 12 inches
# • 1 yard = 3 feet

# Complete the following function.
# def convert (meters, centimeters):

from lib2to3.pytree import convert


def convert (meters, centimeters):
    cm_sum = meters * 100 + centimeters

    inches = cm_sum / 2.54
    feet = int(inches // 12)
    inches = inches % feet

    yards = int(feet // 3)
    feet = int(feet % 3)

    return yards, feet, inches

if __name__ == "__main__":
    y,f,i = convert(3, 77)
    print(f"{y} yards {f} feet {i} inches")


