N, Q = map(int, input().split())
P = list(map(int, input().split()))

last = {}
for i in range(Q):
  a = int(input())
  last[a] = i

P = [p for p in P if p not in last] + sorted(last, key=last.get)

print(*P)