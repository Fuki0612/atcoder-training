T = int(input())
N = int(input())

count = [0] * (T+1)

for i in range(N):
  l, r = map(int, input().split())
  count[l] += 1
  count[r] -= 1

S = [0]
for x in count[:-1]:
  S.append(S[-1] + x)

for i in range(1,T+1):
  print(S[i])




