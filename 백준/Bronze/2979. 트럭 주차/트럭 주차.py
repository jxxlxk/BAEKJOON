a,b,c = map(int,input().split())
f,f1 = map(int,input().split())
s,s1 = map(int,input().split())
t,t1 = map(int,input().split())
k = 0
g = [0]*(max(f1,s1,t1)+1)
for i in range(f,f1):
         g[i]+=1
for i in range(s,s1):
         g[i]+=1
for i in range(t,t1):
         g[i]+=1
for i in range(len(g)):
  if g[i] == 1:
    k += a
  elif g[i] == 2:
    k += b*2
  elif g[i] == 3:
    k += c*3
print(k)