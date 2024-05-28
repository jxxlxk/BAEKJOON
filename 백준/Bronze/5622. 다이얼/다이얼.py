a = input().lower()
d = {2:('a','b','c'),3:('d','e','f'),4:('g','h','i'),5:('j','k','l'),6:('m','n','o'),7:('p','q','r','s'),8:('t','u','v'),9:('w','x','y','z')}
ans = 0
for i in a:
    for j in d:
        if i in d[j]:
            ans += j+1
print(ans)            