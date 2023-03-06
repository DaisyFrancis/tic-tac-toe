from tkinter import * #It is the standard Python interface to the Tk GUI toolkit,
import random


def next_turn(row, column):
    global player
    #for having access ouside of the function
    if buttons[row][column]['text'] == "" and check_winner() is False:

       if player == players[0]:
            
           buttons[row][column]['text']=player

           if check_winner() is False:
               player = players[1]
               label.config(text=(players[1]+" Turn"))

           elif check_winner() is True:
               label.config(text=(players[0]+" Wins"))

           elif check_winner() == "Tie":   
               label.config(text="It's a Tie!")
           
           
       else:
            buttons[row][column]['text'] = player
            if check_winner() is False:
               player = players[0]
               label.config(text=(players[0]+" Turn"))

            elif check_winner() is True:
               label.config(text=(players[1]+" Wins"))

            elif check_winner()=="Tie":   
               label.config(text="It's a Tie!")
                   
           
           

def check_winner():

    #for rows
    for row in range(3):
        if buttons[row][0]['text']==buttons[row][1]['text'] == buttons[row][2]['text'] !="":
            buttons[row][0].config(bg="blue")
            buttons[row][1].config(bg="blue")
            buttons[row][2].config(bg="blue")
            return True
    #for column  
        for column in range(3):
            if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
                buttons[0][column].config(bg="blue")
                buttons[1][column].config(bg="blue")
                buttons[2][column].config(bg="blue")
                return True
        
        #for diagonal 
        if buttons[0][0]['text']==buttons[1][1]['text'] == buttons[2][2]['text'] !="":
            buttons[0][0].config(bg="blue")
            buttons[1][1].config(bg="blue")
            buttons[2][2].config(bg="blue")
            return True
        #for diagonal  
        elif buttons[0][2]['text']==buttons[1][1]['text'] == buttons[2][0]['text'] !="":
            buttons[0][2].config(bg="blue")
            buttons[1][1].config(bg="blue")
            buttons[2][0].config(bg="blue")
            return True
        #if tie, bg=yellow
        elif empty_space() is False:
            for row in range(3):
                for column in range(3):
                    buttons[row][column].config(bg="yellow")
            return "Tie"
        else:
            return False
      
    
def empty_space():
    spaces=9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] !="":
                spaces-=1
    if spaces == 0:
        return False 
    else:
        return True           


def new_game():#will launch a new game
    global player
    player=random.choice(players)
    label.config(text=player+" turn")
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="purple")



#creating a window
window=Tk()
#setting title
window.title("Tic-Tac-Toe")
players = ["x","o"]
player = random.choice(players)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]
label = Label(text=player + " turn", font=('consolas',40,"underline"))
label.pack(side="top")
#reset button
reset_button=Button(text="Restart",cursor="plus",font=('consolas',16),command=new_game)#should call the new_game function
reset_button.config(bg="green")
reset_button.pack(side="bottom")
#adding frame to window
frame=Frame(window)
#packing frame
frame.pack()

#nested for-loop for adding buttons
for row in range(3):
    for column in range(3):
        buttons[row][column]=Button(frame,text="",font=('consolas',25),width=8,height=4,
                                    command=lambda row=row,column=column: next_turn(row,column))
        buttons[row][column].grid(row=row,column=column)
#at the end of our program we need to add main loop
window.mainloop()
