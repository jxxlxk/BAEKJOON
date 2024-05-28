day =  [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week =  ["SUN","MON", "TUE", "WED", "THU", "FRI", "SAT"]

a,b = map(int,input().split())
x = 0

for i in range(a-1):
  x += day[i]

x+=b

if x <= 6:
  if x == 1:
    print('MON')
  elif x == 2:
    print("TUE")
  elif x == 3:
    print("WED")
  elif x == 4:
    print("THU")
  elif x == 5:
    print("FRI")
  elif x == 6:
    print("SAT")

else:
  print(week[x%7])
