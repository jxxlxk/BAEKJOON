import sys

input = sys.stdin.readline
g = [0]*10000
a = int(input())
for i in range(a):
  k = int(input())
  g[k-1]+=1

for i in range(len(g)):
  if g[i] != 0:
    for j in range(g[i]):
        print(i+1)