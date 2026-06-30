class Solution:
    def minWindow(self, s: str, t: str) -> str:
        have, need = 0, len(set(t))
        tmap = {}
        freq = {}
        reslen = float('inf')
        res = [-1, -1]


        for c in t:
            tmap[c] = tmap.get(c, 0) + 1

        l=0
        for r in range(len(s)):
            c = s[r]
            freq[c] = freq.get(c, 0) + 1

            if c in t and freq[c] == tmap[c]:
                have += 1

            while have == need:
                if (r-l+1) < reslen:
                    res = [l,r+1]
                    reslen = r-l+1

                freq[s[l]] -= 1
                if s[l] in t and freq[s[l]] < tmap[s[l]]:
                    have -= 1
                l+= 1

        return s[res[0]:res[1]] if reslen != float('inf') else ""