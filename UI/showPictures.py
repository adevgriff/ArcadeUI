from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("SUNY Poly Arcade")

#Get the games from the gamedev team and store them in a list
#Show the first game using a grid
gameImage1 = ImageTk.PhotoImage(Image.open("UI\\GameImages\\game1.jpg"))
gameImage2 = ImageTk.PhotoImage(Image.open("UI\\GameImages\\game2.jpg"))
gameImage3 = ImageTk.PhotoImage(Image.open("UI\\GameImages\\game3.jpg"))
gameImage4 = ImageTk.PhotoImage(Image.open("UI\\GameImages\\game4.jpg"))
gameList = [gameImage1, gameImage2, gameImage3, gameImage4]
showGame = Label(image = gameList[0])
showGame.grid(row = 0, column = 1)

#This function is to show the next game in the list
def nextGamef(imagePos):
    global showGame
    global nextGame
    global previousGame

    showGame.grid_forget()
    showGame = Label(image = gameList[imagePos - 1])
    showGame.grid(row = 0, column = 1)
    nextGame = Button(root, text = ">>", command=lambda : nextGamef(imagePos + 1))
    previousGame = Button(root, text = "<<", command = lambda : previousGamef(imagePos - 1))
    #The next button is disabled if we are at the end of the list
    if imagePos == len(gameList):
        nextGame = Button(root, text = ">>", command=lambda : nextGamef(imagePos + 1), state = DISABLED)
        
    nextGame.grid(row = 0, column = 3)
    previousGame.grid(row = 0, column = 0)
    
#This function is to show the previous game in the list
def previousGamef(imagePos):
    global showGame
    global nextGame
    global previousGame
    showGame.grid_forget()
    showGame = Label(image = gameList[imagePos - 1])
    showGame.grid(row = 0, column = 1)
    nextGame = Button(root, text = ">>", command=lambda : nextGamef(imagePos + 1))
    previousGame = Button(root, text = "<<", command = lambda : previousGamef(imagePos - 1))
    #The previous button is disabled if we are at the beginning of the list
    if imagePos == 0:
         previousGame = Button(root, text = "<<", command = lambda : previousGamef(imagePos - 1), state = DISABLED)
        
    nextGame.grid(row = 0, column = 3)
    previousGame.grid(row = 0, column = 0)
    
#Shows the default buttons
nextGame = Button(root, text = ">>", command=lambda : nextGamef(2))
previousGame = Button(root, text = "<<", command = lambda : previousGamef(2))
nextGame.grid(row = 0, column = 3)
previousGame.grid(row = 0, column = 0)


root.mainloop()