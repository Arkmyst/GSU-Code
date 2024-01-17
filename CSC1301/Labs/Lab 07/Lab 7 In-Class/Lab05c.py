"""
Program: CS 1301 Lab 07

Author: Asrar

Description: This program will read a positive integer and
    express it as the sum of powers of 2.
"""


    # Read user's input and store it as an integer in a variable called i_num.

    # Outer loop:
    # while i_num is larger than zero:
        # Initialize n and two_to_n.

        # Do all the stuff you were doing before to find n and two_to_n.
        # Remember that two_to_n is the largest power of 2 less than i_num.

        # print 2**n

def main():

    i_num = int(input("Enter a number: "))
    result = ""

    while i_num > 0:
        
        n = 0
        two_to_n = 2**n
        
        while two_to_n < i_num:
            n += 1
            two_to_n *= 2  
        if two_to_n > i_num:
            n -= 1
            two_to_n /= 2
        if result == "":
            result = (f"2 ** {n}")
        else:
            result = result + " " + "+" + " " + (f"2**{n}")
        i_num = i_num - two_to_n
    print(result)

main()
