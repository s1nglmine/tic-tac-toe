import tkinter as tk

window = tk.Tk()
window.title('Крестики нолики')
window.resizable(False, False)

result_label = tk.Label(window, font=('Helvetica', 20))
result_label.grid(row=3, column=0, columnspan=3)

board = []
for i in range(3):
    row = []
    for j in range(3):
        button = tk.Button(window, width=5, height=2, font=('Helvetica', 20), command=lambda i=i, j=j: click(i, j))
        button.grid(row=i, column=j)
        row.append(button)
    board.append(row)

current_player = 'X'

def click(i, j):
    global current_player
    board[i][j]['text'] = current_player
    board[i][j]['state'] = 'disabled'
    if check_winner():
        result_text = f'Игрок {current_player} выиграл!'
    elif check_draw():
        result_text = 'Ничья!'
    else:
        current_player = 'O' if current_player == 'X' else 'X'
        result_text = f'Игрок {current_player} ходит.'
    result_label.config(text=result_text)

def check_winner():
    for row in board:
        if row[0]['text'] == row[1]['text'] == row[2]['text'] != '':
            return True
    for col in range(3):
        if board[0][col]['text'] == board[1][col]['text'] == board[2][col]['text'] != '':
            return True
    if board[0][0]['text'] == board[1][1]['text'] == board[2][2]['text'] != '':
        return True
    if board[0][2]['text'] == board[1][1]['text'] == board[2][0]['text'] != '':
        return True
    return False

def check_draw():
    for row in board:
        for button in row:
            if button['text'] == '':
                return False
    return True

window.mainloop()
