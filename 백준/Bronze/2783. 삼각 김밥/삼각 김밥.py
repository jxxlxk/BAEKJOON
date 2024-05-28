a,b = map(int,input().split())
c = int(input())
t = []
t.append(a/b*1000)



for i in range(c):

  f,j = map(int,input().split())

  t.append(f/j*1000)



t.sort()



print(round(t[0],2))    