import os
import sys
import time
from operator import itemgetter, methodcaller

path = '.'
fileList = []
entry_count = 0

#get the file listing for the current directory
with os.scandir(path) as it:
    for entry in it:
        if entry.is_file():
            print(entry.name)

# HANDLE THE INPUT ARGUEMNTS
if len(sys.argv)  > 3:
    print("Maximum of 2 arguments expected: python fileSorter.py [sort field] [sort order]")
    sys.exit(1)
# COMPELTE THE REMAINING PART OF INPUT ARGUMENT HANDLING


# COMPLETE THE REST OF THE PROGRAM