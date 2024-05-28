b = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
c = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
a = input().upper()


mi = 0
mc = 0
max_ = 0
for w in a:
  for i in range(26):
     if w == b[i]:
       c[i] += 1

       
for i in range(26):
  if c[i] > max_:
    max_ = c[i]
    mi = i
    mc = 1
  elif c[i] == max_:
    mc += 1
if mc > 1:
  print('?')
else:  
  print(b[mi])    