from tkinter import *
import random

# Tic-Tac-Toe Window
window = Tk()
window.title("TIC-TAC-TOE Lab Project")

window_width = 750
window_height = 750
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
screen_x = (screen_width / 2) - (window_width / 2)
screen_y = (screen_height / 2) - (window_height / 2)
window.geometry("%dx%d+%d+%d" %
                (window_width, window_height, screen_x, screen_y))
window.resizable(width=False, height=False)

# Function to check if there are spaces within the buttons list
# from the 9 possible spots we iterate and check if they are empty returning True or False
# If we return False - I can end the game and output a Tie Draw
# If we return True - I can continue the game


def blank_spaces():
    blank = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]["text"] != "":
                blank -= 1

    if blank == 0:
        return False
    else:
        return True


# Function to operate the Turns of Players
# For both X and Y we check for a Winner or a Tie
def player_turn(row, column):

    global turn
    global xWins
    global yWins
    global ties

    if buttons[row][column]["text"] == "" and winner_check() is False:

        if turn == players[0]:

            buttons[row][column]["text"] = turn

            if winner_check() is False:
                turn = players[1]
                ongoing.config(text=(players[1] + "'s turn"))

            elif winner_check() is True:
                ongoing.config(text=(players[0] + " wins"))
                xWins += 1

            elif winner_check() == "Tie":
                ongoing.config(text="Tie!")
                ties += 1

        else:

            buttons[row][column]["text"] = turn

            if winner_check() is False:
                turn = players[0]
                ongoing.config(text=(players[0] + "'s turn"))

            elif winner_check() is True:
                ongoing.config(text=(players[1] + " wins"))
                yWins += 1

            elif winner_check() == "Tie":
                ongoing.config(text="Tie Draw!")
                ties += 1


# Function to find the Winner - I took some ideas from Lab 6 and reworked them to check all test cases
# Checks for both X and Y
def winner_check():

    # 3 ways to win Horizontal
    for row in range(3):
        if (
            buttons[row][0]["text"]
            == buttons[row][1]["text"]
            == buttons[row][2]["text"]
            != ""
        ):
            return True

    # 3 ways to win Vertical
    for column in range(3):
        if (
            buttons[0][column]["text"]
            == buttons[1][column]["text"]
            == buttons[2][column]["text"]
            != ""
        ):
            return True

    # 2 ways to win Diagonal
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True

    elif buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True

    # Ways to Tie
    elif blank_spaces() == False:
        return "Tie"

    else:
        return False


# Function to reset the buttons and
# output a random player to go first
def reset_game():
    global turn

    turn = random.choice(players)

    ongoing.config(text=turn + " turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="")


# players
players = ["X", "O"]
turn = random.choice(players)

# Button list For Storing
buttons = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Font 1
Font1 = ("Comic Sans MS", 25, "bold")

# Labels
ongoing = Label(text=turn + "'s turn", font=(Font1))
ongoing.pack(ipadx=15, ipady=15, anchor=CENTER)

# Font 2
Font2 = ("Comic Sans MS", 60, "bold")

# Frame and Grid of Buttons
board = Frame(window, padx=20, pady=20)
board.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(
            board,
            text="",
            font=(Font2),
            width=4,
            height=2,
            highlightbackground="#C1E1C1",
            command=lambda row=row, column=column: player_turn(row, column),
        )
        buttons[row][column].grid(row=row, column=column)

# Lower Frame
Lower = Frame(window)
Lower.pack()

# Reset Button
reset_button = Button(Lower, text="RESTART", font=(Font1), command=reset_game)
reset_button.pack(ipadx=15, ipady=5, anchor=CENTER)

# Win Counter Variables
xWins = 0
yWins = 0
ties = 0

# Font 3
Font3 = ("Comic Sans MS", 20, "bold")

# Label for X wins
tempX = f"X WON: {xWins} Times!"
numberXwins = Label(Lower, text=tempX, font=(Font3))
numberXwins.config(text=tempX)
numberXwins.pack(side=LEFT, padx=5)

# Label for Y wins
tempY = f"Y WON: {yWins} Times!"
numberYwins = Label(Lower, text=tempY, font=(Font3))
numberYwins.pack(side=RIGHT, padx=5)

# Label for Ties
tempY = f"Tie: {ties} Times!"
numberYwins = Label(Lower, text=tempY, font=(Font3))
numberYwins.pack(side=BOTTOM, padx=5)

window.mainloop()
