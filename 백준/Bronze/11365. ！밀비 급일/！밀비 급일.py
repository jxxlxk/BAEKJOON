l = []
while True:
  a = input()
  l.append(a)
  if a == 'END':
    break
l.remove("END")
for i in range(len(l)):
  b = ''
  a = l[i]
  for i in range(len(a)-1,-1,-1):
    b += a[i]
  print(b)  