class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()

        for i in range(len(nums)):
            #print(i)
            # The number in spot i is the center
            l=i-1
            r=i+1

            while l>-1 and r<len(nums):
                total = nums[i]+nums[l]+nums[r]
                #print(l,i,r,total)
                if total == 0:
                    triplet = [nums[l],nums[i],nums[r]]
                    if triplet not in triplets:
                        triplets.append(triplet)
                    l-=1
                    r+=1
                elif total < 0:
                    r+=1
                elif total > 0:
                    l-=1
            
        return triplets

