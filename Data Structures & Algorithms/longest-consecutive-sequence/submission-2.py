class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest_l = 0

        for num in nums:
            if num-1 not in numSet:
                l = 1
                while num+1 in numSet:
                    num = num+1
                    l+=1
                longest_l = max(longest_l, l)
        return longest_l