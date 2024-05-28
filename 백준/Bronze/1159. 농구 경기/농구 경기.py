a  = int(input())
x = []
f = []

scam =[]
for i in range(a):
  a = input()
  x.append(a[0])


b = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in range(26):
  if x.count(b[i]) >= 5:
    f.append(b[i])

if f == scam:
  print('PREDAJA')
else:
  print(''.join(f))