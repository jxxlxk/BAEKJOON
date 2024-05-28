import sys
input = sys.stdin.readline

a,b = map(int,input().split())
h = []
count = 0 
for i in range(a):
  h.append(int(input()))

for i in range(len(h)):
  for j in range(i, len(h)):
    if i != j :
      if h[i] + h[j] <= b:
        count+=1


print(count) 