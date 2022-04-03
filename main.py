# IMPORTING LIBRARIES
import prettytable
import os
import sys
import time

# VARIABLES
data_cols = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]

coor_to_num = {
    "a": "0",
    "b": "1",
    "c": "2"
}

user_symbol = "0"
game_over = False

# FUNCTIONS


def draw_grid(data):
    if sys.platform.startswith("linux"):
        os.system("clear")
    elif sys.platform.startswith("win32"):
        os.system("cls")
    else:
        print("Can not detect OS. Tables can not be deleted!")

    table = prettytable.PrettyTable()

    table.add_column("", [num for num in range(0, len(data))])
    table.add_column("A", [d for d in data[0]])
    table.add_column("B", [d for d in data[1]])
    table.add_column("C", [d for d in data[2]])

    print(table)


def get_user_input():
    user_i = input("Enter Input: ")

    if not user_i or len(user_i) > 2 or len(user_i) <= 1:
        print("Please enter a valid input.")
        get_user_input()
    else:
        try:
            split_input = [i for i in user_i]
            split_input[1] = coor_to_num[split_input[1].lower()]
        except KeyError:
            print("Enter valid coordinates!")
            get_user_input()
        else:
            return split_input



# CODE && LOGIC && FRONT-END
print("Tic Tac Toe")
print("Answer format: [Row][Column] => 1C")
print(f"You are {user_symbol}.")

# Adding a delay so that the user can see the text
time.sleep(4)

while not game_over:
    draw_grid(data_cols)

    user_input = get_user_input()

    if user_input:
        data_to_change = data_cols[int(user_input[1])][int(user_input[0])]

        if data_to_change == "":
            data_to_change = user_symbol
        else:
            print("You can't change this cell!")
            time.sleep(2)