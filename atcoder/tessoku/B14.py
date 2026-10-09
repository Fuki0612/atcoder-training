N, K = map(int, input().split())
A = list(map(int, input().split()))

zenhan = A[:N//2]
kouhan = A[N//2:]

zenhan_S = [0]
kouhan_S = [0]

for x in zenhan:
  t = []
  for arr in zenhan_S:
    t.append(x + arr)
  zenhan_S += t
zenhan_S = set(zenhan_S)

for x in kouhan:
  t = []
  for arr in kouhan_S:
    t.append(x + arr)
  kouhan_S += t
kouhan_S = set(kouhan_S)

for x in zenhan_S:
  if K - x in kouhan_S:
    print('Yes')
    exit()

print('No')