class Solution:
    def minWindow(self, s: str, t: str) -> str:
        have, need = 0, len(set(t))
        smap, tmap = {}, {}
        size=float('inf')
        res = [0,0]
        l = 0

        for c in t:
            tmap[c] = tmap.get(c,0) + 1
            
        for r in range(len(s)):
            c = s[r]
            smap[c] = smap.get(c,0) + 1

            if c in tmap and smap[c] == tmap[c]:
                have += 1
            
            while have == need:
                if (r-l+1) < size:
                    size = r-l+1
                    res = [l,r]
                
                lchar = s[l]
                smap[lchar] -= 1
                if lchar in tmap and smap[lchar] < tmap[lchar]:
                    have-=1
                l+=1
        return s[res[0]:res[1]+1] if size != float('inf') else ""
                