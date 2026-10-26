from collections import deque

N, M, S, T = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
  a, b = map(int, input().split())
  G[a].append(b)

INF = float('inf')
dist = [INF] * (N+1)
dist[S] = 0
dq = deque([S])

while dq:
  u = dq.popleft()
  if not G[u]:
    continue
  m = min(G[u])
  for v in G[u]:
    if v == m:
      w = 0
    else:
      w = 1
    if dist[u] + w < dist[v]:
      dist[v] = dist[u] + w
      if w == 0:
        dq.appendleft(v)
      else:
        dq.append(v)

print(dist[T] if dist[T] < INF else -1)