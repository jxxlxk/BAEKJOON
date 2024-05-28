a,b,c = map(int, input().split())

box = []
box.append(a)
box.append(b)
box.append(c)

box.sort()
print(box[1])