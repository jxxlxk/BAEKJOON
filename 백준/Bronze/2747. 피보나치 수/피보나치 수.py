a = int(input())
n = 0
m = 1
if a <= 2:
  print(1)
else:
  for i in range(a-1):
     x = n+m
     n =m
     m = x
  print(x)