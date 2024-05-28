up,down,hei = map(int,input().split())
if (hei-down)%(up-down) == 0:
  print((hei-down)//(up-down))
else:
  print((hei-down)//(up-down)+1)