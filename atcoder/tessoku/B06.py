N = int(input())
A = list(map(int, input().split()))
win_sum = [0]
lose_sum = [0]

for a in A:
  if a == 1:
    win_sum.append(win_sum[-1] + 1)
    lose_sum.append(lose_sum[-1])
  else:
    win_sum.append(win_sum[-1])
    lose_sum.append(lose_sum[-1] + 1)

Q = int(input())

for i in range(Q):
  l,r = map(int, input().split())
  win = win_sum[r] - win_sum[l-1]
  lose = lose_sum[r] - lose_sum[l-1]
  if win == lose:
    print('draw')
  elif win > lose:
    print('win')
  else:
    print('lose')