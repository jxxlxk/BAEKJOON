mex = 0
count = 0
for i in range(10):
  a,b = map(int,input().split())
  count -= a
  count += b
  if count > mex:
    mex = count
print(mex)    