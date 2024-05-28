n = int(input())
for i in range(n):
  x = [0,0,0,0]
  a = int(input())
  x[0] += a//25
  a = a%25
  x[1] += a//10
  a = a%10
  x[2] += a//5
  a = a%5
  x[3] += a//1
  a = a%1
  print(*x)  