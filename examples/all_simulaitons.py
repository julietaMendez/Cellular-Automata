import numpy as np
import matplotlib.pyplot as plt

def get_rule(idx):
    if idx < 256:
        input_patterns = [
            (1,1,1),
            (1,1,0),
            (1,0,1),
            (1,0,0),
            (0,1,1),
            (0,1,0),
            (0,0,1),
            (0,0,0)
        ]
        #outputs = list(map(int,format(idx, "#010b")[2:]))
        # binary = int(format(idx, 'b')) # convert to binary of type int
        binary = format(idx, "0>8b")
        binary = (list(map(int,binary))) #prints as list of int, cannot print list(int) bc int not iterable

        mapping = dict(zip(input_patterns, binary))
        # print(mapping)
        mapping["name"] = "Rule %d" % (idx)
        # print(mapping)
        return mapping
    else:
        raise ValueError("Rule number out of range")

def iterate(board, rule):
    board = np.pad(board, (1, 1), 'constant', constant_values=(0,0))
    # print("board after pad: ", board)
    new_board = np.zeros_like(board)
    # print("new baord: ", new_board)

    # print("rule: ", type(rule), "board: ", type(board))
    

    for i in range(1, board.shape[0] - 1):
        # print("rule", rule)
        new_board[i] = rule[tuple(board[i-1:i+2])]
        # print(tuple(board[i-1:i+2]))
    return new_board[1:-1]

def generate_map(initial_board, rule, num_iterations=100):
    # print(initial_board)

    if isinstance(initial_board, list):
        board = np.array(initial_board)
        # print("is")
    else:
        board = initial_board
        # print("is not")
    
    # print("board before: ",board)
    board = np.pad(board, (num_iterations, num_iterations), 'constant', constant_values=(0,0))
    # print("board after: ", type(board))
    rows = [board]
    # print(rows)
    for i in range(num_iterations):
        # print("board passed in: ", board)
        board = iterate(board, rule)
        rows.append(board)

    rows = np.array(rows)
    return rows

def visualize_board(board, title=None):
    plt.figure(figsize=(5,3), facecolor="pink")
    plt.imshow(board, cmap="Greys")
    plt.axis("off")
    plt.title(title, fontsize=20)
    plt.show()
    # plt.close()

rule = get_rule(30)
board = generate_map([0,1,0], rule, num_iterations=5)
print((board))
visualize_board(board, rule["name"]) 