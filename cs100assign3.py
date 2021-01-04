x = float(input('Enter x'))
y = float(input('Enter y'))
if x >= 0:
    if y >= 0:
        print(x + y)
    else:
        print(x + y ** 2)
else:
    if y >= 0:
        print(x ** 2 + y)
    else:
        print(x**2 + y**2)
