# AtCoder / Coding Test Training

就活のコーディング試験対策用リポジトリ。AtCoder（ABC/ARC等）やコーディングテストの過去問・頻出アルゴリズムを整理する。

## 構成

```
atcoder/
  abc/        # AtCoder Beginner Contest ごとの解答（例: abc300/a.py）
  arc/
templates/    # 頻出アルゴリズムのテンプレート集
  union_find.py
  segment_tree.py
  bfs_dfs.py
  binary_search.py
  dp_examples.py
notes/        # 詰まった問題・典型パターンのメモ
```

## 進捗管理

| 分野 | 状況 |
|---|---|
| 全探索・累積和 | 未着手 |
| DP | 未着手 |
| グラフ（BFS/DFS） | 未着手 |
| Union-Find | 未着手 |
| 二分探索 | 未着手 |
| セグメント木 | 未着手 |

## 方針

- 解いた問題はディレクトリに追加し、コミットログを解答履歴として残す
- 頻出アルゴリズムはtemplates/に汎用実装として蓄積し、本番で使い回せるようにする
- 詰まった問題は notes/ に典型パターンとしてまとめる
