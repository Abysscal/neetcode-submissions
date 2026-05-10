class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0, 0
        counter = {}
        result = 0


        for r in range(len(s)):
            # AAABB , k = 1
            # size of window - maximum occuring char(A) = number remaining char to swap
            counter[s[r]] = counter.get(s[r], 0) + 1
            while (r-l+1) - max(counter.values()) > k:
                counter[s[l]] -=1
                l+= 1
            result = max(r-l+1, result)

        return result