import sys
input = sys.stdin.readline

z = int(input())
m = []

for i in range(z):
  n = []
  a,b,c,d = input().split()
  n.append(int(d))
  n.append(int(c))
  n.append(int(b))
  n.append(a)
  m.append(n)
m.sort()
print(m[z-1][3])
print(m[0][3])
  