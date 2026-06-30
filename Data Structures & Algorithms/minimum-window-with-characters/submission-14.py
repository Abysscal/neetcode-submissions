class Solution:
    def minWindow(self, s: str, t: str) -> str:
        uniqueCount = 0
        tCount = {}
        freq = {}
        l = 0
        finalRes = [0,0]
        res = float('inf')

        # init freq
        for c in t:
            tCount[c] = tCount.get(c, 0) + 1

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r],0) + 1

            if s[r] in t and freq[s[r]] == tCount[s[r]]:
                uniqueCount += 1

            while uniqueCount == len(set(t)):
                if s[l] in t and freq[s[l]] == tCount[s[l]]:
                    uniqueCount -= 1
                    if res > (r-l+1):
                        finalRes = [l,r+1]
                        res = r-l+1
                freq[s[l]] -= 1
                l += 1

        return s[finalRes[0]:finalRes[1]] if res != float('inf') else ''