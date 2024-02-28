class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addword(self,string):
        cur = self.root

        for strs in string:
            if strs not in cur.children:
                cur.children[strs] = TrieNode()

            cur = cur.children[strs]

        cur.is_end = True

class Solution:
    def longestWord(self, words: list[str]) -> str:
        words.sort()

        wordsTrie = Trie()

        for word in words:
            wordsTrie.addword(word)

        ans = ""

        for word in words:
            cur = wordsTrie.root
            flag = True
            for w in word:
                cur = cur.children[w]

                if not cur.is_end:
                    flag = False
                    break
            
            if flag and len(ans) < len(word):
                ans = word

        return ans




        