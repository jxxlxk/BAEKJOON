a = int(input())
b = [] 
for i in range(a):
    b.append(int(input()))

for i in range(a):
    for j in range(a-1):
      if b[j] > b[j+1]:
        b[j],b[j+1] = b[j+1],b[j]
for i in b : 
  print(i) 
