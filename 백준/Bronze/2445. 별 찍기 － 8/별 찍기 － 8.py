a  =int(input())

for i in range(a):
  
  print(((i+1)*('*')) + ((' ')*((a*2)-((i+1)*2))) + ((i+1)*("*")))

for i in range(a-1,0,-1):
  print((i*("*")) + ((a*2-i*2)*(" ")) + (i*("*")) )
