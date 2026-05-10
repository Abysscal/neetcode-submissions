class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = set()

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in visited:
                return [nums.index(diff), i]
            visited.add(nums[i])