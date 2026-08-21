class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        prod_nozero = 1
        count_zeroes = 0
        for n in nums:
            if n != 0:
                prod_nozero *= n
            else:
                count_zeroes += 1
        if count_zeroes == 1:
            prod = 0
        elif count_zeroes > 1:
            prod = 0
            prod_nozero = 0
        else:
            prod = prod_nozero

        output = []
        for n in nums:
            if n == 0:
                output.append(int(prod_nozero))
            else:
                output.append(int(prod/n))
        return output