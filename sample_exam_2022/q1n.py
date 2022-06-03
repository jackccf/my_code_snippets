# (i) What is the output when the following program is executed?
# (ii) How many times will the if statement executed after the execution is completed?
# (iii) Explain the difference between the data stored in the variables clist and dlistdlist.

from q1m import alist


for num in alist:
    count = 0
    clist = "AKLMNO"
    dlist = ['A', 'E', 'I', 'O', 'U']
    for ch in clist:
        for d in dlist:
            if ch == d:
                count += 1
print (count)                
