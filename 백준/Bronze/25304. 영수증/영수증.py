real = 0
x = int(input())
n = int(input())
for i in range(n):
  a,b = map(int,input().split())
  real = real + a * b
if real == x:
  print('Yes')
else:
  print('No')