#   Author: Arkmyst
#   Email: asyed23@student.gsu.edu
#   CSC 1301 – Section: 002
#   Python Lab 10

''' 
Purpose:
    Create a Rock Paper Scissor Game with While and if statements
Pre-conditions:
    Initalize choices and get user and computer choices
Post-conditions:
    Output result with if statements, also make it so the while loop is continous
'''
import random

def main():
    print("\nThe Rock Paper Scissors Game\n")
    print("""Game Elements: 

    Enter 1 for ROCK
    Enter 2 for PAPER
    Enter 3 for SCISSOR

    Enter -1 to quit game
    """)

    rock = 1 # Initializing rock
    paper = 2 # Initializing paper
    scissor = 3 # Initializing scissor
    user_choice = 0 # Initializing User Choice
    cpu_choice = 0 # Initializing Computer Choice

    user_choice = int(input("Enter your Choice: ")) # Getting User Choice
    print()
    cpu_choice = random.randint(1,3) # Getting a random Computer Choice

    while user_choice != -1 and user_choice <= 3: # While loop to run if user is not quitting or a number greater than 3

        if user_choice == rock: # Getting all potential User Choices
            print("\tYou chose ROCK\n")
        elif user_choice == paper:
            print("\tYou chose PAPER\n")
        elif user_choice == scissor:
            print("\tYou chose SCISSOR\n")

        if cpu_choice == rock: # Getting all potential Computer Choices
            print("\tThe computer chose ROCK\n")
        elif cpu_choice == paper:
            print("\tThe computer chose PAPER\n")
        elif cpu_choice == scissor:
            print("\tThe computer chose SCISSOR\n")

         # Testing Winner when Rock Beats Scissor
        if user_choice == rock and cpu_choice == scissor:
            print("Congratulations you win!")
        elif user_choice == scissor and cpu_choice == rock:
            print("Sorry you Lose!")

         # Testing Winner when Paper Beats Rock
        if user_choice == paper and cpu_choice == rock:
            print("Congratulations you win!")
        elif user_choice == rock and cpu_choice == paper:
            print("Sorry you Lose!")

         # Testing Winner when Scissor Beats Paper
        if user_choice == scissor and cpu_choice == paper:
            print("Congratulations you win!")
        elif user_choice == paper and cpu_choice == scissor:
            print("Sorry you Lose!")

        # All potential Tie Cases
        if user_choice == cpu_choice:
            print("You have tied with Computer")

        user_choice = int(input("\nEnter your Choice: ")) # Gets another User Choice 
        cpu_choice = random.randint(1,3) # Gets another Computer Choice 

    print("\n\tGoodbye") # If User quits then while loops ends and prints this

main() # Calls main
