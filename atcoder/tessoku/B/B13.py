N, K = map(int, input().split())
A = list(map(int, input().split())) + [0]

ans = []
j = 0

for i in range(N):
  if j < i : j = i
  while sum(A[i:j+1]) <= K and j <= N-1:
    j += 1
  ans.append(j - i)

print(sum(ans))