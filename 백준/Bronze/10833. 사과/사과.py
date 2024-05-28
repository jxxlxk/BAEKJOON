a = int(input())
x = 0
for i in range(a):
  n,m = map(int,input().split())
  x+=m%n
print(x)  