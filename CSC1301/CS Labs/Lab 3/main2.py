import math

X = float(input())
Y = float(input())
Z = float(input())

#Given three floating-point numbers x, y, and z

#output x to the power of z
your_value1 = pow(X,Z)
#x to the power of (y to the power of z)
y = pow(Y,Z)
your_value2 = pow(X,y)
#the absolute value of (x minus y)
your_value3 = abs(X-Y)
#and the square root of (x to the power of z).
your_value4 = math.sqrt(pow(X,Z))


print(f'{your_value1:.2f} {your_value2:.2f} {your_value3:.2f} {your_value4:.2f}')
