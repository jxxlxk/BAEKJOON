N = int(input())
cards = set(   map(int,  input().split())   )
M = int(input())
sample = list(   map(int,  input().split())   )


for i in sample:
  if i in cards:
    print(1,end = ' ')
  else:
    print(0,end = ' ')
    