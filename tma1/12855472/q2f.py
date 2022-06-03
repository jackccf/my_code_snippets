# assignment q2f
# purpose: this program is to read the period of analysis and IAPI of each day, and print the result
# On 9/11/2021
# For Assignment q2f (comp-s258, 2021Autumn)

# main code starts

# to create and initial variables
inputList = []
sum = 0.0
unhealthyValue = 10.0
healthyValue = 2.0
counterUnhealthy = 0
counterHealthy = 0
counterHigher = 0

print ("IAPI Analyser")

# get the input of number of days
totalDays = int (input ("Enter number of days of the IAPI data collection period: "))

# to initial inputList
for d in range(totalDays) :
    inputList.append(d)


for d in range (totalDays) :
    print ("Enter the daily IAPI of day", d+1, ": ", end='')
    inputList[d] = float (input ())

    # input validation
    while inputList[d] <= 0 or inputList[d] > 20 :
        print ("Input Error: IAPI should be between 0 and 20.0")
        print ("Enter the daily IAPI of day", d+1, ": ", end='')
        inputList[d] = float (input ())
    
    # calculate the sum of all input data
    sum += inputList[d]

# calculate and print the average of all data
average = sum / totalDays
print ("Average daily IAPI in the period:", average)

# print the max daily IAPI
print ("Maximum daily IAPI in the period:", max(inputList))

# print the min daily IAPI
print ("Minimum daily IAPI in the period:", min(inputList))

# find and print number of days with very unhealthy IAPI
for v in inputList :
    if v > unhealthyValue :
        counterUnhealthy += 1
print ("Number of days with Very Unhealthy IAPI is", counterUnhealthy)

# find and print number of days with healthy IAPI
for v in inputList :
    if v <= healthyValue :
        counterHealthy += 1
print ("Number of days with Very Healthy IAPI is", counterHealthy)

# find and print number of days with IAPI higher than previous day
for d in range (totalDays-1) :
    if inputList[d+1] > inputList[d] :
        counterHigher += 1
print ("Number of days with IAPI higher than previous day is", counterHigher)

# for the purpose of displaying/seeing executing result
input ()
