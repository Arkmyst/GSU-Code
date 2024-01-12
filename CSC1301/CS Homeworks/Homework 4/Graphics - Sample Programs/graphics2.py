import turtle

step = 200
decrement = 4
angle1 = 60
angle2 = 120
count = 0

turtle.left(angle1)
while step > 0:
    turtle.forward(step)
    step = step - decrement
    if count % 2 == 0:
        turtle.right(angle2)
    else:
        turtle.right(angle1)
    count = count + 1