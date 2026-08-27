class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:[] for w in words for c in w}
        indeg = {c:0 for c in adj}


        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            minLen = min(len(w1), len(w2))

            if w1[:minLen] == w2[:minLen] and len(w1) > len(w2):
                return ""

            for j in range(minLen):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].append(w2[j])
                        indeg[w2[j]] += 1
                    break

        q = deque()

        for deg in indeg:
            if indeg[deg] == 0:
                q.append(deg)

        res = []
        while q:
            c = q.popleft()
            res.append(c)

            for nei in adj[c]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)

        return "".join(res) if len(res) == len(adj) else ""


