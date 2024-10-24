# Project2-TicTacToe
### This is my first Python project! I have spent the last few months, diligently pacing through the Python Essentials 1 course created by Cisco. 

### What does this project entail?
### This project entails me to create a Tic-Tac-Toe game between the program and a user. 
### Some guidelines include:
- The program should play the game using X's
- The user should play the game using O's
- The first move is made by the program (move is an X in the middle of the board)
- Each square is numbered row by row with the first being 1 and the last being 9
- The user makes their move by inputting a square with a valid number (integer between 0 and 10, not already occupied)
- The program checks for a winner with 1 of 4 conclusions selected:
  - The program wins!
  - The user wins!
  - The game is a tie.
  - The game should continue.
- The program responds with its move and the check is repeated.

### Additional requirements:
- The board should be stored as a three-element list, while each element is another three-element list (the inner lists represent rows) so that all of the squares may be accessed using the following syntax:
  
          board[row][column]
- Each of the inner list's elements can contain 'O', 'X', or a digit representing the square's number (that square will be considered free)
- There will be functions pre-defined for you, use them to construct your program

#### ***Note: Use randrange() to draw a random integer number for the program's turn***

        from random import randrange

        for i in range(10):
                print(randrange(8))

			
	
	
