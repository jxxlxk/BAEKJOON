a = int(input())
b = list(map(int,input().split()))
num  = []
for i in range(a):
  if b[i] not in num:
    num.append(b[i])
num.sort()
print(*num)