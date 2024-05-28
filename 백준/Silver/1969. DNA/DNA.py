a,b = map(int,input().split())
g = []
ans = []
tot = 0
for i in range(a):
  g.append(input())

for i in range(b):
  A,T,G,C = 0,0,0,0
  for j in range(a):
    if g[j][i] == "A":
      A+=1
    elif g[j][i] == "T":
      T+=1
    elif g[j][i] == "G":
      G+=1
    else:
      C+=1
  wow = ['A',A,'C',C,'G',G,'T',T]
  y = A+T+G+C - max(A,T,G,C)
  ans.append(wow[wow.index(max(A,T,G,C))-1])
  tot += y

print(''.join(ans))
print(tot)