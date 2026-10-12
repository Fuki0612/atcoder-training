S = input()

words = ["dream", "dreamer", "erase", "eraser"]

while S:
  for w in words:
    if S.endswith(w):
      S = S[:-len(w)]
      break
  else:
    print('NO')
    exit()

print('YES')