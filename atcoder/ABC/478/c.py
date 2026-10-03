N, K = map(int, input().split())
A = list(map(int, input().split()))
sortA = sorted(A)

if A == sortA:
  print('Yes')
  exit()    

l = r = 0
flagl = flagr = True
for i in range(N):
  if flagl == False and flagr == False:
    break 
  if A[i] != sortA[i] and flagl:
    l = i
    flagl = False
  if A[-1-i] != sortA[-1-i] and flagr:
    r = i
    flagr = False

if l + r + K >= N:
  print('Yes')
else:
  print('No')