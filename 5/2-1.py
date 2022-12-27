""" Создайте программу для игры в "Крестики-нолики". 
tkinter 
"""
import os
from tkinter import *
import tkinter.messagebox
from random import randint

os.system('CLS')


def end_game():
    global positions
    positions = [[5, 5, 5] for i in range(3)]
    return positions


def who_first():
    x = randint(0, 1)
    if x == 0:
        tkinter.messagebox.showinfo("Кто ходит?", "  Первым ходит Бот!  ")
    else:
        tkinter.messagebox.showinfo("Кто ходит?", "  Твой ход первый!  ")
    return x


def summa_elem(array):
    summa = 0
    for i in range(3):
        for j in range(3):
            summa += array[i][j]
    return summa


# Нолики победили
def who_wins():
    global positions
    if positions[0][0] == positions[0][1] == positions[0][2] == 0:
        tkinter.messagebox.showinfo("Конец игры", "  Нолики победили!")
        end_game()
    elif positions[1][0] == positions[1][1] == positions[1][2] == 0:
        tkinter.messagebox.showinfo("Конец игры", "  Нолики победили!")
        end_game()
    elif positions[2][0] == positions[2][1] == positions[2][2] == 0:
        tkinter.messagebox.showinfo("Конец игры", "  Нолики победили!")
        end_game()

    elif positions[0][0] == positions[1][0] == positions[2][0] == 0:
        tkinter.messagebox.showinfo("Конец игры", "  Нолики победили!")
        end_game()
    elif positions[0][1] == positions[1][1] == positions[2][1] == 0:
        tkinter.messagebox.showinfo("Конец игры", "  Нолики победили!")
        end_game()
    elif positions[0][2] == positions[1][2] == positions[2][2] == 0:
        tkinter.messagebox.showinfo("Конец игры", "  Нолики победили!")
        end_game()

    elif positions[0][0] == positions[1][1] == positions[2][2] == 0:
        tkinter.messagebox.showinfo("Конец игры", "  Нолики победили!")
        end_game()
    elif positions[0][2] == positions[1][1] == positions[2][0] == 0:
        tkinter.messagebox.showinfo("Конец игры", "  Нолики победили!")
        end_game()

    # Крестики победили
    if positions[0][0] == positions[0][1] == positions[0][2] == 1:
        tkinter.messagebox.showinfo("Конец игры", "  Крестики победили!")
        end_game()
    elif positions[1][0] == positions[1][1] == positions[1][2] == 1:
        tkinter.messagebox.showinfo("Конец игры", "  Крестики победили!")
        end_game()
    elif positions[2][0] == positions[2][1] == positions[2][2] == 1:
        tkinter.messagebox.showinfo("Конец игры", "  Крестики победили!")
        end_game()

    elif positions[0][0] == positions[1][0] == positions[2][0] == 1:
        tkinter.messagebox.showinfo("Конец игры", "  Крестики победили!")
        end_game()
    elif positions[0][1] == positions[1][1] == positions[2][1] == 1:
        tkinter.messagebox.showinfo("Конец игры", "  Крестики победили!")
        end_game()
    elif positions[0][2] == positions[1][2] == positions[2][2] == 1:
        tkinter.messagebox.showinfo("Конец игры", "  Крестики победили!")
        end_game()

    elif positions[0][0] == positions[1][1] == positions[2][2] == 1:
        tkinter.messagebox.showinfo("Конец игры", "  Крестики победили!")
        end_game()
    elif positions[0][2] == positions[1][1] == positions[2][0] == 1:
        tkinter.messagebox.showinfo("Конец игры", "  Крестики победили!")
        end_game()
    elif summa_elem(positions) == 4 or summa_elem(positions) == 5:
        tkinter.messagebox.showinfo("Конец игры", "  Ничья!")
        end_game()


