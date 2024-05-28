a, b, c = map(int, input().split())

burgers = list(map(int, input().split()))
sides = list(map(int, input().split()))
drinks = list(map(int, input().split()))

tot = sum(burgers) + sum(sides) + sum(drinks)
print(tot)

burgers.sort(reverse = True)
sides.sort(reverse = True)
drinks.sort(reverse = True) 

home = 0
ty = 0

for i in range(min(a,b,c)):
  home += (burgers[i] + sides[i] + drinks[i])*0.9
  ty += (burgers[i] + sides[i] + drinks[i])

home += tot-ty


print(int(home))