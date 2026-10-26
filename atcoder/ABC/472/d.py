from collections import deque

H, W, K = map(int, input().split())

coord = []

for i in range(H):
  coord.append(input())

r = [0] * H
c = [0] * W

for i in range(H):
  for j in range(W):
    if coord[i][j] == '#':
      r[i] += 1
      c[j] += 1

point = deque([])
d = [[-1] * W for _ in range(H)]

for i in range(H):
  for j in range(W):
    if r[i] == 0 and c[j] == 0:
      d[i][j] = 0
      point.append([i,j])

ans = 0

while point:
  i, j = point.popleft()
  if  d[i][j] <= K :
    ans += 1
  for ni,nj in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
    if 0 <= ni and ni <= H-1 and 0 <= nj and nj <= W-1:
      if coord[ni][nj] == '.' and d[ni][nj] == -1:
        d[ni][nj] = d[i][j] + 1
        point.append([ni,nj])

print(ans)
