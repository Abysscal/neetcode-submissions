class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash = set()
        maxsize = 0
        l= 0

        for r in range(len(s)):
            if s[r] not in hash:
                hash.add(s[r])
            else:
                while s[r] in hash:
                    hash.remove(s[l])
                    l+=1
                hash.add(s[r])
            maxsize = max(maxsize, r-l+1)
        return maxsize