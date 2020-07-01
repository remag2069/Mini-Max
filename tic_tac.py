import tkinter as tk
from tkinter import *
import numpy as np


window=tk.Tk()
pixelVirtual = tk.PhotoImage(width=1, height=1)

class spaces():
    def __init__(self,pos):
        self.button=Button(window,image=pixelVirtual,text='',command=self.switch,bg="white",width=40,height=40)
        self.button.grid(row = pos[0], column = pos[1])
        self.state=0

    def give_button(self):
        return self.button

    def switch(self):
        if self.button['bg']=='white':
            player=check_board()
            if player==1:
                self.button.configure(bg = "green")
                self.button.configure(text = "O")
                self.state=1
            else:
                self.button.configure(bg = "red")
                self.button.configure(text = "X")
                self.state=-1

            if ended():
                exit()

class Board():
    def __init__(self):
        self.board=[]
        for i in range(3):
            temp=[]
            for j in range(3):
                s=spaces([i,j])
                # b=s.give_button()
                temp.append(s)
            self.board.append(temp)
    


my_board=Board()

def check_board():
    sum=0
    for i in range(3):
        for j in range(3):
            sum+=my_board.board[i][j].state
    if sum==-1:
        return 1

    return -1 

def ended():
    xy_diag=[]
    x_y_diag=[]
    top_horizontal=[]
    mid_horizontal=[]
    bot_horizontal=[]
    left_vertical=[]
    mid_vertical=[]
    right_vertical=[]

    states=[]
    for i in range(3):
        temp=[]
        for j in range(3):
            temp.append(my_board.board[i][j].state)
            if i+j==2:
                xy_diag.append(my_board.board[i][j].state)
            if i==j:
                x_y_diag.append(my_board.board[i][j].state)
            if i==0:
                top_horizontal.append(my_board.board[i][j].state)
            if i==1:
                mid_horizontal.append(my_board.board[i][j].state)
            if i==2:
                bot_horizontal.append(my_board.board[i][j].state)
            if j==0:
                left_vertical.append(my_board.board[i][j].state)
            if j==1:
                mid_vertical.append(my_board.board[i][j].state)
            if j==2:
                right_vertical.append(my_board.board[i][j].state)
        states.append(temp)
    if sum(xy_diag)==3 or sum(x_y_diag)==3 or sum(top_horizontal)==3 or sum(mid_horizontal)==3 or sum(bot_horizontal)==3 or sum(left_vertical)==3 or sum(mid_vertical)==3 or sum(right_vertical)==3:
        print("O or Green wins")
        return True
    elif sum(xy_diag)==-3 or sum(x_y_diag)==-3 or sum(top_horizontal)==-3 or sum(mid_horizontal)==-3 or sum(bot_horizontal)==-3 or sum(left_vertical)==-3 or sum(mid_vertical)==-3 or sum(right_vertical)==-3:
        print("X or Red wins")
        return True
     
    states=np.array(states)
    p=np.where(states==0)
    if len(p[0])==0:
        print("Game is a draw")
        return True
    
    return False
    
window.mainloop()