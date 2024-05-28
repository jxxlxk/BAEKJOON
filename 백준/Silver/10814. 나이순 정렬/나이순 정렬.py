n = int(input())

x = []

for i in range(n):
  x.append(list(input().split()))
x.sort(key = lambda x :int(x[0]))

for i in range(n):
  print(x[i][0]),print(x[i][1])