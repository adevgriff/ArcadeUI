#imports cvs to allow program to read .cvs score file
import csv

#initializes the high score class
class HighScore:

    #takes in the input for the class
    def __init__(self, listSize):
        #stores int for number of top scores displayed
        self.listSize = listSize

    #opens the high scores file
    with open("./highscores.csv", 'r') as file:
        #creates lists
        scores = []
        ordered = []

        #reads through each line in the file
        csv_reader = csv.reader(file)
        for row in csv_reader:
            #places row number input into scores list
            nums = row
            #converts the row input into ints
            nums = [int(x) for x in nums]
            scores.append(nums)

        #rearranges order of numbers into ordered list
        ordered = sorted(scores)
        ordered.reverse()
        #print(ordered)

        #creates window to display top 5 high scores
        import tkinter as tk
        window = tk.Tk()
        window.title("High Scores")

        for element in ordered:
            for item in element:
                items = item
                #reads the scores onto a window
                greeting = tk.Label(text=(item))
                greeting.pack()

        window.mainloop()