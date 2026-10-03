N, K = map(int, input().split())

ans = 0
for x in range(1,N+1):
  for y in range(1,x+1):
    z = K - x - y
    if z <= 0:
      break
    if 1 <= z and z <= y:
      if x == y and y == z : ans += 1
      elif x == y or y == z : ans += 3
      else : ans += 6

print(ans)