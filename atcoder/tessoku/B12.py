N = int(input())

l = 0
r = N
pos = (l+r) / 2

def F(x):
  return x**3 + x

while True:
  f = F(pos)
  if abs(f - N) <= 0.001:
    break
  if f < N :
    l = pos
  else:
    r = pos
  pos = (l+r) / 2

print(pos)