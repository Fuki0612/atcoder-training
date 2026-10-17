N, K, T = map(int, input().split())
A = sorted(map(int, input().split()))

cur = 0
out = 0

for a in A:
  if a >= T:
    break
  if a > cur:
    c = -(-(a - cur) // K)
    out += c
    cur += c * K
  cur = max(cur, a + K)

if cur < T:
  out += -(-(T - cur) // K)

print(out)