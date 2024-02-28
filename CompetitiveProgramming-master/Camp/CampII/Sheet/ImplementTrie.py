class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()

            cur = cur.children[w]

        cur.is_end = True
        

    def search(self, word: str) -> bool:
        cur = self.root

        for letter in word:
            if letter not in cur.children:
                return False

            cur = cur.children[letter]
            
        return cur.is_end

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for letter in prefix:
            if letter not in cur.children:
                return False

            cur = cur.children[letter]

        return True
        
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)