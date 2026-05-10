class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        maxcount = {}
        maxf = 0
        maxsize = 0

        for r in range(len(s)):
            maxcount[s[r]] = maxcount.get(s[r],0) + 1
            maxf = max(maxcount.values())

            # diff = totalSize - maxF
            if (r-l+1) -maxf > k:
                maxcount[s[l]] -=1
                l+=1
            
            maxsize = max(maxsize, (r-l+1))

        return maxsize


            
