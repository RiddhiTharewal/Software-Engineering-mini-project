# Software-Engineering-mini-project


# Tic-Tac-Toe

Developing the famous Tic-Tac-Toe game.

## Introduction

This is the code repository for th tic-tac-toe game. It allows you to play this game with another human or with the computer (AI algorithm). It is tested for the win and the draw conditions and uses an interractive terminal and let's the user insert his/her choices of placing the "X's" and the "0's" on the board. 


## Two Player Game

  * **Human VS Human**

    Here, you play the game in the most traditional way, where after every player's move, the board is examined for any win conditions. When the gird's have been exhausted, the game is declared as Draw!


  * **Human VS Computer**
  
    Here, you play with the AI engine that runs in the backend. For this particular implementation, I have used the game tree approach. Here, different states of the game are mapped to the node of the tree. When the computer is given a chance, it will calculate the rollout all the possibilities of the given current board state/configuration until it reaches a win condiiton. The root node would be the current board configuration and the algorithm keeps building the child nodes in levels. The first level from the root node would be all the possible moves the computer/AI can take from the given state. The second level would be the moves the human would probably take for every node in the first level. This is continued untill the game is over i.e. the algorithm reaches it's leaf nodes. This condition could leave the player in three states i.e. win, loose or draw/tie.  

    

## Code Files
   
  * main.py: 
    
    Contains the main script for running the game 
  
  * TicTacToe.py: 
  
    Class file for the game
  
   
  * test.py: 
  
    Class file for the unit tests
    
    

## Unit Testing

`test_func_1()` : This unit test function tests for win condition accross row, column, diagonal and lose

`test_func_2` : This unit test function tests for the minimax algorithm to choose the correct next move in order to stop the other player from winning. 

## Run Unit Testing Code 
   
`cd <path_to_repository>`

`python3 unit_test.py`




