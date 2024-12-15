"""
Program: CS 1301 Lab 07

Author: Asrar Syed

Description: This program will read a positive integer and
    find the largest power of two that is less than or equal to it.
"""

# TODO: Complete this code

# Read user's input and store it as an integer in a variable called i_num.

# Initialize a variable n to serve as the exponent.
# Initialize a variable two_to_n to hold the value of 2**n

# complete the while-loop
# while two_to_n is less than i_num:
# add 1 to n
# multiply two_to_n by 2

# if two_to_n is greater than i_num:
# subtract 1 from
# divide two_to_n by 2

# Print the result


def main():

    i_num = int(input("Enter a number: "))

    n = 0

    two_to_n = 2**n

    while two_to_n < i_num:
        n += 1
        two_to_n *= 2

    if two_to_n > i_num:
        n -= 1
        two_to_n /= 2

    # Print the result
    print(f"2 ** {n}")


main()
