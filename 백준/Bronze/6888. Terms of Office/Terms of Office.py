a = int(input())
b = int(input())

v = b-a

print('All positions change in year',a)

for i in range(1,v//60+1):
  
  print('All positions change in year',(a+i*60))