a = input()
i =  0
g = []

while i < len(a):
  if a[i] in ('a','e','i','o','u'):
    g.append(a[i])
    i+=3
  else:
    g.append(a[i])
    i+=1
print(''.join(g))