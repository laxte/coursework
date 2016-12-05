
location = [0,0]
previousLocation = [0,0]
compasDirection = 0 # 0 = N, 1 = E, 2 = S, 3 = w 
visitedLocations = [0,0]

# Compas direction maps to : 0 = N, 1 = E, 2 = S, 3 = w 
def updateDirection(turn, compas):
  if turn == 'R':
	return (compas + 1)%4
  else: # 'L'
     return (compas - 1)%4


def readDirectionLenght(direction):
   value = "" 
   for integer in direction[1:]:
	value = value + integer
   return int(value)
 
def updateVisitedLocations(lenght):
   for x in range(1, lenght+1):
        if (compasDirection == 0):
	   appendToList(location[0],location[1] + x)	
       	if (compasDirection == 1):
	   appendToList(location[0] + x, location[1])		
    	if (compasDirection == 2):
	   appendToList(location[0], location[1] - x)	
 	if (compasDirection == 3):
           appendToList(location[0] - x, location[1])	


def appendToList(x,y):
    if [x,y] in visitedLocations:
       print str([x,y]) + " found in list already"
    visitedLocations.append([x,y])


with open ("input.txt", "r") as myfile:
 
   for line in myfile:
       values = line.split(",") 
       #print values
       for direction in values: 
           direction = direction.strip()
           #print direction
	   compasDirection = updateDirection(direction[0], compasDirection)
	   lenght = readDirectionLenght(direction)    
	   #print compasDirection , " " , lenght
           updateVisitedLocations(lenght)	   
           #print visitedLocations            

	   if (compasDirection == 0):
	        location[1] = location[1] + lenght	
       	   if (compasDirection == 1):
	        location[0] = location[0] + lenght		
    	   if (compasDirection == 2):
	        location[1] = location[1] - lenght	
 	   if (compasDirection == 3):
	        location[0] = location[0] - lenght	
 
	   #print location
