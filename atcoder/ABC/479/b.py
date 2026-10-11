N = int(input())
S = input()

ans = 0
renzoku = 0

for i in range(N):
  if S[i] == 'R':
    renzoku += 1
    ans = max(ans,renzoku)
  else:
    renzoku = 0

print(ans)