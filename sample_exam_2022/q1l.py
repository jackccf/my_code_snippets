# What is the output when the following program is executed?

def funcC(a, b):
    a = a * b
    return b * b > a
x = funcC(a=2, b=3)
print(x)