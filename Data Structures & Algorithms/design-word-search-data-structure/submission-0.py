class WordDictionary:
    def __init__(self):
        self.children = [None] * 26
        self.wordEnd = False

    def addWord(self, word: str) -> None: 
        curr = self
        for c in word:
            index = ord(c) - ord('a')

            if curr.children[index] is None:
                newNode = WordDictionary()
                curr.children[index] = newNode

            curr = curr.children[index]
        
        curr.wordEnd = True


    def search(self, word: str) -> bool:
        def dfs(j, trie):
            curr = trie
            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    for child in curr.children:
                        if child is not None:
                            if dfs(i+1, child):
                                return True
                    return False
                else:            
                    index = ord(c) - ord('a')
                    if curr.children[index] is not None:
                        curr = curr.children[index]
                    else:
                        return False
                    
            return curr.wordEnd
            
        return dfs(0, self)