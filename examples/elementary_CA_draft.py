import numpy as np
import matplotlib.pyplot as plt

def apply_rule(rule, iterations):
    if rule > 255 or rule < 0:
        print("No such rule.")
        return

    binary = format(rule, "0>8b") # convert rule to binary
    binary = (list(map(int,binary))) # create list
    print(binary)
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
    board_list = [0,1,0] # initial board
    curr_row = board_list

    # repeat for every row
    for i in range(0, 10): # -------------------------- change to iterations
        curr_row.insert(0, 0)
        curr_row.append(0)
        next_row = [0]

        # Get pattern to create next row
        for i in range(0, len(curr_row)):
            if(i < len(curr_row) - 2): # should stop when there are less than 3 values left in the board
                pattern_tuple = tuple(curr_row[i:i+3]) # get patterns to create next row
                value = pattern_rules_dict[pattern_tuple]
                next_row.append(value)

        next_row.append(0)
        curr_row = next_row
        print("next row: ", next_row)

    return board_list

def visualize_board(board, title=None):
    plt.figure(figsize=(5,3), facecolor="pink")
    plt.imshow(board, cmap="Greys")
    plt.axis("off")
    plt.title(title, fontsize=20)
    plt.show()
    # plt.close()

rule = 30
iterations = 100
board = [[0,1,1], [0,1,0], [0,0,1]]
# board = apply_rule(rule, iterations)
visualize_board(board, rule) 