from tkinter import *
from PIL import ImageTk, Image


class Game:
    def __init__(self, name, exec_path, image_path, highScore_path):
        self.name = name
        self.exec_path = exec_path
        self.image = ImageTk.PhotoImage(Image.open(image_path))
        self.highScore_path = highScore_path
        self.previousGame = self
        self.nextGame = self

    def display(self):

        return

    def start(self):
        return

    def setPointers(self, prev, next):
        self.previousGame = prev
        self.nextGame = next
        return
