import sys
input = sys.stdin.readline



a,b = map(int,input().split())
z = []
x = list(input().split())
y = list(input().split())
for i in range(len(x)):
  z.append(x[i])
for i in range(len(y)):
  z.append(y[i])
 
for i in range(len(z)):
  z[i] = int(z[i])
z.sort()
print(*z)