from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as tkFont
from game import Game
from inputs import get_gamepad

X_PAD = 75
TEXT_WIDTH = 400
TEXT_HEIGHT = 800


def processingInputs(root, gameList, currentGame, imageLabel):
    for event in get_gamepad():
        print("code: ", event.code, " state: ", event.state)
        if event.code == "ABS_X" and event.state == 255:
            prevGame(gameList, currentGame, imageLabel)
        elif event.code == "ABS_Y" and event.state == 255:
            nextGame(gameList, currentGame, imageLabel)

    root.after(200, lambda:processingInputs(root, gameList, currentGame,
               imageLabel))

    return


def start():
    root = Tk()
    root.title("SUNY Poly Arcade")
    root.geometry("1280x1024")
    root.configure(bg='black')

    fontStyle = tkFont.Font(family="Lucida Console", size=25, underline=True, weight=tkFont.BOLD)

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

    gameImageLabel.grid(row=1, column=2, padx=0, pady=50)

    gameScoreLabel = Label(text="*************HIGHSCORES*************")
    gameScoreLabel.grid(row=1, column=1, padx=0, pady=50, sticky='N')

    root.after(200, lambda:processingInputs(root, gameList, currentGame,
               gameImageLabel))

    print("something")

    root.mainloop()

    return


def nextGame(gameList, currentGame, imageLabel):
    imageLabel.grid_forget()
    currentGame[0] += 1
    if currentGame[0] >= len(gameList):
        currentGame[0] = 0
    imageLabel = Label(image=gameList[currentGame[0]].image)
    imageLabel.grid(row=1, column=2, padx=0, pady=50)

    gameScoreLabel = Label(text="*************HIGHSCORES*************")
    gameScoreLabel.grid(row=1, column=1, padx=0, pady=50, sticky='N')
    return


def prevGame(gameList, currentGame, imageLabel):
    imageLabel.grid_forget()
    currentGame[0] -= 1
    if currentGame[0] < 0:
        currentGame[0] = len(gameList) - 1
    imageLabel = Label(image=gameList[currentGame[0]].image)
    imageLabel.grid(row=1, column=2, padx=0, pady=50)

    gameScoreLabel = Label(text="*************HIGHSCORES*************")
    gameScoreLabel.grid(row=1, column=1, padx=0, pady=50, sticky='N')
    return


start()
