
def isAValidTriangle(sideLenghts):
   sideLenghts = list(map(int, sideLenghts))
   sideLenghts.sort()
   return sideLenghts[0] + sideLenghts[1] > sideLenghts[2]
