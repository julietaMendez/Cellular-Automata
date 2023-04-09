import numpy as np
import matplotlib.pyplot as plt

def apply_rule(rule, iterations):
    if rule > 255 or rule < 0:
        print("No such rule.")
        return

    binary = format(rule, "0>8b") # convert rule to binary
    binary = (list(map(int,binary))) # create list
    patterns = [ # list of tuples
        (1,1,1),
        (1,1,0),
        (1,0,1),
        (1,0,0),
        (0,1,1),
        (0,1,0),
        (0,0,1),
        (0,0,0)
    ]

    pattern_rules_dict = dict(zip(patterns, binary)) # assigns each pattern its respective value (0 or 1)
    row_length = iterations * 2 - 1 
    first_row_start_index = int(row_length / 2)
    initial_board = [0] * row_length
    initial_board[first_row_start_index] = 1

    board.append(initial_board)
    curr_row = initial_board
    curr_row.insert(0, 0)
    curr_row.append(0)

    # repeat for every row
    for i in range(0, iterations-1):
        next_row = [0] * row_length
        next_row_len = len(next_row)
        print("Next row len: ",next_row_len, "curr row len: ", len(curr_row))
        first_row_start_index  -= 1
        value_index = 0
        stop_index = len(curr_row) - 2

        # Get pattern to create next row
        for j in range(0, len(curr_row)):
            if(j < stop_index): # should stop when there are less than 3 values left in the board
                print("j", j)
                pattern_tuple = tuple(curr_row[j:j+3]) # get patterns to create next row
                value = pattern_rules_dict[pattern_tuple]
                next_row[value_index] = value
                
                # FOR DEBUGGING PURPOSES
                # print("value ", value, "value index ", value_index)
                # print("curr row ", curr_row)
                # print("next_row:   ", next_row)
                
                value_index += 1

        board.append(next_row)
        curr_row = next_row
        curr_row.insert(0, 0)
        curr_row.append(0)

    return board

def show_board(board, rule):
    plt.figure(figsize=(5,3), facecolor="pink")
    plt.imshow(board, cmap="Greys")
    plt.axis("off")
    plt.title(rule, fontsize=20)
    plt.show()
    plt.close()

board = []
rule = 30
iterations = 5
board = apply_rule(rule, iterations)
# print(board)
show_board(board, rule) 