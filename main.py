import sys
import numpy as np 
import random
from random import choice
import time

import TicTacToe

sys.dont_write_bytecode = True

COMP = +1 
HUMAN = -1
def run_code(tic_tac_toe, test_case, grid_size, player_1=None, player_2=None):

	# Loops until there are empty spaces available on the grid for more inputs
	player_1_val = +1
	player_2_val = -1
	itr = 0
	while len(tic_tac_toe.emptyGrid()) > 0 and not tic_tac_toe.isGameOver():

		# Get user input 1: "X"
		success = False
		while not success and len(tic_tac_toe.emptyGrid()):
			try:
				# use user inputs
				tic_tac_toe.clean()
				
				tic_tac_toe.initialGridDisplay()
				tic_tac_toe.printGrid(player_1, player_2)
				user_input_x = int(input("\nX: Choose between 0-{}: ".format(grid_size*grid_size)))

			except Exception as e:
				# the input is invalid
				print("Invalid input. Please try again.")
				continue
			j = user_input_x % grid_size
			i = user_input_x // grid_size
			success = tic_tac_toe.updateGrid(i, j, player_1_val)
			if success:
				itr += 1

		# Check if X is a winner
		result = tic_tac_toe.isWinner(player_1_val)
		if result:
			tic_tac_toe.clean()
			tic_tac_toe.printGrid(player_1, player_2)
			print("Player 1 is the winner")
			sys.exit()
			break

		# Get user input 2: "O"
		success = False
		while not success and len(tic_tac_toe.emptyGrid()):
			try:
				# use user inputs
				tic_tac_toe.clean()
				
				tic_tac_toe.initialGridDisplay()
				tic_tac_toe.printGrid(player_1, player_2)
				user_input_y = int(input("\n0: Choose between 0-{}: ".format(grid_size*grid_size)))
				
			except Exception as e:
				# the input is invalid
				print("Invalid input. Please try again.")
				continue
			j = user_input_y % grid_size
			i = user_input_y // grid_size
			success = tic_tac_toe.updateGrid(i, j, player_2_val)
			if success:
				itr += 1
		# Check if Y is a winner
		result = tic_tac_toe.isWinner(player_2_val)
		if result:
			tic_tac_toe.clean()
			tic_tac_toe.printGrid(player_1, player_2)
			print("Player 2 is the winner")
			sys.exit()
			break


	print("DRAW!")

def computer_turn(tic_tac_toe, grid_size, human_choice, computer_choice):
	game_depth = len(tic_tac_toe.emptyGrid())
	if game_depth == 0 or tic_tac_toe.isGameOver():
		return 

	tic_tac_toe.clean()
	print(f'Computer turn [{computer_choice}]')
	tic_tac_toe.initialGridDisplay()
	tic_tac_toe.printGrid(computer_choice, human_choice)

	if game_depth == (grid_size*grid_size):
		x = np.random.randint(0, grid_size, 1)[0]
		y = np.random.randint(0, grid_size, 1)[0]
	else:
		move = tic_tac_toe.minimaxAlgorithm(game_depth, COMP)
		x, y = move[0], move[1]

	tic_tac_toe.updateGrid(x, y, COMP)
	time.sleep(1)


def human_turn(tic_tac_toe, grid_size, human_choice, computer_choice):
	game_depth = len(tic_tac_toe.emptyGrid())
	if game_depth == 0 or tic_tac_toe.isGameOver():
		return

	tic_tac_toe.clean()
	print(f'Human turn [{human_choice}]')
	tic_tac_toe.initialGridDisplay()
	tic_tac_toe.printGrid(computer_choice, human_choice)
	grid_no = -1

	while grid_no <= 0 or grid_no > (grid_size*grid_size):
		try:
			grid_no = int(input('Use numpad (0..{}): '.format(grid_size*grid_size)))
			j = grid_no % grid_size
			i = grid_no // grid_size
			can_move = tic_tac_toe.updateGrid(i, j, HUMAN)

			if not can_move:
				print('Bad move')
				grid_no = -1
		except (EOFError, KeyboardInterrupt):
			print('Bye')
			exit()
		except (KeyError, ValueError):
			print('Bad choice') 

def main():

	print("============")
	print("TIC-TAC-TOE")
	print("============")

	grid_size = int(input('Choose the game size: '))
	# grid_size = 3
	print('Initializing a Game (' + str(grid_size) + 'x' + str(grid_size) + ')')
	tic_tac_toe = TicTacToe.TicTacToe(grid_size=grid_size, board=np.zeros((grid_size, grid_size)))
	print("--------------------------")

	human_choice = ''
	computer_choice = ''
	is_player_computer = ''
	first_player = ''
	second_player = ''


	# let's human choose if he wants to play with another human or computer
	while is_player_computer != 'y' and is_player_computer != 'n':
		try:
			is_player_computer = input("Do you want to play vs the computer?(y/n):\nChoice: ").lower()
			print("--------------------------")
		except:
			print("Bad Choice")

		if is_player_computer =='y':
			print("Human VS Computer")
			print("--------------------------")
			# let's human choose to be X or 0
			while human_choice != '0' and human_choice != 'X':
				try:
					human_choice = input("Choose X or O\nChoice: ",).upper()
					print("--------------------------")
				except Error as e:
					print(e)
				except(Keyerror, ValueError):
					print("Bad Choice! Please try again")

			# assigning computer a choice/label
			if human_choice == 'X':
				computer_choice = '0'
			else:
				computer_choice = 'X'


			while first_player != 'Y' and first_player != 'N':
				try:
					first_player = input('Do you want to start first?[y/n]: ').upper()
					print("--------------------------")
				except (EOFError, KeyboardInterrupt):
					print('Bye')
					exit()
				except (KeyError, ValueError):
					print('Bad choice')
			tic_tac_toe.clean()
			# main loop
			while len(tic_tac_toe.emptyGrid()) > 0 and not tic_tac_toe.isGameOver():
				if first_player == 'N':
					computer_turn(tic_tac_toe, grid_size, human_choice, computer_choice)
					first_player = ''
				human_turn(tic_tac_toe, grid_size, human_choice, computer_choice)


				if tic_tac_toe.isWinner(HUMAN):
					tic_tac_toe.clean()
					tic_tac_toe.printGrid(computer_choice, human_choice)
					print('YOU WIN!')
					sys.exit()


				# print("Execute computer")
				computer_turn(tic_tac_toe, grid_size, human_choice, computer_choice)
				if tic_tac_toe.isWinner(COMP):
					tic_tac_toe.clean()
					tic_tac_toe.printGrid(computer_choice, human_choice)
					print('YOU LOOSE!')
					sys.exit()

			tic_tac_toe.printGrid(computer_choice, human_choice)
			print('DRAW!') 

		else:
			print("Human VS Human")
			print("--------------------------")
			while human_choice != '0' and human_choice != 'X':
				try:
					human_choice = input("Choose X or O\nChoice: ",).upper()
					print("--------------------------")
				except Error as e:
					print(e)
				except(Keyerror, ValueError):
					print("Bad Choice! Please try again")

			if human_choice == 'X':
				computer_choice = '0'
			else:
				computer_choice = 'X'

			run_code(tic_tac_toe, None, grid_size, human_choice, computer_choice)


if __name__ == '__main__':
	main()
