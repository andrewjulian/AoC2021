import numpy as np

# store random values as a randomArray ------------------------------------------------------

input4 = open("input4.txt")
data = input4.read()
bingoNums = data.split('\n', 1)[0]

bingoNumsArray = bingoNums.split(",")

print(bingoNumsArray)
print(" ")

# creates an array of arrays with each index as a grid ---------------------------------------
otherValues = []
otherValues = data.split("\n")
#print(otherValues)

for item in otherValues:
    if item == "":
        otherValues.remove(item)

""" otherValuesNP = np.array(otherValues)
otherValuesNP[0:6]
print(otherValuesNP) """

for i in range(1,len(otherValues)-1,5):
    print(otherValues[i:i+5])

""" 

def divide_chunks(l, n):
      
    # looping till length l
    for i in range(0, len(l), n): 
        yield l[i:i + n]

otherValuesArray = list(divide_chunks(otherValues, 6))
print(otherValuesArray)

# create separate 2D arrays for each grid ---------------------------------------------------



#removes space at beginning of bingo card
for i in range(0,len(otherValuesArray)-1):
    otherValuesArray[i].pop(0)

otherValuesArray = otherValuesArray[:-1]

#removes last item which was just an empyt set
#print(otherValuesArray)

#creates bingo cards from array items in sets of 5

# evaluate each table for values in randomArray using [][] and nested for loops
    # change value to 0 if found, otherwise leave value as is
    # include test(s) to determine if a winning row or column is found

# total the values remaining in teach 2D array (for each table)
# multiply the board sum total and mulitply by winning number from randomArray """