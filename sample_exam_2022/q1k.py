# What is the output when the following program is executed?

def funcB(x, y):
    x += 2
    return x + y
x = 3
y = 4
y = funcB(y, x)
print(x, y)