def bot_move():
    global positions
    global first_turn
    global X_or_O

    if X_or_O == 1:
        x = 'X'
    else:
        x = 'O'

    # 1st row
    if positions[0][0] == positions[0][1] == X_or_O and positions[0][2] < 0:
        btn0_2.configure(text=x, font=('Arial Bold', 9))
        positions[0][2] = X_or_O
    elif positions[0][0] == positions[0][2] == X_or_O and positions[0][1] < 0:
        btn0_1.configure(text=x, font=('Arial Bold', 9))
        positions[0][1] = X_or_O
    elif positions[0][1] == positions[0][2] == X_or_O and positions[0][0] < 0:
        btn0_0.configure(text=x, font=('Arial Bold', 9))
        positions[0][0] = X_or_O
    # 2nd row
    elif positions[1][0] == positions[1][1] == X_or_O and positions[1][2] < 0:
        btn1_2.configure(text=x, font=('Arial Bold', 9))
        positions[1][2] = X_or_O
    elif positions[1][0] == positions[1][2] == X_or_O and positions[1][1] < 0:
        btn1_1.configure(text=x, font=('Arial Bold', 9))
        positions[1][1] = X_or_O
    elif positions[1][1] == positions[1][2] == X_or_O and positions[1][0] < 0:
        btn1_0.configure(text=x, font=('Arial Bold', 9))
        positions[1][0] = X_or_O
    # 3rd row
    elif positions[2][0] == positions[2][1] == X_or_O and positions[2][2] < 0:
        btn2_2.configure(text=x, font=('Arial Bold', 9))
        positions[2][2] = X_or_O
    elif positions[2][0] == positions[2][2] == X_or_O and positions[2][1] < 0:
        btn2_1.configure(text=x, font=('Arial Bold', 9))
        positions[2][1] = X_or_O
    elif positions[2][1] == positions[2][2] == X_or_O and positions[2][0] < 0:
        btn2_0.configure(text=x, font=('Arial Bold', 9))
        positions[2][0] = X_or_O
    # 1st col
    elif positions[0][0] == positions[1][0] == X_or_O and positions[2][0] < 0:
        btn2_0.configure(text=x, font=('Arial Bold', 9))
        positions[2][0] = X_or_O
    elif positions[0][0] == positions[2][0] == X_or_O and positions[1][0] < 0:
        btn1_0.configure(text=x, font=('Arial Bold', 9))
        positions[1][0] = X_or_O
    elif positions[1][0] == positions[2][0] == X_or_O and positions[0][0] < 0:
        btn0_0.configure(text=x, font=('Arial Bold', 9))
        positions[0][0] = X_or_O
    # 2nd col
    elif positions[0][1] == positions[1][1] == X_or_O and positions[2][1] < 0:
        btn2_1.configure(text=x, font=('Arial Bold', 9))
        positions[2][1] = X_or_O
    elif positions[0][1] == positions[2][1] == X_or_O and positions[1][1] < 0:
        btn1_1.configure(text=x, font=('Arial Bold', 9))
        positions[1][1] = X_or_O
    elif positions[1][1] == positions[2][1] == X_or_O and positions[0][1] < 0:
        btn0_1.configure(text=x, font=('Arial Bold', 9))
        positions[0][1] = X_or_O
    # 3rd col
    elif positions[0][2] == positions[1][2] == X_or_O and positions[2][2] < 0:
        btn2_2.configure(text=x, font=('Arial Bold', 9))
        positions[2][2] = X_or_O
    elif positions[0][2] == positions[2][2] == X_or_O and positions[1][2] < 0:
        btn1_2.configure(text=x, font=('Arial Bold', 9))
        positions[1][2] = X_or_O
    elif positions[1][2] == positions[2][2] == X_or_O and positions[0][2] < 0:
        btn0_2.configure(text=x, font=('Arial Bold', 9))
        positions[0][2] = X_or_O
    # Main diag
    elif positions[0][0] == positions[1][1] == X_or_O and positions[2][2] < 0:
        btn2_2.configure(text=x, font=('Arial Bold', 9))
        positions[2][2] = X_or_O
    elif positions[0][0] == positions[2][2] == X_or_O and positions[1][1] < 0:
        btn1_1.configure(text=x, font=('Arial Bold', 9))
        positions[1][1] = X_or_O
    elif positions[1][1] == positions[2][2] == X_or_O and positions[0][0] < 0:
        btn0_0.configure(text=x, font=('Arial Bold', 9))
        positions[0][0] = X_or_O
    # Secondary diag
    elif positions[0][2] == positions[1][1] == X_or_O and positions[2][0] < 0:
        btn2_0.configure(text=x, font=('Arial Bold', 9))
        positions[2][0] = X_or_O
    elif positions[0][2] == positions[2][0] == X_or_O and positions[1][1] < 0:
        btn1_1.configure(text=x, font=('Arial Bold', 9))
        positions[1][1] = X_or_O
    elif positions[2][0] == positions[1][1] == X_or_O and positions[0][2] < 0:
        btn0_2.configure(text=x, font=('Arial Bold', 9))
        positions[0][2] = X_or_O
    # Other solo positions
    elif positions[1][1] < 0:
        btn1_1.configure(text=x, font=('Arial Bold', 9))
        positions[1][1] = X_or_O
    elif positions[0][0] < 0:
        btn0_0.configure(text=x, font=('Arial Bold', 9))
        positions[0][0] = X_or_O
    elif positions[0][2] < 0:
        btn0_2.configure(text=x, font=('Arial Bold', 9))
        positions[0][2] = X_or_O
    elif positions[2][0] < 0:
        btn2_0.configure(text=x, font=('Arial Bold', 9))
        positions[2][0] = X_or_O
    elif positions[2][2] < 0:
        btn2_2.configure(text=x, font=('Arial Bold', 9))
        positions[2][2] = X_or_O
    elif positions[0][1] < 0:
        btn0_1.configure(text=x, font=('Arial Bold', 9))
        positions[0][1] = X_or_O
    elif positions[2][1] < 0:
        btn2_1.configure(text=x, font=('Arial Bold', 9))
        positions[2][1] = X_or_O
    elif positions[1][0] < 0:
        btn1_0.configure(text=x, font=('Arial Bold', 9))
        positions[1][0] = X_or_O
    elif positions[1][2] < 0:
        btn1_2.configure(text=x, font=('Arial Bold', 9))
        positions[1][2] = X_or_O

    who_wins()

    if X_or_O == 1:
        X_or_O = 0
    else:
        X_or_O = 1


