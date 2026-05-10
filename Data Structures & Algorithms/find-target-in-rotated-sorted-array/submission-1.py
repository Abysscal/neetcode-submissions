class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1

        while l<r:
            mid = (r+l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        pivot = l
        l, r = 0, len(nums) - 1
        if target >= nums[pivot] and target <= nums[r]:
            l = pivot
        else:
            r = pivot -1

        while l<=r:
            mid = (r+l) // 2
            if target < nums[mid]:
                r = mid-1
            elif target > nums[mid]:
                l= mid + 1
            else:
                return mid

        return -1