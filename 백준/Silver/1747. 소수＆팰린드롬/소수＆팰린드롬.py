import sys
input = sys.stdin.readline
a = int(input())

if a <= 2 :
  print(2)

else : 
  while True :
    b = str(a)
    l = []
    if b == b[::-1] :
      for i in range(2, a) :
        if a % i == 0:
          l.append(i)
          break
      if len(l) == 0 :
        print(a)
        break
    a += 1 
