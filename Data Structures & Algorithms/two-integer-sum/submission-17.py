class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twodict = {}

        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in twodict:
                return [twodict[diff], i]
            twodict[nums[i]] = i
        