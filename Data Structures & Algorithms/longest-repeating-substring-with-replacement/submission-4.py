class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        counter = {}
        largest = 0
        maxf= 0

        for r in range(len(s)):
            counter[s[r]] = 1 + counter.get(s[r], 0)
            maxf = max(counter.values())
            # length of sliding window - max frequency in the counter = # of chars left to transform
            while (r-l+1) - maxf > k:
                counter[s[l]] -= 1
                l+=1 
            largest = max((r-l+1, largest))
        return largest


            
