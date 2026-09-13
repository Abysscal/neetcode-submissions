class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        hashmap = {}
        l,r = 0,0
        
        while r < len(s):
            if s[r] in hashmap and hashmap[s[r]] >= l:
                l = hashmap[s[r]] + 1
            
            hashmap[s[r]] = r
            res = max(res, (r-l+1))
            r += 1
        return res

