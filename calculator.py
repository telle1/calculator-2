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
        print(tokens)
#         if the first token is "q":
        if tokens[0] == "q":
            break
#             quit
calculator()

#         else:
#             (decide which math function to call based on first token)
#             if the first token is 'pow':
#                   call the power function with the other two tokens

#             (...etc.)
