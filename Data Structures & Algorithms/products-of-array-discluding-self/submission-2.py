class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero = 1,0

        for num in nums:
            if num:
                prod *= num
            else:
                zero += 1
        
        if zero > 1: return [0] * len(nums)

        res = [0] * len(nums)
        for i,c in enumerate(nums):
            if zero:
                if c:
                    res[i] = 0
                else:
                    res[i] = prod
            else:
                res[i] = prod//c
        return res          
