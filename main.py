from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as tkFont
from game import Game


def start():
    myGame = Game("game1", "exe path", "UI/GameImages/game1.jpg", "hs path")
    myGame.display()
    return


start()