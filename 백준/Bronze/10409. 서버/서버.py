a,b = map(int,input().split())
l = list(map(int,input().split()))

for i in range(a):
  if sum(l[:i + 1]) > b:
    print(i) 
    break
    
  elif i == a - 1:
    print(a)