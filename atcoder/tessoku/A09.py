H, W, N = map(int, input().split())

S = [0 * (W+1) for i in range(H+1)]

for i in range(N):
  a,b,c,d = map(int, input().split())
  S[b-1][a-1] += 1
  S[b-1][c] -= 1
  S[d][a-1] -= 1
  S[d][c] += 1

print(S)