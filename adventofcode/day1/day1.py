with open ("input.txt", "r") as myfile:
  data=myfile.read()

count = 0
opened = 0
closed = 0

for char in data:

  count+=1
  if char == '(':
    opened+=1
  if char == ')':
    closed+=1

  if (opened-closed) == -1:
    print count
