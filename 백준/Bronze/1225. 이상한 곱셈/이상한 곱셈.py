a,b = input().split()
tot = 0
for i in range(len(b)):
  for j in range(len(a)):
    tot += int(b[i]) * int(a[j])


print(tot)