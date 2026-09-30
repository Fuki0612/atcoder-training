import heapq

N = int(input())
A = list(map(int, input().split()))

heap = A[:3]
heapq.heapify(heap)
ans = [heap[0]]

for i in range(3, N):
  heapq.heappush(heap, A[i])
  heapq.heappop(heap)  
  ans.append(heap[0])

print("\n".join(map(str, ans)))