n = int(input())
b = 10
while n>b:
    if n%b>=b//2:
        n+=b
    n = n-(n%b)    
    b = b*10
print(n)