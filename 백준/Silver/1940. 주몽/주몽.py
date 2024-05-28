a = int(input())
b = int(input())

total = 0

n = list(map(int,input().split()))

for i in range(a):
  for j in range(a-1,0,-1):
    if n[i] == n[j]:
      break
    else:
      if n[i] + n[j] == b:
        total+=1


print(total)