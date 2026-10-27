import heapq

Q, V = map(int, input().split())
h = []
out = []

for _ in range(Q):
  S = list(map(int, input().split()))
  if S[0] == 1:
    t, w = S[1], S[2]
    heapq.heappush(h, -(w - t))
  else:
    T = S[1]
    if not h:
      out.append(-1)
    else:
      key = -heapq.heappop(h)
      out.append(min(V, key + T))

print("\n".join(map(str, out)))