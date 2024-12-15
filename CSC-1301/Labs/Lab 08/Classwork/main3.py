
''' Read in first equation, ax + by = c '''
a = int(input())
b = int(input())
c = int(input())

''' Read in second equation, dx + ey = f '''
d = int(input())
e = int(input())
f = int(input())

test = False
for x in range(-10, 10):
    for y in range(-10,10):
        if (a*x + b*y - c == 0) and (d*x + e*y - f == 0):
            test = True
            print(f"X is {x} and Y is {y}")
    if test == False :
        print('No solution')