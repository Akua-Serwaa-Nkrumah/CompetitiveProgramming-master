class Node:
    def __init__(self):
        self.children =  {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root

        for w in word:
            if w not in cur.children:
                cur.children[w] = Node()

            cur = cur.children[w]

        cur.is_end = True

    def search(self, word: str) -> bool:

        def helper(word,cur = self.root):
            for i in range(len(word)):
                if word[i] == ".":
                    seen = False
                    for c in cur.children:
                        seen = seen or helper(word[i+1:],cur.children[c])
                    return seen
                if word[i] not in cur.children :
                    return False
                cur = cur.children[word[i]]
            return cur.is_end
            
        return helper(word) 


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)