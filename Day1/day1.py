file = open("input1.txt")
count = 0
count2 = 0
depths=[]
threeDepths=[]

for line in file:
    depths.append(int(line.rstrip()))

for i in range(0,len(depths)-1):
  if depths[i] < depths[i+1]:
    count = count + 1
print(count)

for i in range(0, len(depths)-2):
  #print(depths[i])
  #print(depths[i+1])
  #print(depths[i+2])
  threeDepths.append(depths[i] + depths[i+1] + depths[i+2])

#print(threeDepths)

for i in range(0,len(threeDepths)-1):
  if threeDepths[i] < threeDepths[i+1]:
    count2 = count2 + 1
    
print(count2)
