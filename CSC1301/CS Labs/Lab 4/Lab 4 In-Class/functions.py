# A simple Python functions
import random

def printHello():
    print("Hello World")


def HiFive():
    Amt = random.randint(1,100)
    print("HiFive!")
    return Amt

def printGoodbye():
    print("Goodbye")


def main():
    print("Calling PrintHello")
    printHello()
    print("Calling HiFive")
    variable = HiFive()
    print("Result of HiFive: ", variable)
    print("Calling Goodbye")
    printGoodbye()
main()