
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        output = []

        for n in nums:
            freq[n] += 1
        heap = []
        for key in freq:
            # We maintain a heap of size k to have more efficient heap operations since we don't need any more info
            if len(heap) < k:
                heapq.heappush( heap, (freq[key], key) )
            else:
                heapq.heappushpop(heap, (freq[key], key) )
        for i in range(k):
            t = heapq.heappop(heap)
            output.append(t[1])
        return output