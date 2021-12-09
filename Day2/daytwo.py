file = open("input2.txt")
directions=[]
splitDirections=[]

for line in file:
  directions.append(line.rstrip())

for i in directions:
  splitDirections.extend(i.split())

#print(splitDirections)

horizontal = 0
depth = 0
total = 0
aim = 0;

for index in range(0,len(splitDirections)-1):
  if int(index) % 2 != 0: 
    splitDirections[index] = int(splitDirections[index])

#print(splitDirections)

#for i in range(0,len(splitDirections)-1):
#  if splitDirections[i] == 'forward':
#    horizontal = horizontal + int(splitDirections[i+1])
#  elif splitDirections[i] == 'down':
#    depth = depth + int(splitDirections[i+1])
#  elif splitDirections[i] == 'up':
#    depth = depth - int(splitDirections[i+1])

#total = depth * horizontal
#print(total)

for i in range(0,len(splitDirections)-1):
  if splitDirections[i] == 'forward':
    horizontal = horizontal + int(splitDirections[i+1])
    depth = depth + (aim * int(splitDirections[i+1]))
  elif splitDirections[i] == 'down':
    aim = aim + int(splitDirections[i+1])
  elif splitDirections[i] == 'up':
    aim = aim - int(splitDirections[i+1])

total = horizontal * depth
print(total)