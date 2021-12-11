# store random values as a randomArray ------------------------------------------------------
""" >>> f = open('myfile.txt')
>>> data = f.read()
>>> # I'm assuming you had the above before asking the question
>>> first_line = data.split('\n', 1)[0] """

input4 = open("input4.txt")
data = input4.read()
bingoNums = data.split('\n', 1)[0]

bingoNumsArray = bingoNums.split(",")

print(bingoNumsArray)
print(" ")



# creates an array of arrays with each index as a grid ---------------------------------------
otherValues = []
otherValuesArray = []

otherValues = data.split("\n")
otherValues.remove(otherValues[0])

#print(otherValues)
def divide_chunks(l, n):
      
    # looping till length l
    for i in range(0, len(l), n): 
        yield l[i:i + n]

otherValuesArray = list(divide_chunks(otherValues, 6))
print(otherValuesArray)

# create separate 2D arrays for each grid ---------------------------------------------------



# evaluate each table for values in randomArray using [][] and nested for loops
    # change value to 0 if found, otherwise leave value as is
    # include test(s) to determine if a winning row or column is found

# total the values remaining in teach 2D array (for each table)
# multiply the board sum total and mulitply by winning number from randomArray

