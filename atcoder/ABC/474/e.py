T = int(input())

out = []
for i in range(T):
  N = int(input())
  AB = [tuple(map(int, input().split())) for _ in range(N)]

  d = sorted((a - b for a, b in AB), reverse=True)
  sA = sum(a for a, b in AB)
  minA = min(a for a, b in AB)

  ans = sA
  pre = 0
  for k in range(1, N+1):
    pre += d[k-1]
    ans = min(ans, sA - pre + minA * max(0, 2*k - N))

  out.append(ans)

print("\n".join(map(str, out)))