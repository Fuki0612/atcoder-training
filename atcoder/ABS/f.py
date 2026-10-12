N,A,B = map(int, input().split())

def Sum(num):
  t = num
  ret = t % 10
  while t // 10 > 0:
    t //= 10
    ret += t % 10
  return ret

out = 0

for i in range(1,N+1):
  count = Sum(i)
  if count >= A and count <= B :
    out += i

print(out)