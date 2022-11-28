# -*- coding: utf-8 -*-
# importing Packages from tkinter
from tkinter import *
from  random import choice

# from tkinter import messagebox

# Player1 = 'X'
# stop_game = False

# def clicked(r,c):

# 	#player
# 	global Player1
# 	# global stop_game

# 	if Player1 == "X" and states[r] == 0 and stop_game == False:
# 		b[r].configure(text = "X")
# 		states[r] = 'X'
# 		Player1='O'


# 	if Player1 == 'O' and states[r] == 0 and stop_game == False:
# 		b[r].configure(text = 'O')
# 		states[r] = "O"
# 		Player1 = "X"

# 	check_if_win()
# 	# check_if_tie()
# 	# if check_if_win() == False:
# 	#	 tie = messagebox.showinfo("tie","its tie")
# 	#	 return tie
# def check_if_win():
# 	global stop_game
# 	# count = 0

# 	for i in range(3):
# 		if states[i][0] == states[i][1] == states[i][2] !=0:
# 			stop_game = True

# 			winner = messagebox.showinfo("Winner", states[i][0] + " Won")
# 			# disableAllButton()
# 			break

# 	# for j in range(3):
# 		elif states [0][i] == states[1][i] == states[2][i] != 0:
# 			stop_game = True

# 			winner = messagebox.showinfo("Winner", states[0][i]+ " Won!")
# 			break

# 		elif states[0][0] == states[1][1] == states[2][2] !=0:
# 			stop_game = True

# 			winner = messagebox.showinfo("Winner", states[0][0]+ " Won!")
# 			break

# 		elif states[0][2] == states[1][1] == states[2][0] !=0:
# 			stop_game = True

# 			winner = messagebox.showinfo("Winner" , states[0][2]+ " Won!")
# 			break

# 		elif states[0][0] and states[0][1] and states[0][2] and states[1][0] and states[1][1] and states[1][2] and states[2][0] and states[2][1] and states[2][2] != 0:
# 			stop_game = True

# 			winner = messagebox.showinfo("tie", "Tie")

# # Design window
# #Creating the Canvas
# root = Tk()
# # Title of the window
# root.title("GeeksForGeeks-:Tic Tac Toe")
# root.resizable(0,0)

# #Button
# b = [
# 	[0,0,0],
# 	[0,0,0],
# 	[0,0,0]]

# #text for buttons
# states = [
# 	[0,0,0],
# 	[0,0,0],
# 	[0,0,0]]

# for i in range(3):
# 	for j in range(3):

# 		b[i][j] = Button(
# 						height = 4, width = 8,
# 						font = ("Helvetica","20"),
# 						command = lambda r = i, c = j : clicked(r,c))
# 		b[i][j].grid(row = i, column = j)

# mainloop()
# Взял с интернета - не работает
root = Tk()
field = []
main = choice(['O', 'X'])
root.title(f'Ходят {main}')

for row in range(3):
    table = []
    for col in range(3):
        button = Button(root, text=' ', width=10, height=4, command=lambda row1=row, col1=col: click(row1, col1))
        button.grid(row=row, column=col, sticky='nsew')
        table.append(button)

    field.append(table)


def click(row, col):
    global main
    if field[row][col]['text'] == ' ' and main == 'X':
        field[row][col]['text'] = 'X'
        check_win()
        main = 'O'

    if field[row][col]['text'] == ' ' and main == 'O':
        field[row][col]['text'] = 'O'
        check_win()
        main = 'X'

def check_win():
    if field[0][0]['text'] == 'X' and field[0][1]['text'] == 'X' and field[0][2]['text'] == 'X':
        field[1][1]['text'] = 'Победил X'
    if field[1][0]['text'] == 'X' and field[1][1]['text'] == 'X' and field[1][2]['text'] == 'X':
        field[1][1]['text'] = 'Победил X'
    if field[2][0]['text'] == 'X' and field[2][1]['text'] == 'X' and field[2][2]['text'] == 'X':
        field[1][1]['text'] = 'Победил X'
    if field[0][0]['text'] == 'X' and field[1][1]['text'] == 'X' and field[2][2]['text'] == 'X':
        field[1][1]['text'] = 'Победил X'
    if field[0][2]['text'] == 'X' and field[1][1]['text'] == 'X' and field[2][0]['text'] == 'X':
        field[1][1]['text'] = 'Победил X'

    if field[0][0]['text'] == 'O' and field[0][1]['text'] == 'O' and field[0][2]['text'] == 'O':
        field[1][1]['text'] = 'Победил O'
    if field[1][0]['text'] == 'O' and field[1][1]['text'] == 'O' and field[1][2]['text'] == 'O':
        field[1][1]['text'] = 'Победил O'
    if field[2][0]['text'] == 'O' and field[2][1]['text'] == 'O' and field[2][2]['text'] == 'O':
        field[1][1]['text'] = 'Победил O'
    if field[0][0]['text'] == 'O' and field[1][1]['text'] == 'O' and field[2][2]['text'] == 'O':
        field[1][1]['text'] = 'Победил O'
    if field[0][2]['text'] == 'O' and field[1][1]['text'] == 'O' and field[2][0]['text'] == 'O':
        field[1][1]['text'] = 'Победил O'


root.mainloop()
