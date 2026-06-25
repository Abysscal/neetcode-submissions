class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freq = {}
        totalSize = 0
        res = 0

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r],0) + 1
            totalSize += 1

            while totalSize - max(freq.values()) > k:
                freq[s[l]] -= 1
                totalSize -= 1
                l+= 1
            res = max(totalSize, res)

        return res