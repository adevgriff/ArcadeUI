from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as tkFont
from game import Game
from inputs import get_gamepad

X_PAD = 75
TEXT_WIDTH = 400
TEXT_HEIGHT = 800


def processingInputs(root, gameList, currentGame, imageLabel, nameLabel):
    events = get_gamepad()
    for event in events:
        print(event.code, " , ", event.state)
        if event.code == "ABS_X" and event.state == 255:
            prevGame(gameList, currentGame, imageLabel, nameLabel)

    root.after(200, lambda: processingInputs(root, gameList, currentGame,
               imageLabel, nameLabel))
    return


def start():
    root = Tk()
    root.title("SUNY Poly Arcade")
    root.geometry("1280x1024")
    root.configure(bg='black')

    fontStyle = tkFont.Font(family="Lucida Console",
                            size=25, underline=True, weight=tkFont.BOLD)

    # Joystick

    # bind keys

    # open games.csv
    gamesFile = open("games.csv", 'r')

    gameList = []
    for line in gamesFile:
        properties = line.split(',')
        if (len(properties) > 3):
            gameList.append(
                Game(properties[0], properties[1], properties[2], properties[3]))

    currentGame = []
    currentGame.append(0)

    gameImageLabel = Label(image=gameList[currentGame[0]].image)
    gameNameLabel = Label(text=gameList[currentGame[0]].name)

    gameNameLabel.grid(row=0, column=1, columnspan=4, padx=X_PAD, pady=25)
    gameImageLabel.grid(row=1, column=2, padx=0, pady=50)

    gameScoreLabel = Label(text="*************HIGHSCORES*************")

    gameScoreLabel.grid(row=1, column=1, padx=0, pady=50, sticky='N')

    nextButton = Button(root, text=">>", command=lambda: nextGame(
        gameList, currentGame, gameImageLabel, gameNameLabel))

    prevButton = Button(root, text="<<", command=lambda: prevGame(
        gameList, currentGame, gameImageLabel, gameNameLabel))

    nextButton.grid(row=1, column=3)
    prevButton.grid(row=1, column=0)

    root.after(0, lambda: processingInputs(root, gameList, currentGame,
               gameImageLabel, gameNameLabel))

    root.mainloop()

    return


def nextGame(gameList, currentGame, imageLabel, nameLabel):
    imageLabel.grid_forget()
    nameLabel.grid_forget()
    currentGame[0] += 1
    if currentGame[0] >= len(gameList):
        currentGame[0] = 0
    imageLabel = Label(image=gameList[currentGame[0]].image)
    nameLabel = Label(text=gameList[currentGame[0]].name)
    nameLabel.grid(row=0, column=1, columnspan=3, padx=X_PAD, pady=25)
    imageLabel.grid(row=1, column=1, padx=X_PAD, pady=50)
    return


def prevGame(gameList, currentGame, imageLabel, nameLabel):
    imageLabel.grid_forget()
    nameLabel.grid_forget()
    currentGame[0] -= 1
    if currentGame[0] < 0:
        currentGame[0] = len(gameList) - 1
    imageLabel = Label(image=gameList[currentGame[0]].image)
    nameLabel = Label(text=gameList[currentGame[0]].name)
    nameLabel.grid(row=0, column=1, columnspan=3, padx=X_PAD, pady=25)
    imageLabel.grid(row=1, column=1, padx=X_PAD, pady=50)
    return


start()
