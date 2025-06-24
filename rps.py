import sys
import random
import time
from tkinter import *

playerChoice = None
lastPlayerMove = None

#####################################################################
#GUI
#####################################################################
window = Tk() 
window.geometry("500x500")
window.title("Rock, Paper, Scissors")

icon = PhotoImage(file='jashIcon.png')
window.iconphoto(True, icon)


window.config(background="#B2B1CF")
#####################################################################

#images
photo = PhotoImage(file = 'jashIcon.png')
photoS = PhotoImage(file = 'scissors.png')
photoP = PhotoImage(file = 'paper.png')
photoR = PhotoImage(file = 'rock.png')

#labels
labelPlayer = Label(window,
                    text="You", 
                    font=('Comic Sans MS',20,'bold'), 
                    fg='#e1f2fe',
                    bg='#49392c',
                    relief=RAISED,
                    bd=10,
                    padx=20,
                    pady=20,
                    image = photo,
                    compound='top')
labelPlayer.place(x=50, y=0)

labelComputer = Label(window,
                      text="Computer", 
                      font=('Comic Sans MS',20,'bold'), 
                      fg='#e1f2fe',
                      bg='#49392c',
                      relief=RAISED,
                      bd=10,
                      padx=20,
                      pady=20,
                      image = photo,
                      compound='top')
labelComputer.place(x=450, y=0)

# Computer's move image (starts empty)
computerImageLabel = Label(window, bg="#B2B1CF")
computerImageLabel.place(x=450, y=400)

# Result label
resultLabel = Label(window, text="", font=("Comic Sans MS", 16, "bold"),
                    fg="white", bg="#B2B1CF")
resultLabel.place(x=180, y=50)






###################################################################################
#Game Logic
#####################################################################

#Helper fun
def choice_to_word(choice):
    return {1: "Rock", 2: "Paper", 3: "Scissors"}.get(choice, "Unknown")

def get_image_for_choice(choice):
    return {1: photoR, 2: photoP, 3: photoS}.get(choice)

#The game
def play_rps():
    global playerChoice, lastPlayerMove

    if playerChoice is None:
        return
    


     #Basic AI
    aiChoice = random.choice([1, 2, 3])

    if aiChoice == 1: #chooses counter to player's last move
        if lastPlayerMove == 1:
            computer = 2 # rock > scissors
        elif lastPlayerMove == 2:
            computer = 3 # scissors > paper
        elif lastPlayerMove == 3:
            computer = 1 # rock > scissors
        else:
            computer = random.choice([1, 2, 3])
    elif aiChoice == 2: # chooses the "losing move" to the player's last move
        if lastPlayerMove == 1:
            computer = 3 
        elif lastPlayerMove == 2:
            computer = 1 
        elif lastPlayerMove == 3:
            computer = 2 
    else: #chooses the same as the player's last move
        if lastPlayerMove == 1:
            computer = 1
        elif lastPlayerMove == 2:
            computer = 2
        elif lastPlayerMove == 3:
            computer = 3
    


    

    lastPlayerMove = playerChoice

    # Update computer's image
    computerImageLabel.config(image=get_image_for_choice(computer))

    player = playerChoice

    if player == 1 and computer == 3 or \
        player == 2 and computer == 1 or \
        player == 3 and computer == 2:
        result = "You win!"
    elif player == computer:
        result = "Tie!"
    else:
        result = "AI wins!"

    resultLabel.config(text=f"You chose {choice_to_word(player)}.\nAI chose {choice_to_word(computer)}.\n{result}")

#Button funcs
def scissors1click():
    global playerChoice
    playerChoice = 3
    play_rps()

def paper1click():
    global playerChoice
    playerChoice = 2
    play_rps()

def rock1click():
    global playerChoice
    playerChoice = 1
    play_rps()

#Playerbuttons
scissorsButton= Button(window,
                    bg="#b2b1cf",
                    image = photoS)
scissorsButton.config(command=scissors1click)
scissorsButton.place(x = 50, y = 230)

paperButton= Button(window,
                    bg="#b2b1cf",
                    image = photoP)
paperButton.config(command=paper1click)
paperButton.place(x = 50, y = 330)

rockButton= Button(window,
                    bg="#b2b1cf",
                    image = photoR)
rockButton.config(command = rock1click)
rockButton.place(x = 50, y = 430)








window.mainloop() 

'''
lastPlayerMove = None #track the player's last move

while True: 

    playerChoice = input("Enter...\n 1 for Rock, 2 for Paper,\n 3 for Scissors, or 4 to exit\n\n")

#Handling user input code
    if not playerChoice.isdigit():
        print("Invalid input, please enter a number.\n")
        continue

    player = int(playerChoice)

    if player == 4:
       sys.exit("Goodbye!")

    if player < 1 or player > 3:
        print("You must enter 1, 2, or 3")
        continue

#Basic AI chooses the counter to the user's last move
    print("...")
    time.sleep(1)

    if lastPlayerMove is None:
        computerChoice = random.choice("123")
    else:
        if lastPlayerMove == 1:
            computerChoice = "2"
        elif lastPlayerMove == 2:
            computerChoice = "3"
        elif lastPlayerMove == 3:
            computerChoice = "1"

    computer = int(computerChoice)

#update playerMove
    lastPlayerMove = player

    print("")
    print("You chose " + playerChoice + ".\n")
    time.sleep(2)
    print("Python chose " + computerChoice + ".\n")
    print("")

    time.sleep(1)

#Game Logic
    if player == 1 and computer == 3:
        print("You win!")
    elif player == 2 and computer == 1:
        print("You win!")
    elif player == 3 and computer == 2:
        print("You win!")
    elif player == computer:
        print("Tie!")
    else:
        print("Python wins!")

    print("")
'''