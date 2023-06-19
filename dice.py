from tkinter import *
import random

from PIL import Image,ImageTk 
root=Tk()

root.title("dice")
root.geometry("600x600")

img=ImageTk.PhotoImage(Image.open("dice1.4.jpg"))

player1=Label(root,text="player1")
player1.place(relx=0.1,rely=0.4,anchor=CENTER)

player2=Label(root,text="player2")
player2.place(relx=0.9,rely=0.4,anchor=CENTER)

score1=Label(root,text="score of player 1:")
score1.place(relx=0.1,rely=0.5,anchor=CENTER)

score2=Label(root,text="score of player 2:")
score2.place(relx=0.9,rely=0.5,anchor=CENTER)

turn=Label(root,text="turn of :")
turn.place(relx=0.5,rely=0.5,anchor=CENTER)

player1score=0
def rolldice1():
    global player1score
    r1=random.randint(1,6)
    turn["text"]="player 2's turn , random number = "+str(r1)
    player1score=player1score+r1
    score1["text"]=str(player1score)

player2score=0
def rolldice2():
    global player2score
    r2=random.randint(1,6)
    player2score=player2score+r2
    score2["text"]=str(player2score)
    turn["text"]="player 1s turn, random number= "+str(r2)
    
btn1=Button(root,image=img,command=rolldice1)
btn1.place(relx=0.1,rely=0.7,anchor=CENTER)

btn2=Button(root,image=img,command=rolldice2)
btn2.place(relx=0.9,rely=0.7,anchor=CENTER)

root.mainloop()