a,b= map(int,input().split())
h =list(map(int,input().split()))
h.sort()

for i in range(a):
  if h[i] <=b:
    b+=1
  else:
    break
    
print(b)