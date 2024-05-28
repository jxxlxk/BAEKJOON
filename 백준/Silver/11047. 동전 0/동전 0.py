N,K = map(int,input().split())
b = []
for i in range(N):
  b.append(int(input()))

count = 0
for i in b[::-1] : 
  count += K // i
  K %= i
print(count)