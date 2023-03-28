# Battle-Ship-Game
This is a Python implementation of the Battleship game where the computer plays against itself. The game board is a 10x10 2D list, and five ships are randomly placed on it at the start of the game.
Battleship Game
This program simulates a game of Battleship, where the computer plays against itself. The objective of the game is to sink all of the opponent's ships by guessing their locations on a grid. The computer randomly places its ships on the grid, and then takes turns making guesses until all ships have been sunk.

Usage
To run the program, simply execute the main() function in the battleship.py script.
The program will play 1000 games of Battleship and output the average number of turns it took to win.
Battleship Game
This program simulates a game of Battleship, where the computer plays against itself. The objective of the game is to sink all of the opponent's ships by guessing their locations on a grid. The computer randomly places its ships on the grid, and then takes turns making guesses until all ships have been sunk.

Usage
To run the program, simply execute the main() function in the battleship.py script. 
The program will play 1000 games of Battleship and output the average number of turns it took to win.

Implementation Details
The game is implemented using Python 3, and uses a 2D list to represent the game board. The prepare_board() function randomly places the computer's ships on the board, while the player() function selects a random location to guess. The check() function determines whether a guess is a hit or a miss, and updates the board accordingly. The play_game() function orchestrates the gameplay by repeatedly calling player() and check() until all ships have been sunk. Finally, the main() function runs 1000 games of Battleship and calculates the average number of turns it took to win.

Future Work
Possible improvements to this program include:

Adding a graphical user interface to make the game more interactive.
Implementing a two-player version of the game, where players take turns guessing each other's ship locations.
Allowing the user to specify the size of the game board and the number of ships, instead of using fixed values.
Adding more intelligence to the computer's guessing strategy, to make it more challenging for human players.
