
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

        i=len(counts)-1
        while(k>0 and i>=0):
            while counts[i] != []:
                res.append(counts[i][0])
                del counts[i][0]
                k-=1
            i-=1


        return res