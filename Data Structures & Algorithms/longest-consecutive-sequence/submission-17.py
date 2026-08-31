class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        finalres = 0
        for i in nums:
            res = 1
            if i-1 not in nums:
                while i+res in nums:
                    res += 1
            
            finalres = max(finalres, res)
        return finalres
