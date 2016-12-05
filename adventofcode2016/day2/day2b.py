#    1
#  2 3 4
#5 6 7 8 9
#  A B C
#    D

matrix = [[0,0,1,0,0],
	  [0,2,3,4,0],
	  [5,6,7,8,9],
	  [0,10,11,12,0],
	  [0,0,13,0,0]]

def moveOnKeyPad(direction, location):
   if direction == 'U': 
      if location[0] > 0 and matrix[location[0]-1][location[1]] != 0:
         location[0] -= 1
   if direction == 'D':
      if location[0] < 4 and (matrix[location[0]+1][location[1]] != 0):
	 location[0] += 1
   if direction == 'L':
      if location[1] > 0 and (matrix[location[0]][location[1]-1] != 0):
          location[1] -= 1
   if direction == 'R':
      if location[1] < 4 and matrix[location[0]][location[1]+1] != 0:
	 location[1] += 1


with open ("input.txt", "r") as myfile:
 
   for line in myfile:
       location = [2,0]
       for direction in line:
	  moveOnKeyPad(direction, location)

       print matrix[location[0]][location[1]]
       print location
       print "new line" 
