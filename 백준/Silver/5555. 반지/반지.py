a = input()
s = int(input())
count = 0
for i in range(s):
  g = input()
  h = g+g
  if a in h:
    count +=1

print(count)