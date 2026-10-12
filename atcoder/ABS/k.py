N = int(input())

last = (0,0,0)

for i in range(N):
  t,x,y = map(int, input().split())
  move = abs(x-last[1]) + abs(y-last[2])
  if (t - last[0] - move) >= 0 and (t - last[0] - move) % 2 == 0:
    last = (t,x,y)
  else:
    print('No')
    exit()

print('Yes')