import PySimpleGUI as psg
import time

def count_head_neighbors(board, col, row):
    num_head_neighbors = 0

    if(col != 0): # ensure there is a col to the left (L)
        if(board[col-1][row] == "purple"):
            print("L")
            num_head_neighbors += 1

    if(col != row_length - 1): # ensure there is a col to the right (R)
        if(board[col+1][row] == "purple"):
            num_head_neighbors += 1 

    # check U, UL, and UR
    if(row != row_length - 1): # ensure there is a row above
        if(board[col][row+1] == "purple"): # (U)
            print("U")
            num_head_neighbors += 1 
        if(col != 0): # ensure there is a col to the left (UL)
            if(board[col-1][row+1] == "purple"):
                num_head_neighbors += 1       
        if(col != row_length - 1): # ensure there is a col to the right (UR)
            if(board[col+1][row+1] == "purple"):
                num_head_neighbors += 1 

    # check D, DL, and DR
    if(row != 0): # ensure there is a row below
        if(board[col][row-1] == "purple"): # (D)
            num_head_neighbors += 1 
        if(col != 0): # ensure there is a col to the left (DL)
            if(board[col-1][row-1] == "purple"):
                num_head_neighbors += 1 
        if(col != row_length - 1): # ensure there is a col to the right (DR)
            if(board[col+1][row-1] == "purple"):
                num_head_neighbors += 1 

    return num_head_neighbors

def run(current_board):
    new_board = init_cells() # creates board for next iteration
    x = 500
    BOX_SIZE = 15 #length is 33

    # time.sleep(3) # doesn't work as intended yet
    graph = psg.Graph((x, x), (0, 0), (x, x), background_color='white', enable_events=True, key='-GRAPH-', visible=True)                  
    layout = [[graph], [psg.Button('Run', button_color="green", key='-DONE-'), 
                        psg.Button('Head', button_color="purple"), psg.Button('Tail', button_color="black"), 
                        psg.Button('Connector',button_color="orange"), psg.Button('Empty',button_color="white")]]
    window = psg.Window('Wire World by Julieta Mendez', layout, finalize=True)

    # update board with new cells
    for col in range(0,row_length):
        for row in range(0, row_length):

            if(current_board[col][row] == "purple"):
                # print("1")
                graph.draw_rectangle((row * BOX_SIZE, col * BOX_SIZE), # top left, bottom right
                    (row * BOX_SIZE + BOX_SIZE, col * (BOX_SIZE) + BOX_SIZE), line_color='white', fill_color="black")
                new_board[col][row] = "black"

            if(current_board[col][row] == "black"):
                # print("2")
                graph.draw_rectangle((row * BOX_SIZE, col * BOX_SIZE), # top left, bottom right
                    (row * BOX_SIZE + BOX_SIZE, col * (BOX_SIZE) + BOX_SIZE), line_color='white', fill_color="orange")
                new_board[col][row] = "orange"

            if(current_board[col][row] == "orange"):
                # print("3")
                num_head_neighbors = count_head_neighbors(current_board, col, row)
                print("nieghbors", num_head_neighbors)
                if(num_head_neighbors == 1 or num_head_neighbors == 2):
                    print("purple")
                    graph.draw_rectangle((row * BOX_SIZE, col * BOX_SIZE), # top left, bottom right
                    (row * BOX_SIZE + BOX_SIZE, col * (BOX_SIZE) + BOX_SIZE), line_color='white', fill_color="purple")
                    new_board[col][row] = "purple"
                else:
                    graph.draw_rectangle((row * BOX_SIZE, col * BOX_SIZE), # top left, bottom right
                    (row * BOX_SIZE + BOX_SIZE, col * (BOX_SIZE) + BOX_SIZE), line_color='white', fill_color="orange")
                    new_board[col][row] = "orange"
    
    return new_board

def create_init_board(board): # user places cells
    x = 500
    BOX_SIZE = 15 #length is 33
    color = "black"

    graph = psg.Graph((x, x), (0, 0), (x, x), background_color='white', enable_events=True, key='-GRAPH-', visible=True)                  
    layout = [[graph], [psg.Button('Run', button_color="green"), 
                        psg.Button('Head', button_color="purple"), psg.Button('Tail', button_color="black"), 
                        psg.Button('Connector',button_color="orange"), psg.Button('Empty',button_color="white")]]
    window = psg.Window('Wire World by Julieta Mendez', layout)

    color = "black"

    while True:
        event, values = window.read()
        if event == psg.WIN_CLOSED:
            break

        mouse = values['-GRAPH-'] # gets coords of plot point
        row = mouse[0] // BOX_SIZE # gets x coord
        col = mouse[1] // BOX_SIZE # gets y coord

        # initally, user draws
        if event == '-GRAPH-':
            graph.draw_rectangle((row * BOX_SIZE, col * BOX_SIZE),
                (row * BOX_SIZE + BOX_SIZE, col * (BOX_SIZE) + BOX_SIZE), line_color='white', fill_color=color)          
            board[col][row] = color

        if event == 'Empty': 
            color = "white"
        if event == 'Head': 
            color = "purple"
        if event == 'Tail': 
            color = "black"
        if event == 'Connector':
            color = "orange"
        if event == "Run":
            for i in range(0,iterations):
                board = run(board) # returns new board

    window.close()

def init_cells():
    board = []
    for i in range(0, row_length):
        next_row = ["Empty"] * row_length # set all cells as empty initially
        board.append(next_row)
    return board

iterations = 5
row_length = 34 #if size is 15
initial_board = init_cells() # initiate cells as Empty
create_init_board(initial_board) # player sets cells