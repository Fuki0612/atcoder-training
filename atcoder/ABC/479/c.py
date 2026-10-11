N, W = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]

subsets = [(0, 0)]

for a, b in items:
  subsets += [(sw + b, sv + a) for sw, sv in subsets]

print(max(sv for sw, sv in subsets if sw <= W))