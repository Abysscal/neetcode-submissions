class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums = set(nums)
        nums = list(nums)

        for i in range(len(nums)):
            if (nums[i]-1) not in nums:
                length = 1
                while nums[i]+length in nums:
                    length += 1
                res = max(res, length)
        
        return res
