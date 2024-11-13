import pytest
from tkinter import *
from SOS import gui, board, game_type_and_conditions  # Import your actual classes

class TestMoves: #camel case because pytest rquirement
    def test_move_in_simple_game(self):
        mock_board = board(board_size = 3, game_mode = "Simple") #chooing the board size and game type
        mock_board.board[0][0] = "S" # row and col on board where we enter S
        assert mock_board.board[0][0] == "S" # return True if it works

    def test_move_in_simple_game(self): # all same logic as Simple
        mock_board = board(board_size = 3, game_mode = "General")
        mock_board.board[0][0] = "S"
        assert mock_board.board[0][0] == "S"

class TestConditions:
    def test_simple_game_win(self):
        root = Tk()
        
        mock_board = board(board_size=3, game_mode="Simple")
        mock_board.board[0][0] = "S"
        mock_board.board[0][1] = "O"
        mock_board.board[0][2] = "S"
        
        mock_buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                row.append(Button(root))
            mock_buttons.append(row)
        
        result = game_type_and_conditions("Simple").is_sos(0, 1, mock_board.board, mock_buttons)
        
        root.destroy()
        assert result == 1

    def test_general_game_draw(self):
        root = Tk()
        
        mock_board = board(board_size=3, game_mode="General")

        mock_board.board[0][0] = "S"
        mock_board.board[0][1] = "O" 
        mock_board.board[0][2] = "S"
        mock_board.board[1][0] = "O"
        mock_board.board[1][1] = "S"
        mock_board.board[1][2] = "O"
        mock_board.board[2][0] = "S"
        mock_board.board[2][1] = "O"
        mock_board.board[2][2] = "S"
        
        mock_buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                row.append(Button(root))
            mock_buttons.append(row)
        
        assert game_type_and_conditions("General").is_draw(mock_board.board) == True
        
        root.destroy()



if __name__ == "__main__":
    pytest.main()