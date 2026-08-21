
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        output = []
        for n in nums:
            freq[n] += 1
        heap = []
        for key in freq:
            heap.append( (-freq[key], key) )
        heapq.heapify(heap)
        for i in range(k):
            t = heapq.heappop(heap)
            output.append(t[1])
        return output