import tkinter as tk
from tkinter import *
import numpy as np


window=tk.Tk()
pixelVirtual = tk.PhotoImage(width=1, height=1)

p=0

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
                v_ended=ended()
                if v_ended=="Green" or v_ended=="Red" or v_ended=="Draw":
                    print("The Game Result:",v_ended)
                    exit()
                Play()
            v_ended=ended()
            if v_ended=="Green" or v_ended=="Red" or v_ended=="Draw":
                print("The Game Result:",v_ended)
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
    
    def show_states(self):
        temp1=[]
        for i in range(3):
            temp2=[]
            for j in range(3):
                temp2.append(self.board[i][j].state)
            temp1.append(temp2)
        # print(np.array(temp1))


my_board=Board()

def Play():
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # print(my_board.show_states())
    score,action=Maximizer(None,True)
    # print(action)
    player=check_board()
    my_board.board[action[0]][action[1]].switch()

def check_board(states=None):
    try:
        if states==None:
            sum=0
            for i in range(3):
                for j in range(3):
                    sum+=my_board.board[i][j].state
            if sum==-1:
                return 1

            return -1 
    except:
        pass
    sum=0
    for i in range(3):
        for j in range(3):
            sum+=states[i][j]
    if sum==-1:

        return 1

    return -1 

def ended(states=None):
    xy_diag=[]
    x_y_diag=[]
    top_horizontal=[]
    mid_horizontal=[]
    bot_horizontal=[]
    left_vertical=[]
    mid_vertical=[]
    right_vertical=[]
    # # print((my_board.board[2][2].state))
    try:
        if states==None:
            states=[]
            for i in range(3):
                temp=[]
                for j in range(3):
                    # # print("******************",my_board.board[i][j].state)
                    temp.append(my_board.board[i][j].state)
                states.append(temp)
        # # print("trrrrrrrrrrry")
    except:
        pass
    # # print(states)
    for i in range(3):
        for j in range(3):
            if i+j==2:
                xy_diag.append(states[i][j])
            if i==j:
                x_y_diag.append(states[i][j])
            if i==0:
                top_horizontal.append(states[i][j])
            if i==1:
                mid_horizontal.append(states[i][j])
            if i==2:
                bot_horizontal.append(states[i][j])
            if j==0:
                left_vertical.append(states[i][j])
            if j==1:
                mid_vertical.append(states[i][j])
            if j==2:
                right_vertical.append(states[i][j])


    
    if sum(xy_diag)==3 or sum(x_y_diag)==3 or sum(top_horizontal)==3 or sum(mid_horizontal)==3 or sum(bot_horizontal)==3 or sum(left_vertical)==3 or sum(mid_vertical)==3 or sum(right_vertical)==3:
        # print("O or Green wins")
        return "Green"
    elif sum(xy_diag)==-3 or sum(x_y_diag)==-3 or sum(top_horizontal)==-3 or sum(mid_horizontal)==-3 or sum(bot_horizontal)==-3 or sum(left_vertical)==-3 or sum(mid_vertical)==-3 or sum(right_vertical)==-3:
        # print("X or Red wins")
        return "Red"
     
    states=np.array(states)
    p=np.where(states==0)
    if len(p[0])==0:
        # print("Game is a draw")
        return "Draw"
    
    return False


def actions(states):
    avail=np.where(states==0)
    options=[]
    for i in range(len(avail[1])):
        options.append([avail[0][i],avail[1][i]])
    return options



def result(states,option):
    states=np.array(states)
    player=check_board(states)
    states[option[0]][option[1]]=player
    
    return states

def Maximizer(states=None,give=False,depth=0):
    extension=""
    for i in range(depth):
        extension+="\t"
    # print(extension,"max########################",depth)
    
    
    # try:
    v_ended=ended(states)
    # # print(extension,states)
    if v_ended=="Green":
        # print(extension,"###########",depth,"#############end",1)
        return 1
    elif v_ended=="Red":
        # print(extension,"###########",depth,"#############end",-1)
        return -1
    elif v_ended=="Draw":
        # print(extension,"###########",depth,"#############end",0)
        return 0
    # except:
    #     pass
    try:
        if states==None:
            states=[]
            for i in range(3):
                temp=[]
                for j in range(3):
                    temp.append(my_board.board[i][j].state)
                states.append(temp)
            states=np.array(states)
    except:
        pass
    # # print(extension,states)
    states=np.array(states)

    v=-100
    all_actions=actions(states)
    # best_action =all_actions[0]
    for action in all_actions:
        value=Minimizer(result(states,action),False,depth+1)
        if (v<value):
            best_action=action
            v=value
    # print(extension,"###########",depth,"#############",v)
    if give:
        return v,best_action
    return v

def Minimizer(states=None,give=False,depth=0):
    extension=""
    for i in range(depth):
        extension+="\t"
    # print(extension,"min*************************",depth)
    v_ended=ended(states)
    # # print(extension,states)
    if v_ended=="Green":
        # print(extension,"###########",depth,"#############end",1)
        return 1
    elif v_ended=="Red":
        # print(extension,"###########",depth,"#############end",-1)
        return -1
    elif v_ended=="Draw":
        # print(extension,"###########",depth,"#############end",0)
        return 0

    try:
        if states==None:
            states=[]
            for i in range(3):
                temp=[]
                for j in range(3):
                    temp.append(my_board.board[i][j].state)
                states.append(temp)
            states=np.array(states)
    except:
        pass
    # # print(extension,states)
    states=np.array(states)
    v=100
    all_actions=actions(states)
    # best_action =all_actions[0]
    for action in all_actions:
        # print("into max of depth",depth+1)
        value=Maximizer(result(states,action),False,depth+1)
        # print("out of max of depth",depth+1)
        # # print(states)
        if (v>value):
            best_action=action
            v=value
    # print(extension,"************",depth,"************",v)
    if give:
        return v,best_action
    return v
    




window.mainloop()