import pytest
from tkinter import Tk
from tkinter import Button
from tkinter import Checkbutton
from tkinter import BooleanVar
from tkinter import Label
from tkinter import messagebox
import random

from project import TicTacToeGame, initialize_board, check_winner, is_board_full, get_valid_moves

@pytest.fixture
def setup_game():
    root = Tk()
    game = TicTacToeGame(root)
    game.pack()
    yield game
    root.destroy()

def test_initialize_board():
    board = initialize_board()
    assert len(board) == 9
    assert all(spot == ' ' for spot in board)

def test_check_winner():
    winning_boards = [
        ['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', 'X', 'X', 'X', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', 'X', 'X', 'X'],
        ['X', ' ', ' ', 'X', ' ', ' ', 'X', ' ', ' '],
        [' ', 'X', ' ', ' ', 'X', ' ', ' ', 'X', ' '],
        [' ', ' ', 'X', ' ', ' ', 'X', ' ', ' ', 'X'],
        ['X', ' ', ' ', ' ', 'X', ' ', ' ', ' ', 'X'],
        [' ', ' ', 'X', ' ', 'X', ' ', 'X', ' ', ' '],
    ]
    for board in winning_boards:
        assert check_winner(board) is True

    no_winner_board = ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X', 'O']
    assert check_winner(no_winner_board) is False

def test_is_board_full():
    full_board = ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X', 'O']
    assert is_board_full(full_board) is True

    not_full_board = ['X', 'O', 'X', 'O', 'X', ' ', 'O', 'X', 'O']
    assert is_board_full(not_full_board) is False

def test_get_valid_moves():
    board = ['X', ' ', 'O', ' ', 'X', 'O', ' ', ' ', 'X']
    valid_moves = get_valid_moves(board)
    assert valid_moves == [2, 4, 7, 8]

def test_game_reset(setup_game):
    game = setup_game
    game.current_player = 'O'
    game.board = ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X', 'O']
    game.reset_game()
    assert game.current_player == 'X'
    assert game.board == [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def test_game_win(setup_game, monkeypatch):
    game = setup_game
    game.ai_enabled = False

    monkeypatch.setattr(messagebox, 'showinfo', lambda *args: None)
    game.board = ['X', 'X', 'X', 'O', 'O', ' ', ' ', ' ', ' ']
    game.make_move(5)
    assert game.current_player == 'O'
    assert game.board == ['X', 'X', 'X', 'O', 'O', 'X', ' ', ' ', ' ']

def test_game_draw(setup_game, monkeypatch):
    game = setup_game
    game.ai_enabled = False

    monkeypatch.setattr(messagebox, 'showinfo', lambda *args: None)
    game.board = ['X', 'O', 'X', 'X', 'O', 'O', 'O', 'X', 'X']
    game.make_move(6)
    assert game.current_player == 'O'
    assert game.board == ['X', 'O', 'X', 'X', 'O', 'O', 'X', 'X', 'X']

def test_ai_move(setup_game, monkeypatch):
    game = setup_game
    game.ai_enabled = True

    monkeypatch.setattr(random, 'choice', lambda seq: 5)
    game.make_move(0)
    game.make_move(1)
    assert game.board == ['X', 'O', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    assert game.current_player == 'X'

if __name__ == "__main__":
    pytest.main()
