# assignment q3a
# purpose: a python program that accepts two optional parameters of sort key and sort order,
#          and prints out the list of files in the current directory sorted and ordered accordingly.
#          default sort is 'name' and default order is 'asc' if no parameters taken in
# written by Cheung Chun Fai (s1285547)
# On 3/31/2021
# For Assignment_03 q3a (comp-s258, 2021Autumn)


import os
import sys
from datetime import datetime

path = '.'
fileList = []
entry_count = 0
size_sum = 0
key_sort, order_sort = 0, False

# change cwd
os.chdir(r'D:\HKMU\2021Autumn - s258\s258_assignments\assignment_03')

# get the file listing for the current directory
with os.scandir(path) as it:
    entry_file = []
    for entry in it:
        if entry.is_file():
            # store file_name, file_size, last_modify_time in entry_file list
            entry_file.append(
                [entry.name, entry.stat().st_size, entry.stat().st_mtime])
            size_sum += entry.stat().st_size


li_argv_1 = {'name': 0, 'size': 1, 'date': 2, 'NAME': 0, 'SIZE': 1, 'DATE': 2}
li_argv_2 = {'asc': False, 'desc': True, 'ASC': False, 'DESC': True}

# handle input from command-line argument
# handle case for more than 3 arguments
if len(sys.argv) > 3:
    print(
        "Maximum of 2 arguments expected: python fileSorter.py [sort field] [sort order]")
    sys.exit(1)

# handle case for 2 arguments
elif len(sys.argv) == 2:
    # handle invalid argument values
    if sys.argv[1] not in li_argv_1:
        print(
            f'''input {list(li_argv_1.keys())[:3]} for argument 1 \ninput {list(li_argv_2.keys())[:2]} for argument 2''')
        sys.exit(1)
    # set sort_key and sort_order based on input arguments
    else:
        key_sort = li_argv_1[sys.argv[1]]

# handle case for only one argument
elif len(sys.argv) == 1:
    pass    # default sorting and ordering

# handle case for 3 arguments
else:
    # handle invalid argument values
    if sys.argv[1] not in li_argv_1 or sys.argv[2] not in li_argv_2:
        print(
            f'''input {list(li_argv_1.keys())[:3]} for argument 1 \ninput {list(li_argv_2.keys())[:2]} for argument 2''')
        sys.exit(1)

    # set sort_key and sort_order based on input arguments
    key_sort = li_argv_1[sys.argv[1]]
    order_sort = li_argv_2[sys.argv[2]]

# sort file data according to acquired key_sort and order_sort
entry_file.sort(key=lambda li: li[key_sort], reverse=order_sort)

# print headers
print(f'{"Filename":<30s}{"Size":<18s}{"Last Modified":<15s}')

# print file data and total size
for i in entry_file:
    print(f'{i[0]:<27s} / {i[1]:<15d} / {datetime.fromtimestamp(i[2]).strftime("%a %b %d %H:%M:%S %Y")}')
print(f'Total file size: {size_sum}')
