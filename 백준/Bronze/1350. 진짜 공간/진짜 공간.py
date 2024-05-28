a = int(input())
tot = 0
b = list(map(int,input().split()))
n = int(input())
for i in range(a):
  if b[i] == 0:
    tot += 0
  else:
    if b[i] % n == 0:
      tot += b[i] // n *n
    else:  
      tot += (b[i] // n+1)*n


print(tot)