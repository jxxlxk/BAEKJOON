a = int(input())

for i in range(a):
  b = int(input())
  if b %2 == 1 or b %2 == -1:
    print(b,'is odd')
  else:
    print(b,'is even')