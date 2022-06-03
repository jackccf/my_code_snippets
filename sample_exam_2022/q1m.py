# What is the output when the following program is executed?

alist = list()
alist.append(1)
alist.append(2)
alist.append(3)
alist.append(4)
alist[1:2] = [0]
# print(alist)
alist.insert(0, -1)
# print(alist)

if __name__ == '__main__':
    print(alist[0:2])
