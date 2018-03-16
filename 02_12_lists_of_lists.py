#!/usr/bin/env python
# Example 2-12 A list with three lists of length 3 can represent a tic-tac-toe board

# Create a list of three lists of three items each. Inspect the structure
board = [['_'] * 3 for i in range(3)]

board
# Out[2]: [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

# Place a mark in row 1, column 2 and check the result
board[2][0] = 'X'
# Out[2]: [['_', '_', '_'], ['_', '_', '_'], ['X', '_', '_']]


# Example 2-13 A list with three references to the same list is useless
weird_board = [['_'] * 3] * 3

weird_board
# Out[6]: [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

# Placing a mark in row 1, column 2 reveals that all rows are aliases
#   referring to the same object
weird_board[1][2] = '0'

weird_board
# Out[8]: [['_', '_', '0'], ['_', '_', '0'], ['_', '_', '0']]



# Each iteration builds a new row and appends it to board
