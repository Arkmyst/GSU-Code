'''
Program: CS 1301 Lab 07

Author: Asrar Syed

Description: This program will ask the user for a value
and tell the user whether the value is even or odd.
'''
def main(number):

        if number % 2 == 0:
            print(number // 2, 'is even.')
            return number // 2

        elif number % 2 == 1:
            result = 3 * number + 1
            print(result, 'is odd.')
            return result

N = int(input('Enter a number: '))
while N != 1:
    N = main(int(N))


