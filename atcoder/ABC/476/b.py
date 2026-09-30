N = int(input())

S = input()
T = input()

for i in range(N):
  if S[i] != T[i] and T[i] != '*':
    print('No')
    exit()

print('Yes')
