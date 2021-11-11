from math import inf 
import numpy as np 
import platform
import sys
from os import system
sys.dont_write_bytecode = True


class TicTacToe:

	def __init__(self, grid_size=3, player_2=None, game_depth=0, board=np.zeros((3, 3))):
		
		self.human = -1
		self.computer = +1


		self.grid_size = grid_size

		self.input_grid = board
		
	def initialGridDisplay(self):
		initial_grid = np.arange(start=0, stop=self.grid_size*self.grid_size, step=1)
		initial_grid = np.reshape(initial_grid, (self.grid_size, self.grid_size))

		for i in range(0, initial_grid.shape[0]):
			print(" "),
			for j in range(0, initial_grid.shape[1]):
				print(' |   ',initial_grid[i][j], sep=' ', end=' ',flush=True)
			print("\n"),

	
	def printGrid(self, computer_choice, human_choice):
		
		chars = {
		-1: human_choice,
		+1: computer_choice,
		0: ' '}
		
		str_line = '---------------'

		print('\n' + str_line)
		for row in self.input_grid:
			for cell in row:
				symbol = chars[cell]
				print(f'| {symbol} |', end='')
			print('\n' + str_line)



	def isValidMove(self, i,j):

		if self.input_grid[i][j] == 0:
			return True
		else:
			return False


	def updateGrid(self, i, j, user):

		if self.isValidMove(i,j):
			self.input_grid[i][j] = user
			return True
		else:
			print("Already Occupied...Choose another position")
			return False

	
	def emptyGrid(self):
		self.empty_grid = []

		for x, row in enumerate(self.input_grid):
			for y, cell in enumerate(row):
				if cell == 0:
					self.empty_grid.append([x,y])
		return self.empty_grid

	

	def isWinner(self, user):

		# comp = 1
		# human = -1

		# across diagonal
		input_grid_diag_0 = np.diagonal(self.input_grid)
		input_grid_diag_1 = np.fliplr(self.input_grid).diagonal()

		if (np.sum(input_grid_diag_0) == user*self.grid_size):
			return True

		if (np.sum(input_grid_diag_1) == user*self.grid_size):
			return True

		val_rows = np.sum(self.input_grid, axis=1) # for comp
		arr_rows = np.where(val_rows == user*self.grid_size)[0] #for human
		if len(arr_rows) != 0:
			return True

		val_col = np.sum(self.input_grid, axis=0)
		arr_col = np.where(val_col == user*self.grid_size)[0]
		if len(arr_col) != 0:
			return True
		
		return False
	def evaluateScore(self):
		if self.isWinner(self.computer):
			score = self.computer
		elif self.isWinner(self.human):
			score = self.human
		else:
			score = 0

		return score

	
	def isGameOver(self):
		return self.isWinner(user=self.human) or self.isWinner(user=self.computer)


	
	def minimaxAlgorithm(self, game_depth, player):
		if player == self.computer:
			best = [-1, -1, -inf]
		else:
			best = [-1, -1, +inf]

		if game_depth == 0 or self.isGameOver():
			score = self.evaluateScore()
			return [-1, -1, score]


		for cell in self.emptyGrid():
			x, y = cell[0], cell[1]

			self.input_grid[x][y] = player
			score = self.minimaxAlgorithm(game_depth - 1, -player)
			self.input_grid[x][y] = 0
			score[0], score[1] = x, y

			if player == self.computer:
				if score[2] > best[2]:
					best = score

			else:
				if score[2] < best[2]:
					best = score
	
		return best


	
	def clean(self):
		os_name = platform.system().lower()
		if 'windows' in os_name:
			system('cls')
		else:
			system('clear')


