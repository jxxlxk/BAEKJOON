n = int(input())

for i in range(n) :
  A, B = map(int,input().split())
  n1 = A
  n2 = B

  n = 1
  while n != 0 :
    n = n1 % n2
    n1 = n2
    n2 = n
    
  print(int(A * B / n1)) 