class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} #value -> index

        for i,n in enumerate(nums):
            diff = target-n
            if diff in prevMap:
                # the diff will always be smaller than current
                return [prevMap[diff], i]
            prevMap[n] = i