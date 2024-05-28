a = int(input())

for i in range(a):
  ans = ''
  b = []
  n,m = input().split()
  n = int(n)
  for j in m:
    ans+=j*n
  print(ans)  