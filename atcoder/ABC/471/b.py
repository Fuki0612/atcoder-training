from collections import Counter

N = int(input())
S = [input().lower() for _ in range(N)]
c = Counter(S).most_common(1)

print(c[0][1])