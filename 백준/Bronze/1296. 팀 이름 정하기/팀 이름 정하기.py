a = input()
q = a.count('L')
w = a.count('O')
e = a.count('V')
r = a.count('E')
y = []
name = []

max = -1
for i in range(int(input())):
  dl = input()
  y.append( (((q+w+dl.count('L')+dl.count('O')) *(q+e+dl.count('L')+dl.count('V')) * (q+r+dl.count('L')+dl.count('E')) * (w+e+dl.count('O')+dl.count('V')) * (w+r+dl.count('O')+dl.count('E')) * (e+r+dl.count('V')+dl.count('E'))) % 100))

  name.append(dl)
  if y[i] > max :
    max = y[i]
    team = dl

  elif y[i] == max :
    t1 = list(dl)
    t2 = list(team)
    if t1 < t2 :
      team = dl
print(team) 