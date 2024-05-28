a = int(input())
l = set()
count = 0
for i in range(a):
  x = input()
  if x == "ENTER":
    l = set()
  else:
    if x not in l:
      count += 1
      l.add(x)
  
print(count)
