import pytest
from tkinter import *
from SOS import board, computer, gui

class Test_CvH:
    def test_computer_response(self): 
        game = board(board_size=3, game_mode="Simple") # we're just setting intital conditions
        comp = computer(board_size=3)

        # player sets an S in the middle
        game.board[1][1] = 'S'
        
        # computer sees this and makes a movve based on the algo
        buttons = [[None, None, None],
                  [None, None, None],
                  [None, None, None]]
        
        move = comp.mock_sos(game.board, buttons)
        
        #pretty sure it uses this method
        if not move:
            move = comp.brute_force(game.board)
        row, col, symbol = move
        
        # this is just way to check if eveyrthing was done corretly
        assert 0 <= row < 3 
        assert 0 <= col < 3
        assert symbol in ['S', 'O']

class Test_CvC:
    def test_computer_moves(self):
        
        # making the initial setup.
        game = board(board_size = 3, game_mode="Simple")
        comp1 = computer(board_size = 3)
        comp2 = computer(board_size = 3)
        
        # make empty buttons
        buttons = [[None, None, None],
                  [None, None, None],
                  [None, None, None]]
        
        # this is the part where the first computer plays
        move1 = comp1.mock_sos(game.board, buttons)
        
        if not move1:
            move1 = comp1.brute_force(game.board)
        row1, col1, symbol1 = move1
        game.board[row1][col1] = symbol1
        
        # the second computer makes a move 
        move2 = comp2.mock_sos(game.board, buttons)
        
        if not move2:
            move2 = comp2.brute_force(game.board)
        row2, col2, symbol2 = move2
        
        # thi ensure it is all done corrently
        assert 0 <= row1 < 3 
        assert 0 <= col1 < 3
        assert symbol1 in ['S', 'O']
        assert symbol2 in ['S', 'O']