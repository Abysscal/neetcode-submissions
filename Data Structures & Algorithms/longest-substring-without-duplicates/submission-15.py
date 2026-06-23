class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0, 0
        visit = []
        res = 0

        while r < len(s):

            while s[r] in visit:
                visit.pop(0)
                l+=1

            visit.append(s[r])
            r += 1
            if len(visit) > res:
                res = len(visit)
        return res