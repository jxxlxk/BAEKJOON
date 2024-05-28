a = int(input())
for i in range (a):
    result = "*"
    count = 0
    while(count<i):
        result = result + "*"
        count = count + 1
    print(result)