#! /usr/bin/env python3
import random
import tkinter as tk
from tkinter import *

numbers = list(x for x in range (1,26))
currentPosition = 0
moves = 0

root = tk.Tk()
root.title("Snakes and Ladders GUI")
root.grid()

# statusLabel positionLabel rollLabel scoreLabel
rollVar = StringVar()
scoreVar = StringVar()
positionVar = StringVar()
statusVar = StringVar()

label = tk.Label(root,text="",width=25)
statusLabel = tk.Label(root,textvariable=statusVar,width=27,bg='pink')
positionLabel = tk.Label(root,textvariable=positionVar,width=27,bg='purple')
rollLabel = tk.Label(root,textvariable=rollVar,width=27,bg='yellow')
scoreLabel = tk.Label(root,textvariable=scoreVar,width=27,bg='green')

scoreVar.set("The score at this point is %d" % moves)
rollVar.set("no roll yet")
positionVar.set("Current Position is: %d" % (currentPosition+1))
statusVar.set("no new status")

def tkPrintBoard():
    global scoreVar,scoreLabel
    numbers.reverse()
    c = 0
    r = 0
    for i in range(0,len(numbers)):
        if i == 24-currentPosition:
            label = tk.Label(root,text="X",width=5,bg='green')
            label.grid(column=c,row=r)
        elif i%2 == 0:
            label = tk.Label(root,text=str(numbers[i]),width=5,bg='red')
            label.grid(column=c,row=r)
        else:
            label = tk.Label(root,text=str(numbers[i]),width=5,bg='pink')
            label.grid(column=c,row=r)
        c += 1
        if c > 4:
            c = 0
            r += 1
    numbers.reverse()
    r += 1
    scoreLabel.grid(row=10,column=0,columnspan=5)
    statusLabel.grid(row=8,column=0,columnspan=5)
    positionLabel.grid(row=9,column=0,columnspan=5)
    rollLabel.grid(row=7,column=0,columnspan=5)

def FandB():
    for i in range(0,len(numbers)):
        val = numbers[i-1]
        if (i == 1 or i == 10 or i == 20):
            numbers[i-1] = "FB"
        elif (i == 7 or i == 17 or i == 23):
            numbers[i-1] = "BP"

def Check(position,roll):
    global statusVar,positionVar,currentPosition,moves,scoreVar,button
    val = position + roll
    if val > 24:
        statusVar.set("Need to roll a %d" % (24-currentPosition))
    elif val < 24:
        currentPosition = val
        positionVar.set("Current Position: %d" % (currentPosition+1))
        statusVar.set("Good, A little more!")
    elif val == 22:
        currentPosition = 19 
        statusVar.set("Hit BP!! Moved back to nearest FB")
        positionVar.set("Current Position: %d" % (currentPosition+1))
    elif val == 19:
        currentPosition = 22
        statusVar.set("Hit FB!! Moved up to nearest BP")
        positionVar.set("Current Position: %d" % (currentPosition+1))
    else:
        currentPosition = val
        statusVar.set("You Win!!!")
        positionVar.set("Position: %d" % (currentPosition+1))
        scoreVar.set("Final Score: %d" % moves)
        button.grid_forget()
    tkPrintBoard()

def tkMain():
    global numbers,currentPosition,moves
    global rollvar,scoreVar,statusVar,positionVar
    moves += 1
    FWDs = [0,9,19]
    BCKs = [6,16,22]
    roll = random.randint(1,6)
    rollVar.set("You rolled a: %d" % roll)
    val = currentPosition + roll
    statusVar.set("no new status")
    scoreVar.set("The score is: %d" % moves)
    positionVar.set("The current position is: %d" % (currentPosition+1))
    if currentPosition >= 18:
        Check(currentPosition,roll)
    else:
        if (val in FWDs) or (val in BCKs):
            if val in FWDs:
                i = FWDs.index(val)
                currentPosition = BCKs[i]
                statusVar.set("Hit FB!! Moved up to nearest BP")
                positionVar.set("Current Position is: %d" % (currentPosition+1))
            else:
                i = BCKs.index(val)
                currentPosition = FWDs[i]
                statusVar.set("Hit BP!! Moved back to nearest FB")
                positionVar.set("Current Position is: %d" % (currentPosition+1))
        else:
            currentPosition = val
            positionVar.set("Current Position is: %d" % (currentPosition+1))
    tkPrintBoard() 

def main():
    global numbers,currentPosition,moves
    FandB()
    tkPrintBoard()
    button.grid(row=11,column=0,columnspan=5)
    root.mainloop()

button = tk.Button(root,command=tkMain,text="Roll!!!")
main()


