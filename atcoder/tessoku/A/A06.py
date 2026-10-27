N, Q = map(int, input().split())
A = list(map(int, input().split()))
S = [0]
for a in A:
  S.append(S[-1] + a)

for i in range(Q):
  l, r = map(int, input().split())
  print(S[r] - S[l-1])
