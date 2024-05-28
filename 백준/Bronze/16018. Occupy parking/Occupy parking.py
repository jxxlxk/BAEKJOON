a = int(input())
b = []
cnt = 0
c = 'C'
for i in range(2):
  b.append(input())

for i in range(a):
  if b[0][i] == c :
    if b[1][i] == c:
      cnt+=1


print(cnt)