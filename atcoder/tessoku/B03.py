N = int(input())
A = list(map(int, input().split()))

for x in range(N-2):
  for y in range(x+1,N-1):
    if A[x] + A[y] > 1000:
      continue
    for z in range(y+1,N):
      if A[x] + A[y] + A[z] == 1000:
        print('Yes')
        exit()

print('No')