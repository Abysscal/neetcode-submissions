class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        res = []
        numSorted = sorted(nums)
        for i in range(len(numSorted)):
            l,r = 0, len(numSorted)-1
            if l == i:
                l+=1
            if r == i:
                r-= 1
            while l<r and l>=0 and r< len(numSorted):
                if l == i:
                    l += 1
                    continue
                if r == i:
                    r -= 1
                    continue
                if numSorted[i] + numSorted[l] + numSorted[r] == 0:
                    if sorted([numSorted[i], numSorted[l], numSorted[r]]) not in res:
                        res.append(sorted([numSorted[i], numSorted[l], numSorted[r]]))
                    l+=1
                    continue
                if numSorted[i] + numSorted[l] + numSorted[r] > 0:
                    r -= 1
                    continue
                if numSorted[i] + numSorted[l] + numSorted[r] < 0:
                    l += 1
                    continue

        return res