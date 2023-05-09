import PySimpleGUI as psg

def count_head_neighbors(board, col, row):
    num_head_neighbors = 0

    if(col != 0): # ensure there is a col to the left (L)
        if(board[col-1][row] == "purple"):
            num_head_neighbors += 1

    if(col != row_length - 1): # ensure there is a col to the right (R)
        if(board[col+1][row] == "purple"):
            num_head_neighbors += 1 

    # check U, UL, and UR
    if(row != row_length - 1): # ensure there is a row above
        if(board[col][row+1] == "purple"): # (U)
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

def run(current_board, graph):
    new_board = init_cells() # creates board for next iteration
    x = 500
    BOX_SIZE = 15

    # update board with new cells
    for col in range(0,row_length):
        for row in range(0, row_length):

            if(current_board[col][row] == "purple"):
                graph.draw_rectangle((row * BOX_SIZE, col * BOX_SIZE), # top left, bottom right
                    (row * BOX_SIZE + BOX_SIZE, col * (BOX_SIZE) + BOX_SIZE), line_color='white', fill_color="black")
                new_board[col][row] = "black"

            if(current_board[col][row] == "black"):
                graph.draw_rectangle((row * BOX_SIZE, col * BOX_SIZE), # top left, bottom right
                    (row * BOX_SIZE + BOX_SIZE, col * (BOX_SIZE) + BOX_SIZE), line_color='white', fill_color="orange")
                new_board[col][row] = "orange"

            if(current_board[col][row] == "orange"):
                num_head_neighbors = count_head_neighbors(current_board, col, row)
                if(num_head_neighbors == 1 or num_head_neighbors == 2):
                    graph.draw_rectangle((row * BOX_SIZE, col * BOX_SIZE), # top left, bottom right
                    (row * BOX_SIZE + BOX_SIZE, col * (BOX_SIZE) + BOX_SIZE), line_color='white', fill_color="purple")
                    new_board[col][row] = "purple"
                else:
                    graph.draw_rectangle((row * BOX_SIZE, col * BOX_SIZE), # top left, bottom right
                    (row * BOX_SIZE + BOX_SIZE, col * (BOX_SIZE) + BOX_SIZE), line_color='white', fill_color="orange")
                    new_board[col][row] = "orange"
    
    return new_board, graph

def init_cells():
    board = []
    for i in range(0, row_length):
        next_row = ["Empty"] * row_length # set all cells as empty initially
        board.append(next_row)
    return board

def create_init_board(): # user places cells
    board = init_cells() # initiate cells as Empty
    x = 500
    BOX_SIZE = 15
    color = "white" # default color is white
    graph = psg.Graph((x, x), (0, 0), (x, x), background_color='white', enable_events=True, key='-GRAPH-', visible=True)                  
    layout = [[graph], [psg.Button('Run', button_color="green"), 
                        psg.Button('Head', button_color="purple"), psg.Button('Tail', button_color="black"), 
                        psg.Button('Conductor',button_color="orange"), psg.Button('Empty',button_color="white")]]
    window = psg.Window('Wire World by Julieta Mendez', layout)

    while True:
        event, values = window.read()
        
        # user can place cells
        if event == '-GRAPH-':
            mouse = values['-GRAPH-'] # gets coords of plot point
            row = mouse[0] // BOX_SIZE # gets x coord
            col = mouse[1] // BOX_SIZE # gets y coord
            graph.draw_rectangle((row * BOX_SIZE, col * BOX_SIZE),
                (row * BOX_SIZE + BOX_SIZE, col * (BOX_SIZE) + BOX_SIZE), line_color='white', fill_color=color)          
            board[col][row] = color # save color in board for next iteration
        
        # user can change the color of the cells
        if event == 'Empty': 
            color = "white"
        if event == 'Head':      
            color = "purple"
        if event == 'Tail': 
            color = "black"
        if event == 'Conductor':
            color = "orange"
        
        # user can run or exit
        if event == "Run":
            board, graph = run(board, graph)

        if event == psg.WIN_CLOSED:
            break

    window.close()

iterations = 2
row_length = 34 # according to the size of the graph & cells
create_init_board() # player sets cells

# Instructions:
# Just run the program. Select any color and click on the white board to set cells. Run.