class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tdict = {}
        sdict = {}
        minsize = float('inf')
        res = [0,0]

        for c in t:
            tdict[c] = tdict.get(c,0) + 1
        have, need = 0, len(tdict)
        l=0
        for r in range(len(s)):
            c = s[r]
            sdict[c] = sdict.get(c, 0) + 1
            if c in tdict and sdict[c] == tdict[c]:
                have += 1
            while have == need:
                if (r-l+1) < minsize:
                    minsize = r-l+1
                    res = l,r

                sdict[s[l]] -= 1
                if s[l] in tdict and sdict[s[l]] < tdict[s[l]]:
                    have -= 1

                l+=1

        return s[res[0]:res[1]+1] if minsize != float('inf') else ""