from collections import deque

H,W = map(int, input().split())

coord = []
for i in range(H):
  coord.append(input())

score = [[0] * W for _ in range(H)]
score[0][0] = 1

for i in range(H):
  for j in range(W):
    for nh,nw in ((i+1,j),(i,j+1)):
      if 0 <= nh and nh <= H-1 and 0 <= nw and nw <= W-1:
        if coord[nh][nw] == '.':
          if nh == 0 :
            score[nh][nw] = score[nh][nw-1]
          elif nw == 0:
            score[nh][nw] = score[nh-1][nw]
          else:
            score[nh][nw] = score[nh][nw-1] + score[nh-1][nw]

print(score[-1][-1])