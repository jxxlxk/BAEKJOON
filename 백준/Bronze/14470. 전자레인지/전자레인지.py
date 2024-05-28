temp = int(input())
want = int(input())
icedmeat = int(input())
haedong = int(input())
cook = int(input())

time = 0

if temp > 0:
  print(cook*(want-temp))
else:
  time += abs(temp)*icedmeat
  temp = 0
  time += haedong
  time += cook*want
  print(time)