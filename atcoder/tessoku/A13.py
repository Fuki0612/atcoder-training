N, K = map(int, input().split())
A = list(map(int, input().split())) + [0]

j = 0
i = 0

ans = []
while i < N-1:
  if i == j : j += 1
  if A[j] - A[i] <= K and j <= N-1:
    j += 1
  else:
    ans.append(j - i - 1)
    i += 1

print(sum(ans))