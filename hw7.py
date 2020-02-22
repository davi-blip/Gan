import random
# Purpose: returns the list of numbers in the collatz sequence from​ n​ to 1, inclusive. 
# Input Parameter(s): ls represents a positive integer
# Return Value(s): This function returns a list 
def collatz(ls):
    if ls == 1:
      return [1]
    
    elif ls % 2 ==0:
        return [ls]+collatz(ls//2)
    else:
        return [ls]+[ls*3+1]+collatz((ls*3+1)//2)



# Purpose: returns the minimum value in that list
# Input Parameter(s):  ​num_list​ contains at least one element
# Return Value(s): returns the minimum value in that list

def find_min(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        x = find_min(num_list[1:])
        minimum = num_list[0]
        if  x < minimum:
            minimum = x
        return minimum


def open_slots(board):
    i = []
    for a in range (len(board)):
        if board[a] == '-':
            i.append(a)
    return i

def row_win(board):
    for row in range (0,len(board),3):
        if board[row] == board[row+1] == board[row+2] and board[row]!='-':
            return board[row]
    return None
    



def diagonals_win(board):
    if (board[0] == board[4] == board[8]) or (board[2] == board[4] == board[6]) and board!= '-':
        return board[4]
    return None

def column_win(board):    
    for column in range (0,3):
        if (board[column] == board[column+3]==board[column+6]) and board[column] !='-':            
            return board[column]
    return None


def game_not_over(board):
    for i in board:
        if i == '-':
            return '-'
    else:
        return 'D'

def winner(board):
    result = row_win(board) or diagonals_win(board) or column_win(board)
    if result:
        return result

    return game_not_over(board)        

# Purpose:  AI will look at every possible sequence of moves and try to find a strategy that forces a win, or at least forces a draw if that’s not possible. 
# Input Parameter(s):  board​ is a list representation of a tic-tac-toe board
# Return Value(s):  return an integer that represents the current state of the board. 

def force_win(board):
    opens = open_slots(board)

    if len(opens) % 2 == 0:
        player_turn = 'O'
    else:
        player_turn = 'X'
    
    if winner(board) == 'X':
        return 1
    elif winner(board) == 'O':
        return -1
    elif winner(board) == 'D':
        return 0

    scores = []
    for i in opens:
        current_board = board[:]
        current_board[i] = player_turn
        scores.append(force_win(current_board))

    if player_turn =='X':
        return max(scores)
    elif player_turn =='O':
        return min(scores)
     



# Purpose: (What does the function do?)takes in no arguments, and simulates a single game of tic-tac-toe in which the computer plays randomly against itself.
# Input Parameter(s): None
# Return Value(s): (What gets returned? Possibilities?) 'X','O' or tie      

def tic_tac_toe():
    board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
    start_player = 'X'
    while winner(board) == '-':
        opens = open_slots(board)
        if start_player == 'X':
            random_next_step = random.choice(open_slots(board))
            board[random_next_step] = start_player
            start_player = 'O'
        else:
            scores = []
            for i in opens:
                current_board = board[:]
                current_board[i] = 'O'
                scores.append(force_win(current_board))

            winning_position = opens[scores.index(min(scores))]
            board[winning_position] = start_player
            start_player = 'X'
    return winner(board)


# Purpose: (What does the function do?)  It then calls ​tic_tac_toe​ n times, and prints out the total number of times X won, the number of times O won, and the number of times that a draw occurred.
# Input Parameter(s): (Each parameter by name and what it represents)number times of playing
# Return Value(s): (What gets returned? Possibilities?) This function does not return anything


def play_games(n):
    X_wins = 0
    O_wins = 0
    draws = 0

    for i in range(n):
        round_winner = tic_tac_toe()
        if round_winner == 'X':
            X_wins += 1
        elif round_winner== 'O':
            O_wins += 1
        elif round_winner == 'D':
            draws += 1

    print('X wins:', X_wins)
    print('O wins:', O_wins)
    print('Draws:', draws)



