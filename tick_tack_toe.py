board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_"]
current_player = "X"
winner = None
game_running = True

# printing the game board
def print_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("__________")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("__________")
    print(board[6] + " | " + board[7] + " | " + board[8])

# Take player input (If player input is not an int the program shuts down)
def player_input(board):
    inp = int(input("Enter a number 1-9: "))
    if 1 <= inp <= 9 and board[inp - 1] == "_":
        board[inp-1] = current_player
    else:
        print("Player is already in that spot/Invalid number")

# Check for win or tie
def check_horizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "_":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "_":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "_":
        winner = board[6]
        return True

def check_vertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "_":
        winner = board[0]
        return True
    elif board[1] == board[4] == board [7] and board[1] != "_":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "_":
        winner = board[1]
        return True

def check_diagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "_":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "_":
        winner = board[2]
        return True

# Switch the player
def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

# Check for win or tie
def check_win():
    global game_running
    if check_diagonal(board) or check_horizontal(board) or check_vertical(board):
        print(f"The winner is {winner}!")
        game_running = False

def check_tie(board):
    global game_running
    if "_" not in board:
        print_board(board)
        print("It's a TIE!")
        game_running = False



while game_running:
    print_board(board)
    player_input(board)
    check_win()
    check_tie(board)
    switch_player()

