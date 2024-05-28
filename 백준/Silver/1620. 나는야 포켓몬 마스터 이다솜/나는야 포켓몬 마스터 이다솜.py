import sys
input = sys.stdin.readline

dict1 = {}
a,b = map(int,input().split())
for i in range(a):
  c = input().rstrip()
  dict1[c] = str(i+1)
  dict1[str(i+1)] = c
for i in range(b):
  d = input().rstrip()
  print(dict1[d])
  