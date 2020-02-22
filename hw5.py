import random
# Purpose: (What does the function do?)To see any student that does appear to have all three things must be using dark magic.
# Input Parameter(s): (Each parameter by name and what it represents)where ​grades​ represents students who get good grades, ​
# life​ represents students who have a social life, and ​sleep​ represents students who get enough sleep.
# Return Value(s): (What gets returned? Possibilities?) list of all students who are clearly wizards.

def wizards(grades,life,sleep):
    i = []
    for a in grades:
        for b in life:
            for c in sleep:
                if a == b == c:
                    i.append(a)
    return i
          
print(wizards(['Harry','Hermione'], ['Harry','Ron'], ['Harry','Ron']))
   


# Purpose: (What does the function do?) takes in a board list, and returns a list of the indexes which still contain a '-'. 
# Input Parameter(s): (Each parameter by name and what it represents)board represents elements
# Return Value(s): (What gets returned? Possibilities?)  Indexes here refer to standard list indexing in Python,
# so since board is a 9 element list, they should all be numbers between 0 and 8, inclusive.

def open_slots(board):
    i = []
    for a in range (len(board)):
        if board[a] == '-':
            i.append(a)
    return i

##open_slots(['-', '-', '-', '-', '-', '-', '-', '-', '-'])


# Purpose: (What does the function do?)Define how row wins
# Input Parameter(s): (Each parameter by name and what it represents)represents elements
# Return Value(s): (What gets returned? Possibilities?) 'X','O' wins

def row_win(board):
    for row in range (0,len(board),3):
        if board[row] == board[row+1] == board[row+2] and board[row]!='-':
##            print(board[row])
            return board[row]
    return None
    
##print(row_win(['X', 'X', 'O', 'O', 'X', 'X', 'O', 'X', 'O']))

# Purpose: (What does the function do?)Define how diagonals wins
# Input Parameter(s): (Each parameter by name and what it represents)represents elements
# Return Value(s): (What gets returned? Possibilities?) 'X','O' wins
def diagonals_win(board):
    if (board[0] == board[4] == board[8]) or (board[2] == board[4] == board[6]) and board!= '-':
##        print(board[0])
        return board[4]
    return None
##print(diagonals_win(['X', 'X', 'O', 'O', 'X', 'X', 'O', 'X', 'O']))

# Purpose: (What does the function do?)Define how column wins
# Input Parameter(s): (Each parameter by name and what it represents)represents elements
# Return Value(s): (What gets returned? Possibilities?) 'X','O' wins
def column_win(board):    
    for column in range (0,3):
        if (board[column] == board[column+3]==board[column+6]) and board[column] !='-':            
##            print(board[column])
            return board[column]
    return None
#print(column_win(['X', 'X', 'O', 'O', 'X', 'X', 'O', 'X', 'O']) )
# Purpose: (What does the function do?)Define are there dash left in list or tie
# Input Parameter(s): (Each parameter by name and what it represents)represents elements
# Return Value(s): (What gets returned? Possibilities?) 'X','O' or tie
def game_not_over(board):
    for i in board:
        if i == '-':
            return '-'
    else:
        return 'D'
##print(game_not_over((['X', 'X', 'O', '-', 'X', '-', 'X', 'O', 'O'])))
# Purpose: (What does the function do?)Define who wins
# Input Parameter(s): (Each parameter by name and what it represents)represents elements
# Return Value(s): (What gets returned? Possibilities?) 'X','O' or tie or any space left
def winner(board):
    result = row_win(board) or diagonals_win(board) or column_win(board)
    if result:
        return result

    return game_not_over(board)        

##print(winner((['X', '-', 'O', 'X', 'O', '-', 'O', '-', 'X'])))
        

# Purpose: (What does the function do?)takes in no arguments, and simulates a single game of tic-tac-toe in which the computer plays randomly against itself.
# Input Parameter(s): None
# Return Value(s): (What gets returned? Possibilities?) 'X','O' or tie       
    
def tic_tac_toe():
    board= ['-','-','-','-','-','-','-','-','-']
    start_index = 0
    while winner(board) == '-':        
        a = random.choice(open_slots(board))
        if board[a] == '-':
            if start_index == 0:
                sign = 'X'
                start_index = 1
            else:
                sign = 'O'
                start_index = 0
        board[a]= sign
    return(winner(board))

print(tic_tac_toe())

# Purpose: (What does the function do?)  It then calls ​tic_tac_toe​ n times, and prints out the total number of times X won, the number of times O won, and the number of times that a draw occurred.
# Input Parameter(s): (Each parameter by name and what it represents)number times of playing
# Return Value(s): (What gets returned? Possibilities?) This function does not return anything

def play_games(n):
    a= 0
    b= 0
    c= 0
    for i in range(n+1):
        tic_tac_toe()
        if tic_tac_toe() =='X':
            a +=1
        elif tic_tac_toe() == 'O':
            b +=1
        else:
            c +=1
            
    print('X wins:',a)
    print('O wins:',b)
    print('Draws:',c)

   
print(play_games(100))       
    


            
                
            
                 
  
        
            
        
        
        
