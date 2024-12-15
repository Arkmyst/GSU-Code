'''
A pedometer treats walking 1 step as walking 2.5 feet. 
Define a function named feet_to_steps that takes a float as a parameter, 
epresenting the number of feet walked, and returns an integer that represents the number of steps walked. 

Then, write a main program that reads the number of feet walked as an input, 
calls function feet_to_steps() with the input as an argument, 
and outputs the number of steps as an integer.
Use floating-point arithmetic to perform the conversion.

'''

feet = float(input("Input: "))

def feet_to_steps(feet):
    return int(feet/2.5)


if __name__ == '__main__':
    print(feet_to_steps(feet))