S = input()

for i in range(len(S) * 2 - 1):
  if i % 2 == 0 :
    print(S[i//2], end="")
  else:
    print('o', end="")

print("")