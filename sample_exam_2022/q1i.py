# What is the output when the following program is executed?

x = 9
y = 8
while True:
    if x <= 0: break
    x = x -3
    y = y - 2
    if x > y: continue
    break
print(x, y)

    