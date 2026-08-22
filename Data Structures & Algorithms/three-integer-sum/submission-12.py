class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()

        # threesum = a + b + c. We fix a and 
        # do TwoSum II on the subarray without a.

        for i,a in enumerate(nums):
            # since nums is sorted and we want to skip duplicate
            # we can just keep going if the number is equal to the one
            # on the left.

            if i>0 and a == nums[i-1]:
                continue
            
            l=i+1 # We already checked all the combinations for previous numbers
            r=len(nums)-1
            while l<r:
                b = nums[l]
                c = nums[r]
                threesum = a + b +c
                
                if threesum > 0:
                    r-=1
                elif threesum < 0:
                    l+=1
                else:
                    l+=1
                    triplets.append([a,b,c])
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
        return triplets
            