a = int(input())
for i in range(a):
  b = input()
  h = b[::-1]
  b = int(b)
  h = int(h)
  b +=h
  b = str(b)

  if b == b[::-1]:
    print('YES')
  else:
    print('NO')