def clicked(row, col):
    global clicks
    global X_or_O
    global positions

    if X_or_O == 1:
        x = 'X'
    else:
        x = 'O'

    if positions[row][col] < 0:

        if row == 0 and col == 0:
            btn0_0.configure(text=x, font=('Arial Bold', 9))
        if row == 0 and col == 1:
            btn0_1.configure(text=x, font=('Arial Bold', 9))
        if row == 0 and col == 2:
            btn0_2.configure(text=x, font=('Arial Bold', 9))
        if row == 1 and col == 0:
            btn1_0.configure(text=x, font=('Arial Bold', 9))
        if row == 1 and col == 1:
            btn1_1.configure(text=x, font=('Arial Bold', 9))
        if row == 1 and col == 2:
            btn1_2.configure(text=x, font=('Arial Bold', 9))
        if row == 2 and col == 0:
            btn2_0.configure(text=x, font=('Arial Bold', 9))
        if row == 2 and col == 1:
            btn2_1.configure(text=x, font=('Arial Bold', 9))
        if row == 2 and col == 2:
            btn2_2.configure(text=x, font=('Arial Bold', 9))

        positions[row][col] = X_or_O
        # print(positions)
        who_wins()

        if X_or_O == 1:
            X_or_O = 0
        else:
            X_or_O = 1

        bot_move()
        # print(positions)


positions = [[-90, -80, -70],
             [-60, -50, -40],
             [-30, -20, -10]]
X_or_O = 1  # 1 - крестик, 0 - нолик
first_turn = -1  # 0 - бот, 1 - игрок

window = Tk()
window.title("Крестики-нолики")

# 1st row
btn0_0 = Button(window, text='', command=lambda: clicked(
    0, 0), height=5, width=10)
btn0_0.grid(column=0, row=1)
btn0_1 = Button(window, text='', command=lambda: clicked(
    0, 1), height=5, width=10)
btn0_1.grid(column=1, row=1)
btn0_2 = Button(window, text='', command=lambda: clicked(
    0, 2), height=5, width=10)
btn0_2.grid(column=2, row=1)

# 2nd row
btn1_0 = Button(window, text='', command=lambda: clicked(
    1, 0), height=5, width=10)
btn1_0.grid(column=0, row=2)
btn1_1 = Button(window, text='', command=lambda: clicked(
    1, 1), height=5, width=10)
btn1_1.grid(column=1, row=2)
btn1_2 = Button(window, text='', command=lambda: clicked(
    1, 2), height=5, width=10)
btn1_2.grid(column=2, row=2)

# 3rd row
btn2_0 = Button(window, text='', command=lambda: clicked(
    2, 0), height=5, width=10)
btn2_0.grid(column=0, row=3)
btn2_1 = Button(window, text='', command=lambda: clicked(
    2, 1), height=5, width=10)
btn2_1.grid(column=1, row=3)
btn2_2 = Button(window, text='', command=lambda: clicked(
    2, 2), height=5, width=10)
btn2_2.grid(column=2, row=3)

first_turn = who_first()

if first_turn == 0:
    bot_move()

window.mainloop()
