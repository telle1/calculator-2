"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

def calculator():
# Replace this with your code
# #repeat forever:
    while True:
#     read input (e.g. + 1 2)
        nums_input = input("Enter your equation: ")
# tokenize input
        tokens = nums_input.split(' ')
#         if the first token is "q":
        if tokens[0] == "q":
            #quit
            break
        elif tokens[0] == "+":
            print(add(int(tokens[1]), int(tokens[2])))
        elif tokens[0] == "-":
            print(subtract(int(tokens[1]), int(tokens[2])))
        elif tokens[0] == "*":
            print(multiply(int(tokens[1]), int(tokens[2])))
        elif tokens[0] == "/":
            print(divide(int(tokens[1]), int(tokens[2])))
        elif tokens[0] == "square":
            print(square(int(tokens[1])))
        elif tokens[0] == "cube":
            print(cube(int(tokens[1])))
        elif tokens[0] == "pow":
            print(power(int(tokens[1]), int(tokens[2])))

calculator()