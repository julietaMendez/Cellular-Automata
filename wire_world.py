import PySimpleGUI as psg

''' 
graph=psg.Graph(canvas_size=(700,300), graph_bottom_left=(0, 0), graph_top_Head=(700,300),
    background_color='red', enable_events=True, drag_submits=True, key='graph')
layout = [[graph], [psg.Button('LEFT'), psg.Button('Head'), psg.Button('UP'), psg.Button('DOWN')]]

window = psg.Window('Graph test', layout, finalize=True)
x1,y1 = 350,150
circle = graph.draw_circle((x1,y1), 10, fill_color='black', line_color='white')
rectangle = graph.draw_rectangle((50,50), (650,250), line_color='purple')
while True:
   event, values = window.read()
   if event == psg.WIN_CLOSED:
      break
   if event == 'Head':
      graph.MoveFigure(circle, 10, 0)
   if event == 'LEFT':
      graph.MoveFigure(circle, -10,0)
   if event == 'UP':
      graph.MoveFigure(circle, 0, 10)
   if event == 'DOWN':
      graph.MoveFigure(circle, 0,-10)
   if event=="graph+UP":
      x2,y2= values['graph']
      graph.MoveFigure(circle, x2-x1, y2-y1)
      x1,y1=x2,y2
window.close()
'''

def count_head_neighbors(board, col, row):
    num_head_neighbors = 0

    if(col != 0): # ensure there is a col to the left (L)
        if(board[col-1][row] == "Head"):
            num_head_neighbors += 1

    if(col != row_length - 1): # ensure there is a col to the right (R)
        if(board[col+1][row] == "Head"):
            num_head_neighbors += 1 

    # check U, UL, and UR
    if(row != row_length - 1): # ensure there is a row above
        if(board[col][row+1] == "Head"): # (U)
            num_head_neighbors += 1 
        if(col != 0): # ensure there is a col to the left (UL)
            if(board[col-1][row+1] == "Head"):
                num_head_neighbors += 1       
        if(col != row_length - 1): # ensure there is a col to the right (UR)
            if(board[col+1][row+1] == "Head"):
                num_head_neighbors += 1 

    # check D, DL, and DR
    if(row != 0): # ensure there is a row below
        if(board[col][row-1] == "Head"): # (D)
            num_head_neighbors += 1 
        if(col != 0): # ensure there is a col to the left (DL)
            if(board[col-1][row-1] == "Head"):
                num_head_neighbors += 1 
        if(col != row_length - 1): # ensure there is a col to the right (DR)
            if(board[col+1][row-1] == "Head"):
                num_head_neighbors += 1 

    return num_head_neighbors

def run(current_board):
    iterations = 10
    new_board = init_cells(current_board) # creates board for next iteration
    x = 500
    BOX_SIZE = 15 #length is 33

    graph = psg.Graph((x, x), (0, 0), (x, x), background_color='white', enable_events=True, key='-GRAPH-', visible=True)                  
    layout = [[graph], [psg.Button('Run', button_color="green", key='-DONE-'), 
                        psg.Button('Head', button_color="purple"), psg.Button('Tail', button_color="black"), 
                        psg.Button('Connector',button_color="orange"), psg.Button('Empty',button_color="white")]]
    window = psg.Window('Wire World by Julieta Mendez', layout, finalize=True)

    for i in range(0,iterations):
        # update board with new cells
        for col in range(0,row_length):
            for row in range(0, row_length):

                if(current_board[col][row] == "purple"):
                    graph.draw_rectangle((row * BOX_SIZE, col * BOX_SIZE), # top left, bottom right
                        (row * BOX_SIZE + BOX_SIZE, col * (BOX_SIZE) + BOX_SIZE), line_color='white', fill_color="black")
                    new_board[col][row] = "Tail"

                if(current_board[col][row] == "black"):
                    graph.draw_rectangle((row * BOX_SIZE, col * BOX_SIZE), # top left, bottom right
                        (row * BOX_SIZE + BOX_SIZE, col * (BOX_SIZE) + BOX_SIZE), line_color='white', fill_color="orange")
                    new_board[col][row] = "Connector"

                if(current_board[col][row] == "orange"):
                    num_head_neighbors = count_head_neighbors(current_board, col, row)
                    if(num_head_neighbors == 1 or num_head_neighbors == 2):
                        graph.draw_rectangle((row * BOX_SIZE, col * BOX_SIZE), # top left, bottom right
                        (row * BOX_SIZE + BOX_SIZE, col * (BOX_SIZE) + BOX_SIZE), line_color='white', fill_color="purple")
                        new_board[col][row] = "Head"
                    else:
                        graph.draw_rectangle((row * BOX_SIZE, col * BOX_SIZE), # top left, bottom right
                        (row * BOX_SIZE + BOX_SIZE, col * (BOX_SIZE) + BOX_SIZE), line_color='white', fill_color="orange")
                        new_board[col][row] = "Connector"

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
            print(board)
            # ------- print for DEBUGGING PURPOSES -------------------------
            # for i in range(0, row_length):
            #     print(i, col, ": ", board[i][row]) #prints row -----------

        if event == 'Empty': 
            color = "white"
        if event == 'Head': 
            color = "purple"
        if event == 'Tail': 
            color = "black"
        if event == 'Connector':
            color = "orange"
            print("fucing orange")
        if event == "Run":
            print("wtf")
            run(board) 

    window.close()

def init_cells(board):
    for i in range(0, row_length):
        next_row = ["Empty"] * row_length # set all cells as empty initially
        board.append(next_row)
    return board


row_length = 34 #if size is 15
initial_board = []
initial_board = init_cells(initial_board) # initiate cells as Empty

create_init_board(initial_board) # player sets cells
# run(initial_board)
