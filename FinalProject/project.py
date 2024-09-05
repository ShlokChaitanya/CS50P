import tkinter as tk
from tkinter import messagebox
import random

def main():
    root = tk.Tk()
    root.title("Tic-Tac-Toe")
    root.geometry("500x500")

    app = TicTacToeGame(root)
    app.pack(expand=True, fill='both')

    root.mainloop()

class TicTacToeGame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.current_player = 'X'
        self.board = initialize_board()
        self.buttons = []
        self.ai_enabled = True
        self.status_label = None
        self.create_widgets()

    def create_widgets(self):
        self.status_label = tk.Label(self, text=f"Player {self.current_player}'s turn", font=('normal', 15))
        self.status_label.grid(row=0, column=0, columnspan=3, pady=10)

        for i in range(9):
            button = tk.Button(self, text='', font=('normal', 20), width=5, height=2, bg='white', fg='black', relief='raised', borderwidth=3, command=lambda i=i: self.on_button_click(i))
            button.grid(row=(i // 3) + 1, column=i % 3, padx=5, pady=5)
            self.buttons.append(button)

        self.reset_button = tk.Button(self, text="Reset", font=('normal', 15), bg='#f0a500', fg='white', command=self.reset_game)
        self.reset_button.grid(row=4, column=0, columnspan=1, pady=10)
        self.exit_button = tk.Button(self, text="Exit", font=('normal', 15), bg='#d9534f', fg='white', command=self.master.quit)
        self.exit_button.grid(row=4, column=2, columnspan=1, pady=10)

        self.ai_checkbox_var = tk.BooleanVar(value=self.ai_enabled)
        self.ai_checkbox = tk.Checkbutton(self, text="Enable AI", font=('normal', 12), variable=self.ai_checkbox_var, command=self.toggle_ai)
        self.ai_checkbox.grid(row=4, column=1, columnspan=1, pady=10)

    def toggle_ai(self):
        self.ai_enabled = self.ai_checkbox_var.get()

    def on_button_click(self, index):
        if self.board[index] == ' ':
            self.make_move(index)
            if self.check_end_conditions():
                return

            if self.ai_enabled and self.current_player == 'O':
                self.ai_move()
                self.check_end_conditions()

    def make_move(self, index):
        self.board[index] = self.current_player
        self.buttons[index].config(text=self.current_player, state=tk.DISABLED, disabledforeground='black')
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        self.update_status()

    def ai_move(self):
        available_moves = get_valid_moves(self.board)
        if available_moves:
            ai_choice = random.choice(available_moves) - 1
            self.make_move(ai_choice)

    def check_end_conditions(self):
        if check_winner(self.board):
            winner = 'O' if self.current_player == 'X' else 'X'
            self.update_status(f"Player {winner} wins!")
            messagebox.showinfo("Tic-Tac-Toe", f"Player {winner} wins!")
            self.master.after(2000, self.reset_game)
            return True
        elif is_board_full(self.board):
            self.update_status("It's a draw!")
            messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
            self.master.after(2000, self.reset_game)
            return True
        return False

    def update_status(self, message=None):
        if message:
            self.status_label.config(text=message)
        else:
            self.status_label.config(text=f"Player {self.current_player}'s turn")

    def disable_buttons(self):
        for button in self.buttons:
            button.config(state=tk.DISABLED)

    def reset_game(self):
        self.board = initialize_board()
        self.current_player = 'X'
        for button in self.buttons:
            button.config(text='', state=tk.NORMAL, bg='white')
        self.update_status()

def initialize_board():
    return [' ' for _ in range(9)]

def check_winner(board):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            return True
    return False

def is_board_full(board):
    return ' ' not in board

def get_valid_moves(board):
    return [i + 1 for i, spot in enumerate(board) if spot == ' ']

if __name__ == "__main__":
    main()
