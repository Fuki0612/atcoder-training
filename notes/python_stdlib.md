# 競プロで使える Python ライブラリメモ

## bisect（ソート済みリストの二分探索）

```python
from bisect import bisect_left, bisect_right
a = [1, 3, 3, 5]
bisect_left(a, 3)   # 1: a[j] >= 3 となる最小の j
bisect_right(a, 3)  # 3: a[j] > 3 となる最小の j
bisect_right(a, 3) - bisect_left(a, 3)  # 3 の個数
```

- 用途: 「x 以上で最小の要素」「x 以下の個数」「区間内に要素があるか」
- 計算量: O(log N)
- 注意: `insort` / `list.insert` は挿入が O(N)．要素を追加し続ける用途では TLE しやすい
- 使用例: ABC477 C（KMP の出現位置から l 以上で最小のものを探す）

## heapq（最小ヒープ）

```python
import heapq
h = []
heapq.heappush(h, x)      # 追加 O(log N)
heapq.heappop(h)          # 最小を取り出す O(log N)
h[0]                      # 最小を参照 O(1)
heapq.heapify(a)          # リストをヒープ化 O(N)
heapq.heappushpop(h, x)   # push してから pop（1回で速い）
```

- 最大ヒープにしたいときは `-x` を入れる
- タプルを入れると先頭要素で比較: `heappush(h, (dist, v))`（ダイクストラ）
- 典型: 「上位 K 個を保つ」→ サイズ K の最小ヒープで，K を超えたら pop．K 番目に大きい値は `h[0]`
- 使用例: ABC476 C（各時点で 3 番目に大きい値）