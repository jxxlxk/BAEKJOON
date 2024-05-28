a =  int(input())
h = []
for i in range(a):
  h.append(int(input()))

h.sort()
t = len(h)
for i in range(len(h)):
  h.append(h[i]*(t-i))

print(max(h))