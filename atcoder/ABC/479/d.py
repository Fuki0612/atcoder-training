N,Q = map(int, input().split())

INF = float('inf')
L = [INF] + list(map(int, input().split()))
R = list(map(int, input().split())) + [INF]

out = []

LL = [INF] * (N)
RR = [INF] * (N)

RR[0] = R[0]
LL[-1] = L[-1]

sufL = [INF] * (N+2)
preR = [INF] * (N+1)

for i in range(N-1, -1, -1):
  sufL[i] = min(L[i], sufL[i+1])

for i in range(N):
  preR[i+1] = min(preR[i], R[i])  

for i in range(N):
  LL[i] = min(L[i], R[i] + sufL[i+1])
  RR[i] = min(R[i], L[i] + preR[i])


out = []
for i in range(Q):
  s,t = map(int, input().split())
  if s < t:
    out.append(RR[s-1])
  else:
    out.append(LL[s-1])

print("\n".join(map(str, out)))