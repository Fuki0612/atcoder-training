A,B = map(int, input().split())

if A < B:
  y = B
  x = A
else:
  y = A
  x = B

while y % x != 0:
  t = y % x
  y = x
  x = t

print(A*B//x)