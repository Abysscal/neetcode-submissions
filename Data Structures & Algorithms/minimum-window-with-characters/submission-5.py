class Solution:
    def minWindow(self, s: str, t: str) -> str:
        thash, shash = {}, {}

        for i in t:
            thash[i] = 1+thash.get(i,0)

        l = 0
        minSize = float('inf')
        res = [0,0]
        have, need = 0, len(thash)

        for r in range(len(s)):
            shash[s[r]] = 1+shash.get(s[r],0)
            if s[r] in thash and shash[s[r]] == thash[s[r]]:
                have += 1

            while have == need:
                if (r-l+1) < minSize:
                    minSize = r-l+1
                    res[0], res[1] = l,r

                shash[s[l]] -= 1
                if s[l] in thash and shash[s[l]] < thash[s[l]]:
                    have -= 1
                l += 1

        return s[res[0]:res[1]+1] if minSize != float('inf') else ""


