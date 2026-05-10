class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # AOUZYX
        tdict, sdict = {},{}
        minSize = float('inf')
        res = [0,0]
        have,need = 0,0
        l=0

        for c in t:
            tdict[c] = tdict.get(c, 0) + 1
        need = len(tdict)

        for r in range(len(s)):
            sdict[s[r]] = sdict.get(s[r], 0) + 1
            
            if s[r] in tdict and sdict[s[r]] == tdict[s[r]]:
                have += 1
        
            while have == need:
                if (r-l+1) < minSize:
                    minSize =  r-l+1
                    res = [l,r]
                sdict[s[l]] -=1
                if s[l] in tdict and sdict[s[l]] < tdict[s[l]]:
                    have -= 1
                l+=1

        return s[res[0]:res[1]+1] if minSize != float('inf') else ""


