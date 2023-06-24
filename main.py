
# variable for "leaderboard"
import os
import math
import sys
import pygame
import numpy as np
player1_wins = 0

player2_wins = 0


def check_score():  # to check who's leading

	if player1_wins > player2_wins:  # checks if player 1 is winning
		print("Player 1 is winning by ["+str(player1_wins - player2_wins) + "]!")

	elif player2_wins > player1_wins:  # checks if player 2 is winning
		print("Player 2 is winning by ["+str(player2_wins - player1_wins) + "]!")

	elif player1_wins == player2_wins:  # if score is the same
		print("Player 1 and Player 2 have the same score!")


def show_score():

	# outputs the score of each player
	print("Player 1: ["+str(player1_wins)+"]")
	print("Player 2: ["+str(player2_wins)+"]")


# Importing numpy for board

# Importing Pygame for Graphics
# Importing sys for exit Pygame

# Importing math for mathematical equations:-

# Importing os:-

# Colors:-
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = "\033[0;32m"
END = '\033[0m'
BOLD = '\033[1m'
ORANGE = "\033[0;33m"


# Creating some global variables
ROW_COUNT = 6
COLUMN_COUNT = 7

# Clear function:-


def clear(): return os.system("clear")


# Win statements:-
player1won = GREEN + BOLD + """
┌─────────────────────────┐
|                         |
|      Player 1 won!      |
|                         |
└─────────────────────────┘
""" + END

player2won = GREEN + BOLD + """
┌─────────────────────────┐
|                         |
|      Player 2 won!      |
|                         |
└─────────────────────────┘
""" + END

# Creating a board


def create_board():
	board = np.zeros((ROW_COUNT, COLUMN_COUNT))
	return board

# Creating a function to drop piece:-


def drop_piece(board, row, column, piece):

	# Filling the board with piece
	board[row][column] = piece

# Creating a function to make sure the location is valid:-


def valid_location(board, column):

	# Checking that the 5th row is not occupied
	return board[ROW_COUNT-1][column] == 0


# Opening a new row
def get_next_open_row(board, column):

	# Checking to see which row the piece will fall
	for r in range(ROW_COUNT):

		# Check the board position:
		if board[r][column] == 0:
			return r


# Creating a funtion to change the orientation
def print_board(board):

	# Flipping the board
	print(np.flip(board, 0))


# To check winning move.
def winning(board, piece):

	# Check Horizontals:-
	for c in range(COLUMN_COUNT-3):
		for r in range(ROW_COUNT):

			if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece:
				return True

	# Check Verticals:-
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT-3):

			if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece:
				return True

	# Check positive sloped diagonals:-
	for c in range(COLUMN_COUNT-3):
		for r in range(ROW_COUNT-3):

			if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece:
				return True

	# Check negativily sloped diagonals:-
	for c in range(COLUMN_COUNT-3):
		for r in range(3, ROW_COUNT):

			if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece:
				return True


# Graphics Board
def draw_board(board):

	# Iterating through every spot:-
	for c in range(COLUMN_COUNT):

		for r in range(ROW_COUNT):

			# Drawing a blue rectange:-
			pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r *
			                 SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))

			# Drawing circles in the color:-
			pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2),
			                   int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)

	# Iterating through every spot:-
	for c in range(COLUMN_COUNT):

		for r in range(ROW_COUNT):

			if board[r][c] == 1:
				pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2),
				                   height - int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)

			elif board[r][c] == 2:
				pygame.draw.circle(screen, YELLOW, (int(
					c*SQUARESIZE+SQUARESIZE/2), height - int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)

	# Update the screen
	pygame.display.update()


# Board
board = create_board()
print_board(board)

# Making Game over False:-
game_over = False

# Turn
turn = 0

# Intializing PyGame:-
pygame.init()

# Screen size
SQUARESIZE = 100
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE

# Radius
RADIUS = int(SQUARESIZE/2 - 5)

# Pygame Screen set:-
screen = pygame.display.set_mode((width, height))


# Update the screen
pygame.display.update()

# Font:-
myfont = pygame.font.SysFont("monospace", 75)

# Main game loop
while not game_over:

	draw_board(board)

	# Events for handling keys
	for event in pygame.event.get():

		# For safely closing window:-
		if event.type == pygame.QUIT:

			sys.exit()

		# Making a event to track mouse:-
		if event.type == pygame.MOUSEMOTION:

			# For clearing out the previous one:-
			pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
			posx = event.pos[0]

			# Drawing some circles based on that:-
			if turn == 0:
				pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)

			else:
				pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)

		# Update the screen
		pygame.display.update()

		# For mouse press down:-
		if event.type == pygame.MOUSEBUTTONDOWN:

			# For clearing the previous screen:
			pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
			#print(event.pos)

			# Ask for Player 1 input:
			if turn == 0:

				# X position:
				posx = event.pos[0]
				column = int(math.floor(posx/SQUARESIZE))

				# Checking for a valid location
				if valid_location(board, column):

					# Getting a new empty row:-
					row = get_next_open_row(board, column)

					# Drop piece:-
					drop_piece(board, row, column, 1)

					# Checking wins for player 1:-
					if winning(board, 1):

						# Printing win
						clear()
						print(player1won)

						player1_wins += 1  # increments player1_wins

						check_score()
						show_score()

						print(ORANGE + BOLD + "\nBy:- ")

						game_over = True

			# Ask for Player 2 input:
			else:

				# X position:
				posx = event.pos[0]
				column = int(math.floor(posx/SQUARESIZE))

				# Checking for a valid location
				if valid_location(board, column):

					# Getting a new empty row:-
					row = get_next_open_row(board, column)

					# Drop piece:-
					drop_piece(board, row, column, 2)

					# Checking wins for player 1:-
					if winning(board, 2):

						# Printing win
						print(player2won)

						player2_wins += 1  # increments player1_wins

						check_score()
						show_score()

						print(ORANGE + BOLD + "By:- ")

						game_over = True

			# Printing the board:-
			print_board(board)
			draw_board(board)

			# Increasing the turn
			turn += 1

			# Alternating from players:-
			turn = turn % 2

			# Waiting before closing:-
			if game_over:
				pygame.time.wait(3000)  # Milliseconds

