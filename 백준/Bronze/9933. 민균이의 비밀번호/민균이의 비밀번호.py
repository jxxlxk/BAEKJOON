a = int(input())
g = []
for i in range(a):
  g.append(input())
for i in range(a):

  q = g.count(g[i][::-1])
  if q == 1:
    
    print(len(g[i]))
    print(g[i][len(g[i])//2])
    break