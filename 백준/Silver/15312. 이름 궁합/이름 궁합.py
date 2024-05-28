a = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
b = []

p = input()
k = input()
for i in range(len(p)):
  b.append(a[ord(p[i])-65])
  b.append(a[ord(k[i])-65])
while 1:
  if len(b) <= 2:
    break

  else:
    for i in range(len(b)-1):
      b[i] = (b[i] + b[i+1]) % 10 
    b.pop()

for l in b:
  print(l,end="") 
  
