unique_locations = [] 
santa_location = [0,0]
robo_location = [0,0]
start_location = [0,0]
even = True

def isNotVisited(location, unique_s):
  try:
    next(obj for obj in unique_s if (obj[0] == location[0] and obj[1] == location[1]))
    return False 
  except StopIteration:
    return True


def updateLocation(location, c):
  if c == '>':
    location = [location[0] + 1 ,location[1]]
  elif c == '<':
    location = [location[0] - 1,location[1]]
  elif c == '^':
    location = [location[0],location[1] + 1]
  elif c == 'v':
   location = [location[0],location[1] - 1]
  else:
    print c
  return location

# main function

with open ("input.txt", "r") as myfile:
  directions = myfile.read()

unique_locations.append(start_location)

for direction in directions:
   
  if even:
    santa_location=location = updateLocation(santa_location, direction)
    even = False
  else:
    robo_location=location = updateLocation(robo_location, direction)
    even = True

  if isNotVisited(location, unique_locations):
    unique_locations.append(location)

# Ouput how many locations received at least one present   
print len(unique_locations)

