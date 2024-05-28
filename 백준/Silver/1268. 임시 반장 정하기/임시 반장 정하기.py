n = int(input())
st2 = []

for i in range(n):
  st1 = list(map(int,input().split()))
  st2.append(st1)
count = [0]*n
for i in range(n):
  v = [False]*n
  for j in range(5):
    for e in range(n):
      if e!= i and st2[e][j] == st2[i][j]:
         v[e] = True
  count[i] = sum(v)
print(count.index(max(count))+1)  
