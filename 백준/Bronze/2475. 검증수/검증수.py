a = list(map(int,input().split()))
c = 0
for i in range(5):
    c += a[i] * a[i]
print(c%10)   
    
   