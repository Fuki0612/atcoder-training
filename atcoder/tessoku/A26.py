Q = int(input())
out = []
primelist = [2]

def isPrime(i):
  k = 2
  while k**2 <= i:
    if i % k == 0:
      return False
    k += 1
  return True

for i in range(Q):
  x = int(input())
  if x in primelist:
    out.append('Yes')
  elif isPrime(x):      
      out.append('Yes')
      primelist.append(x)
  else:
    out.append('No')

print("\n".join(map(str, out)))