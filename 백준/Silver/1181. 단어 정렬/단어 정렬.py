word = []

for i in range(int(input())):
  word.append(input())
new_word = list(set(word))

new_word.sort(key = lambda x : (len(x), x))

for i in new_word :
  print(i) 