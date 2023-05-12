board = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

def print_board(): 
    for row in board:
        print(row[0], row[1], row[2])
        
def checkwin(player):
    if board[0][0] == player and board[0][1] == player and board[0][2] == player:
        return True
    elif board[1][0] == player and board[1][1] == player and board[1][2] == player:
        return True
    elif board[2][0] == player and board[2][1] == player and board [2][2] == player:
        return True
    elif board[0][0] == player and board[1][0] == player and board[2][0] == player:
        return True
    elif board[0][1] == player and board[1][1] == player and board[2][1] == player:
        return True
    elif board[0][2] == player and board[1][2] == player and board[2][2] == player:
        return True
    elif board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    else:
        return False
    
def tic_tac_toe():
    player1 = 'X'
    player2 = 'O'
    current_player = player1
    
    while True:
        print_board()
        
        row = int(input("Enter row number (1-3): ")) - 1
        col = int(input("Enter colum number (1-3): ")) - 1
        
        if board[row][col] != '-':
            print("That cell is already occupied. Try again.")
            continue 
            
        board[row][col] = current_player
        
        if check_win(current_player):
            print_board()
            print(current_player, "wins!")
            break
    
        if all('-' not in row for row in board):
            print_board()
            print("Tie!")
            break
            
        if current_player == player1:
            current_player = player2
        else: 
            current_player = player1
tic_tac_toe()
    