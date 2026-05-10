class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        sdict = {}
        l = 0
        res =0

        for r in range(len(s)):
            sdict[s[r]] = sdict.get(s[r], 0)+1
            while (r-l+1) - max(sdict.values()) > k:
                sdict[s[l]] -= 1
                l+=1
            res = max(res, r-l+1)
        return res