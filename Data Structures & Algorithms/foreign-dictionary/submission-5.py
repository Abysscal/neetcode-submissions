class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:set() for w in words for c in w}
        indeg = {c:0 for c in adj}

        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            minlen = min(len(w1), len(w2))

            if w1[:minlen] == w2[:minlen] and len(w1) > len(w2):
                return ""
            
            for j in range(len(words[i])):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indeg[w2[j]] += 1
                    break
        
        q = deque([])
        
        for i in indeg:
            if indeg[i] == 0:
                q.append(i)

        res = []
        while q:
            node = q.popleft()
            res.append(node)

            for nei in adj[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
            
        return "".join(res) if len(res) == len(adj) else ""
            