import tkinter as tk
from PIL import Image, ImageTk
import random
from tkinter.ttk import *
from tkinter import messagebox
import sys, subprocess

root=tk.Tk()

circle=Image.open("D:\\Daniel Rabe\\Downloads\\circl.png") # 80x80
mycircle=ImageTk.PhotoImage(circle)
cross=Image.open("D:\\Daniel Rabe\\Downloads\\cross.png") # 80x80
mycross=ImageTk.PhotoImage(cross)
choice=[mycircle, mycross]
random_first=random.choice(choice)
random_second=random_second=choice[choice.index(random_first)-1]
player1_moves={}
player2_moves={}
finished=False

def end_game(player):
    for buttons in root.winfo_children():
        buttons.configure(state=tk.DISABLED)
        global finished
    finished=True    
    if player==None:
        messagebox.showinfo("Game information", "It's a tie!")
    else:    
        messagebox.showinfo("Game information", player+" won the game!")
    root.destroy()    
    if messagebox.askyesno("Restart game", "Do you want to play again?"):
        return subprocess.Popen([sys.executable]+sys.argv)

def check_win():
    win_options=[[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for x in win_options:
        if all(element in list(player1_moves.keys()) for element in x):
            end_game("Player 1")
        if all(element in list(player2_moves.keys()) for element in x):
            end_game("Player 2")
    if len(list(player1_moves.keys())) + len(list(player2_moves.keys()))==9:
        end_game(None) #tie

def click(event): 
    button=event.widget
    if str(button) in list(player1_moves.values()) or button in list(player2_moves.values()) or finished:
        return    
    global turn        
    if (not("turn" in globals())) or ("turn" in globals() and turn):
        button.config(image=random_first, width=80, height=80, state=tk.DISABLED)
        button.image=random_first
        turn=False
        button=str(button)
        btn_index=[int(button[-1]) if str(button[-1]).isdigit() else 1 ]        
        player1_moves[btn_index[0]]=button
    else:
        button.config(image=random_second, width=80, height=80, state="disabled")
        button.image=random_second
        turn=True  
        button=str(button)
        k=[int(button[-1]) if str(button[-1]).isdigit() else 1 ]        
        player2_moves[k[0]]=button    
    check_win()    

for row in range(3):
    for col in range(3):
        white=Image.open("D:\\Daniel Rabe\\Downloads\\white.png")
        white_tk=ImageTk.PhotoImage(white)
        btn=tk.Button(root, width=80, height=80, image=white_tk, background="white") 
        btn.image=white_tk
        btn.bind("<Button-1>", click)
        btn.grid(row=row, column=col)

root.mainloop()