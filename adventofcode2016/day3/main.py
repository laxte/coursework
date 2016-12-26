import day3

validTriangles = 0

with open ("input.txt", "r") as myfile:

   for line in myfile:
      sides = line.split()
      if day3.isAValidTriangle(sides):
         validTriangles += 1

print validTriangles
