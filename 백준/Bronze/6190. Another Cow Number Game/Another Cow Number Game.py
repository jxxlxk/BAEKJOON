a = int(input())
b = 0

while a > 1:
  
  if a % 2 == 0:
    a = a// 2
    b+=1
  else:
    a = a*3+1
    b+=1
  

print(b)