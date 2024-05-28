count = 0
for i in range(8):
  a = input()
  for j in range(8):
    if (i+j) % 2 == 0 and a[j] == 'F':
      count += 1
print(count)      