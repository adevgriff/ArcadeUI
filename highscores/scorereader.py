#imports cvs to allow program to read .cvs score file
import csv

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
    print(ordered)