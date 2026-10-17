from collections import defaultdict

N, M = map(int, input().split())
names = []

for i in range(N):
  S = input()
  names.append(S)

out = {x:0 for x in names}

pat = defaultdict(list)
for S in names:
  for j in range(len(S)):
    pat[S[:j] + '?' + S[j+1:]].append(S)

for i in range(M):
  T = input()
  if T in out.keys():
    out[T] += 1
    continue
  ans = ""
  for j in range(len(T)):
    kouho = T[:j] + '?' + T[j+1:]
    if kouho in pat.keys():
      if len(pat[kouho]) > 1:
        ans = ""
        break
      if ans == "":
        ans = pat[kouho][0]
      elif ans != pat[kouho][0]:
        ans = ""
        break
  if ans != "":
    out[ans] += 1

for k,v in out.items():
  print(v)