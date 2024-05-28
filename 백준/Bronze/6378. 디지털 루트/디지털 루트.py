import sys
input = sys.stdin.readline

while True:
  a = int(input())

  if a == 0 :
    break

  while 1 :
    a = sum(list(map(int, str(a))))

    if (a // 10) == 0:
      print(a)
      break 