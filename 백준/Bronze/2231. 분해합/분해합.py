import sys
input = sys.stdin.readline

a = int(input())
i = 0
while 1:
  g = 0
  i += 1
  i = str(i)
  for j in range(len(i)):
    g += int(i[j])
  g+=int(i)
  if g == a:
    
    print(i)
    break
  elif int(i)>a:
    print(0)
    break
    

  else:
    i = int(i)
