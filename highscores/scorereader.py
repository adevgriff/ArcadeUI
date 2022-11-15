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

    #give(# of items, # of those items that are on the top, # index of rest of numbers)
    def give(self, items, top, index):
        #initializes count variable
        count = 0
        #generates new lists
        topn = []
        vertop = []
        rest = []

        #appends new list of top n numbers
        for i in range(items):
            topn.append(self.scores[i])

        #gets top n items of topn list
        for i in range(top):
            vertop.append(topn[i])

        #gets the index of the rest of the items
        for i in range(index,items):
            rest.append(topn[i])

        #print(topn)
        #print(vertop)
        #print(rest)

        #creates list from other lists
        final = []
        final.append(vertop)
        final.append(rest)

        #appends -1 to list to make final list equal in length to final
        for i in range(top+index, items):
            final.append([-1])

        #print(final)
        return final

def doStuff():
    high = HighScore("highscores.csv", 7)
    #high.getList()
    topl = []

    topl = high.give(10,3,5)
    print(topl)
    return 0

doStuff()
