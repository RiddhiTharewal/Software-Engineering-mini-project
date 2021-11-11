import unittest 
import main
import TicTacToe
import numpy as np

class TestAssertEqual(unittest.TestCase):
	
	def test_func_1(self):
		computer_choice = "X"
		human_choice = "0"
		board_config = np.array([[1,1,0],
								[-1,1,1],
								[-1,0,0]])
		print("Running test for win conditions in the board configuration:")
		#Win condition is determined is three move of same kind are in a row, colum or diagonal
		testObject = TicTacToe.TicTacToe(board=board_config)
		testObject.printGrid(computer_choice, human_choice)
		self.assertFalse(testObject.isWinner(user=-1))
		print("Test Output: ",testObject.isWinner(user=-1))

		#Row winning condition
		board_config = np.array([[1,-1,1],
								[-1,-1,-1],
								[0,-1,0]])
		testObject = TicTacToe.TicTacToe(board=board_config)
		testObject.printGrid(computer_choice, human_choice)
		self.assertTrue(testObject.isWinner(user=-1))
		print("Test Output: ",testObject.isWinner(user=-1))

		#Column winning condition
		board_config = np.array([[1,-1,0],
								[1,-1,0],
								[1,1,0]])
		testObject = TicTacToe.TicTacToe(board=board_config)
		testObject.printGrid(computer_choice, human_choice)
		self.assertTrue(testObject.isWinner(user=1))
		print("Test Output: ",testObject.isWinner(user=1))

		#Diagonal winning condition
		board_config = np.array([[-1,0,1],
								[-1,-1,0],
								[0,-1,-1]])
		testObject = TicTacToe.TicTacToe(board=board_config)
		testObject.printGrid(computer_choice, human_choice)
		self.assertTrue(testObject.isWinner(user=-1))
		print("Test Output: ",testObject.isWinner(user=-1))

	def test_func_2(self):
		computer_choice = "X"
		human_choice = "0"
		board_config = np.array([[1,0,1],
								[-1,1,0],
								[0,-1,-1]])
		print("Running test for minimaxAlgorithm():")
		print("Next Turn: Computer (X)")
		
		#Win condition is determined is three move of same kind are in a row, colum or diagonal
		testObject = TicTacToe.TicTacToe(board=board_config)
		testObject.printGrid(computer_choice, human_choice)
		coords = testObject.minimaxAlgorithm(game_depth=4, player=+1)
		x, y = coords[0], coords[1]
		self.assertEqual((x, y), (0,1))
		print("Test Output: ", (x,y))
		testObject.updateGrid(x, y, +1)
		testObject.printGrid(computer_choice, human_choice)

if __name__ == '__main__':
	unittest.main()
