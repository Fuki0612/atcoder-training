D = int(input())
N = int(input())

X = [0] * (D+2)

for i in range(N):
  l, r = map(int, input().split())
  X[l] += 1
  X[r+1] -= 1

S = [0]

for x in X:
  S.append(S[-1] + x)

for s in S[2:-1]:
  print(s)