N, M = map(int, input().split())

ans = [M // N] * N

for i in range(M % N):
  ans[i] += 1

for i in range(N):
  print(ans[i])