m,row,col = 0,0,0

for i in range(9):
  a = list(map(int,input().split()))
  for j in range(9) : 
    if a[j] > m : 
      m = a[j]
      row = i
      col = j
  
print(m)
print(row+1,col+1)