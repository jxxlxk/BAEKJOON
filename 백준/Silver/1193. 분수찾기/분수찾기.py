n = int(input())
line = 1

while n > line :
  n -= line
  line += 1

if line % 2 == 0 :
  bunja = n
  bunmo = line - n + 1

else :
  bunja = line - n + 1
  bunmo = n

print(bunja, '/', bunmo ,sep = "")

