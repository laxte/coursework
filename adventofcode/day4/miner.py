import md5

loop = True
integer = 0

while (integer < 1050000):
  m = md5.new()
  m.update("bgvyzdsv" + str(integer))
  md5sum = m.hexdigest()
  if md5sum[0:5] == "00000":
    print md5sum 
    loop = False
    print integer
  integer += 1


