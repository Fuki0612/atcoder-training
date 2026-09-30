"""
  KMP法
  https://daeudaeu.com/kmp/

  文字列Sの中に部分文字列Tを含むかを考える．
  返り値としてSのindexの中からTの開始位置を返す．（0-indexed，昇順，重なりも含む）
  計算量: O(|S| + |T|)

  使用例: 区間 [l, r]（1-indexed）にTが含まれるか（ABC477 C）
    from bisect import bisect_left
    pos = kmp(S, T)
    j = bisect_left(pos, l-1)
    ok = j < len(pos) and pos[j] <= r - len(T)
"""

def kmp(s, t):
  m = len(t)
  fail = [0]*(m+1)
  fail[0] = -1
  k = -1
  for i in range(m):
    while k >= 0 and t[k] != t[i]:
      k = fail[k]
    k += 1
    fail[i+1] = k

  res = []
  r = 0
  for i in range(len(s)):
    while r >= 0 and (r == m or t[r] != s[i]):
      r = fail[r]
    r += 1
    if r == m:
      res.append(i - m + 1)
  return res
