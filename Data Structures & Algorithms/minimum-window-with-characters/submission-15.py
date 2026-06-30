class Solution:
    def minWindow(self, s: str, t: str) -> str:
        have, need = 0, len(set(t))
        tCount = {}
        freq = {}
        l = 0
        res = [0, 0]
        resLen = float('inf')
        

        # init freq
        for c in t:
            tCount[c] = tCount.get(c, 0) + 1

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1

            if s[r] in t and freq[s[r]] == tCount[s[r]]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r + 1]
                    resLen = r - l + 1
                    if resLen == len(t):
                        return s[res[0]:res[1]]

                freq[s[l]] -= 1
                if s[l] in t and freq[s[l]] < tCount[s[l]]:
                    have -= 1
                l += 1

        return s[res[0]:res[1]] if resLen != float('inf') else ''