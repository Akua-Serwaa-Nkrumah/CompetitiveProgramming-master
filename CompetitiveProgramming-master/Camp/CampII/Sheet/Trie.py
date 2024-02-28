class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]

class Trie:
    def __init__(self):
        self.root = TrieNode()

# Insert Function in a Trie
    def insert(self, word: str) -> None:
        
        node = self.root

        for w in word:
            if node.children[ord(w)-97] == None:
                node.children[ord(w)-97] = TrieNode()

            node = node.children[ord(w)-97]

        node.is_end = True

# Search Word
    def searchWord(self,word:str) -> bool:
        node = self.root
        for w in word:
            if not node.children[ord(w)-97]:
                return False
            
            node = node.children[ord(w)-97]

        return node.is_end 

# Search Prefix
    def searchPrefix(self,prefix:str) -> bool:
        node = self.root

        for l in prefix:
            if not node.children[ord(l)-97]:
                return False
            
            node = node.children[ord(l)-97]

        return True
    
# Search (Word & Prefix)
    def search(self, word:str) -> bool:
        node = self.root
        for w in word:
            return self.searchPrefix(word) and node.is_end
