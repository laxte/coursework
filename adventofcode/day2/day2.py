# surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. 

length = 0
width = 0
height = 0
paper = 0
ribbon = 0
with open ("input1.txt", "r") as myfile:
  for line in myfile:
    line = line.rstrip('\n')
    surfaces = []
    dimensions = line.split('x')
    lenghts = []
    length = int(dimensions[0])
    width = int(dimensions[1])
    height = int(dimensions[2])
    surfaces.append(2*length*width)
    surfaces.append(2*width*height)    
    surfaces.append(2*height*length)
    lenghts.append(length)
    lenghts.append(width)
    lenghts.append(height)
    print lenghts
    lenghts.sort()
    print lenghts   
    ribbon_t = 2*lenghts[0] + 2*lenghts[1] + (lenghts[0]*lenghts[1]*lenghts[2]) 
    ribbon += ribbon_t
    surface=surfaces[0] + surfaces[1] + surfaces[2]
    paper_per_box = surface + (min(surfaces)/2)
    paper += paper_per_box
    print paper
    print ribbon
