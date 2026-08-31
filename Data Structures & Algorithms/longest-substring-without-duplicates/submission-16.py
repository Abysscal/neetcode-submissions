class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hold = set()
        l = 0
        long = 0

        for r in range(len(s)):
            while s[r] in hold:
                hold.remove(s[l])
                l+=1
            hold.add(s[r])
            long = max(long, r-l+1)
        return long
                