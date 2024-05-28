a = int(input())
n = list(map(int, input().split()))
m  = list(map(int, input().split()))
m.sort(reverse=True)
n.sort()


b = 0
for i in range(a):
  b+=n[i]*m[i]
print(b)