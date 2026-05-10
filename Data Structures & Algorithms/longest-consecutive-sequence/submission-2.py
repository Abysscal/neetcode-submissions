class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = set(nums)
        nums = sorted(nums)
        nums = list(nums)

        max = 0
        count = 0
        for i in range(len(nums)):
            if i == 0:
                count += 1
            else:
                if (nums[i-1] + 1) == nums[i]:
                    count += 1
                else:
                    if count > max:
                        max = count
                    count = 1
        if count > max:
            max = count
        return max