import Mason_Snow_stats

#Open Files
file = open("500DayFruitData.txt", "r") 

data = file.read().splitlines()

#Remove title line
data.pop(0)
#Loop to go through the list 
bananas = []
strawberrys = []
apples = []
for day in data:
  temp = day.split()

  if temp[1] == "apple":
    apples.append(int(temp[2]))
  elif temp[1] == "banana":
    bananas.append(int(temp[2]))
  elif temp [1] == "strawberry":
    strawberrys.append(int(temp[2]))

#print(apples)
    
    
 #Takes string and creates a list
bananasmean = Mason_Snow_stats.mean(bananas)
bananasmedian = Mason_Snow_stats.median(bananas)
applesmean = Mason_Snow_stats.mean(apples)
applesmedian = Mason_Snow_stats.median(apples)
strawberrysmean = Mason_Snow_stats.mean(strawberrys)
strawberrysmedian = Mason_Snow_stats.median(strawberrys)
print("Median:", applesmedian)
print("Mean:", applesmean)

with open("Mason_Snow_Output.txt", "w")as f:
  f.write("Apples Mean: "+str(applesmean) + "\n "+ "Apples Median: "+str(applesmedian))

  #The n gaurentees line
  
  f.write("\n " "Bananas Mean: "+str(bananasmean) + "\n " + "Bananas Median: "+str(bananasmedian))
  f.write("\n " "Strawberries Mean: "+str(strawberrysmean) + "\n "+ "Strawberries Median: "+str(strawberrysmedian))
