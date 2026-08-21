
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = [[] for x in range(len(nums))] 
        freq = defaultdict(int)
        res=[]
        for n in nums:
            freq[n] += 1

        #print(freq)
        #print(counts)

        for key in freq:
            counts[freq[key]-1].append(key)

        #print(freq)
        #print(counts)

        for i in range( len(counts)-1, -1, -1):
            for n in counts[i]:
                res.append(n)
                if len(res)==k:
                    return res
        return res