grading_scale =  {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0}
tot = 0
scre = 0
for i in range(20):
  g,p,a = input().split()
  for j in range(20):
    if a == 'P':
      continue
    tot += float(p)*grading_scale[a]
    scre += float(p)
print(float(tot)/scre)