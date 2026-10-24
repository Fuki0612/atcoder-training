N, K = map(int, input().split())
A = list(map(int, input().split()))

if A[0] == K:
  out = 1
else:
  out = 0

for i in range(N-1):
  if A[i+1] == K:
    out += 1
    continue
  under = min(A[i],A[i+1])
  upper = max(A[i],A[i+1])
  if under < K and K < upper:
    out += 1

print(out)