a,b = map(int,input().split())
c = a*b

while b:
    if a>b:
        b,a = a,b
    b = b%a
    
print(c//a)   
    
    