class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        l,r = 0,1
        wind = s[l:r]
        length=1
        while r < len(s):
            if s[r] not in wind:
                r+=1
                wind = s[l:r]
            else:
                length = max(length, len(wind))
                while s[r] in wind:
                    l+=1
                    wind = s[l:r]
        length = max(length, len(wind))
        return length
