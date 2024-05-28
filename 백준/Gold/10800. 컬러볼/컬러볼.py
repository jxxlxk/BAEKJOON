a = int(input())
b = []
for i in range(a):
  c,s = map(int,input().split())
  b.append([s,c,i])
b.sort()
j = 0
total = 0 
ans = [0] * a
color = [0] * (a+1)
for i in range(a):
  f = b[i]
  s = b[j]
  while s[0] < f[0] : 
    total += s[0]
    color[s[1]] += s[0]
    j += 1
    s = b[j]
  ans[f[2]] = total - color[f[1]]    

for i in range(a):
  print(ans[i])