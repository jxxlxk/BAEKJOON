d = int(input())
homesickness = []
hyangsubyeog = []

for i in range(d):
  want_to_go_home = 0
  dl = input()
  dlg,dlgk = map(int,input().split())
  while 1:
    if dlgk-dlg < 0:
      break
    else:
      want_to_go_home += 1
      dlgk-=dlg
      dlgk += 2
  homesickness.append(want_to_go_home) 
  hyangsubyeog.append(dl)


print(sum(homesickness))
print(hyangsubyeog[homesickness.index(max(homesickness))])