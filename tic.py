#  game board
def display_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])
#  if a player has won
def check_win(board, mark):
    # Check rows
    for i in range(1, 8, 3):
        if board[i] == board[i+1] == board[i+2] == mark:
            return True

    # Check columns
    for i in range(1, 4):
        if board[i] == board[i+3] == board[i+6] == mark:
            return True

    # Check diagonals
    if board[1] == board[5] == board[9] == mark or board[3] == board[5] == board[7] == mark:
        return True

    return False
#if board is full
def check_full(board):
    for i in range(1, 10):
        if board[i] == ' ':
            return False
    return True
#play the game
def play_game():
    board = [' '] * 10 
    current_player='X'

    while True:
        #  board
        display_board(board)

        #   Cureent player's move
        position = int(input("Enter the position (1-9): "))
        if board[position] != ' ':
            print("Invalid move. Try again.")
            continue

        # Update the board
        board[position] = current_player

      #if the current player wins
        if check_win(board, current_player):
            display_board(board)
            print("Player", current_player, "wins!")
            break

        #is the board is full(tie)
        if check_full(board):
            display_board(board)
            print("It's a tie!")
            break
        #switch to other player
        current_player = 'O' if current_player == 'X' else 'X'


play_game()




