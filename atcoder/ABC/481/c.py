Q = int(input())
db = {}
count = 1
out = []

for i in range(Q):
  query = input()
  if query not in db:
    db[query] = count
    count += 1
  out.append(db[query])

print("\n".join(map(str, out)))