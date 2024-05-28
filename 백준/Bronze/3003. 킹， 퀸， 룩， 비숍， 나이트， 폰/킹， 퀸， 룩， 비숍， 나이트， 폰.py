ans = [1,1,2,2,2,8]
a = input().split()
for i in range(6):
    ans[i] = ans[i]-int(a[i])
print(ans[0],ans[1],ans[2],ans[3],ans[4],ans[5])    