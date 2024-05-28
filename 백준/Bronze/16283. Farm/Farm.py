a,b,c,d = map(int,input().split())
l = []
for i in range(1,c):
  if i*a+(c-i)*b ==d:

    l.append([i,c-i])
if len(l) != 1:
  print(-1)
else:  
    print(l[0][0],l[0][1])
    
    