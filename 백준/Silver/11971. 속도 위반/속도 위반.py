n, m = map(int, input().split())

a = []
b = []

for i in range(n) :
  doro, sokdo = map(int, input().split())
  for j in range(doro) :
    a.append(sokdo)

for i in range(m):
  doro, sokdo = map(int, input().split())
  for j in range(doro) :
    b.append(sokdo)

big = 0
for i in range(100) :
  if b[i] - a[i] > big:
    big = b[i] - a[i]
print(big) 