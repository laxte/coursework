

#123
#456
#789


with open ("input.txt", "r") as myfile:
 
   for line in myfile:
       location = [1,1]
       for direction in line: 
 	  #print direction
	  if direction == 'U':
	      if location[1] > 0:
		 location[1] -= 1
          if direction == 'D':
	      if location[1] < 2:
		 location[1] += 1
          if direction == 'L':
	      if location[0] > 0:
		 location[0] -= 1
          if direction == 'R':
	      if location[0] < 2:
		 location[0] += 1

       print location 
