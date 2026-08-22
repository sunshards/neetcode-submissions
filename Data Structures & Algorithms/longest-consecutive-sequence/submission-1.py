
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        pos = {}
        longest_l = 0

        for i in range(len(nums)):
            current = nums[i]
            if current in pos:
                continue 

            left = pos.get(current-1,0)
            right = pos.get(current+1,0)

            pos[current] = right + left + 1
            longest_l = max(longest_l, pos[current])

            pos[current-left] = pos[current]
            pos[current+right] = pos[current]
        return longest_l
        
            
