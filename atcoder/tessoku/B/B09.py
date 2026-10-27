N = int(input())

S = [[0] * 1501 for i in range(1501)]

for i in range(N):
  a,b,c,d = map(int, input().split())
  S[b][a] += 1
  S[d][a] -= 1
  S[b][c] -= 1
  S[d][c] += 1

for y in range(1501):
  for x in range(1,1501):
    S[y][x] += S[y][x-1]

for x in range(1501):
  for y in range(1,1501):
    S[y][x] += S[y-1][x]

out = 0
for y in range(1500):
  for x in range(1500):
    if S[y][x] > 0 : out += 1

print(out)