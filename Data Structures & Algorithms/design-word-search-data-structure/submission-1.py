class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            i = ord(c) - ord('a')
            if cur.children[i] == None:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
        cur.isEndOfWord = True

    def search(self, word: str) -> bool:
        def dfs(j, trie):
            cur = trie
            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    for child in cur.children:
                        if child is not None:
                            if dfs(i+1, child):
                                return True
                    return False
                else:
                    i = ord(c) - ord('a')
                    if cur.children[i] == None:
                        return False
                    cur = cur.children[i]
            return cur.isEndOfWord
        return dfs(0, self.root)