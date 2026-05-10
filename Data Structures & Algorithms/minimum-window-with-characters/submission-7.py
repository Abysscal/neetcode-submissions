class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sDict, tDict = {}, {}
        minSize = float('inf')
        res = [0,0]
        l = 0
        for c in t:
            tDict[c] = tDict.get(c, 0) + 1

        have, need = 0, len(tDict)
        for r in range(len(s)):
            c = s[r]
            sDict[c] = sDict.get(c,0) + 1

            if c in tDict and sDict[c] == tDict[c]:
                have += 1

            while have == need:
                if (r-l+1) < minSize:
                    minSize = r-l+1
                    res = l,r
                sDict[s[l]] -= 1
                if s[l] in tDict and sDict[s[l]] < tDict[s[l]]:
                    have -= 1
                l+=1
        l,r = res
        return s[l:r+1] if minSize != float('inf') else ""