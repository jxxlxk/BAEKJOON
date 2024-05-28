q,w,e = map(int,input().split())
a,s,d = map(int,input().split())

fin = []
h = q/a
j = w/s
k = e/d



x = min(h,j,k)

nn = []

nn.append(q-a*x)
nn.append(w-s*x)
nn.append(e-d*x)

print(*nn)

