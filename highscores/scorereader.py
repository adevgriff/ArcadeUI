#imports cvs to allow program to read .cvs score file
import csv

#initializes the high score class
class HighScore:
    num=0

    #takes in the input for the class
    def __init__(self, fileName, ninput):
        self.num = ninput

        #opens the high scores file
        with open(fileName, 'r') as file:
            #creates lists
            self.scores = []

            #reads through each line in the file
            csv_reader = csv.reader(file)
            for row in csv_reader:
                #places row number input into scores list
                nums = row
                #converts the row input into ints
                nums = [int(x) for x in nums]
                self.scores.append(nums)

            #rearranges order of numbers into ordered list
            self.scores.sort()
            self.scores.reverse()

    def getList(self):
        #prints the list in range
        for i in range(self.num):
            print(self.scores[i])

def doStuff():
    high = HighScore("highscores.csv", 7)
    high.getList()
    return

doStuff()
