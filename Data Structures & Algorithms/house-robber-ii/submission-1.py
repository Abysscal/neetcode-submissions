class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def findNums(nums):
            rob1, rob2 = 0,0
            # [0,1,2]
            for n in nums:
                robNew = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = robNew
            return rob2
        
        return max(nums[0],findNums(nums[1:]), findNums(nums[:-1]))