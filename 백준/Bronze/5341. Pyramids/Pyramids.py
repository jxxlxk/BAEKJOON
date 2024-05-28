x = []
while 0 not in x:
    x.append(int(input()))
for i in range(len(x)-1):
    m=0
    for j in range(x[i]+1):
        m+=j
    print(m)
             
             
             