import numpy as np
import matplotlib.pyplot as plt

def apply_rule(rule, iterations):
    if rule > 255 or rule < 0:
        print("No such rule.")
        return

    binary = format(rule, "0>8b") # convert rule to binary
    binary = (list(map(int,binary))) # convert binary num to list of int

    patterns = [ # list of patterns as tuples
        (1,1,1),
        (1,1,0),
        (1,0,1),
        (1,0,0),
        (0,1,1),
        (0,1,0),
        (0,0,1),
        (0,0,0)
    ]
    pattern_rules_dict = dict(zip(patterns, binary)) # assigns each pattern its respective value from the binary num

    row_length = iterations * 2 - 1 
    first_row_start_index = int(row_length / 2 + 1) # index of the first block
    initial_row = [0] * (row_length + 2) # board consists of 0s initially, need 2 extra 0s to determine next row
    initial_row[first_row_start_index] = 1 # set first block

    board = [] # create matrix
    board.append(initial_row) 
    
    curr_row = initial_row
    for i in range(0, iterations-1): 
        next_row = [0] * row_length # create next row with initially all 0s
        stop_index = len(curr_row) - 2

        # Get pattern to create next row
        for j in range(0, len(curr_row)):
            if(j < stop_index): # should stop when there are less than 3 values left in the board
                pattern_tuple = tuple(curr_row[j:j+3]) # get patterns to create next row
                value = pattern_rules_dict[pattern_tuple]
                next_row[j] = value

        board.append(next_row)
        curr_row = next_row
        curr_row.insert(0, 0)
        curr_row.append(0)

    return board

def show_board(board, rule):
    plt.figure(figsize=(10,5), facecolor="pink")
    plt.imshow(board, cmap="Greys")
    plt.axis("off")
    plt.title(rule, fontsize=20)
    plt.show()
    plt.close()

def run_all_rules(iterations):
    for i in range(0, 256):
        board = apply_rule(i, iterations)
        show_board(board, i) 

rule = 30
iterations = 500
show_board(apply_rule(rule, iterations), rule)
# run_all_rules(iterations)

