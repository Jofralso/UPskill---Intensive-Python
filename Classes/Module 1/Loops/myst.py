board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
player = 'X'

while True:
    print("Player", player, "turn.")
    row = int(input("Enter the row (1-3): "))
    col = int(input("Enter the column (1-3): "))
    
    if board[row-1][col-1] != '-':
        print("That position is already taken. Try again.")
        continue
        
    board[row-1][col-1] = player
    print(board[0])
    print(board[1])
    print(board[2])
    
    if board[0][0] == player and board[0][1] == player and board[0][2] == player:
        print("Player", player, "wins!")
        break
    elif board[1][0] == player and board[1][1] == player and board[1][2] == player:
        print("Player", player, "wins!")
        break
    elif board[2][0] == player and board[2][1] == player and board[2][2] == player:
        print("Player", player, "wins!")
        break
    elif board[0][0] == player and board[1][0] == player and board[2][0] == player:
        print("Player", player, "wins!")
        break
    elif board[0][1] == player and board[1][1] == player and board[2][1] == player:
        print("Player", player, "wins!")
        break
    elif board[0][2] == player and board[1][2] == player and board[2][2] == player:
        print("Player", player, "wins!")
        break
    elif board[0][0] == player and board[1][1] == player and board[2][2] == player:
        print("Player", player, "wins!")
        break
    elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
        print("Player", player, "wins!")
        break
    
    player = 'O' if player == 'X' else 'X'
