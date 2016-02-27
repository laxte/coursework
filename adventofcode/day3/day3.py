#a=[100,200,300,400,500]
#def search(b):
# try:
#  k=a.index(b)
#  return a[k] 
# except ValueError:
#    return 'not found'
#print(search(500))

#list = [[0,0],[1,0],[1,1],[0,1]]

match = 0
unique_s = [] 
position = [0,0]

with open ("input.txt", "r") as myfile:
  data = myfile.read()

unique_s.append(position)

print "data length:" + str(len(data)) 
for c in data:
  if c == '>':
    position = [position[0] + 1 ,position[1]]
  elif c == '<':
    position = [position[0] - 1,position[1]]
  elif c == '^':
    position = [position[0],position[1] + 1]
  elif c == 'v':
   position = [position[0],position[1] - 1]
  else:
    print c
  #print position

  #for square in list:
  try:
    match = next(obj for obj in unique_s if (obj[0] == position[0] and obj[1] == position[1]))
   # print match
  except StopIteration:
    #print 'not found'
    unique_s.append(position)


print len(unique_s)

