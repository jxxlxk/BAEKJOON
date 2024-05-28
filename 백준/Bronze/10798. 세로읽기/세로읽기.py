a = []
for i in range(5):
  a.append(input())

for i in range(max(len(j) for j in a)):
  for j in range(5):
    if i < len(a[j]):
      print(a[j][i], end = '') 