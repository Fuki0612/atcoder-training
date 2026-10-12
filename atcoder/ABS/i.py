N, Y = map(int, input().split())

for x in range(0,Y//10000+1):
  if 10000*x > Y : break
  for y in range(0,Y//5000+1):
    if 10000*x + 5000*y > Y : break
    if 10000*x + 5000*y + 1000*(N-x-y) == Y :
      print(f"{x} {y} {N-x-y}")
      exit()

print(f"{-1} {-1} {-1}")