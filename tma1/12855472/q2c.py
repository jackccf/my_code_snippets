# assignment q2c
# purpose: to create a lookup table for equivalent radians
# written by Cheung Chun Fai
# On 9/11/2021
# For Assignment q2c (comp-s258, 2021Autumn)

# main code starts

import math

dgToRd = math.pi/180

print ('%10s %10s %10s %10s' %('Degrees', 'Radians', 'Sin', 'Cos') )

for n in range (0, 91, 5) :
    nInRad = n*dgToRd
    print (format (n, '10.4f'), format (n*dgToRd, '10.4f'), format (math.sin(nInRad), '10.4f'), format (math.cos(nInRad), '10.4f'))

# for the purpose of displaying/seeing executing result
input ()
