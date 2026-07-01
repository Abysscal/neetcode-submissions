class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1

        while l<r:
            mid = (r+l) // 2

            if nums[mid] >= nums[r]:
                l = mid + 1
            else:
                r = mid

        # aka lowest
        pivot = l
        res = -1
        l,r = 0, len(nums) -1
        if nums[pivot] <= target <= nums[r]:
            l = pivot
        else:
            r = pivot - 1

        while l<=r:
            mid = (r+l) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            elif nums[mid] == target:
                res = mid
                break

        return res