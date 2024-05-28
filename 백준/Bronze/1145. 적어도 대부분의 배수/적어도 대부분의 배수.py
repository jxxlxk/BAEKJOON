a,b,c,d,e = map(int,input().split())
g = min(a,b,c,d,e)
l = [a,b,c,d,e]
count = 0

while 1:
  for i in l:
    if g % i == 0:
      count += 1
  if count >= 3:
    break
  else:
    g += 1
    count = 0
print(g)    
