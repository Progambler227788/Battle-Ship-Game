import random #using random library

''' M for missed cell
    H for hit cell
    - for unexplored cell
    P for ships placed cell (occupied by ship) '''
    
def prepare_board(size, ship_sizes): # function to prepare board with size (10) and ship sizes (5,4,3,2,2)

    #using list comprehension to initialize list with - (hypen sign)
    board = [['-' for outer in range(size)] for inner in range(size)]
    #ship_sizes is actually a list holding sizes of list like 
    # There are 5 ships: Carrier (occupies 5 cells), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).

    for ship_size in ship_sizes: # ship_size is variable that will be used in iteration
    #ship_size variable value will be 5 then 4. So, 5,4,3,3,2
        while True: # loop using True in condtion mean it will run till we apply breaking condtion
        
            start_row = random.randint(0, size-1) # starting row
            start_col = random.randint(0, size-1) # starting column
            
            direction = random.choice(['horizontal', 'vertical']) # direction is actually orientation
            
            '''---- is horizontal
               |
               |
               |
               | is vertical'''
               
               
            '''if direction is horizontal, we will use columns. 
        For example, 1,2,3 are in horizontal order. To access 2, we have to move our column by increment of 1.
        Similary, in vertical order. We have to move by rows.
            '''
            
            if direction == 'horizontal' and start_col + ship_size <= size and all(board[start_row][j] == '-' for j in range(start_col, start_col+ship_size)):
                for counter in range(start_col, start_col+ship_size):
                    board[start_row][counter] = 'P' #it will place P in cells that are unexplored or occupied by - sign
                break # break the condition
            elif direction == 'vertical' and start_row + ship_size <= size and all(board[i][start_col] == '-' for i in range(start_row, start_row+ship_size)):
                for counter in range(start_row, start_row+ship_size):
                    board[counter][start_col] = 'P' #it will also place P in cells but it will place vertically
                break
    return board #finally return the updated board 


def player(size, board, hits, misses): #player function is taking size of board,current board, hits and misses as parameters
    while True:
        row = random.randint(0, size-1) # get random row
        column = random.randint(0, size-1) # get random column
        if (row,column) not in hits and (row,column) not in misses: # check if element ar (row,column) is not in hits and misses sets then return it
            return (row,column)
            
def check(board,guess): # function to check whether value to be placed is Miss or Hit 
    if all(cell != 'P' for row in board for cell in row):
        return "win"
    row, column = guess
    
    '''  #Actually, we are accessing index of 2D Board list using columns (column by column)
    That's why column is used first then row. '''
    
    if board[column][row] == '-': # in case of unused cell 
        board[column][row]  = 'M'
        return "miss" 
    elif board[column][row]  =='P': # - placed by M, P placed by H. H for hit and M for miss
        board[column][row]  = 'H'
        return "hit"
        
def play_game(size, ships): # function to start game
    board = prepare_board(size, ships)  # call prepare_board function
    
    #make sets of hits and misses
    hits = set()
    misses = set()
    num_turns = 0 #initialize number of turns of game
    while any('P' in row for row in board):
        num_turns += 1
        guess = player(size, board, hits, misses)
        result = check(board, guess)
        if result == "hit": # add pair in hits set
            hits.add(guess) #actually set will hold pairs. Pairs will be in form of rows,columns returned by player function
        else:
            misses.add(guess) # add pair in misses sets
    return num_turns # return number of turns calculated

def main():
    num_games = 1000  # no of iterations for our game to get average number of turns
    ship_sizes = [5, 4, 3, 3, 2] # ship_sizes will hold list of numbers 
    size = 10 # size of 10 mean our board size 10 by 10 . 10 rows and 10 columns
    total_turns = 0 # total turns taken by game to complete
    print("----Battlship game. Computer will be a Player in this game----")
    for i in range(num_games):
        num_turns = play_game(size, ship_sizes)
        total_turns += num_turns
    #calculated Average number of turns
    print(f"Average number of turns taken in this game: {round(total_turns / num_games)}")

if __name__ == "__main__":
    main() # main function
