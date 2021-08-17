# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 17:43:02 2021

@author: Ronak
"""
'''
Create 3x3 grid with buttons that can be clicked to change to X or O
Use a counter to ensure that maximum moves are not achieve
Use a counter to change between turns (even is X, odd is O)

Add a function to check for a winner
'''

from tkinter import *
from tkinter import messagebox

window = Tk()
window.title('Tic Tac Toe')
window.iconbitmap('D:/Coding/tic-tac-toe/ttt.ico')
window.geometry = ('1000x1000')

   
def disable_buttons():
    buttons = [b1,b2,b3,b4,b5,b6,b7,b8,b9]
    for b in buttons:
        b.config(state=DISABLED)
        
def check_winner():
    # Check for X Win
    if b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X':
        b1.config(bg='green')
        b2.config(bg='green')
        b3.config(bg='green')
        messagebox.showinfo('Winner','Congratulations X! You have won')
        disable_buttons()
        
    if b4['text'] == 'X' and b5['text'] == 'X' and b6['text'] == 'X':
        b4.config(bg='green')
        b5.config(bg='green')
        b6.config(bg='green')
        messagebox.showinfo('Winner','Congratulations X! You have won')
        disable_buttons()
        
    if b6['text'] == 'X' and b7['text'] == 'X' and b9['text'] == 'X':
        b1.config(bg='green')
        b2.config(bg='green')
        b3.config(bg='green')
        messagebox.showinfo('Winner','Congratulations X! You have won')
        disable_buttons()
         
    if b1['text'] == 'X' and b4['text'] == 'X' and b7['text'] == 'X':
        b1.config(bg='green')
        b4.config(bg='green')
        b7.config(bg='green')
        messagebox.showinfo('Winner','Congratulations X! You have won')
        disable_buttons()

    if b2['text'] == 'X' and b5['text'] == 'X' and b8['text'] == 'X':
        b2.config(bg='green')
        b5.config(bg='green')
        b8.config(bg='green')
        messagebox.showinfo('Winner','Congratulations X! You have won')
        disable_buttons()
        
    if b3['text'] == 'X' and b6['text'] == 'X' and b9['text'] == 'X':
        b3.config(bg='green')
        b6.config(bg='green')
        b9.config(bg='green')
        messagebox.showinfo('Winner','Congratulations X! You have won')
        disable_buttons()
        
    if b1['text'] == 'X' and b5['text'] == 'X' and b9['text'] == 'X':
        b1.config(bg='green')
        b5.config(bg='green')
        b9.config(bg='green')
        messagebox.showinfo('Winner','Congratulations X! You have won')
        disable_buttons()
        
    if b3['text'] == 'X' and b5['text'] == 'X' and b7['text'] == 'X':
        b3.config(bg='green')
        b5.config(bg='green')
        b7.config(bg='green')
        messagebox.showinfo('Winner','Congratulations X! You have won')
        disable_buttons()
        
    # Check for O Win
    if b1['text'] == 'O' and b2['text'] == 'O' and b3['text'] == 'O':
        b1.config(bg='green')
        b2.config(bg='green')
        b3.config(bg='green')
        messagebox.showinfo('Winner','Congratulations O! You have won')
        disable_buttons()
        
    if b4['text'] == 'O' and b5['text'] == 'O' and b6['text'] == 'O':
        b4.config(bg='green')
        b5.config(bg='green')
        b6.config(bg='green')
        messagebox.showinfo('Winner','Congratulations O! You have won')
        disable_buttons()
        
    if b6['text'] == 'O' and b7['text'] == 'O' and b9['text'] == 'O':
        b1.config(bg='green')
        b2.config(bg='green')
        b3.config(bg='green')
        messagebox.showinfo('Winner','Congratulations O! You have won')
        disable_buttons()
         
    if b1['text'] == 'O' and b4['text'] == 'O' and b7['text'] == 'O':
        b1.config(bg='green')
        b4.config(bg='green')
        b7.config(bg='green')
        messagebox.showinfo('Winner','Congratulations O! You have won')
        disable_buttons()

    if b2['text'] == 'O' and b5['text'] == 'O' and b8['text'] == 'O':
        b2.config(bg='green')
        b5.config(bg='green')
        b8.config(bg='green')
        messagebox.showinfo('Winner','Congratulations O! You have won')
        disable_buttons()
        
    if b3['text'] == 'O' and b6['text'] == 'O' and b9['text'] == 'O':
        b3.config(bg='green')
        b6.config(bg='green')
        b9.config(bg='green')
        messagebox.showinfo('Winner','Congratulations O! You have won')
        disable_buttons()
        
    if b1['text'] == 'O' and b5['text'] == 'O' and b9['text'] == 'O':
        b1.config(bg='green')
        b5.config(bg='green')
        b9.config(bg='green')
        messagebox.showinfo('Winner','Congratulations O! You have won')
        disable_buttons()
        
    if b3['text'] == 'O' and b5['text'] == 'O' and b7['text'] == 'O':
        b3.config(bg='green')
        b5.config(bg='green')
        b7.config(bg='green')
        messagebox.showinfo('Winner','Congratulations O! You have won')
        disable_buttons()
    
# Turn counter; if even, then X, if odd, then O. Count to make sure the moves do not exceed 9
turn = 0
count = 0

def b_click(b):
    global turn, count
    
    if b['text'] == '' and turn%2 == 0:
        b['text'] = 'X'
        count += 1
        turn += 1
        check_winner()
        
    elif b['text'] == '' and turn%2 != 0:
        b['text'] = 'O'
        count += 1
        turn += 1
        check_winner()
        
    elif b['text'] == 'X' or b['text'] == 'O':
        messagebox.showinfo('Rewind', 'You have selected an occupied box.\nIf you have made an error, click on your own box to remove your selection.\nIf multiple moves must be removed, please do so in order.')
        b['text'] = ''
        count -= 1
        turn -= 1
        check_winner()
        
    elif count == 9:
        messagebox.showerror(title = 'Game Over', message = 'Maximum number of moves achieved')
        check_winner()
        
# Buttons to click on to play Tic-Tac-Toe

b1 = Button(window, height=2, width = 5, font=('Arial', 20), bg='red', command=lambda: b_click(b1))
b2 = Button(window, height=2, width = 5, font=('Arial', 20), bg='red', command=lambda: b_click(b2))
b3 = Button(window, height=2, width = 5, font=('Arial', 20), bg='red', command=lambda: b_click(b3))

b4 = Button(window, height=2, width = 5, font=('Arial', 20), bg='red', command=lambda: b_click(b4))
b5 = Button(window, height=2, width = 5, font=('Arial', 20), bg='red', command=lambda: b_click(b5))
b6 = Button(window, height=2, width = 5, font=('Arial', 20), bg='red', command=lambda: b_click(b6))

b7 = Button(window, height=2, width = 5, font=('Arial', 20), bg='red', command=lambda: b_click(b7))
b8 = Button(window, height=2, width = 5, font=('Arial', 20), bg='red', command=lambda: b_click(b8))
b9 = Button(window, height=2, width = 5, font=('Arial', 20), bg='red', command=lambda: b_click(b9))

# Grid the buttons
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)

# Reset the game
def reset_game():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global turn, count
    turn = 0
    count = 0
    # Buttons to click on to play Tic-Tac-Toe
    
    b1 = Button(window, height=2, width = 5, font=('Arial', 20), bg='red', command=lambda: b_click(b1))
    b2 = Button(window, height=2, width = 5, font=('Arial', 20), bg='red', command=lambda: b_click(b2))
    b3 = Button(window, height=2, width = 5, font=('Arial', 20), bg='red', command=lambda: b_click(b3))
    
    b4 = Button(window, height=2, width = 5, font=('Arial', 20), bg='red', command=lambda: b_click(b4))
    b5 = Button(window, height=2, width = 5, font=('Arial', 20), bg='red', command=lambda: b_click(b5))
    b6 = Button(window, height=2, width = 5, font=('Arial', 20), bg='red', command=lambda: b_click(b6))
    
    b7 = Button(window, height=2, width = 5, font=('Arial', 20), bg='red', command=lambda: b_click(b7))
    b8 = Button(window, height=2, width = 5, font=('Arial', 20), bg='red', command=lambda: b_click(b8))
    b9 = Button(window, height=2, width = 5, font=('Arial', 20), bg='red', command=lambda: b_click(b9))
    
    # Grid the buttons
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)
    
    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)
    
    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)
    
menubar = Menu(window)
window.config(menu=menubar)
    
optionmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Option', menu=optionmenu)
optionmenu.add_command(label='Reset Game', command=reset_game)

window.mainloop()
