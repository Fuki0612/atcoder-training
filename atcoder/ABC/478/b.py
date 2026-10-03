N, V = map(int, input().split())
W = list(map(int, input().split()))

ans = 0
for i in range(N):
  for j in range(N):
    if i == j : continue
    for k in range(N):
      if i == k or j == k : continue
      if i + j + k + 3 <= V and ans < W[i] + W[j] + W[k]:
        ans = W[i] + W[j] + W[k]

print(ans)