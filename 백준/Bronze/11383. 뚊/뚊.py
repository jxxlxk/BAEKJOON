n, m = map(int, input().split())

s1 = []
s2 = []

for i in range(n):
  s1.append(list(input()))

for j in range(n):
  s2.append(list(input()))
flag = True
new = []
for i in range(n):
  for j in range(m):
    new.append(s1[i][j])
    new.append(s1[i][j])
  if new == s2[i]:
    new = []
  else : 
    flag = False
if flag == False:
  print("Not Eyfa")
else:
  print("Eyfa") 