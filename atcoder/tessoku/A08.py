H, W = map(int, input().split())
masu = []
S = [[0] * (W+1) for _ in range(H+1)]    

for i in range(H):
  x = list(map(int, input().split()))
  masu.append(x)
                                                                         
for i in range(1, H+1):
  row = masu[i-1]
  for j in range(1, W+1):
    S[i][j] = S[i][j-1] + S[i-1][j] - S[i-1][j-1] + row[j-1]

Q = int(input())

ans = []
for _ in range(Q):
  A,B,C,D = map(int, input().split())
  ans.append(S[C][D] - S[A-1][D] - S[C][B-1] + S[A-1][B-1])

for i in range(Q): 
  print(ans[i])