import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Initialize the board
board = [' ' for _ in range(9)]
current_player = 'X'

def reset_board():
    global board, current_player
    board = [' ' for _ in range(9)]
    current_player = 'X'
    for button in buttons:
        button.config(text=" ", state=tk.NORMAL)

def check_winner():
    global current_player
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            for i in combo:
                buttons[i].config(bg="lightgreen")
            messagebox.showinfo("Tic Tac Toe", f"Player {current_player} wins!")
            disable_buttons()
            return True
    if ' ' not in board:
        messagebox.showinfo("Tic Tac Toe", "It's a draw!")
        disable_buttons()
        return True
    return False

def disable_buttons():
    for button in buttons:
        button.config(state=tk.DISABLED)

def button_click(index):
    global current_player
    if board[index] == ' ':
        board[index] = current_player
        buttons[index].config(text=current_player)
        
        if check_winner():
            return
        
        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

# Create buttons for the board
buttons = []
for i in range(9):
    button = tk.Button(root, text=" ", font=('Arial', 20), width=5, height=2,
                       command=lambda i=i: button_click(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

# Add a reset button
reset_button = tk.Button(root, text="Reset", font=('Arial', 14), command=reset_board)
reset_button.grid(row=3, column=0, columnspan=3)

# Start the main loop
root.mainloop()
