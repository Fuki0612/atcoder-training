N = int(input())

out = [0] + [1] * (N-1)

i = 2

while i**2 <= N:
  for j in range(2*i,N+1,i):
    out[j-1] = 0
  i+=1

for i in range(len(out)):
  if out[i]:
    print(i+1)