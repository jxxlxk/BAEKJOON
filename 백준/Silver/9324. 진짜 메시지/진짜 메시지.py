a = int(input())

for p in range(a):
  check = True
  al = [0]*26
  b = input()

  for j in range(len(b)):
    al[ord(b[j]) - 65] += 1

    if al[ord(b[j])-65] == 3:
      if j < len(b) - 1 and b[j] != b[j + 1] :
        check = False
        print("FAKE")
        break

      if j == len(b) - 1 :
        check = False
        print("FAKE")
        break
    if al[ord(b[j]) - 65] == 4 :
      al[ord(b[j]) - 65] = 0

  if check == True :
    print("OK")