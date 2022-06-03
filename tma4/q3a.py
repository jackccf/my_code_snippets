# tma4 q3a
# purpose: a python program that schedule meeting requests to two conference room according to given rules
# written by Cheung Chun Fai (s1285547)
# On 4/24/2021
# For tma4 q3a (comp-s258, 2021Autumn)
# progress: all completed


from csv import DictReader
from datetime import datetime
import sys, os
from time import strptime
from unittest import skip

# change working directory
# os.chdir(r"D:\HKMU\2021Autumn - s258\s258_assignments\assignment_04")

# create file object for both rm A and B
in_A = list(DictReader(open("meeting_requests.csv", "r", encoding="utf-8-sig")))
in_B = list(DictReader(open("conf_B_sched.csv", "r", encoding="utf-8-sig")))


# sort schedule of rm A by "end time" (sort by "Start Time" first in order to utilise the stable property of python sort)
in_A.sort(key=lambda i : datetime.strptime(i["Start Time"], "%I:%M %p"))
in_A.sort(key=lambda i : datetime.strptime(i["End Time"], "%I:%M %p"))

# sort schedule of rm-B with end time (sort with start time first)
in_B.sort(key=lambda i : datetime.strptime(i["Start Time"], "%I:%M %p"))
in_B.sort(key=lambda i : datetime.strptime(i["End Time"], "%I:%M %p"))

# use greedy approach algo to evaluate and classify each request to choosen, not-choosen and rejected
a_ok = []
a_no = []
a_rej = []
count_rej = 0

for i in range(len(in_A)):

    # create date object of "Start time" and "end time" from given csv data 
    ts = datetime.strptime(in_A[i]["Start Time"], "%I:%M %p")
    te = datetime.strptime(in_A[i]["End Time"], "%I:%M %p")

    # create date object of "morning time" and "night time" additional requiremnt
    tm = datetime.strptime("08:00 AM", "%I:%M %p")
    tn = datetime.strptime("07:00 PM", "%I:%M %p")

    # check addtional requirement, only request from 8am to 7pm is allowed
    if ts < tm or te > tn:
        a_rej.append(in_A[i])
        count_rej += 1

    else:
        # evaluate and classify the first request (offset by addtional requirement)
        if i-count_rej == 0:
            a_ok.append(in_A[i])

        else:
            # if meeting time is overlapped, put it to not-choosen 
            if ts < datetime.strptime(a_ok[len(a_ok)-1]["End Time"], "%I:%M %p"):
                a_no.append(in_A[i])
            else:
                a_ok.append(in_A[i]) # put it to choosen otherwise

# evaluate and classify "not-choosen" request to rm B or to rejected
a_to_b = []
for i in a_no:
    t = datetime.strptime(i["Start Time"], "%I:%M %p")
    for j in in_B:
        ts = datetime.strptime(j["Start Time"], "%I:%M %p")
        te = datetime.strptime(j["End Time"], "%I:%M %p")
        # put to rejected if "start time" is clash with existing schedules in rm B
        if t > ts and t < te:
            a_rej.append(i)
            break
    if i not in a_rej:
        a_to_b.append(i)    # put to rm B if no clash


# extract request number from result 
rst_a = []
rst_b = []
rst_rej = []

for i in a_ok:
    rst_a.append(i["Request"])

for i in a_to_b:
    rst_b.append(i["Request"])

for i in a_rej:
    rst_rej.append(i["Request"])

# print out the result
print("conference A Schedule: ", ', '.join(rst_a))
print("conference B Schedule: ", ', '.join(rst_b))
print("Rejected Meetings: ", ', '.join(rst_rej))
