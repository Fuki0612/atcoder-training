N = int(input())
A = list(map(int, input().split()))

a = b = c = 0

for i in range(N):
  oturi = (-A[i]) % 1000    
  c += oturi // 100
  oturi %= 100
  b += oturi // 10
  oturi %= 10
  a += oturi

print(a,b,c)