class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        combos = {}
        for i in range(len(nums)):
            if not nums[i] in combos:
                combos[target-nums[i]] = i
            else:
                return [ combos[nums[i]] ,i]
        