m = 0
mini = float('inf')
a = int(input())
d = list(map(int,input().split()))
p = list(map(int,input().split()))
for i in range(a-1):
  if p[i] < mini:
    mini = p[i]
  m += d[i] * mini
print(m)