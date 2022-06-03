# assignment q3a
# purpose: this program is to solve equation a^2 + b^2 = c^3
# On 9/11/2021
# For Assignment q3a (comp-s258, 2021Autumn)

# main code starts

import math
from typing import Counter

# initialize variables
rootList = []
counter = 0

for a in range (1, 11, 1) :
    for b in range (1, 11, 1) :
        for c in range (1, 11, 1) :
            if a ** 2 + b ** 2 == c ** 3 :
                rootList.append (a)
                rootList.append (b)
                rootList.append (c)

                # count the number of combinations
                counter += 1

print (counter)
print ()
print (rootList)

# for the purpose of displaying/seeing executing result
input ()


