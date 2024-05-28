a = int(input())
n = 1000 - a
count = 0
count += n // 500
count += n % 500 // 100
count += n % 500 % 100 // 50
count += n % 500 % 100 % 50 // 10
count += n % 500 % 100 % 50 % 10 //5 
count += n % 500 % 100 % 50 % 10 % 5 // 1
print(count)