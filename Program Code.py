from random import randrange

def display_board(board):
    """Displays the current state of the board."""
    print("+-------" * 3,"+", sep="")
	  for row in range(3):
		      print("|       " * 3,"|", sep="")
		for col in range(3):
			    print("|   " + str(board[row][col]) + "   ", end="")
		print("|")
		print("|       " * 3,"|",sep="")
		print("+-------" * 3,"+",sep="")

def enter_move(board):
    """Prompts the user to enter a move and updates the board."""
    while True:
        move = input("Enter your move (1-9): ")
        if move.isdigit() and '1' <= move <= '9':
            move = int(move) - 1
            row, col = divmod(move, 3)
            if board[row][col] not in ['O', 'X']:
                board[row][col] = 'O'
                break
            else:
                print("Field already occupied - repeat your input!")
        else:
            print("Bad move - repeat your input!")

def make_list_of_free_fields(board):
    """Returns a list of all unoccupied cells."""
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] not in ['O', 'X']]

def victory_for(board, sgn):
    """Checks if the given sign ('X' or 'O') has won the game."""
    win_conditions = [
        [(0, 0), (0, 1), (0, 2)], # rows
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)], # columns
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)], # diagonals
        [(0, 2), (1, 1), (2, 0)]
    ]
    for condition in win_conditions:
        if all(board[row][col] == sgn for row, col in condition):
            return 'you' if sgn == 'O' else 'me'
    return None

def draw_move(board):
    """Draws the computer's move ('X') randomly on the board."""
    free = make_list_of_free_fields(board)
    if free:
        row, col = free[randrange(len(free))]
        board[row][col] = 'X'

# Initialize the board
board = [[3 * j + i + 1 for i in range(3)] for j in range(3)]
board[1][1] = 'X' # Computer starts with an 'X' in the center

# Main game loop
human_turn = True
while make_list_of_free_fields(board):
    display_board(board)
    if human_turn:
        enter_move(board)
        winner = victory_for(board, 'O')
    else:
        draw_move(board)
        winner = victory_for(board, 'X')
    if winner:
        break
    human_turn = not human_turn

# Display the final board and outcome
display_board(board)
if winner == 'you':
    print("You won!")
elif winner == 'me':
    print("I won!")
else:
    print("It's a tie!")
