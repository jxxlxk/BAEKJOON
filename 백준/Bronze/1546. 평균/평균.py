a = int(input())
b = list(map(int, input().split()))
m = 0
n = 0
for i in range(a):
  if b[i] > m:
    m = b[i]
for i in range(a):
  n = n + b[i]/m*100/len(b)
print(n)