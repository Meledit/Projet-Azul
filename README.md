# Azul
## Introduction
Azul is a Python implementation of the popular board game Azul. This project was developed as part of a student project, in collaboration with one of my classmates. The game utilizes a custom library based on tkinter, created by our professors.

## Rules of Azul
Azul is a strategic tile-placement game where players compete to decorate the walls of the Royal Palace of Evora. The game is played with a set of colorful tiles, each representing a different pattern. The objective is to earn the most points by strategically placing tiles on your personal player board.

## How to Play
To play Azul Project, follow these steps:

* Launch the game by executing the "Fonctions_Actualisation" file in a terminal using the command: python Fonctions_Actualisation.py.
* Click on "Nouvelle Partie" (New Game) to start a new game session.
* Return to the terminal and enter the name of the text file representing the desired game board. For example, to use the default game board, enter "MatriceC.txt".
* During each round, tiles will be randomly placed in the factories and the center of the table.
* On your turn, select tiles from a factory or the center and place them on your personal player board.
* Each round, you must take all the tiles of the same color from a factory or the center and place them in a corresponding pattern line on your board.
* Be careful, once you choose a color from a factory or the center, you cannot place any additional tiles of that color in the same pattern line until the next round.
* Any remaining tiles not chosen are moved to the floor line, which will result in negative points at the end of the round.
* Keep playing, the game ends when one player has completed an entire row.
* At the end of the game, players score points based on completed rows, columns, and sets of colors on their board. The player with the highest score wins!

## Playing Options
Azul offers the following playing options:

* Number of Players: You can play with 2, 3, or 4 players.
* Player vs. AI: You can choose to play against 3 AI opponents.

## Creating Custom Game Boards
To create your own custom game board, you need to adhere to the following rules:

* Only basic colors can be used: Bc for white, R for red, Bl for blue, V for green, and J for yellow.
* Each color can appear only once per row.
* To declare your game board, use the "|" character at the beginning of each row, and "_" after each color. Here's an example: |Bl_J_R_V_Bc_|Bc_Bl_J_R_V_|V_Bc_Bl_J_R_|R_V_Bc_Bl_J_|J_R_V_Bc_Bl_
* Save the game board in a text file with the .txt extension.
* To use your custom game board, enter the file name (including the .txt extension) in the terminal at the beginning of the game.

## AI Gameplay
The AI in Azul Project follows a specific sequence of steps during its turn:

* Step 1: The AI selects the line that requires the most tiles to be filled (5 -> 4 -> 3, and so on).
* Step 2: The AI determines the colors that can be used to fill the chosen line. If the stair line already contains a specific tile color, the AI prioritizes * that color. Otherwise, it creates a list of colors that are not yet filled in that line.
* Step 3: The AI determines the number of tiles it needs to search for, based on the number of empty spaces in the stair line.
* Step 4: The AI scans the factories and the center until it finds a location with the required number of tiles of the correct color.
* Step 5: If the AI finds a suitable location, it plays the tiles. Otherwise, it moves to the next stair line and restarts from Step 2.
* Step 6: If the AI cannot find any line that can be completely filled without placing tiles in the floor, it returns to Step 1, allowing for a margin of * error. The margins of error are examined in the following order: -1 -> -2 -> 1 -> 2 -> -3 -> -4 -> 3 -> 4. A negative number indicates that the AI accepts that number of empty spaces in the stair line. A positive number indicates that the AI accepts that number of tiles ending up in the floor.
* Step 7: If the AI cannot fill any lines, despite the possible margins of error, it searches for the minimum number of tiles that can be placed in the floor by scanning the factories and the center.

Enjoy playing Azul Project and have fun decorating the Royal Palace of Evora!
