class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nMap = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nMap:
                return [nMap[diff], i]
            nMap[nums[i]] = i