class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0

        for num in numSet:
            if num-1 not in numSet:
                tempBig = 0
                incre = 0
                while num+incre in numSet:
                    tempBig += 1
                    incre += 1
                res = max(res, tempBig)
        return res